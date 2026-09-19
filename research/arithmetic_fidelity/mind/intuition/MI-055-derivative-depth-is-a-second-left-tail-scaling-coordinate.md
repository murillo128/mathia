# MI-055 — Derivative depth and source amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-428](../../findings/AF-428-second-order-exceptional-amplitudes-are-residual-but-null.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal. AF-417 shows that this closure is not uniform in an independently moving derivative offset: fixed partition sectors see `s_n/n->sigma` by multiplying the Cauchy parameter by `e^sigma`. AF-418 then shows that the complete growing partition family detects a finer critical coordinate at `sigma=2`, namely

`tau_n=((s_n/n)-2)log n`.

AF-419 proves that if `limsup s_n/n<2`, a shape-uniform absolute majorant closes the entire exceptional-`1` partition family. AF-420 sharpens the phase boundary. In the critical window `s_n/n->2`, derivative depth and source amplitude no longer separate; the effective coordinate is

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`, with `a=c^2/(4pi^2)`.

AF-421 resolves the signed finite-window organization beyond that absolute boundary. When `b_n->b in (0,infinity)`, the exponentially leading families are full-column packets around rectangles `(r^n)` with nth-root rates `L_r(b)=b^r/(r!)^2`. Away from square values `b=m^2`, one packet dominates. At a square value, adjacent packets tie and the problem acquires a hierarchy of finer retained coordinates.

AF-422--AF-424 identify the first two such coordinates. Writing `s_n=2n+d_n`, `alpha_n=d_n/n`, the adjacent rectangular ratio is controlled by `Xi_(n,m)`, complete packets add an inverse-`n` drift, and the corrected packet ratio retains the derivative offset through `m alpha_n` before limits are taken. On generic square-transition paths that term can dominate the packet correction itself.

AF-425 pushes the hierarchy one order deeper and exposes a source-realizability gate. Its formal second-order cancellation target is continuously solvable, but `d_n` is an integer source coordinate. Increasing `d_n` by one changes the corrected target by `~log n`, while the required residual window shrinks by inverse powers of `n`.

AF-426 closes the exact square-amplitude fibers without an equidistribution hypothesis. If `a=m^2` and the complete adjacent-packet ratio stays bounded, the integer depth must satisfy `d_n=-1` eventually. At that only surviving depth the packet ratio tends to `m K_m>1`, so it cannot approach one; the `o(n^-2)` shrinking target has no solutions.

AF-427 shows that allowing the amplitude to move does not restore a metrically generic escape. Put `A=log(m^2/a)`. Square compatibility is `d log n/n -> A`, so on a compact displacement range there are only `O(n/log n)` admissible integer depths at scale `n`. The second-order target `H_(n,m)(d;A)` is transverse in `A`, with derivative of size `~n`; therefore each `|H|<=n^-2` source cell occupies only `O(n^-3)` amplitude width. The limsup has Lebesgue measure zero and Hausdorff dimension at most `2/3`.

AF-428 proves that the very same exceptional set is nevertheless a dense `G_delta`. The branch is therefore **residual but null**: topological genericity, metric prevalence and pointwise source membership diverge. Exact square amplitude remains excluded, while exceptional amplitudes occur arbitrarily near every point. Consequently neither an open-neighborhood obstruction nor an almost-everywhere theorem can decide a distinguished source-forced amplitude.

The reusable lesson is a **nested asymptotic-coordinate hierarchy whose final tuning must survive the actual source lattice, and whose surviving set must be classified in the right notion of size**. Equality at one scale does not control a collision fiber at the next, and solving a continuous cancellation equation is not enough when the physical parameter is discrete. Even after transversality makes successful recurrence metrically thin, Baire category can make the same recurrence topologically generic. The final gate is therefore exact arithmetic membership in the moving shrinking target, not generic perturbation or prevalence.

**Boundary.** AF-428 does not show that any particular distinguished amplitude belongs to the residual exceptional set, improve the Hausdorff-dimension upper bound, control the undisplayed determinant remainder, or couple different packet indices. Lower saddles, tall-column families, beyond-all-orders effects, the genuinely supercritical regime `s_n/n>2`, other determinant sectors and zero selection remain separate.