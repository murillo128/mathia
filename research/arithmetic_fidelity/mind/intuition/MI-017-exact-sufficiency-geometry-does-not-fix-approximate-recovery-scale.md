# MI-017 — Stable recovery scale is set jointly by source complexity and observation structure

**Evidence level:** supported by exact Blaschke conditioning and exact adaptive Euler-cluster controls through AF-188

## Core intuition

Exact sufficiency does not determine stable recovery. The inverse scale is controlled jointly by the destination quotient/metric, the admissible source geometry, how source complexity may grow, the regularity and bandwidth of the observation map, and algebraic structure in the observation that can create or suppress resonant recovery channels.

The finite-Blaschke results show one local axis: after quotienting harmless phase, the interpolation/separation modulus controls the inverse slope. AF-180--AF-186 expose another axis that survives even when every source pair remains geometrically close and positive. By increasing a local cancellation order while keeping source separation exactly `W_1=delta`, one can drive observations below every fixed power whenever the available derivative budget cannot resolve that order.

AF-187--AF-188 add a crucial boundary: the same high-order controls cease to be uniformly invisible when the actual kernel contains a harmonic ladder and the observation bandwidth reaches the reciprocal-separation scale. Stable fidelity is therefore a **scale-dependent interaction between source complexity and observation structure**, not a one-sided regularity obstruction.

## Strongest justified principle

For a derivative envelope `|K^(m)| <= C A_delta^m M_m`, locality allows cancellation only up to an order `n_delta` with `n_delta delta -> 0`. AF-186 proves that the parity-split finite-difference controls optimize this mechanism through

`Omega_(M,n_delta)(t) = max_(1<=m<=n_delta) [m log t - log M_m]`, with `t=2/(A_delta delta)`.

The resulting forward envelope is `2C exp[-Omega]`. If `Omega/log(1/delta) -> infinity`, the observation discrepancy is super-algebraically smaller than the exact source distance `delta`, so no uniform inverse Hölder estimate can hold on a class containing those controls by a regularity-only argument.

For the Euler logarithm, however, AF-187 proves that every fixed positive reciprocal-band fraction detects the same controls at order one: high-order finite differencing becomes an odd residue-class harmonic filter when `delta T` stays bounded below. AF-188 calibrates the intermediate logarithmic regime. Under its isolating-order conditions, if `delta T log(1/delta) -> lambda in (0,infinity)`, the discrepancy has exponent

`log D_delta / log delta -> pi sigma x / lambda`,

up to the explicit logarithmic factor. Thus the same source family exhibits super-algebraic invisibility, algebraic visibility with a continuously varying exponent, and order-one visibility as the observation bandwidth crosses its natural scales.

## Counterevidence / boundary

The associated-function envelope is exact for one matched-control construction and declared derivative bound, not a converse theorem for the full inverse problem. A source class may forbid high-order positive clusters, and a kernel may contain additional algebraic structure not captured by derivatives alone.

Conversely, AF-187--AF-188 do not prove stable inversion of all generalized-prime sources. Their lower bounds separate one adaptive parity family by exploiting the Euler prime-power harmonic ladder; other source pairs may use different cancellations. The exact algebraic profile is also tied to a continuous vertical band and to the stated source-complexity conditions, including the locality/isolation constraints on `m_delta` and `q_delta`.

The Blaschke separation modulus, the adaptive-cluster associated function, and the Euler harmonic resonance describe different source/observation geometries. None should be silently substituted for another.

## Epistemic status

**Supported mechanism-level phase diagram from exact component theorems; no universal inverse theorem is claimed.**

## Falsification criterion

Invalidate the exact finite-difference/associated-function optimization, the Euler harmonic residue projection, or the AF-188 two-sided discrepancy scale. A purported universal recovery law based only on derivative regularity is also falsified if it predicts the same conditioning across the AF-186 low-band regime and the AF-187--AF-188 reciprocal/logarithmic regimes.

A positive source-class recovery theorem should identify the structural restriction or observation lower bound that blocks the relevant matched controls at the declared bandwidth.
