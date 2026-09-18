# MI-039 — Wang's lower-source crossover is resolution-dependent

**Evidence level:** exact error-budget synthesis from [VIS-294](../../findings/VIS-294-wang-lower-moving-source-sqrtlog-crossover.md) and [VIS-295](../../findings/VIS-295-wang-gamma-subtracted-residual-relative-crossover.md), using the Wang/PNT inputs already audited in the preceding findings.

Write `H=T^theta` and `L=log T`. VIS-294 keeps Wang's explicit gamma contribution visible and shows that, for one fixed `lambda<theta`,

`F_I(x)=(H/(2pi))(L^2/x^2+log x)+o(H)`

uniformly through moving lower-source families satisfying `x/sqrt(L)->infinity` and `x<=T^lambda`. The apparent escape `beta(T)=log x/log T -> 0` is therefore too coarse: many vanishing-exponent families are already controlled to absolute `H` accuracy.

At that normalization, the current source-dependent errors `H L/x^2` and `H sqrt(L)/x` first reach `H` scale around `x~sqrt(L)`. This makes `sqrt(log T)` the first unresolved **absolute-`H`** lower corridor in the existing theorem, not a proved transition of the true statistic.

VIS-295 changes only the requested resolution. After subtracting the known gamma term, put

`R_gamma=F_I-(H/(2pi))L^2/x^2`.

The same error budget gives

`R_gamma=(H/(2pi))log x+o(H log x)`

whenever `x^2 log x/L -> infinity`. Thus relative linearization of the gamma-subtracted residual survives strictly below `sqrt(L)`. The current relative-error boundary is instead `x^2 log x=O(L)`, roughly `sqrt(L/log L)` up to slowly varying factors.

The two scales answer different questions. `x~sqrt(L)` is where present errors stop being negligible compared with `H`; it is **not** where they stop being negligible compared with the remaining diagonal signal `H log x`. Any lower-boundary claim must therefore specify what has been subtracted and what output scale is supposed to reveal new information before interpreting an error crossover as a mathematical mechanism.

**Boundary.** Neither `sqrt(L)` nor `sqrt(L/log L)` is proved sharp or intrinsic. They are consequences of the currently propagated Wang error terms, and a sharper estimate or cancellation among those terms could move them. The near-ceiling source regime is separate, and no new zero-free region or RH implication follows from these normalizations.