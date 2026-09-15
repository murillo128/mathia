# MI-041 — Positive Riesz order crosses critical regularity; recovery is target-relative and the half-order endpoint pays a square-root bandwidth discount

**Evidence level:** exact/literature-derived boundary statement from [AF-352](../../findings/AF-352-every-positive-riesz-order-crosses-the-critical-boundary-conditioning-threshold.md), quantitatively sharpened by [AF-353](../../findings/AF-353-riesz-endpoint-conditioning-cost-diverges-quadratically-in-absolute-zero-budget.md) through [AF-364](../../findings/AF-364-critical-half-order-riesz-recovery-scales-as-e-v-over-sqrt-v.md). The zero-shell interpretation remains conditional on RH where stated in the findings.

For every fixed real `delta>0`, the Riesz profile crosses the critical regularity threshold without moving the off-critical singularity discriminator. AF-358 makes the Sobolev gain exact, while AF-359 shows that an order-one fraction of the absolute endpoint defect first appears on the moving scale `delta log T=Theta(1)`. AF-360 then shows that every bounded-ratio high-frequency shell is asymptotically one common complex scalar times the endpoint shell, so well-conditioned projective phase/shape statistics are blind there.

AF-361 resolves the finite exponential-band worst case. Put `x=delta log(gamma/T)` on `T<gamma<=T exp(v/delta)`. After dividing by the lower-edge scalar, the exact Gamma-quotient multiplier converges uniformly to `e^-x`. Hence for fixed `v` the normalized transport has condition number tending to `e^v`, while the lower-edge multiplier itself has size `e^-u` with `u=delta log T`. Relative band conditioning and absolute attenuation are separate currencies.

AF-362 identifies the sharper currency for a declared target. If `L_a(z)=<a,z>` and `mu_a` is the probability measure carrying target energy `|a_gamma|^2` at the scaled coordinates `x_gamma`, the unique exact linear recovery rule has normalized noise amplification

`(int e^(2x) dmu_a(x))^(1/2)`

up to the vanishing Gamma-ratio error. Uniform target recovery is therefore equivalent to a bounded exponential second moment of the target-energy distribution. The hard upper width `v` is only the operator worst case: even when `v->infinity`, a target whose energy stays exponentially localized can remain uniformly recoverable, whereas target mass near the upper edge pays the full `e^v` cost.

AF-363 makes that criterion source-native. For the Sobolev/Bessel probes

`a_gamma^(beta,y0)=(1+gamma^2)^(-beta/2)e^(i gamma y0)`,

the zero-shell energy density gives a half-order transition. For `beta<1/2`, the normalized recovery modulus pays the upper-edge cost `e^v`; for `beta>1/2`, it tends to `1` on every fixed scaled band.

AF-364 resolves the critical value rather than interpolating it from either side. At `beta=1/2` the target energy is spread across logarithmic zero scales. With `u=delta log T` and fixed `v`, the squared recovery modulus is trapped, up to the known positive distinct-zero density constant, around the explicit profile

`R(u,v)=((2u+2v-1)e^(2v)-2u+1)/(2v(2u+v))`.

If distinct zeros have an asymptotic positive density, that scalar density cancels and `K_(1/2)^2 -> R(u,v)`. More robustly, no exact density is needed for the growing-band scale: as `v->infinity`,

`K_(1/2)=Theta(e^v/sqrt(v))`.

The critical target therefore receives a genuine `sqrt(v)` discount relative to the worst/subcritical `e^v` cost, but it is still exponentially ill-conditioned on growing scaled bands. The discount comes from normalization by target energy spread over the full logarithmic interval, not from a new arithmetic cancellation.

The absolute price still factors separately. Multiplying back the lower-edge attenuation makes the critical growing-band recovery bill `Theta(e^(u+v)/sqrt(v))`. Regularity can therefore change target conditioning by an entire polynomial bandwidth factor without changing where the off-critical discriminator lives or creating rational-prime specificity.

This closes the conditioning side of the half-order question. The live diagnostic is now: derive the representer of an arithmetic endpoint **before** looking at the Riesz multiplier, determine its target-energy profile, price its `u` and `v` costs, and only then ask whether the same target separates the rational-prime source from matched controls. A source-independent Sobolev target with excellent recovery is not useful if its law is reproduced by a non-arithmetic frequency system.

**Boundary.** AF-364 uses the inherited RH channel interpretation and a modern positive lower density of distinct zeros; its exact fixed-band limit additionally assumes an asymptotic distinct-zero density, while the `e^v/sqrt(v)` scale does not. None of AF-362--AF-364 identifies the actual arithmetic destination target, controls nonlinear source operations, removes the separate `e^-u` attenuation, or proves that good target conditioning carries prime specificity. Nothing here says exponentially high zero information is necessary for every possible proof of RH.