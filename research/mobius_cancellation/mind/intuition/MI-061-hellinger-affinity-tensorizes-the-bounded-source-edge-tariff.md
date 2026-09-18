# MI-061 — Hellinger affinity tensorizes the bounded source-edge tariff and exposes an additive endpoint depth

**Evidence level:** exact synthesis from [MC-340](../../findings/MC-340-bounded-energy-dephasing-forces-linear-joint-source-information.md), [MC-359](../../findings/MC-359-total-variation-source-edge-tariff.md), [MC-360](../../findings/MC-360-hellinger-product-component-edge-tariff.md), [MC-361](../../findings/MC-361-binary-entropy-sharpens-reciprocal-endpoint-information-floor.md), [MC-362](../../findings/MC-362-tv-to-hellinger-near-endpoint-transfer.md), [MC-363](../../findings/MC-363-sharp-js-hellinger-endpoint-envelope.md), and [MC-364](../../findings/MC-364-product-affinity-log-depth-tariff.md). The Hellinger/Bhattacharyya identities and product tensorization are classical; the Mathia content is their composition with the reciprocal-endpoint source geometry and sharp dephasing floor.

Total variation remains the natural bounded currency for a genuine common-seed architecture, while squared Hellinger distance is the natural bounded currency for a genuine latent/product architecture because **affinity multiplies** through conditionally independent components. MC-360 therefore prevents source sensitivity from disappearing merely by splitting a transcript into many weak pieces.

MC-363 makes that bounded Hellinger requirement endpoint-sharp. If `H_1=(2/m)sum_e H^2(P_x,P_x')`, the sharp Jensen--Shannon/Hellinger envelope implies, at matched-filter energy and dephasing error `epsilon`,

`liminf H_1/R >= 1-sqrt(2 epsilon-epsilon^2)`.

Thus the aggregate Hellinger boundary approaches its maximal value as the endpoint becomes deterministic, with deficit `O(sqrt(epsilon))`.

MC-364 identifies the stronger additive coordinate hidden behind that product statement. Suppose the latent law is source-independent and, conditional on it, the transcript factors into components. If component `j` changes by at most squared Hellinger cost `alpha_(j,i)` when source direction `i` is flipped, define its negative log-affinity cost

`lambda_(j,i)=-log(1-alpha_(j,i))`,

and the total directional depth

`Lambda_i=sum_j lambda_(j,i)`.

Product affinity gives the exact nonlinear upper envelope

`H^2(P_x,P_x') <= 1-exp(-Lambda_i)`.

Combining this with the sharp destination lower bound yields

`(1/R) sum_i exp(-Lambda_i) <= beta_R`,

where `beta_R` is the required residual output affinity. Hence

`(1/R) sum_i Lambda_i >= -log beta_R`.

At matched-filter energy with dephasing error at most `epsilon`,

`liminf (1/R) sum_i Lambda_i >= (1/2) log[1/(2 epsilon-epsilon^2)]`.

So near exact dephasing the correct product tariff is not merely an extensive linear incidence cost: its average **Bhattacharyya depth diverges logarithmically** like `(1/2)log(1/epsilon)`. The stronger quantile statement

`# {i: Lambda_i<=L}/R <= beta_R exp(L)`

shows that the tariff cannot be paid by a small exceptional set of heavily source-dependent directions. At the exact endpoint every direction must have infinite total depth, meaning either a mutually singular component occurs on that direction or an infinite component family accumulates divergent depth.

This separates three related resources. Hellinger distance is the bounded output separation; affinity is the multiplicative product coordinate; negative log-affinity is the additive depth coordinate that reveals how hard near-singularity is to synthesize from weak independent pieces. Replacing the product by the linear union bound hides precisely this logarithmic endpoint growth.

If every component remains uniformly nonsingular, `alpha_(j,i)<=a<1`, MC-364 converts the same lower bound into logarithmically growing linear Hellinger cost and component depth. A proposed many-weak-components Möbius architecture therefore has to expose enough source incidences per direction to meet this divergence, not merely a positive extensive average.

**Boundary.** MC-364 is still an admission theorem, not an arithmetic upper bound and not an estimate for `M(x)`. The latent law must truly be source-independent and the conditional product factorization must be genuine. Source-dependent latent selection has to be charged separately, and arbitrary dependent components do not inherit product affinity. The live theorem remains architecture-specific: expose the actual Möbius-derived transcript, including latent choices and side channels, and prove that its directional Bhattacharyya depth cannot meet the required endpoint tariff, or identify the concrete source-dependent component that pays it.