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
  - research/arithmetic_fidelity/findings/AF-432-supercritical-packet-center-amplitudes-are-residual-but-metrically-thin.md
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

AF-431 shows that this first supercritical lattice gate is **not universally obstructive**. For every fixed rational density `q=u/v>2`, the exact source progression `n=vk, s=uk` has a continuously interpolated saddle satisfying

\[
\tau'(n)=\frac{q-2}{q}\frac{R(n)}n(1+o(1)).
\]

The sampled saddle is increasing, divergent, and moves by only `Theta(R_n/n)` per admissible source step, so a deterministic integer-crossing argument forces infinitely many `O(R_n/n)` hits for every `a>0`. If `v` is odd, the same holds on the odd progression `n=v(2k+1)`, where adjacent packet signs alternate.

AF-432 resolves the first finer amplitude-genericity question. For fixed rational `q`, write the AF-430 leading corrected center as

\[
\widehat\tau_n(a)
=
\tau_n(a)+a e^q R_n(a)/n^2.
\]

Its amplitude derivative is `Theta(R_n)=Theta(n^(1-2/q))` on compact positive amplitude intervals. Each `R_n/n^2` integer target therefore pulls back to only `O(n^-2)` amplitude width, while only `O(R_n)` integer targets occur at scale `n`. The amplitudes with infinitely many `o(R_n/n^2)` hits form a Lebesgue-null set of Hausdorff dimension at most `1-1/q`, yet exact corrected-center roots are dense at every large source scale, so the same exceptional set is a dense `G_delta`. Actual `log Q=o(n^-1)` packet balance is contained in this residual-null set.

## Research question

Which **concrete distinguished amplitudes** supplied by the source construction belong to, or are excluded from, the residual-null critical exceptional set? What exact arithmetic mechanism decides membership in

\[
H_n(d_n)=o(n^{-2}),
\qquad
\frac{d_n\log n}{n}\to\log(m^2/a),
\]

along infinitely many odd source-compatible depths?

Separately, in the genuinely supercritical regime, AF-431 closes first-window realizability positively for the constant rational source class and AF-432 classifies the first packet-corrected `R_n/n^2` target over amplitudes. For an actual distinguished source sequence outside the constant-rational class, first classify its allowed saddle mesh as in AF-431. For an exact rational constant-density source, the live question is now **pointwise membership of the distinguished amplitude in AF-432's residual-null fine-hit set**, followed, on a surviving amplitude, by the next uniform packet correction and the omitted determinant sectors.

## Why it may matter

For `m>=2`, the tied square packets carry an exponential rate `Lambda_m>1`, so any uncancelled polynomial relative mismatch dominates every exponentially smaller neighboring saddle. AF-426 excludes the exact square-amplitude fiber pointwise, AF-427 says almost every displaced amplitude is nonexceptional, and AF-428 shows exceptional amplitudes nevertheless occur in every neighborhood.

Consequently, neither metric scarcity nor perturbative/local stability can close the remaining critical branch for a source-forced constant. The deciding input must distinguish that exact amplitude from arbitrarily close exceptional ones.

The supercritical branch now exhibits the same lesson at a different scale. AF-429--AF-431 make the first `R_n/n` window automatic on rational constant-density sources; AF-432 then makes the factor-`n` finer `R_n/n^2` target metrically exceptional but topologically generic in amplitude. Thus the source-step mismatch is a genuine metric obstruction but still not a pointwise arithmetic obstruction. A concrete source constant cannot be decided by either “almost every amplitude fails” or “a residual set succeeds.”

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

If a specific distinguished critical amplitude is proved exceptional, only then derive the first beyond-all-orders complete-packet residual—including the tall-column sector suppressed in AF-423--AF-425—and compare it with the first subleading full-column saddle. For `m=1`, keep the same source-realizability test but do not import the `Lambda_m>1` divergence conclusion.

For the independent constant-rational `q=u/v>2` branch, use AF-432's exact fine target

\[
\operatorname{dist}\!\left(
\tau_n(a)+a e^q R_n(a)/n^2,\mathbb Z
\right)
=
o(R_n(a)/n^2).
\]

For the actual distinguished amplitude, prove a **pointwise** lower bound excluding this along every admissible source subsequence, or exhibit a source/arithmetic mechanism producing infinitely many such hits. Do not use measure-zero or residuality as a proxy for membership. If the amplitude survives, derive the next uniform term in the complete packet ratio and compare the omitted-`1` and singular-block determinant sectors. For varying `q_n`, first prove the source-mesh hypotheses needed to reduce to an analogous fine target rather than importing the constant-density theorem.

## Evidence boundary

AF-428 proves that AF-427's critical exceptional set is residual and dense; it does **not** identify a single distinguished source amplitude in that set. Residuality gives no membership statement for a fixed arithmetic constant, no Hausdorff-dimension lower bound, and no control of the undisplayed determinant remainder.

AF-430 proves that, conditional on reaching AF-429's `R_n/n` candidate window, the complete residual partition packets inside the exceptional-`1` sector share the limit `exp(-a e^sigma)` and differ adjacently only by the explicit inverse-`n` drift `sigma a e^sigma/n`.

AF-431 proves infinitely many first-window hits for exact constant rational derivative density, and on an odd sign-alternating progression when the reduced denominator is odd. It does not prove the packet-corrected hit or sufficient cancellation.

AF-432 proves that the **first displayed corrected center** has a residual but Lebesgue-null fine-hit set, with Hausdorff dimension at most `1-1/q`, and that actual `log Q=o(n^-1)` balance can occur only inside that set. It does **not** identify any fixed distinguished amplitude in the set, prove that corrected-center membership is sufficient for packet cancellation, control the next packet term, or bound the omitted determinant sectors. No rational-prime discriminator has been recovered.

## Research disposition

Accepted. AF-419--AF-425 reduce the finite critical window to integer source realizability; AF-426 closes the exact square-amplitude fiber; AF-427 makes displaced second-order cancellation metrically exceptional; AF-428 proves the same exceptional set is residual and dense. The live critical gate is therefore **arithmetic membership of exact distinguished amplitudes**, not whether the exceptional set exists or is generic in either measure or category. Beyond-all-orders critical packet analysis should wait until one such source-forced amplitude is proved to survive.

For `sigma>2`, AF-429 locates the moving rectangle saddle, AF-430 identifies its first complete-packet correction, AF-431 shows that exact rational constant-density sources hit the first `R_n/n` window automatically, and AF-432 classifies the finer `R_n/n^2` corrected-center target as residual but metrically thin in amplitude. On constant rational sources the owner question has therefore narrowed again: **decide the exact distinguished amplitude pointwise**, then—only on a survivor—compute the next packet scale and control the omitted determinant sectors. For nonconstant source densities, source-mesh classification remains prerequisite.
