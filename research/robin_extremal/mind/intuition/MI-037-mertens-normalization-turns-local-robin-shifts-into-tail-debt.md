# MI-037 — Mertens normalization is a conservation law; only spatial exhaustion turns it into Robin-prefix rigidity

**Evidence level:** exact/literature-backed synthesis from [RE-153](../../findings/RE-153-self-tangent-robin-height-is-a-pareto-weighted-chebyshev-deficit-average.md), [RE-164](../../findings/RE-164-korobov-vinogradov-fidelity-controls-robin-source-ambiguity.md) through [RE-171](../../findings/RE-171-exact-mertens-matching-still-permits-transient-post-selector-robin-excursions.md). Classical Mertens normalization is external mathematics; the exact Robin-kernel debt identity, quantitative tail capacity and compensated matched controls are line-specific.

RE-165--RE-168 show that a quantitative PNT/Korobov--Vinogradov envelope still allows order-one normalized Robin motion whenever enough displacement width is available near the moving capacity center. Those matched generalized-source controls preserve the Chebyshev envelope but were deliberately free to change the asymptotic Mertens product.

RE-169 identifies the relevant global invariant. With `h(t)=-log(1-t^(-1))/log t`, the difference of source Mertens constants for sources agreeing below `T` is exactly the full future Robin-kernel weighted discrepancy,

`Gamma(Q_2)-Gamma(Q_1)=int_T^infty (theta_(Q_2)(t)-theta_(Q_1)(t))(-h'(t)) dt`.

The normalized Robin coordinate uses the same kernel. Once the Mertens constants are fixed, any accumulated post-selector Robin displacement is therefore a compensation debt that must be repaid by the unseen tail. Under the KV envelope, the remaining debt above `U` is bounded by the remote capacity

`K_b(p,U)=sqrt(p) log p exp(-bV(U))/V(U)`.

If this future capacity is `o(1)`, a fixed debt can no longer be repaid; Mertens matching plus a KV-rigid tail therefore yields prefix rigidity.

RE-170 shows that critical-scale Mertens matching alone is not enough: two bounded-multiplicative shells can create an order-one intermediate excursion and later repay it while making `Gamma(Q_p)-gamma=o((sqrt(p)log p)^(-1))` and remaining negligible relative to the KV envelope.

RE-171 proves that **no stronger scalar Mertens precision can repair this**. The residual left by the first two shells is only `O(log p/p)`. A third shell of `O(log p)` Chebyshev-mass-neutral prime pairs provides a continuous finite-dimensional dial whose Mertens shift covers that residual, while its worst cumulative Chebyshev cost is only `O((log p)^2)`. The completed generalized source can therefore satisfy

`Gamma(Q_p)=gamma`

exactly, preserve the order-one intermediate prefix excursion, and return the final Robin displacement to zero exactly after the last shell.

The distinction is now sharp. **Mertens fidelity is purely a conservation law for total Robin-kernel charge; tail exhaustion or another selector-sensitive spatial rule is the localization law.** Exact conservation cannot say where opposite signed charge sits. As long as enough future weighted capacity remains, later shells can repay an earlier debt without violating the global invariant.

For the ordinary-prime/CA problem, the missing theorem can no longer be phrased as “improve the Mertens normalization.” It must connect the selector-selected prefix to a region in which compensating charge is unavailable, constrain the permitted sign/location of future debt using genuine prime structure, or supply another source-specific invariant that the exact three-shell matched control cannot preserve.

**Boundary.** The debt identity assumes the relevant Mertens constants exist. RE-171 is a generalized matched-control construction, not an ordinary-prime or CA counterexample. It proves that exact `Gamma=gamma` plus pointwise KV fidelity remains logically insufficient without a spatial/tail restriction. It does not prove Robin's inequality, RH, or a sign theorem for ordinary CA selectors.