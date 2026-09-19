# MI-055 — Derivative depth and source amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-427](../../findings/AF-427-displaced-square-packet-cancellation-is-metrically-exceptional.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal. AF-417 shows that this closure is not uniform in an independently moving derivative offset: fixed partition sectors see `s_n/n->sigma` by multiplying the Cauchy parameter by `e^sigma`. AF-418 then shows that the complete growing partition family detects a finer critical coordinate at `sigma=2`, namely

`tau_n=((s_n/n)-2)log n`.

AF-419 proves that if `limsup s_n/n<2`, a shape-uniform absolute majorant closes the entire exceptional-`1` partition family. AF-420 sharpens the phase boundary. In the critical window `s_n/n->2`, derivative depth and source amplitude no longer separate; the effective coordinate is

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`, with `a=c^2/(4pi^2)`.

AF-421 resolves the signed finite-window organization beyond that absolute boundary. When `b_n->b in (0,infinity)`, the exponentially leading families are full-column packets around rectangles `(r^n)` with nth-root rates `L_r(b)=b^r/(r!)^2`. Away from the square values `b=m^2`, one packet dominates. At a square value, adjacent packets tie and the problem acquires a hierarchy of finer retained coordinates.

AF-422--AF-424 identify the first two such coordinates. Writing `s_n=2n+d_n`, `alpha_n=d_n/n`, the adjacent rectangular ratio is controlled by `Xi_(n,m)`, complete packets add an inverse-`n` drift, and the corrected packet ratio retains the derivative offset through `m alpha_n` before limits are taken. On generic square-transition paths that term can dominate the packet correction itself.

AF-425 pushes the hierarchy one order deeper and exposes a source-realizability gate. Its formal second-order cancellation target is continuously solvable, but `d_n` is an integer source coordinate. Increasing `d_n` by one changes the exact corrected target by `log(n/m)+m/n+O(n^-2)`, hence by `~log n`, while the required residual window shrinks by inverse powers of `n`.

AF-426 closes the exact square-amplitude fibers without an equidistribution hypothesis. If `a=m^2` and the complete adjacent-packet ratio stays bounded, the integer depth must satisfy `d_n=-1` eventually. At that only surviving depth the packet ratio tends to `m K_m>1`, so it cannot approach one; the `o(n^-2)` shrinking target has no solutions. Thus the square transition is not merely hard to tune on the source lattice: on exact square amplitude it has an irreducible integer packet gap.

AF-427 shows that allowing the amplitude to move does not restore a generic escape. Put `A=log(m^2/a)`. Square compatibility is `d log n/n -> A`, so on a compact displacement range there are only `O(n/log n)` admissible integer depths at scale `n`. The second-order target `H_(n,m)(d;A)` is transverse in `A`, with `|partial_A H|>=n/2` for large `n`; therefore each `|H|<=n^-2` source cell occupies only `O(n^-3)` amplitude width. The limsup of all such cells has Lebesgue measure zero and Hausdorff dimension at most `2/3`.

The reusable lesson is a **nested asymptotic-coordinate hierarchy whose final tuning must survive both discrete-source spacing and metric transversality**. Equality at one scale does not control a collision fiber at the next, and solving a continuous cancellation equation is not enough when the physical parameter lives on a source lattice. Pull every target back to the admissible source coordinates and measure how much source parameter space can hit the required shrinking window: an exact fiber can be empty, while a drifting family can survive only on a metrically thin exceptional set.

**Boundary.** AF-427 does not prove that its exceptional set is empty, countable or sharp at dimension `2/3`, and an arithmetically distinguished amplitude could still lie in it. The remaining finite-window question is pointwise Diophantine structure of those exceptional amplitudes. Lower saddles, tall-column families, beyond-all-orders effects, the genuinely supercritical regime `s_n/n>2`, other determinant sectors and zero selection remain separate.