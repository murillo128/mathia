# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Convert endpoint defect geometry into an arithmetic impossibility for the high-cost quotient

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`, `MI-024-arithmetic-image-blind-exclusion-is-directional-leverage`, `MI-025-small-exceptional-character-family-is-forced-toward-an-affine-halfspace`, `MI-026-low-source-cost-near-negative-spectrum-collapses-to-one-landau-page-mode`.

MC-281--MC-292 reduce the collision-rich odd branch to finite Fourier, odd-girth, common-cell and entropy constraints. MC-293 adds source cost: below `D_y=exp(kappa log y/loglog y)` the near-negative spectrum contains at most one Landau--Page exceptional functional. MC-294 then shows that many independent near-negative directions cannot hide behind a cheap subspace: after deleting at most one direction, their images in the high-cost quotient have no short dependencies, so Hamming sphere packing forces a quantitative quotient-dimension bill.

MC-295 proves that this generic bill can still be saturated by a fixed-weight defect-shell model. At the live `k=1`, even-`R` endpoint it realizes defect `1/R`, effective participation `R2^-R`, full high-cost quotient dimension and no common preferred-sign cell while every cheap nonzero direction is perfectly balanced. Thus the existing generic coding package is not an impossibility theorem.

MC-296 extracts substantially more source-cost information from the **endpoint partition itself**. If independent selected shell functionals `lambda_i` have disjoint defect sets partitioning the shell with masses `d_i`, then every subset sum has the exact Fourier bias

`x_(lambda_I)=(-1)^|I| (1-2 d(I))`, `d(I)=sum_(i in I)d_i`.

Hence, except for the possible unique Page-exceptional functional, every subset with `|d(I)-1/2|>epsilon_y/2` must have source cost above `D_y`. If `d_min>epsilon_y`, the low-cost subsets form an antichain, so Sperner gives

`# low-cost <= binom(R,floor(R/2))+1`.

For equal endpoint defects `d_i=1/R` and `R=o((log y)^2)`, almost the entire selected Fourier subspace is therefore forced high-cost: all nonzero modes for odd `R`, and all but the middle Hamming layer for even `R`, up to the one Page exception. The high-cost fraction is `1-O(R^-1/2)`.

This sharpens the remaining gate. It is no longer enough to ask whether the selected basis vectors are expensive. An actual Legendre-shell realization of the endpoint geometry would force **almost every noncentral linear combination** in the selected span above the Page threshold. What is still missing is a theorem saying that an arithmetic shell cannot support that exponentially large high-cost spectrum, or that source cost across so many combinations forces a quotient-dimension/occupancy/multiplicity contradiction.

The next useful theorem should therefore couple source cost to multiplicity or collective realizability, not refine the bias estimate again. Source cost of individual functionals is not quotient dimension, and MC-296 deliberately stops before asserting that many expensive modes require many independent expensive coordinates.

## Keep parity, occupancy, entropy complexity, individual source cost, spectrum-wide source cost and quotient realizability separate

Even weights are killed by equal-cell pairing. Odd weights require an odd nucleus plus pair capacity. MC-289--MC-292 constrain non-affine escape using odd moments, common-cell geometry and entropy. MC-293 constrains minimum lower-prime product cost of individual generated shell functionals; MC-294 charges many selected directions to high-cost quotient dimension and girth.

MC-295 separates arithmetic realizability from those generic bills. MC-296 then separates **basis cost** from **subset-spectrum cost**: under an exact endpoint partition, Page balance prices almost all subset sums, not just the chosen generators. None of these statements by itself bounds the dimension or multiplicity of the expensive arithmetic source. A closing theorem must connect those currencies rather than conflate them.

## Preserve matched controls and classical exceptional-character/coding theory as falsifiers

The Geelen threshold, entropy inequalities, Hamming sphere-packing and Sperner bounds are sharp or near-sharp finite controls, not arithmetic impossibility theorems. MC-293 imports Landau--Page/character-PNT input only into the quasi-subpower source-cost sector. MC-296 uses that same arithmetic input plus the exact endpoint partition to force an almost-total high-cost subset spectrum.

Further progress must exploit properties of the actual Legendre shell unavailable to the fixed-weight model: an upper bound on collective high-cost realizability, a source-cost/multiplicity law, occupancy forced by lower-prime incidence, or a mechanism excluding the exceptional mode. The next theorem should state explicitly how an exponential family of expensive subset characters consumes an arithmetic resource that MC-295 is free to assign abstractly.