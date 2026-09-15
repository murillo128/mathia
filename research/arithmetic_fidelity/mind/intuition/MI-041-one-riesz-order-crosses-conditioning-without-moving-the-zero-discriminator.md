# MI-041 — Positive Riesz order crosses critical regularity; recovery is target-relative and has a half-order source-native transition

**Evidence level:** exact/literature-derived boundary statement from [AF-352](../../findings/AF-352-every-positive-riesz-order-crosses-the-critical-boundary-conditioning-threshold.md), quantitatively sharpened by [AF-353](../../findings/AF-353-riesz-endpoint-conditioning-cost-diverges-quadratically-in-absolute-zero-budget.md) through [AF-363](../../findings/AF-363-source-native-sobolev-probes-have-half-order-riesz-recovery-transition.md).

For every fixed real `delta>0`, the Riesz profile crosses the critical regularity threshold without moving the off-critical singularity discriminator. AF-358 makes the Sobolev gain exact, while AF-359 shows that an order-one fraction of the absolute endpoint defect first appears on the moving scale `delta log T=Theta(1)`. AF-360 then shows that every bounded-ratio high-frequency shell is asymptotically one common complex scalar times the endpoint shell, so well-conditioned projective phase/shape statistics are blind there.

AF-361 resolves the finite exponential-band worst case. Put `x=delta log(gamma/T)` on `T<gamma<=T exp(v/delta)`. After dividing by the lower-edge scalar, the exact Gamma-quotient multiplier converges uniformly to `e^-x`. Hence for fixed `v` the normalized transport has condition number tending to `e^v`, while the lower-edge multiplier itself has size `e^-u` with `u=delta log T`. Relative band conditioning and absolute attenuation are separate currencies.

AF-362 identifies the sharper currency for a declared target. If `L_a(z)=<a,z>` and `mu_a` is the probability measure carrying target energy `|a_gamma|^2` at the scaled coordinates `x_gamma`, the unique exact linear recovery rule has normalized noise amplification

`(int e^(2x) dmu_a(x))^(1/2)`

up to the vanishing Gamma-ratio error. Uniform target recovery is therefore equivalent to a bounded exponential second moment of the target-energy distribution. The hard upper width `v` is only the operator worst case: even when `v->infinity`, a target whose energy stays exponentially localized can remain uniformly recoverable, whereas target mass near the upper edge pays the full `e^v` cost.

AF-363 makes that criterion source-native rather than abstract. For the Sobolev/Bessel probes

`a_gamma^(beta,y0)=(1+gamma^2)^(-beta/2)e^(i gamma y0)`,

the zero-shell energy density produces an exact half-order transition on every fixed scaled band. When `0<=beta<1/2`, the normalized recovery modulus tends to the worst-edge cost `e^v`; when `beta>1/2`, it tends to `1`. At the critical value `beta=1/2`, the energy remains logarithmically spread across scaled shells and AF-363 deliberately does not promote a universal limiting constant. The threshold is the same one at which point evaluation becomes bounded for the corresponding Hilbert/Sobolev scale.

The absolute price still factors separately. If `u=delta log T`, the common base attenuation contributes `e^u`; the subcritical probes then additionally pay the `e^v` differential band cost, while supercritical probes remove that differential cost without removing `e^u`. Regularity can therefore change target conditioning without changing where the off-critical discriminator lives or creating arithmetic specificity.

This changes the live diagnostic from a two-scalar bandwidth test to a **base attenuation plus target Picard/regularity test**. Price where the band starts through `u=delta log T`, then price the declared destination functional through its exponential moment under `mu_a`; for natural Sobolev probes, identify which side of `beta=1/2` the target occupies. A proof cannot evade the cost by choosing a target adapted after seeing the Riesz multiplier; the representer must come from the arithmetic endpoint independently of the transport.

The universal normalized envelope still contains no rational-prime selector, and AF-363's half-order transition is reproduced by the generic zero-shell density used in the derivation. Good target-relative recovery only says that a particular functional can be transported stably through this channel. Arithmetic specificity must already be present in the target/source relation or in information that the universal Riesz envelope does not erase.

**Boundary.** The zero-shell interpretation used in AF-358--AF-363 is conditional on RH where stated in the findings. AF-362 is an exact diagonal inverse-problem statement for a declared linear target, and AF-363 is its source-native Sobolev specialization. Neither establishes that the relevant arithmetic endpoint has the required spectral localization, controls nonlinear source operations, removes the separate `e^-u` attenuation, or makes the `beta=1/2` endpoint uniformly recoverable. Nothing here says exponentially high zero information is necessary for every possible proof of RH.