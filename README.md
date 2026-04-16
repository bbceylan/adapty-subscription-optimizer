# Adapty Subscription Optimizer

Analyze Adapty exports, paywalls, pricing, and churn signals, then turn them into concrete product and implementation decisions.

This skill is built for agents working with subscription apps. It can use a fresh Adapty export when you have one, but it also works without external imports by using the bundled benchmark and interpretation markdown files included in this repo.

## Example prompts

- Analyze this Adapty export and tell me what is actually broken in my funnel.
- Review my onboarding paywall and tell me whether pricing or timing is the real problem.
- Compare this app's monetization setup against the bundled Adapty benchmarks.
- I updated the benchmark report, use the newest reference material and reassess my paywall strategy.
- Look at this app repo and tell me what to change in the paywall, packages, or analytics.
- Turn these Adapty findings into concrete implementation tasks for the app.

## Who is this for?

- developers shipping subscription apps
- indie builders trying to improve conversion or retention
- product engineers working on onboarding and paywalls
- growth-minded app teams that want sharper analysis than generic monetization advice
- agents that need bundled benchmark context instead of depending on live external research every time

## What is included

- `SKILL.md` for the workflow and trigger instructions
- `references/` for benchmark facts, summaries, app patterns, and output structure
- `scripts/analyze_adapty_export.py` for quick export inspection

## Default behavior

The skill is designed to work in two modes:

1. **Fresh-export mode**
   - Use a new Adapty CSV or JSON export if one is provided.

2. **Bundled-reference mode**
   - If no fresh export is provided, the skill should still work using the bundled markdown references in this repo.
   - This means users can install and use it immediately without importing extra files first.

## Install

```bash
npx skills add https://github.com/bbceylan/adapty-subscription-optimizer --skill adapty-subscription-optimizer
```
