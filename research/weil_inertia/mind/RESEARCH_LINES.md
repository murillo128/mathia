# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Rule out zero-critical supports using the full aperture-growing prime family, not its nearest-prime shadow

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`, `MI-020-complete-one-signed-screening-trades-discrete-vanishing-for-support-packing`, `MI-021-complete-screening-promotes-support-avoidance-to-prime-deleted-spectral-criticality`, `MI-022-fixed-finite-prime-power-screening-cannot-buy-prime-deleted-spectral-coercivity`, `MI-023-nearest-prime-width-has-a-lambert-w-spectral-endpoint`.

WI-281--WI-283 exhaust pure support topology. WI-284 restores the operator-level first-crossing constraint: complete one-signed screening deletes the von Mangoldt translation form on the entire supported form-domain subspace, so the prime-deleted gamma-plus-pole form must be PSD there with bottom exactly zero. WI-285 shows that every fixed finite prime-base approximation is too weak; arbitrarily sparse full-span supports can screen all those powers while retaining arbitrarily negative prime-deleted directions.

WI-286 introduces the first genuinely growing-family compression. A prime near the two-island separation forces exponentially thin components, and comparison with gamma uncertainty and the exact pole factor exposes the strict square-root prime-gap threshold. The peer-reviewed Baker--Harman--Pintz exponent `0.525` gives width exponent `0.475`; Runbo Li's current `0.52` preprint claim improves it to `0.48`. Both remain on the wrong side of `1/2` for this interface, so neither closes the spectral contradiction.

WI-287 sharpens the critical-scale compression. For `H(x)=sqrt(x)F(x)`, the width-relaxed two-island bottom is

`lambda_width(x) = (1/2)log x - log F(x) - F(x) + O(1)`,

with transition

`F_*(x)=W(sqrt(x))=(1/2)log x-log log x+log 2+o(1)`.

Below `F_*-omega(1)` the whole width-relaxed class becomes positive; above `F_*+omega(1)` the relaxation still contains explicit negative odd directions. The direct contradiction target remains the full WI-284 statement

`for every admissible completely screened E, inf q_arch^a|_(D_E) != 0`.

The next theorem must therefore either beat the Lambert-`W` width endpoint or exploit information that nearest-prime compression discards: simultaneous screening by the entire aperture-growing prime family, quantitative amplitudes from the actual null equation, multi-component geometry, or another collective source-specific constraint.

## Keep complete-screening spectral criticality separate from sign-changing and incomplete branches

The operator-domain deletion in WI-284 uses one-signedness to turn zero autocorrelation into support disjointness and uses complete screening to erase every prime term. Sign-changing cancellation does not imply disjointness, and one surviving prime lag destroys the prime-deleted identity. WI-285 concerns fixed finite screening shadows; WI-286--WI-287 concern only a scalar width consequence of growing screening. None can be promoted to the full complete branch without restoring the missing information.

## Keep endpoint firstness, source reserve, growing-family rigidity and sign geometry as separate gates

The reserve inequalities are sign-independent, while the support/spectral bootstrap uses a one-signed mode. A support-sensitive archimedean contradiction would not prove that the relevant first mode has one sign, and a sign theorem would not close the quantitative reserve. WI-285 prices finite-base packing; WI-286 prices current nearest-prime width information at the square-root scale; WI-287 gives the exact Lambert-`W` endpoint of that compression. Future work should state which gate and which information loss it actually crosses.