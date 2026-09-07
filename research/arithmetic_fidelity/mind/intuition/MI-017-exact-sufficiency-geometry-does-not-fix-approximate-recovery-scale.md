# MI-017 — Stable recovery scale is set jointly by source complexity and observation regularity

**Evidence level:** supported by exact Blaschke conditioning and exact adaptive local-cluster obstructions through AF-186

## Core intuition

Exact sufficiency does not determine stable recovery. The inverse scale is controlled jointly by the destination quotient/metric, the admissible source geometry, how source complexity may grow, and the regularity/bandwidth of the observation map.

The finite-Blaschke results show one local axis: after quotienting harmless phase, the interpolation/separation modulus controls the inverse slope. AF-180--AF-186 expose another axis that survives even when every source pair remains geometrically close and positive. By increasing a local cancellation order while keeping the source separation exactly `W_1=delta`, one can drive the observed discrepancy below every fixed power whenever the derivative budget cannot resolve that order.

## Strongest justified principle

For a derivative envelope `|K^(m)| <= C A_delta^m M_m`, locality allows cancellation only up to an order `n_delta` with `n_delta delta -> 0`. AF-186 proves that the parity-split finite-difference controls optimize this mechanism exactly through

`Omega_(M,n_delta)(t) = max_(1<=m<=n_delta) [m log t - log M_m]`, with `t=2/(A_delta delta)`.

The resulting forward envelope is `2C exp[-Omega]`. If `Omega/log(1/delta) -> infinity`, the observation discrepancy is super-algebraically smaller than the exact source distance `delta`, so no uniform inverse Hölder estimate can hold on a class containing those controls.

AF-185 is the Gevrey specialization: `M_m=(m!)^q` converts the regularity order `q` into a logarithmic resolution penalty `[log(1/delta)]^q`. This explains why fixed-order moment tests can look stable while an adaptive family crosses a qualitatively different resolution boundary.

## Counterevidence / boundary

The associated-function envelope is exact for this matched-control construction and declared derivative bound, not a converse theorem for the full inverse problem. A source class may forbid high-order positive clusters, a kernel may contain additional algebraic structure not captured by the derivative envelope, or an independent lower bound may restore stability above the obstruction scale.

Likewise the Blaschke separation modulus and the adaptive-cluster associated function describe different source geometries; neither should be silently substituted for the other.

## Epistemic status

**Exact mechanism-level conditioning laws with an open source-specific converse problem.** The durable lesson is that stable recovery requires a declared complexity/regularity regime in addition to exact sufficiency.

## Falsification criterion

Produce a uniform inverse estimate on a source class containing the AF-186 adaptive controls in a regime where the truncated associated-function exponent dominates every logarithmic power, or invalidate the exact finite-difference/derivative-envelope optimization. A positive recovery theorem should instead identify the structural source restriction or observation lower bound that blocks those controls.