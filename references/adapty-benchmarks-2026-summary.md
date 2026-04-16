# Adapty Benchmarks 2026 - PDF-Grounded Summary

Source PDF:
- `/Users/berkerceylan/Desktop/In-App Subscription Benchmarks 2026 — Pricing, Сonversion & LTV Data.pdf`

This is the primary readable benchmark file for the skill.
Use it first for onboarding, pricing, trial, and paywall recommendations.
If deeper provenance is needed, fall back to `adapty-benchmarks-2026.md`.

## Report scope

Directly from the report:
- based on **16,000+ apps**
- based on **$3B** in subscription revenue through Adapty
- analysis covers **2025**
- revenue is **gross, in USD**
- mostly **Apple App Store** data, with Google Play included where store comparisons exist
- segmented by:
  - **region**
  - **billing cycle**: weekly, monthly, annual
  - **acquisition**: trial vs direct
  - in some places, **paywall type** and **country**
- includes lifetime subscriptions where applicable

Covered regions and categories named in the report:
- regions: **US, Europe, LATAM, MEA, APAC**
- categories: **Health & Fitness, Education, Lifestyle, Photo & Video, Productivity, Utilities, Entertainment, Graphics & Design**

## Actual benchmark facts from the PDF

### 1. Weekly with trials is the strongest broad LTV pattern

The report states:
- **Weekly plans with trials have the highest 12-month LTV**

From the report takeaway pages:
- weekly plans made up **43.3%** of app revenue two years ago
- weekly plans now make up **55.5%** of app revenue
- adding a trial to weekly increases one-year LTV from **$7.40** to **$54.50**
- the report describes this as a **636% increase**

Skill interpretation:
- treat weekly + trial as a serious benchmark-backed test idea for subscription-first apps
- do not treat it as an automatic default if app retention or category fit is weak

### 2. Trials are category-specific, not a universal best practice

The report explicitly argues that “always offer a free trial” is bad advice.

Directly supported by the PDF:
- trials boost **annual subscription** LTV in:
  - **Utilities**
  - **Health & Fitness**
  - **Education**
- direct buyers are worth more in:
  - **Productivity**
  - **Lifestyle**
  - **Entertainment**
  - **Graphics & Design**

Extra report details:
- in **Productivity**, direct buyers are worth **$56.95** vs **$49.13** for trial users
- in **Lifestyle**, trial users end up **21% less valuable** than direct buyers
- the report says trials are a **quality filter in some categories** and a **churn magnet in others**

Skill interpretation:
- do not recommend a free trial by default
- for onboarding and paywall advice, first ask whether the app behaves more like Utilities / Health / Education or more like Productivity / Lifestyle
- if a trial increases front-end conversion but hurts downstream value, treat it as a bad outcome

### 3. Country and regional differences matter a lot

Top one-year LTV countries listed in the PDF:
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

The report also says:
- each of the top-3 European countries outperforms the US in median LTV
- top LATAM countries are **35% lower** than top European ones

Skill interpretation:
- onboarding and paywall recommendations should not assume one global pricing posture
- if geography is available, prefer geo-aware pricing and paywall strategy
- country-level or region-level performance should be treated as meaningful, not noise

### 4. Europe supports higher pricing than many teams assume

The report takeaway says:
- European prices now run **up to 40% higher** than North American prices in some segments
- this is not just currency movement, it reflects real willingness to pay

Skill interpretation:
- do not default to overly conservative European pricing
- if the app has meaningful EU volume, price sensitivity assumptions should be tested instead of inherited

### 5. Install LTV differs substantially by category

Median one-year install LTV from the report:
- **Health & Fitness**: **$1.21**
- **Productivity**: **$1.10**
- **Utilities**: **$1.09**
- **Education**: **$1.06**
- **Photo & Video**: **$0.82**
- **Graphics & Design**: **$0.78**
- **Lifestyle**: **$0.70**
- **Entertainment**: **$0.59**

The report also states:
- install LTV varies about **2x across categories**
- in most categories, **North American install LTV is roughly 2x the global average**

Skill interpretation:
- category fit should shape onboarding and paywall aggressiveness
- strong categories can justify more assertive monetization testing
- lower install-LTV categories need tighter paywall efficiency and stronger downstream value capture

### 6. Utilities plus trials are exceptionally strong

The PDF takeaway says:
- **Utilities lead all categories in long-term LTV**
- a typical utility app user brings in about **$68.90** in the first year
- the catch is that **trials must be present**
- utilities also lead in **retention**

Skill interpretation:
- utility-like apps have stronger justification for trial-led onboarding or paywall strategy
- but this should only be used when the product solves a recurring enough problem to sustain retention

### 7. Market concentration is severe

The report says:
- top **10%** of apps now earn **95%** of all revenue
- this increased from **92.7%** in 2023
- newer apps earn roughly **25% less at the median** than apps launched a few years earlier
- among new apps with at least some revenue, **57.7%** bring in only **$1 to $1,000 per year**

Skill interpretation:
- onboarding, pricing, and paywall execution quality matter a lot
- weak generic paywalls are unlikely to be good enough
- experiment discipline is necessary, not optional

## What this means for onboarding and paywalls

These are still interpretations, but they are grounded in the report above.

### Onboarding
- A hard onboarding paywall should not be justified only because weekly + trial performs well globally
- Use category fit and app data to decide whether onboarding should be:
  - hard-gated
  - soft-gated
  - deferred to a stronger moment of intent
- Trial-led onboarding is more defensible in apps behaving like Utilities / Health & Fitness / Education
- Direct-buyer framing may be stronger in apps behaving like Productivity / Lifestyle

### Paywall plan mix
- Weekly deserves explicit consideration because the report shows major revenue and LTV strength there
- Annual still matters, especially where trials improve annual performance
- If presenting weekly and annual together, the skill should evaluate whether:
  - weekly is the conversion driver
  - annual is the value anchor
  - the lower-commitment option is creating low-quality wins

### Trial framing
- Trials should be treated as a category-sensitive lever, not default doctrine
- When trial is recommended, the skill should still ask whether the app has retention behavior strong enough to support it

### Pricing
- European pricing should not automatically mirror North America
- If country or region data is available, the skill should recommend localized pricing review instead of flat global assumptions

## App-specific use

### Topik
- More trial-friendly than Leaf or MyCloset
- Benchmark support exists for serious trial-led testing
- Paywall analysis should compare onboarding and activation separately
- Weekly could be interesting later, but only with careful retention monitoring

### MyCloset
- Weekly/annual direction is benchmark-consistent enough to test
- Hard onboarding paywall should still be validated against activation loss
- If weekly wins conversion but weakens retention quality, do not over-celebrate it

### Leaf
- This report is secondary for Leaf
- Leaf is structurally closer to one-time unlock optimization than recurring-subscription optimization

## Mandatory reading behavior for the skill

When the skill is used:
1. read this file first
2. use it as the benchmark source of truth for benchmark-backed recommendations
3. if real app data conflicts with these benchmarks, prioritize app data and explain the contrast clearly
4. only use generic internet wisdom when the user explicitly asks for broader research
