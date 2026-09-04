---
id: CLUE-visual-exploration-zeta-three-gap-conditional-residual
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/clues/CLUE-zeta-critical-strip-multiscale-geometry.md
  - research/visual_exploration/findings/VIS-019-raw-adjacent-gap-geometry-finite-size-rmt-baseline.md
  - research/visual_exploration/SOURCES.md
---

# Does an adjacent-pair-marginal-preserving three-gap residual expose zeta-specific higher-order structure?

## Observation

`VIS-019` closes every visual observable determined only by one or two consecutive unfolded gaps unless the finite-size CUE/arithmetic baseline is removed. The accepted multiscale clue explicitly leaves three-or-more-gap organization as a live channel, but raw higher-order spacing ratios are themselves established random-matrix objects. A sharper object is therefore the part of a three-gap joint law not determined by its two overlapping adjacent-pair marginals.

For a fixed finite partition of unfolded gaps, write `P3(i,j,k) = P(G_{n-1} in i, G_n in j, G_{n+1} in k)`, with adjacent-pair marginals `P12(i,j)`, `P23(j,k)` and middle marginal `P2(j)`. The first-order Markov closure carrying those two pair marginals is `Q(i,j,k) = P12(i,j) P23(j,k) / P2(j)` wherever `P2(j) > 0`. Thus `Delta = P3 - Q` isolates coarse three-gap conditional dependence beyond the adjacent two-gap marginals. Equivalently, conditional mutual information `I(G_{n-1}; G_{n+1} | G_n)` vanishes at this Markov closure.

## Research question

For high unfolded zeta zeros near height `T`, does the residual tensor `Delta_T`, or a stable scalar/function derived from it, differ from the corresponding finite-size CUE or sine-kernel-plus-arithmetic baseline after the known one-gap and two-gap laws are matched? Is any surviving difference stable across partitions, unfoldings, disjoint windows, and multiple heights, with a coherent effective-size scaling?

The target is not nonzero `Delta` itself: CUE has higher-order determinantal dependence and need not be first-order Markov in its gap sequence. The candidate signal is the **zeta-minus-matched-RMT residual of the conditional-dependence residual**.

## Why it may matter

This is one of the smallest information channels that genuinely lies beyond `VIS-019`. It removes the two overlapping adjacent-pair marginals algebraically before searching for geometry, rather than comparing a raw three-gap cloud with Poisson or infinite-size random-matrix theory. If a reproducible excess survives finite-size CUE and known arithmetic corrections, it would localize candidate arithmetic information at irreducible three-gap order. If it does not, it closes the next natural extension of the adjacent-gap visual program.

## Decisive test

Use large high-zero windows at several heights for which finite-size baselines are meaningful. Pre-register a small family of stable partitions or a continuous estimator. In each window, unfold locally, estimate `P3`, `P12`, `P23`, and `P2`, form `Q` and `Delta`, and compare against `CUE_{N_e(T)}` and, where available, the finite-height Riemann-kernel/arithmetic correction rather than a Poisson or shuffled-gap control. Repeat with estimator/bin perturbations and disjoint windows, and compare both a scalar conditional-mutual-information excess and the full residual shape with multiplicity-aware uncertainty.

Keep the direction only if a zeta-minus-baseline residual reproduces across heights/windows and cannot be explained by finite-sample bias, unfolding drift, known higher-order spacing-ratio/random-matrix statistics, or the arithmetic correction already encoded in the established kernel expansion. Kill it if the residual agrees with the matched determinantal baseline or if the apparent structure is a partition, finite-size, or unfolding artifact.

## Evidence boundary

The Markov-closure identity is elementary probability/information-theory structure, not a new theorem. Higher-order spacing ratios and higher-order random-matrix statistics are established prior art. No new arithmetic signal, asymptotic scaling, or RH criterion is established here. This clue proposes a controlled residualization test designed to remove the exact lower-order channel closed by `VIS-019`; it remains speculative until tested on high-zero data against the correct finite-size/arithmetic baseline.
