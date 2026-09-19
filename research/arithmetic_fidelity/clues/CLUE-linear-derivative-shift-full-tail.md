---
id: CLUE-linear-derivative-shift-full-tail
type: research-clue
status: accepted
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md
  - research/arithmetic_fidelity/findings/AF-418-full-height-rectangles-expose-sigma-2-absolute-tail-transition.md
  - research/arithmetic_fidelity/findings/AF-419-subcritical-linear-shifts-admit-uniform-full-tail-resummation.md
  - research/arithmetic_fidelity/findings/AF-420-critical-derivative-window-has-sharp-subthreshold-absolute-resummation-domain.md
  - research/arithmetic_fidelity/findings/AF-421-finite-critical-windows-reduce-to-full-column-saddle-hierarchy.md
  - research/arithmetic_fidelity/findings/AF-422-square-transition-detuning-controls-adjacent-packet-cancellation.md
  - research/arithmetic_fidelity/findings/AF-423-adjacent-residual-packets-have-universal-inverse-n-drift.md
  - research/arithmetic_fidelity/findings/AF-424-complete-square-packet-cancellation-has-explicit-derivative-offset-detuning.md
  - research/arithmetic_fidelity/findings/AF-425-second-order-square-packet-detuning-exposes-source-lattice.md
  - research/arithmetic_fidelity/findings/AF-426-exact-square-amplitude-has-irreducible-integer-source-packet-gap.md
  - research/arithmetic_fidelity/findings/AF-427-displaced-square-packet-cancellation-is-metrically-exceptional.md
  - research/arithmetic_fidelity/findings/AF-428-second-order-exceptional-amplitudes-are-residual-but-null.md
  - research/arithmetic_fidelity/findings/AF-429-supercritical-full-column-saddle-has-shrinking-integer-window.md
  - research/arithmetic_fidelity/findings/AF-430-supercritical-residual-packets-preserve-shrinking-saddle-window.md
  - research/arithmetic_fidelity/findings/AF-431-constant-rational-supercritical-sources-hit-first-saddle-window.md
---

# Linear derivative-shift full-tail resummation

## Observation

AF-417 identifies the fixed-degree candidate when `s_n/n -> sigma`: every fixed excess degree in the exceptional-`1` Cauchy--Binet sector is renormalized by `e^{sigma d}`, suggesting

\[
\exp\!\left(-\frac{e^\sigma c^2}{4\pi^2}\right).
\]

AF-418--AF-420 show that complete resummation is controlled by large partitions rather than fixed-degree data alone. Strictly subcritical ratios are under uniform control, while the critical window is governed by

\[
a=\frac{c^2}{4\pi^2},
\qquad
b_n=a n^{s_n/n-2}.
\]

AF-421 reduces every finite critical window `b_n -> b in (0,infinity)` to full-column packets with exponential rates

\[
L_r(b)=\frac{b^r}{(r!)^2}.
\]

Away from square values `b=m^2`, one packet dominates. At `b=m^2`, only the adjacent packets `m-1,m` tie exponentially. AF-422--AF-424 expose the rectangle detuning, the first complete-packet inverse-`n` drift, and the derivative-offset coordinate needed to cancel it.

AF-425 pushes the complete-packet ratio to second order. Writing `s_n=2n+d_n` and `alpha_n=d_n/n`, it gives

\[
\log Q_{n,m}
=
\Omega_{n,m}
+
\frac{B_1(\alpha_n)}{n}
+
\frac{B_2(\alpha_n)}{n^2}
+o(n^{-2}),
\]

with exact integer-source detuning

\[
\Omega_{n,m}
=
C_{n,m}(a)+d_n L_{n,m},
\qquad
L_{n,m}=\log(n/m)+m/n\sim\log n.
\]

AF-426 closes the exact-amplitude subfiber `a=m^2`: bounded packet balance forces `d_n=-1` eventually, and at that only admissible depth `Q_{n,m}->mK_m>1`.

