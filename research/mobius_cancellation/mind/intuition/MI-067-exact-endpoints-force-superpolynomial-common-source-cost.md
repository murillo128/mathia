# MI-067 — Exact endpoints force a quantitatively superpolynomial common source cost

**Evidence level:** exact synthesis from [MC-377](../../findings/MC-377-smooth-subspace-prime-frame-forces-superpolynomial-source-cost.md) and [MC-378](../../findings/MC-378-moving-smooth-frame-forces-iterated-log-source-cost-rate.md).

Let `P` be the common lower-prime source radical of an exact endpoint package at shell scale `y`, with source rank `R`. MC-377 proves the qualitative escape

`log P / log y -> infinity`,

so every fixed `A>0` eventually fails as an upper bound `P<=y^A`. MC-378 upgrades this from a fixed-parameter contradiction to a moving-parameter theorem. There are absolute constants such that `P<=y^A` is impossible whenever

`A^2=o(R)` and `A 2^(C A)=o(log log y)`.

A concrete nonoptimized consequence is

`log P/log y >= c min{sqrt(R/log(R+2)), log log log y}`

for some absolute `c>0` and all sufficiently large shells.

The mechanism explains exactly where the rate comes from. Assuming `P<=y^A`, choose a roughness threshold of order `1/A`. Killing the incidence columns of source primes above that threshold and the moving exceptional-prime set costs only `O(A^2)` dimensions, leaving a mode space of dimension `R-O(A^2)`. Every surviving package character and pair product then has a smooth polynomial-size ambient modulus. The moving smooth-character estimate supplies a saving `sigma_A` no worse than exponentially small in `A`; choosing the Selberg cutoff proportionally to that saving keeps the diagonal cost controlled. Bombieri's frame inequality then gives an upper bound incompatible with the exponential normalized Gram eigenvalue forced by the exact endpoint partition.

This changes the source-cost picture twice. MC-372--MC-376 describe conditional near-equality structure inside `P=y^(4+o(1))`, but MC-377 proves no exact endpoint inhabits any fixed-power regime. MC-378 now shows that the escape is not merely qualitative: within the current smooth-character/frame architecture the common radical must climb at least through an explicit iterated-log/rank-dependent exponent.

The rate should not be mistaken for an intrinsic optimum. Its bottlenecks are visible: the rough-column codimension is quadratic in `A`, while the moving character saving deteriorates exponentially with the differencing depth. Improving either uniformity could strengthen the exponent; changing the endpoint representation could evade the common-radical tariff entirely.

**Boundary.** This is a source-realization obstruction, not a bound for `M(x)` and not an RH implication. It does not prove that the displayed lower bound is sharp, nor that every alternative endpoint architecture pays the same currency. What is now ruled out is broader and quantitative: an exact endpoint cannot be implemented by one common lower-prime radical whose exponent stays below the stated moving threshold.