---
name: adapty-subscription-optimizer
description: Analyze Adapty subscription reports, exports, paywalls, products, experiments, and renewal/churn signals, then identify what to improve and help implement the fixes in an app codebase. Use when a user asks to review Adapty performance, inspect subscription funnels, diagnose weak conversion or retention, improve pricing/package strategy, refine paywall timing/copy/layout, or turn Adapty findings into concrete product, analytics, and code changes.
---

# Adapty Subscription Optimizer

Review Adapty data, find the highest-leverage subscription improvements, and convert findings into concrete implementation work in the target app.

## Quick start

1. Identify what inputs are available:
   - Adapty CSV/JSON export
   - dashboard screenshots
   - manually pasted metrics
   - app repo with paywall/subscription code
   - bundled benchmark context from `references/adapty-benchmark-facts.md`
2. Read `references/adapty-benchmark-facts.md` first. Treat it as the strict benchmark source of truth.
3. Use `references/adapty-benchmarks-2026-summary.md` as the default readable benchmark companion.
4. Use `references/adapty-benchmarks-2026.md` only for backup provenance.
5. If the user does not provide a fresh export, still proceed using the bundled benchmark references and whatever app/paywall context is available. Do not block on an external import when the request is strategy, review, or improvement planning.
6. Summarize the available app data first, then diagnose the bottleneck.
7. Read `references/app-patterns.md` when the target app is Topik, Leaf, or MyCloset.
8. Read `references/onboarding-paywall-interpretation.md` when the user wants actionable onboarding/paywall strategy.
9. Use `references/output-template.md` for the final response shape.
10. Read `references/implementation-maps.md` before making repo changes.
11. Prioritize the top 1-3 improvements, not an unfocused laundry list.
12. If the user wants changes made, inspect the repo and implement the most justified fixes.

## Workflow

### 1. Normalize the input

This skill should work in two modes:

- **Bundled-reference mode:** default fallback when no fresh Adapty export is provided. Use the bundled markdown references in `references/` and whatever app, screenshot, or repo context is available.
- **Fresh-export mode:** when the user provides a new Adapty CSV or JSON export, use it as the primary performance input.

If the user provides a CSV or JSON export, run:

```bash
python3 /Users/berkerceylan/.agents/skills/adapty-subscription-optimizer/scripts/analyze_adapty_export.py <export-file>
```

Use the script for a quick structural summary only. Do not overstate precision. The script is meant to accelerate inspection, not replace judgment.

If the user does not provide a fresh export, do not ask for one unless it is genuinely required for the requested precision level. The bundled benchmark markdown files are part of the skill and should be enough for baseline guidance, diagnosis framing, and improvement recommendations.

If the user provides screenshots instead of exports, inspect them directly and extract:
- products/packages
- paywall names
- conversion metrics
- trial and renewal signals
- platform/country splits

If the metrics are incomplete, say what is missing and continue with the strongest available read. Default to a useful answer, not a blocked answer.

### 2. Diagnose the main problem

Use `references/improvement-checklist.md` after the initial summary.
Read `references/adapty-benchmark-facts.md` before making any benchmark-backed recommendation.
Read `references/adapty-benchmarks-2026-summary.md` only for convenience.
Read `references/adapty-benchmarks-2026.md` only when you need backup provenance.
Read `references/app-patterns.md` before making app-specific recommendations for Topik, Leaf, or MyCloset.
Read `references/onboarding-paywall-interpretation.md` when turning PDF facts into strategy.

Classify the dominant issue into one or more buckets:
- weak paywall conversion
- weak trial start rate
- weak trial-to-paid conversion
- weak renewal / high churn
- pricing/package confusion
- timing / placement problem
- analytics visibility gap
- implementation mismatch between UI copy and actual product setup

Avoid generic advice. Tie every recommendation to an observed metric, a visible UX issue, or a clear instrumentation gap.

### 3. Produce recommendations in priority order

Default output structure lives in `references/output-template.md`.
Use it unless the user requests a different format.

For each recommendation, explain:
- why it matters
- expected impact area, conversion, retention, clarity, or trust
- whether it is a copy, UI, pricing, offer, trigger, or analytics change

### 4. Map findings to implementation

When the user wants changes made, inspect the target repo and map the recommendation to actual files.

Use `references/implementation-maps.md` before changing code.
Typical implementation targets include:
- paywall view copy/layout
- default package selection
- onboarding gating logic
- feature-gate timing
- analytics event tracking
- restore / terms / privacy links
- StoreKit / RevenueCat / Adapty product wiring

When implementing:
- prefer the smallest high-confidence change set first
- keep pricing/product IDs aligned with the store configuration
- verify trial/billing copy exactly matches real purchase behavior
- build or test after edits when feasible

### 5. Call out risks clearly

Escalate or warn when you see:
- misleading price or trial copy
- paywall math that is confusing or false
- missing restore, privacy, or terms links
- product IDs or packages that do not match the UI
- analytics events too weak to support confident recommendations
- a recommendation that needs store-console changes, not just code changes

## Working style

- Be sharp and specific.
- Prefer 1-3 strong recommendations over 15 shallow ones.
- Distinguish evidence from hypothesis.
- Treat `references/adapty-benchmark-facts.md` as the strict benchmark source of truth for this skill.
- Do not present non-PDF advice as if it came from the PDF.
- If you infer onboarding or paywall strategy from the PDF facts, label it as interpretation.
- If app data conflicts with benchmark assumptions, say so plainly and prioritize app data.
- If data is weak, say so plainly.
- If implementation is requested, do the repo work instead of stopping at analysis.

## Resources

### scripts/
- `analyze_adapty_export.py` - export analyzer for CSV/JSON files with detected funnel, revenue, paywall, product, country, and platform summaries

### references/
- `adapty-benchmark-facts.md` - strict PDF-only benchmark facts that the skill should read first
- `adapty-benchmarks-2026-summary.md` - readable companion summary of the PDF facts
- `adapty-benchmarks-2026.md` - backup benchmark detail and provenance file
- `improvement-checklist.md` - diagnostic checklist for funnel, pricing, paywall, and retention review
- `app-patterns.md` - app-specific interpretation rules for Topik, Leaf, and MyCloset
- `onboarding-paywall-interpretation.md` - clearly labeled strategy layer that converts PDF facts into actionable hypotheses
- `output-template.md` - standard answer structure for analysis output
- `implementation-maps.md` - app-specific code surface map for Topik, MyCloset, and Leaf
