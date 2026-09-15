# MI-021 — Fixed-count pair calibration removes Poissonization noise

**Evidence level:** exact finite variance comparison from [VIS-238](../../findings/VIS-238-fixed-count-tent-calibration-removes-poissonization-variance.md), applied to the origin-quotiented triangular pair statistic of [VIS-237](../../findings/VIS-237-random-origin-cell-collisions-are-triangular-pair-functional.md).

Once grid-origin averaging turns same-cell collisions into a triangular pair-gap functional, the next control choice is not innocuous. The prime-coordinate sample at a fixed height contains a fixed observed number of points. An unconditioned Poisson process varies that count and therefore injects a source of pair-count variance that the observed representation does not possess.

VIS-238 makes the discrepancy exact at critical occupancy `kappa=m ell/L=Theta(1)`. For `m` uniform points with fixed count, the tent-pair statistic has

`Var(T_m)=m kappa/3+O(1)`.

For the corresponding unconditioned Poisson process with mean count `m`, the variance is

`m(kappa/3+kappa^2)+O(1)`.

The extra leading `m kappa^2` term is exactly the total-count fluctuation channel exposed by conditioning. It is not short-gap geometry and cannot be used as evidence that the fixed-count prime sample is unusually rigid or structured.

The reusable lesson is that **a representation-faithful null must match the sigma-field already fixed by data acquisition before residual variance is interpreted**. Exact nuisance quotienting and stochastic calibration are separate operations: VIS-237 removes grid phase, while VIS-238 shows that count randomness must also be removed when the statistic is evaluated at fixed count.

This still leaves a genuine modeling problem. Fixed-count uniform order statistics are only the minimal homogeneous calibration. A prime-sensitive test may need a frozen nonuniform intensity, an independently justified gap law or another ordered-point baseline. The arithmetic question begins only after those generic geometric effects have been priced without conditioning away the statistic itself.

**Boundary.** VIS-238 is a null-calibration theorem, not evidence of an anomalous prime residual. It does not establish that the fixed-count uniform model is the correct final baseline, describe prime short-gap dependence, or imply an RH consequence. Its role is to remove one artificial variance channel before source-sensitive interpretation.