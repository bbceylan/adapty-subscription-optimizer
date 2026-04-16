# Adapty Subscription Optimizer

A public Agent Skill for analyzing Adapty subscription performance and turning weak monetization signals into concrete product, paywall, pricing, and implementation improvements.

## What this skill does

This skill helps an AI agent:

- analyze Adapty exports and performance snapshots
- inspect paywall conversion, trial start, renewal, and churn patterns
- compare results against benchmark guidance
- identify the main monetization bottleneck
- recommend the highest-leverage improvements
- translate findings into real product or code changes

It is especially useful when you want more than a generic "improve your paywall" answer and need a structured diagnosis tied to actual data.

## Best use cases

Use this skill when you want an agent to:

- review an Adapty CSV or JSON export
- diagnose low paywall conversion
- understand whether pricing or UX is the real issue
- improve onboarding paywall timing and messaging
- compare multiple products or packages
- turn monetization findings into implementation work in an app repo

## Included resources

- `SKILL.md` — core workflow and usage instructions
- `references/` — benchmark notes, app patterns, interpretation guides, and output templates
- `scripts/analyze_adapty_export.py` — helper script for summarizing Adapty export structure

## Install

With the skills CLI:

```bash
npx skills add https://github.com/bbceylan/adapty-subscription-optimizer --skill adapty-subscription-optimizer
```

## Notes

- This repo is the install source for the skill.
- The main benchmark logic in this version is tailored around the bundled reference material.
- The skill was created to help with real onboarding, paywall, and subscription optimization work across apps like Topik, Leaf, and MyCloset.
