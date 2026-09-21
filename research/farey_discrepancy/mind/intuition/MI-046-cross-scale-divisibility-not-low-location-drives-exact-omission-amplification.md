# MI-046 — Exact-omission amplification is weighted divisibility conditioning, and one high-arity merge already makes it unbounded

**Evidence level:** exact divisor-poset synthesis from [FD-247](../../findings/FD-247-primitive-increment-support-gives-sharp-linear-exact-omission-cost.md), [FD-248](../../findings/FD-248-weighted-incidence-mobius-norm-localizes-exact-omission-amplification.md), and [FD-249](../../findings/FD-249-single-high-arity-merge-forces-unbounded-incidence-conditioning.md). Finite-poset Möbius inversion and the primorial reciprocal-mass estimates are classical ingredients; the line-specific content is their exact-omission realization and conditioning consequence.

Let `g=Delta Y`, `D=supp(g)∩[1,N]`, and order `D` by divisibility. After normalizing the active divisor map, the inverse has entries

`W_D^(-1)(d,q) = 1_(q|d) mu_D(q,d) q/d`,

so the exact conditioning parameter is

`kappa(D)=||W_D^(-1)||_infty = max_d sum_(q|d,q∈D) |mu_D(q,d)| q/d`.

Under `|b_n|<=Cn` and `K` exact omissions, `|D|<=2K` and

`sum_(n<=N)|b_n| <= 2 C N K kappa(D)`.

This keeps the earlier negative controls intact: antichains have `kappa=1`, and induced divisibility forests with no downward merges have `kappa<=3/2`, so arbitrarily long chains do not by themselves create large amplification.

FD-249 shows that repeated merge depth is nevertheless unnecessary for growth. There are exact omission supports with `K=N^(o(1))` whose active divisor interval below the top point is a height-one star: all proper active divisors are pairwise incomparable and attach directly to the top. A rank-selected primorial construction gives

`kappa(D_N) >> log log N / sqrt(log log log N)`.

The growth is the reciprocal mass of one high-arity weighted antichain. Thus chain depth and repeated nested merges are not the structural threshold; **one sufficiently wide merge already makes the incidence inverse unbounded**.

This still falls far short of the scale needed to hide macroscopic coefficient mass. With `K=o(N)`, such mass forces `kappa(D) >> N/K`, while the known star construction is only polylogarithmic. The durable response-side frontier is therefore quantitative: determine the maximal growth of `kappa(D)` under the genuine adjacent-pair constraint `D⊆E∪(E+1)`, and whether nested/rank-selected merge geometries can approach the required `N/K` scale or a universal subcritical upper bound survives.

**Boundary.** These are signed exact-response statements. They do not control approximate residuals and do not impose positivity, finite prime-reservoir capacity, squarefree physical-source realization or full arithmetic coherence. Those source-side constraints remain a separate transversality question.