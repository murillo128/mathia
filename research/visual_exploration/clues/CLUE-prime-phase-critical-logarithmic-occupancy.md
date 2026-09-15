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
---

# Is there prime-specific critical pair geometry after fixed-count dependent-spacing and endpoint-phase calibration?

## Observation

The critical coherence-cell branch has progressively quotiented the obvious representation and null-model confounds. `VIS-227`--`VIS-236` calibrate occupancy, heterogeneous/Markov effects, and the degeneracy of controls that ignore the actual monotone ordered-point support. `VIS-237` removes arbitrary grid origin by identifying the triangular short-range pair functional. `VIS-238` removes Poisson count noise, and `VIS-239` separates an independently specified one-point intensity from the dependence question.

`VIS-240` supplies a nontrivial representation-matched dependence family: symmetric cyclic Dirichlet gaps with fixed count, uniform one-point intensity after random rotation, monotone ordered support, and a predeclared parameter `alpha` controlling spacing dependence. Its tent-statistic mean is exact. `VIS-241` then removes the arbitrary phase introduced by cutting the stationary circle into an interval: for endpoint phase treated as nuisance, the intrinsic statistic is

`bar T=sum_(i<j) (1-delta_ij/ell)_+(1-delta_ij/L)`.

`VIS-242` closes the remaining mathematical variance gap. Under symmetric Dirichlet gaps, `Var_G(bar T)` is exactly a finite sum over cyclic-arc overlap classes, each term an at-most-four-component Dirichlet expectation. At `alpha=1`, where the model is exactly iid uniform points on the circle, the variance collapses to the closed benchmark

`Var(bar T)=binom(m,2)[2u/3-4u^2/3+11u^3/15-u^4/9]`, `u=ell/L`.

The live question is therefore no longer how to construct or calibrate this null in principle. It is whether the frozen prime-coordinate configuration has a residual after applying the now explicit representation-matched calibration without tuning the null on the confirmation statistic.

## Research question

Fix the critical `lambda` family, midpoint-symmetric taper, phase/coherence tolerance, point-coordinate normalization, width rule, endpoint convention, statistic, and dependence model before confirmation. Choose `alpha` from theory, independent data, or a fitting procedure whose uncertainty is carried into the null rather than from the same `bar T` value being tested.

Under that frozen specification, does the prime-coordinate `bar T` exhibit a stable residual relative to the symmetric-Dirichlet overlap-class mean/variance calibration of `VIS-240` and `VIS-242` across increasing scales? If endpoints are declared physical signal rather than nuisance, use the post-cut statistic and add the exact `E_G[V_cut]` channel from `VIS-241` instead of switching conventions after observing the result.

If a residual survives, can it also survive a stronger predeclared spacing control and then be translated into a lower bound, obstruction, or structural constraint for the signed prime-phase quadratic energy rather than remaining a generic point-process anomaly?

## Why it may matter

The branch has removed forced occupancy, count fluctuation, specified one-point intensity, arbitrary grid origin, support-mismatched label randomization, a nontrivial spacing-dependence axis, and arbitrary endpoint cut phase. `VIS-242` additionally removes the excuse that the dependent null lacks a mathematically controlled variance.

A residual that now disappears under a frozen symmetric-Dirichlet calibration is generic spacing dependence, not prime-specific structure. A residual that survives is still far below an RH result, but it would have passed a materially stronger representation-matched null and would justify asking whether the surviving statistic couples to the signed arithmetic kernel rather than merely to local point geometry.

## Decisive test

Before examining the confirmation residual, freeze all representation choices and the `alpha` rule. Evaluate the exact overlap-class calibration from `VIS-242`; at `alpha=1`, require agreement with its closed polynomial variance as an implementation audit. For `alpha!=1`, evaluate the finite Dirichlet overlap terms by deterministic quadrature or an independently validated numerical method, with numerical error materially below the proposed residual scale.

Compare the predeclared prime statistic against this calibration across increasing scales without retuning `alpha`, `ell`, the endpoint convention, or the statistic. If `alpha` is estimated from independent data, propagate that estimation uncertainty rather than conditioning on a point estimate silently.

Kill the candidate if the anomaly disappears under the frozen dependence calibration; if it depends on Poisson count noise, same-sample intensity flattening, random-cut phase declared to be nuisance, or post-hoc tuning; if significance is unstable across the predeclared scale family; or if a stronger representation-matched spacing control reproduces the effect.

Only after a stable residual survives should a new mathematical thread translate it back through the signed prime-phase kernel and audit equivalent formulations in logarithmic prime gaps, short-interval counts, prime-pair/higher-correlation statistics, and critical Dirichlet-polynomial theory.

## Evidence boundary

`VIS-237`--`VIS-241` establish the representation quotients and the symmetric-Dirichlet dependence family. `VIS-242` establishes an exact finite-sample variance reduction for the endpoint-quotiented statistic and a closed `alpha=1` benchmark. None of these findings chooses a prime-appropriate `alpha`, establishes that the one-parameter Dirichlet family is a faithful final model of prime gaps, or reports a prime residual.

No cited result establishes prime-specific critical separation or any RH consequence. A future empirical residual would remain a calibrated point-process observation until an independent mathematical bridge connects it to the signed prime-phase object.

## Research disposition

The clue remains `accepted`. Its former variance-calibration bottleneck is closed by `VIS-242`. The current frontier is now a separate confirmation problem: freeze the null and representation choices independently, evaluate the exact calibration, and test whether a stable prime residual survives before opening any new arithmetic interpretation.