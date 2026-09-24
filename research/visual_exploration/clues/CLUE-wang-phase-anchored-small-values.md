---
id: CLUE-visual-wang-phase-anchored-small-values
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-416-wang-bandwidth-normalized-balance-radius.md
  - research/visual_exploration/findings/VIS-417-beat-scale-defeats-coarse-amplitude-controls.md
  - research/visual_exploration/findings/VIS-418-time-translation-defeats-fixed-height-small-value-controls.md
  - research/visual_exploration/findings/VIS-419-wang-shell-translation-orbit-prime-torus-haar.md
  - research/visual_exploration/findings/VIS-420-finite-window-haar-small-divisor-cost.md
  - research/visual_exploration/findings/VIS-421-wang-generic-start-no-distinguished-height-selector.md
  - research/visual_exploration/findings/VIS-422-gram-points-prime-torus-haar-null.md
---

# Does an independently justified arithmetic height selector align with Wang quiet regions beyond each shell's own translation orbit?

## Observation

`VIS-416` isolates the bandwidth-normalized amplitude `a_i(T)=|F_i(T)|/||F_i||_infinity` as the candidate small-value factor after removing the generic reciprocal-bandwidth scale. `VIS-417` shows that long finite-window suppression can still be manufactured by an unresolved beat scale even when mode count, coefficient magnitudes, long-time energy, bandlimit, and global sup norm are fixed.

`VIS-418` strengthens that control. Even after the complete two-mode frequency set and its beat gap are fixed, global translation can move an arbitrarily long quiet interval onto or away from any prescribed observation height while preserving the full frequency geometry, coefficient magnitudes, long-time energy, and sup norm. Fixed-height localization therefore contains a phase/time-origin alignment component that ordinary spectral matching does not remove.

`VIS-419` closes the fixed-shell asymptotic calibration question: each canonical finite Wang shell is a finite character polynomial on its base-prime torus, and long translation of the actual shell is exactly the Haar pushforward of that same character polynomial. The valid Haar coordinates are base-prime phases; ratio-mode phases retain their induced character dependencies.

`VIS-420` closes the elementary finite-window calibration for character-polynomial observables. Translation error is an explicit sinc-weighted Fourier sum whose sufficient bound pays the active small divisors `|m dot (log p)|`; for shell energy these are exactly the pairwise beat gaps `|lambda_j-lambda_k|`. A finite translation window is therefore auditable for polynomial diagnostics, while nonlinear amplitude/persistence tails still require direct Haar evaluation or a controlled Fourier approximation.

`VIS-421` corrects the remaining source-interface assumption. Wang's short-interval source treats `T` as the generic asymptotic interval start, with `H=T^theta`, and the imported explicit formula uses ordinary real `t in (T,T+H]`. The source interface does not itself define a sparse distinguished-height selector. Therefore any actual panel used here must either be derived separately and justified as part of the same source interface, or be declared as an external arithmetic/zeta selector. In the latter case the experiment tests cross-structure alignment, not a height selected by Wang alone.

`VIS-422` now disposes of the most obvious external selector in the **fixed-shell** regime. Existing discrete-universality prior art proves that the full prime-phase vector at ordinary Gram points converges to Haar measure on the prime torus. Combined with the `VIS-419` shell representation, this implies that normalized amplitudes and every fixed-radius continuous persistence statistic sampled at Gram points converge to their exact fixed-shell Haar self-null. Ordinary Gram points therefore cannot generate an asymptotic fixed-shell low-tail excess.

## Research question

Fix, before inspecting shell values, a deterministic arithmetic height selector `S={T_j}` with explicit provenance and a pre-specified rule transporting the Wang shell family across those heights. Do the selected heights exhibit unusually small normalized amplitudes or unusually persistent local quiet regions **relative to the exact translation/Haar self-null of each corresponding frozen shell**, after bandwidth normalization and without scanning the selector, shift, shell scale, or persistence radius to favor the observed values?

If the selector is external to Wang's short-interval construction, does its coupling to the Wang shell family produce a reproducible low-tail excess that cannot be explained by bandwidth, beat scales, shell scaling, the selector's own trivial periodicities, or an equidistribution theorem forcing the selector's prime phases to the same Haar null?

## Why it may matter

