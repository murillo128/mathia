# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve growth of the weighted divisibility inverse under exact omissions

**Linked intuitions:** `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`, `MI-044-finite-exact-omissions-are-triangular-response-columns-not-arbitrary-sparse-increments`, `MI-045-exact-omission-cost-is-a-harmonic-location-profile`, `MI-046-cross-scale-divisibility-not-low-location-drives-exact-omission-amplification`, `MI-047-alternating-rank-merges-create-factorial-incidence-conditioning-without-reaching-the-macroscopic-scale`.

FD-241--FD-247 separate qualitative density-one sampling, approximate residual cost, triangular exact omission columns, harmonic support reach and the primitive-support regime. They show that defect cardinality and absolute location alone do not determine exact-omission amplification.

FD-248 identifies the exact response-side conditioning statistic. For `D=supp(Delta Y)`, the normalized divisor map is a weighted incidence-zeta matrix `W_D`; its inverse has entries `1_(q|d) mu_D(q,d) q/d`, so

`kappa(D)=||W_D^(-1)||_infty`

controls coefficient mass by `sum_(n<=N)|b_n| <= 2 C N K kappa(D)`. Antichains give `kappa=1`, and induced divisibility forests with no downward merges have `kappa<=3/2`.

FD-249 shows that one height-one high-arity merge already makes `kappa(D)` unbounded with `K=N^(o(1))`. FD-250 then proves that nested alternating rank selections can amplify far more: along an exact adjacent-pair omission family with `K=N^(o(1))`,

`log kappa(D_N) >= (1-o(1))(log log log N)(log log log log N)`,

so `kappa(D_N)` beats every fixed power of `log log N`. The factorial Möbius coefficient of a rank-selected Boolean interval survives because it is placed on a reciprocal-heavy squarefree rank.

The live exact-response question is therefore the **ultimate growth scale** permitted by `D subset E union (E+1)`. Long chains, bounded depth and fixed polylogarithmic heuristics are all insufficient controls. Can a more elaborate exact-omission geometry push `kappa(D)` toward the `N/K` scale required for sublinear omissions to hide macroscopic coefficient mass, or is there a universal subpower/subpolynomial upper bound that still keeps that scale unreachable?

The independent source-side question remains whether positivity, finite reservoir capacity, squarefree realization or arithmetic coherence excludes the surviving signed directions. Approximate residual control remains separate from the exact-zero incidence problem.

## Separate boundary/source admissibility from interior integrality

Response-space rounding makes bulk integrality cheap once a real reservoir profile is safely inside its capacity box. The remaining discrete obstruction is source admissibility and exact defect geometry.

The exact hierarchy is now a conditioning ledger: arbitrary sparse defects pay reciprocal-divisor mass; exact omissions have triangular response columns; location bounds reachable support; primitive support diagonalizes the inverse; forest-like support keeps the weighted inverse norm uniformly bounded; one high-arity merge makes it unbounded; alternating rank-selected merges beat every fixed power of `log log N`; and macroscopic hidden mass still requires the much larger `N/K` scale. Any future coercivity theorem should preserve `kappa(D)` until source constraints justify a further relaxation.