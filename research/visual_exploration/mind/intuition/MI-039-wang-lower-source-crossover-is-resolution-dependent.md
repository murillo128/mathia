# MI-039 — Wang's lower-source crossover is resolution-dependent, and the relative boundary is a mean-remainder problem

**Evidence level:** exact error-budget synthesis from [VIS-294](../../findings/VIS-294-wang-lower-moving-source-sqrtlog-crossover.md), [VIS-295](../../findings/VIS-295-wang-gamma-subtracted-residual-relative-crossover.md), and [VIS-296](../../findings/VIS-296-wang-relative-boundary-reduces-to-explicit-formula-remainder-mean.md), using the Wang/PNT inputs already audited in those findings.

Write `H=T^theta` and `L=log T`. VIS-294 keeps Wang's explicit gamma contribution visible and shows that, for one fixed `lambda<theta`,

`F_I(x)=(H/(2pi))(L^2/x^2+log x)+o(H)`

uniformly through moving lower-source families satisfying `x/sqrt(L)->infinity` and `x<=T^lambda`. The apparent escape `beta(T)=log x/log T -> 0` is therefore too coarse: many vanishing-exponent families are already controlled to absolute `H` accuracy.

At that normalization, the current source-dependent errors `H L/x^2` and `H sqrt(L)/x` first reach `H` scale around `x~sqrt(L)`. This makes `sqrt(log T)` the first unresolved **absolute-`H`** lower corridor in the existing theorem, not a proved transition of the true statistic.

VIS-295 changes only the requested resolution. After subtracting the known gamma term, put

`R_gamma=F_I-(H/(2pi))L^2/x^2`.

The same error budget gives

`R_gamma=(H/(2pi))log x+o(H log x)`

whenever `x^2 log x/L -> infinity`. Thus relative linearization survives strictly below `sqrt(L)`. The current relative boundary is `x^2 log x=O(L)`, roughly `sqrt(L/log L)` up to slowly varying factors.

VIS-296 then resolves what actually survives at that relative boundary. On a moving family with

`x^2 log x/L -> kappa in (0,infinity)`, 

one has

`R_gamma/(H log x)=1/(2pi)+Re Q_E(T,x)/(pi kappa)+o(1)`,

where

`Q_E(T,x)=(x/H) integral_I E_x(t) dt`

is the normalized interval mean of Wang's explicit-formula remainder. The pure `B_x^2` contribution that had been hidden inside the coarse `HL/x^2` error is actually `o(H log x)` on the power-short interval, and the other propagated channels are lower order as well. The relative crossover is therefore no longer an undifferentiated error-budget boundary: **one mean remainder is the only currently unresolved order-one channel**.

This gives a precise discriminator. If `Re Q_E->0` uniformly on the crossover, the gamma-subtracted linear profile extends through the present relative boundary. If it does not, the next question is whether the surviving mean encodes genuine prime-power structure or only another classical explicit-formula term that can be extracted. Either outcome is more informative than treating `x~sqrt(L/log L)` as an intrinsic transition.

The two scales still answer different questions. `x~sqrt(L)` is where present errors stop being negligible compared with `H`; `x^2 log x~L` is where the gamma-subtracted residual first becomes sensitive to the mean remainder at its own `H log x` scale. Any lower-boundary claim must specify what has been subtracted and what output scale is supposed to reveal new information.

**Boundary.** Neither `sqrt(L)` nor `sqrt(L/log L)` is proved sharp or intrinsic. VIS-296 does not determine the limit of `Q_E`, and it does not establish that the remainder mean is source-selective or new. A sharper explicit-formula analysis could still remove it. The near-ceiling source regime is separate, and no new zero-free region or RH implication follows from these normalizations.