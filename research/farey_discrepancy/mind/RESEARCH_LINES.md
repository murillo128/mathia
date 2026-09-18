# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Push source-side rigidity into weighted amplitude stability, then expose it from Farey observations

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-028-sparse-midpoint-rigidity-comes-from-cross-coordinate-multiplicativity-not-coefficient-fidelity`.

The observation geometry is sharply source-class relative. Complete Farey fields and consecutive midpoint histories are exactly invertible over unrestricted formal sources. Sparse geometric horizons become target-rigid inside the bounded squarefree multiplicative cone, while FD-175--FD-179 construct permanent deletion-only controls that match every dyadic midpoint despite agreeing with Möbius through essentially the whole squarefree-rank range.

Prime-extension energy is now the exact source-side relation currency. For a squarefree-supported source `a`, put `delta=a-mu` and

`M_(a,q)(x)=sum_((n,pn) in E_x) |a(pn)-a(p)a(n)|^q`.

FD-182 shows that the complete dyadic midpoint ladder cannot control this relation below its critical `x/log x` scale on the broad null-source class: one fixed non-Möbius source matches every dyadic midpoint exactly while retaining `M_(a,q)(x)=(C+o(1))x/log x` with `C>0`.

Inside the physical-prime fibre `a(p)=-1`, the source relation itself is much more rigid. FD-187 identifies the exact finite certificate behind FD-186. If `n_0` is a changed squarefree composite, `k=omega(n_0)` and `Delta=|a(n_0)-mu(n_0)|`, every fresh prime generates a translated divisor cube in parallel with the direct edge. Its exact `q`-capacity gives, for `q>1`,

`M_(a,q)(x) >= (pi(x/n_0)-k) Delta^q / B_(k,q)^(q-1)`,

where `B_(k,q)=1+sum_(j=0)^(k-1)[k binom(k-1,j)]^(-1/(q-1))`, while for `q=1` the local cost is exactly `Delta`. Since `B_(k,q)->1` at fixed `q>1`, the apparent high-rank penalty was a one-path artefact: parallel multiplicative routes make subcritical `M_(a,q)=o(x/log x)` fully rigid on the physical-prime fibre.

FD-188 removes support cardinality from the complementary moved-prime problem. Define the coefficient amplitude mass

`D_(a,q)(x)=sum_(n<=x, mu^2(n)=1) |a(n)-mu(n)|^q`.

For a fixed moved prime `p`, with `Delta_p=|a(p)+1|`, the fixed-`p` matching and the exact edge identity give, for `q>1`,

`D_(a,q)(x)+lambda M_(a,q)(x) >= |E_(p,x)| Delta_p^q / (1+|a(p)|^(q')+lambda^(-1/(q-1)))^(q-1)`,

with the corresponding `l^1/l^infinity` formula at `q=1`. Since `|E_(p,x)|=x/[zeta(2)(p+1)]+O_p(sqrt x)`, subcritical relation energy forces positive linear coefficient mass for every nonzero prime error. Combining this with FD-187 yields the support-free classification

`D_(a,q)(x)=o(x)` and `M_(a,q)(x)=o(x/log x)  =>  a=mu`.

The linear `D_q` scale is real rather than an artefact: the exact multiplicative one-prime deformation with `a(p)=0` has `M=0` and `D_q(x)=x/[zeta(2)(p+1)]+O_p(sqrt x)`. Source identification therefore has two distinct currencies: coefficient fidelity fixes the prime-label gauge, while prime-extension energy fixes composite consistency once that gauge is anchored.

The high-value frontier is now observation-side. What minimal additional Farey spatial statistic destroys the FD-179 dyadic kernel and quantitatively controls enough of `D_q` and `M_q` to cross their exact source-side thresholds? Complete fields are source-invertible but vastly stronger than needed; the interesting object is an intermediate observation family with a provable modulus. A secondary source-side question is whether the explicit moved-prime constants are globally sharp for prescribed nonzero `a(p)`, where simultaneous multiplicative consistency may impose more cost than the isolated-edge convex relaxation.

Inside the genuinely multiplicative cone, the finite certification bound for geometric ladders remains quantitatively crude and may admit sharper orbit-hitting estimates. Pairwise sparse inversion also remains distinct from one-target rigidity.

## Apply information budgets only after fixing source class, observation family and destination

The same midpoint coordinate can encode the full source when observed through changing consecutive horizons, become sparse-target-rigid under multiplicativity, and retain a permanent kernel under deletion-only sources that are coordinatewise indistinguishable from Möbius outside an `o(first-correction)` extremal cap. The source-side relation theorem is now stronger still: on the physical-prime fibre, finite divisor-cube capacity makes subcritical relation energy rigid with no support assumption, while on the unrestricted prime-coordinate fibre FD-188 replaces cardinal support by a quantitative `L^q` amplitude tariff.

Any lower bound should therefore first declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; whether changing horizon counts as a new operator; the source class and which coordinates are fixed or allowed to move; the relation graph and normalization; the observation/noise topology; and whether support cardinality or weighted amplitude mass is the relevant fidelity currency. Only then do rank, sample count, inverse modulus, support cardinality or information capacity become meaningful.

## Keep source coercivity and the Franel--Landau destination separate

The results above concern recovery or non-rigidity of the coefficient source. They do not prove the RH-critical discrepancy estimate. FD-188 makes this separation especially explicit: `D_q` is an additional source-fidelity observable, not a quantity derived from Farey discrepancy. Even a source condition that kills every midpoint repair must still be shown to control the nonlocal Franel--Landau norm with the required scale and conditioning.

Conversely, FD-182 rules out a dyadic-midpoint-to-prime-extension bridge on a broad nonmultiplicative source class, while FD-187--FD-188 make the two source currencies exact enough to state what a successful richer observation theorem would have to control. The missing theorem is therefore not more source identification in disguise; it is a quantitative observation-to-source bridge followed by the separate destination estimate.