# MI-055 — Derivative depth and source amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-423](../../findings/AF-423-adjacent-residual-packets-have-universal-inverse-n-drift.md).

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

and `K_m>0` is explicit. Thus equality of exponential rates is still too coarse. Even `n` reinforces the adjacent packets, while for odd `n` leading rectangular cancellation is possible only when `Xi_(n,m)->-log K_m`.

AF-423 shows that this rectangle-level tuning is still one scale too coarse. If `G_(n,r)` is the complete residual Schur--Cauchy factor of the `r`-column packet, then on every fixed square fiber

`log(G_(n,m)/G_(n,m-1)) = 2 a e^2/n + o(1/n)`.

Hence the complete adjacent-packet ratio `Q_(n,m)=F_(n,m)G_(n,m)/G_(n,m-1)` satisfies

`log Q_(n,m)=log F_(n,m)+2 a e^2/n+o(1/n)`.

For odd `n`, even `F_(n,m)->1` does not cancel the complete packets. First packet-level cancellation additionally requires the inverse-`n` tuning

`n log F_(n,m) -> -2 a e^2`.

For `m>=2`, failure of this condition leaves only a polynomial suppression of a tied saddle whose common nth-root rate is greater than one, so the residual still diverges exponentially. The coefficient `2ae^2` is not an arbitrary correction: AF-423 derives a one-partition drift depending only on residual degree and sums it exactly under the limiting signed Schur packet.

The reusable lesson is now a **nested asymptotic-coordinate hierarchy**. The square condition `b_n=m^2+o(1)` retains too little information; rectangle balance `F_(n,m)=1+o(1)` retains more but still loses the first complete-packet asymmetry; cancellation at the next level requires `n log F_(n,m)+2ae^2->0`. Each time a collision is tuned away, the load-bearing object changes and exposes a finer coordinate. Uniformity on an open stratum therefore does not control its collision fibers, and equality of leading saddles does not control the summed packets around them.

**Boundary.** This synthesis concerns the exceptional-`1` Cauchy--Binet sector in finite critical windows. AF-423 gives a necessary first packet-level cancellation condition, not boundedness or recovery of the fixed-partition exponential. After `n log F_(n,m)->-2ae^2`, the decisive quantities are the next asymptotic term in the complete packet ratio, the correspondingly finer expansion of `F_(n,m)`, and the size of lower saddle packets. The genuinely supercritical regime `s_n/n>2` with `b_n->infinity`, other determinant sectors, and zero selection remain separate.