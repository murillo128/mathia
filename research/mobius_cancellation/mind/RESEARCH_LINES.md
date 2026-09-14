# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Break half-cube concentration or pay near-injective shell encoding

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`, `MI-024-arithmetic-image-blind-exclusion-is-directional-leverage`.

MC-281 turns blind exclusion into the exact arithmetic-image Christoffel/leverage problem. MC-282 shows that nonblindness, feature surplus and arithmetic provenance are weaker than favorable leverage; MC-284 shows the actual shell is Boolean-complete on moderate-conductor coordinate shadows.

MC-285 makes the even-weight obstruction deterministic: equal-pattern pairing forces an endpoint row unless the projected support is almost injective, giving `d` of order `log y` and primorial-scale coordinate conductor in the live regime. MC-286 identifies the odd support obstruction exactly: an odd zero-sum row exists iff `0` lies in the affine hull of the occupied `F_2^d` cells; failure is equivalent to a generated product character that is constantly `-1` on the shell.

MC-287 closes the broad dense odd-support gap. If `K` projected cells are occupied and `K>2^(d-1)`, there is already an odd zero-sum nucleus of size at most three. If the collision excess also satisfies `N-K>=t-1`, equal-cell pairs pad that nucleus to the prescribed odd weight `t`. Therefore every endpoint-normalized energy-`<1` certificate must satisfy

`K<=2^(d-1)  or  N-K<=t-2`.

At `t=O(log log y)`, the second branch is near-injective and again forces `d>=log_2 y-log_2 log y+O(1)` and `log Q(U)>=(1/log 2+o(1)) log y log log y`. There is no large intermediate regime with both dense occupancy and substantial collision mass.

The live source theorem is now a dichotomy, not generic pattern realization: either rule out **half-cube-or-smaller concentration** of the actual growing-support Legendre shell, or show that the alternative near-injective encoding cannot occur at the admissible support/conductor scale. Full Boolean universality is sufficient but much stronger than necessary.

## Keep parity, occupancy, collision excess and conductor separate

Even weights are killed directly by equal-cell pairing. Odd weights need an odd nucleus plus parity-neutral pair capacity; MC-287 shows that density above half the cube makes the nucleus uniformly tiny, but it does not rule out the half-cube branch. Large `d`, large conductor, affine span and favorable Christoffel leverage remain different currencies. A theorem improving one must state which branch of the exact occupancy dichotomy it removes.

## Preserve source-depth and matched controls as falsifiers

Separated-prime Boolean controls, moderate-conductor shell universality and the actual localized shell remain complementary. Any successful inverse must use a source-native collective relation strong enough to exclude the surviving concentration/near-injectivity alternatives, or abandon endpoint Christoffel leverage for a different arithmetic inverse.
