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

Away from square values `b=m^2`, one packet dominates. At `b=m^2`, only the adjacent packets `m-1,m` tie exponentially. AF-422--AF-424 successively expose the rectangle detuning, the first complete-packet inverse-`n` drift, and the derivative-offset coordinate needed to cancel it.

AF-425 now derives the next complete-packet term:

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

for `alpha_n=d_n/n`, with explicit `B_1,B_2`. More importantly, the leading source detuning is exactly

\[
\Omega_{n,m}
=
C_{n,m}(a)+d_n L_{n,m},
\qquad
L_{n,m}=\log(n/m)+m/n\sim\log n.
\]

Thus the remaining formal tuning is sampled by the original integer derivative depth on a lattice whose spacing grows like `log n`.

## Research question

Does the **complete signed** exceptional-`1` sector have a controlled limit throughout the finite critical window and beyond it, once the actual integer source coordinate is enforced? In the only surviving finite-window branch—odd square transitions—can an integer sequence `d_n` realize the shrinking-target condition required for complete-packet cancellation through polynomial orders, or does source quantization force a residual mismatch?

Separately, for genuinely supercritical ratios `s_n/n -> sigma>2`, what moving full-column saddle replaces the finite-`b` classification, and can that complete signed regime be controlled without importing fixed-window asymptotics?

## Why it may matter

For `m>=2`, the tied square packets carry an exponential rate `Lambda_m>1`. Any uncancelled polynomial relative mismatch between them therefore dominates every exponentially smaller neighboring saddle and closes that tuned branch. AF-425 shows that cancellation is no longer just a matter of choosing a continuous asymptotic coefficient: the source offers integer derivative depth with detuning spacing asymptotic to `log n`.

If the integer shrinking target cannot be hit infinitely often at the required precision, the remaining finite-window escape route closes before any beyond-all-orders packet analysis is needed. If it can be hit arbitrarily deeply, then the first exponentially small residual/tall-column contribution becomes the genuinely decisive scale.

## Decisive test

Fix `m>=1`, `a>0`, odd `n`, and require `b_n=a n^{d_n/n}->m^2` with integer `d_n`. Using AF-425's explicit functions, study

\[
H_n(d)
=
\Omega_{n,m}(d)
+\frac{B_1(d/n)}{n}
+\frac{B_2(d/n)}{n^2}.
\]

Determine whether there exists an integer sequence `d_n` on infinitely many odd `n` with

\[
H_n(d_n)=o(n^{-2}).
\]

Equivalently, reduce the nearest admissible source to an explicit inhomogeneous Diophantine/shrinking-target condition and either prove a polynomial lower bound for the miss or exhibit a mechanism producing infinitely many sufficiently accurate hits. Do not infer impossibility merely from the `~log n` lattice spacing; the moving target must be analyzed.

If a polynomial miss is forced, then for `m>=2` the finite square branch is closed. If the source can realize arbitrarily deep polynomial cancellation, derive the first beyond-all-orders complete-packet residual—including the tall-column sector suppressed in AF-423--AF-425—and compare it with the first subleading full-column saddle.

For `m=1`, keep the same source-realizability test but do not import the `Lambda_m>1` divergence conclusion because `Lambda_1=1`.

For the separate `sigma>2` branch, derive the growing saddle scale directly rather than extrapolating the finite-window packet hierarchy.

## Evidence boundary

The clue does not assert that the shrinking target is missed or hit infinitely often. AF-425 proves the second-order packet law and the source lattice, not a Diophantine distribution theorem for its moving centers. It also does not control the genuinely supercritical moving-saddle regime, the omitted-`1` sector, or one-/zero-singular-block contributions for growing derivative depth.

## Research disposition

Accepted. AF-419 closes the strictly subcritical regime; AF-420 handles the finite-`tau` absolute subthreshold phase; AF-421--AF-425 reduce the signed finite-window obstruction to a discrete square collision whose next gate is now **integer source realizability**, not another unconstrained formal coefficient. The live finite-window test is whether the AF-425 shrinking target can be met along infinitely many odd indices. Only after that gate survives should the investigation pay the cost of beyond-all-orders packet asymptotics. The genuinely supercritical `sigma>2` moving-saddle problem remains independent and unresolved.