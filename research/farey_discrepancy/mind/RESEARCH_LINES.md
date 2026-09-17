# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Push quantitative prime-extension rigidity to the source-fibre-dependent sparsity boundary

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-028-sparse-midpoint-rigidity-comes-from-cross-coordinate-multiplicativity-not-coefficient-fidelity`.

The observation geometry is sharply source-class relative. Complete Farey fields and consecutive midpoint histories are exactly invertible over unrestricted formal sources. Sparse geometric horizons become target-rigid inside the bounded squarefree multiplicative cone, while FD-175--FD-179 construct permanent deletion-only controls that match every dyadic midpoint despite agreeing with Möbius through essentially the whole squarefree-rank range.

FD-180 identified the first quantitative cross-coordinate separator for those deletion-only controls. FD-181 removes the fragile parts of that statement. For an arbitrary squarefree-supported source `a`, put `delta=a-mu`, let `S` be the support of `delta`, and define the true prime-extension energy

`M_(a,q)(x)=sum_((n,pn) in E_x) |a(pn)-a(p)a(n)|^q`.

If `S(x)=o(x/log x)`, with arbitrary signed amplitudes and even allowing prime coordinates themselves to move, then

`liminf_(x->infinity) (log x/x) M_(a,q)(x) >= sum_(n in S) |delta(n)|^q/n`.

Consequently an `o((log x loglog x)^(-1/q))` normalized finite-`L^q` relation defect forces `a=mu`. On the bounded subpolynomial fibre with physical primes, the lower bound is an exact first-order asymptotic and recovers FD-180 with the weighted reciprocal perturbation mass in place of deletion count.

FD-182 closes one possible route for making that separator source-native. Composing the permanent dyadic-null source of FD-179 with the exact FD-181 asymptotic gives one fixed non-Möbius source for which every dyadic midpoint agrees exactly with Möbius while

`M_(a,q)(x)=(C+o(1)) x/log x`

for a constant `C>0`. Thus the complete dyadic midpoint ladder cannot by itself control prime-extension energy below the critical fan scale. The missing bridge must use richer Farey spatial observations, or a source class that already excludes the FD-179 kernel.

FD-183 showed that the apparent `x/log x` support frontier belongs to the **moving-prime source fibre**, not to prime-extension multiplicativity in isolation. If the prime coordinates are fixed exactly, `a(p)=-1`, and `n_0` is the first changed coordinate, then subcritical energy `M_(a,q)(x)=o(x/log x)` already forces a semiprime-scale family of changed coordinates.

FD-184 propagates that mechanism through every fixed multiplicative rank, but FD-186 shows that this growing-rank route is unnecessary for the physical-prime classification. Write `c(n)=a(n)/mu(n)` on squarefree coordinates. When `a(p)=-1`, every prime is anchored by `c(p)=1`, and one changed composite `n_0` with `Delta=|a(n_0)-mu(n_0)|>0` creates, for each fresh prime `r`, an edge-disjoint finite detour from the anchored prime `r` to `n_0r`. Hölder on the `omega(n_0)+1` edges gives

`M_(a,q)(x) >= (pi(x/n_0)-omega(n_0)) Delta^q/(omega(n_0)+1)^(q-1)`,

hence

`liminf_(x->infinity) (log x/x) M_(a,q)(x) >= Delta^q/(n_0(omega(n_0)+1)^(q-1)) > 0`.

So `M_(a,q)(x)=o(x/log x)` already forces `a=mu` on the entire physical-prime squarefree fibre, with no perturbation-support hypothesis and no growing-rank uniformity problem.

FD-185 supplies the complementary moving-prime tariff. If a prime coordinate `p` is moved by `Delta_p=|a(p)+1|>0`, then

`S(x) >= x/(zeta(2)(p+1)) - M_(a,q)(x)/Delta_p^q + O_p(sqrt(x))`.

The tariff is sharp: changing only that prime coordinate gives zero prime-extension energy and exactly the corresponding positive-density support. Combining FD-185 with FD-186 yields the clean global sparse classification

`S(x)=o(x)` and `M_(a,q)(x)=o(x/log x)  =>  a=mu`.

The main source-side questions are now quantitative rather than rank-uniform. On the physical-prime fibre, determine the sharp critical-energy constant or a useful stability modulus. On the unrestricted prime-coordinate fibre, understand weighted substitutes for support sparsity when moved-prime amplitudes or dense perturbations become small enough that cardinal support is the wrong currency.

A second live question is observation design rather than midpoint refinement: what minimal additional Farey spatial data destroys the FD-179 dyadic kernel and quantitatively exposes prime-extension relations? Complete fields are source-invertible but vastly stronger than needed; the interesting target is an intermediate observation family with a provable relation-energy modulus on the declared source fibre.

Inside the genuinely multiplicative cone, the finite certification bound for geometric ladders remains quantitatively crude and may admit sharper orbit-hitting estimates. Pairwise sparse inversion also remains distinct from one-target rigidity.

## Apply information budgets only after fixing source class, observation family and destination

The same midpoint coordinate can encode the full source when observed through changing consecutive horizons, become sparse-target-rigid under multiplicativity, and retain a permanent kernel under deletion-only sources that are coordinatewise indistinguishable from Möbius outside an `o(first-correction)` extremal cap. FD-180--FD-186 sharpen the separation further: exact dyadic-null data can coexist with critical prime-extension defect, while the relation itself becomes fully rigid at subcritical energy on the physical-prime fibre by a finite anchored detour certificate. Allowing prime coordinates to move restores a zero-energy escape, but FD-185 prices it by positive-density support. Hence “approximately multiplicative” is not inferable from midpoint accuracy, and even a valid relation tariff is meaningless without its source-fibre, amplitude and support quantifiers.

Any lower bound should first declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; whether changing horizon counts as a new operator; the source class and which coordinates are fixed or allowed to move; the relation graph and normalization; the observation/noise topology; and whether support cardinality or a weighted amplitude notion is the relevant sparsity currency. Only then do rank, sample count, inverse modulus, support cardinality or information capacity become meaningful currencies.

## Keep source coercivity and the Franel--Landau destination separate

The results above concern recovery or non-rigidity of the coefficient source. They do not prove the RH-critical discrepancy estimate. Even a source condition that kills every sparse midpoint repair must still be shown to control the nonlocal Franel--Landau norm with the required scale and conditioning. Conversely, FD-182 rules out only a dyadic-midpoint-to-prime-extension bridge on a broad nonmultiplicative source class; FD-186 makes the relation theorem exact on the physical-prime fibre but supplies no missing observation-to-relation bridge.
