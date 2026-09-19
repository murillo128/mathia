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

AF-427 now treats the displaced amplitudes metrically. Reparameterizing by `A=log(m^2/a)`, the source-compatible depths at scale `n` number only `O(n/log n)`, while the second-order target `|H_n(d)|<=n^-2` pulls back to amplitude intervals of width `O(n^-3)`. Hence the amplitudes admitting infinitely many second-order hits form a Lebesgue-null set of Hausdorff dimension at most `2/3`.

Thus the finite-window question is no longer whether generic displaced source depths can track the continuous saddle. They cannot at the required precision. The surviving question is whether the **specific exceptional set** contains any distinguished amplitudes supplied by the original source problem.

## Research question

On the surviving odd square-transition branch, can any mathematically distinguished amplitude `a!=m^2` lie in AF-427's exceptional set and realize

\[
H_n(d_n)=o(n^{-2})
\]

along infinitely many source-compatible integer depths? If so, what arithmetic mechanism produces those hits? If not, can the pointwise obstruction be proved for the amplitudes actually forced by the source construction without relying on an almost-everywhere statement?

Separately, for genuinely supercritical ratios `s_n/n -> sigma>2`, what moving full-column saddle replaces the finite-`b` classification, and can that complete signed regime be controlled without importing fixed-window asymptotics?

## Why it may matter

For `m>=2`, the tied square packets carry an exponential rate `Lambda_m>1`. Any uncancelled polynomial relative mismatch dominates every exponentially smaller neighboring saddle. AF-426 eliminates the exact-amplitude fiber pointwise, and AF-427 eliminates almost every displaced amplitude metrically, so spending effort on beyond-all-orders packet asymptotics is justified only after one concrete exceptional amplitude survives the source-realizability gate.

The remaining issue is therefore qualitatively sharper. A metric theorem cannot exclude a distinguished arithmetic constant merely because the exceptional set has measure zero. The next useful result must use the exact moving centers or arithmetic nature of the physical amplitude, rather than another generic spacing or equidistribution heuristic.

## Decisive test

Fix `m>=1` and a concrete positive amplitude `a!=m^2` supplied by, or naturally singled out in, the source construction. Put

\[
A=\log(m^2/a),
\qquad
b_n=a n^{d_n/n},
\]

and require `b_n->m^2` along odd `n` with integer `d_n`. Using AF-425's exact functions, reduce the nearest admissible depth to the explicit moving-center condition for

\[
H_n(d)
=
\Omega_{n,m}(d)
+\frac{B_1(d/n)}{n}
+\frac{B_2(d/n)}{n^2}.
\]

Prove one of two pointwise outcomes: either a lower bound preventing `H_n(d_n)=o(n^-2)` for every source-compatible sequence, or an explicit mechanism yielding infinitely many hits at that precision. A merely metric or generic theorem is no longer enough; AF-427 already supplies that layer.

If a specific exceptional amplitude survives, only then derive the first beyond-all-orders complete-packet residual—including the tall-column sector suppressed in AF-423--AF-425—and compare it with the first subleading full-column saddle. For `m=1`, retain the same source-realizability test but do not import the `Lambda_m>1` divergence conclusion.

For the independent `sigma>2` branch, derive the growing saddle scale directly rather than extrapolating the finite-window packet hierarchy.

## Evidence boundary

AF-427 proves only that the second-order-hit amplitudes have Lebesgue measure zero and Hausdorff dimension at most `2/3`. It does not prove that this exceptional set is empty, identify its elements, or exclude any distinguished fixed amplitude. AF-426 remains the only pointwise closure of an entire amplitude fiber, namely `a=m^2`.

The genuinely supercritical moving-saddle regime, omitted-`1` sector, one-/zero-singular-block contributions for growing derivative depth, and beyond-all-orders packet residuals at a surviving exceptional amplitude remain uncontrolled.

## Research disposition

Accepted. AF-419 closes the strictly subcritical regime; AF-420 handles the finite-`tau` absolute subthreshold phase; AF-421--AF-425 reduce the signed finite-window obstruction to integer source realizability. AF-426 closes the exact-amplitude fiber pointwise, and AF-427 shows that the displaced second-order cancellation set is metrically exceptional. The live finite-window gate is now **pointwise exceptional-set arithmetic for distinguished amplitudes**, not generic source-lattice spacing. Beyond-all-orders packet analysis should wait until such an amplitude is actually shown to survive. The genuinely supercritical `sigma>2` moving-saddle problem remains independent and unresolved.