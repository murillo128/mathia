# MI-047 — Phase-saturated carriers still have bounded fixed-resolution entropy

**Evidence level:** exact synthesis from [WI-343](../../findings/WI-343-fixed-aperture-carriers-have-bounded-effective-rank.md), [WI-347](../../findings/WI-347-extensive-bow-feature-rank-requires-projective-resolution-collapse.md), and [WI-348](../../findings/WI-348-global-phase-sensitivity-still-needs-resolution-collapse.md). The covering-number argument is classical metric entropy; the Mathia content is its application to the phase-saturated bow carrier and destination rank audit.

Quotienting global carrier phase is not what creates fixed-aperture compressibility. If the global phase is retained explicitly, the raw source family gains one compact circle but still has bounded fixed-resolution complexity.

Center the bow carrier by its common logarithmic frequency and saturate it under global phase. When the height-aperture product satisfies `H Delta<=1`, WI-348 constructs a Hilbert-norm `rho`-net of the full phase-saturated family with at most

`20/rho^2`

points. The rapid physical phase may wind many times with height, but repeated winding around one compact circle does not generate new fixed-resolution source states.

Therefore any height-independent normalized feature map with a `T`-uniform ordinary continuity radius `rho_epsilon` at output tolerance `epsilon` has Gram spectral tail at most `m epsilon^2` beyond rank `O(rho_epsilon^(-2))`. If a fixed spectral-tail tolerance `tau` requires effective rank `r_tau(T)->infinity`, then necessarily

`rho_(sqrt(tau)) <= sqrt(20/r_tau(T))`.

For an `L`-Lipschitz feature whose output norm is bounded below by `mu`, this becomes the explicit sensitivity/transmission tariff

`L/mu >= sqrt(tau r_tau(T)/80)`

once the target rank is large.

This complements WI-347 rather than replacing it. Projectively, global phase is quotiented out and the source arc is essentially one-dimensional, producing a stronger `rho=O(1/r)` resolution requirement. Without that quotient, the phase-height source is two-dimensional and the generic entropy argument weakens to `rho=O(r^(-1/2))`. The exponent change measures one additional compact coordinate; it does not make extensive rank available at fixed resolution.

The reusable lesson is: **an apparently rapidly varying nuisance coordinate only creates new usable information if its metric entropy grows at the destination's physical resolution.** Large winding number, oscillation count or nominal phase sensitivity is not enough when the source orbit repeatedly revisits the same compact set.

For Weil Inertia, a genuine escape from fixed-aperture compression must therefore pay one of the explicit currencies: collapsing source-resolution radius, diverging sensitivity relative to transmission, growing aperture, explicit height dependence, cross-window/cross-scale coupling, or a direct source-specific covariance identity. The latter remains especially attractive because it could bypass the generic need to manufacture extensive feature rank.

**Boundary.** WI-348 assumes height-independent feature processing with a useful uniform ordinary continuity modulus on the full phase-saturated source family. Hard quantizers, deliberately height-dependent maps, growing-aperture observations, maps whose sensitivity diverges, or direct arithmetic identities are outside the theorem. The result does not prove the distinguished `Lambda-Lambda^sharp` covariance sign or any RH implication.