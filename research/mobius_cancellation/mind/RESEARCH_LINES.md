# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Exploit hereditary endpoint source complexity before adding another scalar capacity

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-034-endpoint-sparsity-is-hereditary-under-projection`.

MC-293--MC-300 move the problem from individual character cost to the selected subset spectrum and price the current Page/Deuring--Heilbronn ceiling. MC-301--MC-302 give generic and quadratic family-energy bounds, but even an ideal loss-free quadratic large sieve of the same shape leaves an `O(log y)` capacity and a factor-`R` gap at the blind-support rank.

MC-303 packages the selected modes into a degree-`2^R` multiquadratic field; generic effective Chebotarev then pays through the huge discriminant. MC-304 exposes the finer common squarefree ramification radical `P`, with `|D_K|=P^(2^(R-1))`, and derives a necessary energy dichotomy between reduced-residue density and radical size. MC-305 then uses the endpoint's occupation of only `R` out of `2^R` quotient sign cells to force the full common radical to the shell scale.

MC-306 is still the decisive matched control for those **full-family scalar** quantities. Its independent prime conductors near `y^(1/R)` simultaneously realize critical rank, primitive-conductor scale, a near-shell full radical, totient density, multiquadratic discriminant, Fourier energy and quotient-state cardinality. Those aggregate capacities therefore do not contradict one another.

MC-307 finds the information that this control omits. Project the exact one-defect endpoint partition to any proper `k` selected coordinates. Only the `k` one-defect cells and the all-minus cell remain, so the projection occupies at most `k+1` of the `2^k` sign cells. If `P_I` is the common radical of minimum lower-prime representatives for those coordinates, Brun--Titchmarsh gives

`log(y/P_I) <= (2+o(1))(k+1)log y/2^k + O(1)`,

hence

`P_I >= y^(1-(2+o(1))(k+1)/2^k)e^(-O(1))`.

Since `P_I <= prod_{i in I} Q_i`, this is also a hereditary source-cost bound. Already `k=6` forces every six-subfamily product to be at least `y^(25/32-o(1))`, and therefore all but at most five selected directions have minimum source cost at least `y^(25/192-o(1))`. More generally, whenever `k/2^k -> 0`, every such `k`-subfamily must collectively see radical `y^(1-o(1))`.

This destroys the disjoint-singleton realization from MC-306 as a model of the actual endpoint: its fixed-`k` projected radicals are only `y^o(1)`. The endpoint itself remains open. The live question is now whether the actual lower-prime Legendre system can support an independent endpoint family whose source complexity survives **every relevant coordinate projection**. A surviving realization must make most directions polynomially expensive, force strong overlap among minimum representatives, or exhibit another mechanism that satisfies the same hereditary profile.

## Keep pointwise zero control, family energy, full radical, quotient occupancy, hereditary projection and target localization separate

Page/Deuring--Heilbronn controls individual modes strongly but in a smaller conductor band. Large sieves control family energy. Multiquadratic packaging controls an algebraic field but can inflate discriminant through degree replication. MC-304 moves to the common radical and its totient density. MC-305 prices full quotient occupancy. MC-306 proves that these aggregate currencies can coexist at critical rank.

MC-307 adds a genuinely different currency: **restriction stability of source complexity**. A large full radical can be assembled from many cheap almost-disjoint coordinates, but that mechanism collapses after projecting to a fixed small subfamily. The exact endpoint does not collapse in the same way because its projected sign law remains exponentially sparse: only `k+1` cells survive out of `2^k`.

This does not make actual prime localization irrelevant. The projected Brun--Titchmarsh argument is itself a localization constraint, but it still supplies only a necessary hereditary profile. The next useful theorem must act on the arithmetic geometry of the minimum lower-prime representatives — their overlap, individual cost, compatibility across many projections, or their interaction with family-energy/zero-free information — or else add a target-prime statement not already encoded by that profile.

## Preserve matched controls, but require them to match the hereditary profile

The exchangeable controls of MC-295/MC-298 show that low-order combinatorial regularity can coexist with forbidden parity. The reciprocal endpoint partition gives the sharp finite-geometric energy and quotient-support profiles. MC-306 remains valuable because it demonstrates that the previous aggregate package was noncoercive, but MC-307 proves that it is **not** a matched endpoint control once coordinate projections are audited.

Future controls must therefore reproduce not only rank, energy, conductor scale, full radical, totient density and full quotient occupancy, but also the source cost seen after restriction to small and growing coordinate subsets. A proposed closing theorem has real discriminatory content only if the same hereditary test either kills the control or is independently verified on it. Repackaging the old aggregate capacities without this restriction test is no longer a plausible route.