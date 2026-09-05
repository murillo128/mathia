---
id: CLUE-farey-discrepancy-gap-order-bridge-suppression
type: research-clue
status: proposed
origin: research-watch
target_line: farey_discrepancy
based_on:
  - research/visual_exploration/findings/VIS-026-gap-permutation-discrepancy-bridge-covariance.md
  - research/visual_exploration/findings/VIS-027-farey-reflection-dirichlet-mode-filter.md
  - research/visual_exploration/findings/VIS-028-farey-endpoint-fan-forces-n-scale-spectrum.md
  - research/visual_exploration/findings/VIS-029-farey-fixed-nx-endpoint-totient-layers.md
  - research/visual_exploration/findings/VIS-030-farey-endpoint-profile-totient-riesz-remainder.md
  - research/visual_exploration/findings/VIS-031-farey-fixed-endpoints-vanish-sublinear-bands.md
  - research/visual_exploration/findings/VIS-032-reflection-null-sublinear-band-saturates-green-energy.md
  - research/farey_discrepancy/README.md
---

# Does Farey ordering suppress discrepancy beyond fixed gaps, reflection, endpoint geometry, and matched-null Green weighting?

## Observation

`VIS-026` gives an exact same-gap permutation control: uniformly permuting a fixed gap multiset makes the cumulative rank discrepancy a finite-population bridge with exact mean squared energy `sigma_g^2 N(N+1)/6`. The actual Farey discrepancy is far smaller at tested orders, so gap ordering contains information beyond the one-point gap multiset.

`VIS-027` removes an exact symmetry artifact. Farey reflection makes the discrepancy path antisymmetric, annihilating every odd Dirichlet sine mode. Conditioning the same-gap permutation null on the exact reflection symmetry gives the stronger exact total baseline

`E_sym[E_2]=sigma_g^2 N(N+2)/12`,

and the finite Farey energy remains strongly suppressed relative to it.

`VIS-028` and `VIS-029` show that deterministic fixed-`nx` endpoint geometry generates an `r=Theta(n)` even-mode spectral scale. For every fixed endpoint cutoff `Y`, the rank profile is governed by

`K(y)=sum_(a<=y) phi(a)(1/a-1/y)`

and the scaled endpoint discrepancy by

`H(y)=y-(pi^2/3)K(y)`.

`VIS-030` identifies `K` as a first-order Riesz mean of normalized totients, with Dirichlet series `zeta(s)/zeta(s+1)` and an exact finite Möbius decomposition. Thus an endpoint subtraction with cutoff growing with `n` is not automatically an arithmetic-free nuisance removal.

`VIS-031` supplies a non-circular alternative. For every **fixed** endpoint cutoff `Y`, the even Dirichlet coefficients satisfy

`|d_(2r)^(Y)|=O_Y(r/n^2)`,

so every sublinear cutoff `q_n=o(n)` has

`n sum_(r<=q_n)|d_(2r)^(Y)|^2 -> 0`.

Fixed endpoint geometry is therefore asymptotically invisible in such a band without subtracting it.

`VIS-032` shows that the same band is nevertheless not starved under the reflection-preserving same-gap null. If

`E_q=sum_(r<=q)d_(2r)^2`,

then exactly

`E_sym[E_q]=C_N sum_(r<=q) 1/[4 sin^2(pi r/N)]`,

with `C_N=2M sigma_g^2/(M-1)` for `N=2M`. The expected null fraction in the band is

`F_q(N)=[6/(N^2-4)] sum_(r<=q)csc^2(pi r/N)`.

Whenever `q->infinity` and `q=o(N)`, `F_q(N)->1`. For Farey, any `q->infinity` with `q=o(n)` therefore lies in a useful control sandwich: every fixed endpoint hierarchy vanishes there by `VIS-031`, while the reflection-same-gap null places asymptotically all of its expected Green energy there by `VIS-032`.

This also gives the exact-null normalized observable

`Q_q=E_q/[E_sym[E_q]]`,

