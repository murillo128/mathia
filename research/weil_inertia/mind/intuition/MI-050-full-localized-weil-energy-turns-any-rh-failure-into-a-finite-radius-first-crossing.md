# MI-050 — Full localized Weil energy turns RH failure into a finite first crossing whose threshold regularity is controlled by the null equation

**Evidence level:** exact synthesis from `WI-355`--`WI-357`, using Suzuki's localized Weil-form framework.

For the localized Weil form on `(-a,a)`, let `lambda(a)` be the lowest normalized energy. Suzuki's framework makes `lambda(a)` continuous, positive for sufficiently small `a`, and negative at some finite radius iff RH fails; nested test spaces make it monotone. Under `not RH` there is therefore a canonical finite first crossing `a_*` with `lambda(a_*)=0`, and zero is an actual ground-state eigenvalue. At aperture `a`, only prime powers up to `e^(2a)` enter the arithmetic source ledger.

WI-356 shows that a newly activated prime-power channel is singular in the wrong topology. At `a_q=(log q)/2`, its compressed-translation operator is zero exactly at threshold but has full coefficient-size `L^2` operator norm immediately above it. The same channel is nevertheless small relative to Suzuki's logarithmic form, with a coefficient tending to zero like an inverse logarithm. Vectors that nearly saturate the ambient norm jump must concentrate in shrinking endpoint strips and drive their logarithmic energy to infinity.

WI-357 closes the missing compatibility step for actual null/ground states. Suzuki's fixed-domain null identity yields an explicit finite bound

`Lbar(w) <= B(a)`

for every normalized null state. His Fourier representation then gives an explicit inverse-logarithmic modulus for the zero-extended autocorrelation on bounded-`Lbar` sets, and hence a quantitative modulus in the aperture parameter for the whole finite source ledger. Actual first-crossing states therefore cannot exploit the ambient `L^2` norm discontinuity.

Combining that bounded-energy modulus with the WI-356 endpoint estimate gives a sharper inheritance statement. If a null state occurs just above a prime-power threshold, deleting the newly activated channel leaves an approximate null state for the form that was already present before the threshold. In particular, a new prime atom cannot create a crossing out of a fixed positive reserve.

The first-crossing program has therefore moved from **regularity** to **coercive reserve**. Bounding logarithmic energy is no longer an independent open theorem, and neither is qualitative threshold continuity. What remains is to prove that the pre-existing/source-deleted form has enough positive reserve along the threshold sequence, or to use the exact null equation to derive an arithmetic sign/cancellation condition incompatible with the inherited near-null state. A reserve that merely stays positive pointwise may still decay too quickly for local exclusion neighborhoods to globalize.

The reusable distinction is between three topologies/resources: ambient operator norm, the source-selected logarithmic form domain, and the actual coercive margin. An arithmetic channel can be large in the first, small in the second, and still threaten positivity if the third tends to zero. The topology removes false singularities; it does not supply the sign theorem.

**Boundary.** WI-357 gives explicit bounded-energy and continuity estimates but no uniform spectral gap, no global threshold induction and no lower bound on `lambda(a_q)`. The already-active prime terms, archimedean term and continuous remainder remain part of the source-deleted form. No RH conclusion follows without the missing reserve/arithmetic-sign input.