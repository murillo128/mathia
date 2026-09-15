# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Complete one-signed screening is closed; the remaining source currency is signed prime discrepancy

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-028-dyadic-screening-forces-a-uniform-archimedean-reserve-before-any-nonpositive-one-signed-weil-test`.

WI-298--WI-301 close complete one-signed dyadic screening. Rearrangement plus the independently replayed compact-window certificate gives

`q_arch(f) >= c_0 ||f||_2^2`,  `c_0=8.9e-18`,

for every nonzero real one-signed compactly supported test that screens all powers of two. Hence any such nonpositive Weil test needs a uniform unscreened arithmetic contribution.

WI-241 sharpens what that contribution must mean. For every compactly supported complex test, not only odd tests, the pole term and the density-one prime main term cancel exactly. The Weil form can be written schematically as

`Q_W = Q_gamma + R - 2 Delta_Lambda`,

where `R` is a bounded nonnegative density-one autocorrelation remainder and `Delta_Lambda` is the smoothed signed discrepancy of `d(psi-x)`. The total prime-power mass is therefore not the decisive currency: the universal main density has already been neutralized by the pole.

On the odd negative-index branch, Weil positivity would force a uniform signed deficit in `Delta_Lambda`. Thus the live source theorem is to control the **signed discrepancy relative to the density-one baseline**, not merely to prove that some unscreened prime-power mass exists. WI-301's reserve remains a necessary one-signed constraint, but it does not identify or lower-bound this discrepancy.

A surviving route must therefore couple the one-signed reserve to a source-specific statement about `psi-x`, or leave the one-sign/screening class and control sign-changing tests by another mechanism.

## Keep structural reduction, compact positivity, total source mass and signed discrepancy separate

WI-298 is an exact rearrangement theorem. WI-300 is a rigorous computer-assisted compact-window certificate, not a formal Lean proof. WI-301 converts them into an aperture-independent reserve theorem on a nonlinear one-signed screened class. WI-241 is a parity-free exact cancellation identity separating the density-one baseline from the prime discrepancy; oddness enters only when deriving the negative-index consequence.

None of these statements is unrestricted large-aperture Weil positivity. In particular, a lower bound on total unscreened prime interaction does not imply the signed `Delta_Lambda` estimate required after the pole/main-density cancellation.