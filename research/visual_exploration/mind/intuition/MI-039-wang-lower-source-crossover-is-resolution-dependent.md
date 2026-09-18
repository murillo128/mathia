# MI-039 — Wang's lower-source crossover is resolution-dependent, and the relative mean is gamma normalization

**Evidence level:** exact error-budget and explicit-formula synthesis from [VIS-294](../../findings/VIS-294-wang-lower-moving-source-sqrtlog-crossover.md), [VIS-295](../../findings/VIS-295-wang-gamma-subtracted-residual-relative-crossover.md), [VIS-296](../../findings/VIS-296-wang-relative-boundary-reduces-to-explicit-formula-remainder-mean.md), and [VIS-297](../../findings/VIS-297-wang-boundary-remainder-mean-is-gamma-normalization.md), using the Wang/PNT inputs audited in those findings.

Write `H=T^theta` and `L=log T`. VIS-294 keeps Wang's explicit gamma contribution visible and shows that, for one fixed `lambda<theta`,

`F_I(x)=(H/(2pi))(L^2/x^2+log x)+o(H)`

uniformly through moving lower-source families satisfying `x/sqrt(L)->infinity` and `x<=T^lambda`. The apparent escape `beta(T)=log x/log T -> 0` is therefore too coarse: many vanishing-exponent families are already controlled to absolute `H` accuracy.

At that normalization, the current source-dependent errors `H L/x^2` and `H sqrt(L)/x` first reach `H` scale around `x~sqrt(L)`. This makes `sqrt(log T)` the first unresolved **absolute-`H`** lower corridor in the existing theorem, not a proved transition of the true statistic.

VIS-295 changes only the requested resolution. After subtracting the known gamma term, put

`R_gamma=F_I-(H/(2pi))L^2/x^2`.

Then

`R_gamma=(H/(2pi))log x+o(H log x)`

whenever `x^2 log x/L -> infinity`, so relative linearization survives below `sqrt(L)`. VIS-296 identifies the finite relative boundary exactly: if

`x^2 log x/L -> kappa in (0,infinity)`, 

then

`R_gamma/(H log x)=1/(2pi)+Re Q_E(T,x)/(pi kappa)+o(1)`,

where `Q_E(T,x)=(x/H) integral_I E_x(t) dt` is Wang's normalized explicit-formula remainder mean.

VIS-297 evaluates that channel. Refining the exact Landau/functional-equation decomposition gives

`Re Q_E(T,x)=-log(2pi)+o(1)`.

The constant comes from the gamma factor omitted by the coarse baseline `B_x(t)=log(t+2)/x`; the absolutely convergent `zeta'/zeta(3/2-it)` term has vanishing interval mean and the pole/trivial-zero terms are negligible. Hence

`R_gamma/(H log x)=1/(2pi)-log(2pi)/(pi kappa)+o(1)`.

The finite relative crossover is therefore not a new source-arithmetic regime. It records a deterministic choice of baseline. Replacing the coarse logarithmic scale by the natural gamma-normalized one removes the apparent order-one remainder mean. The reusable diagnostic is stronger than before: **a moving error boundary is not evidence of new arithmetic until every deterministic explicit-formula normalization surviving at the requested output scale has been extracted.**

The two lower scales still answer different questions. `x^2 log x~L` is now a resolved relative normalization crossover. The first unresolved absolute-`H` corridor remains `x=O(sqrt(L))`, where the current theorem's load-bearing errors are large enough that a sharper source-specific calculation could still matter.

**Boundary.** Neither `sqrt(L)` nor `sqrt(L/log L)` is proved to be an intrinsic transition of the true statistic. VIS-297 closes the relative mean channel only; it does not resolve the absolute-`H` boundary, the near-ceiling source regime, the fixed-power real-axis branch, or any RH implication.