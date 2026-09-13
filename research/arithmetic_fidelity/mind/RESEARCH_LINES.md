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

## Separate exact prime incidence from finite-height conditioning on the eight-point singular stratum

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`, `MI-026-zero-count-fidelity-is-distance-to-the-boundary-zero-discriminant`, `MI-027-one-sided-source-constraints-replace-nullspace-rank-by-reachable-cone-geometry`, `MI-028-exact-zero-incidence-is-thinner-than-stable-access`, `MI-029-prime-phase-character-rank-exhausts-the-small-polygon-obstruction-at-the-pentagon`, `MI-030-five-prime-harmonic-rigidity-constrains-recurrence-not-first-incidence`, `MI-031-two-harmonics-recover-five-point-zero-fiber-except-torsion`, `MI-032-six-point-zero-shapes-cross-the-one-complex-coordinate-threshold`, `MI-033-parity-controls-minimal-harmonic-recovery`, `MI-035-fixed-prime-conditioning-has-zero-uniform-gap-but-a-polynomial-finite-height-modulus`.

AF-316--AF-320 isolate the eight-point middle singularity and repair exact representation on the actual eight-prime source class: at a centered common nonzero time, `e_4=0` forces `e_3!=0`, and the fifth harmonic reconstructs the product phase. AF-321 shows that relation rank alone gives no uniform conditioning margin because matched rank-one controls approach a regular octagon with `|s_3|->0`.

AF-322 now adds the source-specific metric statement that AF-321 was missing. For any fixed eight-prime support the prime orbit has **no positive uniform gap** from the four-antipodal-pair geometry, but Baker-type logarithmic lower bounds prevent approach faster than a fixed power of the time height. On an exact middle-singular hit, Łojasiewicz transfer gives a conditional polynomial lower bound for `|s_3|`, so the AF-320 inverse deteriorates at worst polynomially in height on that fixed support.

The live theorem is therefore no longer a generic conditioning question. First decide whether the actual common-time prime orbit ever meets `s_1=0,e_4=0`. If it does, determine whether the finite-height polynomial modulus is sufficient for the downstream target and whether any analogue survives uniformly as the prime support grows. Exact incidence, fixed-support conditioning and support-uniform stability must remain separate.

## Derive an equicoercive quartic profile restriction from source structure

**Linked intuition:** `MI-034-a-sub-boundary-profile-cap-makes-quartic-euler-minimization-equicoercive`.

AF-319 closes the optimizer-transfer problem once one assumes a homogeneous profile cap `Q<=C<3`: the cap is projectively compact, the normalized full Euler objective converges uniformly to the quartic homogeneous objective with `O(delta)` error, and its minimizers converge to the unique certified homogeneous optimizer. The unrestricted problem still admits escaping source shapes.

The remaining question is provenance of the non-escape resource. Can the arithmetic/source construction force a cap below the certified boundary level, or another condition strong enough to give projective equicoercivity, without inserting that restriction solely to recover the desired optimizer?

## Keep incidence, exact recovery, finite-height conditioning and support-uniform stability separate

Generic low-harmonic identifiability is no longer the larger-support problem. AF-320 repairs exact eight-prime singular representation, AF-321 proves the extracted rank-one invariant has zero uniform margin on matched controls, and AF-322 recovers a polynomial finite-height margin on each fixed rational-prime support. None settles exact middle-singular incidence or provides constants uniform over growing supports. Those are now distinct source currencies rather than variants of the same recovery theorem.