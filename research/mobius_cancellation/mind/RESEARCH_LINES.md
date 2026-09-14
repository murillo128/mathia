# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Control the blind endpoint before aggregation, or find a source-native rational inverse

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`.

MC-266--MC-277 show that the existing degree-`m` row representation still carries the blind bit with exact margin `delta_(k,m)~2m/k`; pointwise polynomial normalization is expensive, while L2 normalization is cheap precisely because it subtracts the target atom. The main loss is therefore created when many row identities are normalized or aggregated and exceptional-row provenance disappears.

MC-278 tests the first obvious nonlinear escape. The rational decoder `(1+b)^(-q)` isolates a blind row with only `q=Theta(log C)` rational degree, but its unique positive Walsh expansion places asymptotically all coefficient mass near source degree `k/2`. At the live depth `m=Theta(log log y)=o(k)`, the low-source-depth truncation carries only `o(1)` of the blind value. Rational degree has not supplied a low-depth arithmetic representation; denominator inversion has hidden the source cost.

Two genuinely different routes remain. First, control the existing Christoffel row scalar at its natural margin before provenance is discarded, or derive signed cross-row cancellation that cannot mask one blind contribution. Second, find a **source-native direct rational/resolvent identity** that evaluates an endpoint-sensitive aggregate without expanding the denominator into Walsh subsets. The latter must use localized arithmetic structure rather than generic Boolean rational approximation.

## Keep algebraic degree, source depth, conditioning, normalization and aggregation separate

A negative witness simplifies one row; overlapping witnesses remains low-degree; the raw row scalar has a polynomially small but exact margin; polynomial normalization can reconstruct OR at high degree; rational normalization can have low numerator/denominator degree while importing macroscopic Walsh depth; and L2 aggregation can erase the target atom by design. These are different resources.

MC-252 remains the matched control: once tight prime-shell localization is removed, separated-prime Legendre data can realize the full Boolean cube. Any successful escape must therefore identify where the localized arithmetic source supplies information unavailable to this generic cube geometry.