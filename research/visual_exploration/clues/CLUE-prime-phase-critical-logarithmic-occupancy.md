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

`VIS-230` removes the assumption that matching this one-point law also centers a dependent control. For a stationary Markov cell process with stationary law `pi` and lag return probabilities

`c_r=P(X_0=X_r)=sum_i pi_i(P^r)_(ii)`,

the exact collision center is

`E[S]=sum_(r=1)^(m-1)(m-r)c_r`,

not `binom(m,2)q_2` unless all `c_r=q_2`. For a finite ergodic chain the difference from the independent center is `mA-B+o(1)`, where `A=sum_(r>=1)(c_r-q_2)`.

`VIS-231` now closes the finite-sample covariance gate for any specified stationary finite-state Markov null. Squaring `S` and classifying two collision indicators by whether their index pairs overlap or are disjoint gives an exact variance in terms of three-time coincidence probabilities and the three possible four-time pair-pair probabilities. In the rank-one iid chain this formula reduces exactly to `VIS-229`.

Therefore a first-order Markov surrogate with fixed `pi,P` has no remaining centering-or-variance ambiguity: its collision residual can be standardized exactly. The unresolved issue is whether that surrogate is the right admitted dependence control for the prime construction, not how to compute its finite-sample covariance.

## Research question

For fixed critical `lambda`, after choosing a dependence control independently of the confirmation statistic, does the actual prime system exhibit a stable collision residual beyond that control's calibrated center and covariance?

If a stationary first-order Markov surrogate is justified from a frozen calibration range or an analytic local model, use the exact `VIS-230` center and `VIS-231` variance. Does the resulting predeclared residual remain non-generic across increasing scales and reasonable fixed cell-origin perturbations after parameter-estimation uncertainty is accounted for?

If first-order Markov structure is not an honest approximation to the intended logarithmic-gap or short-interval preserving control, what is the weakest stronger surrogate — renewal, higher-order Markov, block-preserving, or another explicit mechanism — that preserves the admitted local dependence without importing the critical-scale conclusion being tested?

If pair collisions become generic under that stronger control, is there a genuinely different phase-cell observable — multiscale occupancy persistence, nearest-neighbor phase crowding, or a direction-sensitive kernel statistic — that remains non-generic and can be translated into a critical-scale lower bound for the full prime-phase quadratic energy?

## Why it may matter

The deterministic floor, independent uniform baseline, nonuniform categorical baseline, Markov centering, and now exact Markov covariance remove five increasingly strong sources of false arithmetic structure. A surviving residual after a genuinely predeclared dependent calibration would isolate information not explained by cell geometry, marginal occupancy, ordinary serial recurrence, or the covariance induced by that recurrence.

That is still not enough for the prime-phase objective: the surviving dependence must eventually couple with the signed phase kernel rather than merely produce a scalar occupancy anomaly. Failure at either stage would close pair collisions as a useful critical discriminator and redirect the search toward observables that retain more of the interaction geometry.

## Decisive test

Fix the taper, phase tolerance, cell-origin convention, a finite set of `lambda` values, the primary collision statistic, and the rule selecting the null family before inspecting confirmation outcomes. The one-point law and dependence parameters must come from an analytic model, an independently frozen calibration range, or another construction whose uncertainty can be carried into the test.

For an independent categorical null, use `VIS-229`. For a stationary first-order Markov null, use the exact `VIS-230` center and `VIS-231` variance; do not substitute the independent variance and do not infer Gaussianity merely from having an exact second moment. If `pi,P` are estimated rather than fixed, propagate that estimation uncertainty rather than treating the plug-in center and variance as exact.

The next coherent gate is **model admission**. Specify what prime-local information the surrogate is allowed to preserve — for example one-step phase-cell transitions, logarithmic-gap bins, or short-interval counts — and why that control does not already encode the critical-scale collision behavior being tested. Freeze the surrogate construction before confirmation and require any candidate separation to persist under reasonable fixed cell-origin perturbations and across the predeclared `lambda` family.

Only if this residual survives should it be translated back through the signed phase kernel. Kill the pair-collision route if the residual is explained by the calibrated dependent control, is unstable under allowed representation perturbations, or cannot be connected to the signed phase energy. Any successor statistic must be genuinely different rather than another monotone renormalization of `S_lambda`.

Before promotion to a prime-specific finding, audit equivalent formulations in logarithmic-scale prime gaps, short-interval counts, occupancy/U-statistic models for dependent sequences, Markov/renewal controls, and prime-pair statistics.

## Evidence boundary

`VIS-227` establishes the deterministic occupancy floor. `VIS-228` establishes the exact uniform independent mean/variance and proves that extensive excess above the floor is generic. `VIS-229` establishes the exact nonuniform independent mean/variance. `VIS-230` establishes the exact stationary-Markov collision center. `VIS-231` establishes the exact stationary finite-state Markov collision variance through three- and four-time joint probabilities and recovers `VIS-229` as the iid special case.

None of these results establishes that first-order Markov dependence is a faithful prime control, the behavior of the actual prime residual after a frozen dependent calibration, a central limit theorem for the chosen null, any critical-scale optimizer separation, or any RH consequence.

## Research disposition

The clue remains accepted. The dependent moment calculation is no longer the bottleneck for a specified first-order Markov null. The next research question is to define and justify the admitted dependent surrogate independently of confirmation, including parameter-estimation uncertainty, and then test whether any prime-specific standardized collision residual survives.