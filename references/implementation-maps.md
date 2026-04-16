# Implementation Maps

Use this file when the user wants actual changes made after analysis.

This file is meant to help map monetization findings into real code surfaces across different product types.

## 1. Mobile app subscription surfaces

Typical code surfaces:
- onboarding flow
- paywall view
- subscription or entitlement manager
- product-loading or package-selection layer
- settings or manage-subscription screen
- analytics event definitions

Typical changes:
- default plan selection
- trial copy consistency
- yearly anchor or badge framing
- onboarding vs activation trigger logic
- restore / terms / privacy visibility
- product ID and package alignment
- analytics event coverage by paywall entry point

## 2. Web app or SaaS subscription surfaces

Typical code surfaces:
- pricing page
- upgrade modal or upgrade route
- checkout session creation
- billing portal integration
- entitlement middleware or access guards
- analytics events around pricing page, checkout, and upgrade prompts

Typical changes:
- pricing table structure
- default billing interval
- annual savings framing
- CTA copy near plan comparison
- upgrade timing after limit hits
- checkout step reduction
- plan metadata alignment between frontend and billing backend

## 3. Freemium gating and feature access

Typical code surfaces:
- feature flags or entitlement checks
- usage limit counters
- gating overlays or limit-reached prompts
- onboarding completion gates
- server responses or local state that expose remaining quota

Typical changes:
- free-tier limit clarity
- paywall timing after a meaningful value moment
- hard-gate vs soft-gate behavior
- clearer explanation of what becomes paid
- consistent premium feature naming across app and store

## 4. Analytics and instrumentation

Typical code surfaces:
- analytics client wrappers
- event enums or event schemas
- paywall impression and dismissal events
- checkout start and purchase completion events
- trial start and renewal quality events
- activation milestones that happen before purchase

Typical changes:
- add paywall entry-point attribution
- separate onboarding paywall and activation paywall metrics
- track selected package before purchase
- track downstream quality after purchase, not just top-of-funnel conversion
- align event names with the actual billing logic and UI states

## 5. Store and billing configuration checks

Before changing UI recommendations into code:
- verify products or plans really exist
- verify product IDs or price IDs match code
- verify trial settings match copy
- verify region pricing assumptions are possible in the billing system
- verify the subscription interval shown in UI matches the real billing interval
- verify checkout and entitlement logic reflect the same plan structure

## Bundled product-specific examples

The skill has been used on products like Topik, MyCloset, and Leaf. Those examples are useful reference points, but they should not override the more general mapping above when the current project is a different kind of subscription product.
