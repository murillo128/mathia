---
id: CLUE-weil-inertia-four-point-weighted-cover-assembly
type: research-clue
status: accepted
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-011-refined-four-point-envelope-improves-certified-bound.md
  - research/weil_inertia/formalization/WI011TraceEnergy.lean
  - research/weil_inertia/formalization/WI011FourPointAssembly.lean
  - research/weil_inertia/findings/WI-164-schur-normalization-cancels-horizontal-collapse.md
---

# Is the certified four-point input better assembled by a nonuniform positive block cover?

## Observation

WI-011 combines the external four-point certificate `F_4>=231/100000`, span-pressure coefficient `1/2500`, a trace--energy envelope, and exact shifted-block accounting. Its displayed choice `m=438` yields the assembled proportion `0.672852563956780847...`. The local Lean files check finite envelope/counting components; they do not by themselves instantiate the complete analytic zeta theorem with the external certificate.

This is a concrete surviving quantitative channel. In contrast, WI-164 shows that normalized Schur cancellation equals `K_V K_V^*` and can vanish on a genuinely off-line pair, so that particular operator normalization does not supply an automatic new charge for horizontal collapse.

## Research question

With the same proved four-point certificate and arithmetic inputs, can a positive cover using different block lengths or source-dependent placement improve the final bound, or is uniform shifted-block accounting optimal in a precisely delimited cover class?

## Why it may matter

Either an improved finite assembly or an exact dual ceiling would convert the strongest existing numerical deduction into a sharper, closed mathematical result. It would distinguish an avoidable bookkeeping loss from the need for a genuinely stronger local certificate or analytic input.

## Decisive test

Define the admissible covers before optimization. Track every pair-energy coefficient and every span-pressure charge; overlapping blocks may not spend the same Gram defect twice. Require an exact domination inequality replacing WI-011's pinching/shift average whenever a proposed cover leaves that argument's hypotheses.

First test a finite two-length family against arbitrary nonnegative pair weights and gaps, as in the existing finite Lean statements. Derive the resulting bound symbolically, including endpoints and the passage to zeta. Either give an exact certificate strictly above the WI-011 benchmark or a dual witness proving a ceiling for this cover class. Adaptive placement must earn its advantage under the same unconditional information, not assume inaccessible gap statistics. An end-to-end formal instantiation would validate a successful assembly but is not itself the new mathematical question.

## Evidence boundary

No better constant or global optimality theorem is claimed. Failure of a two-length test would not prove optimality over all covers. The external local certificate, finite assembly, analytic limit, and numerical evaluation remain separate obligations; this clue does not revive the resolved Schur-cancellation route.

## Research disposition

The first, post-collapse two-length branch is closed exactly by [[research/weil_inertia/findings/WI-165-positive-mixtures-of-fixed-block-bounds-cannot-beat-best-constituent.md]]: any fixed geometry-independent nonnegative combination of already-scalarized block inequalities is a convex combination of the constituent ratios and cannot beat the best constituent. The clue remains active because this obstruction does not cover placement or weighting chosen before scalar collapse. The surviving question is whether a geometry-aware positive cover can exploit complementary local Gram entries or span information while proving a new universal domination inequality that is not merely a positive sum of separately averaged block bounds.