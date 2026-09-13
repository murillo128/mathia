# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the support-matched signed Krawtchouk cancellation theorem or the surviving blind source mode

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`.

The conductor and fixed-order algebraic escapes are largely exhausted. Full shell generation is equivalent to an all-class smooth-representative theorem at generator cutoff `y=(1+o(1))log R`, far below generic polynomial generator scales, and the growing-order quadratic-large-sieve route loses its saving before the first possible blind support.

[MC-264](../findings/MC-264-support-matched-high-moment-blind-threshold.md) identifies a viable amplification scale: moment order `2(t+1)` crosses the single-blind-atom threshold with large slack at the live support `t~(1/log 2)log log y`. The unresolved analytic object is the fixed-weight Krawtchouk expansion of the tensor family.

[MC-265](../findings/MC-265-even-support-central-krawtchouk-balance-obstruction.md) now rules out a broad simplification of that target. Even at **perfect first-order Hamming balance**, the central even Krawtchouk coefficient is of size roughly `(t/N)^(t/2)`, super-polynomially larger than the pointwise kernel scale that a termwise absolute-value proof would require. Therefore “every Legendre product character is balanced on the shell” is not enough.

The live theorem must instead exploit the **signed weighted distance distribution** before absolute values are taken, prove concentration near suitable Krawtchouk zeros at the required order, or obtain the sparse fixed-weight high moment by another family-specific argument. The alternative exits remain logarithmic all-class generation or direct source-scale control of the single surviving blind character.

## Keep support order, family entropy, moment amplification and signed high-order balance separate

A smaller conductor does not improve the source exponent if the projector pays the same factor. Low-order or first-order balance does not control the fixed-weight transform at support order `t`. Conversely, MC-264 shows that the shell family is not doomed by cardinality: the extra tensor power makes one blind atom detectable. The missing resource is specifically **high-order signed cancellation in the exact shell family**, not another generic pseudorandomness estimate on a larger ensemble.
