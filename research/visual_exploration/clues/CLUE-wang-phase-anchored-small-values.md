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
  - research/visual_exploration/findings/VIS-423-gram-block-character-small-divisor-tariff.md
  - research/visual_exploration/findings/VIS-424-normalized-wang-amplitude-moment-tariff.md
---

# Does an independently justified arithmetic height selector align with Wang quiet regions beyond each shell's own translation orbit?

## Observation

`VIS-416` isolates the bandwidth-normalized amplitude `a_i(T)=|F_i(T)|/||F_i||_infinity` as the candidate small-value factor after removing the generic reciprocal-bandwidth scale. `VIS-417` shows that long finite-window suppression can still be manufactured by an unresolved beat scale even when mode count, coefficient magnitudes, long-time energy, bandlimit, and global sup norm are fixed.

`VIS-418` strengthens that control. Even after the complete two-mode frequency set and its beat gap are fixed, global translation can move an arbitrarily long quiet interval onto or away from any prescribed observation height while preserving the full frequency geometry, coefficient magnitudes, long-time energy, and sup norm. Fixed-height localization therefore contains a phase/time-origin alignment component that ordinary spectral matching does not remove.

`VIS-419` closes the fixed-shell asymptotic calibration question: each canonical finite Wang shell is a finite character polynomial on its base-prime torus, and long translation of the actual shell is exactly the Haar pushforward of that same character polynomial. The valid Haar coordinates are base-prime phases; ratio-mode phases retain their induced character dependencies.

`VIS-420` closes the elementary finite-window calibration for character-polynomial observables. Translation error is an explicit sinc-weighted Fourier sum whose sufficient bound pays the active small divisors `|m dot (log p)|`; for shell energy these are exactly the pairwise beat gaps `|lambda_j-lambda_k|`. A finite translation window is therefore auditable for polynomial diagnostics, while nonlinear amplitude/persistence tails still require direct Haar evaluation or a controlled approximation.

`VIS-421` corrects the remaining source-interface assumption. Wang's short-interval source treats `T` as the generic asymptotic interval start, with `H=T^theta`, and does not itself define a sparse distinguished-height selector. Any actual panel must therefore be justified separately or declared as an external arithmetic/zeta selector. In the latter case the experiment tests cross-structure alignment, not a height selected by Wang alone.

`VIS-422` disposes of ordinary Gram points in the fixed-shell regime: their finite prime-phase vectors converge to Haar, so every fixed finite Wang shell and fixed continuous persistence observable has the same asymptotic Gram law as its exact Haar self-null.

`VIS-423` supplies a quantitative partial closure for changing Laurent-polynomial observables on dyadic Gram blocks. Increasing prime support alone is not enough: the total Fourier mass, frequency-weighted mass, and reciprocal-frequency/small-divisor mass must actually exceed the explicit Gram tariff to escape the Haar mean.

`VIS-424` removes the remaining ambiguity for **pointwise normalized amplitude**. With `X_N=|F_N|^2/||F_N||_infinity^2`, every fixed moment `X_N^r` is again a Laurent polynomial, and its `VIS-423` costs are bounded by the normalized Wiener mass `W_N`, outer frequency scale `Omega_N`, and the fixed-order prime-log small divisor `delta_(N,r)`. If those moment tariffs vanish for every fixed `r`, then every fixed continuous function of normalized amplitude has the same Gram-block average as the corresponding Haar self-null. A fixed low-tail threshold is also forced to Haar once the Haar amplitude laws satisfy a uniform boundary-mass/anti-concentration condition.

Thus the modulus itself is no longer an unspecified nonlinear escape. The remaining Gram-point resource must be visible as moment-tariff failure, nonuniform Haar concentration near the chosen threshold, or genuinely path-valued persistence structure.

## Research question

Fix, before inspecting shell values, a deterministic arithmetic height selector `S={T_j}` with explicit provenance and a pre-specified rule transporting the Wang shell family across those heights. Do the selected heights exhibit unusually small normalized amplitudes or unusually persistent local quiet regions **relative to the exact translation/Haar self-null of each corresponding frozen shell**, after bandwidth normalization and without scanning the selector, shift, shell scale, or persistence radius to favor the observed values?

For ordinary Gram points, the pointwise amplitude branch is now narrower: do the actual changing Wang shells violate the `VIS-424` moment conditions through excessive normalized Wiener mass, high character scale, fixed-order prime-log small divisors, or nonuniform Haar concentration at the intended low-tail threshold? If not, the normalized-amplitude route is already asymptotically Haar and should be closed without numerical anomaly hunting.

