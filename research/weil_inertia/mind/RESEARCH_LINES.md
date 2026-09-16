# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Find genuinely intermediate coercivity rather than an RH-equivalent threshold or scalar self-bootstrap

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-035-finite-localization-portfolios-cannot-self-contract-a-scalar-defect`.

WI-304--WI-316 build the source-exact comparison architecture, separate compact negative sectors from positive tail reserve, and show that cofinal vanishing-cap comparison bottoms converge to the global compact-support Weil floor. Consequently a comparison lower bound with `o(1)` threshold loss is already RH-equivalent; vanishing threshold error is not a softer intermediate theorem.

WI-317--WI-318 show that feeding the same scalar lower semibound back through source-exact localization cannot produce a fixed contraction for finite portfolios or for arbitrary adaptive unit-window families with bounded total `H^1`. WI-319 identifies a sharp `t^2/log t` frequency-second-moment threshold for the **high-frequency recurrence witness** used in those proofs: critical-scale resonant localizers can defeat that witness.

WI-320 removes the apparent architectural loophole. The exact source-localization defect has an archimedean coefficient `K(a)>0` on `(0,h_0)`, where `h_0=log rho<log 2` and `rho^3-rho-1=0`. Choose one nonnegative smooth test function whose support diameter is below `h_0`. Its autocorrelation is nonnegative inside that interval and vanishes before the first arithmetic lag `log 2`, so every prime-power term is exactly zero. For every normalized real admissible multiwindow localizer, aggregate autocorrelation satisfies `R(a)<=1`; hence the entire localization defect on this same test vector is nonnegative.

Therefore **no adaptive source-exact multiwindow family can strictly improve a scalar Weil semibound by recycling only that same scalar semibound on the localized pieces**, regardless of portfolio size, regularity budget or carrier frequency. The `t^2/log t` scale remains sharp only for the old recurrence falsifier; paying that complexity no longer counts as an escape from the scalar-bootstrap no-go.

The live route must add information absent from the scalar premise: a genuinely stronger localized arithmetic estimate, vector/matrix/mode/prime-dependent state carried between scales, a different source-exact decomposition whose correction is not trapped by this sign witness, or direct coercivity/inertia control of the exact comparison form. Localization may still organize such information, but it cannot manufacture a stronger scalar constant from itself.

## Track comparison coercivity, compact complexity and information content separately

Endpoint concentration, carrier frequency, compact correction size, cap defect and localization complexity remain useful implementation resources. WI-320 changes their logical role: none is a source of scalar contraction by itself. The decisive new currency is **what extra information is fed into the localized pieces beyond the global scalar floor**. A more complex localizer without stronger input is still the same ineffective channel.

## Keep compact certificate design separate from full Weil positivity

Finite-dimensional trial-subspace optimization remains downstream of source-valid information retention. The capped decomposition can expose bounded positive tail margin and finite negative sectors, but WI-315--WI-316 make its cofinal semantics RH-equivalent and WI-320 blocks autonomous scalar improvement. Any compact certificate that contributes to RH must therefore import a nontrivial sign-producing estimate rather than rely on iterative scalar localization.

## Preserve the signed-density quotient

Even a successful reserve-lifted architecture must survive the exact density-one cancellation of WI-241. Large positive reserve or retained arithmetic mass is not yet the required signed discrepancy theorem; the RH-relevant source variable remains the signed discrepancy after universal prime main density and pole cancellation.
