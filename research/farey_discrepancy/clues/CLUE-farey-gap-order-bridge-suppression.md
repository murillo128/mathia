---
id: CLUE-farey-discrepancy-gap-order-bridge-suppression
type: research-clue
status: proposed
origin: research-watch
target_line: farey_discrepancy
based_on:
  - research/visual_exploration/findings/VIS-026-gap-permutation-discrepancy-bridge-covariance.md
  - research/visual_exploration/findings/VIS-027-farey-reflection-dirichlet-mode-filter.md
  - research/farey_discrepancy/README.md
---

# Does Farey ordering suppress discrepancy through a genuinely multiscale mechanism beyond the fixed gap multiset and reflection symmetry?

## Observation

`VIS-026` gives an exact matched control for any ordered point set: uniformly permuting a fixed gap multiset makes the cumulative grid discrepancy a finite-population bridge with covariance

`Cov(D_k,D_l)=sigma_g^2 min(k,l)[N-max(k,l)]/(N-1)`

and exact mean squared energy `sigma_g^2 N(N+1)/6`.

For Farey order `n=100`, the actual squared grid-discrepancy energy is only about `0.0235` of that unrestricted same-gap permutation mean. The same finite diagnostic stays below one across the tested orders `n=20,30,...,300`, with no asymptotic fit imposed. This holds every gap size fixed and therefore localizes the observed cancellation to ordering information.

`VIS-027` removes an important representation artifact from that comparison. Farey reflection `x_(N-k)=1-x_k` makes the gap vector palindromic and the discrepancy path antisymmetric, so every odd Dirichlet sine mode vanishes identically. A spectral picture of the missing odd modes is therefore forced symmetry, not arithmetic evidence.

Conditioning the same-gap permutation null on that exact reflection symmetry still gives an elementary finite baseline:

`E_sym[E_2] = sigma_g^2 N(N+2)/12`.

At `n=100`, the actual Farey energy is about `0.04698` of this stronger symmetry-preserving null. Across `n=20,30,40,60,80,100,120,150,200,250,300`, the corresponding finite ratios are approximately

`0.30161, 0.18693, 0.12932, 0.08563, 0.06438, 0.04698, 0.03931, 0.03063, 0.02432, 0.01703, 0.01403`.

Thus exact reflection symmetry explains the obvious odd-mode deletion but does not exhaust the observed finite ordering suppression.

Rogelio Tomás García's 2026 Farey-discrepancy work independently identifies gap ordering as important for `L^1` average local discrepancy and studies the same family of fixed-gap permutations. The exact unrestricted and reflection-conditioned controls sharpen the second-order baseline but do not explain the arithmetic ordering.

## Research question

Can the Farey suppression relative to the **reflection-preserving same-gap** control be decomposed into an explicit multiscale or denominator-stratified ordering invariant that is not already determined by the classical Franel–Landau discrepancy, a familiar Möbius summatory quantity, or a bounded amount of local gap-adjacency data?

In Dirichlet spectral coordinates, the trivial parity channel is now removed exactly. After conditioning progressively on the gap multiset, reflection symmetry, adjacent gap-pair counts, and natural denominator/mediant strata, is there a residual coupling among the surviving even modes whose contribution to squared discrepancy can be written exactly and estimated at the RH-critical scale?

## Why it may matter

The Farey mandate asks specifically whether geometric or multiscale information survives after the classical scalar discrepancy is formed. The permutation controls give two clean quotients. Gap sizes alone predict a much larger second-order discrepancy than the deterministic Farey order realizes, and exact left-right reflection removes only the easiest spectral artifact while leaving a large residual suppression at the tested orders.

If a small exact collection of local ordering statistics explains the remaining suppression, the visual effect is not a new channel and the branch can be narrowed. If substantial suppression remains only in cross-scale or denominator-mediated coupling among the surviving modes, that isolates a concrete structure worth relating to Franel–Landau and Möbius cancellation.

## Decisive test

Use a fixed multiscale decomposition, preferably the exact Dirichlet sine/Green decomposition from `VIS-027` or a predeclared dyadic/Haar equivalent, and compare the Farey ordering against a hierarchy of matched controls in this order: fixed gap multiset; fixed gap multiset plus exact reflection symmetry; then additional controls preserving adjacent pair counts, bounded-depth local blocks, or a predeclared denominator/mediant stratification.

Do **not** count the vanished odd Dirichlet modes as a signal: they are deterministically forced by reflection. On the surviving even modes, derive how much quadratic discrepancy energy is fixed by each admitted lower-order statistic and test whether a reproducible residual remains across Farey orders.

Keep the direction only if the residual admits an exact arithmetic description not algebraically equivalent to the existing scalar discrepancy or a familiar Möbius estimate. Kill or hand off the route if the suppression is exhausted by reflection/local adjacency/stratum statistics, or if the modal decomposition merely repackages the Franel scalar with no independently controllable cross-scale relation.

## Evidence boundary

The unrestricted bridge covariance and permutation-mean `L^2` energy are established in `VIS-026`. The Dirichlet spectral decomposition, odd-mode reflection filter, and exact reflection-preserving permutation mean are established in `VIS-027`. The displayed Farey ratios are reproducible finite evaluations for the stated orders.

None of these establishes an asymptotic law, an RH implication, or a new Farey theorem about the cause of the suppression. The clue asks which mathematical structure remains after the known symmetry and same-gap controls are removed; it does not treat the declining finite-order ratios or low-frequency spectral appearance as evidence of a new RH mechanism.
