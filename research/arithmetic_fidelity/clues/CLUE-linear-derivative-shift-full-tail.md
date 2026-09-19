---
id: CLUE-linear-derivative-shift-full-tail
type: research-clue
status: accepted
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md
  - research/arithmetic_fidelity/findings/AF-421-finite-critical-windows-reduce-to-full-column-saddle-hierarchy.md
  - research/arithmetic_fidelity/findings/AF-425-second-order-square-packet-detuning-exposes-source-lattice.md
  - research/arithmetic_fidelity/findings/AF-426-exact-square-amplitude-has-irreducible-integer-source-packet-gap.md
  - research/arithmetic_fidelity/findings/AF-427-displaced-square-packet-cancellation-is-metrically-exceptional.md
  - research/arithmetic_fidelity/findings/AF-428-second-order-exceptional-amplitudes-are-residual-but-null.md
  - research/arithmetic_fidelity/findings/AF-429-supercritical-full-column-saddle-has-shrinking-integer-window.md
  - research/arithmetic_fidelity/findings/AF-430-supercritical-residual-packets-preserve-shrinking-saddle-window.md
  - research/arithmetic_fidelity/findings/AF-431-constant-rational-supercritical-sources-hit-first-saddle-window.md
  - research/arithmetic_fidelity/findings/AF-432-supercritical-packet-center-amplitudes-are-residual-but-metrically-thin.md
  - research/arithmetic_fidelity/findings/AF-433-free-left-tail-amplitude-is-not-a-source-discriminator.md
---

# Linear derivative-shift full-tail resummation

## Observation

AF-417--AF-432 reduce the left-tail derivative-shift hierarchy to increasingly fine integer-source and packet-balance conditions. In the critical regime the decisive coordinate is

\[
a=\frac{c^2}{4\pi^2},
\qquad
b_n=a n^{s_n/n-2},
\]

with square transitions `b=m^2`. AF-426 excludes exact square amplitude at the second packet scale. AF-427--AF-428 show that displaced critical amplitudes with infinitely many second-order hits form a set that is simultaneously residual and Lebesgue-null.

For exact rational supercritical density `q=u/v>2`, AF-429--AF-431 show that the first `R_n/n` saddle window is reached infinitely often for every positive amplitude, and AF-432 refines the packet-corrected target to

\[
\operatorname{dist}\!\left(
\tau_n(a)+a e^q R_n(a)/n^2,\mathbb Z
\right)
=o(R_n(a)/n^2).
\]

The amplitudes satisfying this infinitely often are again residual but metrically thin: Lebesgue-null with Hausdorff dimension at most `1-1/q`.

AF-433 changes the provenance gate. In AF-416--AF-432 the diagonal constant `c>0` remains externally free, and `a=c^2/(4\pi^2)` is a diffeomorphic reparameterization of that whole family. Therefore the existing exceptional sets classify tuned diagonal/probe paths through the fixed source. They do not yet classify a source-forced arithmetic constant.

## Research question

Can the underlying arithmetic/source construction canonically select a positive diagonal constant `c`—equivalently an amplitude `a`—**before** any square-saddle or shrinking-target condition is inspected?

If such a selector exists, what source invariant or normalization forces it, and is it stable under the symmetries/gauges that the line treats as non-discriminating? Only after this source-provenance question is answered does pointwise membership in the AF-428 or AF-432 exceptional set become a genuine arithmetic-fidelity question.

## Why it may matter

The metric/category work is now strong enough that genericity cannot decide a fixed amplitude: the same exceptional sets can be topologically large and measure-theoretically thin. AF-433 adds a more basic obstruction: the current chain has not produced a fixed amplitude at all.

Without an independent selector, one can choose `c=2\pi\sqrt a` for any desired `a>0`. Chasing a special amplitude because it hits a target would therefore tune the observation path to the downstream phenomenon instead of showing that the source preserved a discriminator through compression. That is exactly the provenance failure this research line is intended to detect.

## Decisive test

**Gate 0 — source selection.** Starting from the intrinsic source data, derive a canonical rule

\[
S(\text{source})=c_*>0
\qquad\text{or equivalently}\qquad
a_*=\frac{c_*^2}{4\pi^2},
\]

without using the desired packet cancellation, square collision, or exceptional-set membership as part of the definition. Audit the rule against the relevant source symmetries, normalizations, and matched controls. A merely convenient choice such as `c=2\pi m` does not pass this gate unless it is independently forced by source structure.

**Gate 1 — pointwise target membership.** Only after Gate 0 passes, test the resulting fixed `a_*` against the exact critical or supercritical target. In the critical branch use AF-425's cancellation function and prove either a pointwise lower bound excluding `H_n(d_n)=o(n^-2)` or a mechanism producing infinitely many source-compatible hits. In the rational supercritical branch test

\[
\operatorname{dist}\!\left(
\tau_n(a_*)+a_* e^q R_n(a_*)/n^2,\mathbb Z
\right)
=o(R_n(a_*)/n^2)
\]

along admissible source indices.

**Gate 2 — next packet scale.** Only on a pointwise survivor derive the next uniform complete-packet correction and compare omitted-`1`, singular-block, or other determinant sectors. Do not spend beyond-all-orders effort before Gates 0 and 1 survive.

## Evidence boundary

AF-426 proves a genuine negative statement at exact square amplitude, but square amplitudes are selected by downstream saddle equality, not by an intrinsic source rule. AF-427--AF-428 classify the critical displaced exceptional set; AF-432 classifies the first supercritical packet-corrected exceptional set. None identifies a source-forced amplitude.

AF-433 proves only the provenance obstruction for the current chain: `c` remains free and `a=c^2/(4\pi^2)` is onto `(0,\infty)`. It does not prove that no future source theorem can select `c`, nor does it weaken the analytic content of the packet results.

A new cross-line arithmetic construction may legitimately supply a selector. If it does, its source provenance must be established independently before this clue treats the resulting amplitude as distinguished.

## Research disposition

Accepted. The live owner question is now **source-amplitude selection before Diophantine membership**. Do not continue pointwise exceptional-set analysis for an arbitrarily chosen amplitude. First derive or rule out a canonical source-side selector; then apply AF-428/AF-432 to the selected value. If no such selector is available inside the current construction, the packet hierarchy remains mathematically interesting but ceases to be a discriminator for the underlying source.