# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove directional separation of the blind endpoint on the actual arithmetic image, or find a source-native inverse

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`, `MI-024-arithmetic-image-blind-exclusion-is-directional-leverage`.

MC-266--MC-277 show that the existing degree-`m` row representation still carries the blind bit with exact margin `delta_(k,m)~2m/k`; pointwise polynomial normalization is expensive, while L2 normalization is cheap precisely because it subtracts the target atom. The main loss is created when row identities are normalized or aggregated and exceptional-row provenance disappears.

MC-278 shows that one low-rational-degree decoder does not escape this source-depth bill: its positive Walsh mass concentrates near degree `k/2`. MC-279 removes dependence on that formula for positive-definite decoders: pointlike positive endpoint localization forces essentially half-cube source depth.

MC-280 closes the remaining **signed full-cube pointwise scalar** loophole at the accuracy actually required by direct exceptional-row counting. For an arbitrary real or complex decoder with `D(x_*)=1` and uniform off-atom error `epsilon`, Parseval and Cauchy--Schwarz bound the entire low-depth Walsh coefficient variation by `sqrt(Z_m(k)) ||D||_2`. At the live atom-sensitive accuracy `epsilon<1/(2C)` and source depth `m=t+1`, this variation is `o(1)`.

MC-281 turns the surviving arithmetic-image route into an exact directional question. With `A` the actual shell feature matrix and `v=1_Z` the virtual blind row, the empirical Christoffel value `inf_(v^*a=1)||Aa||_2^2` bounds the blind count. Equivalently, blindness is excluded if `v` lies outside `ran(A^*)`, or if its minimum signed synthesis cost `Lambda=v^*(A^*A)^+v` exceeds one. Generic coefficient-uniform operator norms cannot prove either alternative because the row-norm barrier stops exactly at `Lambda>=1`.

The live theorem is therefore shell-specific **directional leverage/rank geometry**: prove that tight arithmetic localization makes the blind endpoint leave the actual degree-`m` row span, or makes its signed synthesis norm strictly larger than one. This is cancellation across target rows before sharp scalarization. A genuinely source-native arithmetic/operator inverse remains the other qualitatively distinct escape.

## Keep algebraic degree, source depth, scalar accuracy, normalization, aggregation and endpoint orientation separate

A negative witness simplifies one row; overlapping witnesses remain low-degree; the raw row scalar has a polynomially small exact margin; polynomial normalization can reconstruct OR at high degree; rational normalization can have low numerator/denominator degree while importing macroscopic Walsh depth; MC-279 gives a positivity-driven half-depth barrier; MC-280 shows that atom-sensitive full-cube accuracy alone kills low-depth signed coefficient variation; and MC-281 shows that restricting to the actual arithmetic image replaces uniform decoding by one directional row-span/inverse-Gram problem. These are different resources.

MC-252 remains the matched control: once tight prime-shell localization is removed, separated-prime Legendre data can realize the full Boolean cube. Any successful directional leverage theorem must therefore identify how the localized arithmetic shell constrains the orientation of `v` relative to its actual feature span, rather than infer that separation from width, rank deficiency or a generic large-sieve norm alone.
