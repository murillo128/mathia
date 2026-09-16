# MI-028 — Fiber dissipation moments certify nonlinear heat-bath slowdown

**Evidence level:** exact operator synthesis from [VIS-254](../../findings/VIS-254-block-heat-bath-fiber-variance-nonlinear-slowdown.md) and the sharp two-moment refinement [VIS-255](../../findings/VIS-255-two-moment-spectral-autocorrelation-certificate.md), calibrated by the exact additive eigenmodes of [VIS-252](../../findings/VIS-252-uniform-triple-gibbs-linear-eigenmode.md) and [VIS-253](../../findings/VIS-253-additive-invariants-random-block-gibbs-eigenmodes.md). The underlying heat-bath Dirichlet identities are classical.

For an exact fixed-weight block heat-bath chain, each block update is conditional expectation and hence an orthogonal projection in `L^2(mu)`. If

`D_f = sum_B w_B E[Var(f | F_(B^c))]`,

then the normalized ratio `delta_f=D_f/Var(f)` is exactly the Rayleigh quotient of `I-P`. The one-step correlation is `1-delta_f`, the spectral gap is at most `delta_f`, and positivity of the heat-bath spectrum gives the one-moment certificate

`tau_int(f) >= 2/delta_f - 1`.

VIS-255 shows that the next dissipation moment contains strictly more rigorous information. With the spectral variable `S=1-Z in [0,1]`, let

`delta=E[S]`, `eta=E[S^2]=||(I-P)f||^2/Var(f)`.

Then `delta^2<=eta<=delta`, and for `0<delta<1`, `eta<delta`,

`tau_int(f) >= B2(delta,eta) = 2(1-delta+delta^2-eta)/(delta-eta)-1`.

This is the sharp lower bound determined by the first two moments, attained by a two-point spectral law. Its improvement over `2/delta-1` is controlled by the spectral spread rather than by another fitted long-lag parameter.

For the exact block chain, `eta` also has a local residual representation: using two independent block choices `B,C` at the same stationary state,

`eta Var(f) = E[(f-K_B f)(f-K_C f)]`.

Thus both moments can be estimated from exact block/fiber operations without first fitting an autocorrelation tail. The VIS-252--VIS-253 ordinary and logarithmic coordinate contrasts remain exact single-eigenvalue calibrations; for the uniform triple scan they have `delta=2/(m-1)` and `tau_int=m-2`.

This sharpens the nonlinear gate for the cut-averaged tent statistic `bar T`. If `delta_(bar T)<2/(m-1)`, VIS-254 already certifies slowdown. If that one-moment test is inconclusive, VIS-255 can still certify nonlinear slowdown whenever `B2(delta_(bar T),eta_(bar T))>m-2`. Failure of both inequalities still does not prove fast mixing; separated-start and long-lag calibration remain necessary.

**Boundary.** The result requires an exact reversible heat-bath operator with the stated positivity and fixed state-independent scan weights. Approximate, Metropolis-within-Gibbs, adaptive or state-dependent kernels need their own operator analysis, and stationary outer expectations cannot be estimated reliably from an unvalidated chain merely because the inner fiber law is exact. The two-moment bound is optimal for the information `(delta,eta)` alone, not a reconstruction of the full spectrum.

**Falsification criterion.** For a claimed two-moment certificate, exhibit a spectral law on `[0,1]` with the same `(delta,eta)` and smaller integrated autocorrelation than `B2`, or show that the residual estimator fails under the declared exact heat-bath assumptions. For the visual null, failure to exceed the additive benchmark after both exact moment gates leaves the nonlinear slowdown question open rather than settled.
