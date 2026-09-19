# MI-055 — Derivative depth, source-shell provenance, and probe amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-434](../../findings/AF-434-full-column-saddle-does-not-transport-source-shell-index.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal. AF-417 shows that this closure is not uniform in an independently moving derivative offset: fixed partition sectors see `s_n/n->sigma` by multiplying the Cauchy parameter by `e^sigma`. AF-418 then shows that the complete growing partition family detects the finer transition `sigma=2`, with critical coordinate

`tau_n=((s_n/n)-2)log n`.

AF-419--AF-420 identify the corresponding phase boundary. Below `2` a shape-uniform absolute majorant closes the exceptional-`1` family. In the critical window derivative depth and probe amplitude combine into

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`.

AF-421--AF-424 resolve the signed organization near square transition values `b=m^2`. Full-column packets around adjacent rectangles tie at leading exponential order; then the exact rectangle ratio, complete-packet drift and the discrete derivative offset become successive retained coordinates. A nominal saddle equality is therefore only the first layer of the cancellation problem.

AF-425--AF-428 show why those coordinates must be pulled back to the actual admissible source variables. The formal second-order target is continuously tunable, but `d_n=s_n-2n` is integral. On exact square-amplitude fibres bounded packet balance forces `d_n=-1` eventually and still misses the target. Allowing the amplitude to move produces an exceptional set that is Lebesgue-null and Hausdorff-thin but dense `G_delta`. Pointwise membership is not decided by either metric or category genericity.

AF-429--AF-430 expose a second shrinking-target hierarchy above the critical transition. For `q_n=s_n/n->sigma>2`, the dominant rectangle width moves to

`R_n=a^(1/q_n)n^(1-2/q_n)`.

The exact adjacent ratio crosses one at a real center `tau_n~R_n`; integer packets can be comparable only if `dist(tau_n,Z)=O(R_n/n)`. Summing all residual partition shapes preserves that first aperture and shifts the refined complete-packet balance center only by `Theta(R_n/n^2)`.

AF-431 changes the interpretation of the first supercritical gate. For any fixed rational density `q=u/v>2` on the exact progression `n=vk, s=uk`, the real saddle is eventually monotone and its consecutive source samples are spaced at `Theta(R_n/n)`. Because the sampled saddle diverges while its increments tend to zero, it crosses every sufficiently large integer within one source step. The AF-429 first window is therefore hit infinitely often automatically; when `v` is odd the same conclusion survives on an odd-`n` sign-alternating progression.

AF-432 shows that the next aperture has a different logical status. With the first packet correction included,

`hat(tau)_n(a)=tau_n(a)+a e^q R_n(a)/n^2`,

the amplitude set for which `dist(hat(tau)_n(a),Z)=o(R_n/n^2)` infinitely often is a dense `G_delta`, has Lebesgue measure zero, and has Hausdorff dimension at most `1-1/q`. First-order complete exceptional-`1` packet balance implies membership in this set. The factor-`n` refinement is therefore neither generically absent nor generically present in a pointwise sense.

AF-433 sharpens the provenance gate rather than making the square hierarchy purely target-side. In the canonical source chain the diagonal probe is `x_n(c)=c/n`, so every `c>0` remains externally selectable and `a=(c/(2pi))^2` is still a smooth coordinate on a free probe family. But the source function itself has the exact ordered singularity shells

`r_m=2pi m`.

Hence

`a=m^2  <=>  c=r_m`.

The square amplitudes therefore have **dual provenance**: they are both source-shell values and downstream saddle-collision values. What is absent is not source realization but a source-intrinsic rule selecting one shell or one `c` from the available family.

AF-434 then separates realization from transport. In the shell-resolved coefficient formula, the singularity-shell label is summed into zeta factors before the determinant partition packets are formed. At every fixed packet depth the shell-sensitive numerator contributes only a subexponential factor on the relevant `n`-th-root scale, whereas the full-column saddle law remains

`L_r(b)=b^r/(r!)^2`.

Thus the numerical coincidence `c=r_m <=> a=m^2` does not transport source shell index `m` into determinant packet index `m`. Aggregate shell information survives through low-order zeta factors, but selected-shell identity is not the mechanism producing the square saddle threshold.

The reusable lesson is therefore three-stage. **First establish selection provenance: does the source choose the asymptotic coordinate, or merely permit it inside a free probe family? Second establish transport provenance: does that selected source coordinate survive into the representation variable consumed by the destination, or is it aggregated away before the critical packet geometry appears? Only then compare the admissible source mesh with the target aperture at the same scale.** The critical displaced branch exhibits a genuinely too-coarse integer depth at second order. The supercritical rational constant-density branch passes its first lattice gate because source motion and target width match. But the next packet-corrected target becomes source-discriminating only if both a source-native selector and a source-to-packet transport mechanism are supplied.

**Boundary.** AF-433 does not prove that no source-intrinsic selector for `c` or the shell index can exist; it proves that none is supplied by the canonical probe family. AF-434 does not prove that no alternative determinant or observable can transport shell identity; it proves that the present full-column saddle does not. AF-432 still classifies the first packet-corrected `R_n/n^2` target for fixed rational supercritical density and gives a necessary condition for first-order complete-packet balance. The current synthesis does not construct a selector, a transport mechanism, decide pointwise membership after both are supplied, control omitted determinant sectors, settle arbitrary varying `q_n`, select rational primes or zeta zeros, or imply RH.
