# VIS-373 — a small Gram commutator is only a gap-weighted departure from commuting preconditioning

## Claim

Let `A_W` be a finite-dimensional Wang coefficient map with source-free Gram

`G=A_W^*A_W>=0`,

and let `C>0` be a positive Hermitian relative coefficient metric. Write the distinct spectral decomposition

`G=sum_alpha lambda_alpha P_alpha`

and define the Gram-block pinching

`C_0=sum_alpha P_alpha C P_alpha`.

Then `C_0>0`, `[C_0,G]=0`, and the Hilbert--Schmidt/Frobenius norm satisfies the exact identities

`||C-C_0||_F^2 = sum_(alpha!=beta) ||P_alpha C P_beta||_F^2`,

`||[G,C]||_F^2 = sum_(alpha!=beta) |lambda_alpha-lambda_beta|^2 ||P_alpha C P_beta||_F^2`.

Hence, if `G` has at least two distinct eigenvalues and

`delta_G=min_(alpha!=beta)|lambda_alpha-lambda_beta|>0`,

then

`||C-C_0||_F <= delta_G^(-1) ||[G,C]||_F`.

Thus the raw statement `[G,C]!=0` is only a qualitative escape from the commuting class of `VIS-370`. Quantitatively, cross-Gram orientation is priced by the **spectral-gap-normalized commutator**. A metric with

`||[G,C]||_F << delta_G`

is close to a positive metric that commutes exactly with `G`, regardless of how complicated or externally motivated the original constructor of `C` may be.

There is also a direct Wang singular-spectrum consequence. Suppose

`C>=m I`, `m>0`.

Then `C_0>=m I`, and with

`A_C=A_W C^(1/2)`, `A_0=A_W C_0^(1/2)`,

one has

`||C^(1/2)-C_0^(1/2)||_op <= ||C-C_0||_op/(2 sqrt(m))`

and therefore

`|s_k(A_C)-s_k(A_0)|`
` <= ||A_W||_op ||[G,C]||_F /(2 sqrt(m) delta_G)`

for every singular-value index `k`.

So, whenever the normalized quantity

`||[G,C]||_F /(sqrt(m) delta_G)`

is small, the whole metric-modified Wang singular spectrum is close to that of an exactly commuting positive metric and hence close to the spectral-filter/preconditioning class already identified in `VIS-370`.

The caveat is structural and important: if `delta_G` collapses, a small raw commutator can coexist with large mixing among nearly degenerate Gram sectors. The next positive-Hilbert frontier is therefore not merely “find a noncommuting external metric,” but “produce cross-sector orientation that remains non-negligible after normalization by the relevant Gram spectral gaps and by the metric lower scale.”

