# MI-055 — Derivative depth and source amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-421](../../findings/AF-421-finite-critical-windows-reduce-to-full-column-saddle-hierarchy.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal. AF-417 shows that this closure is not uniform in an independently moving derivative offset: fixed partition sectors see `s_n/n->sigma` by multiplying the Cauchy parameter by `e^sigma`. AF-418 then shows that the complete growing partition family detects a finer critical coordinate at `sigma=2`, namely

`tau_n=((s_n/n)-2)log n`.

AF-419 proves that the opposite side is genuinely controlled: if `limsup s_n/n<2`, a shape-uniform absolute majorant closes the entire exceptional-`1` partition family. AF-420 sharpens the phase boundary. In the critical window `s_n/n->2`, derivative depth and source amplitude no longer separate; the effective coordinate is

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`, with `a=c^2/(4pi^2)`.

If `limsup b_n(A)<1`, absolute resummation survives uniformly on `0<=a<=A`. If `tau_n->tau`, the controlled domain is every compact `a<e^(-tau)`. On the exact sequence `s_n=2n`, this is every compact `a<1`, equivalently `c<2pi`.

AF-421 resolves the signed finite-`tau` organization beyond that absolute boundary. When `b_n->b in (0,infinity)`, the exponentially leading families are full-column packets around rectangles `(r^n)` with nth-root rates

`L_r(b)=b^r/(r!)^2`.

Away from the square values `b=m^2`, a single packet dominates: `r=floor(sqrt(b))`. The packet carries the same residual Schur--Cauchy factor `exp(-a e^2)`, so every nonsquare superthreshold value `b>1` gives genuine signed divergence rather than cancellation back to the fixed-partition limit. The apparent continuum boundary therefore resolves into a **discrete saddle hierarchy** with transitions at `1,4,9,...`.

At `b=m^2`, exactly two adjacent full-column packets tie exponentially. Their exact ratio is the remaining cancellation coordinate. For even `n` the packet signs agree; for odd `n` they oppose, so only a finer tuning in which the ratio approaches one can cancel at leading order. The first transition is already closed on `s_n=2n,a=1`: the complete signed sector diverges linearly with parity-alternating sign.

The reusable lesson is stronger than “two moving parameters matter.” A joint critical coordinate can itself contain a **quantized family of competing saddles**. The right phase diagram is not only `sigma<2`, `sigma=2`, `sigma>2`, nor even only `b<1` versus `b>1`; after absolute control fails, one must identify which large-complexity packet actually carries the signed asymptotics and where two packet rates tie.

**Boundary.** This synthesis concerns the exceptional-`1` Cauchy--Binet sector in finite critical windows. The remaining finite-window problem is the odd-`n` next-order cancellation at square fibers `b=m^2`; the genuinely supercritical regime `s_n/n>2` with `b_n->infinity` requires a different moving saddle analysis. Other determinant sectors and zero selection remain separate.