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

## Classify rational-prime incidence and conditioning on the eight-point middle-singular stratum

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`, `MI-026-zero-count-fidelity-is-distance-to-the-boundary-zero-discriminant`, `MI-027-one-sided-source-constraints-replace-nullspace-rank-by-reachable-cone-geometry`, `MI-028-exact-zero-incidence-is-thinner-than-stable-access`, `MI-029-prime-phase-character-rank-exhausts-the-small-polygon-obstruction-at-the-pentagon`, `MI-030-five-prime-harmonic-rigidity-constrains-recurrence-not-first-incidence`, `MI-031-two-harmonics-recover-five-point-zero-fiber-except-torsion`, `MI-032-six-point-zero-shapes-cross-the-one-complex-coordinate-threshold`, `MI-033-parity-controls-minimal-harmonic-recovery`.

AF-316 gives the generic post-hit information law: odd `n=2m+1` needs `(s_2,...,s_m,E)`, while even `n=2m` needs only `(s_2,...,s_m)` on `e_m != 0`; after common-phase quotient the generic information bill is `n-3` real dimensions. AF-317--AF-318 then show that the eight-point middle singularity `e_4=0` is neither forced into six-point-style antipodal geometry nor excluded by the strongest elementary prime-phase character-rank test.

AF-320 now closes the **representation** failure on the actual eight-prime source class. At a centered common nonzero time, `e_4=0` forces `e_3 != 0`; the deeper `e_4=e_3=0` stratum would create four antipodal pairs and violate the prime-log relation-rank bound. Consequently the fifth harmonic recovers the product phase exactly,

`E = (6 s_5 - 5 s_2 s_3)/(10 conjugate(s_3))`,

so `(s_2,s_3,s_4,s_5)` globally recovers every centered eight-prime configuration. Generic recovery still needs only `(s_2,s_3,s_4)`; the extra harmonic pays only for the source-reachable singular branch.

The live eight-point question is therefore no longer whether a finite harmonic representation exists. Can the common-time rational-prime orbit actually meet `s_1=0,e_4=0`? If it can, does source arithmetic give a quantitative lower bound on `|s_3|` or another stable separation from the deeper forbidden stratum? Exact incidence and conditioning are distinct: AF-320 prevents exact denominator failure but does not prevent arbitrarily poor conditioning.

## Derive an equicoercive quartic profile restriction from source structure

**Linked intuition:** `MI-034-a-sub-boundary-profile-cap-makes-quartic-euler-minimization-equicoercive`.

AF-319 closes the optimizer-transfer problem once one assumes a homogeneous profile cap `Q<=C<3`: the cap is projectively compact, the normalized full Euler objective converges uniformly to the quartic homogeneous objective with `O(delta)` error, and its minimizers converge to the unique certified homogeneous optimizer. The unrestricted problem still admits escaping source shapes.

The remaining question is provenance of the non-escape resource. Can the arithmetic/source construction force a cap below the certified boundary level, or another condition strong enough to give projective equicoercivity, without inserting that restriction solely to recover the desired optimizer?

## Keep incidence, exact recovery, singular compatibility, conditioning and equicoercivity separate

Generic low-harmonic identifiability is no longer the larger-support problem, and AF-320 shows that even an exact singular representation can be repaired without proving the singular event absent. The remaining currencies are first prime-log incidence, arithmetic accessibility of singular fibers, quantitative conditioning near deeper forbidden strata, and source-derived non-escape conditions when asymptotic variational models are transported to the full Euler objective. Successful quartic optimizer transfer on a compact source class likewise does not establish that the source class is natural.
