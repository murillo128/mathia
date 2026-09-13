# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Use the negative-witness normal form without paying atom-scale conditioning depth

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`.

MC-266--MC-272 reduce the endpoint to the exact flat quadratic-character source and close arbitrary-coefficient operator norms, positive generating majorants and raw complex-circle norms at the one-blind-row threshold. MC-273 then finds a sharper conditional normal form: once any negative lower-prime witness is known, the mixed Hamming-ball coefficient collapses exactly to one homogeneous degree-`m` shell on the remaining coordinates.

MC-274 shows why this is not yet the endpoint estimate. Exact witness conditioning through query depth `J` raises the Walsh/source degree of the energy from `2m` to `2m+J`, even after all found-witness leaves are recombined. An atomwise strategy that resolves every target row naturally needs `J` on the order of `log C`, which at the live target-shell size is parametrically larger than the original Christoffel depth.

The live theorem is therefore to exploit **nonblindness collectively**. Find an aggregate negative-witness certificate, phase-sensitive partition, averaging identity or source-specific transform that benefits from the MC-273 homogeneous-shell collapse without explicitly resolving each row through a deep coordinate-query tree. Failing that, prove direct signed cancellation for the flat coefficient before positive/absolute scalarization.

## Keep rowwise normal form, conditioning complexity and endpoint cancellation separate

The existence of a negative witness simplifies one row exactly; discovering a witness for every row is a different observable and can be much more expensive in source degree. MC-274 makes that distinction exact. A future proof should state whether it controls the original flat vector, a conditioned subfamily, the unresolved all-positive subcube, or an aggregate witness statistic, and should price the source degree introduced by that choice.

The main dead ends remain unchanged: enlarging the flat source to arbitrary coefficients or replacing its signed target coefficient by a positive scalar envelope spends the blind-row budget before arithmetic cancellation is tested. The new opportunity is narrower and more structured: use the negative-witness homogeneous-shell identity without converting it into atom-scale Boolean search.