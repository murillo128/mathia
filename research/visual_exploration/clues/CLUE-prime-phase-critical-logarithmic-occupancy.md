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

`VIS-236` closes that exact-type escape for the **actual coherence-cell representation**. The cells inherited from `VIS-225` are ordered intervals in prime coordinate, and the primes are listed increasingly, so their cell labels are nondecreasing. Every occupied cell is one contiguous run. Hence

`T_2=sum_j (N_j-2)_+`,

and the actual endpoint-matched transition table has a singleton realization. Its `VIS-234` PGF is always a monomial. A generic Euler-trail/Markov-type randomization therefore either has no freedom on the actual table or, if enlarged to create revisits, leaves the support of the ordered prime-coordinate representation.

`VIS-237` removes one nuisance without leaving that support: average the equal-width interval grid over a uniform origin shift while keeping the ordered source points fixed. For any ordered points `x_1<...<x_m` and cell width `ell`, the exact origin-averaged collision count is

`(1/ell) integral_0^ell S(U)dU`
` = sum_(a<b) (1-|x_b-x_a|/ell)_+`.

Thus cell-origin averaging is a representation-matched control, but it is not a new independent null family. It quotients the arbitrary grid phase and reduces the statistic exactly to a triangular/tent-weighted short-range pair-gap functional. Cell-origin robustness can therefore be handled analytically; the remaining source of freedom is the ordered point configuration itself.

`VIS-238` now separates a further null-model choice that is leading-order at the critical scale. For the tent pair functional, an unconditioned homogeneous Poisson process has critical variance

`lambda(kappa/3+kappa^2)+O(1)`,

where `lambda` is the expected point count and `kappa=lambda ell/L=Theta(1)`, while a fixed-count uniform sample with `m` points has

`m kappa/3+O(1)`.

The extra Poisson term `lambda kappa^2` is exactly the leading count-fluctuation channel exposed by conditioning on the Poisson total count. Since the prime configuration at fixed `y` already has a fixed observed number of points, a scalar geometry test should not mistake this global-count fluctuation for uncertainty in the short-gap geometry.

The live issue is therefore narrower: after quotienting grid origin and removing the leading count-randomness confound, how should the remaining local pair-gap geometry be calibrated without conditioning away the tested quantity?

## Research question

At fixed critical `lambda`, after choosing a dependence model independently of confirmation data and matching the support of the ordered prime-coordinate construction, does the prime system exhibit a stable residual that is not explained by generic local intensity and short-gap fluctuations?

The most direct surviving route is the origin-invariant triangular pair functional exposed by `VIS-237`, now calibrated at minimum against the fixed-count uniform order-statistic baseline of `VIS-238`, or against a stronger fixed-count monotone model that also represents admitted nonuniform intensity or short-gap structure. Can one predeclare such a model/statistic, calibrate its finite-sample center and covariance without conditioning away the statistic, and find a residual that survives increasing scales?

If a residual survives, can it be translated into a lower bound, obstruction, or structural constraint for the signed prime-phase quadratic energy rather than remaining a generic point-process anomaly?

## Why it may matter

The branch has separated forced finite occupancy, independent occupancy noise, one-point heterogeneity, serial dependence, conditioning sigma-field, representation support, grid-origin nuisance, and now total-count randomization. `VIS-236` shows that a statistically nondegenerate null is not automatically admissible if it creates paths the underlying geometry cannot realize. `VIS-237` shows that grid translation can be quotiented exactly. `VIS-238` shows that even a geometrically admissible Poisson point-process null can inject a separate leading variance channel if it randomizes a total count that is fixed in the observed source configuration.

This materially narrows the search. Future controls should spend complexity on the actual source of freedom — local intensity, prime gaps, run occupancies, and within-cell geometry — rather than arbitrary label permutations, repeated grid-origin scans, or unconditioned count noise. A surviving signal under such a control would be substantially more informative; failure would close the critical cell route without mistaking representation or null-model variability for arithmetic structure.

## Decisive test

Freeze the midpoint-symmetric taper, phase/coherence tolerance, the critical `lambda` family, the inherited cell-width rule, the statistic, and the null family before inspecting confirmation outcomes.

