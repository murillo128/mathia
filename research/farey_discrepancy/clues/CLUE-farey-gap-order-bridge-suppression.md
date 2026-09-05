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
  - research/visual_exploration/findings/VIS-034-farey-low-band-suppression-factorization.md
  - research/arithmetic_fidelity/findings/AF-133-restricted-witness-composition-requires-quotient-compatible-recovery.md
  - research/farey_discrepancy/README.md
---

# Does Farey ordering suppress discrepancy beyond fixed gaps, reflection, endpoint geometry, and matched-null Green weighting?

## Observation

`VIS-026` gives an exact same-gap permutation control: uniformly permuting a fixed gap multiset makes the cumulative rank discrepancy a finite-population bridge with exact mean squared energy `sigma_g^2 N(N+1)/6`. The actual Farey discrepancy is far smaller at tested orders, so gap ordering contains information beyond the one-point gap multiset.

`VIS-027` removes an exact symmetry artifact. Farey reflection makes the discrepancy path antisymmetric, annihilating every odd Dirichlet sine mode. Conditioning the same-gap permutation null on the exact reflection symmetry gives the stronger exact total baseline

`E_sym[E_tot]=sigma_g^2 N(N+2)/12`,

and the finite Farey total discrepancy energy remains strongly suppressed relative to it.

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

`F_null(q,N)=[6/(N^2-4)] sum_(r<=q)csc^2(pi r/N)`.

Whenever `q->infinity` and `q=o(N)`, `F_null->1`. For Farey, any `q->infinity` with `q=o(n)` therefore lies in a useful control sandwich: every fixed endpoint hierarchy vanishes there by `VIS-031`, while the reflection-same-gap null places asymptotically all of its expected Green energy there by `VIS-032`.

`VIS-034` removes one remaining interpretive confound. The first-null-normalized band statistic

`Q_q=E_q/E_sym[E_q]`

factors exactly as

`Q_q=A S_q`,

where

`A=E_tot/E_sym[E_tot]`

is the **global total-discrepancy suppression**, and

`S_q=(E_q/E_tot)/(E_sym[E_q]/E_sym[E_tot])`

is the **spectral-allocation suppression**. Thus a very small `Q_q` does not by itself identify a low-frequency mechanism: it can be small because the whole discrepancy path is small, because the remaining energy is shifted away from the null's low-mode profile, or both.

For the finite values already tabulated in `VIS-032`, both effects are present. At `n=1200`, the common global factor is about `A~2.84e-3`, while the spectral factors are about `S_q~0.0813` for `q=floor(sqrt(n))` and `S_q~0.238` for `q=floor(n^(2/3))`. The reported `Q_q` values are their products. These are finite diagnostics only, not asymptotic claims.

## Research question

The next finite experiment should determine which ordering information is necessary for `S_q`, not accumulate more instances of small combined `Q_q`. The source facts needed from Visual Exploration are the exact factorization `Q_q=A S_q`, the reflection-conditioned Green baseline above, and invisibility of every fixed endpoint layer in a diverging sublinear band. None supplies an asymptotic law for the actual Farey residual.

After separating global discrepancy suppression from spectral reallocation, does the complete Farey discrepancy retain a stable **spectral-allocation deficit `S_q<1`** in pre-registered sublinear even-mode bands after progressively preserving stronger local ordering information? Can any surviving `S_q` residual be shown not to reduce to the classical Franel–Landau scalar discrepancy or familiar Möbius/totient quantities?

If a residual survives, can it be localized to genuinely interior information such as adjacent-gap blocks, denominator strata, mediant/Farey-parent ancestry, or long-range gap order, rather than to the fixed endpoint hierarchy already excluded in this band?

## Why it may matter

The visual branch has successively removed several false positives and control failures: the raw gap multiset, exact reflection parity, deterministic endpoint spectral scale, the assumption that arbitrarily enlarging endpoint subtraction remains a neutral geometric null, and now the conflation of **total amplitude** with **spectral shape**.

The selected sublinear bands simultaneously reject every fixed endpoint hierarchy and retain essentially the full expected Green energy of the current matched null. `VIS-034` makes the next test sharper still: a genuinely spectral effect must survive in `S_q` after the scalar/global factor `A` is divided out.

If stronger local-order controls drive `S_q` back to one while `A` remains small, the visual spectral branch collapses to a global discrepancy-ordering effect. If `S_q` remains nontrivial, the remaining information channel becomes much narrower and genuinely scale-sensitive.

