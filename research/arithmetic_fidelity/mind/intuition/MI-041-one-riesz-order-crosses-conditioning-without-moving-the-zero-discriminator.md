# MI-041 — Positive Riesz order crosses critical regularity; recovery is target-relative after base attenuation

**Evidence level:** exact/literature-derived boundary statement from [AF-352](../../findings/AF-352-every-positive-riesz-order-crosses-the-critical-boundary-conditioning-threshold.md), quantitatively sharpened by [AF-353](../../findings/AF-353-riesz-endpoint-conditioning-cost-diverges-quadratically-in-absolute-zero-budget.md) through [AF-362](../../findings/AF-362-riesz-target-recovery-is-exponential-picard-moment.md).

For every fixed real `delta>0`, the Riesz profile crosses the critical regularity threshold without moving the off-critical singularity discriminator. AF-358 makes the Sobolev gain exact, while AF-359 shows that an order-one fraction of the absolute endpoint defect first appears on the moving scale `delta log T=Theta(1)`. AF-360 then shows that every bounded-ratio high-frequency shell is asymptotically one common complex scalar times the endpoint shell, so well-conditioned projective phase/shape statistics are blind there.

AF-361 resolves the finite exponential-band worst case. Put `x=delta log(gamma/T)` on `T<gamma<=T exp(v/delta)`. After dividing by the lower-edge scalar, the exact Gamma-quotient multiplier converges uniformly to `e^-x`. Hence for fixed `v` the normalized transport has condition number tending to `e^v`, while the lower-edge multiplier itself has size `e^-u` with `u=delta log T`. Relative band conditioning and absolute attenuation are separate currencies.

AF-362 identifies the sharper currency for a declared target. If `L_a(z)=<a,z>` and `mu_a` is the probability measure carrying target energy `|a_gamma|^2` at the scaled coordinates `x_gamma`, the unique exact linear recovery rule has normalized noise amplification

`(int e^(2x) dmu_a(x))^(1/2)`

up to the vanishing Gamma-ratio error. Uniform target recovery is therefore equivalent to a bounded exponential second moment of the target-energy distribution. The hard upper width `v` is only the operator worst case: even when `v->infinity`, a target whose energy stays exponentially localized can remain uniformly recoverable, whereas target mass near the upper edge pays the full `e^v` cost.

This changes the live diagnostic from a two-scalar bandwidth test to a **base attenuation plus target Picard test**. Price where the band starts through `u=delta log T`, then price the declared destination functional through its exponential moment under `mu_a`. A proof cannot evade the cost by choosing a target adapted to the Riesz multiplier; the representer must come from the arithmetic endpoint independently of the transport.

The universal normalized envelope still contains no rational-prime selector. Good target-relative recovery only says that a particular functional can be transported stably through this channel. Arithmetic specificity must already be present in the target/source relation or in information that the universal Riesz envelope does not erase.

**Boundary.** The zero-shell interpretation used in AF-358--AF-362 is conditional on RH where stated in the findings. AF-362 is an exact diagonal inverse-problem statement for a declared linear target; it does not establish that the relevant arithmetic endpoint has the required exponential spectral localization, control nonlinear source operations, or remove the separate `e^-u` absolute attenuation. Nothing here says exponentially high zero information is necessary for every possible proof of RH.