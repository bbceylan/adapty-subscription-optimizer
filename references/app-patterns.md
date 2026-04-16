# App patterns: Topik, Leaf, MyCloset

Use these app-specific heuristics when the user asks for Adapty/report review plus implementation.

## Leaf

Positioning:
- Leaf is not a subscription-first app.
- Core model is freemium with a one-time unlock, not recurring subscription.
- If the user asks for Adapty work on Leaf, first verify whether the request is actually about subscription analytics, experimental paywalls, or future monetization exploration.

Implications:
- Do not assume recurring pricing experiments are appropriate.
- Focus on unlock conversion, paywall clarity, and free-limit communication.
- If an Adapty request conflicts with the established one-time unlock positioning, flag that tension directly.

Good questions for Leaf:
- Is the free limit understandable?
- Is the one-time unlock value obvious?
- Are paid ads sending users into a weak unlock funnel?
- Are `paywall_shown`, `paywall_dismissed`, and unlock events instrumented cleanly?

## Topik

Positioning:
- Topik uses recurring subscription logic and has both onboarding and activation paywall surfaces.
- Repo contains multiple paywall implementations and trial-centric copy.

Known repo signals:
- onboarding paywall in `Apps/TopikApp/Features/Onboarding/OnboardingFlowView.swift`
- main paywall in `Apps/TopikApp/Features/Subscription/PaywallView.swift`
- activation paywall in `Apps/TopikApp/Features/Subscription/ActivationPaywallFlowView.swift`

Implications:
- Compare performance by paywall entry point, not just by product.
- Watch for inconsistent trial messaging across surfaces.
- Check whether onboarding and activation paywalls use the same plan defaults, badges, and pricing logic.
- Validate that App Review-safe wording still leaves the premium path compelling.

Good questions for Topik:
- Which paywall converts best: onboarding or activation?
- Does trial framing outperform direct premium framing?
- Is yearly sufficiently anchored versus monthly?
- Does the pet-health value prop stay concrete, or drift generic?

## MyCloset

Positioning:
- Freemium subscription app using StoreKit 2.
- Recently changed locally from monthly/yearly to weekly/annual in code and local StoreKit config.

Known repo signals:
- `FitCheck/Services/Subscription/SubscriptionManager.swift`
- `FitCheck/Views/Settings/SubscriptionView.swift`
- `FitCheck/Views/Onboarding/OnboardingContainerView.swift`
- `FitCheck/Resources/Subscription.storekit`
- existing launch/docs may still reference older monthly/yearly assumptions

Implications:
- First verify whether App Store Connect metadata and product setup match local code.
- Treat stale monthly/yearly references as a possible implementation/config mismatch.
- Evaluate whether a hard onboarding paywall is helping or hurting based on available funnel data.
- Weekly pricing can increase front-door conversion but worsen retention quality, so watch downstream churn closely.

Good questions for MyCloset:
- Did hard-gating onboarding improve paid starts, or just suppress activation?
- Is annual framed strongly enough to avoid weekly becoming the default low-LTV sink?
- Are product IDs, copy, and App Store Connect assets aligned?
- Is the app still promising a generous freemium story while gating too early?

## Cross-app interpretation rules

- Always distinguish one-time unlock economics from subscription economics.
- Always separate paywall conversion from subscription quality, churn and renewal.
- Never recommend a pricing/layout experiment without checking whether the repo and store configuration can actually support it.
- If the codebase and store metadata disagree, fix the mismatch before trying to interpret performance.
