---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-283-wang-fixed-source-cross-frequency-separation.md
  - research/visual_exploration/findings/VIS-284-wang-fixed-source-packet-projection-bound.md
  - research/visual_exploration/findings/VIS-285-wang-q-zero-source-observable-analytic.md
  - research/visual_exploration/findings/VIS-286-wang-large-source-diagonal-linearizes.md
  - research/visual_exploration/findings/VIS-287-wang-fixed-power-source-escape-linear.md
  - research/visual_exploration/findings/VIS-288-wang-fixed-power-residual-h-frontier.md
  - research/visual_exploration/findings/VIS-289-wang-fixed-power-residual-o-h.md
  - research/visual_exploration/findings/VIS-290-wang-fixed-power-classical-pnt-envelope.md
  - research/visual_exploration/findings/VIS-291-wang-fixed-power-korobov-vinogradov-envelope.md
  - research/visual_exploration/findings/VIS-292-wang-symmetric-smoothing-green-resolvent.md
  - research/visual_exploration/findings/VIS-293-wang-source-dirichlet-rh-half-plane.md
  - research/visual_exploration/findings/VIS-294-wang-lower-moving-source-sqrtlog-crossover.md
  - research/visual_exploration/findings/VIS-295-wang-gamma-subtracted-residual-relative-crossover.md
  - research/visual_exploration/findings/VIS-296-wang-relative-boundary-reduces-to-explicit-formula-remainder-mean.md
  - research/visual_exploration/findings/VIS-297-wang-boundary-remainder-mean-is-gamma-normalization.md
  - research/visual_exploration/findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md
  - research/visual_exploration/findings/VIS-299-wang-pointwise-moving-ceiling-h-over-log-cubed.md
  - research/visual_exploration/findings/VIS-300-wang-localization-cross-coherence.md
  - research/visual_exploration/findings/VIS-301-wang-zero-free-localization-log-squared-window.md
  - research/visual_exploration/findings/VIS-302-wang-weighted-mean-value-log-boundary.md
  - research/visual_exploration/findings/VIS-303-wang-odd-shift-power-two-sparsity.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

`VIS-283`--`VIS-291` isolate Wang's source channel and show that fixed-interior packet localization does not create new information: the complete statistic on compact power panels reduces to the linear source law plus the classical Korobov--Vinogradov arithmetic envelope. `VIS-292` and `VIS-293` then rule out two cheap escapes: the symmetric smoother has no exact blind frequency, while excluding all poles of the squared-von-Mangoldt source transform in `Re(s)>1/2` is already RH-equivalent.

`VIS-294`--`VIS-298` close the apparent moving lower-source boundary. Exact gamma recentering removes the square-root-log `H` barrier and yields

`F_I(x) = (H/(2*pi))[log x + (L-log(2*pi))^2/x^2] + o(H)`

for every moving `x->infinity` below one fixed exponent ceiling.

`VIS-299` removes the fixed exponent gap as a pointwise obstruction. `VIS-300` separates the localization leakage energies from the inside--outside coherence, and `VIS-301` uses the classical zero-free region to show that all localization terms are already `o(H)` through `x=o(H/L^2)`. That exposed Wang's generic Montgomery--Vaughan error weight

`sum_n n a_n^2 << x log^2(2x)`

as the next apparent boundary.

`VIS-302` shows that this `log^2` scale is also a proof-packaging artifact for Wang's exact coefficients. Reusing the same classical asymptotic

`sum_(n<=u) Lambda(n)^2 = u log u-u+O(u exp(-cV(log u)))`

already established in `VIS-291`, direct weighted partial summation gives

`sum_n n a_n^2`
` = (4/3)x log x + (8/9)x`
`   + O(x exp(-cV(log x)))`.

Hence the mean-value error is `O(x log x)`, not merely `O(x log^2 x)`. Re-running the `VIS-301` localization bounds shows that the complete pointwise asymptotic survives throughout

`x log(2x)=o(H)`.

`VIS-303` now removes another whole sector from the boundary problem. Splitting Wang's polynomial into the powers-of-two part `D_2` and the odd-prime-power part `D_o`, the exact support identity for `Lambda` gives

`sum_(2^k) a_(2^k)^2 << 1/x`,

`sum_(2^k) 2^k a_(2^k)^2 << 1`.

The cross term `2 Re integral_I D_2 overline(D_o)` is exactly the full off-diagonal sector with odd additive difference. By Montgomery--Vaughan and Cauchy--Schwarz it is `o(H)` whenever `x log(2x)=O(H)`. Thus at the current boundary the full remainder agrees at `H` resolution with the remainder formed only from **odd prime powers**, whose pairwise additive differences are necessarily even.

