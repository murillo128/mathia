# MI-041 — Positive Riesz order crosses the critical regularity threshold, but removing the smoothing is an exponential-bandwidth endpoint problem

**Evidence level:** exact/literature-derived boundary statement from [AF-352](../../findings/AF-352-every-positive-riesz-order-crosses-the-critical-boundary-conditioning-threshold.md), quantitatively sharpened by [AF-353](../../findings/AF-353-riesz-endpoint-conditioning-cost-diverges-quadratically-in-absolute-zero-budget.md) through [AF-359](../../findings/AF-359-riesz-endpoint-has-universal-exponential-spectral-transition.md).

For fixed real `delta>0`, the Riesz profile

`R_delta[Lambda-1](X)=sum_(n<=X)(Lambda(n)-1)(1-n/X)^delta`

has the exact qualitative transition

`RH <=> R_delta[Lambda-1](X)=O_delta(sqrt(X))`,

whereas `delta=0` cannot satisfy the same bound. On the critical line the Mellin coefficient gains the factor `gamma^(-delta)`, so every fixed positive order improves high-frequency regularity without moving the off-critical singularity discriminator.

AF-358 makes the regularity gain exact. Under RH,

`E_delta in H^s_(B,zeta) <=> s < 1/2 + delta`,

whereas for every fixed `delta>0`,

`E_delta-E_0 in H^s_(B,zeta) <=> s < 1/2`.

Thus a fixed positive order crosses the ordinary absolute-summability/uniform-convergence gate, but removing the smoothing leaves an endpoint-sized high-frequency tail. For every fixed `s<1/2` the difference is still `O_s(delta)`, so the singularity is topology-specific rather than generic instability.

AF-359 locates that tail sharply when smoothing order and zero height move together. If `delta_j->0`, `T_j->infinity` and `delta_j log T_j->u`, then the critical half-derivative dyadic shell ratios satisfy

`A_delta(T)/A_0(T) -> exp(-2u)`

and

`D_delta(T)/A_0(T) -> (1-exp(-u))^2`.

Hence polynomial or otherwise subexponential bandwidth in `1/delta` sees asymptotically none of the relative endpoint defect. An order-one fraction first appears at `T=exp(Theta(1/delta))`; above that scale the smoothed shell dies relative to the endpoint shell. This turns the qualitative high-frequency obstruction of AF-358 into an exact moving-bandwidth law.

The spectral scale matches the physical one already exposed by AF-357: the Beta smoothing kernel places fixed mass at relative lags `exp(-Theta(1/delta))`. The reciprocal scales arise from the exact Riesz multiplier and kernel, not from a general uncertainty principle. AF-354--AF-355 likewise show that sufficiently fast moving orders inherit endpoint oscillation, while AF-356 shows average `B^2` stability can coexist with the extremal failure.

The reusable proof obligation is now narrow. A uniform moving-order theorem must either control the exponentially moving spectral/physical band or exploit information that bypasses magnitude-only shell energy: source-native phase cancellation, maximal/tail control, signed short-interval coupling, endpoint-to-past correlation or another cross-scale law. A larger but subexponential cutoff, a stronger monotone quadratic weight, or another scalar source envelope cannot by itself reach the endpoint transition identified here.

**Boundary.** AF-358--AF-359 are conditional on RH and concern the nontrivial-zero Fourier profile. The exponential transition is specific to the Riesz multiplier and its quadratic critical-shell metric. It does not rule out phase-sensitive, nonlinear, maximal or arithmetic-specific mechanisms, and it does not prove that exponentially high zero information is necessary for every possible proof of an endpoint theorem.