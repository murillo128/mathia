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

`VIS-302` now shows that this `log^2` scale is also a proof-packaging artifact for Wang's exact coefficients. Reusing the same classical asymptotic

`sum_(n<=u) Lambda(n)^2 = u log u-u+O(u exp(-cV(log u)))`

already established in `VIS-291`, direct weighted partial summation gives

`sum_n n a_n^2`
` = (4/3)x log x + (8/9)x`
`   + O(x exp(-cV(log x)))`.

Hence the mean-value error is `O(x log x)`, not merely `O(x log^2 x)`. Re-running the `VIS-301` localization bounds shows that the complete pointwise asymptotic in fact survives throughout

`x log(2x)=o(H)`.

The first unresolved moving upper layer is therefore near `x log x asymp H`, equivalently `x asymp H/L` in the polynomial source regime.

## Research question

Two distinct source routes remain.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`,

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293`, that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, what is the actual off-diagonal Montgomery--Vaughan remainder for Wang's exact coefficients when

`x log x asymp H`?

Does the interval integral of `D_x` contain coefficient-specific oscillatory cancellation that pushes the asymptotic beyond this scale, is there a stable deterministic `H`-scale correction, or can an admissible matched coefficient/control model realize the `x log x` scale and show that additional arithmetic information is necessary?

A genuinely bounded source `x=O(1)` remains separate. A moving-support version of Wang's integrated Theorem 2.2 is also separate: the current findings concern the pointwise source statistic and do not establish uniformity for a test function whose support changes with `T`.

## Why it may matter

The source-scale search space has been compressed repeatedly by decomposing the first term that appears to reach output scale instead of interpreting its packaged big-O as a transition. The moving lower boundary, fixed exponent gap, `H/L^3` localization wall, and now the `H/L^2` interior wall have all collapsed under exact recombination, proof-level uniformity, classical zero-free information, or coefficient-specific moment evaluation.

A further positive result must therefore act on the actual off-diagonal time integral, not on a loose coefficient majorant. A gain beyond `x log x=o(H)` would genuinely enlarge the pointwise source window; a sharp `H`-scale correction or matched lower construction would instead certify that the current proof has finally reached a real Dirichlet-polynomial boundary rather than another bookkeeping artifact.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all `D_x`, gamma/zeta, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, work with the exact off-diagonal identity behind

`integral_I |D_x(t)|^2 dt - H sum_n a_n^2`,

using

`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`.

Analyze the range `x log x asymp H`. Preserve the actual frequencies `log(n/m)`, coefficient signs/weights, and interval kernel rather than replacing them immediately by the generic Montgomery--Vaughan absolute bound. Determine whether the remainder is `o(H)`, has a stable explicit `H`-scale term, or admits a matching admissible lower/control construction.

A decisive outcome is one of: an unconditional coefficient-specific cancellation extending the pointwise asymptotic beyond `x log x=o(H)`; a deterministic `H`-scale correction that can be separated from the main source law; or a matched admissible model showing that the `x log x` scale is genuinely attainable and additional arithmetic input is necessary.

Do not reopen the old `H/L^3` localization or `H/L^2` coefficient-bound branches unless a new hypothesis invalidates `VIS-301` or `VIS-302`. Re-estimating already-subcritical leakage, or reusing `Lambda(n)<=log n` after the weighted moment has been evaluated, is no longer a live upper-boundary test.

## Evidence boundary

`VIS-283`--`VIS-300` establish the source reductions, normalization corrections, lower-source closure, pointwise moving-source extension, and exact localization-energy decomposition. `VIS-301` establishes that classical zero-free information makes localization `o(H)` before the interior mean-value term becomes critical. `VIS-302` then evaluates the exact coefficient weight in that mean-value theorem and proves that the complete pointwise asymptotic holds whenever `x log(2x)=o(H)`.

None of these findings evaluates the actual off-diagonal mean-value remainder at `x log x asymp H`, improves the fixed-power Korobov--Vinogradov source envelope, controls a genuinely bounded source by the same formula, or proves a moving-support version of Wang's integrated pair-correlation theorem. In particular, `H/L` is currently a **proof boundary exposed by the remaining off-diagonal Dirichlet-polynomial estimate**, not an established transition of `F_I`.

## Research disposition

Outcome so far: **upper pointwise branch narrowed to the true off-diagonal mean-value problem near `x log x asymp H`**.

The moving lower-source, `H/L^3` localization, and `H/L^2` coefficient-majorant branches are closed under the current hypotheses. The accepted clue remains live for the off-diagonal `H/L`-scale question and for the separate fixed-power source-specific arithmetic question; bounded-source and moving-test-function questions still require independently justified targets.