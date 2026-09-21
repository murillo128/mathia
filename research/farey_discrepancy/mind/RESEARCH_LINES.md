# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the polynomial growth window of the weighted divisibility inverse under exact omissions

**Linked intuitions:** `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`, `MI-044-finite-exact-omissions-are-triangular-response-columns-not-arbitrary-sparse-increments`, `MI-045-exact-omission-cost-is-a-harmonic-location-profile`, `MI-046-cross-scale-divisibility-not-low-location-drives-exact-omission-amplification`, `MI-047-alternating-rank-merges-create-factorial-incidence-conditioning-without-reaching-the-macroscopic-scale`, `MI-048-ordered-factorization-entropy-caps-exact-omission-conditioning`.

FD-241--FD-247 separate qualitative density-one sampling, approximate residual cost, triangular exact omission columns, harmonic support reach and the primitive-support regime. They show that defect cardinality and absolute location alone do not determine exact-omission amplification.

FD-248 identifies the exact response-side conditioning statistic. For `D=supp(Delta Y)`, the normalized divisor map is a weighted incidence-zeta matrix `W_D`; its inverse has entries `1_(q|d) mu_D(q,d) q/d`, so

`kappa(D)=||W_D^(-1)||_infty`

controls coefficient mass by `sum_(n<=N)|b_n| <= 2 C N K kappa(D)`. Antichains give `kappa=1`, and induced divisibility forests with no downward merges have `kappa<=3/2`.

FD-249 shows that one height-one high-arity merge already makes `kappa(D)` unbounded with `K=N^(o(1))`. FD-250 then proves that nested alternating rank selections can amplify far more: along an exact adjacent-pair omission family with `K=N^(o(1))`,

`log kappa(D_N) >= (1-o(1))(log log log N)(log log log log N)`,

so `kappa(D_N)` beats every fixed power of `log log N`. The factorial Möbius coefficient of a rank-selected Boolean interval survives because it is placed on a reciprocal-heavy squarefree rank.

FD-251 supplies the missing universal upper scale. Writing `rho_*>1` for the root of `zeta(rho_*)=2`, strict divisibility chains inject into ordered factorizations and give

`kappa(D) <= N^(rho_*-1+o(1))`, with `rho_*=1.7286472389...`,

for every finite induced divisibility set, even before using the genuine adjacent-pair geometry. Consequently exact omissions with `K=N^(alpha+o(1))` cannot hide coefficient-capacity-scale mass whenever `alpha<2-rho_*=0.2713527610...`; in particular every `K=N^(o(1))` family is response-side coercive.

The live exact-response question is therefore the **polynomial window**. Can the special constraint `D subset E union (E+1)` lower the universal exponent `rho_*-1`, perhaps substantially, or can one build polynomial-size omission families whose induced weighted inverse reaches a positive power of `N`? The alternating-rank mechanism is no longer decisive if it remains subpolynomial. Any candidate lower construction must now be compared directly with the ordered-factorization ceiling and with the `N/K` scale actually required for macroscopic hidden mass.

The independent source-side question remains whether positivity, finite reservoir capacity, squarefree realization or arithmetic coherence excludes the surviving signed directions. Approximate residual control remains separate from the exact-zero incidence problem.

## Separate boundary/source admissibility from interior integrality

Response-space rounding makes bulk integrality cheap once a real reservoir profile is safely inside its capacity box. The remaining discrete obstruction is source admissibility and exact defect geometry.

The exact hierarchy is now a conditioning ledger: arbitrary sparse defects pay reciprocal-divisor mass; exact omissions have triangular response columns; location bounds reachable support; primitive support diagonalizes the inverse; forest-like support keeps the weighted inverse norm uniformly bounded; one high-arity merge makes it unbounded; alternating rank-selected merges beat every fixed power of `log log N`; and ordered-factorization entropy still caps every induced-divisibility inverse by `N^(rho_*-1+o(1))`. Any future coercivity or countermodel theorem should preserve `kappa(D)` until the adjacent-pair geometry or source constraints justify a sharper reduction.