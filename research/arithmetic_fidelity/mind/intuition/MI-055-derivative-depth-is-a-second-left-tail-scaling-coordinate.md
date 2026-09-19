# MI-055 — Derivative depth and source amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-425](../../findings/AF-425-second-order-square-packet-detuning-exposes-source-lattice.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal. AF-417 shows that this closure is not uniform in an independently moving derivative offset: fixed partition sectors see `s_n/n->sigma` by multiplying the Cauchy parameter by `e^sigma`. AF-418 then shows that the complete growing partition family detects a finer critical coordinate at `sigma=2`, namely

`tau_n=((s_n/n)-2)log n`.

AF-419 proves that if `limsup s_n/n<2`, a shape-uniform absolute majorant closes the entire exceptional-`1` partition family. AF-420 sharpens the phase boundary. In the critical window `s_n/n->2`, derivative depth and source amplitude no longer separate; the effective coordinate is

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`, with `a=c^2/(4pi^2)`.

AF-421 resolves the signed finite-window organization beyond that absolute boundary. When `b_n->b in (0,infinity)`, the exponentially leading families are full-column packets around rectangles `(r^n)` with nth-root rates `L_r(b)=b^r/(r!)^2`. Away from the square values `b=m^2`, one packet dominates. At a square value, adjacent packets tie and the problem acquires a hierarchy of finer retained coordinates.

AF-422 gives the first such coordinate. Writing `s_n=2n+d_n`, `alpha_n=d_n/n`, the adjacent rectangular ratio is controlled by

`Xi_(n,m)=log n+n log(b_n/m^2)-d_n log m`.

AF-423 shows that rectangle balance is still one scale too coarse because the complete residual packet contributes an inverse-`n` drift. AF-424 then retains `alpha_n` before taking limits and proves that the complete adjacent-packet ratio has

`log Q_(n,m)=Omega_(n,m)+B_1(alpha_n)/n+O(n^-2)`,

with `Omega_(n,m)=Xi_(n,m)+log K_m+m alpha_n` and an explicit `B_1`. On generic square paths `m alpha_n` can be order `1/log n`, larger than the packet correction itself. The first complete cancellation condition therefore lives in the joint source/derivative coordinate rather than in the limiting square value alone.

AF-425 pushes this hierarchy one order deeper and adds a qualitatively new gate. The second-order cancellation condition can be written

`n^2 Omega_(n,m)+n B_1(alpha_n)+B_2(alpha_n)->0`,

but `d_n` is an integer source coordinate. In the exact corrected target, increasing `d_n` by one changes the cancellation coordinate by `log(n/m)+m/n+O(n^-2)`, hence by `~log n`. The formal continuous saddle can therefore sit between admissible source points. Achieving an `o(n^-1)` residual requires a shrinking fractional alignment of order `o((n log n)^-1)`; an `o(n^-2)` residual requires `o((n^2 log n)^-1)`.

The reusable lesson is a **nested asymptotic-coordinate hierarchy with a source-realizability gate**. Equality at one scale does not control a collision fiber at the next, and solving the continuous cancellation equation is not enough when the physical parameter lives on a discrete lattice. After each tuning, identify the new load-bearing coordinate, then pull its required accuracy back to the admissible source class before interpreting the tuned branch as real.

**Boundary.** AF-425 does not prove that the moving lattice target is hit or avoided infinitely often, and it does not give boundedness of the determinant on the tuned square fiber. The remaining arithmetic question is an inhomogeneous shrinking-target problem for the integer derivative-depth source. Lower saddles, tall-column families, beyond-all-orders effects, the genuinely supercritical regime `s_n/n>2`, other determinant sectors and zero selection remain separate.
