# MI-055 — Derivative depth and source amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-422](../../findings/AF-422-square-transition-detuning-controls-adjacent-packet-cancellation.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal. AF-417 shows that this closure is not uniform in an independently moving derivative offset: fixed partition sectors see `s_n/n->sigma` by multiplying the Cauchy parameter by `e^sigma`. AF-418 then shows that the complete growing partition family detects a finer critical coordinate at `sigma=2`, namely

`tau_n=((s_n/n)-2)log n`.

AF-419 proves that the opposite side is genuinely controlled: if `limsup s_n/n<2`, a shape-uniform absolute majorant closes the entire exceptional-`1` partition family. AF-420 sharpens the phase boundary. In the critical window `s_n/n->2`, derivative depth and source amplitude no longer separate; the effective coordinate is

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`, with `a=c^2/(4pi^2)`.

If `limsup b_n(A)<1`, absolute resummation survives uniformly on `0<=a<=A`. If `tau_n->tau`, the controlled domain is every compact `a<e^(-tau)`. On the exact sequence `s_n=2n`, this is every compact `a<1`, equivalently `c<2pi`.

AF-421 resolves the signed finite-`tau` organization beyond that absolute boundary. When `b_n->b in (0,infinity)`, the exponentially leading families are full-column packets around rectangles `(r^n)` with nth-root rates

`L_r(b)=b^r/(r!)^2`.

Away from the square values `b=m^2`, a single packet dominates: `r=floor(sqrt(b))`. The packet carries the same residual Schur--Cauchy factor `exp(-a e^2)`, so every nonsquare superthreshold value `b>1` gives genuine signed divergence rather than cancellation back to the fixed-partition limit. The apparent continuum boundary therefore resolves into a **discrete saddle hierarchy** with transitions at `1,4,9,...`.

AF-422 resolves the first subleading coordinate on those collision fibers. Write `s_n=2n+d_n`, `d_n=o(n)`, and suppose `b_n->m^2`. Then the ratio of the two adjacent rectangular packet amplitudes has the form

`F_(n,m)=K_m exp(Xi_(n,m))(1+o(1))`,

where

`Xi_(n,m)=log n+n log(b_n/m^2)-d_n log m`

and `K_m>0` is explicit. Thus the equality of exponential rates is still too coarse. Even `n` reinforces the adjacent packets, while for odd `n` leading rectangular cancellation is possible only under the finer tuning

`Xi_(n,m)->-log K_m`.

Outside that tuning the two leading rectangles do not cancel. For `m>=2` the surviving packet has exponential nth-root rate greater than one. The exact square path `a=m^2, s_n=2n` has `Xi_(n,m)=log n`, so it is not a cancellation path; the first square `m=1` reproduces the previously known linear divergence, and higher exact squares diverge exponentially.

The reusable lesson is now stratified. A joint critical coordinate can contain a quantized family of saddle collisions, and the collision locus can require a **second retained asymptotic coordinate** before the sign is decided. After that coordinate is tuned, the relevant object changes again: one must compare the complete packet factors, not merely their rectangular cores. Uniformity on an open stratum therefore does not automatically control its collision fibers.

**Boundary.** This synthesis concerns the exceptional-`1` Cauchy--Binet sector in finite critical windows. The remaining finite-window problem is only the odd tuned interface `Xi_(n,m)->-log K_m`, where cancellation of the rectangular cores makes the complete residual packet ratio load-bearing. The genuinely supercritical regime `s_n/n>2` with `b_n->infinity` requires a different moving-saddle analysis. Other determinant sectors and zero selection remain separate.