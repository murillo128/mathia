# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove phase-sensitive cancellation for the exact flat quadratic-character coefficient

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`.

MC-266--MC-269 reduce the radial/tensor description to the actual Legendre-sign source and then to the endpoint-optimal flat quadratic-character second moment

`F_t = sum_(|T|=t) |sum_(S in B_m) chi_T(q_S)|^2`,

whose diagonal scale is exactly the scale of one blind row. MC-270 proves that coefficient-uniform operator estimates cannot cross that scale because the exact matrix already has row norm `Z`.

MC-271--MC-272 close two further relaxations that still preserve the flat source vector. The nonnegative shell generating polynomial cannot isolate `F_t` below the blind scale by any positive-real majorant, and complex Cauchy extraction followed by any raw circle `L^p`/Hardy norm remains above the same threshold for every radius. The obstruction is therefore not merely generic coefficient uniformization: **positive scalar envelopes of the full shell family also erase the required gain**.

The live theorem must keep the target phase/sign structure until after extraction. Equivalent forms are direct `o(Z^2)` control of the signed off-diagonal part of `<1_Z,A^*A1_Z>`, a genuinely phase-sensitive Fourier/Cauchy coefficient estimate for the exact shell polynomial, or a source-specific relaxation whose norm floor is strictly below one blind atom. Better operator norms, nonnegative generating majorants and absolute circle norms are now known dead ends for this endpoint.

## Keep basis changes, detector efficiency, flat-vector structure and phase extraction separate

MC-267 says Krawtchouk coordinates do not create information. MC-268 says detector choice can remove artificial high-moment loss. MC-269 identifies the distinguished flat source vector. MC-270 says enlarging that vector to arbitrary coefficients spends the blind-row budget. MC-271--MC-272 say collapsing the remaining shell data to a positive scalar envelope spends the same budget even without coefficient uniformization.

The unresolved arithmetic currency is consequently narrower: signed/angular cancellation attached to the exact flat lower-prime subset family at the target shell, before absolute values or positive majorants destroy it.