AF-427 treats displaced amplitudes metrically. With `A=log(m^2/a)`, the source-compatible depths at scale `n` number only `O(n/log n)`, while the second-order target `|H_n(d)|<=n^-2` pulls back to amplitude intervals of width `O(n^-3)`. Hence the amplitudes admitting infinitely many second-order hits form a Lebesgue-null set of Hausdorff dimension at most `2/3`.

AF-428 supplies the complementary category statement: the very same exceptional set is a dense `G_delta`, hence residual. Exact second-order roots become dense because at each large odd scale the affine source grid can be centered within `O(log n)` of the target, while `partial_A H=-n+O(n^-1)` moves the resulting root only `O(log n/n)` in amplitude. The surviving set is therefore simultaneously metrically thin and topologically generic.

AF-429 resolves the first scale question in the independent supercritical branch. If `q_n=s_n/n->sigma>2`, the full-height rectangular family has moving width

\[
R_n=a^{1/q_n}n^{1-2/q_n},
\]

with normalized profile `sigma t(1-log t)` at `r~tR_n`. The exact adjacent ratio has a real crossing `tau_n~R_n`, but integer adjacent rectangles are comparable only when

\[
\operatorname{dist}(\tau_n,\mathbb Z)=O(R_n/n).
\]

AF-430 controls the **complete residual partition packets** attached to the two adjacent rectangles whenever that window is reached. Both packets tend to `exp(-a e^sigma)`, and

\[
\log\frac{G_{n,r}}{G_{n,r-1}}
=
\frac{\sigma a e^\sigma}{n}+o(n^{-1}).
\]

Thus the nonrectangular packet does not wash out AF-429's lattice window. It shifts the first refined real balance point only by

\[
a e^\sigma R_n/n^2\,(1+o(1)),
\]

a factor `1/n` smaller than the `R_n/n` integer-comparability window.

AF-431 now shows that this first supercritical lattice gate is **not universally obstructive**. For every fixed rational density `q=u/v>2`, the exact source progression `n=vk, s=uk` has a continuously interpolated saddle satisfying

\[
\tau'(n)=\frac{q-2}{q}\frac{R(n)}n(1+o(1)).
\]

The sampled saddle is increasing, divergent, and moves by only `Theta(R_n/n)` per admissible source step, so a deterministic integer-crossing argument forces infinitely many `O(R_n/n)` hits for every `a>0`. If `v` is odd, the same holds on the odd progression `n=v(2k+1)`, where adjacent packet signs alternate. This positive control does not reach the finer `R_n/n^2` packet center.

## Research question

Which **concrete distinguished amplitudes** supplied by the source construction belong to, or are excluded from, the residual-null critical exceptional set? What exact arithmetic mechanism decides membership in

\[
H_n(d_n)=o(n^{-2}),
\qquad
\frac{d_n\log n}{n}\to\log(m^2/a),
\]

along infinitely many odd source-compatible depths?

Separately, in the genuinely supercritical regime, AF-431 closes first-window realizability positively for the constant rational source class. For an actual distinguished source sequence outside that class, the live first question is whether its allowed saddle samples inherit the same monotone mesh condition `Delta tau_n=O(R_n/n)`—which would make first-window hits automatic—or whether source-induced jumps/oscillations create a genuine obstruction. On rational constant-density sources that already pass this gate, the live target moves immediately to AF-430's packet-corrected `R_n/n^2` scale and to the omitted determinant sectors.

## Why it may matter

For `m>=2`, the tied square packets carry an exponential rate `Lambda_m>1`, so any uncancelled polynomial relative mismatch dominates every exponentially smaller neighboring saddle. AF-426 excludes the exact square-amplitude fiber pointwise, AF-427 says almost every displaced amplitude is nonexceptional, and AF-428 shows exceptional amplitudes nevertheless occur in every neighborhood.

Consequently, neither metric scarcity nor perturbative/local stability can close the remaining critical branch for a source-forced constant. The deciding input must distinguish that exact amplitude from arbitrarily close exceptional ones. In the supercritical branch, AF-429--AF-431 now separate three scales: packet geometry preserves the `R_n/n` window; ordinary constant-rational source sampling can hit that window automatically; but the packet correction lives at `R_n/n^2`, a factor `n` below the source-step scale. That finer mismatch, rather than first-window existence by itself, is the next candidate arithmetic obstruction on the positive control class.

