---
id: CLUE-robin-extremal-extremal-exchange-discretization-budget
type: research-clue
status: proposed
origin: master-researcher
target_line: robin_extremal
based_on:
  - research/robin_extremal/README.md
  - research/robin_extremal/SOURCES.md
  - research/prior_art/robin-criterion.md
  - research/arithmetic_fidelity/findings/AF-054-maximal-safe-target-envelope-under-isometric-refinement.md
---

# Can exact prime-exponent exchanges control the discrete error in a Robin extremal relaxation?

## Observation

The Robin mandate identifies a concrete gap between a continuous exponent optimization and the discrete prime-supported maximizers of `sigma(n)/(n log log n)`. A smooth optimum does not bound the original functional unless the relaxation and its rounding error preserve the exact target inequality.

Arithmetic Fidelity's AF-054 provides a relevant methodological constraint: even an isometric refinement can change distance to a target if the refined target admits realizations that do not descend. Its safe-envelope theorem is metric and does not prove anything about Robin extrema, but motivates auditing the admissible discrete target before using a continuous relaxation.

## Research question

Within a literature-justified extremal family, can exact single-prime increments and two-prime exponent exchanges yield a uniform restriction on potential counterexample profiles, after the complete `log log n` normalization and rounding costs are retained?

## Why it may matter

A restriction valid for an infinite family would be a first structural result beyond finite verification. It could distinguish a useful variational mechanism from a relaxation that recovers only the classical maximal-order law.

## Decisive test

First verify the precise theorem permitting restriction to the selected extremal family. Write `L=log n` and the exact change of `log(sigma(n)/n)-log(log L)` under one admissible exponent increment or exchange, keeping all terms. Derive which continuous optimum, if any, bounds the same discrete objective and which rounding/exchange defects accumulate.

Choose one resulting restriction and prove it uniformly on a stated infinite range, or construct admissible exponent profiles that defeat it despite satisfying the known extremal constraints. Compare with synthetic prime-like sequences only under a clearly stated transport of the extremal hypotheses and target functional. Finally audit the prime-distribution estimate needed for the sign: an RH-strength error assumption would not explain Robin's inequality. Rediscovering standard ordering of exponents or colossally abundant reductions is a prior-art outcome, not the desired new restriction.

## Evidence boundary

No monotone potential, new extremal reduction, or bound for Robin's functional is established. A synthetic sequence without the relevant extremal hypotheses is not a counterexample to the arithmetic theorem, and an apparent continuous margin cannot absorb an unbounded discretization error by assumption.
