---
id: CLUE-visual-exploration-prime-phase-critical-logarithmic-occupancy
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-225-coherent-prime-blocks-force-divergent-ising-scale.md
  - research/visual_exploration/findings/VIS-226-subcritical-symmetric-taper-worst-start-exact-scale.md
  - research/visual_exploration/findings/VIS-227-critical-phase-cell-collisions-have-balanced-occupancy-floor.md
  - research/visual_exploration/findings/VIS-228-multinomial-cell-collisions-have-extensive-excess-above-balanced-floor.md
  - research/visual_exploration/findings/VIS-229-nonuniform-categorical-cell-collisions-have-third-moment-variance.md
  - research/visual_exploration/findings/VIS-230-stationary-markov-cell-collisions-have-lag-return-center.md
  - research/visual_exploration/findings/VIS-231-stationary-markov-cell-collisions-have-exact-triple-quadruple-variance.md
  - research/visual_exploration/findings/VIS-232-transition-conditioned-collision-controls-are-occupancy-degenerate.md
  - research/visual_exploration/findings/VIS-233-lag-two-returns-escape-first-order-markov-type.md
  - research/visual_exploration/findings/VIS-234-markov-type-lag-two-pgf-recursion.md
  - research/visual_exploration/findings/VIS-235-lag-two-markov-type-mean-by-two-step-deletion.md
  - research/visual_exploration/findings/VIS-236-ordered-prime-coordinate-cells-make-first-order-type-degenerate.md
  - research/visual_exploration/findings/VIS-237-random-origin-cell-collisions-are-triangular-pair-functional.md
  - research/visual_exploration/findings/VIS-238-fixed-count-tent-calibration-removes-poissonization-variance.md
  - research/visual_exploration/findings/VIS-239-cumulative-intensity-gauge-uniformizes-specified-iid-intensity.md
  - research/visual_exploration/findings/VIS-240-rotation-randomized-dirichlet-gaps-give-fixed-count-uniform-intensity-dependence-null.md
  - research/visual_exploration/findings/VIS-241-random-cut-separates-endpoint-phase-variance.md
  - research/visual_exploration/findings/VIS-242-dirichlet-gap-tent-variance-overlap-classes.md
  - research/visual_exploration/findings/VIS-243-complement-symmetry-closes-cyclic-overlap-multiplicities.md
  - research/visual_exploration/findings/VIS-244-empirical-gap-concentration-identifies-dirichlet-alpha.md
  - research/visual_exploration/findings/VIS-245-gap-concentration-tent-covariance-beta-moments.md
---

# Is there prime-specific critical pair geometry after fixed-count dependent-spacing and endpoint-phase calibration?

## Observation

The critical coherence-cell branch has progressively quotiented the obvious representation and null-model confounds. `VIS-227`--`VIS-236` calibrate occupancy, heterogeneous/Markov effects, and the degeneracy of controls that ignore the actual monotone ordered-point support. `VIS-237` removes arbitrary grid origin by identifying the triangular short-range pair functional. `VIS-238` removes Poisson count noise, and `VIS-239` separates an independently specified one-point intensity from the dependence question.

`VIS-240` supplies a nontrivial representation-matched dependence family: symmetric cyclic Dirichlet gaps with fixed count, uniform one-point intensity after random rotation, monotone ordered support, and a predeclared parameter `alpha` controlling spacing dependence. `VIS-241` removes the arbitrary interval-cut phase when endpoints are nuisance. `VIS-242` reduces the exact tent variance to finite Dirichlet overlap classes, and `VIS-243` closes their deterministic cyclic multiplicities.

`VIS-244` gives a distinct same-configuration identification statistic,

`C=m sum_i X_i^2-1`,

with exact mean and variance under fixed `alpha`. `VIS-245` now closes the remaining fixed-parameter second-moment cross term: `Cov(C,bar T)` is an explicit finite sum of one-dimensional truncated beta moments through degree four. Consequently the complete mean vector and covariance matrix of `(C,bar T)` are exact for every predeclared symmetric-Dirichlet `alpha`.

This still does not make a same-sample plug-in test exact. The nonlinear estimator `alpha_hat(C)` and the conditional/full joint law of `bar T` after observing `C` are not determined by the covariance matrix. The live question is therefore whether the frozen prime-coordinate configuration has a residual after that final nuisance-propagation step, rather than after a naive fixed `alpha_hat` substitution.