## Decisive test

Freeze a new larger-order panel and the two existing cutoffs before inspecting its residuals. A concrete candidate panel is `n in {2400,3200,4800}`, after checking that those outcomes have not already been used to tune this question. If they have, declare them exploratory and reserve a separate untouched confirmation panel. Retain the same normalization and report `(A,S_q)` separately at every order.

Use the reflection/same-gap ensemble as the exact first control, then predeclare one stronger local-order control and one denominator/mediant control. For each, specify the realizable sample space, which relations are preserved, and how it is sampled. If the constraints determine the original order or prevent adequate sampling, that control is degenerate rather than evidence that the residual survives. Recompute its total and band expectations; do not transfer the weaker null's Green law to it.

Calibrate the distribution of the actual chosen statistic under each null, including uncertainty in simulated expectations. In particular, a ratio of expected energies does not make `S_q` a random variable of null mean one. Use a joint predeclared rule across orders and bands rather than independent-looking marginal thresholds. The finite direction survives only if spectral allocation remains separated after global amplitude and the stronger realizable controls are accounted for; disappearance of `S_q` with surviving `A` redirects this candidate to scalar discrepancy. Neither outcome alone establishes an asymptotic rate.

The transport warning from AF-133 is specific: changing the retained witness class can make a previously invisible residual visible unless recovery respects the quotient. Accordingly, any norm change or reconstruction used to connect a surviving band residual to the Franel--Landau target must have its stability and retained information proved, rather than inherited from an exact finite identity.

Keep the two cutoffs pre-registered:

`q_n=floor(sqrt(n))`

and

`q_n=floor(n^(2/3))`.

For substantially larger Farey orders, compute the complete even Dirichlet coefficients in the fixed coordinates of `VIS-027`. For each matched null, report separately

`A=E_tot/E_null[E_tot]`

and

`S_q=(E_q/E_tot)/(E_null[E_q]/E_null[E_tot])`,

with `Q_q=A S_q` only as the derived combined diagnostic. Do not interpret a tiny `Q_q` as specifically spectral unless the corresponding `S_q` is also suppressed.

For the reflection-preserving same-gap null the needed expectations are exact from `VIS-027` and `VIS-032`; Monte Carlo is needed only for distributional quantiles/concentration or for stronger nulls without an analytic expectation.

If the finite spectral-allocation suppression persists, strengthen the null in a fixed order without changing the bands after inspection: first preserve adjacent-gap pair information or bounded-depth gap blocks; then test denominator strata and mediant/Farey-parent relations when a mathematically well-defined matched ensemble is available. Recompute both `A` and `S_q` for each stronger null rather than carrying the same-gap normalization into a different ensemble.

Kill the **spectral** route if `S_q` returns to one under a stronger local-order null, tends to one at larger orders, collapses to a known scalar discrepancy/Möbius estimate, or requires changing the pre-registered band in response to the data. A small `A` may remain mathematically interesting, but it belongs to the global discrepancy channel rather than to a new low-mode geometry.

If a proposed test needs modes on the `r=Theta(n)` scale or an endpoint cutoff `Y=Y(n)` growing with `n`, return to the `VIS-029`/`VIS-030` endpoint accounting before interpreting it.

## Evidence boundary

`VIS-026` establishes the fixed-gap bridge control. `VIS-027` establishes reflection parity and the exact reflection-preserving same-gap total baseline. `VIS-028` and `VIS-029` establish the deterministic endpoint hierarchy and its `r=Theta(n)` scale. `VIS-030` establishes the Riesz/Möbius arithmetic carried by progressively enlarged endpoint subtraction. `VIS-031` proves that every fixed endpoint hierarchy vanishes from every sublinear even-mode band at the stated normalization. `VIS-032` proves that any diverging sublinear band captures asymptotically all of the current matched-null Green expectation. `VIS-034` proves only the exact normalization factorization separating total-amplitude and spectral-allocation effects.

None of these findings proves that the actual Farey `A`, `S_q`, or `Q_q` has a limiting value, that finite spectral reallocation is independent of stronger local-order structure, that a new non-scalar invariant exists, or that any restricted-band estimate strengthens the classical RH-equivalent discrepancy criterion. The finite values are exploratory diagnostics. This file remains a `status: proposed` clue, not mathematical evidence.
