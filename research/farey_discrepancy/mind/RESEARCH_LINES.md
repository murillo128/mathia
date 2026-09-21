# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve growth of the weighted divisibility inverse under exact omissions

**Linked intuitions:** `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`, `MI-044-finite-exact-omissions-are-triangular-response-columns-not-arbitrary-sparse-increments`, `MI-045-exact-omission-cost-is-a-harmonic-location-profile`, `MI-046-exact-omission-amplification-is-the-weighted-divisibility-inverse-norm`.

FD-241--FD-247 separate qualitative density-one sampling, approximate residual cost, triangular exact omission columns, harmonic support reach and the primitive-support regime. They show that defect cardinality and absolute location alone do not determine exact-omission amplification.

FD-248 identifies the exact response-side conditioning statistic. For `D=supp(Delta Y)`, the normalized divisor map is a weighted incidence-zeta matrix `W_D`; its inverse has entries `1_(q|d) mu_D(q,d) q/d`, so

`kappa(D)=||W_D^(-1)||_infty`

controls coefficient mass by `sum_(n<=N)|b_n| <= 2 C N K kappa(D)`. Antichains give `kappa=1`, and every induced divisibility forest with no downward merges has `kappa<=3/2`; in particular arbitrarily long chains remain only `O(NK)`.

The live exact-response question is now sharply localized: with `D⊆E∪(E+1)` and `|E|=K`, how large can `kappa(D)` become, and which repeated merge patterns make the weighted incidence Möbius norm grow? A sublinear omission family carrying macroscopic coefficient mass requires `kappa(D)≳N/K`, so a useful bad construction must exhibit that scale of conditioning rather than merely cross-scale support.

The independent source-side question remains whether positivity, finite reservoir capacity, squarefree realization or arithmetic coherence excludes the surviving signed directions. Approximate residual control remains separate from the exact-zero incidence problem.

## Separate boundary/source admissibility from interior integrality

Response-space rounding makes bulk integrality cheap once a real reservoir profile is safely inside its capacity box. The remaining discrete obstruction is source admissibility and exact defect geometry.

The exact hierarchy is now a conditioning ledger: arbitrary sparse defects pay reciprocal-divisor mass; exact omissions have triangular response columns; location bounds reachable support; primitive support diagonalizes the inverse; forest-like support keeps the weighted inverse norm uniformly bounded; and only genuinely growing incidence-Möbius conditioning can exceed the linear `NK` scale. Any future coercivity theorem should preserve `kappa(D)` until source constraints justify a further relaxation.