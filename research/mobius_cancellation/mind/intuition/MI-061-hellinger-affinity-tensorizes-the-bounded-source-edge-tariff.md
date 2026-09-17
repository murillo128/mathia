# MI-061 — Hellinger affinity tensorizes the bounded source-edge tariff

**Evidence level:** exact synthesis from [MC-340](../../findings/MC-340-bounded-energy-dephasing-forces-linear-joint-source-information.md), [MC-359](../../findings/MC-359-total-variation-source-edge-tariff.md), and [MC-360](../../findings/MC-360-hellinger-product-component-edge-tariff.md). The Jensen--Shannon/Hellinger comparison, Hellinger data processing, joint convexity and product affinity are classical; the Mathia content is their composition with the reciprocal-endpoint information floor and source-edge geometry.

Total variation solved the singular-endpoint problem but did not provide a canonical additive accounting rule for conditionally independent transcript components. Squared Hellinger distance supplies both properties. For neighboring source states `e={x,x'}` let

`h_e^2=H^2(P_x,P_x')`

and normalize

`H_1=(2/m) sum_e h_e^2`.

MC-360 proves

`I(X;Y) <= H_1 + 2(R-1)/m`.

Combining this with the independent endpoint information floor gives, under coefficient energy at most `C` and fixed nontrivial dephasing `eta`,

`liminf H_1/R >= eta^2/(2C)`

along the even-rank endpoint regime. Hellinger therefore remains finite at singularity while still forcing an extensive average separation across the source graph.

Its additional value is compositional. Suppose an edge is represented by a genuine common latent coordinate `Theta` and, conditional on `Theta`, a product transcript `Y=(Y_1,...,Y_k)`. If the latent laws are `nu_x,nu_x'` and `h_(e,j)^2(theta)` is the conditional component Hellinger cost, then MC-360 proves

`H^2(P_x,P_x') <= H^2(nu_x,nu_x') + sum_j int sqrt(r_x r_x') h_(e,j)^2 d kappa`.

Thus source dependence may move between the latent law and the conditionally independent components, but it cannot disappear. Unlike a post-hoc TV coupling, the Hellinger accounting is intrinsic to the product architecture because affinity factorizes.

When the latent law is source-independent and component `j` depends only on source coordinates `A_j`, uniform per-direction bounds `alpha_(j,i)` imply an extensive weighted-incidence tariff:

`liminf (1/R) sum_j sum_(i in A_j) alpha_(j,i) >= eta^2/(2C)`.

Splitting a source-sensitive transcript into many individually weak components therefore does not evade the global information floor. A successful architecture-specific contradiction can now work from the opposite direction: expose the actual latent/product decomposition of the Möbius endpoint and prove that the total affinity-weighted source-coordinate sensitivity is subextensive.

The reusable distinction is between **bounded distinguishability and compositional bounded distinguishability**. TV is especially natural when a genuine common-seed representation turns source flips into change probabilities. Hellinger is especially natural when the transcript has a genuine latent/product factorization. Jeffreys/Fisher remain sharper in regular smooth channels. These are different currencies, but the destination imposes the same qualitative requirement: enough neighboring source states must become observably different.

**Boundary.** MC-360 is still a necessary admission theorem, not an arithmetic upper bound and not an estimate for `M(x)`. Conditional independence and the latent representation must be genuine properties of the architecture rather than an artificial refactorization. The `JS<=H^2` route is not asymptotically sharp at the matched-filter singular limit, even though exact unit-energy dephasing makes every surviving edge maximally Hellinger-separated. The next useful result remains architecture-specific: prove a subextensive Hellinger latent/component budget for the actual Möbius-derived transcript, or identify the real source-dependent component that pays the extensive tariff.
