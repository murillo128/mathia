# MI-041 — Positive Riesz order crosses critical regularity; finite exponential bandwidth separates attenuation from conditioning

**Evidence level:** exact/literature-derived boundary statement from [AF-352](../../findings/AF-352-every-positive-riesz-order-crosses-the-critical-boundary-conditioning-threshold.md), quantitatively sharpened by [AF-353](../../findings/AF-353-riesz-endpoint-conditioning-cost-diverges-quadratically-in-absolute-zero-budget.md) through [AF-361](../../findings/AF-361-riesz-exponential-band-recovery-splits-attenuation-from-conditioning.md).

For every fixed real `delta>0`, the Riesz profile crosses the critical regularity threshold without moving the off-critical singularity discriminator. AF-358 makes the Sobolev gain exact, while AF-359 shows that an order-one fraction of the absolute endpoint defect first appears on the moving scale `delta log T=Theta(1)`. AF-360 then shows that every bounded-ratio high-frequency shell is asymptotically one common complex scalar times the endpoint shell, so well-conditioned projective phase/shape statistics are blind there.

AF-361 resolves the remaining finite exponential-band question. Put

`x=delta log(gamma/T)`

on `T<gamma<=T exp(v/delta)`. After dividing by the lower-edge scalar, the exact Gamma-quotient multiplier converges uniformly to `e^-x`. Hence for fixed `v` the normalized transport has operator norm tending to `1`, inverse norm tending to `e^v`, and condition number tending to `e^v`. An exponentially broad band is therefore stably recoverable whenever its **scaled width** `v=delta log R` stays finite.

Absolute attenuation is a different currency. If `u=delta log T`, the lower-edge multiplier has size asymptotic to `e^-u`, so the unnormalized inverse carries the combined cost `e^(u+v)`. The endpoint problem cannot use “conditioning” as a synonym for this loss: finite relative-band conditioning may coexist with severe absolute attenuation at large base height.

This leaves three genuinely different escape routes. A theorem may need an absolute error/noise bound strong enough to survive `e^-u`; it may have to control bands with `v->infinity`, where relative conditioning really diverges; or it may use source-native arithmetic information before the Riesz channel replaces frequency dependence by the universal `e^-x` envelope. The finite-width envelope itself contains no rational-prime selector.

The reusable diagnostic is therefore two-parameter: price **where the band starts** through `u=delta log T` and **how wide it is** through `v=delta log R`. Only the second is relative conditioning; only the first controls common attenuation. Neither alone supplies arithmetic specificity.

**Boundary.** The zero-shell interpretation used in AF-358--AF-361 is conditional on RH where stated in the findings. AF-361 proves stable relative recovery only for finite scaled width; it does not control `v->infinity`, absolute observational noise, source-side nonlinear operations, or deliberately ill-conditioned observers. Nothing here says exponentially high zero information is necessary for every possible proof of RH.