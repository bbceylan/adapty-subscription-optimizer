# Implementation Maps

Use this file when the user wants actual changes made after analysis.

## Topik

Likely code surfaces:
- onboarding paywall: `Apps/TopikApp/Features/Onboarding/OnboardingFlowView.swift`
- main paywall: `Apps/TopikApp/Features/Subscription/PaywallView.swift`
- activation paywall: `Apps/TopikApp/Features/Subscription/ActivationPaywallFlowView.swift`
- diagnostics / loaded products visibility: `Apps/TopikApp/Root/TopikRootView.swift`

Typical changes:
- default plan selection
- trial copy consistency
- yearly anchor / badge framing
- onboarding vs activation trigger logic
- restore / terms / privacy visibility
- analytics event coverage by paywall entry point

## MyCloset

Likely code surfaces:
- subscription products and entitlement handling: `FitCheck/Services/Subscription/SubscriptionManager.swift`
- paywall UI: `FitCheck/Views/Settings/SubscriptionView.swift`
- onboarding gate: `FitCheck/Views/Onboarding/OnboardingContainerView.swift`
- local product config: `FitCheck/Resources/Subscription.storekit`

Typical changes:
- weekly vs annual presentation
- featured/default plan logic
- onboarding hard-gate behavior
- trial/billing wording accuracy
- stale product IDs or metadata alignment
- analytics around onboarding paywall conversion and downstream retention

## Leaf

Likely code surfaces:
- paywall/unlock UI: `Leaf/Leaf/Views/PaywallView.swift`
- app/root flow depending on context

Typical changes:
- one-time unlock framing
- free-limit communication
- unlock CTA clarity
- paywall timing after intent moments
- event instrumentation for unlock funnel

## Store and config checks

Before changing UI recommendations into code:
- verify store products/packages really exist
- verify product IDs match code
- verify trial settings match copy
- verify region pricing assumptions are possible in store configuration
