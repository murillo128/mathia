# MI-051 — Bounded Wang collisions have a Hermite budget and block Riesz floor

**Evidence level:** exact/classical-conditioning synthesis from [VIS-352](../../findings/VIS-352-hermite-collision-scale-budget.md) and [VIS-353](../../findings/VIS-353-separated-cluster-block-riesz-floor.md), refining the stable divided-difference coordinates of VIS-351. Hermite interpolation, divided differences and finite Riesz conditioning are classical; the line-specific content is the Wang tail resource ledger.

For a fixed collision cluster with `B` phase fibers and polynomial depth `q`, total confluent multiplicity is `N=Bq`. If its physical phase diameter is `delta` and the normalized cluster shape stays nondegenerate, the stable divided-difference coordinates satisfy a worst-case lower scale

`||u||_2 >= C delta^(N-1) ||c||_2`

relative to the raw polynomial coefficient vector. Thus a bounded cluster can buy an extra `X^-1` only by becoming polynomially microscopic, unless the Wang coefficient map itself is already small. Raw Vandermonde blow-up is not free cancellation; its usable part is priced by the Hermite collision scale.

There is no second asymptotic gain from combining finitely many already-priced clusters that remain separated inside bounded spectral span. Their union has a uniform block Riesz lower bound, so inter-cluster cancellation contributes only a fixed constant. If clusters approach one another, they must be merged into a new collision hierarchy and the additional scale charged explicitly.

The durable accounting rule is therefore **local collision powers first, separated-block geometry second**. A bounded finite bank cannot stack an intra-cluster conditioning gain and an independent inter-cluster cancellation gain without another degenerating parameter.

**Boundary.** Growing multiplicity or cluster count, expanding spectral span/density, shrinking reference windows, hierarchical collisions, frequency/source-dependent coefficients and a singular source-to-Wang coefficient map are outside the fixed compact regime. Those are genuine new resources; bounded separated cluster cancellation is not.