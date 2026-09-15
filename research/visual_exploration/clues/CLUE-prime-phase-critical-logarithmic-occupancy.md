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
---

# Is there prime-specific critical phase-cell structure after dependent occupancy calibration?

## Observation

`VIS-225` obtains a strict-subcritical worst-start lower bound by partitioning primes in `(y/2,y]` into phase-coherent cells of width `eta_v y/(8H)`. `VIS-226` closes the strict-subcritical worst-start scale through a finite phase-net scan, leaving the critical scale `H=lambda y/log y` outside that argument.

`VIS-227` shows that at critical scale the raw same-cell collision count

`S_lambda(y)=sum_j binom(n_j,2)`

has an exact deterministic floor forced solely by fitting `m` points into `J` cells. `VIS-228` removes the next false positive: under independent uniform allocation with the same `m` and `J`, an extensive excess above that floor is generic.

`VIS-229` removes a further representation mismatch. For independent categorical cell probabilities `(p_j)`, with

`q_2=sum_j p_j^2`, `q_3=sum_j p_j^3`,

the exact null is

`E[S]=binom(m,2)q_2`,

`Var(S)=binom(m,2)(q_2-q_2^2)+6binom(m,3)(q_3-q_2^2)`.

The term `q_3-q_2^2=Var(p_X)` is already positive under independent sampling whenever the one-point cell law is nonuniform. Thus neither the uniform center nor the uniform variance is an admissible arithmetic baseline once the intended control has unequal cell probabilities.

`VIS-230` now removes the assumption that matching this one-point law also centers a dependent control. For a stationary Markov cell process with stationary law `pi` and lag return probabilities

`c_r=P(X_0=X_r)=sum_i pi_i(P^r)_(ii)`,

the exact collision center is

`E[S]=sum_(r=1)^(m-1)(m-r)c_r`,

not `binom(m,2)q_2` unless all `c_r=q_2`. For a finite ergodic chain the difference from the independent center is `mA-B+o(1)`, where `A=sum_(r>=1)(c_r-q_2)`. Ordinary serial recurrence can therefore create an extensive residual even when the marginal cell law is matched perfectly.

## Research question

For fixed critical `lambda`, after fixing both a mathematically justified one-point cell law and an admitted dependence model independently of the confirmation statistic, does the actual prime system exhibit a stable collision residual beyond the center and covariance of that dependent control?

For a stationary first-order Markov surrogate, the center must use the full lag-return profile from `VIS-230`. What is the corresponding dependent covariance of `S_lambda`, and does a predeclared standardized residual remain non-generic across increasing scales and reasonable fixed cell-origin perturbations once that covariance is calibrated?

If pair collisions become generic under a logarithmic-gap or short-interval preserving control, is there a genuinely different phase-cell observable — multiscale occupancy persistence, nearest-neighbor phase crowding, or a direction-sensitive kernel statistic — that remains non-generic and can be translated into a critical-scale lower bound for the full prime-phase quadratic energy?

## Why it may matter

The deterministic floor, the uniform multinomial baseline, the nonuniform categorical baseline, and the exact Markov centering formula remove four increasingly strong sources of false arithmetic structure. A surviving residual after dependent calibration would isolate information not explained by cell geometry, marginal occupancy, or ordinary serial recurrence.

That is still not enough for the prime-phase objective: the surviving dependence must eventually couple with the signed phase kernel rather than merely produce a scalar occupancy anomaly. Failure at either stage would close pair collisions as a useful critical discriminator and redirect the search toward observables that retain more of the interaction geometry.

## Decisive test

Fix the taper, phase tolerance, cell-origin convention, a finite set of `lambda` values, the primary collision statistic, and the rule selecting the null family before inspecting confirmation outcomes. The one-point law and dependence parameters should come from an analytic model, an independently frozen calibration range, or another construction whose uncertainty can be carried into the test.

For an independent categorical null, use the exact `VIS-229` center and variance. For a stationary first-order Markov null with the same one-point law, replace the center by the exact `VIS-230` lag-return sum. Do not call a residual prime-specific merely because it is separated from `binom(m,2)q_2`; that separation can be generated entirely by ordinary Markov recurrence.

The next mathematical gate is the dependent covariance. Derive or independently calibrate the variance of `S_lambda` under the admitted gap-preserving/Markov-like control, including covariance between overlapping and separated pair indicators. Freeze that standardization before confirmation. Require any candidate separation to persist under reasonable fixed cell-origin perturbations and across the predeclared `lambda` family.

Only if this residual survives should it be translated back through the signed phase kernel. Kill the pair-collision route if the residual is explained by the calibrated dependent control, is unstable under allowed representation perturbations, or cannot be connected to the signed phase energy. Any successor statistic must be genuinely different rather than another monotone renormalization of `S_lambda`.

Before promotion to a prime-specific finding, audit equivalent formulations in logarithmic-scale prime gaps, short-interval counts, occupancy/U-statistic models for dependent sequences, Markov/renewal controls, and prime-pair statistics.

## Evidence boundary

`VIS-227` establishes the deterministic occupancy floor. `VIS-228` establishes the exact uniform independent mean/variance and proves that extensive excess above the floor is generic. `VIS-229` establishes the exact nonuniform independent mean/variance and shows that one-point heterogeneity contributes a third-moment covariance term even without pair dependence. `VIS-230` establishes that stationary Markov dependence changes the collision center through the full lag-return profile even when the stationary one-point law is unchanged.

None of these results establishes the dependent variance for a prime-relevant control, the behavior of the actual prime residual after that calibration, any critical-scale optimizer separation, or any RH consequence.

## Research disposition

The clue is accepted for continued investigation. The current unresolved question is no longer whether one-point calibration suffices; `VIS-230` rules that out for dependent controls. The next coherent gate is to calibrate the collision covariance under an admitted dependence model and only then test whether a prime residual survives.