This isolates a cleaner question than comparing raw balance radii against loosely matched random sums. A fixed-shell translation/Haar baseline preserves the shell's exact frequencies, coefficient magnitudes, beat gaps, internal spectral crowding, and all algebraic dependencies among ratio modes. What it changes is only alignment between the frozen shell and the selected height.

`VIS-421` prevents false source attribution, while `VIS-422` adds a selector-level negative control: a deterministic arithmetic selector can still be asymptotically neutral because its prime phases already sample Haar. A positive effect from another external selector would therefore require genuine non-Haar or growing-family structure rather than deterministic sparsity by itself.

## Decisive test

Before evaluating any comparison value, freeze all of the following:

- the deterministic rule defining the arithmetic height panel and the mathematical reason for choosing it;
- whether that selector is internal to the Wang source interface or explicitly external to it;
- the shell-family transport rule across heights, including the choices of `theta`, `lambda`/`x`, dyadic shell identity or scaling rule, and bandwidth normalization;
- the amplitude/persistence statistic and, for persistence, the fixed radius or its pre-specified scale law;
- the panel-level aggregation rule for combining conditional Haar tail ranks;
- any numerical approximation rule.

Before numerical evaluation, audit whether the selector's base-prime phase vectors are already known or derivably forced to equidistribute to Haar for every fixed finite prime set. If so, as for ordinary Gram points by `VIS-422`, kill the fixed-shell asymptotic anomaly route for that selector rather than simulating a comparison whose limit is already determined.

For a selector not eliminated by that audit, use the exact base-prime Haar pushforward supplied by `VIS-419` as the canonical fixed-shell self-null. Independent randomization of ratio-mode phases is not an admissible substitute.

Apply the same bandwidth normalization from `VIS-416`. For persistence, use a pre-specified continuous observable such as

`Q_(i,rho)(T)=sup_(|u|<=rho)|F_i(T+u)|/||F_i||_infinity`,

or another statistic with an explicitly justified continuity/tail calibration.

Prefer direct prime-torus Haar integration or Haar phase sampling for the null. If finite translation of the actual shell is used instead, pre-register the translation window and apply `VIS-420`: polynomial calibration observables must have an explicit small-divisor error bound below the intended tolerance, while nonlinear amplitude/persistence statistics require either a quantitative Fourier approximation or a separate stability argument. A window is not justified merely because it is large compared with the shell's outer bandwidth.

Kill the direction if no non-arbitrary selector with defensible provenance can be frozen, if a selector is already asymptotically Haar on the relevant prime torus in the fixed-shell regime, if the selected heights are typical under their exact fixed-shell self-nulls, if any apparent excess disappears under the pre-registered shell-scaling or numerical calibration, or if the effect can be recreated by selecting favorable heights, shell scales, radii, or shifts after inspection. Any jointly growing shell/height regime requires a separate uniform quantitative equidistribution argument before a residual can be interpreted.

## Evidence boundary

`VIS-419` proves the asymptotic fixed-shell translation/Haar calibration. `VIS-420` supplies the exact finite-window sinc formula and small-divisor bound for finite character-polynomial observables, including shell mean and energy. `VIS-421` proves only an interface boundary: the Wang source currently imported by this line does not itself supply the distinguished-height selector that an anomaly test needs. `VIS-422`, using direct prior art on Gram-point prime phases, proves that ordinary Gram points converge to the same Haar null for every fixed finite shell and fixed-radius continuous persistence observable.

None of these findings identifies a selector with an anomalous Wang-shell phase law. `VIS-422` does not cover shell observables whose support or scale grows with the Gram-point index, nor does it cover a different selector whose prime-phase image is not Haar. The intended normalized-amplitude and quiet-region tail statistics remain nonlinear, and no current result justifies a jointly growing shell/height limit.

A positive result with an external selector would establish only a source-grounded cross-structure anomaly after the declared controls. It would not by itself produce an RH mechanism or turn the selector into part of Wang's theorem.

## Research disposition

Accepted, further narrowed by `VIS-422`. **Ordinary Gram points are no longer a live fixed-shell selector candidate:** their prime phases already converge to the exact Haar self-null. Continue only with a selector whose provenance is independent of observed shell values and whose prime-phase law is not already forced to the same fixed-shell Haar limit, or with an explicitly formulated growing-shell regime where the fixed-observable Gram-point theorem is insufficient. Selector/equidistribution audit precedes numerical evaluation.
