# MI-030 — Isolated-pole Julia reduction forces collective support geometry

**Evidence level:** exact local scalar-Julia classification from [WP-316](../../findings/WP-316-scalar-julia-reduction-erases-every-asymptotically-isolated-mangoldt-pole.md), complementing the noncompact atom-mass-scale obstruction [WP-315](../../findings/WP-315-mangoldt-atom-mass-scale-is-not-a-uniform-isolated-pole-scale.md).

WP-315 shows that the intrinsic Mangoldt atom mass is not a uniform isolated-pole scale: bounded prime clusters can collapse arbitrarily many comparable positive atoms into one normalized support-side chart. A natural escape is to choose a gap-adapted scale or subsequence where one focal pole really does dominate.

WP-316 shows that classical scalar Julia--Nevanlinna reduction then removes precisely that isolated geometry. Write

`f(z)=-a/(z-x)+h(z)`

with positive Herglotz background `h`, choose a regular real node `t=x+sigma r`, and measure the background derivative by

`kappa=(r^2/a) h'(t)`.

If `kappa->0`, positivity controls the entire normalized background increment and the canonical local Julia profile converges to the real constant `sigma`. For the pure one-pole control this collapse is exact at every scale. The pole mass and gap scale survive only through a removable real scalar; they do not generate a nonconstant local Pick geometry.

For the reflected Mangoldt source the same ratio is the positive collectivity index

`kappa_n = sum_(m!=n) (a_m/a_n) (r_n/(x_m-t_n))^2`.

There is no cancellation in this expression. Therefore every nonconstant support-side scalar Julia tangent must retain an order-one contribution from other prime-power atoms before the sign-producing Julia theorem is applied.

The reusable dichotomy is **isolated source atom versus collective positive geometry**. A source-specific one-pole normalization can fail in either direction: if nearby atoms collapse at the chosen scale, the chart is not locally compact; if the chart is genuinely one-pole dominated, scalar Julia reduction trivializes it. The surviving scalar category is necessarily multipole.

This changes the proof obligation from “find the right prime gap scale” to “derive a canonical collective normalization.” The collective object must be forced by the source, remain locally controlled under clustering, preserve Pick positivity, and still couple to the archimedean/Gamma discriminator with the correct orientation. A synthetic positive multipole measure remains a matched control, so collectivity alone is not yet arithmetic specificity.

**Boundary.** WP-316 does not claim that every support-side node has `kappa->0`, nor that `kappa` bounded away from zero is sufficient for a useful Weil tangent. It does not touch matrix/operator-valued Julia reduction, generalized resolvents or nonseparable finite--archimedean couplings. The conclusion is only that an asymptotically isolated Mangoldt pole cannot carry the missing Weil positivity through the classical scalar Julia mechanism.