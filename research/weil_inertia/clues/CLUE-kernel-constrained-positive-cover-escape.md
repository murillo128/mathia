---
id: CLUE-weil-inertia-kernel-constrained-positive-cover-escape
type: research-clue
status: proposed
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/weil_inertia/clues/CLUE-four-point-weighted-cover-assembly.md
  - research/weil_inertia/findings/WI-166-four-point-positive-cover-relaxation-is-sharp.md
---

# Can a source-constrained cover evade the sharp positive-cover relaxation?

## Observation

WI-166 closes the arbitrary nonnegative pair-weight/gap relaxation behind the four-point positive-cover program: coefficientwise pair-energy domination admits an exact witness that makes the relaxation sharp. The resolved cover clue explicitly leaves only escapes that retain structure discarded by that relaxation, such as the actual Montgomery--Taylor kernel, Gram/PSD coupling, or another source-derived arithmetic constraint.

## Research question

Does the source problem impose a concrete kernel, Gram/PSD, placement, or arithmetic compatibility condition that excludes the WI-166 extremal witness and permits a strictly stronger domination or defect bound before scalarization?

## Why it may matter

This is the precise remaining question after the positive-cover optimization itself has been exhausted. A positive answer would identify the extra information needed for a genuine improvement; a negative answer would show that another cover parametrization cannot improve the RH-facing bound without stronger arithmetic input.

## Decisive test

Freeze the smallest exact constrained cover class inherited from the source rather than adding free weights. Prove the retained kernel/PSD/arithmetic constraints and test whether the WI-166 witness is realizable in that class. If it is not, derive an exact strengthened domination inequality or dual certificate and propagate the gain through the complete finite assembly. If it is realizable, or if the proposed constraint disappears under the normalization actually used by the zeta argument, close that escape.

Keep a finite matrix/semidefinite certificate separate from its zeta instantiation and analytic limit. Any claimed numerical improvement must account for every pair-energy and pressure contribution without double spending.

## Evidence boundary

No constrained improvement is established. WI-166 is sharp only for its stated relaxed class; this clue does not weaken that theorem. The existence of a Gram or kernel representation by itself is not extra information unless the source proves restrictions that exclude the sharp witness and survive the downstream assembly.