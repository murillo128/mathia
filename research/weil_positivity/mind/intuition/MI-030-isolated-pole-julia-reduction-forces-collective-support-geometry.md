# MI-030 — Scalar Julia reduction forces genuinely unbounded collective support geometry

**Evidence level:** exact local scalar-Julia classifications from [WP-316](../../findings/WP-316-scalar-julia-reduction-erases-every-asymptotically-isolated-mangoldt-pole.md) and [WP-317](../../findings/WP-317-finite-multipole-julia-reduction-is-interlacing-degree-reduction.md), complementing the noncompact atom-mass-scale obstruction [WP-315](../../findings/WP-315-mangoldt-atom-mass-scale-is-not-a-uniform-isolated-pole-scale.md).

WP-315 shows that the intrinsic Mangoldt atom mass is not a uniform isolated-pole scale: bounded prime clusters can collapse arbitrarily many comparable positive atoms into one normalized support-side chart. A natural escape is to choose a gap-adapted scale or subsequence where one focal pole really does dominate.

WP-316 shows that classical scalar Julia--Nevanlinna reduction then removes precisely that isolated geometry. Write

`f(z)=-a/(z-x)+h(z)`

with positive Herglotz background `h`, choose a regular real node `t=x+sigma r`, and measure the background derivative by

`kappa=(r^2/a) h'(t)`.

If `kappa->0`, positivity controls the entire normalized background increment and the canonical local Julia profile converges to the real constant `sigma`. For the pure one-pole control this collapse is exact at every scale. For the reflected Mangoldt source, every nonconstant scalar Julia tangent must therefore retain an order-one positive contribution from other prime-power atoms.

WP-317 closes the next obvious escape: retaining a **fixed finite** cluster does not create a new arithmetic sign mechanism. For a positive atomic scalar Herglotz function with `N` poles, one regular normalized Julia step removes the original poles and produces exactly `N-1` positive poles interlacing the old support. Iterating gives

`N -> N-1 -> ... -> 1 -> 0`

atoms, ending in the same constant collapse. Reversing the steps is classical Julia augmentation/continued-fraction reconstruction. The positivity and interlacing hold for arbitrary positive atomic input and therefore carry no prime-specific content by themselves.

The reusable dichotomy is now stronger than isolated versus multipole. **One-pole geometry is Julia-trivial, and every bounded finite multipole geometry is classical finite-degree Julia data.** A scalar support-side route can remain genuinely open only if the collectivity itself grows without bound or leaves the finite pure-atomic rational category through a continuous/affine component. Otherwise the reduction either erases the pole immediately or consumes the finite cluster in finitely many classical degree drops.

This changes the proof obligation from “find the right prime gap scale” or even “retain several nearby primes” to “derive a canonical infinite collective normalization.” The collective object must be forced by the source, remain locally controlled despite WP-315 clustering, survive matched positive-measure controls, and still couple to the archimedean/Gamma discriminator with the correct orientation. Merely taking larger fixed clusters does not satisfy this: the relevant limit must show new stable geometry as multiplicity grows.

The same evidence also sharpens the category escape. Matrix/operator-valued Julia reduction, generalized resolvents, nonseparable finite--archimedean couplings, or a surviving continuous Herglotz component are not ruled out because they are not finite scalar rational reductions. But a proposed scalar construction should first prove why its infinite collective limit exists and is source-specific before positivity is interpreted as Weil positivity.

**Boundary.** WP-317 treats finite pure positive atomic scalar Herglotz tangents at regular real Julia nodes. It does not classify an unbounded/infinite cluster limit, continuous measure, affine Herglotz channel, matrix/operator-valued response or a different non-Julia global operation. WP-315 shows that unbounded local multiplicity is genuinely available as a source phenomenon; it does not show that the corresponding normalized measures are compact or that their limit has the required Gamma orientation.