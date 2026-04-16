# Onboarding and Paywall Interpretation Layer

This file is intentionally **not** a PDF-facts file.
It translates the PDF-backed benchmark facts into practical hypotheses and decision rules.
Always separate these recommendations from direct PDF claims.

## How to use this file

When giving advice, split your reasoning into two layers:
1. **PDF-backed fact** from `adapty-benchmark-facts.md`
2. **Interpretation** from this file

Never blur them together.

## Core interpretation rules

### 1. Hard onboarding paywall
Use a hard onboarding paywall only when at least one of these is true:
- the app behaves like a subscription-first utility or recurring-use product
- user intent is already strong at install
- the product promise is easy to understand before first use
- historical app data shows activation is not collapsing

Avoid or question a hard onboarding paywall when:
- the product needs demonstration before value is obvious
- retention depends on habit formation after setup
- the free promise is part of the app's positioning
- app data suggests activation falls faster than monetization improves

### 2. Soft onboarding or deferred paywall
Prefer softer gating when:
- value becomes clearer after first action
- category fit looks weaker for trials or aggressive paywalls
- direct buyer quality is uncertain
- the app has multiple meaningful intent moments

Good deferred moments:
- immediately after first success
- at first premium-feature attempt
- after the user experiences the main loop once

### 3. Weekly versus annual interpretation
If weekly is present:
- treat it as the likely front-door converter
- treat annual as the strategic LTV anchor
- inspect whether weekly is producing low-quality conversions or weak renewal

If annual is present:
- make sure it is understandable and visibly better value
- do not let annual become visually secondary if long-term value depends on it

### 4. Trial use
When trials are used:
- verify that trial wording matches the actual billing behavior
- watch trial-start to paid conversion closely
- watch refund, churn, and early cancellation after trial end

### 5. Paywall structure heuristics
These are implementation heuristics, not PDF facts.

Good defaults to test:
- 2 visible plans, not a crowded menu
- strongest strategic plan visually anchored
- clear restore / terms / privacy links
- benefit-first messaging, not feature soup
- explicit billing cadence and savings framing

### 6. Winning experiment principles
A test should not be called a win on purchase-start rate alone.
Check:
- paywall conversion
- trial start rate
- purchase completion
- renewal quality
- refund/churn quality
- activation impact when paywall appears early

### 7. Interpretation output template
When making recommendations, format them like this:
- PDF fact
- Interpretation
- Recommended test/change
- Success metric
- Failure guardrail