## Decisive test

Fix `m>=1` and an actual positive amplitude `a!=m^2` supplied by, or naturally singled out in, the source construction. Put

\[
A=\log(m^2/a),
\qquad
b_n=a n^{d_n/n},
\]

and use AF-425's exact cancellation function

\[
H_n(d)
=
\Omega_{n,m}(d)
+\frac{B_1(d/n)}{n}
+\frac{B_2(d/n)}{n^2}.
\]

Prove a pointwise membership theorem for this exact `A`: either a lower bound excluding `H_n(d_n)=o(n^-2)` for every source-compatible integer sequence, or an explicit arithmetic mechanism producing infinitely many hits at that precision. A generic measure theorem, Baire-category theorem, or neighborhood-stability argument is no longer decisive: AF-427 and AF-428 show that those notions of genericity point in opposite directions.

If a specific distinguished amplitude is proved exceptional, only then derive the first beyond-all-orders complete-packet residual—including the tall-column sector suppressed in AF-423--AF-425—and compare it with the first subleading full-column saddle. For `m=1`, keep the same source-realizability test but do not import the `Lambda_m>1` divergence conclusion.

For the independent `sigma>2` branch, do **not** try to prove a universal no-hit theorem at the `O(R_n/n)` scale: AF-431 supplies exact rational-density controls that hit it infinitely often. Instead classify the actual allowed source mesh. If its saddle is eventually increasing/divergent and consecutive admissible samples differ by `O(R_n/n)`, first-window membership follows by the same crossing argument. If that criterion fails, identify the exact source mechanism producing larger jumps or persistent avoidance. On a source class that passes, refine directly to AF-430's corrected center at `R_n/n^2`; because admissible constant-rational saddle steps are `Theta(R_n/n)`, this finer target is not supplied by AF-431 and requires a genuinely sharper arithmetic mechanism. Only then compare the omitted-`1` and singular-block determinant sectors.

## Evidence boundary

AF-428 proves that AF-427's critical exceptional set is residual and dense; it does **not** identify a single distinguished source amplitude in that set. Residuality gives no membership statement for a fixed arithmetic constant, no Hausdorff-dimension lower bound, and no control of the undisplayed determinant remainder.

AF-430 proves that, conditional on reaching AF-429's `R_n/n` candidate window, the complete residual partition packets inside the exceptional-`1` sector share the limit `exp(-a e^sigma)` and differ adjacently only by the explicit inverse-`n` drift `sigma a e^sigma/n`.

AF-431 proves infinitely many first-window hits for exact constant rational derivative density, and on an odd sign-alternating progression when the reduced denominator is odd. It does **not** prove first-window membership for an arbitrary prescribed `q_n->sigma`, `o(R_n/n)` alignment, the packet-corrected `R_n/n^2` hit, sufficient cancellation of the two exponentially large leading packets, or negligibility of the omitted determinant sectors. No rational-prime discriminator has been recovered.

## Research disposition

Accepted. AF-419--AF-425 reduce the finite critical window to integer source realizability; AF-426 closes the exact square-amplitude fiber; AF-427 makes displaced second-order cancellation metrically exceptional; AF-428 proves the same exceptional set is residual and dense. The live critical gate is therefore **arithmetic membership of exact distinguished amplitudes**, not whether the exceptional set exists or is generic in either measure or category. Beyond-all-orders critical packet analysis should wait until one such source-forced amplitude is proved to survive.

For `sigma>2`, AF-429 locates the moving rectangle saddle, AF-430 proves that the complete residual packet preserves its first `R_n/n` window, and AF-431 shows that exact rational constant-density source lattices can hit that window automatically. The supercritical owner question therefore no longer treats first-window membership as an intrinsic obstruction. It is now a **source-mesh classification problem**, followed—on source classes that pass—by the factor-`n` finer `R_n/n^2` alignment and control of omitted determinant sectors.