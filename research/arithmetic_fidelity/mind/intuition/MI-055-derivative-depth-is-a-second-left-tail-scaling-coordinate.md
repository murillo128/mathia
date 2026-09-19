# MI-055 — Derivative depth and source amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-430](../../findings/AF-430-supercritical-residual-packets-preserve-shrinking-saddle-window.md).

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

AF-429 shows that the same lattice issue reappears on the genuinely supercritical side in a different coordinate. If `q_n=s_n/n->sigma>2`, the full-height rectangular family has moving saddle width

`R_n=a^(1/q_n) n^(1-2/q_n)`,

and for `r_n/R_n->t` its logarithmic profile is

`(n R_n)^(-1) log C_(n,r_n) -> sigma t(1-log t)`.

The continuous maximum is at `t=1`, but the exact adjacent-width ratio crosses one at a real point `tau_n~R_n` with local slope of order `n/R_n`. Hence two adjacent **integer** rectangles can even have comparable magnitude only if

`dist(tau_n,Z)=O(R_n/n)=O(n^(-2/sigma+o(1)))`.

AF-430 shows that the complete residual partition packet does not repair that mismatch. Whenever an integer sequence reaches the AF-429 window, the adjacent residual factors satisfy

`G_(n,r_n-1), G_(n,r_n) -> exp(-a e^sigma)`

and

`log(G_(n,r_n)/G_(n,r_n-1)) = sigma a e^sigma/n + o(n^-1)`.

Thus the complete-packet balance center moves only by `a e^sigma R_n/n^2(1+o(1))`, while the necessary integer-comparability window remains `R_n/n`. The packet correction is a real finer coordinate, but it is **sub-window**: summing all residual partition shapes does not enlarge the lattice aperture in which cancellation can start.

The reusable lesson is a **nested asymptotic-coordinate hierarchy whose final tuning must survive the actual source lattice**. At the critical transition, square-amplitude balance descends to an integer derivative-depth shrinking target whose exceptional amplitude set is residual but null. Above the transition, the optimizer moves to `R_n`, adjacent cancellation requires a shrinking integer hit at resolution `R_n/n`, and the complete residual packet only refines the center at `R_n/n^2`. Continuous saddle balance, packet resummation and discrete source realizability are separate mathematical gates.

**Boundary.** AF-430 does not decide whether a distinguished source amplitude satisfies the critical displaced shrinking target, whether the supercritical centers `tau_n` hit integers at the required `R_n/n` rate, whether a surviving hit reaches the packet-corrected `R_n/n^2` center closely enough, or whether the omitted determinant sectors remain subordinate. No statement here selects rational primes, zeta zeros or RH.