**Evidence/status:** `EXACT-DERIVED + CLASSICAL SPECTRAL-BLOCK/SYLVESTER ESTIMATE + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This proves no stronger bound for the normalized Chebyshev-theta remainder, the PNT remainder, zeta zeros, or RH.

## 1. Alternate representation: the commutator is a gap-weighted off-diagonal energy

The previous frontier treats noncommutation as evidence that a metric uses structure beyond the Gram alone. To measure how much orientation has actually been imported, keep the spectral projectors of `G` and decompose `C` into Gram blocks.

Because

`G P_alpha=lambda_alpha P_alpha`,

one has for every pair `(alpha,beta)`

`P_alpha [G,C] P_beta`
` = (lambda_alpha-lambda_beta) P_alpha C P_beta`.

The Gram-diagonal blocks vanish from the commutator. Orthogonality of the matrix blocks in the Frobenius inner product gives

`||[G,C]||_F^2`
` = sum_(alpha,beta) ||P_alpha [G,C] P_beta||_F^2`
` = sum_(alpha!=beta) |lambda_alpha-lambda_beta|^2 ||P_alpha C P_beta||_F^2`.

Meanwhile `C_0` deletes exactly those off-diagonal Gram blocks, so

`||C-C_0||_F^2`
` = sum_(alpha!=beta) ||P_alpha C P_beta||_F^2`.

The minimum distinct Gram gap therefore yields the stated bound immediately. More locally, the exact identity already supplies the sharper audit: mixing between two particular sectors is charged by their own gap `|lambda_alpha-lambda_beta|`, not by one global number.

If `G` is scalar, every `C` commutes with it and there is no orientation distinction to detect. If several eigenvalues coalesce, orientation inside the resulting eigenspace is likewise invisible to `G`; only mixing between distinct spectral sectors contributes to the commutator.

## 2. The nearest Gram-block metric remains positive

The pinched matrix is not merely a formal commuting approximation. If `C>=mI`, then for every vector `v`,

`<v,C_0 v>`
` = sum_alpha <P_alpha v, C P_alpha v>`
` >= m sum_alpha ||P_alpha v||^2`
` = m ||v||^2`.

Hence `C_0>=mI>0`. It is therefore an admissible positive relative metric in the same Hilbert geometry, not a projection that leaves the allowed class.

This matters for the Wang control. The comparison is between the proposed noncommuting metric and a genuine positive commuting metric obtained without changing the baseline Gram sectors or importing any arithmetic source information.

## 3. Small normalized commutator gives a nearby commuting Wang spectrum

Let

`X=C^(1/2)`, `Y=C_0^(1/2)`, `Z=X-Y`.

Since

`C-C_0=XZ+ZY`,

`Z` solves a Sylvester equation. Because `X,Y>=sqrt(m) I`, the standard integral solution is

`Z = integral_0^infinity exp(-tX) (C-C_0) exp(-tY) dt`.

Therefore

`||Z||_op`
` <= integral_0^infinity exp(-2 sqrt(m)t) dt ||C-C_0||_op`
` = ||C-C_0||_op/(2 sqrt(m))`.

Using `||M||_op<=||M||_F` and the gap estimate gives

`||C^(1/2)-C_0^(1/2)||_op`
` <= ||[G,C]||_F/(2 sqrt(m) delta_G)`.

Now

`A_C-A_0=A_W(C^(1/2)-C_0^(1/2))`,

so

`||A_C-A_0||_op`
` <= ||A_W||_op ||[G,C]||_F/(2 sqrt(m) delta_G)`.

The standard singular-value perturbation inequality

`|s_k(M)-s_k(N)|<=||M-N||_op`

then yields the claimed bound for every `k`.

This is stronger than saying that an almost commuting metric “looks roughly diagonal.” It gives an explicit route from the commutator budget to the full Wang singular spectrum, with the exact cost exposed in the Gram gap and the positive-metric lower scale.

## 4. What survives when Gram gaps collapse

The global estimate deliberately fails when `delta_G` becomes tiny. That is not a weakness to hide; it identifies the next possible escape.

Two Gram sectors with eigenvalues separated by `epsilon` may support an `O(1)` off-diagonal block of `C` while contributing only `O(epsilon)` to `[G,C]`. Such mixing is large in coefficient orientation but occurs inside an almost-degenerate spectral cluster. A raw small-commutator test therefore cannot distinguish “nearly spectral filtering” from “large rotation inside a collapsing Gram cluster.”

The exact block identity gives the correct refinement. For any threshold `gamma>0`, the Frobenius energy of metric blocks connecting pairs with

`|lambda_alpha-lambda_beta|>=gamma`

is at most

`gamma^(-2) ||[G,C]||_F^2`.

Thus a candidate whose commutator is small can carry substantial noncommuting orientation only across Gram gaps that are comparably small. To claim a genuine Wang mechanism from that regime, the candidate must show that near-degenerate-sector rotation produces a destination gain not already explained by the same collapsing source-free Gram geometry and must propagate the metric cost through the physical coefficient norm.

This narrows the positive-Hilbert route after `VIS-372`. A noncommuting external observable passes the first structural gate, but **small noncommutation at resolved Gram gaps remains quantitatively close to commuting preconditioning**. The surviving regime is concentrated near collapsing Gram clusters or requires a commutator of the same scale as the gaps it crosses.

## Prior-art audit

All matrix-analysis ingredients are classical. The block formula is the elementary spectral representation of a commutator with one Hermitian matrix; the associated inverse-gap estimates are the finite-dimensional Sylvester-equation mechanism. Rajendra Bhatia, *Perturbation Bounds for Matrix Eigenvalues*, SIAM Classics in Applied Mathematics (2007), Chapter 10, discusses Sylvester equations and commutator inequalities in the separated-spectrum setting, DOI `10.1137/1.9780898719079.ch10`.

Perturbation estimates for matrix square roots via Sylvester equations are classical; see Bernhard A. Schmitt, **Perturbation bounds for matrix square roots and Pythagorean sums**, *Linear Algebra and its Applications* 174 (1992), 215--227, DOI `10.1016/0024-3795(92)90052-C`.

The broader theory of almost commuting Hermitian matrices is much stronger and does not require a fixed spectral gap. Huaxin Lin's theorem and its later short proof show dimension-uniform approximation of almost commuting self-adjoint matrices by commuting ones; see Peter Friis and Mikael Rordam, **Almost commuting self-adjoint matrices — a short proof of Huaxin Lin's theorem**, *Journal für die reine und angewandte Mathematik* 479 (1996), 121--131, DOI `10.1515/crll.1996.479.121`. Quantitative and constructive refinements include Matthew B. Hastings, **Making almost commuting matrices commute**, *Communications in Mathematical Physics* 291 (2009), 321--345, DOI `10.1007/s00220-009-0877-2`.

No novelty is claimed for commutator block identities, pinching, Sylvester estimates, almost-commuting matrix theory, square-root perturbation, or singular-value perturbation. The Mathia-specific contribution is the Wang accounting boundary: after `VIS-370`--`VIS-372`, the relevant noncommuting resource is not the Boolean condition `[G,C]!=0` but the amount of metric orientation carried across resolved Gram gaps after the positive-metric scale is charged.

## Dependencies

- `VIS-369`: freely aligned degenerating positive metrics can prescribe the active singular spectrum.
- `VIS-370`: exactly commuting positive metrics are sectorwise spectral filters of the baseline Wang Gram.
- `VIS-371`: a coordinate-free metric rule built from the Gram alone is forced into that commuting class.
- `VIS-372`: additional commuting Hermitian structure still yields joint spectral filtering; a genuine orientation escape requires noncommuting extra structure.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue further narrowed by this result.

## Research consequence

For future positive-Hilbert Wang candidates, “the external metric does not commute with the Gram” is necessary to leave the exact `VIS-370` class but is not yet quantitatively informative. Compute the Gram spectral blocks of the relative metric and compare their off-diagonal energy with the gaps they cross.

If `||[G,C]||_F/(sqrt(m) delta_G)` is small on the relevant resolved sectors, the candidate's complete Wang singular spectrum lies close to that of a valid exactly commuting positive metric. Such a gain remains near-preconditioning. A surviving orientation mechanism must either carry order-one gap-normalized commutator mass, live in collapsing near-degenerate Gram clusters and explain why that collapse is not itself the source-free mechanism, or leave the finite-dimensional positive-Hilbert framework.