Do **not** use the exact endpoint-matched first-order Markov-type law of `VIS-234` as the confirmation null for the ordered prime-coordinate cell labels. `VIS-236` proves that the actual type class is a singleton and that `T_2` is already determined by occupancies.

Do **not** treat a sweep over cell origins as multiple independent evidence channels. `VIS-237` gives the exact origin average. For the scalar collision route, use the origin-invariant triangular pair-gap functional directly unless an origin-specific deviation has a separately predeclared mathematical role.

Do **not** use an unconditioned homogeneous Poisson process as the sole scalar confirmation null when the intended question conditions on the observed number of source points. `VIS-238` proves that Poisson count randomness contributes a leading `Theta(m)` variance term at critical occupancy. The fixed-count uniform order-statistic model is the minimal homogeneous baseline for the geometric statistic, not a claim that uniform points are a faithful prime model.

Choose one stronger representation-matched ordered-point control before confirmation if the homogeneous fixed-count baseline is intentionally insufficient. A natural next candidate is a fixed-count nonhomogeneous or gap-based model whose realizations remain increasing and whose center/covariance for the triangular functional accounts for the admitted local intensity and short-gap law. Another admissible route is a weaker conditional control on counts/gaps that leaves the predeclared statistic nondegenerate.

For any proposed control, verify first that the statistic varies inside its admitted sample space and that the control does not condition on sufficient information for that statistic. Then calibrate its center/covariance or exact conditional law as appropriate, and test the confirmation residual without retuning `lambda`, width, coordinate, or null.

Kill a candidate if its anomaly disappears under the monotone matched control, if it is determined by preserved occupancy/gap data, if the claimed origin robustness is only repeated measurement of the `VIS-237` triangular functional, if its significance depends on the extra Poisson count-fluctuation variance isolated by `VIS-238`, or if the null gains apparent power only by permitting label revisits/backtracking impossible for the prime-coordinate cells.

Only after a residual survives these gates should it be translated back through the signed phase kernel. Before promotion to a prime-specific finding, audit equivalent formulations in logarithmic prime gaps, short-interval counts, renewal/point-process controls, prime-pair or higher-correlation statistics, and the relevant critical Dirichlet-polynomial literature.

## Evidence boundary

`VIS-227`--`VIS-231` establish deterministic, independent, heterogeneous and Markov baselines for cell collisions. `VIS-232` establishes the conditioning degeneracy of `S`. `VIS-233`--`VIS-235` correctly describe generic endpoint-matched Markov types and show that lag-two pattern information can escape first-order counts in that larger combinatorial class.

`VIS-236` establishes that the specific ordered prime-coordinate coherence cells occupy a much smaller support: the label sequence is monotone, `T_2` is an occupancy functional, and the actual first-order type class is a singleton. It therefore refutes the planned exact-type `T_2` confirmation route for this representation, not the general combinatorics of `VIS-233`--`VIS-235`.

`VIS-237` establishes an exact representation-matched quotient for the grid origin: the mean same-cell collision count is a triangular pair-gap functional. It does **not** establish a faithful stochastic model for prime gaps/counts, a nonzero prime residual relative to such a model, or any independence gained by origin averaging.

`VIS-238` establishes exact finite-window mean/variance formulas for that tent statistic under fixed-count uniform and homogeneous Poisson point models, and shows that Poissonization adds a leading critical count-fluctuation variance channel. It does **not** establish that the fixed-count uniform model is a faithful final null for primes or that any prime residual remains after such conditioning.

None of these results establishes prime-specific critical separation, a faithful confirmation null for the ordered prime process, or any RH consequence.

## Research disposition

The clue remains `accepted`, but its live route is narrower. The generic exact Markov-type branch is closed for the actual monotone labels by `VIS-236`; grid-origin nuisance is reduced exactly by `VIS-237`; and `VIS-238` removes unconditioned Poisson count fluctuation as a clean source of scalar significance when the observed point count is fixed. The next useful test should operate directly on representation-matched monotone point geometry and compare the tent statistic against a predeclared **fixed-count** ordered-point null that accounts for whichever local intensity or short-gap structure is intentionally admitted.