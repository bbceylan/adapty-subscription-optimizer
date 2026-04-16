# Subscription Benchmarks 2026 - Summary

Source benchmark document:
- `/Users/berkerceylan/Desktop/In-App Subscription Benchmarks 2026 — Pricing, Сonversion & LTV Data.pdf`

This is the primary readable benchmark file for the skill.
Use it first for onboarding, pricing, trial, and paywall recommendations.
If deeper provenance is needed, fall back to `subscription-benchmarks-source-notes.md`.

## Report scope

Directly from the document:
- based on **16,000+ apps**
- based on **$3B** in subscription revenue
- analysis covers **2025**
- revenue is **gross, in USD**
- mostly **Apple App Store** data, with Google Play included where store comparisons exist
- segmented by:
  - **region**
  - **billing cycle**: weekly, monthly, annual
  - **acquisition**: trial vs direct
  - in some places, **paywall type** and **country**
- includes lifetime subscriptions where applicable

Covered regions and categories named in the document:
- regions: **US, Europe, LATAM, MEA, APAC**
- categories: **Health & Fitness, Education, Lifestyle, Photo & Video, Productivity, Utilities, Entertainment, Graphics & Design**

## Actual benchmark facts

### 1. Weekly with trials is the strongest broad LTV pattern

The document states:
- **Weekly plans with trials have the highest 12-month LTV**

From the takeaway pages:
- weekly plans made up **43.3%** of app revenue two years ago
- weekly plans now make up **55.5%** of app revenue
- adding a trial to weekly increases one-year LTV from **$7.40** to **$54.50**
- the document describes this as a **636% increase**

Skill interpretation:
- treat weekly + trial as a serious benchmark-backed test idea for subscription-first products
- do not treat it as an automatic default if retention or category fit is weak

### 2. Trials are category-specific, not a universal best practice

The document explicitly argues that “always offer a free trial” is bad advice.

Directly supported by the benchmark:
- trials boost **annual subscription** LTV in:
  - **Utilities**
  - **Health & Fitness**
  - **Education**
- direct buyers are worth more in:
  - **Productivity**
  - **Lifestyle**
  - **Entertainment**
  - **Graphics & Design**

Extra benchmark details:
- in **Productivity**, direct buyers are worth **$56.95** vs **$49.13** for trial users
- in **Lifestyle**, trial users end up **21% less valuable** than direct buyers
- the document says trials are a **quality filter in some categories** and a **churn magnet in others**

Skill interpretation:
- do not recommend a free trial by default
- for onboarding and paywall advice, first ask whether the product behaves more like Utilities, Health, or Education, or more like Productivity or Lifestyle
- if a trial increases front-end conversion but hurts downstream value, treat it as a bad outcome

### 3. Country and regional differences matter a lot

Top one-year LTV countries listed in the benchmark:
- **Switzerland**: **$28.5**
- **Qatar**: **$27.5**
- **Israel**: **$27.0**
- **Iceland**: **$23.9**
- **United Kingdom**: **$23.6**
- **Japan**: **$23.4**
- **Singapore**: **$22.2**
- **UAE**: **$21.8**
- **Australia**: **$21.5**
- **Canada**: **$20.9**
- **United States**: **$19.9**
- **Argentina**: **$17.9**
- **Mexico**: **$17.6**
- **Chile**: **$15.3**

The document also says:
- each of the top three European countries outperforms the US in median LTV
- top LATAM countries are **35% lower** than top European ones

Skill interpretation:
- onboarding and paywall recommendations should not assume one global pricing posture
- if geography is available, prefer geo-aware pricing and paywall strategy
- country-level or region-level performance should be treated as meaningful, not noise

### 4. Europe supports higher pricing than many teams assume

The benchmark takeaway says:
- European prices now run **up to 40% higher** than North American prices in some segments
- this is not just currency movement, it reflects real willingness to pay

Skill interpretation:
- do not default to overly conservative European pricing
- if the product has meaningful EU volume, price sensitivity assumptions should be tested instead of inherited

### 5. Install LTV differs substantially by category

Median one-year install LTV from the benchmark:
- **Health & Fitness**: **$1.21**
- **Productivity**: **$1.10**
- **Utilities**: **$1.09**
- **Education**: **$1.06**
- **Photo & Video**: **$0.82**
- **Graphics & Design**: **$0.78**
- **Lifestyle**: **$0.70**
- **Entertainment**: **$0.59**

The document also states:
- install LTV varies about **2x across categories**
- in most categories, **North American install LTV is roughly 2x the global average**

Skill interpretation:
- category fit should shape onboarding and paywall aggressiveness
- stronger categories can justify more assertive monetization testing
- lower-install-LTV categories need tighter paywall efficiency and stronger downstream value capture

### 6. Utilities plus trials are exceptionally strong

The benchmark takeaway says:
- **Utilities lead all categories in long-term LTV**
- a typical utility user brings in about **$68.90** in the first year
- the catch is that **trials must be present**
- utilities also lead in **retention**

Skill interpretation:
- utility-like products have stronger justification for trial-led onboarding or paywall strategy
- but this should only be used when the product solves a recurring enough problem to sustain retention

### 7. Market concentration is severe

The benchmark says:
- top **10%** of apps now earn **95%** of all revenue
- this increased from **92.7%** in 2023
- newer apps earn roughly **25% less at the median** than older cohorts
- among new apps with at least some revenue, **57.7%** bring in only **$1 to $1,000 per year**

Skill interpretation:
- onboarding, pricing, and paywall execution quality matter a lot
- weak generic paywalls are unlikely to be good enough
- experiment discipline is necessary, not optional

## What this means for onboarding and paywalls

These are still interpretations, but they are grounded in the benchmark above.

### Onboarding
- A hard onboarding paywall should not be justified only because weekly + trial performs well globally.
- Use category fit and product data to decide whether onboarding should be hard-gated, soft-gated, or deferred to a stronger moment of intent.
- Trial-led onboarding is more defensible in products behaving like Utilities, Health & Fitness, or Education.
- Direct-buyer framing may be stronger in products behaving like Productivity or Lifestyle.

### Paywall plan mix
- Weekly deserves explicit consideration because the benchmark shows major revenue and LTV strength there.
- Annual still matters, especially where trials improve annual performance.
- If presenting weekly and annual together, the skill should evaluate whether weekly is the conversion driver, annual is the value anchor, and the lower-commitment option is creating low-quality wins.

### Trial framing
- Trials should be treated as a category-sensitive lever, not default doctrine.
- When trial is recommended, the skill should still ask whether the product has retention behavior strong enough to support it.

### Pricing
- European pricing should not automatically mirror North America.
- If country or region data is available, the skill should recommend localized pricing review instead of flat global assumptions.

## Mandatory reading behavior for the skill

When the skill is used:
1. read this file early
2. use it as a benchmark source of truth for benchmark-backed recommendations
3. if real product data conflicts with these benchmarks, prioritize product data and explain the contrast clearly
4. only use generic internet wisdom when the user explicitly asks for broader research