whose null mean is exactly one. At the pre-registered cutoffs `q=floor(sqrt(n))` and `q=floor(n^(2/3))`, finite Farey evaluations through `n=1200` have `Q_q` far below one; for example at `n=1200`, the values are approximately `2.31e-4` and `6.77e-4`, respectively. These are finite diagnostics only, not an asymptotic claim.

## Research question

Does the complete Farey discrepancy retain a stable sublinear even-mode or cross-band suppression, measured against the exact `Q_q` reflection-same-gap baseline, after progressively preserving stronger local ordering information, and can any surviving residual be shown not to reduce to the classical Franel–Landau scalar discrepancy or familiar Möbius/totient quantities?

If a residual survives, can it be localized to genuinely interior information such as adjacent-gap blocks, denominator strata, mediant/Farey-parent ancestry, or long-range gap order, rather than to the fixed endpoint hierarchy already excluded in this band?

## Why it may matter

The visual branch has successively removed several false positives and control failures: the raw gap multiset, exact reflection parity, deterministic endpoint spectral scale, and the assumption that arbitrarily enlarging endpoint subtraction remains a neutral geometric null.

`VIS-031` and `VIS-032` now make the first spectral test cleaner. The selected band simultaneously rejects every fixed endpoint hierarchy and retains essentially the full expected Green energy of the current matched null. A surviving difference therefore cannot be dismissed merely as endpoint localization or as choosing a band in which the null has negligible expected energy.

This still does not identify an arithmetic mechanism. Its value is to make the next stronger null genuinely discriminating: if suppression disappears once bounded local order or denominator/mediant structure is preserved, that closes the visual branch at a precise structural boundary; if it survives, the remaining information channel becomes much narrower.

## Decisive test

Keep the two cutoffs pre-registered:

`q_n=floor(sqrt(n))`

and

`q_n=floor(n^(2/3))`.

For substantially larger Farey orders, compute the complete even Dirichlet coefficients in the fixed coordinates of `VIS-027` and use `Q_q` as the primary first-null-normalized statistic. The reflection-preserving same-gap mean is exact from `VIS-032`; Monte Carlo is needed only if distributional quantiles or concentration under the null are required.

If the finite suppression persists, strengthen the null in a fixed order without changing the spectral bands after inspection: first preserve adjacent-gap pair information or bounded-depth gap blocks; then test denominator strata and mediant/Farey-parent relations when a mathematically well-defined matched ensemble is available. Recompute the same `Q_q`-type observable against each stronger null rather than introducing a new visual statistic after seeing the result.

Kill the route if the sublinear-band suppression is reproduced by a stronger local-order null, collapses to a known Franel–Landau/Möbius estimate, disappears at larger orders, or requires changing the pre-registered band in response to the data. If a proposed test needs modes on the `r=Theta(n)` scale or an endpoint cutoff `Y=Y(n)` growing with `n`, return to the `VIS-029`/`VIS-030` endpoint accounting before interpreting it.

## Evidence boundary

`VIS-026` establishes the fixed-gap bridge control. `VIS-027` establishes reflection parity and the exact reflection-preserving same-gap total baseline. `VIS-028` and `VIS-029` establish the deterministic endpoint hierarchy and its `r=Theta(n)` scale. `VIS-030` establishes the Riesz/Möbius arithmetic carried by progressively enlarged endpoint subtraction. `VIS-031` proves that every fixed endpoint hierarchy vanishes from every sublinear even-mode band at the stated normalization. `VIS-032` proves that any diverging sublinear band captures asymptotically all of the current matched-null Green expectation and provides the exact `Q_q` null mean.

None of these findings proves that the **actual** Farey `Q_q` has a limiting value, that the finite suppression is independent of stronger local-order structure, that a new non-scalar invariant exists, or that any restricted-band estimate strengthens the classical RH-equivalent discrepancy criterion. The finite values are exploratory diagnostics. This file remains a `status: proposed` clue, not mathematical evidence.
