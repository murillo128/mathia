# MI-041 — Fixed positive Riesz order crosses the critical conditioning threshold, while endpoint regularity depends on topology

**Evidence level:** exact/literature-derived boundary statement from [AF-352](../../findings/AF-352-every-positive-riesz-order-crosses-the-critical-boundary-conditioning-threshold.md), quantitatively sharpened by [AF-353](../../findings/AF-353-riesz-endpoint-conditioning-cost-diverges-quadratically-in-absolute-zero-budget.md), [AF-354](../../findings/AF-354-fast-vanishing-riesz-order-inherits-endpoint-oscillation.md), [AF-355](../../findings/AF-355-rh-cancellation-strengthens-moving-riesz-endpoint-obstruction.md), and [AF-356](../../findings/AF-356-riesz-endpoint-is-b2-stable-but-uniformly-ill-conditioned.md)

For fixed real `delta>0`, the Riesz profile

`R_delta[Lambda-1](X)=sum_(n<=X)(Lambda(n)-1)(1-n/X)^delta`

has the exact qualitative transition

`RH <=> R_delta[Lambda-1](X)=O_delta(sqrt(X))`,

whereas `delta=0` cannot satisfy the same bound because `psi(X)-X=Omega_±(sqrt(X) log log log X)`. The Mellin multiplier `B(rho,delta+1)` decays like `Gamma(1+delta)|gamma|^(-1-delta)` on the critical line, so every fixed positive order crosses the absolute-summability threshold without moving the off-critical singularity discriminator.

The endpoint is singular in two different extremal senses. AF-353 gives the absolute zero-mode budget

`A_+(delta)=1/(2*pi*delta^2) - (log(2*pi)+gamma_E)/(2*pi*delta) + O(1)`,

while the cancellation-aware physical norm `K(delta)=sup X^(-1/2)|R_delta[Lambda-1](X)|` also diverges as `delta->0+` under RH but need not have the same rate.

AF-354 and AF-355 show that a moving order cannot be treated by plugging `delta=delta(X)` into the fixed-parameter theorem. On the half-integer mesh `X_N=N+1/2`, the unconditional source comparison is

`|R_delta(X_N)-R_0(X_N)| << delta X_N`.

Hence orders with `delta_N sqrt(N)/logloglog(N)->0` inherit the Hardy--Littlewood endpoint oscillation and cannot be `O(sqrt(N))`; in particular every power `N^-a` with `a>=1/2` fails.

Under RH, Abel summation retains cancellation and improves the comparison to

`|R_delta(X_N)-R_0(X_N)| << sqrt(X_N) log^2(2X_N) min(1, delta log(2X_N))`.

Therefore, if `delta_N log^3(N)/logloglog(N)->0`, the moving profile still has `Omega_±(sqrt(N) logloglog(N))`. This rules out **every polynomially vanishing order** `delta_N=N^-a`, `a>0`, on the RH side. AF-355 also forces a subsequential lower rate `K(delta_j) >> log log(1/delta_j)`.

AF-356 shows that this singularity is not visible in every natural topology. Under RH, in logarithmic coordinates `E_delta(y)=e^(-y/2)R_delta(e^y)`, the critical-zero Fourier coefficients satisfy a square-summable perturbation law giving

`||E_delta-E_0||_(B^2)=O(delta)`.

The associated limiting distributions are likewise Lipschitz in bounded-Lipschitz distance, `d_BL(mu_delta,mu_0)=O(delta)`. Thus the same endpoint is **mean-square stable while uniformly ill-conditioned**: ordinary second-moment spectral energy and limiting-law convergence can remain regular even as the sharp supremum norm diverges and moving schedules inherit rare endpoint excursions.

The reusable point is that crossing a fixed-parameter summability threshold and controlling a moving family are different theorems, and the answer depends on the topology consumed by the endpoint. The missing uniform resource cannot be inferred from `B^2` continuity or limiting distributions; it must control the tail/peak/phase-coherence mechanism that the supremum norm sees.

**Boundary.** No moving-order RH criterion is proved. The region `delta_N` comparable to or larger than `logloglog(N)/log^3(N)` remains open to these arguments, and the true growth of `K(delta)` is still unknown. The `delta^-2` law is the triangle-inequality zero-mode budget, not the optimal cancellation-aware norm, while `B^2` continuity is not pointwise or uniform control.