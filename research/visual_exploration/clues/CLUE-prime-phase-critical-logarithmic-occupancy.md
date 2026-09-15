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

`VIS-231` closes the finite-sample covariance gate for any specified stationary finite-state Markov null. Squaring `S` and classifying two collision indicators by whether their index pairs overlap or are disjoint gives an exact variance in terms of three-time coincidence probabilities and the three possible four-time pair-pair probabilities. In the rank-one iid chain this formula reduces exactly to `VIS-229`.

`VIS-232` adds the model-admission obstruction. The scalar collision statistic is exactly

`S=sum_j binom(N_j,2)`,

so it depends only on the confirmation-sample occupancy histogram. Conditioning on the exact `N_j` makes `S` deterministic. Preserving the full first-order transition-count matrix plus an endpoint also fixes every `N_j`; for a non-balanced transition type the matrix already determines the endpoints. Thus an exact transition-count-preserving or block-reordering surrogate cannot serve as a stronger nondegenerate null for `S`: it conditions away the statistic rather than calibrating it.

Therefore the unresolved issue is now narrower. A useful dependent control for `S` must be stochastic at the confirmation occupancy level — for example parameters fitted from independent calibration data — or the statistic itself must become order-sensitive if exact realized local structure is to be preserved.

## Research question

For fixed critical `lambda`, after choosing a dependence control independently of the confirmation statistic and without conditioning away the occupancy variation measured by `S`, does the actual prime system exhibit a stable collision residual beyond that control's calibrated center and covariance?

If a stationary first-order Markov surrogate is justified from a frozen calibration range or an analytic local model, use the exact `VIS-230` center and `VIS-231` variance and propagate parameter-estimation uncertainty. Does the resulting predeclared residual remain non-generic across increasing scales and reasonable fixed cell-origin perturbations?

If the scientifically necessary control must preserve realized transition counts, logarithmic-gap blocks, or other local structure that fixes the occupancy histogram, replace `S` by a genuinely order-sensitive observable that varies inside that conditional class. Can such an observable remain non-generic and still be translated into a critical-scale lower bound for the full prime-phase quadratic energy?

## Why it may matter

The deterministic floor, independent uniform baseline, nonuniform categorical baseline, Markov centering, exact Markov covariance, and now the conditional-degeneracy obstruction remove six increasingly strong sources of false arithmetic structure or circular control design. A surviving residual under a genuinely predeclared stochastic dependence model would isolate information not explained by cell geometry, marginal occupancy, ordinary serial recurrence, or the covariance induced by that recurrence.

That is still not enough for the prime-phase objective: the surviving dependence must eventually couple with the signed phase kernel rather than merely produce a scalar occupancy anomaly. If credible controls require conditioning on realized local structure, the branch must switch to an order-sensitive statistic instead of trying to rescue `S` by increasingly restrictive randomization.

## Decisive test

Fix the taper, phase tolerance, cell-origin convention, a finite set of `lambda` values, the primary statistic, and the rule selecting the null family before inspecting confirmation outcomes.

For the scalar collision statistic `S`, do **not** condition the confirmation null on the exact occupancy histogram or on endpoint-matched exact transition counts; `VIS-232` proves that these controls make `S` degenerate. Estimate any stochastic null parameters from an analytic model, an independently frozen calibration range, or another source that leaves confirmation occupancies random. For an independent categorical null use `VIS-229`; for a stationary first-order Markov null use the exact `VIS-230` center and `VIS-231` variance. If `pi,P` are estimated rather than fixed, propagate that estimation uncertainty rather than treating the plug-in moments as exact, and do not infer Gaussianity merely from the exact second moment.

If the admitted control must preserve exact confirmation-sample transitions or blocks, predeclare an order-sensitive replacement statistic and verify that it is not measurable from the preserved summary. Freeze the surrogate and statistic before confirmation, then require any candidate separation to persist under reasonable fixed cell-origin perturbations and across the predeclared `lambda` family.

Only if a residual survives should it be translated back through the signed phase kernel. Kill the scalar pair-collision route if the residual is explained by the calibrated stochastic control, is unstable under allowed representation perturbations, or credible model admission requires conditioning on information that already determines `S`. Any successor statistic must be genuinely different rather than another monotone renormalization of `S_lambda`.

Before promotion to a prime-specific finding, audit equivalent formulations in logarithmic-scale prime gaps, short-interval counts, occupancy/U-statistic models for dependent sequences, Markov/renewal controls, conditional randomization, and prime-pair statistics.

## Evidence boundary

`VIS-227` establishes the deterministic occupancy floor. `VIS-228` establishes the exact uniform independent mean/variance and proves that extensive excess above the floor is generic. `VIS-229` establishes the exact nonuniform independent mean/variance. `VIS-230` establishes the exact stationary-Markov collision center. `VIS-231` establishes the exact stationary finite-state Markov collision variance through three- and four-time joint probabilities and recovers `VIS-229` as the iid special case. `VIS-232` establishes that `S` is occupancy-measurable and becomes degenerate under exact histogram conditioning or endpoint-matched exact transition-count conditioning.

None of these results establishes a faithful prime dependence model, the behavior of the actual prime residual after a frozen stochastic calibration, a central limit theorem for the chosen null, a successful order-sensitive replacement statistic, any critical-scale optimizer separation, or any RH consequence.

## Research disposition

The clue remains accepted. The next scalar-collision gate is no longer to invent a stronger conditional shuffle: exact occupancy or transition-type preservation is circular for `S`. The live route is an independently calibrated stochastic dependence model with confirmation occupancies left random. If that is scientifically too weak, the branch should move to an order-sensitive statistic that remains nondegenerate under the stronger realized local-structure control.