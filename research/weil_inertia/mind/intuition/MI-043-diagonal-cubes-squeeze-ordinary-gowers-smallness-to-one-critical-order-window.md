# MI-043 — Diagonal cubes close the ordinary-Gowers escape at the natural critical threshold

**Evidence level:** exact synthesis from [WI-332](../../findings/WI-332-u2-smallness-cannot-control-bow-sliding-variance.md)--[WI-338](../../findings/WI-338-hypercontractive-cube-concentration-closes-all-start-gowers-gap.md). The Gowers norms, Walsh expansion, hypercontractivity and Rademacher comparison mechanism are classical; the Mathia content is the matched-energy two-sided squeeze at the bow scale and its implication for the ordinary-Gowers proof interface.

Earlier countermodels showed that local `U^2`, square-root cancellation against fixed-degree phases, and every fixed finite hierarchy of small local Gowers norms can coexist with full diagonal-scale sliding variance. WI-335 extended that obstruction to slowly growing order. WI-336 identified the complementary high-order barrier from the same matched energy.

For an interval of length `L` and a sequence with energy `E` comparable to `L log N`, the zero-increment cubes alone force

`||f||_(U^s(I)) >= sqrt(E/(2L)) L^(-1/2^s)`.

At the bow scale define

`R_s(L,N)=2^s loglog N/log L`.

WI-336 shows that any comparable-energy source cannot have ordinary normalized `U^s=o(1)` once `R_s>=2+eta`. WI-337 showed that a matched-energy Rademacher realization can remain `U^s=o(1)` on a density-one set of bow intervals for every fixed margin below `R_s=2`, while those same intervals retain full diagonal sliding variance.

WI-338 removes the remaining all-start gap. Let `K=N^(kappa+o(1))` and choose `delta_N` with `delta_N loglog N->infinity`. A single matched-energy Rademacher realization can be chosen so that for **every** interval `I` with `K<=|I|<=2K` and every retained order satisfying

`R_s(K,N)<=2-delta_N`,

one has `||b||_(U^s(I))=o(1)`, while the same sequence obeys the full sliding-variance law `(1+o(1))NK log N` against any prescribed unit-modulus carrier.

The all-start upgrade comes from concentration at the actual cube-count fluctuation scale rather than worst-case sign sensitivity. Writing the random normalized cube count in Walsh characters, WI-338 bounds the multiplicity of each nonconstant character by a subpower factor, obtains an `L^2` fluctuation far below the mean `1/L` scale, and uses Bonami--Beckner hypercontractivity to union-bound over every interval and every relevant order. This makes the generic countermodel reach exactly as far below `R_s=2` as the deterministic diagonal floor permits.

The two sides now meet at the natural resolution. If `R_s=2-delta_N` with `delta_N loglog N=O(1)`, the diagonal floor itself prevents `U^s=o(1)` for any comparable-energy source. If `delta_N loglog N->infinity`, WI-338 supplies an all-interval countermodel with `U^s=o(1)` and full variance. Thus there is no residual ordinary-Gowers order window whose mere smallness can force the desired bow covariance, even when the arithmetic theorem is all-start.

The reusable lesson is that **a norm hierarchy can saturate exactly at a source-imposed diagonal wall**. Below the wall, generic pseudorandom models satisfy the norm constraints while preserving the destination obstruction; at the wall, the same source energy makes the norm constraint impossible. Strengthening only the order or start quantifier cannot create the missing signed information. A useful replacement must change the observable: remove/renormalize the diagonal cubes, retain source-specific shifted-prime covariance, use a relative linear-forms statistic that remembers `Lambda^sharp`, or otherwise couple directly to the off-diagonal sign consumed by the destination.

For Weil inertia the destination remains the distinguished bow twist. The exact variance needs a macroscopic negative off-diagonal term to beat its positive diagonal contribution. WI-338 does not supply that sign; it establishes that ordinary Gowers smallness cannot supply it as a black-box consequence at any order where such smallness is itself compatible with the source energy.

**Boundary.** WI-338 does not construct an arithmetic counterexample with the prime singular series, describe the actual `Lambda-Lambda^sharp` covariance, or rule out a diagonally renormalized higher-order statistic. The transition exactly at finite `delta_N loglog N` is governed by the deterministic diagonal floor rather than a new covariance theorem. The result closes the ordinary-Gowers interface, not the source-specific arithmetic covariance problem.
