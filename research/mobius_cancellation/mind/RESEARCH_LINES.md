# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Exclude near-injectivity, affine bias, or exponentially small effective occupancy

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`, `MI-024-arithmetic-image-blind-exclusion-is-directional-leverage`.

MC-281--MC-284 reduce blind exclusion to arithmetic-image Christoffel leverage and show that moderate-conductor shadows can already realize the full Boolean cube. MC-285 kills the even-weight branch unless occupancy is nearly injective. MC-286 identifies the odd affine obstruction exactly. MC-288 then shows that in the collision-rich odd branch, failure of the target row forces odd girth greater than `t`, hence either

`0 notin aff(S)`

or

`K/2^r <= (t+2)/2^(t+1)`.

MC-289 converts the non-affine sparse branch into a scalar arithmetic interface that also sees multiplicities. With

`eta = N^2/(2^r sum_s n_s^2)`,

the absence of every short odd relation forces some nontrivial generated character to satisfy

`A_lambda/N <= -(eta/(1-eta))^(1/(t-2))`.

Equivalently, if every generated quadratic product character has negative shell bias smaller than `delta`, then `eta < delta^(t-2)/(1+delta^(t-2))`. At the natural `eta~t 2^-t` scale the forced bias is order one, asymptotically at least `1/2` in magnitude.

Thus the collision-rich escape is no longer merely “support can be exponentially sparse.” It is: **either effective occupancy is exponentially small after multiplicities are priced, or one explicit generated quadratic character has a large negative shell average.** The remaining arithmetic theorem can attack that one-sided character sum, prove a lower bound on `eta`, or exclude near-injective encoding at admissible conductor/support scale.

## Keep parity, affine obstruction, effective occupancy, multiplicity concentration and conductor separate

Even weights are killed by equal-cell pairing. Odd weights require an odd nucleus plus pair capacity. The affine branch has a character with bias exactly `-1`; the non-affine branch of MC-289 may still evade a large character only by making the participation ratio `eta` exponentially small.

Raw support density and `eta` are not interchangeable: severe multiplicity concentration can make `eta` much smaller than `K/2^r`. Likewise the generated character may have large effective conductor. A closing theorem must state which of these resources it controls rather than replacing one by another.

## Preserve source-depth and matched controls as falsifiers

The Geelen threshold is sharp for arbitrary binary matroids, and the odd-moment argument of MC-289 is finite Fourier algebra once short odd relations are absent. Further progress must therefore use arithmetic properties of the actual Legendre shell: one-sided cancellation for the generated product characters, multiplicity spread, conductor restrictions, or another source-native constraint. Generic finite geometry alone has reached its endpoint.
