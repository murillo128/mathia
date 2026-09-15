# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Force source incidence beyond the low-cost half-occupancy and 2-adic rank barriers

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-035-reciprocal-page-cheap-subspaces-have-a-2-adic-rank-ceiling`.

MC-293--MC-306 move from individual character cost through family energy, multiquadratic packaging, common radical and quotient occupancy, and show that the previous full-family scalar capacities can be simultaneously saturated by a matched disjoint-singleton control.

MC-307 finds the information that control omits. Projecting the exact one-defect endpoint to any `k` selected coordinates leaves at most `k+1` of `2^k` cells. Brun--Titchmarsh therefore forces polynomial source cost in every relevant endpoint subfamily; in particular fixed small coordinate sets cannot be assembled from only `y^o(1)` projected radical.

MC-308 adds the source-coordinate dual. For any retained source-prime subset `J`, quotient the endpoint space by the span of omitted source columns. If the resulting quotient has dimension `t_J` and the one-defect simplex has `h_J` distinct images, then compatible source assignments occupy the exact fraction `h_J/2^(t_J)`, forcing

`P_J >= y^(1-(2+o(1))h_J/2^(t_J)) e^(-O(1))`.

MC-309 closes the most direct low-product implementation of that idea. Below the Landau--Page source threshold all but at most one quotient character have bias `epsilon_y << (log y)^-2`. If `2^(t_J)epsilon_y=o(1)`, Parseval forces full occupancy without an exceptional mode and at least half occupancy in general. Hence the MC-308 exponent cannot be positive for low-product source cuts of moderate quotient dimension, including `2^(t_J)=o((log y)^2)`.

MC-310 makes the reciprocal equal-mass endpoint substantially more rigid. In the discrete-resolution regime `R epsilon_y<1`, every nonexceptional Page-cheap frequency is forced exactly onto Hamming weight `R/2`. Linear closure then turns the middle-layer condition into a one-weight binary-code constraint. A uniformly Page-cheap subspace of dimension `t` obeys

`2^t | R` and `t<=nu_2(R)` if it contains no exceptional mode,

while in general

`t<=nu_2(R)+1`.

Thus the reciprocal extremizer cannot hide a large low-source linear sector merely by packing cheap frequencies near half occupancy; except at unusually 2-adically divisible ranks, that entire sector has very small dimension.

The live theorem must now connect this rigidity to the **actual source incidence geometry**. Can the physical Legendre incidence map force a uniformly Page-cheap subspace whose dimension exceeds the `nu_2(R)+1` ceiling, identify/control the unique exceptional direction strongly enough to remove the `+1`, or prove that the complementary high-source directions themselves carry a coercive cost? Another aggregate capacity or another low-product moderate-rank cut cannot close the endpoint.

## Keep target projection, source-cut quotienting and linear cheap-subspace closure distinct

MC-307 asks what remains when endpoint coordinates are deleted. MC-308 asks what remains when source coordinates are deleted and their span is quotiented out. MC-309 adds a Fourier occupancy floor for low-cost source cuts. MC-310 imposes a different condition again: when a **linear subspace** of reciprocal endpoint frequencies is uniformly cheap, the exact lattice spacing of the reciprocal bias converts Page smallness into exact middle-layer membership and hence a 2-adic divisibility law.

These are not interchangeable resources. Half occupancy of a quotient does not imply a large cheap linear subspace; a large quotient rank need not be cheaply generated; and a tiny cheap-subspace rank does not by itself prove that the actual endpoint needs the missing high-cost directions. Any closing argument must state which restriction is applied, what linear or quotient object survives, what source product is paid, whether the exceptional mode occurs, and which endpoint consequence consumes the resulting dimension or cost.

## Preserve matched controls, but require them to match the full hereditary incidence profile

The exchangeable controls of MC-295/MC-298 show that low-order combinatorial regularity can coexist with forbidden parity. MC-306 remains useful because it proves the previous aggregate package noncoercive, while MC-307--MC-310 show that a serious endpoint control must reproduce not only rank, energy, conductor scale, full radical, totient density and full quotient occupancy, but also target-projection occupancies, source-cut occupancies, source-product scale, exceptional-mode allowance and the linear geometry of uniformly cheap reciprocal frequencies.

A proposed theorem has discriminatory content only if the same hereditary and linear-subspace audits kill the matched control or are independently verified on it. Repackaging the old aggregate capacities, searching for a low-product source cut that Landau--Page already forces to half occupancy, or assuming that many individually cheap frequencies automatically span a large cheap sector is no longer a plausible route.