## Research question

Fix the critical `lambda` family, midpoint-symmetric taper, phase/coherence tolerance, point-coordinate normalization, width rule, endpoint convention, statistic, and dependence model before confirmation. Freeze `alpha` from theory/held-out information, or if the same configuration supplies `C`, carry the fitted nuisance through a valid joint/conditional calibration rather than plugging `alpha_hat(C)` into the fixed-parameter `bar T` law.

Under that frozen specification, does the prime-coordinate `bar T` exhibit a stable residual relative to the symmetric-Dirichlet calibration across increasing scales? If endpoints are declared physical signal rather than nuisance, use the post-cut statistic and add the exact endpoint channel from `VIS-241` instead of switching conventions after observing the result.

If a residual survives, can it also survive a stronger predeclared spacing control and then be translated into a lower bound, obstruction, or structural constraint for the signed prime-phase quadratic energy rather than remaining a generic point-process anomaly?

## Why it may matter

The branch has removed forced occupancy, count fluctuation, specified one-point intensity, arbitrary grid origin, support-mismatched label randomization, a nontrivial spacing-dependence axis, arbitrary endpoint cut phase, cyclic-overlap bookkeeping, and the missing covariance between the nuisance-identification statistic and confirmation statistic.

A residual that disappears after honest nuisance propagation is generic spacing heterogeneity, not prime-specific structure. A residual that survives is still far below an RH result, but it would have passed a materially stronger representation-matched null and would justify asking whether the surviving statistic couples to the signed arithmetic kernel rather than merely to local point geometry.

## Decisive test

Before examining the confirmation residual, freeze all representation choices and the `alpha` rule. Evaluate the exact fixed-parameter center/variance calibration from `VIS-240`--`VIS-243`; at `alpha=1`, require agreement with the closed polynomial tent variance from `VIS-242` as an implementation audit.

If `alpha` is supplied by theory or genuinely held-out data, propagate whatever uncertainty remains and test `bar T` under that frozen rule. If `alpha` is estimated from the same cyclic gap vector through `C`, use `VIS-244`--`VIS-245` to audit the nuisance channel and cross-covariance, but do **not** treat those second moments as the final conditional calibration. Derive the conditional/full joint law needed for `bar T | C`, or independently validate a procedure that carries the fitted `alpha_hat(C)` through the null with errors materially below the proposed residual scale.

Compare the predeclared prime statistic against this calibration across increasing scales without retuning `alpha`, `ell`, the endpoint convention, or the statistic. Kill the candidate if the anomaly disappears under the frozen dependence calibration; if it depends on Poisson count noise, same-sample intensity flattening, random-cut phase declared to be nuisance, naive plug-in nuisance fitting, or post-hoc tuning; if significance is unstable across the predeclared scale family; or if a stronger representation-matched spacing control reproduces the effect.

Only after a stable residual survives should a new mathematical thread translate it back through the signed prime-phase kernel and audit equivalent formulations in logarithmic prime gaps, short-interval counts, prime-pair/higher-correlation statistics, and critical Dirichlet-polynomial theory.

## Evidence boundary

`VIS-237`--`VIS-241` establish the representation quotients and the symmetric-Dirichlet dependence family. `VIS-242`--`VIS-243` establish the exact fixed-parameter tent variance reduction and deterministic overlap coefficients. `VIS-244` establishes the concentration-based `alpha` identification channel and its variance. `VIS-245` establishes the exact fixed-parameter cross-covariance between that concentration and `bar T`, completing the covariance matrix of `(C,bar T)`.

None of these findings proves that the one-parameter Dirichlet family is a faithful final model of prime gaps, supplies the exact conditional/full joint law required for same-configuration nuisance fitting, or reports a prime residual. In particular, covariance information alone does not make the nonlinear plug-in statistic calibrated. No cited result establishes prime-specific critical separation or any RH consequence.

## Research disposition

The clue remains `accepted`. Fixed-parameter first and second moments are now explicit, including the same-sample nuisance cross term. The remaining same-configuration gate is the conditional/full joint calibration needed to turn observed `C` into a valid null for `bar T`; alternatively, held-out/theoretical `alpha` bypasses that gate and leaves the actual frozen confirmation test as the next step.
