# MI-041 — Positive Riesz order crosses the critical regularity threshold, but removing the smoothing remains endpoint-sized

**Evidence level:** exact/literature-derived boundary statement from [AF-352](../../findings/AF-352-every-positive-riesz-order-crosses-the-critical-boundary-conditioning-threshold.md), quantitatively sharpened by [AF-353](../../findings/AF-353-riesz-endpoint-conditioning-cost-diverges-quadratically-in-absolute-zero-budget.md) through [AF-358](../../findings/AF-358-riesz-smoothing-crosses-half-derivative-threshold-but-endpoint-difference-does-not.md)

For fixed real `delta>0`, the Riesz profile

`R_delta[Lambda-1](X)=sum_(n<=X)(Lambda(n)-1)(1-n/X)^delta`

has the exact qualitative transition

`RH <=> R_delta[Lambda-1](X)=O_delta(sqrt(X))`,

whereas `delta=0` cannot satisfy the same bound. On the critical line the Mellin coefficient `B(rho,1+delta)` decays like `Gamma(1+delta)|gamma|^(-1-delta)`, so every fixed positive order improves high-frequency regularity without moving the off-critical singularity discriminator.

AF-358 makes the regularity gain exact. Under RH, for the zero-spectrum weighted Fourier--Besicovitch scale,

`||E_delta||_(H^s_(B,zeta)) < infinity  <=>  s < 1/2 + delta`.

Thus a fixed positive order buys exactly `delta` derivatives on the zeta-zero spectrum. Since `s>1/2` is enough, by Riemann--von Mangoldt plus Cauchy--Schwarz, to make the zero coefficients absolutely summable, every fixed `delta>0` crosses the ordinary uniform-convergence gate.

The singular limit is different. For every fixed `delta>0`,

`||E_delta-E_0||_(H^s_(B,zeta)) < infinity  <=>  s < 1/2`,

and for every fixed `s<1/2`,

`||E_delta-E_0||_(H^s_(B,zeta)) = O_s(delta)` as `delta->0+`.

So increasing the quadratic Sobolev weight does not repair AF-356's topology split. The smoothed profile itself crosses the half-derivative threshold, but the operation of removing the smoothing leaves an endpoint-sized high-frequency tail and never reaches the `s>1/2` absolute-summability region. The obstruction is therefore not merely that ordinary `B^2` was too weak.

AF-354--AF-355 show the same singularity in the moving physical profile: sufficiently fast `delta(X)->0` inherits the Hardy--Littlewood endpoint oscillation, and under RH every polynomially vanishing order fails the sharp `O(sqrt X)` profile. AF-356 shows that this can coexist with `B^2`-Lipschitz continuity and limiting-law convergence. AF-357 then identifies the physical resolution hidden in the parameter: the Beta kernel samples relative endpoint lags `exp(-Theta(1/delta))`, and the `min(1,delta log X)` endpoint modulus is sharp for arguments using only a scalar partial-sum envelope plus pointwise jump control.

The spectral and physical descriptions now match. For small `delta`, the smoothed coefficient is endpoint-like through a huge frequency range and only gains the extra `gamma^(-delta)` damping beyond a moving scale of exponential type in `1/delta`; in physical space the kernel likewise reaches exponentially thin endpoint shells. The singular limit is therefore a **moving-bandwidth problem**.

The reusable proof obligation is narrow: a uniform moving-order theorem must exploit information absent from monotone quadratic zero-mode energies and scalar source envelopes. Candidate resources include phase cancellation, maximal/tail control, signed short-interval coupling, endpoint-to-past correlation or another source-native cross-scale constraint. Merely adding finitely many frequency weights to the same quadratic energy cannot cross the endpoint comparison barrier.

**Boundary.** AF-358 is conditional on RH and concerns the nontrivial-zero Fourier profile. The half-derivative obstruction rules out the ordinary weighted-`ell^2` route to uniform endpoint comparison; it does not rule out phase-sensitive, nonlinear, maximal or arithmetic-specific estimates. No moving-order RH criterion is proved, and the true growth of the cancellation-aware norm `K(delta)` remains unknown.