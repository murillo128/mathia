# VIS-374 — bounded positive orientation inside narrow Gram clusters is spectrally cheap

## Claim

Let `A_W` be a finite-dimensional Wang coefficient map with source-free Gram

`G=A_W^*A_W>=0`,

and let `C>0` be a positive Hermitian relative coefficient metric satisfying

`m I <= C <= M I`,

with `0<m<=M<infinity`.

Partition the distinct spectral projectors of `G` into disjoint clusters `J_1,...,J_r`. Put

`Q_j=sum_(alpha in J_j) P_alpha`,

choose one real representative `mu_j` inside the convex hull of the eigenvalues in cluster `J_j`, and define the cluster-coarsened Gram

`G_0=sum_j mu_j Q_j`.

Write

`eta=||G-G_0||_op`

for the within-cluster spectral radius and, when at least two clusters are present,

`gamma=min{|lambda_alpha-lambda_beta|: alpha in J_j, beta in J_l, j!=l}`

for the resolved inter-cluster spectral separation.

Define the cluster pinching of the metric by

`C_cl=sum_j Q_j C Q_j`.

Then `mI<=C_cl<=MI`. Moreover the off-cluster metric energy obeys

`||C-C_cl||_F <= gamma^(-1) ||[G,C]||_F`

whenever more than one cluster is present.

The important new point is what happens **inside** a narrow near-degenerate cluster. There exists a positive metric `C_*` such that

`[C_*,G]=0`,

`mI<=C_*<=MI`,

and, on every cluster `Q_j`, the restriction `C_*|_(Q_j)` has exactly the same eigenvalue multiset as `C_cl|_(Q_j)`. For every ordered squared singular value,

`lambda_k(C^(1/2) G C^(1/2)) = s_k(A_W C^(1/2))^2`,

one has the bound

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2|`
` <= ||G||_op sqrt(M/m) ||[G,C]||_F/gamma + 2 M eta`.

If `C` is already block diagonal across the chosen clusters, the commutator term disappears and

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2| <= 2 M eta`.

Thus large rotations of a bounded positive metric **inside a collapsing Gram cluster are not by themselves an order-one singular-spectrum resource**. When the cluster width `eta` is small, exact orientation inside that cluster can be replaced by an exactly `G`-commuting metric with the same clusterwise metric eigenvalues at an `O(M eta)` cost in the squared Wang spectrum.

Combined with `VIS-373`, a bounded positive-Hilbert metric can escape the commuting/preconditioning class spectrally only by paying at least one of three costs: substantial orientation across **resolved** Gram gaps, non-negligible within-cluster Gram width, or metric degeneration/condition-number growth large enough to compensate those small spectral scales.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL HERMITIAN PERTURBATION/PINCHING + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This proves no stronger estimate for the normalized Chebyshev-theta remainder, the prime-number-theorem remainder, zeta zeros, or RH.

## 1. Representation path and source-grounding status

The canonical Wang branch has already separated the arithmetic source from the coefficient geometry. The source side is the normalized Chebyshev-theta remainder, while `A_W` and its Gram `G=A_W^*A_W` describe the source-free positive compact coefficient geometry after the earlier representation and conditioning reductions.

This finding deliberately stays on that **source-blind control layer**. No value of the arithmetic source, no prime-dependent selector, and no zeta-zero information enters `G`, the spectral clustering, or the metric comparison. The purpose is therefore negative: determine whether near-degenerate orientation of a positive metric can manufacture a new Wang singular-value scale even before arithmetic information is supplied.

The representation chain is

`A_W -> G=A_W^*A_W -> spectral clusters Q_j -> coarsened Gram G_0 -> cluster metric C_cl -> commuting control C_*`.

Every step after `A_W` is an exact finite-dimensional transformation of source-free coefficient geometry. A surviving gain after this audit would still require a separate bridge back to arithmetic source information and then to the Wang destination.

## 2. Coarse pinching removes only orientation across resolved gaps

Write the exact spectral decomposition

`G=sum_alpha lambda_alpha P_alpha`.

The cluster pinching keeps all metric blocks inside each `Q_j` and deletes only blocks between different clusters. Orthogonality of the spectral blocks in Frobenius norm gives

`||C-C_cl||_F^2`
` = sum_(j!=l) ||Q_j C Q_l||_F^2`.

As in `VIS-373`,

`P_alpha [G,C] P_beta`
` = (lambda_alpha-lambda_beta) P_alpha C P_beta`.

Every block joining distinct clusters crosses a gap at least `gamma`, hence

`||[G,C]||_F^2`
` >= gamma^2 sum_(j!=l) ||Q_j C Q_l||_F^2`
` = gamma^2 ||C-C_cl||_F^2`.

