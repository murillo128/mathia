# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Exclude near-injectivity, near-affine exceptional concentration, or exponentially small effective occupancy

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`, `MI-024-arithmetic-image-blind-exclusion-is-directional-leverage`, `MI-025-small-exceptional-character-family-is-forced-toward-an-affine-halfspace`.

MC-281--MC-284 reduce blind exclusion to arithmetic-image Christoffel leverage and show that moderate-conductor shadows can already realize the full Boolean cube. MC-285 kills the even-weight branch unless occupancy is nearly injective. MC-286 identifies the odd affine obstruction exactly. MC-288 then shows that in the collision-rich odd branch, failure of the target row forces odd girth greater than `t`, hence either

`0 notin aff(S)`

or

`K/2^r <= (t+2)/2^(t+1)`.

MC-289 converts the non-affine sparse branch into a scalar arithmetic interface that also sees multiplicities. With

`eta = N^2/(2^r sum_s n_s^2)`,

the absence of every short odd relation forces some nontrivial generated character to satisfy

`A_lambda/N <= -(eta/(1-eta))^(1/(t-2))`.

MC-290 sharpens that interface when analytic input controls all but a small exceptional family. If outside `J` exceptional characters one has `A_lambda/N >= -delta`, then the exact odd moments force the exceptional set to absorb essentially the whole forbidden odd-moment deficit. With `epsilon_m=delta^(m-2)(eta^-1-1)`, some exception obeys

`-A_lambda/N >= ((1-epsilon_m)/J)^(1/m)`.

Hence `epsilon_m=o(1)` and `log J=o(m)` force one exceptional character to be `-1` on a `1-o(1)` fraction of shell mass. At the natural Geelen scale `eta~t2^-t`, a one-exception theorem with `delta=1/2` already forces only `O(t^-2)` positive-side mass; fixed `delta<1/2` is exponentially stronger.

Thus the collision-rich escape is now: **effective occupancy is exponentially small, the encoding is near-injective, or a small analytic exceptional family contains a character whose shell is quantitatively near the exact affine obstruction.** The remaining arithmetic theorem can prove a lower bound on `eta`, bound the size/negative bias of exceptional generated characters, control their conductor, or rule out the resulting near-affine concentration for the actual Legendre shell.

## Keep parity, affine obstruction, effective occupancy, multiplicity concentration, exceptional-family size and conductor separate

Even weights are killed by equal-cell pairing. Odd weights require an odd nucleus plus pair capacity. The affine branch has a character with bias exactly `-1`; MC-289 shows the non-affine branch can avoid a large negative character only by reducing effective occupancy, while MC-290 shows that allowing only a small exceptional family pushes that family back toward the affine endpoint.

Raw support density and `eta` are not interchangeable: severe multiplicity concentration can make `eta` much smaller than `K/2^r`. Likewise `J`, the one-sided threshold `delta`, and effective conductor are separate analytic resources. A closing theorem must state which of these currencies it controls rather than replacing one by another.

## Preserve source-depth and matched controls as falsifiers

The Geelen threshold is sharp for arbitrary binary matroids, and the odd-moment arguments of MC-289--MC-290 are finite Fourier algebra once short odd relations are absent. Further progress must therefore use arithmetic properties of the actual Legendre shell: one-sided cancellation for the generated product characters with quantitative exceptional-set control, multiplicity spread, conductor restrictions, exclusion of near-affine concentration, or another source-native constraint. Generic finite geometry alone has reached its endpoint.