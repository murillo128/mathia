# MI-048 — One-mesh overhang resolves the prime `PF_3` topology boundary

**Evidence level:** exact synthesis from [AF-395](../../findings/AF-395-fixed-successor-depth-loses-curvature-component-topology.md) through [AF-398](../../findings/AF-398-prime-pf3-successor-wall-has-a-third-scale-log-log-correction.md).

The disconnected-curvature control has an exact physical locality wall at log-prime reach one. AF-397 shows that the sampled detector does not need a determinant margin bounded away from zero: it only needs enough physical overhang to place sampled points on both sides of that topology boundary.

If `H_N(R)=log(p_(N+R)/p_N)` and `Delta_N(R)` is the largest adjacent log-prime mesh width in the block, then `H_N(R)<=1` certifies nonnegative order-three minors throughout the block, while `H_N(R)>1+Delta_N(R)` forces a negative minor for the explicit AF-395 profile once the mesh is small. The uncertainty is therefore one mesh width, not an analytic continuity margin.

AF-397 converts the first-order AF-396 transition into a two-term successor-depth threshold. AF-398 now resolves the previously open equality scale one order further. Writing `L=log N`, `ell=log L` and

`R_N(beta)=floor((e-1)N-eN/L+beta N ell/L^2)`,

one has

`H_N(R_N(beta))=1+(beta/e-1)ell/L^2+O(ell^2/L^3)`.

Hence `beta<e` is eventually blind and `beta>e` eventually detects. Equivalently,

`R_N^crit=(e-1)N-eN/log N+eN log log N/log^2 N+O(N(log log N)^2/log^3 N)`.

The exact physical count `pi(e p_N)-N` has the same three-term expansion. Thus the second-order equality case is no longer unresolved: the prime-density correction itself contributes the next combinatorial breadth term needed to cross the fixed physical wall.

The reusable point is precise: when a global discriminator is a component/topology crossing and the witness only requires sampled points on opposite sides of a physical wall, the relevant conditioning quantity is **overhang divided by mesh width**. A vanishing witness margin need not obstruct detection if the sampling mesh vanishes faster than the physical overhang. Once the physical threshold is fixed, successive asymptotic corrections in source density reappear as corrections to the combinatorial successor radius.

**Boundary.** This is a sampling theorem for the explicit smooth `PF_3` control. It does not derive the required local signs or curvature connectedness from prime arithmetic, does not settle the still thinner `N(log log N)^2/log^3 N` boundary, and does not extend automatically to higher determinant order or other source-density laws.