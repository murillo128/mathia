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
---

# Is there prime-specific excess above the critical phase-cell occupancy floor?

## Observation

`VIS-225` obtains a strict-subcritical worst-start lower bound by partitioning primes in `(y/2,y]` into phase-coherent frequency cells of width `eta_v y/(8H)`. Below `H~y/log y`, coarse density forces many same-cell prime pairs. `VIS-226` separately resolves the strict-subcritical worst-start asymptotic through a finite phase-net scan, leaving the critical scale `H=lambda y/log y` outside that argument.

`VIS-227` sharpens what happens to the coherent-block certificate exactly at that boundary. If `m` primes occupy `J` coherence cells and `m=qJ+r`, then the raw pair count

`S_lambda(y)=sum_j binom(n_j,2)`

has the exact representation-free floor

`S_min(m,J)=J binom(q,2)+rq`.

At `H=lambda y/log y`, one has `m/J -> eta_v/(8lambda)`. Consequently, `Theta(1)` mean occupancy does not uniformly mean that coarse forcing has disappeared. For `lambda<eta_v/8`, occupancy alone already forces a positive linear raw collision count; for `lambda>eta_v/8`, the exact balanced floor is eventually zero; at the transition, first-order asymptotics force no positive linear floor. Raw same-cell mass is therefore not the right arithmetic discriminator across the whole critical family.

## Research question

After removing the exact finite balanced-occupancy floor, does the true prime system exhibit a stable positive excess

`S_lambda(y)-S_min(m,J)`

for any fixed range of `lambda`, beyond what is produced by matched logarithmic-gap controls with the same `m` and `J`?

If pair-count excess is not discriminating, is there another phase-cell statistic — for example multiscale occupancy variance, nearest-neighbor phase crowding, or persistence of dense cells across nearby `t` — that survives an appropriate matched control and can be translated into a critical-scale lower bound for the full prime-phase quadratic energy?

## Why it may matter

The exact occupancy floor removes a generic combinatorial source of apparent critical clustering before prime arithmetic enters. This leaves a cleaner question: whether logarithmic-scale prime geometry contributes **excess organization** beyond the minimum forced by fitting `m` points into `J` cells.

A positive, control-stable excess would identify arithmetic information not supplied by the one-point density mechanism used in `VIS-225`. Failure would close an attractive route without confusing a balls-in-cells constraint with prime-specific phase coherence.

## Decisive test

Fix the taper, phase tolerance, and a finite set of `lambda` values before inspecting outcomes, including values on both sides of `eta_v/8`. For each growing `y`, form exactly the `VIS-225` coherence cells at `H=lambda y/log y`, record `m`, `J`, and the occupancies `(n_j)`, and compute the exact finite baseline `S_min(m,J)` from `m=qJ+r`.

Compare the excess `S_lambda-S_min` with matched controls conditioned on the same `m` and `J` and preserving the intended one-point density; use stronger controls only if the first comparison leaves a stable signal. Pre-register at least one statistic beyond raw pair count if testing multiscale persistence. A useful positive result must survive the control and then admit a rigorous translation back through the phase kernel. Kill the route if the excess is asymptotically generic, unstable under fixed cell-origin/phase perturbations allowed by the construction, or explained by already-imposed occupancy information.

Before promoting any surviving arithmetic excess to a finding, audit equivalent formulations in logarithmic-scale prime gaps, short-interval counts, occupancy models, and prime-pair statistics.

## Evidence boundary

`VIS-227` establishes only the exact combinatorial floor and its critical-scale specialization. It does not establish any positive prime-specific excess, control separation, critical worst-start divergence, or RH consequence. `VIS-225` and `VIS-226` remain strict-subcritical results. This clue therefore remains `status: proposed`; the unresolved object is the excess above the forced finite occupancy baseline, not the raw collision count.