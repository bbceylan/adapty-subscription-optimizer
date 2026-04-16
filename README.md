# Subscription Optimizer

A skill for turning bundled subscription benchmarks and product data into concrete onboarding, paywall, pricing, and retention decisions.

Use it to review onboarding, paywalls, pricing, packages, trial flow, churn risk, and subscription UX in mobile apps, web apps, SaaS products, or any other product with a subscription business model.

## Example prompts

- Analyze this subscription report and tell me what is actually broken in the funnel.
- Use the bundled benchmark material and review my onboarding and paywall strategy.
- Compare this product's subscription setup against the included benchmark references.
- Look at this onboarding flow and tell me whether the problem is pricing, packaging, timing, or category fit.
- Review this repo and tell me what to change in the subscription flow, paywall, or analytics.
- I updated the bundled benchmark markdown. Reassess the strategy using the newest benchmark material.
- Apply the benchmark learnings in this repo to a web subscription product, not a mobile app.

## Who is this for?

- developers shipping subscription products
- web engineers building billing or paywall flows
- app developers working on onboarding and monetization
- indie makers who want sharper analysis than generic growth advice
- product and growth teams that want benchmark-backed recommendations without live research every time

## What is included

- `SKILL.md` for workflow and trigger instructions
- `references/` for benchmark facts, summaries, onboarding and paywall playbooks, interpretation rules, and output structure

## How it works

This skill is designed to work without helper scripts.

It supports two practical modes:

1. **Bundled-reference mode**
   - Works out of the box using the markdown files included in this repo.
   - Good for strategy, audits, and improvement planning even when no fresh export is provided.

2. **Fresh-data mode**
   - If you provide newer subscription metrics, screenshots, or copied report values, the skill uses those as the primary input.

The bundled benchmark markdown is the default baseline. Updating those markdown files is enough to update the skill's benchmark context.

## Install

```bash
npx skills add https://github.com/bbceylan/subscription-optimizer --skill subscription-optimizer
```
