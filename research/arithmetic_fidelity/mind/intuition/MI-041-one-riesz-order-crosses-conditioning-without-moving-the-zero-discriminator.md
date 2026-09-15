# MI-041 — Positive Riesz order crosses the critical regularity threshold, but the endpoint remains hidden behind scalarization and exponential scale separation

**Evidence level:** exact/literature-derived boundary statement from [AF-352](../../findings/AF-352-every-positive-riesz-order-crosses-the-critical-boundary-conditioning-threshold.md), quantitatively sharpened by [AF-353](../../findings/AF-353-riesz-endpoint-conditioning-cost-diverges-quadratically-in-absolute-zero-budget.md) through [AF-360](../../findings/AF-360-riesz-dyadic-projective-shape-is-endpoint-blind.md).

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

Hence polynomial or otherwise subexponential bandwidth in `1/delta` sees asymptotically none of the absolute endpoint defect. An order-one fraction first appears at `T=exp(Theta(1/delta))`; above that scale the smoothed shell dies relative to the endpoint shell. The reciprocal physical scale is already visible in AF-357: the Beta smoothing kernel places fixed mass at relative lags `exp(-Theta(1/delta))`.

AF-360 closes the most obvious phase-sensitive escape from this magnitude law. On every bounded-ratio zero shell, the exact Gamma quotient satisfies

`M_delta(rho_gamma)=c_(delta,T)(1+o(1))`

uniformly as `delta->0`, `T->infinity`, with no restriction on `delta log T`. After quotienting the common complex scalar, the entire shell vector converges projectively to the endpoint shell: normalized cross-frequency shape and every continuous uniformly well-conditioned scale-invariant observable are asymptotically unchanged. The shell can therefore lose essentially all endpoint amplitude while retaining the same projective phase geometry.

Cross-scale comparison is equally rigid. If two dyadic shells are separated by a factor `R_delta`, their relative Riesz attenuation is asymptotically `R_delta^(-2delta)`. Thus `log R_delta=o(1/delta)` is still blind, while an order-one relative discriminator requires `R_delta=exp(Theta(1/delta))`. Moving from magnitude to post-Riesz phase, coherence, or subexponentially separated shell ratios does not lower the endpoint bandwidth price.

The reusable proof obligation is consequently narrower. A uniform moving-order theorem must either control an exponentially broad spectral/physical range, accept an observer whose conditioning diverges strongly enough to amplify the vanishing residual, or use information **before** the Riesz channel scalarizes it: source-native signed short-interval structure, maximal/tail information, cancellation coupled before smoothing, endpoint-to-past correlation, or another genuinely pre-compression nonlinear operation. A larger but subexponential cutoff, a stronger monotone quadratic weight, or a well-conditioned post-Riesz phase statistic cannot by itself reach the endpoint.

**Boundary.** AF-358--AF-360 are conditional on RH where they use the nontrivial-zero Fourier-shell interpretation. The scalarization statement is a property of the Riesz Gamma quotient on bounded-ratio shells; it does not rule out exponentially wide bands, source-side nonlinear operations, maximal/tail mechanisms, or deliberately ill-conditioned observers. Nothing here proves that exponentially high zero information is necessary for every possible proof of RH or of an endpoint theorem.