Therefore

`||C-C_cl||_F <= ||[G,C]||_F/gamma`.

The order bounds on `C_cl` are preserved by pinching: for every vector `v`,

`<v,C_cl v> = sum_j <Q_j v,C Q_j v>`,

so `m||v||^2<=<v,C_cl v><=M||v||^2`.

This is the resolved-gap part of `VIS-373`, now localized to a chosen cluster scale. The remaining question is whether arbitrary orientation **within** the `Q_j` blocks can itself produce a new singular-value scale when the Gram eigenvalues inside those blocks are almost equal.

## 3. Inside one cluster the coarsened Gram is scalar

By construction,

`G_0 Q_j=mu_j Q_j`.

Hence every operator that is block diagonal with respect to the `Q_j` commutes with `G_0`, even if it rotates strongly among the exact eigenspaces of `G` lying inside one cluster.

Diagonalize each positive block `C_cl|_(Q_j)` internally. Keep its eigenvalues but assign them to any orthonormal basis formed from exact eigenvectors of `G` inside `Q_j`. Doing this independently for every cluster gives a positive matrix `C_*` with three properties:

- `C_*` commutes with the exact `G`;
- `mI<=C_*<=MI`;
- `C_*|_(Q_j)` and `C_cl|_(Q_j)` have the same eigenvalues for every `j`.

Now consider the coarsened squared-spectrum matrices

`B_0(C_cl)=C_cl^(1/2) G_0 C_cl^(1/2)`,

`B_0(C_*)=C_*^(1/2) G_0 C_*^(1/2)`.

Because `G_0` is scalar on each cluster,

`B_0(C_cl)|_(Q_j)=mu_j C_cl|_(Q_j)`,

while

`B_0(C_*)|_(Q_j)=mu_j C_*|_(Q_j)`.

The two restrictions have the same eigenvalue multiset `{mu_j c_(j,r)}`. Taking the union over clusters shows that

`B_0(C_cl)` and `B_0(C_*)`

have **exactly the same global eigenvalue multiset**.

Thus, after replacing a narrow exact Gram cluster by one scalar eigenvalue, all internal positive-metric orientation disappears from the singular spectrum. Only the clusterwise metric eigenvalues remain.

## 4. Restoring the exact Gram costs only the cluster width

Let

`B(C)=C^(1/2) G C^(1/2)`.

Since `||G-G_0||_op=eta` and `C_cl,C_*<=MI`,

`||B(C_cl)-B_0(C_cl)||_op <= M eta`,

`||B(C_*)-B_0(C_*)||_op <= M eta`.

Hermitian eigenvalue perturbation therefore gives, after ordering the spectra,

`|lambda_k(B(C_cl))-lambda_k(B(C_*))| <= 2 M eta`

for every `k`, because the two intermediate `B_0` matrices have identical spectra.

This is the missing control in the caveat of `VIS-373`. A near-degenerate cluster can permit an `O(1)` rotation while producing a very small raw commutator, but the exact Gram is simultaneously only `eta` away from being scalar on that cluster. For a bounded positive metric, changing orientation inside that cluster can affect the squared Wang singular spectrum by at most `2M eta`.

In particular, when `eta->0` while `M` stays bounded, the internal orientation becomes spectrally invisible even if the eigenvectors of `C_cl` rotate by an order-one angle relative to the exact Gram eigenbasis.

## 5. Adding the resolved cross-cluster term

It remains to compare `C` with `C_cl`. The square-root perturbation argument used in `VIS-373` gives

`||C^(1/2)-C_cl^(1/2)||_op`
` <= ||C-C_cl||_op/(2 sqrt(m))`.

Let `R=C^(1/2)` and `S=C_cl^(1/2)`. Then

`R G R-S G S=(R-S) G R+S G (R-S)`.

Using `||R||_op,||S||_op<=sqrt(M)` yields

`||B(C)-B(C_cl)||_op`
` <= ||G||_op sqrt(M/m) ||C-C_cl||_op`
` <= ||G||_op sqrt(M/m) ||[G,C]||_F/gamma`.

