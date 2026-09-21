# MI-048 — Ordered-factorization entropy caps exact-omission conditioning

**Evidence level:** exact divisor-poset synthesis from [FD-251](../../findings/FD-251-ordered-factorization-chain-entropy-bounds-exact-omission-conditioning.md), combined with the exact weighted incidence inverse of FD-248 and the lower constructions FD-249--FD-250. Ordered factorizations and the root `rho_*>1` of `zeta(rho_*)=2` are classical; the line-specific content is their transfer to exact-omission conditioning and the resulting coercivity threshold.

For every finite induced divisibility set `D subset {1,...,N}`, the weighted inverse norm

`kappa(D)=max_d sum_(q in D, q|d) |mu_D(q,d)| q/d`

obeys

`kappa(D) <= N^(rho_*-1+o(1))`, where `rho_*=1.7286472389...`.

The mechanism is independent of the special omission geometry. Every strict divisibility chain from `q` to `d` injects into an ordered factorization of `d/q`; the number `H(r)` of ordered factorizations satisfies `H(r)<=r^(rho_*)`, and summing `H(r)/r` over divisors gives the universal power ceiling.

Combining this with FD-248 changes the exact-response frontier. If `K` samples are omitted and `|b_n|<=C_b n`, then

`sum_(n<=N) |b_n| <= K N^(rho_*+o(1))`

up to the fixed coefficient-envelope constant. Thus every `K=N^(o(1))` omission family is coercive at the `N^2` coefficient-capacity scale, and more generally `K=N^(alpha+o(1))` is coercive whenever `alpha<2-rho_*=0.2713527610...`.

FD-250 therefore remains a real conditioning lower bound but no longer leaves open whether more elaborate subpolynomial merge geometry can hide macroscopic signed mass: it cannot. The live response-side gap is polynomial. One must either exploit the genuine adjacent-pair support constraint `D subset E union (E+1)` to lower the universal exponent, or construct polynomial-size exact omission families whose weighted inverse grows by a positive power of `N`.

**Boundary.** The chain count takes absolute values, enlarges genuine exact-omission supports to arbitrary induced divisibility sets, and may be far from sharp. It is a signed response-space theorem only. Positivity, finite prime-reservoir capacity, squarefree physical realization, full arithmetic coherence, and approximate residuals remain separate source/destination constraints.