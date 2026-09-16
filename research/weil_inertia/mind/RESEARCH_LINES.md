# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Find genuinely intermediate coercivity rather than an RH-equivalent threshold or scalar self-bootstrap

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-035-finite-localization-portfolios-cannot-self-contract-a-scalar-defect`.

WI-304--WI-316 build the source-exact comparison architecture, separate compact negative sectors from positive tail reserve, and show that cofinal vanishing-cap comparison bottoms converge to the global compact-support Weil floor. Consequently a comparison lower bound with `o(1)` threshold loss is already RH-equivalent; vanishing threshold error is not a softer intermediate theorem.

WI-317--WI-318 show that feeding the same scalar lower semibound back through source-exact localization cannot produce a fixed contraction for finite portfolios or arbitrary adaptive unit-window families with bounded total `H^1`. WI-319 identifies the sharp `t^2/log t` complexity threshold only for the high-frequency recurrence witness used in those proofs.

WI-320 closes the real-window loophole completely. The exact source-localization defect has an archimedean coefficient `K(a)>0` on `(0,h_0)`, with `h_0=log rho<log2`. One nonnegative smooth test supported inside that interval kills every prime-power lag and has nonnegative autocorrelation. Since every normalized real multiwindow localizer has aggregate autocorrelation `R(a)<=1`, the same test makes the entire localization defect nonnegative for **every** adaptive real localizer.

WI-321 shows this is not an artifact of real windows or scalar presentation dimension. Package any finite complex multiwindow family as a Hilbert-valued window `G`. The exact defect becomes

`Re((1-R_G(a)) h_f(a))`.

On the same short real nonnegative witness, `h_f(a)>=0` and Cauchy--Schwarz gives `Re R_G(a)<=1`, so the defect remains nonnegative for every finite complex channelization and every unitary mixing of its channels. Applying the same scalar semibound componentwise therefore cannot contract the scalar constant either.

The live route must add **genuinely non-scalar information**, not merely more channels: a matrix/coupled lower bound with cross-channel terms, prime- or mode-dependent admissible state, a stronger localized arithmetic estimate, a different source-exact decomposition whose correction is not trapped by the short witness, or direct coercivity/inertia control. Finite auxiliary dimension, complex phases and carrier modulation are representation resources only when the propagated premise is still the same scalar inequality.

## Track comparison coercivity, compact complexity and information content separately

Endpoint concentration, carrier frequency, compact correction size, cap defect, localization complexity and channel dimension remain useful implementation resources. WI-320--WI-321 change their logical role: none can strengthen a scalar premise by itself. The decisive currency is **what extra relation is propagated between localized pieces beyond the Cartesian product of scalar semibounds**.

## Keep compact certificate design separate from full Weil positivity

Finite-dimensional trial-subspace optimization remains downstream of source-valid information retention. The capped decomposition can expose bounded positive tail margin and finite negative sectors, but WI-315--WI-316 make its cofinal semantics RH-equivalent and WI-320--WI-321 block autonomous scalar improvement even after finite complex channelization. Any compact certificate that contributes to RH must therefore import a nontrivial sign-producing estimate rather than rely on iterative scalar localization.

## Preserve the signed-density quotient

Even a successful reserve-lifted architecture must survive the exact density-one cancellation of WI-241. Large positive reserve or retained arithmetic mass is not yet the required signed discrepancy theorem; the RH-relevant source variable remains the signed discrepancy after universal prime main density and pole cancellation.
