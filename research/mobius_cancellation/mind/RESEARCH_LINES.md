# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Force the remaining near-negative spectrum into an arithmetically impossible high-cost regime

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`, `MI-024-arithmetic-image-blind-exclusion-is-directional-leverage`, `MI-025-small-exceptional-character-family-is-forced-toward-an-affine-halfspace`, `MI-026-low-source-cost-near-negative-spectrum-collapses-to-one-landau-page-mode`.

MC-281--MC-284 reduce blind exclusion to arithmetic-image Christoffel leverage and show that moderate-conductor shadows can already realize the full Boolean cube. MC-285 kills the even-weight branch unless occupancy is nearly injective. MC-286 identifies the odd affine obstruction exactly. MC-288 then shows that in the collision-rich odd branch, failure of the target row forces odd girth greater than `t`, hence either `0 notin aff(S)` or `K/2^r <= (t+2)/2^(t+1)`.

MC-289 converts the non-affine sparse branch into a scalar arithmetic interface that also sees multiplicities. With `eta=N^2/(2^r sum_s n_s^2)`, the absence of every short odd relation forces some nontrivial generated character to satisfy `A_lambda/N <= -(eta/(1-eta))^(1/(t-2))`. MC-290 sharpens that interface when analytic input controls all but a small exceptional family: the exact odd moments force one exception toward the `-1` affine endpoint whenever the exceptional family is small enough and `eta` is not too small.

MC-291 shows that the near-negative spectrum itself has rigid finite geometry. For `E_tau={lambda:d_lambda<=tau}`, every odd zero-sum subset satisfies `sum d_lambda>=1`; sufficiently small total defect therefore forbids short odd circuits, and a high-rank family with `R tau<1` must place substantial mass in one common preferred-sign cell. MC-292 removes the `R tau<1` threshold from rank control through the entropy budget

`sum_i [1-h_2(d_i)] <= log_2(1/eta)`

for linearly independent biased characters. This bounds independent bias complexity without controlling conductor or cardinality.

MC-293 adds the missing low-source-cost arithmetic axis. Let `Q(lambda)` be the minimum product of lower-prime coordinates representing a shell functional and `D_y=exp(kappa log y/loglog y)` for sufficiently small absolute `kappa`. Outside at most one Landau--Page exceptional functional, every nonzero mode with `Q(lambda)<=D_y` has `|A_lambda|/N << (log y)^-2`. Hence at the live near-negative scale the low-cost spectrum has cardinality at most one. If that singleton is near-affine with defect `d_lambda<=tau<=1/4`, its primitive exceptional real character has a zero `beta_*=1-delta_*` satisfying

`delta_* << (tau+(log y)^-2)/log y`.

At `tau~1/loglog y`, this forces `1-beta_* << 1/(log y loglog y)`. In particular, among `R` independent near-negative directions, at least `R-1` must have source cost larger than `D_y`.

The unresolved escape is therefore no longer an undifferentiated exceptional spectrum. It is one of four concrete regimes: effective occupancy is extremely small; the shell encoding is nearly injective; one classical Landau--Page mode is genuinely load-bearing; or the required independent near-negative directions live in the **high-source-cost** generated family beyond `D_y`. The next theorem must rule out or exploit the singleton exceptional mode, force high source cost to interact with multiplicity/participation, or obtain arithmetic cancellation/structure for that high-cost family.

## Keep parity, occupancy, entropy complexity and source cost as different currencies

Even weights are killed by equal-cell pairing. Odd weights require an odd nucleus plus pair capacity. The affine branch has a character with bias exactly `-1`; MC-289--MC-292 constrain non-affine escape using odd moments, common-cell geometry and entropy, while MC-293 constrains a different variable: the minimum lower-prime product cost of a generated shell functional.

Raw support density and `eta` are not interchangeable: multiplicity concentration can make `eta` much smaller than `K/2^r`. Exceptional cardinality, independent rank, defect profile, entropy cost `1-h_2(d_lambda)`, source cost `Q(lambda)`, primitive conductor and the conductor of a whole family are likewise distinct. MC-293 says almost all sufficiently low-cost modes are balanced; it does not bound the number, rank or bias of high-cost modes. A closing theorem must state which arithmetic currency it controls and how that control reaches the blind endpoint.

## Preserve matched controls and classical exceptional-character theory as falsifiers

The Geelen threshold is sharp for arbitrary binary matroids, and MC-289--MC-292 are finite Fourier/information algebra once the shell data are fixed. MC-293 uses classical Landau--Page/character-PNT input and therefore closes only the quasi-subpower individual source-cost sector; it is not new cancellation technology and it does not rule out a Landau--Siegel zero.

Further progress must use arithmetic properties of the actual Legendre shell that are not already contained in these controls: lower bounds on effective occupancy, exclusion or exploitation of the unique exceptional mode, restrictions linking high source cost to shell multiplicity, or cancellation for the high-cost source-generated product characters. Generic finite geometry, entropy, or another low-conductor exceptional-family estimate will not close the remaining branch.