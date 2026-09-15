---
id: CLUE-visual-exploration-prime-phase-critical-logarithmic-occupancy
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-225-coherent-prime-blocks-force-divergent-ising-scale.md
  - research/visual_exploration/findings/VIS-226-finite-phase-net-scan-controls-subcritical-worst-start.md
  - research/visual_exploration/findings/VIS-227-critical-phase-cell-collisions-have-balanced-occupancy-floor.md
  - research/visual_exploration/findings/VIS-228-multinomial-cell-collisions-have-extensive-excess-above-balanced-floor.md
  - research/visual_exploration/findings/VIS-229-nonuniform-categorical-cell-collisions-have-third-moment-variance.md
  - research/visual_exploration/findings/VIS-230-stationary-markov-cell-collisions-have-lag-return-center.md
  - research/visual_exploration/findings/VIS-231-stationary-markov-cell-collisions-have-exact-triple-quadruple-variance.md
  - research/visual_exploration/findings/VIS-232-transition-conditioned-collision-controls-are-occupancy-degenerate.md
  - research/visual_exploration/findings/VIS-233-lag-two-returns-escape-first-order-markov-type.md
---

# Is there prime-specific critical phase-cell structure after dependent occupancy calibration?

## Observation

`VIS-225` obtains a strict-subcritical worst-start lower bound by partitioning primes in `(y/2,y]` into phase-coherent cells of width `eta_v y/(8H)`. `VIS-226` closes the strict-subcritical worst-start scale through a finite phase-net scan, leaving the critical scale `H=lambda y/log y` outside that argument.

`VIS-227` shows that at critical scale the raw same-cell collision count

`S_lambda(y)=sum_j binom(n_j,2)`

has an exact deterministic floor forced solely by fitting `m` points into `J` cells. `VIS-228` removes the next false positive: under independent uniform allocation with the same `m` and `J`, an extensive excess above that floor is generic. `VIS-229` extends the exact center and variance to nonuniform independent categorical allocation, where `q_3-q_2^2` contributes an additional variance term.

`VIS-230` shows that matching the one-point law is insufficient for a dependent control. For a stationary Markov cell process with lag return probabilities `c_r=P(X_0=X_r)`, the exact collision center is

`E[S]=sum_(r=1)^(m-1)(m-r)c_r`,

and `VIS-231` gives the corresponding exact finite-sample variance through three- and four-time coincidence probabilities.

`VIS-232` adds the model-admission obstruction. Since

`S=sum_j binom(N_j,2)`,

conditioning on the exact confirmation-sample occupancy histogram fixes `S`. Preserving the full first-order transition-count matrix plus an endpoint also fixes the histogram and therefore conditions `S` away. An exact transition-count-preserving or block-reordering surrogate is thus not a stronger nondegenerate null for this scalar statistic.

`VIS-233` identifies the first simple local escape from that degeneracy. If endpoints and first-order transition counts are fixed, every translation-invariant additive observable built from individual states and adjacent pairs is fixed as well. But the lag-two return statistic

`T_2=sum_(t=1)^(m-2) 1_{x_t=x_(t+2)}`

depends on length-three block counts and can vary inside the same endpoint-matched first-order type. The exact binary type with realizations `00010`, `00100`, `01000` has identical transition counts but `T_2` values `2,1,2`, giving conditional variance `2/9` under the uniform conditional ensemble.

The live critical problem therefore has two honest routes. Either keep the scalar collision statistic `S` and use a stochastic dependence model fitted independently of confirmation, leaving confirmation occupancies random; or preserve stronger realized first-order structure and move to a predeclared higher-order observable such as `T_2` that remains nondegenerate inside that conditional class.

## Research question

For fixed critical `lambda`, after choosing a dependence control independently of the confirmation outcome, does the actual prime system exhibit a stable residual beyond that control's calibrated center and covariance?

