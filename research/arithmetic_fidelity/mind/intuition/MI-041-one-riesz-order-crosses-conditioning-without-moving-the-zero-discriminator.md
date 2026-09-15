# MI-041 — Any positive Riesz order crosses the critical conditioning threshold without moving the zero discriminator

**Evidence level:** exact/literature-derived boundary statement from [AF-352](../../findings/AF-352-every-positive-riesz-order-crosses-the-critical-boundary-conditioning-threshold.md), refining the integer-order result [AF-351](../../findings/AF-351-one-riesz-order-is-the-critical-boundary-conditioning-threshold.md) and the singularity-fidelity calibration in [AF-350](../../findings/AF-350-riesz-error-exponents-preserve-right-half-plane-dirichlet-singularities.md)

For fixed real `delta>=0`, let

`R_delta[Lambda-1](X)=sum_(n<=X)(Lambda(n)-1)(1-n/X)^delta`.

AF-352 identifies the exact transition at the sharp `sqrt(X)` boundary:

`RH <=> R_delta[Lambda-1](X)=O_delta(sqrt(X))` for every fixed `delta>0`,

whereas `delta=0` cannot satisfy the same bound because `psi(X)-X=Omega_±(sqrt(X) log log log X)`.

The mechanism is the Mellin multiplier

`B(rho,delta+1)=Gamma(rho)Gamma(delta+1)/Gamma(rho+delta+1)`.

On the critical line its size is `O_delta(|gamma|^(-1-delta))`. Since `N(T)=O(T log T)`, every fixed `delta>0` makes the critical-zero coefficient tail absolutely summable; at `delta=0` the `1/|gamma|` endpoint does not. At the same time the beta multiplier is nonzero in `Re s>1/2`, so an `O(sqrt(X))` profile still excludes every off-critical zero through the Mellin singularity argument.

Thus the useful threshold is not “one integer smoothing step” but the interaction between **target-mode density and multiplier decay**. An arbitrarily small fixed positive gain in decay crosses the summability boundary while preserving the singularity locations that define the discriminator.

This gives a concrete counterexample to the idea that better conditioning must cost the target signal: smoothing may suppress nuisance accumulation faster than it suppresses the discriminator. The audit for another kernel is therefore quantitative: determine the relevant mode density, the multiplier decay needed for the endpoint norm, and whether the same multiplier has zeros or quotient identifications at target-relevant singularities.

**Boundary.** `delta` is fixed. No uniform control is claimed as `delta->0+`, no rate for a scale-dependent `delta(X)` is established, and no source recovery follows. For every fixed `delta>0`, proving the critical bound for the physical prime source is already RH-equivalent; the conditioning improvement does not supply the missing arithmetic estimate.