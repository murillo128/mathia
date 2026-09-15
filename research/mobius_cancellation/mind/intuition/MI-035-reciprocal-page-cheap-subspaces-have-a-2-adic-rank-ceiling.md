# MI-035 — Reciprocal Page-cheap subspaces have a 2-adic rank ceiling

**Evidence level:** exact reciprocal-endpoint rank obstruction from [MC-310](../../findings/MC-310-reciprocal-endpoint-page-cheap-subspace-2-adic-rigidity.md), refining the low-source half-occupancy boundary of [MC-309](../../findings/MC-309-landau-page-half-occupancy-low-cost-source-cuts.md)

In the reciprocal one-defect endpoint extremizer, the `R` defect cells all have mass `1/R`, and a frequency indexed by a mask `a in F_2^R` has exact bias

`x_a=(-1)^|a|(1-2|a|/R)`.

Below the Page source scale, every nonexceptional cheap frequency has `|x_a|<=epsilon_y`. When `R epsilon_y<1`, the reciprocal `1/R` lattice leaves no room for an approximate middle layer: integrality forces every such mask exactly to Hamming weight `R/2`.

That pointwise statement becomes much stronger under linear closure. If a uniformly Page-cheap subspace `C<=F_2^R` has dimension `t`, choose a binary generator matrix and count its column types. Requiring every nonzero codeword to have weight exactly `R/2` makes every nonzero Walsh coefficient of the column-multiplicity function vanish, except possibly the one corresponding to the unique Page-exceptional mode. Walsh inversion then gives the divisibility laws

`2^t | R`

when no exceptional mode lies in `C`, and in general

`2^(t-1) | R`,

so

`t<=nu_2(R)` without the exception and `t<=nu_2(R)+1` always. If the exceptional mask has weight `j_*`, the sharper constraint is `t<=1+min(nu_2(R),nu_2(j_*))`.

The reusable mechanism is **discrete bias resolution plus linear closure**. A small-bias estimate that only implied an approximate occupancy statement for arbitrary sets becomes an exact code-theoretic restriction once the endpoint weights lie on a sufficiently coarse rational lattice and the cheap family is a subspace. The arithmetic gain is not another average over frequencies; it is the incompatibility between one-weight binary linear geometry and generic rank.

For the Möbius route this changes the proof obligation. It is no longer enough to argue that many low-cost characters exist individually or that a low-product quotient has moderate dimension. One must show that the actual source geometry forces enough of those characters to be **simultaneously cheap under addition** to form a subspace larger than the 2-adic ceiling, or else extract coercivity from the complementary directions that necessarily exceed the Page scale.

**Boundary.** The theorem is specific to the reciprocal equal-mass endpoint and the resolution regime `R epsilon_y<1`. It does not prove that the physical Legendre incidence system supplies a large uniformly cheap subspace, does not remove the one exceptional Page direction, and does not imply a Mertens estimate. The 2-adic ceiling is a source-capacity obstruction that becomes useful only if an independent arithmetic argument forces a larger cheap linear sector.
