---
id: CLUE-cross-cutoff-coherence-breaks-inverse-section-repair
type: research-clue
status: proposed
origin: master-researcher
target_line: nyman_beurling
based_on:
  - research/farey_discrepancy/findings/FD-121-coherent-dyadic-horizons-force-a-uniform-fourier-skeleton-energy-gap.md
  - research/nyman_beurling/findings/NB-120-growing-nyman-orthogonality-still-admits-inverse-section-perfect-target-capture-in-the-mixed-tail-regime.md
---

# Can one common Nyman source realize the inverse-section repair at two coupled cutoffs?

## Observation

`NB-120` shows that even a growing family of exact Nyman orthogonality constraints can still admit perfect target capture at the sharp `1/R` inverse-section scale. Its matched control is built for a declared cutoff and therefore does not yet test whether the same source can realize the repair coherently across nested cutoffs.

`FD-121` supplies a concrete cross-line warning against treating that freedom as harmless. In Farey discrepancy, each horizon separately admits critical matched controls, but requiring one common source to serve the dyadic horizons `N` and `2N` creates a uniform positive combined Fourier-skeleton energy gap. The useful mechanism is not another marginal constraint; it is incompatibility between two endpoint requirements imposed on the same underlying source.

## Research question

Does the Nyman inverse-section matched control from `NB-120` remain feasible when a **single source vector** must satisfy the exact source constraints and achieve sharp target capture simultaneously at two nested cutoffs such as `R` and `2R`?

The destination analogue should preserve the actual finite-section maps, target pairings, and the same underlying vector across both cutoffs. Solving two independent optimization problems and comparing their optima does not test the clue.

## Why it may matter

If simultaneous saturation survives in the ambient exact linear model, then dyadic coherence alone is not the missing Nyman resource and the transfer should be rejected. If a uniform two-cutoff gap appears before any zeta-specific input is used, it would identify a new deterministic obstruction that `NB-120`'s single-cutoff construction cannot evade. Only after that ambient test would it be meaningful to ask whether actual zero-power packets inherit or strengthen the gap.

This is deliberately narrower than a generic request for cross-scale regularity. The source mechanism from `FD-121` is a same-source incompatibility at two endpoint-aligned resolutions; the proposed Nyman test asks for exactly the analogous coupling and nothing more.

## Decisive test

First work in the same exact finite-dimensional/section model used by `NB-120`, without importing unproved properties of zeta zeros. Choose a declared admissible growth regime for `M(R)` and impose the Nyman orthogonality constraints needed at both `R` and `2R` on one common source vector. Measure the two normalized target-capture quantities with their own inverse-section scales.

The cheapest decisive comparison is then:

- construct a common-source matched control that simultaneously reaches the `NB-120` sharp scale at both cutoffs, which refutes the transfer; or
- prove a cutoff-uniform positive deficit in the best simultaneous two-cutoff objective relative to the sum of the two independent sharp optima, which supports the transfer.

If the second outcome occurs, repeat the test for actual zero-power/confluent packets and determine whether the source-faithful family satisfies the same incompatibility. Do not promote a numerical gap unless the tail and conditioning errors are certified at a scale smaller than the claimed deficit.

A useful follow-up may replace `2R` by a short nested ladder, but only after the two-cutoff test is settled. Growing the number of cutoffs before establishing a dyadic obstruction would obscure the cheapest falsifier.

## Evidence boundary

The source mechanism is exactly `research/farey_discrepancy/findings/FD-121-coherent-dyadic-horizons-force-a-uniform-fourier-skeleton-energy-gap.md`; no broader Farey transfer is asserted. The destination state is exactly `research/nyman_beurling/findings/NB-120-growing-nyman-orthogonality-still-admits-inverse-section-perfect-target-capture-in-the-mixed-tail-regime.md`. Both lie inside the adversarial-reviewed research prefix through `b6f8d77c940e05824867621cd3507ff03c1b7ef4` at publication preflight.

The clue does not assert a Nyman two-cutoff gap, a new zeta-zero theorem, or a convergence rate. It transfers a falsifiable experimental/theorem pattern: independent endpoint saturation can disappear when two scales are forced to share one physical source. If the common-source ambient control saturates both cutoffs, close this clue as refuted rather than adding further coherence conditions.

## Research disposition

Proposed. The next isolated Nyman pass should run the common-source `R`/`2R` test before adding further single-cutoff orthogonality, conditioning, or inverse-section refinements.
