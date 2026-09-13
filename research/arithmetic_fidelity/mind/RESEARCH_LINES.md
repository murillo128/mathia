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

## Classify nontorsion prime incidence and the exceptional even-support singular strata

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`, `MI-026-zero-count-fidelity-is-distance-to-the-boundary-zero-discriminant`, `MI-027-one-sided-source-constraints-replace-nullspace-rank-by-reachable-cone-geometry`, `MI-028-exact-zero-incidence-is-thinner-than-stable-access`, `MI-029-prime-phase-character-rank-exhausts-the-small-polygon-obstruction-at-the-pentagon`, `MI-030-five-prime-harmonic-rigidity-constrains-recurrence-not-first-incidence`, `MI-031-two-harmonics-recover-five-point-zero-fiber-except-torsion`, `MI-032-six-point-zero-shapes-cross-the-one-complex-coordinate-threshold`, `MI-033-parity-controls-minimal-harmonic-recovery`.

The exact-hit geometry remains stratified. Two-prime supports have exact hits, three- and four-prime supports are exactly zero-free, and from five points onward first nontorsion incidence is not decided by the elementary character-rank/Baker obstructions. Conditional on incidence, [AF-316](../findings/AF-316-parity-controls-minimal-harmonic-lift.md) gives the generic post-hit information law: odd `n=2m+1` needs `(s_2,...,s_m,E)`, while even `n=2m` needs only `(s_2,...,s_m)` on `e_m != 0`. After common-phase quotient the generic information bill is `n-3` real dimensions.

[AF-317](../findings/AF-317-antipodal-extension-recursion-breaks-six-point-singular-rigidity.md) changes the exceptional even-support question. The six-point implication `e_3=0 => global antipodal pairing` is a low-degree accident: at eight points there are exact centered, nontorsion, non-globally-antipodal configurations with `e_4=0`. Hence the six-prime singular-stratum exclusion cannot be extrapolated from self-inversivity or torsion geometry alone.

The first unresolved singular gate is now exact: on the centered eight-point fiber `s_1=0, e_4=0`, determine whether the integer-character relation lattice can have rank at most one. A rank-`0/1` witness would show that AF-310's character restriction cannot by itself remove the recovery singularity; a universal rank-at-least-two theorem would remove it for multiplicatively independent prime-log orbits. This question is already isolated in `CLUE-eight-point-middle-singular-character-rank`.

## Keep incidence, exact recovery, singular-stratum rank and conditioning separate

Generic low-harmonic identifiability is no longer the larger-support problem. The remaining currencies are first prime-log incidence, arithmetic accessibility of `e_m=0`, the character rank forced on that singular fiber, access to the odd product-phase lift, and conditioning near the exceptional set. AF-317 specifically prevents using the six-point antipodal mechanism as a substitute for the source-specific rank theorem at support eight and above.
