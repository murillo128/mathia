---
id: CLUE-visual-exploration-prime-phase-critical-logarithmic-occupancy
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-225-coherent-prime-blocks-force-divergent-ising-scale.md
  - research/visual_exploration/findings/VIS-226-finite-phase-net-scan-controls-subcritical-worst-start.md
  - research/visual_exploration/findings/VIS-227-critical-phase-cell-collisions-have-balanced-occupancy-floor.md
  - research/visual_exploration/findings/VIS-228-multinomial-cell-collisions-have-extensive-excess-above-balanced-floor.md
  - research/visual_exploration/findings/VIS-229-nonuniform-categorical-cell-collisions-have-third-moment-variance.md
---

# Is there prime-specific critical phase-cell structure after one-point occupancy calibration?

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

## Research question

For fixed critical `lambda`, after fixing a mathematically justified one-point cell law `(p_j)` independently of the confirmation statistic, does the actual prime system exhibit a stable residual

`Z_(lambda,p)(y)`
` = [S_lambda-binom(m,2)q_2]`
`   / sqrt[binom(m,2)(q_2-q_2^2)+6binom(m,3)(q_3-q_2^2)]`

that is non-generic across increasing scales and reasonable fixed cell-origin perturbations?

If such a residual survives the independent categorical null, does it also survive controls that preserve logarithmic-scale gap or short-interval structure and therefore introduce genuine dependence between cell labels? If pair collisions become generic under those stronger controls, is there a genuinely different phase-cell observable — multiscale occupancy persistence, nearest-neighbor phase crowding, or a direction-sensitive kernel statistic — that remains non-generic and can be translated into a critical-scale lower bound for the full prime-phase quadratic energy?

## Why it may matter

The deterministic floor, the uniform multinomial baseline, and the nonuniform categorical baseline remove three increasingly strong sources of false arithmetic structure. A surviving residual after one-point calibration would isolate dependence not explained by cell geometry or marginal occupancy alone.

That is still not enough for the prime-phase objective: the surviving dependence must eventually couple with the signed phase kernel rather than merely produce a scalar occupancy anomaly. Failure at either stage would close pair collisions as a useful critical discriminator and redirect the search toward observables that retain more of the interaction geometry.

## Decisive test

Fix the taper, phase tolerance, cell-origin convention, a finite set of `lambda` values, the primary collision statistic, and the rule determining `(p_j)` before inspecting confirmation outcomes. The one-point law should come from an analytic model, an independently frozen calibration range, or another construction whose uncertainty can be carried into the test; do not estimate `(p_j)` from the same confirmation occupancies and then treat the fixed-`p` variance in `VIS-229` as exact.

For each growing confirmation scale, form the `VIS-225` critical cells at `H=lambda y/log y`, compute `(m,J,S_lambda)`, and evaluate the exact independent-categorical center and variance from `VIS-229`. Require any candidate separation to persist under reasonable fixed cell-origin perturbations and across the predeclared `lambda` family.

Only if this residual survives should the control be strengthened to preserve logarithmic-scale gaps, short-interval counts, or another admitted local dependence structure. Such a control needs its own calibrated center and covariance; the independent-categorical formula is not valid after dependence is imposed. The claim survives only if a predeclared residual remains separated and can be translated back through the phase kernel without importing the desired critical lower bound through the control assumptions.

Kill the pair-collision route if the residual is explained by the calibrated one-point law, disappears under a structurally matched dependent control, is unstable under allowed representation perturbations, or cannot be connected to the signed phase energy. Any successor statistic must be genuinely different rather than another monotone renormalization of `S_lambda`.

Before promotion to a prime-specific finding, audit equivalent formulations in logarithmic-scale prime gaps, short-interval counts, occupancy/U-statistic models, and prime-pair statistics.

## Evidence boundary

`VIS-227` establishes the deterministic occupancy floor. `VIS-228` establishes the exact uniform independent mean/variance and proves that extensive excess above the floor is generic. `VIS-229` establishes the exact nonuniform independent mean/variance and shows that one-point heterogeneity contributes a third-moment covariance term even without pair dependence.

None of these results establishes the behavior of the actual prime residual after calibrated one-point removal, the effect of a gap-preserving dependent control, any critical-scale optimizer separation, or any RH consequence. This clue therefore remains `status: proposed`; the unresolved object is dependence beyond an independently specified one-point occupancy law and its relevance to the signed critical phase Hamiltonian.