# MI-028 — Sparse midpoint rigidity comes from cross-coordinate multiplicativity, with the threshold set by the source fibre

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-183](../../findings/FD-183-subcritical-prime-extension-energy-forces-semiprime-scale-support.md). The quantitative relation rigidity is proved for squarefree-supported perturbations of Möbius; the sharp support threshold depends materially on whether prime coordinates are allowed to move. These are source-identifiability statements, not Franel--Landau estimates.

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while sparse geometric horizons become target-rigid inside the genuinely multiplicative squarefree source class. FD-175--FD-179 show that this rigidity is not explained by knowing primes, signs, low multiplicative ranks, or even coordinatewise agreement through essentially the entire squarefree-rank range.

For the dyadic ladder, deletion-only sources can match every sampled midpoint while agreeing with Möbius outside a subpolynomial defect set confined to an exceptionally thin high-rank shell. FD-180 first showed that such a repair cannot also make prime-extension multiplicativity too accurate. FD-181 then removed the fragile source assumptions: if `delta=a-mu`, `S=supp(delta)` and `S(x)=o(x/log x)`, with arbitrary signed amplitudes and prime coordinates allowed to move, then for the true prime-extension energy

`M_(a,q)(x)=sum_((n,pn) in E_x) |a(pn)-a(p)a(n)|^q`

one has

`liminf_(x->infinity) (log x/x) M_(a,q)(x) >= sum_(n in S) |delta(n)|^q/n`.

Thus the general sparse fibre has a first-generation prime-fan rigidity scale `x/log x`: changing enough prime labels or children can in principle screen the fan of one erroneous parent once the support budget reaches that order.

FD-183 shows that this cardinal frontier is not intrinsic to the relation itself. On the **fixed-prime fibre** `a(p)=-1`, the first generation cannot be paid for by moving the prime labels. If `n_0` is the first changed coordinate and `M_(a,q)(x)=o(x/log x)`, then

`S(x) >= (1/n_0+o(1)) x loglog x/log x`.

Equivalently, support `o(x loglog x/log x)` together with subcritical prime-extension energy forces `a=mu`. The extra `loglog x` is a second multiplicative generation: after the root fan has to remain good, its prime extensions create a semiprime-scale family of forced source coordinates. Fixing one part of the source fibre therefore changes the inverse repair geometry by an entire logarithmic factor.

This sharpens the reusable mechanism. The resource is not coefficient fidelity by itself but the **cross-coordinate boundary that must be repaired inside the declared admissible source class**. When prime coordinates may move, one fan can be screened at roughly `x/log x` cost. When primes are fixed, the repair propagates to the next multiplicative layer and costs `x loglog x/log x`. Further gains would require another forced generation or a different relation; they cannot be inferred from the same support count without proving the corresponding propagation.

The dyadic midpoint observations still do not expose this relation automatically. FD-182 gives one permanent non-Möbius source matching the complete dyadic midpoint ladder while retaining prime-extension energy at its critical fan scale. FD-183 strengthens source coercivity on a smaller fixed-prime fibre, but it does not turn midpoint accuracy into a relation-energy estimate. The observation family and the relation tariff remain separate objects.

**Boundary.** FD-183 does not prove that `x loglog x/log x` is the optimal fixed-prime threshold, does not cover dense tiny-amplitude perturbations where support counting is the wrong currency, and does not yield the RH-critical Franel--Landau discrepancy estimate. A useful continuation must either identify the next forced multiplicative generation, construct a near-threshold low-energy control, or prove that a natural Farey observation family quantitatively controls the relation energy on the exact source fibre being used.
