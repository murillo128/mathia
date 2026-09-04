---
id: CLUE-visual-exploration-zeta-three-gap-conditional-residual
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/clues/CLUE-zeta-critical-strip-multiscale-geometry.md
  - research/visual_exploration/findings/VIS-019-raw-adjacent-gap-geometry-finite-size-rmt-baseline.md
  - research/visual_exploration/findings/VIS-020-three-gap-markov-closure-maxent-information-baseline.md
  - research/visual_exploration/SOURCES.md
---

# Does an adjacent-pair-marginal-preserving three-gap residual expose zeta-specific higher-order structure?

## Observation

`VIS-019` closes every visual observable determined only by one or two consecutive unfolded gaps unless the finite-size CUE/arithmetic baseline is removed. The accepted multiscale clue explicitly leaves three-or-more-gap organization as a live channel, but raw higher-order spacing statistics are themselves established random-matrix objects. A sharper object is therefore the part of a three-gap joint law not determined by its two overlapping adjacent-pair marginals.

For a fixed finite partition of unfolded gaps, write `P3(i,j,k) = P(G_{n-1} in i, G_n in j, G_{n+1} in k)`, with adjacent-pair marginals `P12(i,j)`, `P23(j,k)` and middle marginal `P2(j)`. The first-order Markov closure carrying those two pair marginals is `Q(i,j,k) = P12(i,j) P23(j,k) / P2(j)` wherever `P2(j) > 0`. Thus `Delta = P3 - Q` isolates coarse three-gap conditional dependence beyond the adjacent two-gap marginals.

`VIS-020` sharpens this from a convenient construction to an exact information-theoretic baseline: `Q` is the unique maximum-entropy completion of the two adjacent-pair marginals, and

`D(P3 || Q) = I(G_{n-1}; G_{n+1} | G_n) = H(Q)-H(P3)`.

The residual tensor localizes the departure while conditional mutual information supplies its canonical nonnegative scalar information distance for the chosen partition.

## Research question

For high unfolded zeta zeros near height `T`, does the residual tensor `Delta_T`, or a stable scalar/function derived from it, differ from the corresponding finite-size CUE or sine-kernel-plus-arithmetic baseline after the known one-gap and two-gap laws are matched? Is any surviving difference stable across partitions, unfoldings, disjoint windows, and multiple heights, with a coherent effective-size scaling?

The target is not nonzero `Delta` itself: CUE has higher-order determinantal dependence and need not be first-order Markov in its gap sequence. The candidate signal is the **zeta-minus-matched-RMT residual of the conditional-dependence residual**.

## Why it may matter

This is one of the smallest information channels that genuinely lies beyond `VIS-019`. It removes the two overlapping adjacent-pair marginals algebraically before searching for geometry, rather than comparing a raw three-gap cloud with Poisson or infinite-size random-matrix theory. `VIS-020` also shows that the removal is canonical in a precise maximum-entropy/KL sense for the chosen finite partition.

If a reproducible excess survives finite-size CUE and known arithmetic corrections, it would localize candidate arithmetic information at irreducible three-gap order. If it does not, it closes the next natural extension of the adjacent-gap visual program.

## Decisive test

Use large high-zero windows at several heights for which finite-size baselines are meaningful. Pre-register a small family of stable partitions or a continuous estimator. In each window, unfold locally, estimate `P3`, `P12`, `P23`, and `P2`, form that window's own maximum-entropy closure `Q`, and compute both `Delta=P3-Q` and `I=D(P3||Q)`.

Apply the same construction separately to `CUE_{N_e(T)}` and, where available, the finite-height Riemann-kernel/arithmetic correction rather than a Poisson or shuffled-gap control. Compare the zeta-minus-control scalar excess and the full residual shape with multiplicity-aware uncertainty. Repeat with estimator/bin perturbations and disjoint windows.

Keep the direction only if a zeta-minus-baseline residual reproduces across heights/windows and cannot be explained by finite-sample bias, unfolding drift, known higher-order random-matrix spacing statistics, or the arithmetic correction already encoded in the established kernel expansion. Kill it if the residual agrees with the matched determinantal baseline or if the apparent structure is a partition, finite-size, or unfolding artifact.

## Evidence boundary

The Markov-closure/max-entropy identity is classical probability and information theory, not a new theorem; its exact specialization is persisted in `VIS-020`. Higher-order consecutive-spacing correlations are established random-matrix prior art. No new arithmetic signal, asymptotic scaling, or RH criterion is established here.

This clue proposes a controlled residualization test designed to remove the exact lower-order channel closed by `VIS-019`. Its accepted status means the question has survived scope, mathematical-coherence, and baseline/prior-art triage; it does not assert that a zeta-specific residual exists.

## Research disposition

Accepted as a live experiment after the exact baseline audit in `VIS-020`. The unresolved question is now sharply isolated: whether high zeta zeros have reproducible conditional-dependence information beyond the corresponding matched finite-size CUE/arithmetic process after each side is projected against its own adjacent-pair-preserving maximum-entropy closure.