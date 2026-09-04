---
id: CLUE-farey-discrepancy-gap-order-bridge-suppression
type: research-clue
status: proposed
origin: research-watch
target_line: farey_discrepancy
based_on:
  - research/visual_exploration/findings/VIS-026-gap-permutation-discrepancy-bridge-covariance.md
  - research/farey_discrepancy/README.md
---

# Does Farey ordering suppress discrepancy through a genuinely multiscale mechanism beyond the fixed gap multiset?

## Observation

`VIS-026` gives an exact matched control for any ordered point set: uniformly permuting a fixed gap multiset makes the cumulative grid discrepancy a finite-population bridge with covariance

`Cov(D_k,D_l)=sigma_g^2 min(k,l)[N-max(k,l)]/(N-1)`

and exact mean squared energy `sigma_g^2 N(N+1)/6`.

For Farey order `n=100`, the actual squared grid-discrepancy energy is only about `0.0235` of that same-gap permutation mean. The same finite diagnostic stays below one across the tested orders `n=20,30,...,300`, with no asymptotic fit imposed. This holds every gap size fixed and therefore localizes the observed cancellation to **ordering information**.

Rogelio Tomás García's 2026 Farey-discrepancy work independently identifies gap ordering as important for `L^1` average local discrepancy and studies the same family of fixed-gap permutations. The exact bridge control sharpens the second-order baseline but does not explain the arithmetic ordering.

## Research question

Can the Farey suppression relative to the exact same-gap permutation bridge be decomposed into an explicit multiscale or denominator-stratified ordering invariant that is not already determined by the classical Franel–Landau discrepancy, a familiar Möbius summatory quantity, or a bounded amount of local gap-adjacency data?

In particular, after conditioning progressively on the gap multiset, adjacent gap-pair counts, and natural denominator/mediant strata, is there a residual cross-scale coupling whose contribution to squared discrepancy can be written exactly and estimated at the RH-critical scale?

## Why it may matter

The Farey mandate asks specifically whether geometric or multiscale information survives after the classical scalar discrepancy is formed. The permutation bridge gives a clean first quotient: gap sizes alone predict a much larger second-order discrepancy than the deterministic Farey order realizes at the tested finite orders.

If a small exact collection of local ordering statistics explains the suppression, the visual effect is not a new channel and the branch can be narrowed. If substantial suppression remains only in cross-scale coupling, that isolates a concrete structure worth relating to Franel–Landau and Möbius cancellation.

## Decisive test

Write the squared discrepancy as the exact quadratic form in centered ordered gaps and choose a fixed multiscale decomposition, for example dyadic/Haar blocks or denominator strata, before examining favorable Farey patterns. Derive how much of the quadratic energy is determined successively by: the unordered gap multiset; adjacent gap-pair counts; bounded-depth local blocks; and the chosen denominator/mediant stratification.

Compare the actual Farey value with matched permutations constrained to preserve each admitted lower-order statistic. Keep the direction only if a residual contribution remains reproducibly nontrivial across orders and admits an exact arithmetic description that is not algebraically equivalent to the existing scalar discrepancy or a familiar Möbius estimate. Kill or hand off the route if the suppression is exhausted by local adjacency/stratum statistics or collapses exactly to known Franel–Landau/Möbius structure.

## Evidence boundary

The exact bridge covariance and permutation-mean `L^2` energy are established in `VIS-026`; the finite Farey suppression is a reproducible numerical observation for the displayed orders. Neither establishes an asymptotic law, an RH implication, or a new Farey theorem.

The clue asks what mathematical structure causes the ordering effect. It does not treat the declining finite-order ratio or Brownian-bridge terminology as evidence of a new RH mechanism.
