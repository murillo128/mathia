# MI-028 — Sparse midpoint rigidity comes from cross-coordinate multiplicativity, with the threshold set by the source fibre

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-186](../../findings/FD-186-prime-detour-cycles-make-physical-prime-subcritical-energy-rigid.md). The quantitative relation rigidity is proved for squarefree-supported perturbations of Möbius; the sharp escape depends materially on whether prime coordinates are allowed to move. These are source-identifiability statements, not Franel--Landau estimates.

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while sparse geometric horizons become target-rigid inside the genuinely multiplicative squarefree source class. FD-175--FD-179 show that this rigidity is not explained by knowing primes, signs, low multiplicative ranks, or even coordinatewise agreement through essentially the entire squarefree-rank range.

For the dyadic ladder, deletion-only sources can match every sampled midpoint while agreeing with Möbius outside a subpolynomial defect set confined to an exceptionally thin high-rank shell. FD-180 first showed that such a repair cannot also make prime-extension multiplicativity too accurate. FD-181 then removed the fragile source assumptions: if `delta=a-mu`, `S=supp(delta)` and `S(x)=o(x/log x)`, with arbitrary signed amplitudes and prime coordinates allowed to move, then for the true prime-extension energy

`M_(a,q)(x)=sum_((n,pn) in E_x) |a(pn)-a(p)a(n)|^q`

one has

`liminf_(x->infinity) (log x/x) M_(a,q)(x) >= sum_(n in S) |delta(n)|^q/n`.

Thus the general sparse fibre has a first-generation prime-fan rigidity scale `x/log x`: changing enough prime labels or children can in principle screen the fan of one erroneous parent once the support budget reaches that order.

FD-183--FD-184 showed why fixing the prime coordinates changes the geometry. If `a(p)=-1`, a defect cannot be screened by moving the prime labels, and subcritical relation energy propagates through every fixed almost-prime rank. That route suggested a growing-rank uniformity problem, but FD-186 proves that the fixed-rank bootstrap is not the real obstruction.

On the physical-prime fibre define `c(n)=a(n)/mu(n)` on squarefree coordinates, so every prime satisfies `c(p)=1` and

`|a(pn)-a(p)a(n)|=|c(pn)-c(n)|`.

If `n_0` is any changed squarefree coordinate, `k=omega(n_0)` and `Delta=|a(n_0)-mu(n_0)|`, then every fresh prime `r` gives two routes to `n_0r`: the direct edge `n_0 -> n_0r` and a `k`-edge path from the anchored prime `r` obtained by adjoining the prime factors of `n_0`. The triangle inequality followed by Hölder forces at least

`Delta^q/(k+1)^(q-1)`

of `L^q` edge energy on that finite detour. Distinct fresh primes give edge-disjoint detours, hence

`M_(a,q)(x) >= (pi(x/n_0)-k) Delta^q/(k+1)^(q-1)`

and therefore

`liminf_(x->infinity) (log x/x) M_(a,q)(x) >= Delta^q/(n_0(k+1)^(q-1)) > 0`.

So on the physical-prime fibre `M_(a,q)(x)=o(x/log x)` already forces `a=mu`, with no support hypothesis and no rank-uniformity limit. The reusable mechanism is an **anchored finite-cycle consistency certificate**: a changed vertex and a large anchored generator layer create many edge-disjoint short detours, so local relation inconsistency becomes extensive without pushing the defect to growing depth.

FD-185 identifies the only zero-energy escape left by the relation itself. Moving one prime coordinate produces a genuinely multiplicative squarefree source with zero prime-extension energy, but the changed support then has positive density. Quantitatively,

`S(x) >= x/(zeta(2)(p+1)) - M_(a,q)(x)/Delta_p^q + O_p(sqrt(x))`.

Combining this with FD-186 gives

`S(x)=o(x)` and `M_(a,q)(x)=o(x/log x)  =>  a=mu`.

The dyadic midpoint observations still do not expose this relation automatically. FD-182 gives one permanent non-Möbius source matching the complete dyadic midpoint ladder while retaining prime-extension energy at its critical fan scale. The source-side relation theorem is now stronger, but the observation-to-relation bridge remains absent.

**Boundary.** FD-186 is critical-scale rather than a sharp-constant theorem, and relation energy alone cannot eliminate moved-prime multiplicative sources without an additional support/amplitude condition. The finite detour argument does not derive prime-extension energy from Farey observations, does not provide the RH-critical Franel--Landau estimate, and does not settle the right weighted replacement for support sparsity when moved-prime or dense perturbation amplitudes tend to zero. A useful continuation should therefore target either a quantitative observation-to-relation modulus on a declared source fibre, a sharp/stable version of the critical detour tariff, or a weighted moving-prime sparsity principle.