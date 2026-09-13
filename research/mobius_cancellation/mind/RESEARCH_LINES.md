# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Exploit cheap overlapping witnesses without reconstructing generic OR

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`.

MC-266--MC-272 close arbitrary-coefficient operator norms, positive generating majorants and raw complex-circle norms at the one-blind-row threshold. MC-273 then finds an exact nonblind normal form: once any negative lower-prime witness is known, the mixed Hamming-ball coefficient collapses to one homogeneous degree-`m` shell.

MC-274 shows that atomwise witness discovery through a coordinate-query tree raises source/Walsh degree by one per query. MC-275 sharpens the boundary: **using all negative witnesses at once is cheap**. The overlapping aggregate is exactly

`U_m(x)=sum_i n_i(x)e_m(x_hat_i)=b(x)g_m(x)=1/2[(k-m)e_m-(m+1)e_(m+1)]`,

so it has degree only `m+1`.

The expensive operation is normalizing that overlap into one unit per nonblind row. The exact nonblind selector is Boolean OR and has degree `k`; even uniform approximate normalization on the full cube costs `Theta(sqrt(k log(1/epsilon)))`. At constant error this already exceeds the live Christoffel depth, and atom-sensitive accuracy is much worse. A generic polynomial partition of witnesses therefore does not repair the endpoint.

The live theorem must use information absent from the generic cube: the tightly localized Legendre-shell image, a distributional rather than pointwise surrogate on that image, or the unnormalized signed identity `U_m=b g_m` in a way that never divides by the witness count. MC-252 shows that once tight prime-shell localization is removed, genuine separated-prime Legendre data can realize the whole Boolean cube, so reciprocity and primality alone are not enough to evade the OR barrier.

## Keep overlap, normalization complexity and endpoint cancellation separate

A negative witness simplifies one row; summing all such simplifications remains low-degree; making the sum behave as a normalized nonblind classifier is a different observable. MC-275 makes that distinction exact. A future proof should state whether it controls the original flat vector, the cheap overlapping witness aggregate, a source-restricted approximation to nonblindness, or an actual normalized partition.

The main dead ends remain: enlarging the flat source to arbitrary coefficients, positive/absolute scalarization, atomwise witness search, and generic low-degree OR normalization all spend the available budget before arithmetic cancellation is tested. The surviving opportunity is narrower: exploit the arithmetic restricted image or a signed aggregate whose usefulness does not require endpoint classification.
