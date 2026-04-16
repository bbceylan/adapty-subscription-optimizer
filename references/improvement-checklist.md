# Subscription Improvement Checklist

Use this checklist after reviewing a subscription report, dashboard screenshot, or manually pasted metrics.

## 1. Funnel health

Check these stages if data is available:
- paywall shown
- trial started
- purchase started
- purchase completed
- renewal
- churn, cancellation, or refund

Questions to answer:
- Where is the biggest drop-off?
- Is the drop-off consistent across paywalls, placements, countries, products, or platforms?
- Are some paywalls getting traffic but not converting?
- Is trial start healthy but paid conversion weak?
- Is initial conversion healthy but retention poor?

## 2. Offer structure

Look for:
- too many plans
- confusing weekly vs annual framing
- weak default selection
- poor annual anchoring
- missing lifetime or introductory offer testing, if relevant
- trial offer mismatch between copy and product setup

Common improvements:
- reduce visible choices
- emphasize annual value
- improve savings explanation
- align copy with actual billing period and trial rules
- default to the best strategic plan, not the cheapest one

## 3. Paywall messaging

Review:
- headline clarity
- benefit specificity
- proof or trust elements
- CTA clarity
- price framing
- restore, terms, or privacy presence

Common improvements:
- make outcome clearer
- replace generic feature lists with concrete value
- reduce visual clutter
- make the free-vs-paid boundary easier to understand
- clarify whether purchase is optional, trial-based, or immediate billing

## 4. Placement and timing

Check whether the paywall is shown:
- too early
- too late
- after low intent actions
- before the user understands value
- at the strongest moment of intent

Common improvements:
- move paywall to a more motivated moment
- add contextual trigger copy
- test onboarding gate vs feature gate vs mixed model
- personalize copy by trigger source if product architecture supports it

## 5. Pricing and geography

Check:
- storefront or country skew
- low-performing territories
- weak PPP alignment
- unusual refund or churn pockets
- platform skew between iOS and Android or web

Common improvements:
- localize pricing presentation
- test alternative default packages in weak markets
- split experiment strategy by territory or platform

## 6. Retention and subscription quality

Check:
- trial-to-paid conversion
- D7 or D30 retention if available
- renewal rate by product
- churn reasons if available
- refund concentration

Interpretation:
- high install-to-trial plus weak trial-to-paid usually means promise too broad or activation too weak
- high conversion plus weak renewal usually means poor retained value or bad expectation setting
- strong annual conversion plus weak retention can still be acceptable if refunds remain low, but review promise realism

## 7. Implementation mapping

Translate findings into one of these buckets:
- copy change
- layout or UI change
- package or product change
- trigger logic change
- experiment setup change
- analytics instrumentation gap
- backend, store, or billing configuration gap

## 8. Implementation output format

When acting on findings, produce:
1. executive summary
2. top 3 problems
3. top 3 experiments
4. required code or configuration changes
5. risks or assumptions
6. next validation steps

## 9. Good experiment examples

- annual preselected vs weekly preselected
- shorter headline vs benefit-first headline
- onboarding paywall vs first-value-moment paywall
- trial framing vs no-trial framing
- social proof variant vs minimal variant
- feature-specific contextual paywall vs generic paywall

## 10. Red flags

Escalate when you see:
- paywall copy misstates billing or trial behavior
- pricing on screen does not match product metadata
- annual plan is mathematically or visually confusing
- missing restore, privacy, or terms links
- purchase success is low despite high paywall taps
- retention collapses after trial end
- analytics events are missing or inconsistent, making diagnosis unreliable
