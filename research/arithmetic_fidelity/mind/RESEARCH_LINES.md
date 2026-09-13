# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source sign complexity to a quantitative finite-order Euler modulus

**Linked intuition:** `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`.

The ordered sign-complexity results force real source structure, but the live theorem is still quantitative: relate that sign budget to a separation or curvature modulus at the shrinking Euler-log resolution actually consumed downstream. A qualitative sign pattern or a modulus measured at the wrong scale is not enough.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`.

Localization, contraction and lifting can move information without making it cheaper in the metric used by the final theorem. A useful compression claim needs both a genuinely smaller target geometry and a theorem that the downstream argument consumes only that target rather than the hidden source detail used to construct it.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Classify nontorsion prime incidence separately from post-incidence recovery

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`, `MI-026-zero-count-fidelity-is-distance-to-the-boundary-zero-discriminant`, `MI-027-one-sided-source-constraints-replace-nullspace-rank-by-reachable-cone-geometry`, `MI-028-exact-zero-incidence-is-thinner-than-stable-access`, `MI-029-prime-phase-character-rank-exhausts-the-small-polygon-obstruction-at-the-pentagon`, `MI-030-five-prime-harmonic-rigidity-constrains-recurrence-not-first-incidence`, `MI-031-two-harmonics-recover-five-point-zero-fiber-except-torsion`, `MI-032-six-point-zero-shapes-cross-the-one-complex-coordinate-threshold`.

The exact-hit geometry is now sharply stratified. Fixed saturated prime supports can approach zero arbitrarily closely, while two-prime supports have exact hits and three- and four-prime supports are exactly zero-free. At five points, integer-character rank and Baker-type algebraic-linear obstructions stop short of first incidence; conditional on a hit, the next harmonics do not repeat the hit and `(F_P(2t),F_P(3t))` exactly recovers the phase multiset. After quotienting common phase, one complex invariant `kappa=F_P(2t)^3/F_P(3t)^2` recovers the complete five-point shape.

[AF-315](../findings/AF-315-six-point-zero-shapes-need-three-real-harmonic-coordinates.md) identifies the next information threshold exactly. On the centered six-point unit-circle zero fiber, `(s_2,s_3)` still reconstructs the unordered multiset on `s_3!=0`, but the generic shape quotient has real dimension `3`. The complete quotient coordinate `( |s_3|, s_2^3/s_3^2 )` is therefore dimension-tight, while one complex scalar is generically impossible. For distinct rational primes, any hypothetical nonzero six-prime hit automatically has both `F_P(2t)` and `F_P(3t)` nonzero, so the source lies in this faithful stratum.

The unresolved arithmetic problem remains **first nontorsion incidence**: decide whether the prime-log one-parameter orbit can meet the centered polygon-zero cone at all once the small torsion/algebraic-linear obstructions have been exhausted. Post-hit recurrence, exact recovery and quotient compression no longer substitute for that theorem. In parallel, for larger supports determine whether a bounded low-harmonic family remains exactly separating and whether its quotient coordinate count tracks the generic shape dimension; keep this representation problem distinct from incidence.

## Treat information bills as separate resources

Local degree, prime breadth, sample count, nuisance gauge, quotient dimension, exact recoverability, conditioning, exact failure incidence, character/algebraic relation rank, recurrence and first-incidence non-vacuity are not interchangeable. The five-to-six-point transition now gives an explicit calibration: the same two raw harmonics can remain exactly sufficient while the minimal continuous quotient representation grows from two to three real coordinates.