#!/usr/bin/env python3
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


def load_rows(path: Path):
    suffix = path.suffix.lower()
    if suffix == '.csv':
        with path.open('r', encoding='utf-8-sig', newline='') as f:
            return list(csv.DictReader(f))
    if suffix == '.json':
        with path.open('r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            for key in ('rows', 'data', 'items', 'results'):
                if isinstance(data.get(key), list):
                    return data[key]
            return [data]
    raise SystemExit(f'Unsupported file type: {path}')


def normalize_key(name: str) -> str:
    return ''.join(ch.lower() if ch.isalnum() else '_' for ch in str(name)).strip('_')


def to_float(value):
    if value is None:
        return None
    text = str(value).strip().replace(',', '')
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def find_field(fieldnames, *candidates):
    normalized = {normalize_key(name): name for name in fieldnames}
    for candidate in candidates:
        if candidate in normalized:
            return normalized[candidate]
    return None


def pick_value(row, keys):
    for key in keys:
        value = row.get(key)
        if value not in (None, ''):
            return value
    return None


def classify_event(value: str):
    text = normalize_key(value)
    if any(k in text for k in ('paywall_view', 'paywall_shown', 'impression', 'shown', 'view')):
        return 'paywall_shown'
    if any(k in text for k in ('trial_start', 'trial_started', 'start_trial')):
        return 'trial_started'
    if any(k in text for k in ('purchase_start', 'checkout_start', 'billing_start')):
        return 'purchase_started'
    if any(k in text for k in ('purchase', 'subscription_started', 'converted', 'paid')):
        return 'purchase_completed'
    if any(k in text for k in ('renew', 'rebill')):
        return 'renewal'
    if any(k in text for k in ('refund', 'cancel', 'churn', 'expiration', 'expired')):
        return 'churn_or_refund'
    return None


def summarize(rows):
    if not rows:
        return {'row_count': 0, 'notes': ['No rows found.']}

    fieldnames = sorted({str(k) for row in rows for k in row.keys()})

    revenue_key = find_field(fieldnames, 'revenue', 'proceeds', 'price_usd', 'usd_revenue', 'amount_usd', 'amount', 'proceeds_usd')
    country_key = find_field(fieldnames, 'country', 'country_code', 'store_country', 'region')
    product_key = find_field(fieldnames, 'product', 'product_id', 'paywall_product', 'variation', 'subscription_product', 'package')
    paywall_key = find_field(fieldnames, 'paywall', 'paywall_name', 'paywall_id', 'placement', 'audience')
    event_key = find_field(fieldnames, 'event', 'event_name', 'metric', 'conversion_step', 'state', 'action')
    platform_key = find_field(fieldnames, 'platform', 'store', 'os')

    revenue_total = 0.0
    revenue_rows = 0
    by_country = Counter()
    by_product = Counter()
    by_paywall = Counter()
    by_event = Counter()
    by_platform = Counter()
    funnel = Counter()
    paywall_revenue = defaultdict(float)
    product_revenue = defaultdict(float)
    country_revenue = defaultdict(float)

    for row in rows:
        revenue = to_float(row.get(revenue_key)) if revenue_key else None
        country = row.get(country_key) if country_key else None
        product = row.get(product_key) if product_key else None
        paywall = row.get(paywall_key) if paywall_key else None
        platform = row.get(platform_key) if platform_key else None
        event = row.get(event_key) if event_key else None

        if revenue is not None:
            revenue_total += revenue
            revenue_rows += 1
            if paywall:
                paywall_revenue[str(paywall)] += revenue
            if product:
                product_revenue[str(product)] += revenue
            if country:
                country_revenue[str(country)] += revenue

        if country:
            by_country[str(country)] += 1
        if product:
            by_product[str(product)] += 1
        if paywall:
            by_paywall[str(paywall)] += 1
        if platform:
            by_platform[str(platform)] += 1
        if event:
            by_event[str(event)] += 1
            stage = classify_event(str(event))
            if stage:
                funnel[stage] += 1

    notes = []
    if revenue_key:
        notes.append(f'Revenue-like field detected: {revenue_key}')
    if paywall_key:
        notes.append(f'Paywall field detected: {paywall_key}')
    if product_key:
        notes.append(f'Product field detected: {product_key}')
    if event_key:
        notes.append(f'Event field detected: {event_key}')
    if platform_key:
        notes.append(f'Platform field detected: {platform_key}')

    return {
        'row_count': len(rows),
        'columns': fieldnames,
        'revenue_total': round(revenue_total, 2) if revenue_rows else None,
        'top_countries': by_country.most_common(10),
        'top_products': by_product.most_common(10),
        'top_paywalls': by_paywall.most_common(10),
        'top_events': by_event.most_common(15),
        'top_platforms': by_platform.most_common(10),
        'funnel': dict(funnel),
        'top_paywall_revenue': sorted(((k, round(v, 2)) for k, v in paywall_revenue.items()), key=lambda x: x[1], reverse=True)[:10],
        'top_product_revenue': sorted(((k, round(v, 2)) for k, v in product_revenue.items()), key=lambda x: x[1], reverse=True)[:10],
        'top_country_revenue': sorted(((k, round(v, 2)) for k, v in country_revenue.items()), key=lambda x: x[1], reverse=True)[:10],
        'notes': notes,
    }


def print_section(title, items, money=False):
    if not items:
        return
    print()
    print(f'## {title}')
    for key, value in items:
        if money:
            print(f'- {key}: {value:.2f}' if isinstance(value, float) else f'- {key}: {value}')
        else:
            print(f'- {key}: {value}')


def print_summary(path: Path, summary):
    print(f'# Adapty export summary: {path.name}')
    print()
    print(f'- Rows: {summary["row_count"]}')
    if summary.get('revenue_total') is not None:
        print(f'- Revenue total (raw detected sum): {summary["revenue_total"]}')
    if summary.get('notes'):
        print('- Signals:')
        for note in summary['notes']:
            print(f'  - {note}')

    print_section('Top paywalls by row count', summary.get('top_paywalls'))
    print_section('Top products by row count', summary.get('top_products'))
    print_section('Top countries by row count', summary.get('top_countries'))
    print_section('Top platforms by row count', summary.get('top_platforms'))
    print_section('Top events by row count', summary.get('top_events'))
    print_section('Top paywalls by detected revenue', summary.get('top_paywall_revenue'), money=True)
    print_section('Top products by detected revenue', summary.get('top_product_revenue'), money=True)
    print_section('Top countries by detected revenue', summary.get('top_country_revenue'), money=True)

    if summary.get('funnel'):
        print()
        print('## Detected funnel signals')
        for stage in ['paywall_shown', 'trial_started', 'purchase_started', 'purchase_completed', 'renewal', 'churn_or_refund']:
            if stage in summary['funnel']:
                print(f'- {stage}: {summary["funnel"][stage]}')

    print()
    print('## Recommended analysis steps')
    print('- Compare the strongest and weakest paywalls by both traffic and revenue.')
    print('- Compare weekly, monthly, and annual product quality, not just purchase volume.')
    print('- Check whether trial-heavy flows convert to paid and renew well enough.')
    print('- Check whether geography or platform differences justify separate pricing or paywall strategy.')
    print('- Verify that the UI copy and store configuration still match the active products.')


def main():
    if len(sys.argv) != 2:
        raise SystemExit('Usage: analyze_adapty_export.py <path-to-csv-or-json>')
    path = Path(sys.argv[1]).expanduser()
    if not path.exists():
        raise SystemExit(f'File not found: {path}')
    rows = load_rows(path)
    summary = summarize(rows)
    print_summary(path, summary)


if __name__ == '__main__':
    main()
