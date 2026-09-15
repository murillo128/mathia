# MI-032 — Endpoint quotient occupancy forces the common radical near the shell scale

**Evidence level:** exact/literature-derived support-capacity bound from [MC-305](../../findings/MC-305-endpoint-coset-occupancy-forces-near-shell-radical.md), sharpening the common-radical dichotomy in [MC-304](../../findings/MC-304-fixed-ramification-radical-capacity-dichotomy.md)

For `R` independent quadratic source characters induced to one squarefree radical `P`, the map

`Theta:(Z/PZ)^* -> {±1}^R`

is onto and each sign cell contains `phi(P)/2^R` residue classes. The reciprocal endpoint partition is much more concentrated than its energy alone records: every shell prime has exactly one defect coordinate, so the shell occupies only `R` of the `2^R` sign cells.

After the fixed condition `r=1 mod 4`, the shell therefore lies in exactly

`R phi(P)/2^R`

reduced residue classes modulo `4P`. Brun--Titchmarsh then gives the necessary condition

`log(y/P) <= (2+o(1)) R log y / 2^R + O(1)`.

At critical rank `2^R~kappa log y`, this becomes

`P >= y/(log y)^(2/(kappa log 2)+o(1))`.

So the common radical cannot be an arbitrarily small carrier even on the totient-density escape left by MC-304. **Endpoint support concentration itself forces the ramification radical to within a polylogarithmic factor of the shell scale at critical rank.** This is a different constraint from selected-family energy and from the multiquadratic discriminant.

The reusable distinction is between energy capacity and quotient-support capacity. A family may fit a mean-square bound yet still require enough residue classes to host the endpoint sign patterns. When the obstruction occupies only a tiny subset of the available quotient states, counting those states can force source complexity that energy estimates miss.

**Boundary.** The bound is necessary, not contradictory: `P=y/(log y)^O(1)` or larger remains possible, and no theorem here controls whether the required sign cells occur with the endpoint multiplicities for the actual source. No Mertens estimate follows.