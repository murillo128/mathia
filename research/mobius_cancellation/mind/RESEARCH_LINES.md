# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Exploit two-sided hereditary endpoint source complexity

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-034-endpoint-sparsity-is-hereditary-under-projection`.

MC-293--MC-306 move from individual character cost through family energy, multiquadratic packaging, common radical and quotient occupancy, and show that the previous full-family scalar capacities can be simultaneously saturated by a matched disjoint-singleton control.

MC-307 finds the information that control omits. Projecting the exact one-defect endpoint to any `k` selected coordinates leaves at most `k+1` of `2^k` cells. Brun--Titchmarsh therefore forces polynomial source cost in every relevant endpoint subfamily; in particular fixed small coordinate sets cannot be assembled from only `y^o(1)` projected radical.

MC-308 adds the source-coordinate dual. For any retained source-prime subset `J`, quotient the endpoint space by the span of omitted source columns. If the resulting quotient has dimension `t_J` and the one-defect simplex has `h_J` distinct images, then compatible source assignments occupy the exact fraction `h_J/2^(t_J)`, forcing

`P_J >= y^(1-(2+o(1))h_J/2^(t_J)) e^(-O(1))`.

The next theorem should therefore act on the **incidence geometry between endpoint directions and lower-prime representatives**, not on another full-family scalar. Which low-product source cuts retain large quotient rank but small simplex occupancy? Can the actual Legendre incidence pattern satisfy all target-subfamily and source-cut bounds simultaneously? Heavy overlap may help one audit while making another expensive; that tension is now a concrete source-side object.

## Keep target projection and source-cut quotienting distinct

MC-307 asks what remains when endpoint coordinates are deleted. MC-308 asks what remains when source coordinates are deleted and their span is quotiented out. Both are hereditary tests, but they measure different failures.

A large full radical can be assembled from many cheap almost-disjoint coordinates and still collapse under a small target projection. Conversely, a target subfamily can be expensive in aggregate while a carefully chosen source cut fails to see its sparse endpoint image because omitted columns span most of the quotient. The relevant source-cut statistic is `h_J/2^(t_J)`, not `|J|` alone.

Any proposed closing argument must state which restriction is applied, how the endpoint simplex projects to that quotient, and whether the corresponding radical bound is incompatible with the arithmetic source budget. Treating all hereditary complexity as one scalar would erase exactly the new information of MC-308.

## Preserve matched controls, but require them to match the full hereditary incidence profile

The exchangeable controls of MC-295/MC-298 show that low-order combinatorial regularity can coexist with forbidden parity. MC-306 remains useful because it proves the previous aggregate package noncoercive, but MC-307--MC-308 show that a serious endpoint control must now reproduce not only rank, energy, conductor scale, full radical, totient density and full quotient occupancy, but also target-projection and source-cut occupancies across the incidence map.

A proposed theorem has discriminatory content only if the same hereditary audits kill the matched control or are independently verified on it. Repackaging the old aggregate capacities without this restriction geometry is no longer a plausible route.