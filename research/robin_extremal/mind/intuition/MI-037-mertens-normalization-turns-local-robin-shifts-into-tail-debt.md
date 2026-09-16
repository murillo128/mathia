# MI-037 — Mertens normalization turns local Robin shifts into tail debt, but only tail exhaustion makes that debt rigid

**Evidence level:** exact/literature-backed synthesis from [RE-153](../../findings/RE-153-self-tangent-robin-height-is-a-pareto-weighted-chebyshev-deficit-average.md), [RE-164](../../findings/RE-164-korobov-vinogradov-fidelity-controls-robin-source-ambiguity.md) through [RE-170](../../findings/RE-170-critical-mertens-matching-still-permits-compensated-local-robin-excursions.md). Classical Mertens normalization is external mathematics; the exact Robin-kernel debt identity, critical precision and compensated two-shell control are line-specific.

RE-165--RE-168 show that a quantitative PNT/Korobov--Vinogradov envelope still allows order-one normalized Robin motion whenever enough displacement width is available near the moving capacity center. Those matched generalized-source controls preserve the Chebyshev envelope but were deliberately free to change the asymptotic Mertens product.

RE-169 identifies the missing global invariant. With `h(t)=-log(1-t^(-1))/log t`, the difference of source Mertens constants for sources agreeing below `T` is exactly the full future Robin-kernel weighted discrepancy,

`Gamma(Q_2)-Gamma(Q_1)=int_T^infty (theta_(Q_2)(t)-theta_(Q_1)(t))(-h'(t)) dt`.

The normalized Robin coordinate uses the same kernel. Once the Mertens constants are fixed, any accumulated post-selector Robin displacement is therefore a compensation debt that must be repaid by the unseen tail. Under the KV envelope, the remaining debt above `U` is bounded by the remote capacity

`K_b(p,U)=sqrt(p) log p exp(-bV(U))/V(U)`.

If this future capacity is `o(1)`, a fixed debt can no longer be repaid; critical-scale Mertens matching plus a KV-rigid tail therefore yields prefix rigidity.

RE-170 shows that **critical Mertens matching alone is not prefix rigidity**. Two disjoint bounded-multiplicative shells can be coupled so that the first creates an order-one normalized Robin excursion, the second pays it back to `o(1)`, and the final generalized source satisfies

`Gamma(Q_p)-gamma=o((sqrt(p) log p)^(-1))`

while its Chebyshev perturbation is still `o(1)` relative to the full KV envelope. The intermediate prefix remains order-one different even though the final global normalization is matched at the very scale identified by RE-169.

The distinction is now exact. **Mertens fidelity is a conservation law; KV tail exhaustion is the localization law that turns conservation into rigidity.** If enough future weighted capacity remains, opposite-sign shells can transfer the debt spatially without violating the global invariant. If the remaining capacity tends to zero, there is nowhere left for a fixed debt to go.

For the ordinary-prime/CA problem, neither resource by itself is the missing selector theorem. `Gamma(P)=gamma` is exact, but a proof must also connect the selector-selected prefix to a region where future compensation is quantitatively unavailable, or supply another source-specific invariant that forbids the two-shell cancellation pattern before the Robin excursion becomes dangerous.

**Boundary.** The debt identity assumes the relevant Mertens constants exist. RE-170 is a generalized matched-control construction, not an ordinary-prime or CA counterexample. It proves that global critical-scale normalization and pointwise KV fidelity remain logically insufficient without a spatial/tail restriction. It does not prove Robin's inequality, RH, or a sign theorem for ordinary CA selectors.