# MI-028 — Sparse midpoint rigidity comes from cross-coordinate multiplicativity, with the threshold set by the source fibre

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-187](../../findings/FD-187-prime-translated-divisor-cubes-remove-the-rank-penalty-from-physical-prime-rigidity.md). The quantitative relation rigidity is proved for squarefree-supported perturbations of Möbius; the sharp escape depends materially on whether prime coordinates are allowed to move. These are source-identifiability statements, not Franel--Landau estimates.

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while sparse geometric horizons become target-rigid inside the genuinely multiplicative squarefree source class. FD-175--FD-179 show that this rigidity is not explained by knowing primes, signs, low multiplicative ranks, or even coordinatewise agreement through essentially the entire squarefree-rank range.

For the dyadic ladder, deletion-only sources can match every sampled midpoint while agreeing with Möbius outside a subpolynomial defect set confined to an exceptionally thin high-rank shell. FD-181 gives the broad sparse-fibre tariff: if `delta=a-mu`, `S=supp(delta)` and `S(x)=o(x/log x)`, then the true prime-extension energy

`M_(a,q)(x)=sum_((n,pn) in E_x) |a(pn)-a(p)a(n)|^q`

obeys

`liminf_(x->infinity) (log x/x) M_(a,q)(x) >= sum_(n in S) |delta(n)|^q/n`.

The physical-prime fibre is much more rigid. Put `c(n)=a(n)/mu(n)` on squarefree coordinates and assume `a(p)=-1`, so every prime is anchored by `c(p)=1`. FD-186 showed that one changed composite `n_0`, with `k=omega(n_0)` and `Delta=|a(n_0)-mu(n_0)|`, already creates an edge-disjoint finite consistency certificate for every fresh prime.

FD-187 identifies the exact finite geometry hidden inside that certificate. For each fresh prime `r`, the translated divisors `rd`, `d|n_0`, form the full Boolean cube `Q_k`, joined in series with the direct edge `n_0--n_0r`. For `q>1` define

`B_(k,q)=1+sum_(j=0)^(k-1) [k binom(k-1,j)]^(-1/(q-1))`.

The exact `q`-capacity of this finite network gives

`M_(a,q)(x) >= (pi(x/n_0)-k) Delta^q / B_(k,q)^(q-1)`

and hence

`liminf_(x->infinity) (log x/x) M_(a,q)(x) >= Delta^q/[n_0 B_(k,q)^(q-1)] > 0`.

For `q=1` the local cost is exactly `Delta`. For `q=2`, `B_(k,2)-1` is the antipodal effective resistance of the divisor cube. Most importantly, for every fixed `q>1`, `B_(k,q)->1` as `k->infinity`. The apparent multiplicative-rank penalty in the single-path proof was therefore an artifact of throwing away the exponentially many parallel divisor routes. High rank does not weaken the physical-prime rigidity certificate; apart from the unavoidable fresh-prime density `1/n_0`, the local cost approaches the full defect `Delta^q`.

FD-185 identifies the complementary zero-energy escape. Moving a prime coordinate can produce a genuinely multiplicative squarefree source with zero prime-extension energy, but then the changed support has positive density. Combining the moving-prime tariff with the physical-prime capacity theorem keeps the global classification

`S(x)=o(x)` and `M_(a,q)(x)=o(x/log x)  =>  a=mu`.

The reusable mechanism is now stronger than an anchored short-detour principle: **anchored multiplicative consistency should be priced by the capacity of the whole finite relation network, not by one selected path**. Parallel relation routes can remove apparent depth/rank losses even when every individual path becomes longer.

The observation problem remains separate. FD-182 supplies one permanent non-Möbius source matching the complete dyadic midpoint ladder while retaining prime-extension energy at the critical `x/log x` scale. FD-187 strengthens the source-side separator but does not make midpoint data observe it. The live questions are therefore a quantitative observation-to-relation modulus for richer Farey spatial data, the genuinely sharp critical constant/stability law once the full local capacity is used, and a weighted moving-prime sparsity currency when prime perturbation amplitudes can shrink.

**Boundary.** The divisor-cube capacity theorem assumes the physical prime labels are fixed. It does not derive relation energy from Farey observations, remove the moved-prime escape, control dense small-amplitude perturbations by support cardinality, or provide the RH-critical Franel--Landau estimate. The disappearance of the rank penalty is a source-relation result, not a destination theorem.