For the stochastic route, if a stationary first-order Markov surrogate is justified from an independently frozen calibration range or analytic local model, use the exact `VIS-230` center and `VIS-231` variance and propagate parameter-estimation uncertainty. Does the predeclared scalar collision residual remain non-generic across increasing scales and reasonable fixed cell-origin perturbations?

For the exact first-order-type route, does a predeclared lag-two/triple-based observable such as `T_2` have a nondegenerate conditional law for the actual critical prime-phase type, and does the observed value separate from that law without choosing the statistic from confirmation data? If so, can that separation be translated into a lower bound or obstruction for the signed prime-phase quadratic energy rather than remaining a generic higher-order pattern statistic?

## Why it may matter

The deterministic floor, independent uniform baseline, nonuniform categorical baseline, Markov centering, exact Markov covariance, conditional-degeneracy obstruction, and now the range-one/range-two information boundary remove seven increasingly strong sources of false arithmetic structure or circular control design.

`VIS-233` is useful because it turns the vague instruction “use something order-sensitive” into a falsifiable first candidate while also ruling out an entire class of fake replacements: any translation-invariant additive reweighting of states or adjacent transitions remains fixed by the same first-order control. A surviving `T_2`-type residual would therefore contain information genuinely outside the preserved first-order type, though it would still need a separate arithmetic and signed-kernel bridge.

## Decisive test

Freeze the taper, phase tolerance, cell-origin convention, a finite set of `lambda` values, the statistic, and the null family before inspecting confirmation outcomes.

For the scalar collision statistic `S`, do **not** condition the confirmation null on the exact occupancy histogram or endpoint-matched exact transition counts. Estimate any stochastic null parameters from an analytic model, an independently frozen calibration range, or another source that leaves confirmation occupancies random. Use `VIS-229` for an independent categorical null and the exact `VIS-230`/`VIS-231` moments for a specified stationary first-order Markov null, carrying parameter-estimation uncertainty when `pi,P` are estimated.

For an exact first-order transition-count-preserving control, predeclare `T_2` or one other explicitly specified statistic whose value is not measurable from the preserved summary. First enumerate or otherwise characterize its conditional support for the actual endpoint-matched transition type; if its conditional variance is zero, kill that statistic immediately. Otherwise calibrate its exact or faithfully sampled conditional law without using the confirmation value to tune the observable. Account for any predeclared `lambda`/cell-origin family jointly rather than treating searched views as independent confirmations.

If the admitted control is strengthened to preserve all length-three block counts, `T_2` is again conditioned away and is no longer admissible. Any successor must lie outside the stronger preserved sigma-field rather than merely renormalize fixed counts.

Only if a residual survives these gates should it be translated back through the signed phase kernel. Kill the route if the residual is explained by the calibrated control, is unstable under allowed representation perturbations, or cannot be connected to the signed phase energy. Before promotion to a prime-specific finding, audit equivalent formulations in logarithmic-scale prime gaps, short-interval counts, conditional Markov-type pattern statistics, renewal controls, and prime-pair/higher-correlation statistics.

## Evidence boundary

`VIS-227` establishes the deterministic occupancy floor. `VIS-228` and `VIS-229` establish exact independent uniform/nonuniform collision baselines. `VIS-230` and `VIS-231` establish the exact stationary first-order Markov center and variance. `VIS-232` proves that `S` is conditioned away by exact occupancy or endpoint-matched first-order transition counts. `VIS-233` proves that the same first-order type fixes every translation-invariant additive range-one observable but need not fix a lag-two return statistic.

None of these results establishes a faithful prime dependence model, the actual prime residual under a frozen stochastic or conditional calibration, a central limit theorem for the chosen null, prime specificity of `T_2`, any critical-scale optimizer separation, or any RH consequence.

## Research disposition

The clue remains accepted. The combinatorial existence question for an order-sensitive first-order-type escape is now resolved by `VIS-233`; the next gate is to calibrate a predeclared lag-two/triple statistic on the actual critical prime-phase transition type and test whether any residual is prime-specific and stable. In parallel, the scalar-collision route remains viable only under an independently calibrated stochastic dependence model that leaves confirmation occupancies random.