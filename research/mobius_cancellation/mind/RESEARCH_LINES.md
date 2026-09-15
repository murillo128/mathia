# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Close the explicit collective-capacity gap at the blind-support frontier

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-032-endpoint-quotient-occupancy-forces-the-common-radical-near-the-shell-scale`.

MC-293--MC-300 move the problem from individual character cost to the selected subset spectrum and price the current Page/Deuring--Heilbronn ceiling. MC-301--MC-302 give generic and quadratic family-energy bounds, but even an ideal loss-free quadratic large sieve of the same shape leaves an `O(log y)` capacity and a factor-`R` gap at the blind-support rank.

MC-303 packages the selected modes into a degree-`2^R` multiquadratic field; generic effective Chebotarev then pays through the huge discriminant. MC-304 exposes the finer common squarefree ramification radical `P`, with `|D_K|=P^(2^(R-1))`, and derives a necessary energy dichotomy between reduced-residue density and radical size.

MC-305 now uses information that those energy bounds discard. The exact endpoint partition occupies only `R` sign cells in the quotient `(Z/PZ)^*/ker Theta`, out of `2^R` available cells. Brun--Titchmarsh therefore forces

`log(y/P) <= (2+o(1)) R log y/2^R + O(1)`.

At `2^R~kappa log y`, the common radical must satisfy

`P >= y/(log y)^(2/(kappa log 2)+o(1))`.

Thus even the totient-density branch of MC-304 cannot hide inside an arbitrarily small radical: endpoint **support occupancy** already pushes `P` to near shell scale. The live theorem is sharper still: rule out the remaining near-shell radical configurations for the actual selected family, prove that the required `R` sign cells cannot have the endpoint multiplicities, or show that the actual obstruction carries more energy/rank than the reciprocal extremizer.

## Keep pointwise exceptional-zero control, family energy, field complexity, ramification capacity and quotient occupancy separate

Page/Deuring--Heilbronn controls individual modes strongly but in a smaller conductor band. Large sieves control family energy. Multiquadratic packaging controls an algebraic field but can inflate discriminant through degree replication. MC-304 moves to the common radical and its totient density. MC-305 adds a further invariant: how many quotient sign cells the shell is allowed to occupy.

These currencies are not interchangeable. A family can satisfy an energy-capacity bound yet fail the residue-class occupancy needed to realize its endpoint sign pattern; conversely a near-shell radical can satisfy the new counting bound without supplying the required arithmetic distribution among the selected cells.

## Preserve matched controls and exact energy/support accounting as falsifiers

The exchangeable controls of MC-295/MC-298 show that low-order combinatorial regularity can coexist with forbidden parity. The reciprocal endpoint partition gives both the sharp finite-geometric energy profile and, by MC-305, a sharply concentrated quotient-support profile. A successful closing theorem must now alter at least one of the surviving currencies: endpoint energy/rank, radical size/totient roughness, or actual occupancy of the `R` selected sign cells. Repackaging the same modes without changing one of those quantities is not progress.