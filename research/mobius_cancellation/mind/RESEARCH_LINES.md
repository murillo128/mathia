# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Exclude near-injectivity, near-affine exceptional concentration, exponentially small effective occupancy, or a low-information exceptional spectrum

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`, `MI-024-arithmetic-image-blind-exclusion-is-directional-leverage`, `MI-025-small-exceptional-character-family-is-forced-toward-an-affine-halfspace`.

MC-281--MC-284 reduce blind exclusion to arithmetic-image Christoffel leverage and show that moderate-conductor shadows can already realize the full Boolean cube. MC-285 kills the even-weight branch unless occupancy is nearly injective. MC-286 identifies the odd affine obstruction exactly. MC-288 then shows that in the collision-rich odd branch, failure of the target row forces odd girth greater than `t`, hence either `0 notin aff(S)` or `K/2^r <= (t+2)/2^(t+1)`.

MC-289 converts the non-affine sparse branch into a scalar arithmetic interface that also sees multiplicities. With `eta=N^2/(2^r sum_s n_s^2)`, the absence of every short odd relation forces some nontrivial generated character to satisfy `A_lambda/N <= -(eta/(1-eta))^(1/(t-2))`. MC-290 sharpens that interface when analytic input controls all but a small exceptional family: the exact odd moments force one exception toward the `-1` affine endpoint whenever the exceptional family is small enough and `eta` is not too small.

MC-291 shows that the near-negative spectrum itself has rigid finite geometry. For `E_tau={lambda:d_lambda<=tau}`, every odd zero-sum subset satisfies `sum d_lambda>=1`; therefore sufficiently small total defect forbids short odd circuits, and a high-rank family with `R tau<1` must place substantial mass in one common preferred-sign cell. This gives `eta <= 2^(-R)/(1-R tau)^2` in the common-cell regime.

MC-292 removes the artificial `R tau<1` endpoint from rank control. For any linearly independent exceptional modes,

`sum_i [1-h_2(d_i)] <= log_2(1/eta)`.

Thus if every `d_i<=tau<1/2`, then

`R <= log_2(1/eta)/(1-h_2(tau))`,

with no intersection assumption. The mechanism is the classical entropy/large-spectrum principle: every independent biased character consumes part of the shell's finite entropy deficit. It complements rather than replaces MC-291—the common-cell estimate can be sharper when the total defect is small, while the entropy budget remains informative after the preferred-cell union bound becomes vacuous.

The collision-rich escape is therefore narrower: **effective occupancy is exponentially small, the encoding is near-injective, or the actual generated exceptional family must have limited independent bias complexity and/or strong low-rank/conductor structure compatible with the Legendre shell.** The remaining theorem is arithmetic, not another generic finite-geometric refinement: lower-bound `eta`, control exceptional defect/rank/size/conductor for the source-generated quadratic characters, or rule out the resulting affine/common-cell concentration.

## Keep parity, affine obstruction, effective occupancy, multiplicity concentration, exceptional-family size, exceptional rank, entropy deficit and conductor separate

Even weights are killed by equal-cell pairing. Odd weights require an odd nucleus plus pair capacity. The affine branch has a character with bias exactly `-1`; MC-289 shows the non-affine branch can avoid a large negative character only by reducing effective occupancy, MC-290 pushes a small exceptional family toward the affine endpoint, MC-291 controls common-cell geometry while total defect is small, and MC-292 gives a threshold-free entropy budget for independent biased modes.

Raw support density and `eta` are not interchangeable: severe multiplicity concentration can make `eta` much smaller than `K/2^r`. Likewise exceptional cardinality, independent rank, defect profile, entropy cost `1-h_2(d_lambda)`, one-sided threshold and conductor are different currencies. MC-292 controls rank weighted by bias, not cardinality and not conductor. A closing theorem must state which arithmetic currency it actually controls.

## Preserve source-depth and matched controls as falsifiers

The Geelen threshold is sharp for arbitrary binary matroids, and the odd-moment, dual odd-girth and entropy-rank arguments of MC-289--MC-292 are finite Fourier/information algebra once the shell data are fixed. Further progress must therefore use arithmetic properties of the actual Legendre shell: one-sided cancellation with quantitative exceptional-set control, multiplicity spread, conductor restrictions, exclusion of a large common preferred-sign cell, or another source-native constraint. Generic finite geometry or entropy alone has reached its endpoint.