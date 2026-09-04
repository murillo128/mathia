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

The exact even-mode coordinates from `VIS-027` expose a more specific finite pattern. Write `m=2r`, let

`V_n = 2M sigma_g^2/(M-1)`

be the exact reflection-preserving null variance of each surviving normalized edge mode `a_(2r)`, and define cumulative actual and null Green energies

`A_n(K) = sum_(r<=K) a_(2r)^2/lambda_(2r)`,

`B_n(K) = V_n sum_(r<=K) 1/lambda_(2r)`.

The normalized cumulative spectral shape

`Phi_n(K) = [A_n(K)/E_2] / [B_n(K)/E_sym[E_2]]`

removes the already-known total suppression and asks only where, by mode scale, the remaining Farey energy sits relative to the exact reflection null.

Direct finite evaluation for Farey orders `n=100,150,200,300,400,600` gives a strikingly similar profile when `K` is scaled as `K ~= x n`. Across those six orders, `Phi_n(floor(x n))` lies approximately in the ranges

- `0.44–0.51` at `x=0.25`;
- `0.65–0.69` at `x=0.5`;
- `0.79–0.82` at `x=1`;
- `0.88–0.91` at `x=2`.

Over the same orders the total ratio `E_2/E_sym[E_2]` changes substantially, from about `0.04698` at `n=100` to `0.00636` at `n=600`, so the displayed agreement concerns the **shape across surviving modes**, not a hidden normalization of the total energy.

As a matched finite control, `150` uniform first-half gap permutations with exact mirroring at `n=200` keep the same gap multiset and reflection symmetry but destroy the Farey ordering. Their `10–90%` range for `Phi_n` is approximately `0.976–1.006` at `x=0.25`, `0.989–1.003` at `x=0.5`, and `0.995–1.002` at `x=1`, rather than the Farey values near `0.51`, `0.69`, and `0.82`. In the unaccumulated edge-mode power, the same finite data show depletion relative to the null at the lowest normalized modes and compensating excess at mesoscopic modes.

Rogelio Tomás García's 2026 Farey-discrepancy work independently identifies gap ordering as important for `L^1` average local discrepancy and studies the same family of fixed-gap permutations. The exact unrestricted and reflection-conditioned controls sharpen the second-order baseline but do not explain the arithmetic ordering or the finite spectral-shape collapse.

## Research question

Can the Farey suppression relative to the **reflection-preserving same-gap** control be decomposed into an explicit multiscale or denominator-stratified ordering invariant that is not already determined by the classical Franel–Landau discrepancy, a familiar Möbius summatory quantity, or a bounded amount of local gap-adjacency data?

More specifically, is the finite collapse of `Phi_n(floor(x n))` evidence for a genuine mesoscopic spectral organization at even-mode index `r = O(n)` — equivalently rank-space wavelength of order `N/n` — that admits an exact denominator/mediant description? Or does that profile follow automatically from known Farey counting/discrepancy asymptotics, another asymptotically equivalent rescaling such as `r/sqrt(N)`, or a small collection of lower-order ordering statistics?

## Why it may matter

The Farey mandate asks specifically whether geometric or multiscale information survives after the classical scalar discrepancy is formed. The permutation controls give two clean quotients. Gap sizes alone predict a much larger second-order discrepancy than the deterministic Farey order realizes, and exact left-right reflection removes only the easiest spectral artifact while leaving a large residual suppression at the tested orders.

The normalized spectral-shape diagnostic now asks a different question from the total Franel scalar: after quotienting out the total energy itself, does the *distribution* of that energy across the surviving even scales approach a reproducible arithmetic profile? If so, the natural next target is not another norm of the same discrepancy path but an exact relation among mode bands, denominator strata, or mediant generations. If the profile is fixed by already-known scalar asymptotics or bounded local statistics, the apparent multiscale structure should instead be classified as another representation of existing information.

## Decisive test

Use the exact Dirichlet sine/Green decomposition from `VIS-027` as the primary fixed coordinate system. First reproduce the finite `Phi_n` profile over substantially larger Farey orders with the scaling rule fixed in advance, and compare it against the exact reflection-preserving same-gap ensemble rather than an unconstrained shuffle. Treat `r/n`, `r/sqrt(N)`, and any asymptotically equivalent reparameterization as the same candidate scale family unless an arithmetic derivation distinguishes one of them.

Then derive how much of the even-mode spectral measure is forced successively by additional admitted structure: adjacent gap-pair counts, bounded-depth local blocks, denominator strata, and mediant/Farey-parent relations. The useful theorem surface would be an exact or asymptotic formula for a nontrivial band mass, cross-band covariance, or rescaled spectral measure that is not algebraically determined by `E_2` alone and that survives the stronger matched controls.

Do **not** count the vanished odd Dirichlet modes as a signal: they are deterministically forced by reflection. Also do not count finite curve collapse by itself as evidence of a new invariant. Keep the direction only if the surviving shape admits an exact arithmetic description not equivalent to the existing scalar discrepancy or a familiar Möbius estimate. Kill or hand off the route if the collapse is exhausted by known Farey asymptotics, reflection/local adjacency/stratum statistics, or a normalization identity.

## Evidence boundary

The unrestricted bridge covariance and permutation-mean `L^2` energy are established in `VIS-026`. The Dirichlet spectral decomposition, odd-mode reflection filter, and exact reflection-preserving permutation mean are established in `VIS-027`. The total Farey ratios and the `Phi_n` values above are reproducible **finite** evaluations; the reflection-null ranges are finite Monte Carlo controls inside the exact null ensemble.

The normalization defining `Phi_n` deliberately divides out the total `E_2/E_sym[E_2]` amplitude. Therefore the observed curve agreement cannot by itself strengthen the Franel–Landau RH criterion, establish an asymptotic law, or show that `r/n` is a uniquely natural scale. It is a sharper falsifiable lead about where the already-small Farey discrepancy energy is distributed after exact symmetry control, and remains a clue rather than mathematical evidence.
