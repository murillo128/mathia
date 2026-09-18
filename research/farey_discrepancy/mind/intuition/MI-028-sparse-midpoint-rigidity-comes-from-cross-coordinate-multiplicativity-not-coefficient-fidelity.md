# MI-028 — Sparse midpoint rigidity comes from cross-coordinate multiplicativity, with the threshold set by the source fibre

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-188](../../findings/FD-188-subcritical-prime-extension-energy-forces-linear-lq-mass-for-moved-primes.md). The quantitative relation rigidity is proved for squarefree-supported perturbations of Möbius; the sharp currency depends materially on whether prime coordinates are fixed or allowed to move. These are source-identifiability statements, not Franel--Landau estimates.

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while sparse geometric horizons become target-rigid inside the genuinely multiplicative squarefree source class. FD-175--FD-179 show that this rigidity is not explained by knowing primes, signs, low multiplicative ranks, or even coordinatewise agreement through essentially the entire squarefree-rank range.

For the dyadic ladder, deletion-only sources can match every sampled midpoint while agreeing with Möbius outside a subpolynomial defect set confined to an exceptionally thin high-rank shell. FD-182 then makes the observation/source split quantitative: one fixed non-Möbius source matches the complete dyadic midpoint ladder exactly while its true prime-extension energy remains at the critical scale `M_(a,q)(x)=(C+o(1))x/log x`.

On the physical-prime fibre, relation rigidity is exact and finite. Put `c(n)=a(n)/mu(n)` on squarefree coordinates and assume `a(p)=-1`, so every prime is anchored by `c(p)=1`. If `n_0` is changed, with `k=omega(n_0)` and `Delta=|a(n_0)-mu(n_0)|`, FD-187 shows that each fresh prime generates the full translated divisor cube `Q_k` in parallel with the direct edge. For `q>1`, with

`B_(k,q)=1+sum_(j=0)^(k-1) [k binom(k-1,j)]^(-1/(q-1))`,

the exact `q`-capacity gives

`M_(a,q)(x) >= (pi(x/n_0)-k) Delta^q / B_(k,q)^(q-1)`.

For `q=1` the local cost is exactly `Delta`, and for fixed `q>1`, `B_(k,q)->1` as `k->infinity`. The apparent multiplicative-rank loss in a single-path proof is therefore artificial: **anchored consistency is priced by the capacity of the whole finite relation network, and parallel routes can remove depth penalties**.

FD-188 supplies the amplitude-sensitive counterpart when prime coordinates may move. Define

`D_(a,q)(x)=sum_(n<=x, mu^2(n)=1)|a(n)-mu(n)|^q`.

For a fixed moved prime `p`, `Delta_p=|a(p)+1|`, and every `lambda>0`, the fixed-`p` matching gives an exact three-variable stability inequality. For `q>1`,

`D_(a,q)(x)+lambda M_(a,q)(x) >= |E_(p,x)| Delta_p^q /(1+|a(p)|^(q')+lambda^(-1/(q-1)))^(q-1)`,

with the corresponding `l^1/l^infinity` denominator at `q=1`. Choosing `lambda=log x` shows that `M_(a,q)=o(x/log x)` forces a positive linear `D_q` tariff for every moved prime. Combining this with the physical-prime divisor-cube theorem yields

`D_(a,q)(x)=o(x)` and `M_(a,q)(x)=o(x/log x)  =>  a=mu`.

This replaces the earlier positive-density support tariff by a continuous amplitude law. Dense perturbation support is no longer an escape when its mean `q`th-power coefficient error vanishes. The one-prime multiplicative deformation with `a(p)=0` has zero relation energy and `D_q(x)=x/[zeta(2)(p+1)]+O_p(sqrt x)`, so the linear coefficient-mass scale is sharp.

The reusable picture is now a **two-currency source certificate**. Coefficient amplitude mass controls the prime-label gauge; relation-network capacity controls composite inconsistency after that gauge is fixed. Neither currency is supplied automatically by sparse Farey observation. FD-182 remains the decisive warning that an exact observation kernel can hide critical relation energy even when the source-side separator is mathematically sharp.

The live problem is therefore observation design: find a minimal Farey spatial statistic whose error controls enough of `D_q` and `M_q` with a quantitative modulus, or construct a new null source showing that the proposed augmentation still misses one of those currencies. A secondary source-side question is whether the explicit moved-prime constants remain globally sharp for every prescribed nonzero prime value, rather than only for the isolated-edge relaxation and the `a(p)=0` extremizer.

**Boundary.** The divisor-cube theorem assumes physical prime labels, while the weighted matching theorem prices departures from those labels through `D_q`; neither derives either source currency from Farey observations. The support-free classification is a source-relation theorem, not the RH-critical Franel--Landau estimate, and it does not identify the minimal spatial data needed to observe its hypotheses.