# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Exclude near-injectivity, near-affine exceptional concentration, or exponentially small effective occupancy

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`, `MI-024-arithmetic-image-blind-exclusion-is-directional-leverage`, `MI-025-small-exceptional-character-family-is-forced-toward-an-affine-halfspace`.

MC-281--MC-284 reduce blind exclusion to arithmetic-image Christoffel leverage and show that moderate-conductor shadows can already realize the full Boolean cube. MC-285 kills the even-weight branch unless occupancy is nearly injective. MC-286 identifies the odd affine obstruction exactly. MC-288 then shows that in the collision-rich odd branch, failure of the target row forces odd girth greater than `t`, hence either `0 notin aff(S)` or `K/2^r <= (t+2)/2^(t+1)`.

MC-289 converts the non-affine sparse branch into a scalar arithmetic interface that also sees multiplicities. With `eta=N^2/(2^r sum_s n_s^2)`, the absence of every short odd relation forces some nontrivial generated character to satisfy `A_lambda/N <= -(eta/(1-eta))^(1/(t-2))`. MC-290 sharpens that interface when analytic input controls all but a small exceptional family: the exact odd moments force one exception toward the `-1` affine endpoint whenever the exceptional family is small enough and `eta` is not too small.

MC-291 now shows that the exceptional modes themselves have rigid finite geometry. For the near-negative spectrum `E_tau={lambda:d_lambda<=tau}`, every odd zero-sum subset obeys `sum d_lambda>=1`; hence no odd circuit of length `j` can occur when `j tau<1`. Applying the same odd-girth rigidity in the dual space gives: either the near-negative family is exponentially sparse in its generated span, or all its modes share an exactly compatible `-1` sign cell. Moreover, if its independent rank is `R` with `R tau<1`, then

`eta <= 2^(-R)/(1-R tau)^2`.

Thus non-negligible effective occupancy directly limits the rank of almost-constant-negative exceptional characters. The collision-rich escape is now narrower: **effective occupancy is exponentially small, the encoding is near-injective, or the exceptional near-negative spectrum has low rank / sparse dual geometry / a common affine sign cell compatible with the actual Legendre shell.** The remaining arithmetic theorem can lower-bound `eta`, bound exceptional rank/size and conductor, or rule out the resulting common-cell concentration for the source-generated product characters.

## Keep parity, affine obstruction, effective occupancy, multiplicity concentration, exceptional-family size, exceptional rank and conductor separate

Even weights are killed by equal-cell pairing. Odd weights require an odd nucleus plus pair capacity. The affine branch has a character with bias exactly `-1`; MC-289 shows the non-affine branch can avoid a large negative character only by reducing effective occupancy, MC-290 pushes a small exceptional family toward the affine endpoint, and MC-291 shows that many such near-endpoint characters cannot be geometrically independent unless occupancy collapses.

Raw support density and `eta` are not interchangeable: severe multiplicity concentration can make `eta` much smaller than `K/2^r`. Likewise `J`, the one-sided threshold `delta`, near-negative rank `R`, defect threshold `tau` and effective conductor are separate resources. A closing theorem must state which of these currencies it controls rather than replacing one by another.

## Preserve source-depth and matched controls as falsifiers

The Geelen threshold is sharp for arbitrary binary matroids, and the odd-moment/dual-odd-girth arguments of MC-289--MC-291 are finite Fourier algebra once short odd relations are absent. Further progress must therefore use arithmetic properties of the actual Legendre shell: one-sided cancellation with quantitative exceptional-set control, multiplicity spread, conductor restrictions, exclusion of a large common preferred-sign cell, or another source-native constraint. Generic finite geometry alone has reached its endpoint.