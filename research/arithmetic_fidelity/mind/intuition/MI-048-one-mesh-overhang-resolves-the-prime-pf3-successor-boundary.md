# MI-048 — One-mesh overhang resolves the prime `PF_3` topology boundary

**Evidence level:** exact synthesis from [AF-395](../../findings/AF-395-fixed-successor-depth-loses-curvature-component-topology.md) through [AF-397](../../findings/AF-397-prime-pf3-reach-has-a-second-order-successor-threshold.md).

The disconnected-curvature control has an exact physical locality wall at log-prime reach one. AF-397 shows that the sampled detector does not need a determinant margin bounded away from zero: it only needs enough physical overhang to place sampled points on both sides of that topology boundary.

If

`H_N(R)=log(p_(N+R)/p_N)`

and `Delta_N(R)` is the largest adjacent log-prime mesh width in the block, then `H_N(R)<=1` certifies nonnegative order-three minors throughout the block, while `H_N(R)>1+Delta_N(R)` forces a negative minor for the explicit AF-395 profile once the mesh is small. The uncertainty is therefore one mesh width, not an analytic continuity margin.

This converts the first-order AF-396 transition into a two-term successor-depth threshold. For

`R_N=floor((e-1)N-alpha N/log N)`,

prime asymptotics give

`H_N(R_N)=1+(1-alpha/e)/log N+O(log log N/log^2 N)`,

whereas the prime-log mesh is `o(1/log N)`. Hence `alpha>e` is eventually blind and `alpha<e` is eventually detecting. Equivalently,

`R_N^crit=(e-1)N-eN/log N+O(N log log N/log^2 N)`.

In particular the literal first-order radius `floor((e-1)N)` is eventually on the detecting side. The unresolved boundary has moved to the thinner scale where the displayed `1/log N` correction cancels.

The reusable point is precise: when a global discriminator is a component/topology crossing and the witness only requires sampled points on opposite sides of a physical wall, the relevant conditioning quantity is **overhang divided by mesh width**. A vanishing witness margin need not obstruct detection if the sampling mesh vanishes faster than the physical overhang.

**Boundary.** This is a sampling theorem for the explicit smooth `PF_3` control. It does not derive the required local signs or curvature connectedness from prime arithmetic, does not settle the still thinner `alpha=e` boundary, and does not extend automatically to higher determinant order.