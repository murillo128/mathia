# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Rule out zero-critical supports using the aperture-growing prime family, not finite screening shadows

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`, `MI-020-complete-one-signed-screening-trades-discrete-vanishing-for-support-packing`, `MI-021-complete-screening-promotes-support-avoidance-to-prime-deleted-spectral-criticality`, `MI-022-fixed-finite-prime-power-screening-cannot-buy-prime-deleted-spectral-coercivity`, `MI-023-nearest-prime-width-has-a-lambert-w-spectral-endpoint`.

WI-281 shows that complete one-signed screening forces `log 2` support packing and the strict scalar budget `K_pack<K_+`. WI-282--WI-283 prove that adding every prime-power lag, full essential span and the prime-translation support-domination shadow of the Suzuki null equation still leaves that packing relaxation sharp. Pure support topology is exhausted.

WI-284 restores the full first-crossing form constraint before scalar compression. If a nonnegative null mode screens every active prime-power autocorrelation and `E={v>0}`, then the von Mangoldt translation form vanishes on the **entire** supported form-domain subspace `D_E`. Since the first-crossing form is PSD and `v` is null, the prime-deleted gamma-plus-pole form restricted to `D_E` is PSD with bottom exactly zero.

WI-285 blocks every fixed-finite-base approximation to that target. For any fixed finite set of primes, one can build arbitrarily sparse full-span supports that avoid every power `k log p` of those bases, yet contain odd vectors whose prime-deleted Rayleigh quotient tends to `-infinity`. Support measure, span, fixed-family packing and even fixed-family maximal domination therefore do not control the restricted bottom.

WI-286 introduces the first genuinely growing-family compression: complete screening plus a prime-in-short-interval theorem bounds the width of a symmetric two-island support. Its abstract conclusion is the square-root gap threshold: a bound `H(x) << x^theta` makes the gamma cost dominate the pole instability only on the side `theta<1/2`. The exact current best unconditional numerical exponent cited in WI-286 is under adversarial review; the square-root mechanism itself is not the disputed point and is the only part used here.

WI-287 sharpens that compressed interface at critical scale. If `H(x)=sqrt(x)F(x)` with `F(x)->infinity` and `F(x)=O(log x)`, then the bottom of the **nearest-prime width relaxation** is

`lambda_width(x) = (1/2)log x - log F(x) - F(x) + O(1)`.

The transition is therefore

`F_*(x)=W(sqrt(x))=(1/2)log x-log log x+log 2+o(1)`.

Below `F_*-omega(1)` the entire width-relaxed two-island prime-deleted form is forced positive; above `F_*+omega(1)` the width relaxation still contains explicit odd directions whose Rayleigh quotient tends to `-infinity`. No unconditional prime-gap input is currently being promoted here as crossing the positive side.

The highest-value one-signed theorem must now use one of two currencies. Either obtain source information strong enough to beat the Lambert-`W` width endpoint, or exploit information that the nearest-prime compression discards: simultaneous screening by the full aperture-growing family, quantitative amplitudes from the actual null equation, multi-component geometry, or another collective source-specific constraint. Merely increasing a fixed finite screening template or restating a square-root exponent cannot close the route.

The direct contradiction target remains

`for every admissible completely screened E, inf q_arch^a|_(D_E) != 0`,

ideally by producing a negative direction or proving a strictly positive bottom. WI-285 sharpens the finite-family quantifier and WI-287 sharpens one compressed growing-family endpoint; neither replaces the full operator-domain problem.

## Keep complete-screening spectral criticality separate from the sign-changing and incomplete branches

The operator-domain deletion in WI-284 uses one-signedness to turn zero autocorrelation into support disjointness and uses complete screening to erase every prime term. Sign-changing cancellation does not imply disjointness, and one surviving prime lag destroys the prime-deleted identity. WI-285 concerns fixed finite screening shadows, while WI-286--WI-287 concern a scalar width consequence of growing screening. Neither can be promoted to a theorem for the full complete branch without preserving the corresponding missing information.

## Keep endpoint firstness, source reserve, growing-family rigidity and sign geometry as separate gates

The reserve inequalities are sign-independent, while the support/spectral bootstrap uses a one-signed mode. A support-sensitive archimedean contradiction would not prove that the relevant first mode has one sign, and a sign theorem would not by itself close the quantitative reserve. WI-285 separates finite-base packing from growing arithmetic diversity; WI-287 further shows that even the nearest-prime consequence of that growing diversity has a sharp Lambert-`W` spectral endpoint. Future work should state which gate and which compression level are actually being crossed.
