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
  - research/visual_exploration/findings/VIS-425-fixed-radius-wang-persistence-moment-tariff.md
  - research/visual_exploration/findings/VIS-427-growing-window-path-average-no-radius-tariff.md
---

# Does an independently justified arithmetic height selector align with Wang quiet regions beyond each shell's own translation orbit?

## Observation

`VIS-416` isolates normalized shell amplitude after removing the generic reciprocal-bandwidth scale. `VIS-417` and `VIS-418` show that beat scales and global time translation can manufacture long quiet regions while preserving coarse spectral data, so fixed-height smallness must be calibrated against the exact shell orbit rather than against loose random-sum controls.

`VIS-419` supplies that exact fixed-shell null: a finite Wang shell is a Laurent polynomial on its base-prime torus, and long translation is its Haar pushforward. `VIS-420` quantifies finite-window character-polynomial calibration through prime-log small divisors. `VIS-421` then separates selector provenance from Wang's source interface: Wang's generic interval start does not itself choose a sparse distinguished-height panel.

For ordinary Gram points, the escape route has narrowed repeatedly. `VIS-422` proves fixed finite prime-phase vectors are asymptotically Haar. `VIS-423` gives a quantitative tariff for changing Laurent-polynomial observables. `VIS-424` reduces normalized pointwise amplitude to fixed scalar moment tariffs plus Haar anti-concentration.

`VIS-425` removes the remaining ambiguity for **fixed-radius persistence** in the canonical strict near-band shells. Their frequency radius is uniformly below `log 2`, so Bernstein's inequality turns every fixed path window into a finite offset mesh at arbitrary fixed accuracy. Mixed offset moments pay the same `VIS-423` character tariff, with a structural divisor that for a dyadic shell of arithmetic height `Y_N` satisfies

`delta^*_(N,R) >= (2Y_N)^(-2R)`.

Thus fixed-radius local suprema are not an independent nonlinear escape once the strengthened mixed-moment tariffs and Haar boundary-mass condition pass.

`VIS-427` now closes a different growing-path loophole. For every fixed power `q`, the normalized path average

`J_(N,q)=(1/(2rho_N)) int_(-rho_N)^(rho_N) X_(N,u)^q du`

pays **no additional radius tariff**, even when `rho_N -> infinity`: Fubini expands each fixed moment into the same shifted Laurent characters, while the offset-box volume cancels against the path-length normalization. Therefore merely increasing the observation radius cannot create a Gram/Haar anomaly for normalized fixed-power path averages when the existing Wiener/frequency/small-divisor tariffs pass.

A surviving Gram-point anomaly must now expose a quantified tariff failure, nonuniform Haar concentration, a selector with a genuinely non-Haar finite-prime phase law, or **localized path concentration invisible to normalized averages**. Growing radius by itself is no longer an escape.

## Research question

Fix, before inspecting shell values, a deterministic arithmetic height selector `S={T_j}` with explicit provenance and a pre-specified rule transporting the Wang shell family across those heights. Do the selected heights exhibit unusually small normalized amplitudes or unusually persistent quiet regions relative to each corresponding shell's exact translation/Haar self-null, after bandwidth normalization and without scanning the selector, shell scale, shift, persistence radius, moment order, or statistic to favor the observed values?

For ordinary Gram points and strict near-band Wang shells, do the **actual transported source coefficients** violate the combined `VIS-424`/`VIS-425`/`VIS-427` sufficient null through excessive normalized Wiener mass, unexpectedly small fixed-order product-ratio divisors, nonuniform Haar concentration, or concentration of high amplitude into a vanishing relative subset of a growing path window? If not, pointwise amplitude, fixed-radius persistence, and normalized fixed-power path averages are all forced to their own Haar self-nulls under the corresponding gates.

## Why it may matter

The control hierarchy now preserves essentially all fixed-shell arithmetic character structure while removing generic explanations one by one. Deterministic selector sparsity is insufficient (`VIS-422`); growing dimension alone is insufficient below the character tariff (`VIS-423`); scalar modulus is insufficient below the moment tariff (`VIS-424`); a fixed local supremum is insufficient when uniform bandwidth and mixed-moment tariffs hold (`VIS-425`); and a normalized fixed-power path average cannot escape merely by widening its observation window (`VIS-427`).

A positive residual would therefore have to identify a concrete source resource rather than hide behind generic nonlinearity, finite-window beating, path dependence, or growing path length. A negative result is equally useful because it closes the current Gram selector branch at the level of the actual Wang transport rather than by simulation.

