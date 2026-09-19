# MI-055 — Derivative depth and source amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-431](../../findings/AF-431-constant-rational-supercritical-sources-hit-first-saddle-window.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal. AF-417 shows that this closure is not uniform in an independently moving derivative offset: fixed partition sectors see `s_n/n->sigma` by multiplying the Cauchy parameter by `e^sigma`. AF-418 then shows that the complete growing partition family detects the finer transition `sigma=2`, with critical coordinate

`tau_n=((s_n/n)-2)log n`.

AF-419--AF-420 identify the corresponding phase boundary. Below `2` a shape-uniform absolute majorant closes the exceptional-`1` family. In the critical window derivative depth and source amplitude combine into

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`.

AF-421--AF-424 resolve the signed organization near square transition values `b=m^2`. Full-column packets around adjacent rectangles tie at leading exponential order; then the exact rectangle ratio, complete-packet drift and the discrete derivative offset become successive retained coordinates. A nominal saddle equality is therefore only the first layer of the cancellation problem.

AF-425--AF-428 show why those coordinates must be pulled back to the actual source. The formal second-order target is continuously tunable, but `d_n=s_n-2n` is integral. On exact square-amplitude fibers bounded packet balance forces `d_n=-1` eventually and still misses the target. Allowing the amplitude to move produces an exceptional set that is Lebesgue-null and Hausdorff-thin but dense `G_delta`. Pointwise source membership is not decided by either metric or category genericity.

AF-429--AF-430 expose a second shrinking-target hierarchy above the critical transition. For `q_n=s_n/n->sigma>2`, the dominant rectangle width moves to

`R_n=a^(1/q_n)n^(1-2/q_n)`.

The exact adjacent ratio crosses one at a real center `tau_n~R_n`; integer packets can be comparable only if `dist(tau_n,Z)=O(R_n/n)`. Summing all residual partition shapes preserves that first aperture and shifts the refined complete-packet balance center only by `Theta(R_n/n^2)`.

AF-431 changes the interpretation of that first supercritical gate. For any fixed rational density `q=u/v>2` on the exact progression `n=vk, s=uk`, the real saddle is eventually monotone and

`tau'(n)=((q-2)/q)R(n)/n(1+o(1))`.

Hence consecutive admissible saddle samples are themselves spaced at `Theta(R_n/n)`. Because the sampled saddle diverges while its increments tend to zero, it crosses every sufficiently large integer within one source step. The AF-429 first window is therefore hit infinitely often automatically; when `v` is odd the same conclusion survives on an odd-`n` sign-alternating progression. The complete packets are then order-one comparable, but the source step remains a factor `n` coarser than the AF-430 packet-corrected `R_n/n^2` center.

The reusable lesson is not simply that discrete source lattices obstruct continuous saddle tuning. It is that **every retained asymptotic coordinate must be compared with the mesh of the admissible source class at the same scale**. The critical displaced branch exhibits a genuinely too-coarse integer depth at second order. The supercritical rational constant-density branch passes its first lattice gate because source motion and target width match, yet immediately encounters a finer packet target that the same argument does not resolve. Source realizability is a hierarchy, not a binary property.

**Boundary.** AF-431 settles only the first `O(R_n/n)` window for fixed rational supercritical density and, with odd denominator, its odd sign-alternating progression. It does not settle arbitrary varying `q_n`, the refined `R_n/n^2` alignment, cancellation to the precision required by exponentially large packets, or the omitted determinant sectors. No statement here selects rational primes, zeta zeros or RH.