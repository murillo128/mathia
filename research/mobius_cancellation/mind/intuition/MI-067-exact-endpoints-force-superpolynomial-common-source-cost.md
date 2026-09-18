# MI-067 — Exact endpoints force superpolynomial common source cost

**Evidence level:** exact synthesis from [MC-377](../../findings/MC-377-smooth-subspace-prime-frame-forces-superpolynomial-source-cost.md).

Let `P` be the common lower-prime source radical of an exact endpoint package at shell scale `y`. MC-377 proves

`log P / log y -> infinity`.

Equivalently, every fixed `A>0` eventually fails as an upper bound `P<=y^A`. The obstruction is stronger than a fixed conductor floor. Assuming polynomial `P`, only `O_A(1)` source primes can lie above a suitable power `y^theta`. Killing the incidence columns of those rough primes leaves a mode subspace of dimension `R-O_A(1)` in which every package character and pair product has a smooth polynomial-size ambient modulus.

On that large subspace, the smooth-modulus incomplete-character theorem gives a fixed power saving inside the Selberg-sieve transfer. Bombieri's frame inequality then bounds the prime-frame row scale, while the exact endpoint partition forces a largest normalized Gram eigenvalue at least `2^(R-O_A(1))/R`. The two bounds are incompatible. The contradiction holds for every fixed polynomial exponent, so the source tariff escapes the entire fixed-power hierarchy rather than merely moving from quartic to a larger constant exponent.

This changes how the preceding endpoint geometry should be read. MC-372--MC-376 describe conditional near-equality structure inside `P=y^(4+o(1))`, but MC-377 proves that no actual exact endpoint inhabits that regime. The live quantitative object is therefore the **rate of divergence** of `log P/log y`, or an architecture that avoids realization through one common lower-prime radical altogether.

The existing smooth-character proof is fixed-parameter: the roughness threshold, differencing depth, exceptional-prime set and Selberg cutoff depend on the hypothetical fixed `A`. Extracting a growing lower bound requires those constants to remain uniform when `A=A(y)` moves. That is a distinct theorem, not contained in the qualitative divergence.

**Boundary.** Superpolynomial source cost is a source-realization obstruction, not a bound for `M(x)` and not an RH implication. It does not say how fast `log P/log y` diverges, how primitive conductors distribute in the true superpolynomial regime, or whether another endpoint representation can encode the same destination without paying this particular common-radical cost.