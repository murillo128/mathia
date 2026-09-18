# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve Wang's lower moving-source boundary at the resolution actually requested

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-286 classify the isolated coefficient-scale profile and its two source boundaries. VIS-287--VIS-291 then move to Wang's complete pair statistic and show that on every compact power panel `x=T^beta`, `0<beta_0<=beta<=beta_1<theta`, the leading law is uniformly linear after the explicit gamma contribution is retained, with the squared-von-Mangoldt remainder controlled by the standard Korobov--Vinogradov PNT envelope. VIS-292 shows that the symmetric log-source Green filter has no exact blind frequency, and VIS-293 shows that first-half-plane holomorphy of the exact source transform is RH-equivalent rather than an independent continuation mechanism.

VIS-294 narrows the lower moving-source escape sharply. With `H=T^theta`, `L=log T` and one fixed theorem ceiling `x<=T^lambda`, `lambda<theta`, Wang's existing error budget gives

`F_I(x)=(H/(2pi))(L^2/x^2+log x)+o(H)`

through every family with `x/sqrt(L)->infinity`. Thus `beta(T)->0` by itself creates no new `H`-scale regime. The first lower range not resolved to absolute `H` accuracy by the current bounds begins only at `x=O(sqrt(L))`; the explicit gamma term itself is known and must not be misclassified as an unexplained residual.

VIS-295 shows that even this boundary depends on normalization. After subtracting the gamma term, the residual remains relatively linear,

`R_gamma(T,x)=(H/(2pi))log x+o(H log x)`,

whenever `x^2 log x/L -> infinity`. This extends below `sqrt(L)` to the current relative-error boundary `x^2 log x=O(L)`, of order `sqrt(L/log L)` up to slowly varying factors. Neither crossover is proved intrinsic; they are the points where the **current theorem errors** reach the requested absolute or relative scale.

The lower-boundary problem must therefore state its target resolution before claiming a new regime. At absolute `H` resolution, sharpen or understand the terms that become critical near `x=O(sqrt(L))`. For the gamma-subtracted leading profile, a genuinely new effect must reach `x^2 log x=O(L)` or improve the `H L/x^2` contribution enough to move that boundary. The near-ceiling branch `x` approaching `T^theta` remains separate and still requires new uniformity.

## Keep packet conditioning, source arithmetic, theorem uniformity, normalization and analytic continuation separate

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, distance to the source boundary, requested output scale, prime-power source measure, smoothing multiplier, theorem-uniformity range and analytic domain of the source Dirichlet transform. Exact invertibility of the Green filter is not stable recovery, while strong smoothing is not information loss when the multiplier is nonzero.

VIS-294--VIS-295 add a normalization warning: the same error term can be fatal for an `o(H)` statement and negligible for an `o(H log x)` statement. A useful next probe must declare the moving source family and the scale at which a residual is supposed to be informative, charge every theorem error against that same scale, and identify arithmetic structure remaining after the explicit gamma and diagonal baselines are removed. Otherwise a visual boundary can be an artifact of normalization rather than new source information.