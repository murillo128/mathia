# MI-033 — Scalar endpoint capacities are jointly satisfiable, but projection separates the matched model

**Evidence level:** exact matched critical-scale compatibility construction from [MC-306](../../findings/MC-306-near-shell-singleton-source-profile-saturates-current-capacities.md), narrowed by the exact hereditary projection obstruction in [MC-307](../../findings/MC-307-hereditary-endpoint-projection-polynomial-source-cost.md)

At critical rank `2^R=kappa log y`, the aggregate constraints persisted through MC-306 do not contradict one another. MC-306 chooses `R` distinct odd primes `p_i in [z,2z]`, `z=y^(1/R)`, and the independent quadratic characters modulo those primes. Their full common radical

`P=prod_i p_i`

satisfies

`y <= P <= kappa y log y`, `phi(P)/P -> 1`,

while every nontrivial subset character has primitive conductor above the audited Page source scale. The same model fits the other aggregate budgets: selected Fourier energy `2^R/R` lies inside fixed-radical capacity, and the quotient has ample residue-class cardinality in every required one-defect sign cell.

So the original conclusion of MC-306 survives in a precise form: **rank, conductor scale, full radical, totient density, Fourier energy and full quotient-state cardinality are jointly satisfiable scalar capacities.** No recombination of only those aggregate inequalities can close the endpoint.

MC-307 shows why that statement must not be upgraded to “the source profile is fully matched.” The exact endpoint law is hereditary under coordinate restriction. Projecting to any proper `k` coordinates leaves at most `k+1` occupied sign cells, which forces the projected source radical `P_I` to satisfy

`P_I >= y^(1-(2+o(1))(k+1)/2^k)e^(-O(1))`.

For `k=6`, every six-subfamily therefore has `P_I >= y^(25/32-o(1))`. The disjoint-singleton MC-306 model instead has `P_I <= 2^k y^(k/R)=y^o(1)` for fixed `k` at critical rank. It is a valid matched control for the aggregate capacities and an invalid model for the endpoint's hereditary source geometry.

The reusable lesson is sharper than the earlier “capacity accounting can be complete without becoming coercive.” **An aggregate capacity can be saturated while the same object fails immediately after restriction.** Endpoint source complexity must therefore be audited as a profile over coordinate projections, not only through full-family totals.

What remains open is whether the actual lower-prime Legendre system can realize an independent endpoint family with this hereditary polynomial source profile. The surviving mechanism would have to make most directions individually expensive, make minimum representatives overlap strongly enough that small subfamilies already see near-shell radical, or satisfy another source constraint that explains the same projection pressure.

**Boundary.** MC-306 remains a correct aggregate matched construction; MC-307 does not refute it as such. MC-307 does not rule out the arithmetic endpoint, prove a Mertens estimate, or determine the overlap geometry of minimum source representatives. It proves only that the earlier disjoint-singleton control cannot realize the endpoint once hereditary projections are included.