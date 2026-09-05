# VIS-032 — diverging sublinear Farey bands capture the reflection-same-gap Green baseline

## Claim

Let

`0=x_0<x_1<...<x_N=1`, `N=2M`,

be a reflection-symmetric ordered point set as in `VIS-027`, with centered gaps

`delta_i=(x_i-x_(i-1))-1/N`

and

`sigma_g^2=(1/N) sum_i delta_i^2`.

Consider the reflection-preserving same-gap null from `VIS-027`: uniformly permute the first-half centered gaps and mirror that order into the second half. Let

`v_m(k)=sqrt(2/N) sin(pi m k/N)`

be the orthonormal Dirichlet sine basis, write `d_m=<D,v_m>` for the discrepancy coefficients, and define the first-`q` even-mode energy

`E_q(D)=sum_(r=1)^q d_(2r)^2`, `1<=q<=M-1`.

Then the null expectation is exactly

`E_sym[E_q] = C_N B_q(N)`,

where

`C_N = 2M sigma_g^2/(M-1)`

and

`B_q(N)=sum_(r=1)^q 1/[4 sin^2(pi r/N)]`.

The exact expected fraction of the total reflection-same-gap discrepancy energy lying in that band is therefore

`F_q(N)`
` = E_sym[E_q]/E_sym[E_2]`
` = [6/(N^2-4)] sum_(r=1)^q csc^2(pi r/N)`.

If `q=q(N)->infinity` while `q=o(N)`, then

`F_q(N) -> 1`.

More precisely,

`F_q(N)`
` = (6/pi^2) H_q^(2) + O(q/N^2 + 1/N^2)`
` = 1 - 6/(pi^2 q) + O(1/q^2 + q/N^2 + 1/N^2)`,

where `H_q^(2)=sum_(r<=q) r^(-2)`.

Thus a diverging but sublinear set of even Dirichlet modes captures asymptotically all of the **expected inverse-Laplacian/Green energy of the reflection-preserving same-gap null**.

For the Farey sequence of order `n`, `N=Theta(n^2)`. Hence any cutoff satisfying

`q_n -> infinity`, `q_n=o(n)`

has two simultaneous properties:

1. by `VIS-031`, every fixed-`nx` endpoint hierarchy contributes vanishing `n`-scaled energy to the band;
2. by the present result, the reflection-preserving same-gap null puts asymptotically all of its expected Green energy in the same band.

This gives a non-circular **control sandwich**: the band is asymptotically invisible to every fixed endpoint layer but is not asymptotically negligible for the strongest currently available exact same-gap/reflection null.

Finally define the exact-null normalized statistic

`Q_q(D)=E_q(D)/[C_N B_q(N)]`.

For a draw from the reflection-preserving same-gap ensemble,

`E_sym[Q_q]=1`

exactly. No Monte Carlo estimate is needed for this first-null mean.

**Evidence/status:** `EXACT-DERIVED DISCRETE-GREEN CONTROL + FINITE FAREY DIAGNOSTIC + CLASSICAL SPECTRAL INGREDIENTS + NO-NOVELTY-CLAIM`.

No asymptotic law for the actual Farey band energy, new Franel–Landau criterion, or RH implication is claimed.

## Exact band expectation

`VIS-027` diagonalizes the discrepancy path with the Dirichlet path Laplacian. For even modes `m=2r`, its eigenvalues are

`lambda_(2r)=4 sin^2(pi r/N)`.

Writing `a_m` for the corresponding normalized edge coefficient, `VIS-027` gives

`a_m=sqrt(lambda_m) d_m`

and, under the reflection-preserving same-gap null,

`E_sym[a_(2r)^2]=2M sigma_g^2/(M-1)=C_N`

for every surviving even mode.

Therefore

`E_sym[d_(2r)^2]=C_N/lambda_(2r)`

and finite summation through `q` gives

`E_sym[E_q]=C_N sum_(r<=q) 1/[4 sin^2(pi r/N)]`.

For the full even spectrum, `VIS-027` records the elementary path-trace identity

`sum_(r=1)^(M-1) 1/lambda_(2r)=(M^2-1)/6`.

Since `M=N/2`, division by this total gives exactly

`F_q(N)=[6/(N^2-4)] sum_(r<=q) csc^2(pi r/N)`.

The dependence on the actual gap multiset cancels from this fraction. The multiset controls the overall scale through `sigma_g^2`; the **expected spectral allocation under this null depends only on `N` and the cutoff `q`**.

## Sublinear Green-trace saturation

Assume `q=o(N)`. Uniformly for `1<=r<=q`, the small-angle expansion gives

`csc^2(pi r/N)`
` = N^2/(pi^2 r^2) + 1/3 + O(r^2/N^2)`.

Summing and substituting into the exact fraction yields

`F_q(N)`
` = (6/pi^2) sum_(r<=q) 1/r^2 + O(q/N^2 + 1/N^2)`.

The standard tail estimate

`H_q^(2)=pi^2/6-1/q+O(1/q^2)`

then gives the stated refinement and `F_q(N)->1` whenever also `q->infinity`.

This concentration is not a Farey phenomenon. It is the low-frequency weighting of the inverse Dirichlet path Laplacian combined with the mode-flat edge variance of the reflection-preserving permutation null. It is therefore a **baseline geometry that a Farey signal must beat**, not evidence for arithmetic structure.

## Farey control sandwich