## Decisive test

Before numerical evaluation, freeze the selector provenance, the shell-family transport rule, the Wang parameters, bandwidth normalization, amplitude/persistence statistic, persistence-radius law, panel aggregation, moment orders used by any path-average statistic, and numerical approximation rule.

For an ordinary-Gram strict near-band shell

`F_N=sum_a b_(N,a) z^a`,

compute or rigorously bound

`W_N=(sum_a |b_(N,a)|)/||F_N||_infinity`

and the dyadic shell height `Y_N`. For every fixed total moment order `R` relevant to the intended test, use the structural divisor

`delta^*_(N,R)=min |sum_(j=1)^R(lambda_(a_j)-lambda_(c_j))|`

over nonzero values. `VIS-425` gives the source-independent bound

`delta^*_(N,R) >= (2Y_N)^(-2R)`

for the strict near-band ratio shells.

Attempt the explicit sufficient tariff

`W_N^(2R) [ 1/N + R/log N + (log N)(2Y_N)^(2R)/N ] -> 0`

for every fixed `R`, or replace the elementary divisor floor by a sharper proved bound when available. If these mixed-moment tariffs pass, `VIS-425` forces every fixed continuous pointwise-amplitude and fixed-radius persistence diagnostic to its Haar self-null. For a fixed low-tail threshold, additionally require the corresponding Haar boundary mass to vanish uniformly in shrinking neighborhoods of that threshold.

For any normalized growing-window path average of a **fixed** power, do not add a radius penalty: `VIS-427` shows that the same fixed-order character tariff controls its moments for arbitrary `rho_N`. Treat an observed dependence on growing radius in such an averaged statistic as a reason to audit normalization, coefficient transport, moment order, or tariff failure rather than as a new mechanism by itself.

Only a quantified failure of these gates should remain live. A failed sufficient bound is **not** evidence of an anomaly: identify which resource causes the failure and test whether it is specific to the Wang source rather than a generic property of comparable finite character polynomials. If the intended diagnostic is a growing-window **supremum** or another functional sensitive to concentration on a vanishing relative subset, formulate that localization explicitly; `VIS-427` does not reduce such a statistic to fixed-power normalized averages. Likewise, allowing the moment order itself to grow with `N` lies outside the fixed-order closure and needs a separate argument.

For a different external selector, first audit whether its finite prime-phase vectors or the relevant changing observables are already forced to the same Haar null. Independent randomization of ratio-mode phases is not an admissible substitute for the base-prime Haar control.

Kill the direction if no non-arbitrary selector with defensible provenance can be frozen, if the relevant selector is already Haar in the tested regime and the combined amplitude/persistence/path-average tariffs pass, if the selected heights are typical under their exact self-nulls, or if an apparent effect disappears under the pre-registered transport/scaling rules or can be recreated by post-selection.

## Evidence boundary

`VIS-419` proves fixed-shell Haar calibration; `VIS-420` gives finite-window small-divisor costs; `VIS-421` separates Wang's generic source height from an external selector; `VIS-422` closes ordinary Gram points for fixed shells; `VIS-423` controls changing Laurent-polynomial observables; `VIS-424` reduces pointwise amplitude to scalar moments; `VIS-425` extends that reduction to fixed-radius persistence under a uniform frequency bound and stronger mixed-frequency divisor; and `VIS-427` shows that normalized fixed-power path averages acquire no additional growing-radius tariff.

None of these findings proves that the actual transported Wang growing family satisfies the sufficient tariffs, proves uniform Haar anti-concentration at a chosen threshold, or establishes a source-sensitive anomaly when a tariff fails. `VIS-427` also does not control growing-window suprema, concentration supported on a vanishing relative path set, or moment orders that grow with `N`.

No current result identifies a selector with an anomalous Wang-shell phase law, establishes a source-sensitive low-tail excess, produces an RH mechanism, or turns an external selector into part of Wang's theorem.

## Research disposition

Accepted, further narrowed by `VIS-427`. **For ordinary Gram points, pointwise amplitude, fixed-radius persistence, and normalized fixed-power path averages now share the same basic character-tariff decision boundary; growing path length alone is not a residual resource.** Continue only with a quantified failure of those gates, a selector whose prime-phase law is not already driven to the same self-null, a genuinely localized/supremum path effect invisible to normalized averages, a growing-moment regime, or another destination observable not reduced by the current character machinery.