# MI-024 — Exact cyclotomic recovery can be algebraically lossless while ordinary Fourier stability appears only at the classical linear major-arc scale

**Evidence level:** exact cyclotomic injectivity and quantitative prime-packet conditioning boundary from [PC-306](../../findings/PC-306-prime-polygon-centroid-is-algebraically-lossless-but-topologically-unstable.md), [PC-307](../../findings/PC-307-polylog-oriented-prime-packets-require-near-qlogq-conditioning.md) and [PC-308](../../findings/PC-308-ordinary-oriented-fourier-packets-have-a-linear-stability-threshold.md), sharpening the source-reconstruction saturation results [PC-304](../../findings/PC-304-oriented-tensor-hierarchy-reaches-full-dft-and-bispectral-completeness.md) and [PC-305](../../findings/PC-305-prime-support-reconstructs-at-source-sparsity-order.md).

PC-304--PC-305 show that sufficiently many ordinary source moments reconstruct the canonical prime support. PC-306 proves that exact finite-level identifiability is actually much cheaper and therefore even less informative as a geometric resource. For prime conductor `q`, the normalized centroid

`b_q(A)=|A|^-1 sum_(a in A) zeta_q^a`

is injective on every nonempty vertex subset `A subset Z/qZ`; the degree-one oriented moment already determines the full support if retained as an exact cyclotomic-field element.

That exact information is violently unstable in the growing-conductor analytic topology. Translation gives

`F_(A+1)(k)=zeta_q^k F_A(k)`.

PC-307 inserts the actual prime packet asymptotics and shows that, uniformly throughout polylogarithmic frequencies, the prime support and its disjoint one-step translate differ by only

`O((1+log(2+K))/(q log q))`.

A fixed-margin readout therefore needs conditioning at least `q log q/(1+log(2+K))` in that regime.

PC-308 now classifies the entire **ordinary unweighted bandwidth** interpolation. The translation identity alone gives

`Delta_q(K)<=2 pi K/q`,

so every `K=o(q)` packet still has vanishing distance between the disjoint matched sources. Stable separation first becomes available at linear bandwidth. At the explicit parity mode `k=(q-1)/2`, the difference tends to magnitude `4/pi`; more generally every positive linear fraction of the spectrum contains a fixed-denominator rational resonance with a nonzero limit.

The important point is what supplies that stability. The linear witnesses are classical prime congruence/major-arc effects: parity in the simplest case, and PNT in fixed arithmetic progressions together with Ramanujan sums in general. Thus ordinary Fourier resolution has only two audited regimes for this matched pair: below linear scale it is unstable; at linear scale it begins to resolve classical congruence structure and approaches full source information. The larger-bandwidth escape left by PC-307 does not produce a hidden intermediate RH carrier.

**Exact algebraic injectivity, stable analytic recoverability, classical congruence resolution and zero-sensitive usefulness are four different resources.** A representation may contain the whole finite source in exact arithmetic, remain unstable throughout every sublinear ordinary packet, and then become stable for a reason that is already classical and unrelated to the desired zero discriminator.

This changes the live Prime-Circle audit. Ordinary bandwidth growth is no longer enough. A proposed escape must specify the topology and precision in which its distinction survives and identify a genuinely nonordinary operation—such as a controlled singular weighting, Li-centered residual, mixed-conductor coupling or another geometry-forced transformation—whose stable output cannot be reduced to the fixed-denominator major-arc information already present at linear scale. Any singular amplification must expose its operator cost rather than hide the inverse condition number in the observable.

**Boundary.** PC-308 classifies ordinary unweighted oriented Fourier packets against the one-step translated prime support. It does not rule out singular weights, different destination topologies, Li subtraction with a controlled residual theorem, or cross-conductor operations acting before an ordinary packet is formed. The parity/major-arc witnesses are classicalized rather than claimed as RH mechanisms.