For Farey order `n`, the number of gaps satisfies `N=Theta(n^2)`. The cutoffs proposed in the current Farey clue,

`q_n=floor(sqrt(n))`

and

`q_n=floor(n^(2/3))`,

both diverge and satisfy `q_n=o(n)`, hence also `q_n=o(N)`.

`VIS-031` proves that every fixed endpoint hierarchy has vanishing `n`-scaled energy in either band. The present null calculation independently shows that either band captures asymptotically the full expected Green energy of the reflection-preserving same-gap ensemble.

The point is not that these cutoffs are uniquely canonical. It is that they belong to a broad regime in which two previously competing requirements are compatible: fixed endpoint geometry disappears without subtraction, while the matched null retains essentially all of its inverse-Laplacian energy.

## Finite Farey diagnostic

Direct finite evaluation of the Farey discrepancy and its Dirichlet sine coefficients gives the following values. `F_null` is the exact null fraction `F_q(N)`, `F_actual=E_q(F_n)/E_2(F_n)`, and `Q_q` is the actual band energy divided by its exact reflection-same-gap null mean.

| `n` | `q=floor(sqrt(n))` | `F_null` | `F_actual` | `Q_q` | `q=floor(n^(2/3))` | `F_null` | `F_actual` | `Q_q` |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 100 | 10 | 0.942148 | 0.191647 | 0.009556 | 21 | 0.971734 | 0.385083 | 0.018616 |
| 200 | 14 | 0.958091 | 0.238344 | 0.006051 | 34 | 0.982381 | 0.405059 | 0.010029 |
| 400 | 20 | 0.970351 | 0.153900 | 0.001623 | 54 | 0.988846 | 0.321200 | 0.003324 |
| 800 | 28 | 0.978671 | 0.104849 | 0.000487 | 86 | 0.992972 | 0.261984 | 0.001199 |
| 1200 | 34 | 0.982380 | 0.079886 | 0.000231 | 112 | 0.994596 | 0.236748 | 0.000677 |

The finite computation was checked against Parseval: the sine-spectrum energy agrees with the direct squared discrepancy sum to floating-point precision, while the odd modes vanish to numerical roundoff as required by Farey reflection.

These numbers show two finite facts relevant to experimental design. First, the pre-registered bands already contain most of the matched-null Green expectation even at moderate orders. Second, the actual Farey discrepancy places a much smaller **fraction of its own energy** in those low even modes than the matched null does at the tested orders.

No monotonicity, limiting exponent, or nonzero asymptotic residual is inferred from the table. The finite suppression could still be explained by stronger local-order, denominator, mediant, or classical Möbius structure.

## Prior art and novelty assessment

The stochastic-control boundary is inherited from `VIS-026`: fixed-gap permutations and their effect on Farey discrepancy are already explicit in Rogelio Tomás García's 2026 treatment, while finite-population partial-sum processes are classical. The present statistic uses the exact second-order reflection-conditioned null developed in `VIS-027` rather than claiming a new permutation principle.

The spectral ingredients are likewise classical. `VIS-027` already audits the Dirichlet path-Laplacian sine diagonalization, Green-function reciprocal-eigenvalue organization, and reflection parity. The present result is an exact **partial Green-trace specialization** of those ingredients plus the elementary small-angle expansion of `csc^2`.

A targeted structure-based literature check found standard discrete-Green trace theory and the current Farey gap-permutation literature, but no basis for a novelty claim about the general low-band concentration. None is made. The durable contribution is the Mathia-specific control composition: combining the exact reflection-same-gap partial trace with `VIS-031` shows that the same sublinear Farey band can simultaneously reject fixed endpoint geometry and retain the matched-null Green baseline.

## Boundary conditions and falsification

The result concerns the **expectation** under the reflection-preserving same-gap ensemble. It does not establish concentration, quantiles, or the full distribution of `Q_q`; an unusually small `Q_q` should therefore not be assigned a p-value from the mean alone.

The null preserves the complete gap multiset and exact reflection symmetry, but not adjacent gap-pair counts, bounded-depth blocks, denominator strata, mediant ancestry, or other arithmetic order relations. Failure against this null localizes information beyond gap sizes and reflection but does not identify its source.

The limit `F_q->1` is universal null geometry. It cannot itself be counted as arithmetic cancellation, and changing to a low-mode representation does not create information beyond the original discrepancy path.

The finite Farey values above do not prove that `Q_q->0`, that the band obeys a new asymptotic law, or that its suppression is stronger than the classical Franel–Landau/Möbius content. Any such claim must survive stronger controls and an explicit bridge to the RH-critical scale.

The endpoint half of the control sandwich uses `VIS-031` and therefore applies to every **fixed** endpoint cutoff `Y`; it does not cover endpoint windows `Y=Y(n)` growing with `n`.

## Research consequence

The existing cross-line Farey clue

`research/farey_discrepancy/clues/CLUE-farey-gap-order-bridge-suppression.md`

can now use `Q_q` as its first exact-null-normalized observable for the pre-registered sublinear bands. This removes the need to estimate the first null mean by Monte Carlo and verifies that the chosen low-frequency windows are not trivially starved of matched-null Green energy.

If suppression survives, the next mathematical step belongs to the Farey investigation: progressively strengthen the null to preserve local gap order, denominator strata, or mediant/Farey-parent structure and determine whether the residual collapses to known Franel–Landau/Möbius information. That is a separate research question and is not pursued in this finding.