Combining this with the `2M eta` internal-cluster comparison and applying Hermitian eigenvalue perturbation proves

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2|`
` <= ||G||_op sqrt(M/m) ||[G,C]||_F/gamma + 2M eta`.

The bound is intentionally expressed for squared singular values because those are the eigenvalues of the positive Gram-side matrices and avoid introducing an artificial square-root loss near zero. A cruder singular-value estimate follows immediately from `|sqrt(a)-sqrt(b)|<=sqrt(|a-b|)` for `a,b>=0` when needed.

If only one spectral cluster is used, there is no cross-cluster term: set `C_cl=C`. The result then reduces directly to the `2M eta` bound. If a cluster is exactly degenerate, its contribution to `eta` is zero and its internal orientation is exactly irrelevant.

## 6. What this closes and what remains open

`VIS-373` left one explicit loophole: a small commutator may hide large metric rotation inside a cluster whose Gram gaps collapse. The present estimate shows that **bounded positive rotation inside such a narrow cluster is itself spectrally cheap**. The same small spectral width that hides the rotation from the commutator also limits how much that rotation can change the squared singular spectrum.

Therefore a positive-Hilbert continuation cannot claim a new mechanism merely from a rapidly rotating eigenbasis in a near-degenerate Gram sector. To survive this control it must show at least one of the following:

- cross-cluster orientation whose commutator mass is not small after division by the resolved inter-cluster gap;
- a cluster width `eta` whose scale is itself large enough to reach the destination and is not just the source-free Gram collapse already priced by the Wang geometry;
- positive metric norms or condition numbers growing strongly enough that the factors `M` or `sqrt(M/m)` repay the apparent gain, in which case that degeneration must be charged as part of the mechanism;
- genuinely different structure outside finite-dimensional positive-Hilbert metric reorientation, such as indefinite/non-Hilbert topology, noncompact/global geometry, nonlinear source coupling, or a controlled infinite-dimensional limit.

This does not rule out a physically fixed noncommuting operator. It says that, within bounded positive Hilbert geometry, its **orientation alone** is not useful if it lives only inside spectrally narrow source-free Gram clusters.

## Prior-art audit

The matrix-analysis ingredients are classical. Rajendra Bhatia, *Matrix Analysis*, Graduate Texts in Mathematics 169, Springer (1997), DOI `10.1007/978-1-4612-0653-8`, treats variational eigenvalue principles, spectral variation of normal matrices, perturbation of spectral subspaces, and perturbation of matrix functions. Tosio Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer (1995), DOI `10.1007/978-3-642-66282-9`, gives the classical finite-dimensional perturbation framework in which degenerate and nearly degenerate spectral subspaces are treated as clusters rather than as individually stable eigenvectors.

The square-root perturbation step is the same classical ingredient already audited in `VIS-373`; see Bernhard A. Schmitt, **Perturbation bounds for matrix square roots and Pythagorean sums**, *Linear Algebra and its Applications* 174 (1992), 215--227, DOI `10.1016/0024-3795(92)90052-C`.

No novelty is claimed for spectral clustering, block pinching, Weyl/Hermitian eigenvalue perturbation, degenerate perturbation theory, square-root perturbation, or the observation that a scalar operator is invariant under internal rotations. The Mathia-specific result is the accounting consequence for the Wang branch: the near-degenerate-cluster escape left after `VIS-373` collapses to an explicit two-scale error budget consisting of a resolved-gap commutator term plus the within-cluster Gram width.

## Dependencies

- `VIS-367`: growing positive compact polynomial depth already carries a universal source-free Chebyshev/capacity collapse.
- `VIS-368`: uniformly comparable positive metrics change Wang singular values only by bounded factors.
- `VIS-369`: freely aligned degenerating metrics can prescribe the active singular spectrum and therefore are non-identifying without their metric cost.
- `VIS-370`: exactly commuting positive metrics are sectorwise spectral filters/preconditioners of the baseline Gram.
- `VIS-371`: coordinate-free positive metric rules built only from one Gram are forced into the commuting class.
- `VIS-372`: commuting external Hermitian structure still provides only joint spectral filtering.
- `VIS-373`: resolved-gap orientation is controlled by the gap-normalized commutator and identified near-degenerate clusters as the remaining loophole.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue further narrowed by this result.

## Research consequence

The positive-Hilbert metric frontier is now sharper than the raw “noncommuting external geometry” criterion. A proposed Wang metric should first choose a physically justified spectral resolution, cluster the source-free Gram at that scale, and report four quantities together: the within-cluster width `eta`, the inter-cluster separation `gamma`, the metric bounds `m,M`, and the commutator size `||[G,C]||_F`.

If

`||G||_op sqrt(M/m) ||[G,C]||_F/gamma + 2M eta`

is negligible on the destination squared-singular-value scale, the candidate is spectrally approximated by an exactly `G`-commuting positive metric and remains a preconditioning effect. Large eigenvector rotation inside a narrow cluster is not an escape by itself.

A future positive result must therefore import and pay for a genuinely resolved orientation/topology, or leave this finite-dimensional positive-Hilbert representation class.