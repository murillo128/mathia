# MI-055 — Derivative depth and free probe amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-433](../../findings/AF-433-free-left-tail-amplitude-is-not-a-source-discriminator.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal. AF-417 shows that this closure is not uniform in an independently moving derivative offset: fixed partition sectors see `s_n/n->sigma` by multiplying the Cauchy parameter by `e^sigma`. AF-418 then shows that the complete growing partition family detects the finer transition `sigma=2`, with critical coordinate

`tau_n=((s_n/n)-2)log n`.

AF-419--AF-420 identify the corresponding phase boundary. Below `2` a shape-uniform absolute majorant closes the exceptional-`1` family. In the critical window derivative depth and probe amplitude combine into

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`.

AF-421--AF-424 resolve the signed organization near square transition values `b=m^2`. Full-column packets around adjacent rectangles tie at leading exponential order; then the exact rectangle ratio, complete-packet drift and the discrete derivative offset become successive retained coordinates. A nominal saddle equality is therefore only the first layer of the cancellation problem.

AF-425--AF-428 show why those coordinates must be pulled back to the actual admissible source variables. The formal second-order target is continuously tunable, but `d_n=s_n-2n` is integral. On exact square-amplitude fibres bounded packet balance forces `d_n=-1` eventually and still misses the target. Allowing the amplitude to move produces an exceptional set that is Lebesgue-null and Hausdorff-thin but dense `G_delta`. Pointwise membership is not decided by either metric or category genericity.

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

AF-433 adds an earlier provenance gate. In the canonical AF-416--AF-432 source chain the diagonal path is `x_n(c)=c/n` with arbitrary `c>0`, and

`a=c^2/(4pi^2)`

is a smooth bijective reparameterization of that free probe constant. Thus every positive amplitude is reachable without changing the intrinsic source function. The AF-432 exceptional set pulls back to an equally residual, null and dimension-thin set of probe paths `c`; it does not identify a distinguished source amplitude. Likewise the square values `a=m^2` are selected by downstream saddle-rate collisions, not by an independent source rule.

The reusable lesson is therefore two-stage. **First establish provenance: is the asymptotic coordinate selected intrinsically by the source, or is it only an externally chosen probe path? Only after that should its admissible mesh be compared with the target aperture at the same scale.** The critical displaced branch exhibits a genuinely too-coarse integer depth at second order. The supercritical rational constant-density branch passes its first lattice gate because source motion and target width match. But the next packet-corrected target becomes source-discriminating only if a source-native rule first selects `c` or `a` independently of the desired shrinking-target outcome.

**Boundary.** AF-433 does not prove that no source-intrinsic selector for `c` can exist; it proves that none is present in the canonical AF-416--AF-432 chain. AF-432 still classifies the first packet-corrected `R_n/n^2` target for fixed rational supercritical density and gives a necessary condition for first-order complete-packet balance. The current synthesis does not construct an intrinsic amplitude selector, decide pointwise membership after such a selector is supplied, give the next uniform packet correction, control omitted determinant sectors, settle arbitrary varying `q_n`, select rational primes or zeta zeros, or imply RH.
