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
---

# Is there prime-specific critical cell structure after a representation-matched dependence calibration?

## Observation

`VIS-225` and `VIS-226` close the strictly subcritical symmetric-taper worst-start scale and leave the critical transition

`H=lambda y/log y`

as a genuinely different regime. `VIS-227`--`VIS-231` then remove progressively stronger false positives for the critical same-cell collision statistic

`S_lambda(y)=sum_j binom(N_j,2)`:

the deterministic balanced-occupancy floor, independent uniform occupancy, nonuniform categorical occupancy, and stationary first-order Markov centering/covariance all contribute macroscopic structure that must be calibrated before any residual is called arithmetic.

`VIS-232` shows that conditioning on the realized occupancy histogram fixes `S`, and preserving exact first-order transition counts plus an endpoint also fixes those occupancies. `VIS-233`--`VIS-235` explored a generic escape: the lag-two return

`T_2=sum_(t=1)^(m-2) 1_(x_t=x_(t+2))`

can vary inside an arbitrary endpoint-matched first-order Markov type; its complete conditional law has an exact recursion and its mean has a cheaper two-step-deletion formula.

`VIS-236` now closes that exact-type escape for the **actual coherence-cell representation**. The cells inherited from `VIS-225` are ordered intervals in prime coordinate, and the primes are listed increasingly, so their cell labels are nondecreasing. Every occupied cell is one contiguous run. Hence

`T_2=sum_j (N_j-2)_+`,

and the actual endpoint-matched transition table has a singleton realization. Its `VIS-234` PGF is always a monomial. A generic Euler-trail/Markov-type randomization therefore either has no freedom on the actual table or, if enlarged to create revisits, leaves the support of the ordered prime-coordinate representation.

The remaining issue is no longer how to find a higher-order label statistic that escapes the same conditional table. It is how to calibrate dependence **without destroying the monotone geometry that defines the cells**.

## Research question

At fixed critical `lambda`, after choosing a dependence model independently of confirmation data and matching the support of the ordered prime-coordinate construction, does the prime system exhibit a stable residual that is not explained by generic occupancy/gap fluctuations?

The most direct surviving route is to model a genuinely variable monotone object: cell occupancies/counts, normalized prime gaps, within-cell point positions, or another increasing-point-process statistic. Can one predeclare such a model/statistic, calibrate its finite-sample center and covariance without conditioning away the tested quantity, and find a residual that survives increasing scales and reasonable fixed cell-origin perturbations?

If a residual survives, can it be translated into a lower bound, obstruction, or structural constraint for the signed prime-phase quadratic energy rather than remaining a generic point-process anomaly?

## Why it may matter

The branch has now separated several notions that were easy to conflate: forced finite occupancy, independent occupancy noise, one-point heterogeneity, serial dependence, conditioning sigma-field, and representation support. `VIS-236` adds a decisive compatibility check: a statistically nondegenerate null is not automatically admissible if it creates paths the underlying geometric representation cannot realize.

This materially narrows the search. The exact first-order-type / lag-two-label branch no longer needs numerical implementation. Future controls should spend complexity on the actual source of freedom — prime gaps and run occupancies inside an increasing point process — rather than on arbitrary permutations of cell labels. A surviving signal under such a control would be substantially more informative; failure would close the critical cell route without mistaking null-model freedom for arithmetic structure.

## Decisive test

Freeze the midpoint-symmetric taper, phase/coherence tolerance, cell-origin convention, a finite set of critical `lambda` values, the statistic, and the null family before inspecting confirmation outcomes.

Do **not** use the exact endpoint-matched first-order Markov-type law of `VIS-234` as the confirmation null for the ordered prime-coordinate cell labels. `VIS-236` proves that the actual type class is a singleton and that `T_2` is already determined by occupancies.

Instead choose one representation-matched monotone control before confirmation. Two admissible examples are:

- an independently calibrated stochastic model for the ordered cell-count/gap process that generates new occupancies while preserving the increasing-point support; or
- a conditional control on a weaker summary of gaps/counts that leaves the predeclared confirmation statistic nondegenerate and whose realizations remain increasing point configurations.

For any proposed control, verify first that the statistic varies inside its admitted sample space and that the control does not condition on sufficient counts for the statistic. Then freeze the finite `lambda`/cell-origin family jointly, calibrate center/covariance or an exact conditional law as appropriate, and test the confirmation residual without retuning the representation.

Kill a candidate if its anomaly disappears under the monotone matched control, if it is determined by the preserved occupancy/run data, if it is unstable under allowed cell-origin perturbations, or if the null gains apparent power only by permitting label revisits/backtracking impossible for the prime-coordinate cells.

Only after a residual survives these gates should it be translated back through the signed phase kernel. Before promotion to a prime-specific finding, audit equivalent formulations in logarithmic prime gaps, short-interval counts, renewal/point-process controls, prime-pair or higher-correlation statistics, and the relevant critical Dirichlet-polynomial literature.

## Evidence boundary

`VIS-227`--`VIS-231` establish deterministic, independent, heterogeneous and Markov baselines for cell collisions. `VIS-232` establishes the conditioning degeneracy of `S`. `VIS-233`--`VIS-235` correctly describe generic endpoint-matched Markov types and show that lag-two pattern information can escape first-order counts in that larger combinatorial class.

`VIS-236` establishes that the specific ordered prime-coordinate coherence cells occupy a much smaller support: the label sequence is monotone, `T_2` is an occupancy functional, and the actual first-order type class is a singleton. It therefore refutes the planned exact-type `T_2` confirmation route for this representation, not the general combinatorics of `VIS-233`--`VIS-235`.

None of these results establishes a faithful monotone stochastic model for prime gaps/counts, a nonzero prime residual under such a frozen model, representation-stable critical separation, or any RH consequence.

## Research disposition

The clue remains `accepted`, but its live route is narrowed. The generic exact Markov-type calibration branch is resolved negatively by `VIS-236` and should not be instantiated numerically on the actual cell labels. The next useful test must operate on a representation-matched monotone object — occupancies, gaps, within-cell positions, or another increasing-point-process statistic — and must prove its own nondegeneracy before confirmation. The independently calibrated stochastic collision route remains possible only to the extent that its generated support and dependence assumptions are explicitly justified rather than inherited from an arbitrary categorical Markov chain.