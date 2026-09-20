# MI-039 — Dyadic switched response has an exact macroscopic signed nullspace

**Evidence level:** exact synthesis from FD-230--[FD-238](../../findings/FD-238-exact-dyadic-response-zeros-can-carry-macroscopic-signed-capacity.md). No Mertens or RH conclusion is claimed, and the exact nullspace construction is signed rather than a physical nonnegative occupancy.

FD-232--FD-233 identify the one-sided coefficient criterion inside a genuinely nontrivial switched-response class: a switched-preserving nonnegative lift exists exactly when the negative aggregate capacity of a signed representative is asymptotically negligible. FD-234 isolates the canonical real correction, while FD-235--FD-236 show that both the fixed-profile quotient and the natural capacity-normalized triangular quotient are too coarse: the source-forced block-Mertens correction itself becomes asymptotically switched-blind.

FD-238 makes the signed obstruction exact and independent of scalar normalization. There exists an integer sequence `b` with `|b_n|<=n` such that its divisor response `A b` satisfies

`(A b)(2^j)=0`

for every dyadic point, and hence

`((T-I)^r A b)(2^j)=0`

for every fixed finite-difference order `r>=1` and every `j`. These are not small coefficient directions. On dyadic bands, their normalized total variation has lower density at least `12/pi^2-1`, and both positive and negative parts retain at least half of that density asymptotically.

The consequence is stronger than the earlier request to choose a finer scalar normalization on the same dyadic rows. **No scalar strengthening of those same coordinates can control the signed geometry**, because the blind directions are exact zeros before normalization. A signed coercive topology must add genuinely new response information, such as off-dyadic/all-integer or source-forced coordinates, rather than merely rescale the existing dyadic switched family.

The one-sided route remains logically different. FD-230--FD-233 show that positivity can cut across signed null directions, and FD-238 does not construct an admissible nonnegative prime occupancy. The live physical question is therefore whether the concrete source-forced correction class is quantitatively transverse to this exact signed kernel once nonnegativity, finite capacities and source coherence are imposed, or whether additional response coordinates are required even after those restrictions.

FD-237 separately shows that interior integer realization is cheap in exact divisor-response coordinates: rounding in response space and applying the unimodular inverse costs only `tau(n)` in coefficients and bounded error in the existing switched rows. Thus bulk integrality should not be conflated with the exact signed-nullspace obstruction.

**Boundary.** The construction says nothing by itself about the distance of the physical nonnegative cone from the blind affine class, and a finer topology may make the bounded quantization error from FD-237 non-negligible. It proves only that the present dyadic switched coordinates, at any scalar normalization and any finite differencing order, cannot be a signed coercive coordinate system.