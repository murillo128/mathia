# MI-043 — Diagonal cubes squeeze ordinary Gowers smallness to one critical order window

**Evidence level:** exact synthesis from [WI-332](../../findings/WI-332-u2-smallness-cannot-control-bow-sliding-variance.md)--[WI-336](../../findings/WI-336-matched-energy-diagonal-cubes-squeeze-gowers-escape-to-one-order-window.md). The Gowers norms and Rademacher comparison mechanism are classical; the Mathia content is the matched-energy two-sided squeeze at the bow scale.

Earlier countermodels showed that local `U^2`, square-root cancellation against fixed-degree phases, and every fixed finite hierarchy of small local Gowers norms can coexist with full diagonal-scale sliding variance. WI-335 extended that obstruction to slowly growing order. WI-336 now identifies the complementary high-order barrier from the same matched energy.

For an interval of length `L` and a sequence with energy `E` comparable to `L log N`, the zero-increment cubes alone force

`||f||_(U^s(I)) >= sqrt(E/(2L)) L^(-1/2^s)`.

At the bow scale define the dimensionless transition parameter

`R_s(L,N)=2^s loglog N/log L`.

A matched-energy Rademacher model has uniformly small local `U^s` throughout the bow-scale interval family whenever `R_s<=1-eta`, while retaining the full diagonal sliding variance. Conversely, any sequence with comparable diagonal energy cannot have `U^s=o(1)` once `R_s>=2+eta`. Since increasing `s` by one doubles `R_s`, the unresolved region occupies at most one binary order step.

This turns the growing-order escape into a sharply localized transition rather than an open hierarchy. Below the transition, ordinary normalized Gowers smallness is provably too weak because matched-energy countermodels survive. Above it, ordinary smallness is impossible for the source energy itself because diagonal cubes force the norm large. Merely asking for a still higher `U^s` therefore cannot provide the missing bow cancellation.

The reusable lesson is that **a norm hierarchy can saturate from both sides**. Failure at low order need not mean “go to higher order”: the statistic may eventually become dominated by an unavoidable diagonal contribution before it acquires the desired signed two-point information. The correct next object must either exploit the narrow critical-order quantitative structure, renormalize/subtract the diagonal cubes, or leave ordinary norm smallness and control the source-specific signed covariance directly.

For Weil inertia the destination remains the distinguished bow twist. The exact variance needs a macroscopic negative off-diagonal term to beat its positive diagonal contribution. WI-336 does not supply that sign, but it makes clear that generic one-point uniformity below or above the critical order cannot be the whole mechanism. Any successful Gowers-style route must explain how its critical statistic couples specifically to the off-diagonal bow covariance rather than simply reporting a small norm.

**Boundary.** WI-336 does not prove sufficiency at the single remaining critical order, describe the actual von Mangoldt covariance, or rule out a renormalized/diagonal-free higher-order statistic. It also does not replace the accepted distinguished-twist clue. The result is a two-sided obstruction to ordinary normalized Gowers-smallness as a generic escape route, not a theorem that the arithmetic source lacks the required cancellation.