The separate persistence question remains: can a pre-specified path-valued statistic such as a fixed-radius local supremum evade the scalar moment reduction while surviving the `VIS-420`/`VIS-423` calibration gates?

## Why it may matter

This isolates a cleaner question than comparing raw balance radii against loosely matched random sums. The exact prime-torus Haar self-null preserves the shell's frequencies, coefficient magnitudes, beat gaps, internal spectral crowding, and algebraic dependencies among ratio modes. What changes is only alignment between the frozen shell and the selected height.

The cumulative negative controls now distinguish three levels. Deterministic sparsity of a selector is insufficient (`VIS-422`); growing shell dimension is insufficient when its Fourier observables stay below the character tariff (`VIS-423`); and pointwise absolute value is insufficient when the scalar moment tariffs and Haar anti-concentration pass (`VIS-424`). A surviving anomaly must therefore expose a concrete source resource rather than hide behind generic nonlinearity.

## Decisive test

Before evaluating any comparison value, freeze the deterministic height rule and its provenance, whether it is internal or external to the Wang source interface, the shell-family transport rule, bandwidth normalization, the amplitude/persistence statistic, the persistence radius or scale law, the panel aggregation rule, and any numerical approximation rule.

For ordinary Gram points, apply the analytic gates before simulation. For a shell

`F_N=sum_a b_(N,a) z^a`,

compute or bound

`W_N=(sum_a |b_(N,a)|)/||F_N||_infinity`,

`Omega_N=max_a |sum_p a_p log p|`,

and, for each fixed moment order needed by the intended scalar test,

`delta_(N,r)=min{|nu|: nu!=0 occurs in (|F_N|^2/||F_N||_infinity^2)^r}`.

If

`W_N^(2r)[1/N + r Omega_N/log N + log N/(N delta_(N,r))] -> 0`

for every fixed `r`, then `VIS-424` already forces every fixed continuous amplitude diagnostic to its Haar self-null. For a fixed low-tail threshold `t`, additionally test the Haar boundary mass `m_H{|X_N-t|<=eta}` uniformly in `N`; if it vanishes as `eta->0`, the tail frequency is also analytically closed.

Only if one of those amplitude gates fails should the failure be treated as the candidate resource and investigated further. Do not interpret a failed sufficient bound as evidence of an anomaly.

For persistence, use the exact base-prime Haar pushforward from `VIS-419`. If finite translation is used, apply the `VIS-420` small-divisor calibration. Any polynomial surrogate must satisfy `VIS-423`; a genuinely nonlinear path statistic needs a separate uniform approximation/stability argument rather than pointwise-amplitude moments.

Kill the direction if no non-arbitrary selector with defensible provenance can be frozen, if the relevant selector is already Haar for the tested regime, if the Gram amplitude moment and boundary-mass gates pass, if the selected heights are typical under their exact self-nulls, or if an apparent effect disappears under the pre-registered shell scaling or can be recreated by post-selection.

## Evidence boundary

`VIS-419` proves the fixed-shell translation/Haar calibration. `VIS-420` gives the finite-window character-polynomial error with explicit small-divisor cost. `VIS-421` proves only an interface boundary: the imported Wang source does not itself supply a distinguished-height selector. `VIS-422` proves ordinary Gram points are asymptotically Haar for every fixed finite shell. `VIS-423` adds a quantitative sufficient condition for changing Laurent-polynomial observables.

`VIS-424` adds a scalar moment reduction for pointwise normalized amplitude. It does **not** prove that the actual Wang growing family satisfies the moment tariffs, does not prove uniform Haar anti-concentration at any chosen threshold, and does not control the path-valued persistence supremum. Failure of any sufficient gate is not evidence of a positive arithmetic anomaly.

No current result identifies a selector with an anomalous Wang-shell phase law, establishes a source-sensitive low-tail excess, produces an RH mechanism, or turns an external selector into part of Wang's theorem.

## Research disposition

Accepted, further narrowed by `VIS-424`. **Ordinary Gram points remain live only where an explicit amplitude resource or path-valued persistence obstruction survives the analytic nulls.** For pointwise amplitude, first audit `W_N`, `Omega_N`, fixed-order `delta_(N,r)`, and Haar threshold anti-concentration; if they pass, close the Gram amplitude route. Continue only with a quantified failure of those gates, a genuinely different selector, or the persistence statistic whose local-supremum structure is not reduced by `VIS-424`.