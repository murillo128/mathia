# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Control the signed linear residual without reconstructing or deleting the blind atom

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`.

MC-266--MC-272 close arbitrary-coefficient operator norms, positive generating majorants and raw complex-circle norms at the one-blind-row threshold. MC-273--MC-275 then separate witness discovery from normalization: a negative witness collapses a row to one homogeneous shell, all negative witnesses can be aggregated at degree only `m+1`, but exact or pointwise approximate normalization reconstructs Boolean OR and spends too much source degree on the generic cube.

MC-276 closes the natural distributional escape. Quadratic/L2 normalization with the correct blind-point value is cheap because its loss removes the blind atom exactly. The uniform optimizer is the same Christoffel kernel already present in the endpoint-energy route, and on the arithmetic shell

`empirical L2 error = (E_(m,y)(t)-A_y(t))/C`.

Therefore a small distributional classification error cannot upper-bound the blind count `A_y(t)`. Even support-respecting signed witness weights exist at degree `m`, so witness localization itself is not the missing resource.

The live theorem is phase-sensitive and linear. Control

`L_(m,y)(t)=Z_m(k_y)^(-1) sum_(|S|<=m) sum_(|T|=t) chi_T(q_S)`

together with enough signed information on nonblind rows that an integer blind contribution cannot be hidden by cancellation. Equivalently, control the original uncentered Christoffel energy without replacing it by a loss that subtracts the target atom. The relevant source depth is now `m`, not `2m`, but the required arithmetic cancellation is correspondingly sharper.

## Keep overlap, normalization and target visibility separate

A negative witness simplifies one row; overlapping all witnesses remains low-degree; pointwise normalization is generically expensive; L2 normalization is cheap but target-blind. These are four different statements. A future proof should state whether its observable retains the blind atom, whether it is signed or positive, and which source degree it consumes before importing a generic classification or approximation theorem.

MC-252 remains the matched control: once tight prime-shell localization is removed, genuine separated-prime Legendre data can realize the full Boolean cube. Any low-depth signed escape must therefore use the localized arithmetic image or another source-specific relation, not primality or reciprocity alone.
