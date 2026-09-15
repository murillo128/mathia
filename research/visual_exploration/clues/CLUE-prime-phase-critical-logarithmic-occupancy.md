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
---

# Is there prime-specific critical phase-cell structure after stochastic occupancy calibration?

## Observation

`VIS-225` obtains a strict-subcritical worst-start lower bound by partitioning primes in `(y/2,y]` into phase-coherent cells of width `eta_v y/(8H)`. `VIS-226` closes the strict-subcritical worst-start scale through a finite phase-net scan, leaving the critical scale `H=lambda y/log y` outside that argument.

`VIS-227` shows that at critical scale the raw same-cell collision count

`S_lambda(y)=sum_j binom(n_j,2)`

has an exact deterministic floor `S_min(m,J)` forced solely by fitting `m` points into `J` cells. `VIS-228` now removes the next false positive: under independent uniform allocation with the same `m` and `J`,

`E[S]=binom(m,2)/J`,

`Var(S)=binom(m,2)(1/J)(1-1/J)`,

and `E[S-S_min]=Theta(J)` whenever `m/J` tends to a positive constant. Thus even a positive linear excess above the balanced floor is generic under the simplest stochastic occupancy null.

The pair-count question therefore begins only after stochastic centering. For nonuniform independent cell probabilities `p_j`, even the null mean changes to `binom(m,2) sum_j p_j^2`, so the intended one-point occupancy law must be part of the control rather than assumed away.

## Research question

For fixed critical `lambda`, does the actual prime system exhibit a stable non-generic residual after centering the phase-cell statistic against a matched stochastic occupancy model that preserves the same `m`, `J`, cell geometry, and intended one-point density?

For pair collisions, the preliminary equal-cell statistic is

`Z_lambda(y) = [S_lambda-binom(m,2)/J] / sqrt[binom(m,2)(1/J)(1-1/J)]`.

Does an analogous centered statistic survive fixed cell-origin perturbations and stronger logarithmic-gap controls? If pair collisions become generic after those controls, is there a different phase-cell observable — multiscale occupancy persistence, nearest-neighbor phase crowding, or a direction-sensitive kernel statistic — that remains non-generic and can be translated into a critical-scale lower bound for the full prime-phase quadratic energy?

## Why it may matter

The deterministic floor and the multinomial mean are two different baselines. Removing both prevents ordinary balls-in-cells geometry and ordinary random collision fluctuations from being mistaken for prime arithmetic. A surviving, representation-stable residual would therefore have a clearer claim to encode logarithmic-scale prime organization not already supplied by one-point density or independent occupancy.

Failure would also be useful: it would close pair-collision occupancy as a critical discriminator and force the search toward observables that retain information discarded by the cell-count representation.

## Decisive test

Fix the taper, phase tolerance, cell-origin convention, a finite set of `lambda` values, and the primary statistic before inspecting confirmation data. For each growing `y`, form exactly the `VIS-225` coherence cells at `H=lambda y/log y`, record `m`, `J`, and `(n_j)`, and first compare `S_lambda` with the exact independent equal-cell mean/variance from `VIS-228`.

Then replace the equal-cell null by controls that preserve the actual one-point cell probabilities or logarithmic-scale gap information while keeping the same declared geometry. The claim survives only if a predeclared centered statistic remains separated across increasing scales and reasonable fixed cell-origin perturbations, and if the surviving excess can be translated back through the phase kernel without importing the desired critical lower bound through the control assumptions.

Kill the pair-collision route if its centered residual is generic under the matched controls, unstable under allowed representation perturbations, or explained by statistics already fixed by the null. If that happens, any successor statistic must be genuinely different rather than another monotone renormalization of `S_lambda`.

Before promotion to a finding, audit equivalent formulations in logarithmic-scale prime gaps, short-interval counts, occupancy models, and prime-pair statistics.

## Evidence boundary

`VIS-227` establishes the deterministic occupancy floor. `VIS-228` establishes the exact independent-allocation mean/variance and proves that extensive excess above that floor is still generic. Neither result establishes the behavior of the actual prime residual under a matched stochastic control, any critical-scale optimizer separation, or any RH consequence. This clue therefore remains `status: proposed`; the unresolved object is a control-stable residual after stochastic occupancy calibration.