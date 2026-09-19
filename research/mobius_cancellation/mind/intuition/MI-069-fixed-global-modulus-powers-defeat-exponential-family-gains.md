# MI-069 — Fixed global-modulus powers defeat exponential family gains

**Evidence level:** literature-grounded exact synthesis from [MC-383](../../findings/MC-383-small-doubling-family-mean-value-retains-global-modulus-horizon.md), interpreted against the source-cost architecture of MC-377--MC-382. The cited small-doubling theorem is prime-modulus and does not directly apply to the squarefree-composite endpoint; MC-383 uses its quantitative shape as an explicitly stronger stress test.

A collective family estimate can see many source directions at once and still fail to improve the endpoint source exponent if its analytic loss is paid against one global modulus. MC-383 makes that resource mismatch explicit.

In the endpoint specialization, grant a hypothetical composite-modulus extension of the small-doubling character-family theorem, delete its subpower loss, take a family of size `A=2^d`, and choose the most favorable fixed small-doubling parameter. Balancing the family mean value against the endpoint bias still requires

`P >> y^2 2^(3d/2)/(log y)^4`,

so

`log P >= 2 log y+(3/2)d log 2-4 log log y-O(1)`.

Even when `d` is a positive fraction of the source rank, the collective gain is only additive `O(R)` in `log P`. It does not create the `Omega(R log y)` scale needed for a rank-linear source exponent.

The mechanism is more general than that one theorem. Suppose a collective bound contains a favorable family factor `A^(-beta)` but also an unfavorable fixed global-modulus factor `q^theta`, with fixed `beta,theta>0`, while `A<=exp(CR)` and the interval length is only `N=y^(O(1))`. Balancing those resources can at best force

`log q=O(log y+R)`.

The exponential number of source configurations and the analytic modulus horizon live in different currencies. Family breadth contributes `log A=O(R)`, whereas a rank-linear source exponent asks for a gain of order `R log y`. A collective theorem helps only if its conductor dependence itself becomes factor-local, rank-sensitive or otherwise avoids paying a fixed positive power of the complete source modulus.

This sharpens the distinction already visible in MC-381--MC-382. Recovering source rank was necessary to remove a combinatorial square-root loss, but it did not remove q-vdC depth attenuation. Likewise replacing one-character estimates by a large family mean value is not enough when the theorem still prices the family through one global modulus.

The reusable design rule is therefore: **before crediting collective breadth, convert both the family gain and the conductor loss into the same physical source coordinate**. A theorem whose only rank gain is logarithmic in the family cardinality cannot produce a multiplicative `R` gain in the source exponent unless another analytic feature supplies the missing `log y` factor.

**Boundary.** MC-383 does not rule out collective character methods in general. It does not directly apply the cited prime-modulus theorem to the composite endpoint and does not prove an optimal source horizon. Factor-local conductor decompositions, multilinear estimates with no fixed positive full-modulus power, rank-decaying modulus exponents, gains of order `R log y`, or a different source-to-destination invariant remain outside the obstruction.