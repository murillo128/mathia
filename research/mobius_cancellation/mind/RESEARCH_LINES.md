# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove flat-vector cancellation for the exact sparse quadratic-character matrix

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`.

MC-266--MC-267 show that the radial support hierarchy is only a Krawtchouk re-expression of the actual lower-prime Legendre sign distribution. MC-268 replaces the wasteful monomial detector by the endpoint-optimal Christoffel square, and MC-269 writes its arithmetic content exactly as

`F=||A 1_Z||_2^2 = sum_(|T|=t) |sum_(S in B_m) chi_T(q_S)|^2`,

with literal diagonal `CZ`. At the useful choice `m=t+1`, excluding one blind row requires a loss strictly below `Z/C~k_y/(t+1)`.

MC-270 closes the coefficient-uniform large-sieve escape even for this exact sparse matrix. Every row of `A` has squared norm `Z`, so `||A||_op^2>=Z`. Any inequality uniform over arbitrary coefficients therefore gives at best `||A 1_Z||^2<=D Z` with `D>=Z`, exactly the `Z^2` contribution of one blind row. In the target normalization this forces `L_y>=Z/C`, while blind exclusion needs the opposite strict inequality.

The live theorem is therefore **vector-specific**: exploit the all-one source vector before any Cauchy--Schwarz/duality step enlarges it to arbitrary coefficients. Equivalently, control the signed off-diagonal part of `<1_Z,A^*A1_Z>` directly at `o(Z^2)`, or construct an admissible arithmetic configuration showing that such cancellation fails. Better operator norms, generic sparse large sieves and unrestricted coefficient duality cannot cross the threshold by themselves.

## Keep basis changes, detector efficiency, arithmetic cancellation and coefficient uniformization separate

MC-267 says Krawtchouk coordinates do not create information. MC-268 says detector choice can remove large artificial loss. MC-269 says the residual is a flat quadratic second moment. MC-270 says replacing that one flat vector by the whole coefficient space loses exactly the remaining blind-atom budget.

The unresolved arithmetic resource is therefore not “a stronger large sieve” in the usual uniform sense. It is cancellation attached to the specific flat lower-prime subset family, or another source-specific structured coefficient class whose relaxation still stays strictly below the blind-row atom.