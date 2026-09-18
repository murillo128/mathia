# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the absolute-H lower boundary after removing deterministic gamma normalization

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-286 classify the isolated coefficient-scale profile and its two source boundaries. VIS-287--VIS-291 then move to Wang's complete pair statistic and show that on every compact power panel `x=T^beta`, `0<beta_0<=beta<=beta_1<theta`, the leading law is uniformly linear after the explicit gamma contribution is retained, with the squared-von-Mangoldt remainder controlled by the standard Korobov--Vinogradov PNT envelope. VIS-292 shows that the symmetric log-source Green filter has no exact blind frequency, and VIS-293 shows that first-half-plane holomorphy of the exact source transform is RH-equivalent rather than an independent continuation mechanism.

VIS-294 narrows the lower moving-source escape sharply. With `H=T^theta`, `L=log T` and one fixed theorem ceiling `x<=T^lambda`, `lambda<theta`, Wang's existing error budget gives

`F_I(x)=(H/(2pi))(L^2/x^2+log x)+o(H)`

through every family with `x/sqrt(L)->infinity`. Thus `beta(T)->0` by itself creates no new `H`-scale regime. The first lower range not resolved to absolute `H` accuracy by the current bounds begins only at `x=O(sqrt(L))`; the explicit gamma term itself is known and must not be misclassified as an unexplained residual.

VIS-295 shows that even this boundary depends on normalization. After subtracting the gamma term, the residual remains relatively linear,

`R_gamma(T,x)=(H/(2pi))log x+o(H log x)`,

whenever `x^2 log x/L -> infinity`. This extends below `sqrt(L)` to the current relative-error boundary `x^2 log x=O(L)`, of order `sqrt(L/log L)` up to slowly varying factors.

VIS-296 reduces the finite relative crossover `x^2 log x/L -> kappa in (0,infinity)` to one normalized mean remainder,

`R_gamma/(H log x)=1/(2pi)+Re Q_E(T,x)/(pi kappa)+o(1)`,

with `Q_E=(x/H) integral_I E_x(t) dt`. VIS-297 evaluates that remaining channel rather than discovering a new arithmetic transition:

`Re Q_E(T,x)=-log(2pi)+o(1)`.

The contribution is the deterministic gamma-factor constant hidden by Wang's coarse baseline `log(t+2)/x`; the absolutely convergent right-half-plane zeta term has zero interval mean at this normalization, while pole and trivial-zero terms are negligible. Consequently

`R_gamma/(H log x)=1/(2pi)-log(2pi)/(pi kappa)+o(1)`.

Thus the finite relative crossover at `x^2 log x/L=Theta(1)` is a **baseline-normalization effect**, not evidence of a new prime-sensitive channel. Using the natural gamma normalization removes the only order-one mean left by VIS-296.

The lower-boundary problem is now the genuinely harder absolute-`H` question near `x=O(sqrt(L))`: after all deterministic gamma terms are normalized exactly, can the remaining load-bearing errors in Wang's short-interval formula be sharpened or structurally resolved at absolute `H` scale? The near-ceiling regime `x` approaching `T^theta`, fixed-power real-axis source behavior and packet-conditioning questions remain separate and should not be inferred from the now-closed relative-mean calculation.

## Keep packet conditioning, source arithmetic, theorem uniformity, normalization and analytic continuation separate

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, distance to the source boundary, requested output scale, prime-power source measure, smoothing multiplier, theorem-uniformity range, explicit-formula remainder and analytic domain of the source Dirichlet transform. Exact invertibility of the Green filter is not stable recovery, while strong smoothing is not information loss when the multiplier is nonzero.

VIS-294--VIS-297 sharpen the normalization warning. The same nominal `HL/x^2` scale can mix a coarse deterministic replacement with a genuinely unresolved remainder channel. At relative resolution the only surviving mean remainder is now identified exactly as gamma normalization, so no source-selective conclusion should be attached to that crossover. A useful next probe must specify the residual **after** deterministic normalization and the requested absolute or relative output scale before treating an error boundary as new arithmetic structure.