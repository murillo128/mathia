# MI-055 — Derivative depth and source amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-432](../../findings/AF-432-supercritical-packet-center-amplitudes-are-residual-but-metrically-thin.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal. AF-417 shows that this closure is not uniform in an independently moving derivative offset: fixed partition sectors see `s_n/n->sigma` by multiplying the Cauchy parameter by `e^sigma`. AF-418 then shows that the complete growing partition family detects the finer transition `sigma=2`, with critical coordinate

`tau_n=((s_n/n)-2)log n`.

AF-419--AF-420 identify the corresponding phase boundary. Below `2` a shape-uniform absolute majorant closes the exceptional-`1` family. In the critical window derivative depth and source amplitude combine into

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`.

AF-421--AF-424 resolve the signed organization near square transition values `b=m^2`. Full-column packets around adjacent rectangles tie at leading exponential order; then the exact rectangle ratio, complete-packet drift and the discrete derivative offset become successive retained coordinates. A nominal saddle equality is therefore only the first layer of the cancellation problem.

AF-425--AF-428 show why those coordinates must be pulled back to the actual source. The formal second-order target is continuously tunable, but `d_n=s_n-2n` is integral. On exact square-amplitude fibers bounded packet balance forces `d_n=-1` eventually and still misses the target. Allowing the amplitude to move produces an exceptional set that is Lebesgue-null and Hausdorff-thin but dense `G_delta`. Pointwise source membership is not decided by either metric or category genericity.

AF-429--AF-430 expose a second shrinking-target hierarchy above the critical transition. For `q_n=s_n/n->sigma>2`, the dominant rectangle width moves to

`R_n=a^(1/q_n)n^(1-2/q_n)`.

The exact adjacent ratio crosses one at a real center `tau_n~R_n`; integer packets can be comparable only if `dist(tau_n,Z)=O(R_n/n)`. Summing all residual partition shapes preserves that first aperture and shifts the refined complete-packet balance center only by `Theta(R_n/n^2)`.

AF-431 changes the interpretation of the first supercritical gate. For any fixed rational density `q=u/v>2` on the exact progression `n=vk, s=uk`, the real saddle is eventually monotone and

`tau'(n)=((q-2)/q)R(n)/n(1+o(1))`.

Hence consecutive admissible saddle samples are themselves spaced at `Theta(R_n/n)`. Because the sampled saddle diverges while its increments tend to zero, it crosses every sufficiently large integer within one source step. The AF-429 first window is therefore hit infinitely often automatically; when `v` is odd the same conclusion survives on an odd-`n` sign-alternating progression.

AF-432 shows that the next aperture has a different logical status. With the first packet correction included,

`hat(tau)_n(a)=tau_n(a)+a e^q R_n(a)/n^2`,

the amplitude set for which

`dist(hat(tau)_n(a),Z)=o(R_n/n^2)`

infinitely often is a dense `G_delta`, has Lebesgue measure zero, and has Hausdorff dimension at most `1-1/q`. Moreover first-order complete exceptional-`1` packet balance implies membership in this set. The factor-`n` refinement is therefore neither generically absent nor generically present in a pointwise sense: topological prevalence and metric rarity coexist.

The reusable lesson is not simply that discrete source lattices obstruct continuous saddle tuning. **Every retained asymptotic coordinate must be compared with the mesh of the admissible source class at the same scale, and genericity notions do not replace pointwise source membership.** The critical displaced branch exhibits a genuinely too-coarse integer depth at second order. The supercritical rational constant-density branch passes its first lattice gate because source motion and target width match. Its next packet-corrected gate is residual but metrically thin in amplitude, so deciding a distinguished source requires arithmetic information beyond mesh size, Lebesgue measure or Baire category.

**Boundary.** AF-432 classifies only the first packet-corrected `R_n/n^2` target for fixed rational supercritical density and gives a necessary condition for first-order complete-packet balance. It does not decide membership for a distinguished arithmetic amplitude, give the next uniform packet correction, control omitted determinant sectors, settle arbitrary varying `q_n`, select rational primes or zeta zeros, or imply RH.
