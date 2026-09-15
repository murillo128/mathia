# MI-034 — Endpoint sparsity is hereditary under projection and forces polynomial source cost

**Evidence level:** exact endpoint-projection source-complexity obstruction from [MC-307](../../findings/MC-307-hereditary-endpoint-projection-polynomial-source-cost.md), using the source-cost setup of MC-293 and the audited Brun--Titchmarsh mechanism of MC-305

The one-defect endpoint law remains sparse after forgetting coordinates. If `I` is any proper set of `k` selected shell functionals, then the projected sign vector can only be all minus or have its unique plus in one of the `k` retained coordinates. Thus the projected shell occupies at most `k+1` sign cells out of `2^k`.

Let `P_I` be the squarefree radical of minimum lower-prime representatives for those coordinates. Applying Brun--Titchmarsh to the available residue classes gives

`log(y/P_I) <= (2+o(1))(k+1)log y/2^k + O(1)`,

so

`P_I >= y^(1-(2+o(1))(k+1)/2^k)e^(-O(1))`.

Because `P_I <= prod_{i in I} Q_i`, the same exponent lower-bounds the product of the minimum source costs. At the strongest fixed projection dimension `k=6`, every six selected directions satisfy

`prod_{i in I} Q_i >= y^(25/32-o(1))`,

and hence the sixth-smallest selected cost obeys

`Q_(6) >= y^(25/192-o(1))`.

So all but at most five endpoint directions are individually expensive at a fixed polynomial scale. In the growing regime `k/2^k -> 0`, every `k`-subfamily must collectively see radical `y^(1-o(1))`.

This changes the source geometry. A near-shell **full** radical can be assembled from many cheap almost-disjoint coordinates, as MC-306 demonstrates, but such a construction collapses under restriction: for fixed `k`, its projected radical is only `y^o(1)`. The actual endpoint cannot collapse this way. Its source complexity must survive coordinate deletion.

The reusable principle is therefore: **for a sparse endpoint law, test complexity hereditarily, not only in aggregate.** A source model is not genuinely matched merely because it reproduces full-family rank, energy, conductor, radical and quotient capacities; it must also reproduce the capacities of the endpoint after projection to smaller coordinate sets.

For the Möbius line this leaves a concrete arithmetic frontier. Any surviving independent endpoint family must obtain the hereditary profile from polynomially expensive directions, heavy overlap of minimum lower-prime representatives, or a different source mechanism with the same restriction stability.

**Boundary.** The projected bounds are necessary conditions for the exact endpoint partition. They do not rule that partition out, determine the minimum representatives, imply global Möbius cancellation, or show that hereditary source complexity is sufficient for an RH-scale estimate.