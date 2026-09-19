# MI-055 — Derivative depth and source amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-424](../../findings/AF-424-complete-square-packet-cancellation-has-explicit-derivative-offset-detuning.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal. AF-417 shows that this closure is not uniform in an independently moving derivative offset: fixed partition sectors see `s_n/n->sigma` by multiplying the Cauchy parameter by `e^sigma`. AF-418 then shows that the complete growing partition family detects a finer critical coordinate at `sigma=2`, namely

`tau_n=((s_n/n)-2)log n`.

AF-419 proves that the opposite side is genuinely controlled: if `limsup s_n/n<2`, a shape-uniform absolute majorant closes the entire exceptional-`1` partition family. AF-420 sharpens the phase boundary. In the critical window `s_n/n->2`, derivative depth and source amplitude no longer separate; the effective coordinate is

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`, with `a=c^2/(4pi^2)`.

If `limsup b_n(A)<1`, absolute resummation survives uniformly on `0<=a<=A`. AF-421 then resolves the signed finite-window organization beyond that absolute boundary. When `b_n->b in (0,infinity)`, the exponentially leading families are full-column packets around rectangles `(r^n)` with nth-root rates

`L_r(b)=b^r/(r!)^2`.

Away from the square values `b=m^2`, a single packet dominates. At the square values, adjacent packets `r=m-1,m` tie and the problem acquires a hierarchy of finer retained coordinates rather than one scalar critical parameter.

AF-422 gives the first such coordinate. Write `s_n=2n+d_n`, `alpha_n=d_n/n`, and suppose `b_n->m^2`. The adjacent rectangular ratio has the form

`F_(n,m)=K_m exp(Xi_(n,m))(1+o(1))`,

where

`Xi_(n,m)=log n+n log(b_n/m^2)-d_n log m`.

Thus equality of exponential rates is too coarse. Even `n` reinforces the two packets, while for odd `n` leading rectangular cancellation is possible only when `Xi_(n,m)->-log K_m`.

AF-423 shows that rectangle balance is still one scale too coarse. If `G_(n,r)` is the complete residual Schur--Cauchy factor of the `r`-column packet, then

`log(G_(n,m)/G_(n,m-1))=2ae^2/n+o(1/n)`.

AF-424 resolves the missing detuning at the same scale instead of replacing `alpha_n` by its limit too early. It proves

`log F_(n,m)=Xi_(n,m)+log K_m+m alpha_n+[-m^2+m-1-(m^2/2)alpha_n]/n+O(n^-2)`

and

`log(G_(n,m)/G_(n,m-1))=a e^(2+alpha_n)(2+alpha_n)/n+O(n^-2)`.

Consequently, if

`Omega_(n,m)=Xi_(n,m)+log K_m+m alpha_n`,

then the complete adjacent-packet ratio satisfies

`log Q_(n,m)=Omega_(n,m)+[-m^2+m-1-(m^2/2)alpha_n+a e^(2+alpha_n)(2+alpha_n)]/n+O(n^-2)`.

The first complete cancellation condition on the odd square fiber is therefore not merely `n log F_(n,m)->-2ae^2`, but the equivalent explicit source-coordinate condition

`n(Xi_(n,m)+log K_m)+m d_n -> m^2-m+1-2ae^2`.

The term `m alpha_n` is load-bearing. On a generic square path with `a!=m^2`, the square constraint forces `alpha_n log n -> log(m^2/a)`, so this detuning is naturally order `1/log n`, larger than the inverse-`n` packet correction. AF-424 also shows that the first partition-shape correction cancels only after the complete packet is summed by conjugation symmetry. Packetwise asymptotics can therefore contain structure that disappears at the exact signed-family level.

The reusable lesson is a **nested asymptotic-coordinate hierarchy**. Equality at one scale does not control a collision fiber at the next: `b_n=m^2+o(1)` loses rectangle balance; `F_(n,m)=1+o(1)` loses the first complete-packet drift; and even inverse-`n` cancellation must retain derivative-offset detuning before taking limits. Every successful tuning changes the load-bearing object and may expose another coordinate, symmetry cancellation or lower saddle.

**Boundary.** AF-424 supplies a necessary first complete-packet cancellation law, not boundedness or recovery of the fixed-partition exponential. For `m>=2`, a polynomially small mismatch still multiplies an exponentially growing tied saddle. After the displayed tuning, the decisive objects are the next complete-packet expansion and any lower-saddle, tall-column or beyond-all-orders residual. The genuinely supercritical regime `s_n/n>2`, other determinant sectors and zero selection remain separate.
