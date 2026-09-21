# MI-046 — Exact-omission amplification is the weighted divisibility inverse norm

**Evidence level:** exact divisor-poset synthesis from [FD-247](../../findings/FD-247-primitive-increment-support-gives-sharp-linear-exact-omission-cost.md) and [FD-248](../../findings/FD-248-weighted-incidence-mobius-norm-localizes-exact-omission-amplification.md). Finite-poset Möbius inversion is classical; the line-specific content is the exact-omission conditioning statistic and its coefficient-mass consequence.

Let `g=Delta Y`, `D=supp(g)∩[1,N]`, and order `D` by divisibility. On active coordinates, after normalizing `beta_d=b_d/d` and `x_d=g(d)/d`, the response inverse is

`beta = W_D x`,  with  `W_D = R^(-1) Z_D R`.

Hence

`W_D^(-1)(d,q) = 1_(q|d) mu_D(q,d) q/d`,

where `mu_D` is the Möbius function of the induced finite divisibility poset. The exact conditioning parameter is therefore

`kappa(D)=||W_D^(-1)||_infty = max_d sum_(q|d,q∈D) |mu_D(q,d)| q/d`.

Under `|b_n|<=Cn` and `K` exact omissions, `|D|<=2K` and

`sum_(n<=N)|b_n| <= C N |D| kappa(D) <= 2 C N K kappa(D)`.

This sharpens the earlier statement that cross-scale divisibility is necessary: **chains themselves are harmless**. If every nonminimal active `d` has at most one maximal proper active divisor, the induced Hasse diagram has no downward merges and `kappa(D)<=3/2`, even for arbitrarily long divisibility chains. Antichains are the special case `kappa=1`.

Conversely, macroscopic top-scale coefficient mass with `K=o(N)` forces `kappa(D) ≳ (eta/C) N/K`. Thus a bad exact-omission family must develop a quantitatively ill-conditioned incidence inverse; merely placing defects at low scale, spanning many scales, or forming deep chains is insufficient. Repeated merge geometry is the first possible source of growth, but no individual merge pattern is yet proved sufficient.

**Boundary.** This is an exact-zero signed response theorem. It does not control approximate residuals or impose physical positivity, finite prime-reservoir capacity, squarefree realization or arithmetic coherence. The next response-side question is concrete: how large can `kappa(D)` become subject to `D⊆E∪(E+1)` with `|E|=K`, and which repeated divisibility-merge patterns realize growth comparable to `N/K`?