The first unresolved moving upper layer therefore remains near `x log x asymp H`, but its live arithmetic channel has narrowed to the odd-prime-power/even-shift off-diagonal sector.

## Research question

Two distinct source routes remain.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`,

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293`, that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, what is the actual off-diagonal Montgomery--Vaughan remainder for Wang's exact coefficients when

`x log x asymp H`,

after restricting to pairs of odd prime powers, equivalently to even additive differences?

Does the exact interval kernel and the frequencies `log(m/n)` yield further oscillatory cancellation across the even-shift sectors, is there a stable deterministic `H`-scale correction, or can an admissible matched coefficient/control model realize the `x log x` scale and show that additional arithmetic information is necessary?

A genuinely bounded source `x=O(1)` remains separate. A moving-support version of Wang's integrated Theorem 2.2 is also separate: the current findings concern the pointwise source statistic and do not establish uniformity for a test function whose support changes with `T`.

## Why it may matter

The source-scale search space has been compressed repeatedly by decomposing the first term that appears to reach output scale instead of interpreting its packaged big-O as a transition. The moving lower boundary, fixed exponent gap, `H/L^3` localization wall, `H/L^2` interior wall, and now the entire opposite-parity off-diagonal sector have collapsed under exact recombination, proof-level uniformity, classical zero-free information, coefficient-specific moment evaluation, or exact arithmetic support.

A further positive result must therefore act on the surviving even-shift odd-prime-power channel, not on a loose coefficient majorant or a power-of-two interaction. A gain beyond `x log x=o(H)` would genuinely enlarge the pointwise source window; a sharp `H`-scale correction or matched lower construction would instead certify that the current proof has finally reached a real arithmetic Dirichlet-polynomial boundary rather than another bookkeeping artifact.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all `D_x`, gamma/zeta, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, work with the exact off-diagonal identity behind

`integral_I |D_x(t)|^2 dt - H sum_n a_n^2`,

using

`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`.

By `VIS-303`, discard the power-of-two and odd-additive-shift sectors at `H` resolution. Analyze the remaining pairs `m,n` of odd prime powers in the range `x log x asymp H`, preserving the exact interval kernel, frequencies `log(m/n)`, coefficient weights, and even additive differences `m-n=2r`. Determine whether the surviving remainder is `o(H)`, has a stable explicit `H`-scale term, or admits a matching admissible lower/control construction.

A decisive outcome is one of: an unconditional coefficient-specific cancellation extending the pointwise asymptotic beyond `x log x=o(H)`; a deterministic `H`-scale correction that can be separated from the main source law; or a matched admissible model showing that the surviving even-shift channel genuinely attains `H` scale and requires additional arithmetic input.

Do not reopen the old `H/L^3` localization, `H/L^2` coefficient-bound, or opposite-parity branches unless a new hypothesis invalidates `VIS-301`, `VIS-302`, or `VIS-303`. Re-estimating already-subcritical leakage, reusing `Lambda(n)<=log n` after the weighted moment has been evaluated, or attributing the boundary to powers of two is no longer a live upper-boundary test.

## Evidence boundary

`VIS-283`--`VIS-300` establish the source reductions, normalization corrections, lower-source closure, pointwise moving-source extension, and exact localization-energy decomposition. `VIS-301` establishes that classical zero-free information makes localization `o(H)` before the interior mean-value term becomes critical. `VIS-302` evaluates the exact coefficient weight in that mean-value theorem and proves that the complete pointwise asymptotic holds whenever `x log(2x)=o(H)`. `VIS-303` proves that, throughout the boundary regime `x log(2x)=O(H)`, the full off-diagonal remainder differs by only `o(H)` from the remainder restricted to odd prime powers.

None of these findings evaluates the surviving even-shift mean-value remainder at `x log x asymp H`, improves the fixed-power Korobov--Vinogradov source envelope, controls a genuinely bounded source by the same formula, or proves a moving-support version of Wang's integrated pair-correlation theorem. In particular, `H/L` remains a **proof boundary**, now localized to the odd-prime-power/even-shift channel rather than to the unrestricted off-diagonal sum.

## Research disposition

Outcome so far: **upper pointwise branch narrowed to the even-shift odd-prime-power off-diagonal problem near `x log x asymp H`**.

The moving lower-source, `H/L^3` localization, `H/L^2` coefficient-majorant, and opposite-parity branches are closed under the current hypotheses. The accepted clue remains live for the surviving even-shift `H/L`-scale question and for the separate fixed-power source-specific arithmetic question; bounded-source and moving-test-function questions still require independently justified targets.