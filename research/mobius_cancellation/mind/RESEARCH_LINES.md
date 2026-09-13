# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove arithmetic cancellation in the Legendre sign distribution at support-matched moment depth

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`.

The conductor and fixed-order algebraic escapes are largely exhausted. Full shell generation would require an all-class smooth-representative theorem near the logarithmic generator cutoff, while the growing-order quadratic-large-sieve route loses its saving before the first possible blind support.

[MC-264](../findings/MC-264-support-matched-high-moment-blind-threshold.md) identifies the viable amplification scale: at the first unresolved support `t~(1/log 2)log log y`, moment order `2(t+1)` crosses the single-blind-atom threshold with large slack. [MC-265](../findings/MC-265-even-support-central-krawtchouk-balance-obstruction.md) rules out the first-order-balance shortcut, and [MC-266](../findings/MC-266-tensor-pair-krawtchouk-radial-source-walk-collapse.md) collapses the tensor-pair geometry to the finite support hierarchy `H_2,H_4,...,H_(2m)`.

[MC-267](../findings/MC-267-krawtchouk-source-hierarchy-amplitude-duality.md) now closes the purely algebraic recurrence escape. The support hierarchy is exactly the Krawtchouk transform of the Hamming-weight histogram of the original lower-prime Legendre sign vectors; through degree `2m`, the even `H_s` are triangularly equivalent to the corresponding even shell-amplitude moments. Universal Krawtchouk recurrence, orthogonality, Hamming-scheme identities and radial source-walk algebra therefore only change basis. They do not create the missing high-moment saving.

The live theorem must use arithmetic information about the actual Legendre sign image. Equivalent targets include signed cancellation in selected `H_s`, a distribution theorem for the Hamming histogram `A_(y,t)(b)`, a non-radial constraint on the sign vectors, or direct control of the exact weighted mixture at `m=t+1`. The representation may be chosen for convenience, but the gain must not be derivable from universal Krawtchouk identities alone.

## Keep change of basis separate from new arithmetic information

MC-266 removes arbitrary tensor-pair geometry as an independent resource; MC-267 goes further and shows that the radial source hierarchy carries exactly the same scalar-distribution information as the amplitude histogram. Raw masses of nontrivial layers can still be much larger than the diagonal, so absolute-value control remains unusable.

This does not rule out proving an estimate for `H_s`. It changes the burden of proof: a successful support-layer theorem must exploit arithmetic structure of products of lower-prime Legendre characters, not merely the fact that those layers satisfy the classical Krawtchouk recurrence. Future work should identify the arithmetic input explicitly before treating a transformed basis as progress.
