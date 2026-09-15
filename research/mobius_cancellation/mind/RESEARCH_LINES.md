# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Replace scalar endpoint capacity by a theorem on actual prime localization

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-033-current-endpoint-capacities-are-jointly-satisfiable`.

MC-293--MC-300 move the problem from individual character cost to the selected subset spectrum and price the current Page/Deuring--Heilbronn ceiling. MC-301--MC-302 give generic and quadratic family-energy bounds, but even an ideal loss-free quadratic large sieve of the same shape leaves an `O(log y)` capacity and a factor-`R` gap at the blind-support rank.

MC-303 packages the selected modes into a degree-`2^R` multiquadratic field; generic effective Chebotarev then pays through the huge discriminant. MC-304 exposes the finer common squarefree ramification radical `P`, with `|D_K|=P^(2^(R-1))`, and derives a necessary energy dichotomy between reduced-residue density and radical size.

MC-305 uses information those energy bounds discard. The exact endpoint partition occupies only `R` sign cells in `(Z/PZ)^*/ker Theta`, out of `2^R` available cells. Brun--Titchmarsh therefore forces

`log(y/P) <= (2+o(1)) R log y/2^R + O(1)`,

so at `2^R~kappa log y` the common radical must lie within a polylogarithmic factor of the shell scale.

MC-306 shows that this is still not contradictory. An explicit matched critical-scale source profile has `R` independent prime conductors near `y^(1/R)`, common radical

`y <= P <= kappa y log y`, `phi(P)/P -> 1`,

endpoint energy `2^R/R` comfortably below the fixed-radical capacity, and enough residue classes in every required one-defect sign cell. Rank, primitive-conductor scale, radical size, totient density, multiquadratic discriminant, Fourier energy and quotient-state cardinality can therefore satisfy all current necessary inequalities simultaneously.

The live theorem is no longer to combine those scalar capacities more efficiently. It must inject arithmetic localization that the matched model omits: rule out the required distribution of actual primes in `(y,2y]` among prescribed one-defect quadratic-sign cells for a modulus `P=y^(1+o(1))`, prove that the full shell source-cost map has unexpectedly cheap representatives incompatible with the model, or introduce another source invariant not determined by the current capacity package.

## Keep pointwise exceptional-zero control, family energy, field complexity, ramification capacity, quotient occupancy and prime localization separate

Page/Deuring--Heilbronn controls individual modes strongly but in a smaller conductor band. Large sieves control family energy. Multiquadratic packaging controls an algebraic field but can inflate discriminant through degree replication. MC-304 moves to the common radical and its totient density. MC-305 adds how many quotient sign cells the shell may occupy. MC-306 proves that all of those currencies can coexist at critical rank without realizing the actual shell-prime distribution.

These resources are not interchangeable. A family can satisfy energy and quotient-support capacities while the actual primes fail to populate the required cells; conversely, residue-class cardinality alone says nothing about prime occupancy in a dyadic shell when the modulus is already at shell scale. The next useful estimate must act on that source-to-target localization step rather than another relaxation of the same scalar budgets.

## Preserve matched controls and exact energy/support accounting as falsifiers

The exchangeable controls of MC-295/MC-298 show that low-order combinatorial regularity can coexist with forbidden parity. The reciprocal endpoint partition gives the sharp finite-geometric energy and quotient-support profiles. MC-306 now supplies a stronger matched control: a genuine independent quadratic source family whose conductor/radical geometry realizes every current scalar allowance simultaneously.

A closing theorem must therefore distinguish the physical endpoint from that matched source by changing at least one quantity the model does **not** already match — target-prime localization, ambient source-minimization cost, finer conductor correlations, or another arithmetic invariant. Repackaging the same rank/energy/radical/cell-count data without adding such a discriminator is no longer a plausible route.