# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the mean explicit-formula remainder at Wang's relative lower boundary

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-286 classify the isolated coefficient-scale profile and its two source boundaries. VIS-287--VIS-291 then move to Wang's complete pair statistic and show that on every compact power panel `x=T^beta`, `0<beta_0<=beta<=beta_1<theta`, the leading law is uniformly linear after the explicit gamma contribution is retained, with the squared-von-Mangoldt remainder controlled by the standard Korobov--Vinogradov PNT envelope. VIS-292 shows that the symmetric log-source Green filter has no exact blind frequency, and VIS-293 shows that first-half-plane holomorphy of the exact source transform is RH-equivalent rather than an independent continuation mechanism.

VIS-294 narrows the lower moving-source escape sharply. With `H=T^theta`, `L=log T` and one fixed theorem ceiling `x<=T^lambda`, `lambda<theta`, Wang's existing error budget gives

`F_I(x)=(H/(2pi))(L^2/x^2+log x)+o(H)`

through every family with `x/sqrt(L)->infinity`. Thus `beta(T)->0` by itself creates no new `H`-scale regime. The first lower range not resolved to absolute `H` accuracy by the current bounds begins only at `x=O(sqrt(L))`; the explicit gamma term itself is known and must not be misclassified as an unexplained residual.

VIS-295 shows that even this boundary depends on normalization. After subtracting the gamma term, the residual remains relatively linear,

`R_gamma(T,x)=(H/(2pi))log x+o(H log x)`,

whenever `x^2 log x/L -> infinity`. This extends below `sqrt(L)` to the current relative-error boundary `x^2 log x=O(L)`, of order `sqrt(L/log L)` up to slowly varying factors.

VIS-296 resolves the bookkeeping exactly on the finite crossover `x^2 log x/L -> kappa in (0,infinity)`. After the gamma term is removed,

`R_gamma/(H log x)=1/(2pi)+Re Q_E(T,x)/(pi kappa)+o(1)`,

where `Q_E=(x/H) integral_I E_x(t) dt` is the normalized mean of Wang's explicit-formula remainder. The apparently competing pure `B_x^2` error can be sharpened below the relative scale on power-short intervals, and the remaining propagated terms are also lower order. At this normalization the first unresolved order-one channel is therefore **one mean remainder**, not a generic collection of theorem errors.

The lower-boundary problem is now concrete. Prove `Re Q_E(T,x)->0` uniformly on the crossover to extend relative linearization through it, or identify a nonzero limiting/oscillatory contribution and determine whether it is genuinely source-arithmetic rather than another removable explicit-formula baseline. The absolute-`H` crossover near `sqrt(L)` and the near-ceiling regime `x` approaching `T^theta` remain separate questions.

## Keep packet conditioning, source arithmetic, theorem uniformity, normalization and analytic continuation separate

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, distance to the source boundary, requested output scale, prime-power source measure, smoothing multiplier, theorem-uniformity range, explicit-formula remainder and analytic domain of the source Dirichlet transform. Exact invertibility of the Green filter is not stable recovery, while strong smoothing is not information loss when the multiplier is nonzero.

VIS-294--VIS-296 sharpen the normalization warning. The same nominal `HL/x^2` scale can mix a coarse deterministic replacement with a genuinely unresolved remainder channel; after the deterministic part is sharpened, only the normalized mean `Q_E` survives at the relative crossover. A useful next probe must therefore name the residual and requested scale explicitly rather than infer arithmetic structure from an error crossover itself.