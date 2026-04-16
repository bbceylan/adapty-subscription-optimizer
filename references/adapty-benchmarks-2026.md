# Adapty Benchmarks 2026

Source of truth for this skill:
- `/Users/berkerceylan/Desktop/In-App Subscription Benchmarks 2026 — Pricing, Сonversion & LTV Data.pdf`
- Workspace copy used during skill development: `/Users/berkerceylan/.openclaw/workspace/adapty-benchmarks-2026.pdf`

This skill should treat the benchmark PDF above as the primary external benchmark source unless the user explicitly overrides it.

## Canonical benchmark takeaways

### Dataset
- Based on 16,000+ apps
- Based on $3B in subscription revenue
- Covers 2025 data
- Primarily App Store, with Google Play comparisons where relevant
- Segmented by region, billing cycle, and trial vs direct acquisition

### LTV and plan mix
- Weekly plans with trials showed the highest benchmarked 12-month LTV overall
- Report headline takeaway: weekly + trial can raise one-year LTV from about $7.40 to $54.50
- Weekly plans increased their share of app revenue from 43.3% two years ago to 55.5%

### Trial guidance
Trials are not universally positive.

Benchmarked guidance from the report:
- Trials boost LTV for annual subscriptions in:
  - Utilities
  - Health & Fitness
  - Education
- Direct buyers are worth more in:
  - Productivity
  - Lifestyle
  - Entertainment
  - Graphics & Design

Interpretation rule:
- Do not recommend a trial by default
- Match the recommendation to category, retention quality, and product behavior

### Install LTV benchmarks
Median one-year install LTV:
- Health & Fitness: $1.21
- Productivity: $1.10
- Utilities: $1.09
- Education: $1.06
- Photo & Video: $0.82
- Graphics & Design: $0.78
- Lifestyle: $0.70
- Entertainment: $0.59

### Geography and pricing
- Europe can support meaningfully higher subscription pricing than North America
- Report takeaway says Europe can run up to ~40% higher than North America in some segments
- Top one-year LTV countries called out include:
  - Switzerland: $28.5
  - Qatar: $27.5
  - Israel: $27.0
  - UK: $23.6
  - Japan: $23.4
  - US: $19.9

Interpretation rule:
- Avoid overly conservative EU pricing
- Consider region-aware pricing and paywall tests when geography data is available

### Market concentration
- Top 10% of apps earn 95% of revenue
- Median newer apps earn materially less than older cohorts

Interpretation rule:
- Strong execution on pricing, paywall timing, and experimentation matters more than generic parity with competitors

## How this should influence recommendations

### For Topik
- Treat Topik as trial-friendly enough to test aggressively, but verify retention before scaling
- Compare onboarding paywall vs activation paywall separately
- Weekly/trial style tests may be worth considering only if lifetime value quality remains healthy

### For MyCloset
- The recent shift to weekly/annual is directionally consistent with this benchmark source
- Hard onboarding paywall should not be assumed correct just because weekly performs well globally
- Validate whether activation loss outweighs monetization gain
- Watch weekly for low-quality conversion and poor renewal outcomes

### For Leaf
- This benchmark source is secondary only
- Leaf is fundamentally a one-time unlock product, so subscription benchmark logic should not dominate recommendations

## Mandatory skill behavior
- When asked for benchmark-backed subscription advice, use this file first
- When app data conflicts with benchmark data, prioritize app data but explain the benchmark contrast
- When data is missing, explicitly say recommendations are benchmark-led rather than app-validated
- Do not cite generic internet subscription advice over this file unless the user asks for broader research
