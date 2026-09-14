# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## On symmetric two-islands, full screening is exactly a nearest-prime-power gap problem

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`, `MI-020-complete-one-signed-screening-trades-discrete-vanishing-for-support-packing`, `MI-021-complete-screening-promotes-support-avoidance-to-prime-deleted-spectral-criticality`, `MI-022-fixed-finite-prime-power-screening-cannot-buy-prime-deleted-spectral-coercivity`, `MI-023-nearest-prime-width-has-a-lambert-w-spectral-endpoint`.

WI-284 remains the operator target: complete one-signed screening deletes the von Mangoldt translation form on the supported form-domain subspace, so the prime-deleted gamma-plus-pole form must have bottom exactly zero. WI-285 shows fixed finite prime-base shadows are too weak. WI-286--WI-287 calibrate the symmetric two-island width relaxation and expose the Lambert-`W` endpoint.

WI-288 removes the remaining hope that the **full aperture-growing screening family** carries extra support geometry on this fixed topology. For

`E=(-R-b,-R+b) union (R-b,R+b)`, `x=e^(2R)`,

in the narrow-island regime, complete screening by every active prime power is exactly equivalent to

`2b <= delta_pp(x) := min_(q prime power)|log q-log x|`.

The entire family collapses to the two nearest prime-power neighbors of `x`; no additional many-lag packing invariant survives on two symmetric islands.

Combining this exact support equivalence with the WI-284 zero-bottom requirement and the WI-287 gamma/pole bounds yields the necessary condition

`sqrt(x) delta_pp(x) >= W(c_0 sqrt(x)) = (1/2)log x - log log x + O(1)`.

Equivalently, a hypothetical completely screened zero-critical two-island support must sit inside a two-sided prime-power gap of additive size about `sqrt(x) log x`. Current unconditional short-interval results remain too weak to contradict this.

The live two-island theorem is therefore genuinely arithmetic: rule out prime-power gaps at the required Lambert scale, or use information from the actual null equation that is stronger than support screening alone. To gain new support geometry from simultaneous lags, the architecture must leave the symmetric two-island topology (many components, different geometry) or leave the one-signed complete-screening branch.

## Keep support screening, null-equation amplitudes and sign geometry separate

WI-288 is exact only for the one-signed symmetric two-island support geometry. It does not treat sign-changing cancellation, incomplete screening, many-component/fractal supports, or amplitudes imposed by the null vector itself. Those are now the only places where “full-family information” can mean more than the nearest actual prime-power gap in this branch.
