# MI-041 — Any positive Riesz order crosses the critical conditioning threshold, but the endpoint cost is singular

**Evidence level:** exact/literature-derived boundary statement from [AF-352](../../findings/AF-352-every-positive-riesz-order-crosses-the-critical-boundary-conditioning-threshold.md), quantitatively sharpened by [AF-353](../../findings/AF-353-riesz-endpoint-conditioning-cost-diverges-quadratically-in-absolute-zero-budget.md) and refining the integer-order result [AF-351](../../findings/AF-351-one-riesz-order-is-the-critical-boundary-conditioning-threshold.md)

For fixed real `delta>=0`, let

`R_delta[Lambda-1](X)=sum_(n<=X)(Lambda(n)-1)(1-n/X)^delta`.

AF-352 identifies the exact qualitative transition at the sharp `sqrt(X)` boundary:

`RH <=> R_delta[Lambda-1](X)=O_delta(sqrt(X))` for every fixed `delta>0`,

whereas `delta=0` cannot satisfy the same bound because `psi(X)-X=Omega_±(sqrt(X) log log log X)`.

The mechanism is the Mellin multiplier

`B(rho,delta+1)=Gamma(rho)Gamma(delta+1)/Gamma(rho+delta+1)`.

On the critical line its size is asymptotic to `Gamma(1+delta)|gamma|^(-1-delta)`. Since `N(T)=O(T log T)`, every fixed `delta>0` makes the critical-zero coefficient tail absolutely summable; at `delta=0` the `1/|gamma|` endpoint does not. At the same time the beta multiplier is nonzero in `Re s>1/2`, so an `O(sqrt(X))` profile still excludes every off-critical zero through the Mellin singularity argument.

AF-353 prices the approach to the open endpoint. For positive ordinates,

`A_+(delta)=sum_(gamma>0)|B(rho,1+delta)|`

has the unconditional Laurent law

`A_+(delta)=1/(2*pi*delta^2) - (log(2*pi)+gamma_E)/(2*pi*delta) + O(1)`.

The quadratic pole comes from the secondary zero zeta `sum gamma^(-s)`: the target mode density and the barely summable multiplier meet at a double pole. Thus arbitrarily weak positive smoothing crosses the summability threshold, but it does so with an absolute conditioning budget that diverges like `delta^(-2)`.

There is a separate, weaker statement for the actual prime profile. Under RH, if

`K(delta)=sup_(X>=2, X noninteger) X^(-1/2)|R_delta[Lambda-1](X)|`,

then `K(delta)<infinity` for every fixed `delta>0` but `K(delta)->infinity` as `delta->0+`. AF-353 does **not** identify the growth rate of `K(delta)` with `delta^(-2)`; cancellation among zero modes may make the optimal profile norm much smaller than the absolute spectral budget.

The reusable point is therefore two-dimensional. A representation can preserve the discriminator and improve fixed-parameter conditioning, yet become singular as it approaches a less-smoothed boundary. The correct audit is not only whether multiplier decay lies on the summable side of the target mode density, but also the distance to the density singularity and the resulting dependence of constants on the representation parameter.

**Boundary.** All RH equivalences remain fixed-`delta` statements. No criterion is proved for `delta=delta(X)->0`, no `delta`-rate is known for the optimal prime profile norm `K(delta)`, and the conditioning gain does not supply the missing arithmetic estimate. The `delta^(-2)` law prices the triangle-inequality zero-mode budget, not the best possible cancellation-aware norm.