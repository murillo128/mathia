# MI-028 — Sparse midpoint rigidity comes from cross-coordinate multiplicativity, with the threshold set by the source fibre

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-184](../../findings/FD-184-subcritical-prime-extension-energy-forces-every-fixed-almost-prime-layer.md). The quantitative relation rigidity is proved for squarefree-supported perturbations of Möbius; the sharp support threshold depends materially on whether prime coordinates are allowed to move. These are source-identifiability statements, not Franel--Landau estimates.

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while sparse geometric horizons become target-rigid inside the genuinely multiplicative squarefree source class. FD-175--FD-179 show that this rigidity is not explained by knowing primes, signs, low multiplicative ranks, or even coordinatewise agreement through essentially the entire squarefree-rank range.

For the dyadic ladder, deletion-only sources can match every sampled midpoint while agreeing with Möbius outside a subpolynomial defect set confined to an exceptionally thin high-rank shell. FD-180 first showed that such a repair cannot also make prime-extension multiplicativity too accurate. FD-181 then removed the fragile source assumptions: if `delta=a-mu`, `S=supp(delta)` and `S(x)=o(x/log x)`, with arbitrary signed amplitudes and prime coordinates allowed to move, then for the true prime-extension energy

`M_(a,q)(x)=sum_((n,pn) in E_x) |a(pn)-a(p)a(n)|^q`

one has

`liminf_(x->infinity) (log x/x) M_(a,q)(x) >= sum_(n in S) |delta(n)|^q/n`.

Thus the general sparse fibre has a first-generation prime-fan rigidity scale `x/log x`: changing enough prime labels or children can in principle screen the fan of one erroneous parent once the support budget reaches that order.

FD-183 showed that this cardinal frontier is not intrinsic to the relation itself. On the **fixed-prime fibre** `a(p)=-1`, the first generation cannot be paid for by moving the prime labels. If `n_0` is the first changed coordinate and `M_(a,q)(x)=o(x/log x)`, then support must already reach the semiprime scale `x loglog x/log x`.

FD-184 proves that the semiprime layer is not terminal. For every fixed integer `r>=1`, the same subcritical energy assumption forces

`S(x) >= (1/(n_0 (r-1)!)+o(1)) x (loglog x)^(r-1)/log x`.

The mechanism is a fixed-depth path-stability recurrence together with an exceptional-prefix convolution lemma: if the terminal descendant remains unchanged, one edge on its canonical multiplicative path must carry a fixed defect, while an `o(T/log T)` set of bad prefixes remains negligible after convolution with any fixed number of additional primes. Landau's fixed-rank asymptotic then shows that asymptotically almost every eligible rank-`r` descendant is forced into the perturbation support.

Consequently, on the fixed-prime fibre the support tariff beats **every fixed power of `loglog x`** above `x/log x`. This changes the reusable mechanism again. Fixing part of the source does not merely add one extra multiplicative generation; it makes every *fixed* multiplicative depth coercive. The remaining source-side boundary is a uniformity problem: the constants, path threshold and almost-prime asymptotics all deteriorate with `r`, so FD-184 does not permit `r=r(x)`. The live question is whether that deterioration can be controlled far enough into growing rank to force a near-linear support tariff, or whether a construction can exploit it.

The dyadic midpoint observations still do not expose this relation automatically. FD-182 gives one permanent non-Möbius source matching the complete dyadic midpoint ladder while retaining prime-extension energy at its critical fan scale. FD-184 strengthens source coercivity on the narrower fixed-prime fibre, but it does not turn midpoint accuracy into a relation-energy estimate. The observation family and the relation tariff remain separate objects.

**Boundary.** FD-184 is fixed-rank only and supplies no uniform theorem for `r=r(x)`. It does not improve the moving-prime `x/log x` frontier, cover dense tiny-amplitude perturbations where support counting is the wrong currency, or yield the RH-critical Franel--Landau discrepancy estimate. A useful continuation must either obtain growing-rank control on the fixed-prime fibre, construct a near-threshold low-energy control on the moving-prime fibre, or prove that a natural Farey observation family quantitatively controls prime-extension energy on the exact source fibre being used.
