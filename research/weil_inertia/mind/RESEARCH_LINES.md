# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## On symmetric two-islands, reduce full screening to a coupled prime-gap problem at two scales

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`, `MI-020-complete-one-signed-screening-trades-discrete-vanishing-for-support-packing`, `MI-021-complete-screening-promotes-support-avoidance-to-prime-deleted-spectral-criticality`, `MI-022-fixed-finite-prime-power-screening-cannot-buy-prime-deleted-spectral-coercivity`, `MI-023-nearest-prime-width-has-a-lambert-w-spectral-endpoint`.

WI-284 supplies the operator target: complete one-signed screening forces the prime-deleted gamma-plus-pole form to have bottom exactly zero. WI-288 shows that the entire aperture-growing screening family on two symmetric islands is exactly the nearest-prime-power gap condition and forces the Lambert-scale separation

`sqrt(x) delta_pp(x) >= W(c sqrt(x))`.

WI-289 decomposes that condition by roots:

`delta_pp(x)=min_(k>=1) k delta_p(x^(1/k))`.

The prime layer near `x` requires the enormous `sqrt(x) log x`-scale desert already isolated by WI-288. Prime squares are the unique critical composite layer: they additionally require an approximately mean-gap-sized prime-free interval near `sqrt(x)`. Every exponent `k>=3` produces only subunit root windows. On a dyadic shell, all composite prime-power Lambert neighborhoods still leave order `X log log X/log X` measure uncovered, while the `k>=3` layers are negligible on that scale.

The live theorem is therefore not “control prime powers in bulk.” It is to couple a hypothetical very large prime gap near `x` with prime occurrence near `sqrt(x)`, or otherwise control the nearest prime power at the Lambert radius. Support screening alone supplies no such two-scale correlation. A second route is to use amplitudes/signs from the actual null equation, or leave the symmetric two-island topology.

## Keep support screening, two-scale placement, null amplitudes and sign geometry separate

WI-289 identifies the critical square layer but does not show that large prime-gap centers meet or avoid it. No probabilistic independence is available. Many-component supports, sign-changing modes and incomplete screening remain genuinely different geometries and must not inherit the two-island reduction without a new proof.
