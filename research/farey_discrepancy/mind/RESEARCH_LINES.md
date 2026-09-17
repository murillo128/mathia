# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Push quantitative prime-extension rigidity to its real sparsity boundary

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-028-sparse-midpoint-rigidity-comes-from-cross-coordinate-multiplicativity-not-coefficient-fidelity`.

The observation geometry is sharply source-class relative. Complete Farey fields and consecutive midpoint histories are exactly invertible over unrestricted formal sources. Sparse geometric horizons become target-rigid inside the bounded squarefree multiplicative cone, while FD-175--FD-179 construct permanent deletion-only controls that match every dyadic midpoint despite agreeing with Möbius through essentially the whole squarefree-rank range.

FD-180 identified the first quantitative cross-coordinate separator for those deletion-only controls. FD-181 removes the fragile parts of that statement. For an arbitrary squarefree-supported source `a`, put `delta=a-mu`, let `S` be the support of `delta`, and define the true prime-extension energy

`M_(a,q)(x)=sum_((n,pn) in E_x) |a(pn)-a(p)a(n)|^q`.

If `S(x)=o(x/log x)`, with arbitrary signed amplitudes and even allowing prime coordinates themselves to move, then

`liminf_(x->infinity) (log x/x) M_(a,q)(x) >= sum_(n in S) |delta(n)|^q/n`.

Consequently an `o((log x loglog x)^(-1/q))` normalized finite-`L^q` relation defect forces `a=mu`. On the bounded subpolynomial fibre with physical primes, the lower bound is an exact first-order asymptotic and recovers FD-180 with the weighted reciprocal perturbation mass in place of deletion count.

FD-182 now closes one possible route for making that separator source-native. Composing the permanent dyadic-null source of FD-179 with the exact FD-181 asymptotic gives one fixed non-Möbius source for which every dyadic midpoint agrees exactly with Möbius while

`M_(a,q)(x)=(C+o(1)) x/log x`

for a constant `C>0`. Thus the complete dyadic midpoint ladder cannot by itself control prime-extension energy below the critical fan scale. The missing bridge must use richer Farey spatial observations, or a source class that already excludes the FD-179 kernel; no sharper inequality built only from the same dyadic midpoint data can yield the `o(x/log x)` relation estimate required for rigidity.

The live source question remains the actual prime-fan cardinal threshold. Is `S(x)=o(x/log x)` close to optimal? At support size comparable to `x/log x`, a source has enough changed coordinates in principle to corrupt an entire prime fan. Constructing a control there with subcritical relation energy, or proving that some stronger arithmetic obstruction survives, would identify the true cardinal threshold. Dense but tiny-amplitude perturbations require a weighted replacement for support sparsity and are a separate escape.

A second live question is now observation design rather than midpoint refinement: what minimal additional Farey spatial data destroys the FD-179 dyadic kernel and quantitatively exposes prime-extension relations? Complete fields are source-invertible but vastly stronger than needed; the interesting target is an intermediate observation family with a provable relation-energy modulus.

Inside the genuinely multiplicative cone, the finite certification bound for geometric ladders remains quantitatively crude and may admit sharper orbit-hitting estimates. Pairwise sparse inversion also remains distinct from one-target rigidity.

## Apply information budgets only after fixing source class, observation family and destination

The same midpoint coordinate can encode the full source when observed through changing consecutive horizons, become sparse-target-rigid under multiplicativity, and retain a permanent kernel under deletion-only sources that are coordinatewise indistinguishable from Möbius outside an `o(first-correction)` extremal cap. FD-180--FD-182 add a sharper separation: exact dyadic-null data can coexist with prime-extension defect exactly at the `(log x loglog x)^(-1/q)` normalized coercive boundary. Hence “approximately multiplicative” is not inferable from midpoint accuracy without an explicit observation-to-relation theorem.

Any lower bound should first declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; whether changing horizon counts as a new operator; the source class and its cross-coordinate laws; the relation graph and normalization; and the observation/noise topology. Only then do rank, sample count, inverse modulus or information capacity become meaningful currencies.

## Keep source coercivity and the Franel--Landau destination separate

The results above concern recovery or non-rigidity of the coefficient source. They do not prove the RH-critical discrepancy estimate. Even a source condition that kills every sparse midpoint repair must still be shown to control the nonlocal Franel--Landau norm with the required scale and conditioning. Conversely, FD-182 rules out only a dyadic-midpoint-to-prime-extension bridge on a broad nonmultiplicative source class; it does not rule out a bridge from richer Farey observations or a destination theorem using a genuinely different source-native relation.
