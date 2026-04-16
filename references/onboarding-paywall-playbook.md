# Onboarding and Paywall Playbook

Use this file as the main practical reference when the user wants an LLM to improve onboarding and paywall strategy.

This file is intentionally split into two layers:
- **Benchmark-backed facts** grounded in the bundled benchmark source files
- **Interpretation** that turns those facts into decision rules and test ideas

Never present interpretation as if it were a direct benchmark fact.

## 1. Benchmark-backed facts worth carrying into strategy

These are the strongest reusable facts extracted from the benchmark report:

### Plan mix and LTV
- Weekly plans with trials have the highest reported 12-month LTV in the report.
- Weekly plans grew from 43.3% of app revenue two years ago to 55.5%.
- Adding a trial to weekly lifts one-year LTV from $7.40 to $54.50, which the report describes as a 636% increase.

### Trial fit is category-specific
Trials improve annual-subscription LTV in:
- Utilities
- Health & Fitness
- Education

Direct buyers are worth more in:
- Productivity
- Lifestyle
- Entertainment
- Graphics & Design

Additional benchmark details:
- Productivity direct buyers: $56.95
- Productivity trial users: $49.13
- Lifestyle trial users end up 21% less valuable than direct buyers

### Geography and price tolerance
- Each of the top three European countries in the report outperforms the US in median LTV.
- Top LATAM countries are 35% lower than top European ones.
- European prices can run up to 40% higher than North America in some segments.
- In most categories, North American install LTV is roughly 2x the global average.

### Category-level monetization context
Median one-year install LTV:
- Health & Fitness: $1.21
- Productivity: $1.10
- Utilities: $1.09
- Education: $1.06
- Photo & Video: $0.82
- Graphics & Design: $0.78
- Lifestyle: $0.70
- Entertainment: $0.59

### Utilities signal
- Utilities lead all categories in long-term LTV.
- Typical first-year utility LTV in the report is $68.90.
- Trials must be present for that result.
- Utilities also lead in retention.

### Market structure
- Top 10% of apps earn 95% of all revenue.
- This concentration grew from 92.7% in 2023.
- Newer apps already earn roughly 25% less at the median than older cohorts.
- Among new apps with at least some revenue, 57.7% earn only $1 to $1,000 per year.

## 2. What these facts mean for onboarding strategy

### Hard onboarding paywall is not a default
Interpretation:
- Do not justify a hard onboarding paywall just because weekly plus trial benchmarks well globally.
- Hard gating makes more sense when user intent is already strong, the value proposition is obvious before first use, and the product behaves like a recurring utility or strong subscription-first tool.

Hard gating is more defensible when:
- user intent is high at install
- the product solves a recurring, painful problem
- value can be understood before setup is complete
- retention is already strong enough to support aggressive monetization

Hard gating is riskier when:
- the product needs demonstration before value feels real
- habit formation matters more than immediate purchase intent
- the product depends on trust-building first
- activation may collapse if access is restricted too early

### Soft or deferred paywalls are often healthier
Interpretation:
- When value becomes clear only after an action, a deferred paywall is usually safer than an immediate hard gate.
- The best trigger is often the first strong intent moment, not the first screen.

Good paywall trigger moments:
- right after first success
- at the first premium-feature attempt
- when the user hits a meaningful limit
- after one clear exposure to the product's main loop

## 3. What these facts mean for trials

Interpretation:
- Trials are not universal best practice. They are category-sensitive.
- Trial-led flows are more defensible in utility-like, health, and education products than in productivity or lifestyle products.
- A high trial start rate is not enough. Trial-to-paid quality matters.

Use trials more confidently when:
- category fit resembles Utilities, Health & Fitness, or Education
- the user can reach value fast during the trial
- the product has recurring use and strong retained value

Be more skeptical of trials when:
- the product looks more like Productivity, Lifestyle, Entertainment, or Graphics & Design
- user curiosity is high but retained value is less stable
- trial starts are cheap but post-trial conversion is weak

## 4. What these facts mean for plan mix

Interpretation:
- Weekly often acts as a front-door converter.
- Annual often acts as the strategic value anchor.
- The skill should not celebrate weekly wins if they pull in low-quality subscribers with poor renewal.

When weekly and annual both exist:
- test whether weekly is improving top-of-funnel conversion
- test whether annual is clearly framed as the better value choice
- inspect whether weekly harms renewal quality or refund profile
- avoid making annual visually weak if annual is important for long-term economics

## 5. What these facts mean for pricing

Interpretation:
- Do not assume a flat global pricing strategy is good enough.
- European willingness to pay may support stronger pricing than many teams assume.
- Region-level results should influence pricing tests, plan defaults, and paywall framing.

Useful pricing questions:
- Is Europe underpriced because the team copied North America?
- Are weak territories dragging down one global plan strategy?
- Should default plan selection change by region or storefront?
- Is localized price presentation missing where it would help trust and conversion?

## 6. Paywall structure rules an LLM should use

These are interpretation rules, not direct benchmark facts.

Prefer these defaults unless app data argues otherwise:
- show a small number of visible plans, usually two or three at most
- make the strategic plan visually legible, not hidden
- make billing cadence explicit
- make savings framing easy to verify
- lead with concrete outcome, not generic feature soup
- include restore, terms, and privacy links clearly
- make it obvious whether the charge is trial-first or immediate

## 7. What to measure before calling any change a win

A paywall experiment is not a win on tap rate alone.

Check:
- paywall shown
- CTA tap
- purchase started
- purchase completed
- trial started, if relevant
- trial-to-paid conversion
- renewal quality
- refund, cancellation, or churn quality
- activation impact if onboarding timing changed

## 8. Common strategic patterns the skill should recognize

### Pattern A: High trial start, weak paid conversion
Likely meaning:
- promise is too broad
- trial audience quality is weak
- the user reaches curiosity, not conviction
- onboarding sells before value is proven

Typical fixes:
- reduce hype in copy
- delay paywall until stronger intent
- tighten who sees the trial pitch
- improve expectation setting before trial start

### Pattern B: Good conversion, weak renewal
Likely meaning:
- the product over-promises
- value is not retained after purchase
- weekly is converting low-quality subscribers
- trial attracts poor-fit users

Typical fixes:
- revisit plan mix
- reduce misleading framing
- strengthen retained-value loop
- watch renewal by package, not just total paid starts

### Pattern C: Weak paywall conversion, decent activation
Likely meaning:
- users understand the product but not the paid value
- pricing anchor is weak
- copy is too generic
- package presentation is confusing

Typical fixes:
- sharpen outcome-led messaging
- simplify plan count
- improve annual anchor
- move the paywall closer to a stronger intent moment

### Pattern D: Hard onboarding paywall hurts activation
Likely meaning:
- monetization is appearing before belief
- the product needs demonstration first
- category fit is weaker for aggressive upfront gating

Typical fixes:
- switch to soft gate or deferred gate
- add one clear pre-paywall value moment
- gate at feature attempt or usage limit instead of install

## 9. LLM decision rules

When using this skill, an LLM should:
1. read `subscription-benchmark-facts.md` first
2. read `subscription-benchmarks-summary.md` for the broad benchmark picture
3. read this playbook when recommending onboarding or paywall changes
4. separate benchmark facts from interpretation clearly
5. prioritize app data over benchmark assumptions when the two conflict
6. avoid generic growth advice that is not grounded in either the benchmark files or the product evidence

## 10. Recommended output shape

For onboarding or paywall advice, structure recommendations like this:
- benchmark fact
- interpretation for this product
- recommended change or experiment
- success metric
- failure guardrail
