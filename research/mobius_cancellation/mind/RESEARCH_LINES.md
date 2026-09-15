# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Exploit two-sided hereditary endpoint source complexity beyond the low-cost half-occupancy barrier

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-034-endpoint-sparsity-is-hereditary-under-projection`.

MC-293--MC-306 move from individual character cost through family energy, multiquadratic packaging, common radical and quotient occupancy, and show that the previous full-family scalar capacities can be simultaneously saturated by a matched disjoint-singleton control.

MC-307 finds the information that control omits. Projecting the exact one-defect endpoint to any `k` selected coordinates leaves at most `k+1` of `2^k` cells. Brun--Titchmarsh therefore forces polynomial source cost in every relevant endpoint subfamily; in particular fixed small coordinate sets cannot be assembled from only `y^o(1)` projected radical.

MC-308 adds the source-coordinate dual. For any retained source-prime subset `J`, quotient the endpoint space by the span of omitted source columns. If the resulting quotient has dimension `t_J` and the one-defect simplex has `h_J` distinct images, then compatible source assignments occupy the exact fraction `h_J/2^(t_J)`, forcing

`P_J >= y^(1-(2+o(1))h_J/2^(t_J)) e^(-O(1))`.

MC-309 now closes the most direct low-product implementation of that idea. Below the Landau--Page source threshold all but at most one quotient character have bias `epsilon_y << (log y)^-2`. If `2^(t_J)epsilon_y=o(1)`, Parseval forces full occupancy without an exceptional mode and at least half occupancy in general. Hence the MC-308 exponent cannot be positive for low-product source cuts of moderate quotient dimension, including `2^(t_J)=o((log y)^2)`.

The live theorem must therefore exploit the **incidence geometry outside that barrier**. Can the actual Legendre pattern force a high-product cut, a quotient dimension beyond the Landau--Page occupancy range, or a structural constraint that controls the one exceptional Fourier mode? Alternatively, can target-projection constraints and source-cut constraints be combined in a way that makes half occupancy itself impossible for the actual incidence map? Another aggregate capacity or another low-cost cut inside the same regime cannot close the endpoint.

## Keep target projection and source-cut quotienting distinct, and price the exceptional mode

MC-307 asks what remains when endpoint coordinates are deleted. MC-308 asks what remains when source coordinates are deleted and their span is quotiented out. Both are hereditary tests, but they measure different failures.

MC-309 adds a third layer: even when a source cut leaves a large quotient, low arithmetic source cost imposes a Fourier occupancy floor. The decisive statistic is not `|J|` alone or even `h_J/2^(t_J)` in isolation, but how that quotient sits relative to the low-cost character spectrum and its possible single Landau--Page exceptional direction.

Any proposed closing argument must state which restriction is applied, how the endpoint simplex projects to that quotient, what source product is paid, whether the quotient dimension lies inside the low-bias regime, and how the exceptional mode is handled. Treating all hereditary complexity as one scalar would erase exactly the information of MC-307--MC-309.

## Preserve matched controls, but require them to match the full hereditary incidence profile

The exchangeable controls of MC-295/MC-298 show that low-order combinatorial regularity can coexist with forbidden parity. MC-306 remains useful because it proves the previous aggregate package noncoercive, while MC-307--MC-309 show that a serious endpoint control must reproduce not only rank, energy, conductor scale, full radical, totient density and full quotient occupancy, but also target-projection occupancies, source-cut occupancies, source-product scale and the exceptional-mode allowance across the incidence map.

A proposed theorem has discriminatory content only if the same hereditary audits kill the matched control or are independently verified on it. Repackaging the old aggregate capacities, or searching for a low-product source cut that Landau--Page already forces to half occupancy, is no longer a plausible route.