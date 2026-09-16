# MI-028 — Fiber variance certifies nonlinear heat-bath slowdown

**Evidence level:** exact operator synthesis from [VIS-254](../../findings/VIS-254-block-heat-bath-fiber-variance-nonlinear-slowdown.md), calibrated by the exact additive eigenmodes of [VIS-252](../../findings/VIS-252-uniform-triple-gibbs-linear-eigenmode.md) and [VIS-253](../../findings/VIS-253-additive-invariants-random-block-gibbs-eigenmodes.md). The underlying heat-bath Dirichlet identity is classical.

For an exact fixed-weight block heat-bath chain, each block update is conditional expectation and hence an orthogonal projection in `L^2(mu)`. If

`D_f = sum_B w_B E[Var(f | F_(B^c))]`,

then the normalized ratio `delta_f=D_f/Var(f)` is exactly the Rayleigh quotient of `I-P`. The one-step correlation is `1-delta_f`, the spectral gap is at most `delta_f`, and positivity of the heat-bath spectrum gives

`tau_int(f) >= 2/delta_f - 1`.

The VIS-252--VIS-253 ordinary and logarithmic coordinate contrasts are exact single-eigenvalue calibrations. For the uniform triple scan they have `delta=2/(m-1)` and attain equality, giving `tau_int=m-2`.

This makes `delta_f` a useful nonlinear certificate rather than merely a local sensitivity score. For the cut-averaged tent statistic `bar T`, the inner conditional variances can be computed from the exact one-dimensional VIS-248 triple fiber. If

`delta_(bar T) < 2/(m-1)`,

then `bar T` is rigorously slower in integrated autocorrelation than both universal linear benchmark families, before fitting any long-lag decay.

The converse is deliberately false: `delta_(bar T)>=2/(m-1)` does not prove fast mixing because a spectral mixture can retain mass near one. The certificate is therefore one-sided. It should be used after the exact linear/log implementation checks and before expensive separated-start/long-lag calibration, not as a replacement for the latter when the inequality fails.

**Boundary.** The result requires exact heat-bath conditionals and fixed state-independent scan weights. Approximate, Metropolis-within-Gibbs, adaptive or state-dependent kernels need their own operator analysis, and stationary outer expectations cannot be estimated reliably from an unvalidated chain merely because the inner fiber law is exact.
