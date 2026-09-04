# VIS-025 — three-gap Pearson fibers are classical correspondence-analysis interaction spaces

## Claim

Let `P(i,j,k)` be a fully supported distribution on three consecutive `s`-state bins and let

`Q(i,j,k) = P_12(i,j) P_23(j,k) / P_2(j)`

be the adjacent-pair-preserving Markov closure from `VIS-020`. Write `Delta=P-Q` and use the Pearson-weighted residual from `VIS-024`,

`W_ijk = Delta_ijk / sqrt(Q_ijk)`.

For a fixed middle state `j`, put

`p_j = P(Y=j)`,
`R_j(i,k) = P(X=i,Z=k | Y=j)`,
`a_j(i) = P(X=i | Y=j)`,
`b_j(k) = P(Z=k | Y=j)`.

Then the Markov closure on that fiber is `Q_j=p_j a_j b_j^T`, and

`W_j = sqrt(p_j) D_(a_j)^(-1/2) (R_j-a_j b_j^T) D_(b_j)^(-1/2)`.

The matrix after `sqrt(p_j)` is exactly the standardized residual matrix of ordinary two-way **correspondence analysis** for the conditional table `R_j`. Thus the local likelihood geometry isolated in `VIS-024` is not a new visual metric: fiber by fiber it is classical correspondence-analysis chi-square geometry.

Moreover, if `A_j` and `B_j` have orthonormal columns spanning respectively

`sqrt(a_j)^perp` and `sqrt(b_j)^perp`,

then there is a unique interaction-coordinate matrix

`C_j = A_j^T W_j B_j`

with

`W_j = A_j C_j B_j^T`.

Hence each fiber has exactly `(s-1)^2` interaction coordinates, `||C_j||_F=||W_j||_F`, and the nonzero singular values of `C_j` and `W_j` agree. Changing orthonormal contrast bases rotates `C_j` on the left and right, so its singular values and Frobenius norm are invariant. Reordering bins also only applies orthogonal permutation matrices and leaves those quantities unchanged.

Consequently the exact Pearson energy is

`sum_ijk Delta_ijk^2 / Q_ijk = sum_j ||W_j||_F^2 = sum_j sum_l sigma_(j,l)^2`,

and the local KL expansion from `VIS-024` becomes

`2 I_P(X;Z|Y) = sum_j sum_l sigma_(j,l)^2 + higher-order terms`

for small relative departures from the Markov fiber. The singular spectrum is therefore a compact representation-invariant diagnostic of interaction strength, but it is **not lossless**: it forgets the orientation of the residual within the `(s-1)^2`-dimensional interaction space.

**Evidence/status:** `CLASSICAL-CORRESPONDENCE-ANALYSIS + EXACT-DERIVED SPECIALIZATION`.

No zeta-specific higher-order signal is established.

## Exact conditional-table identification

For fixed `j`, the triple slice has total mass `p_j`, so

`P_j(i,k)=p_j R_j(i,k)`.

Its row and column marginals are `p_j a_j` and `p_j b_j`. The adjacent-pair-preserving closure therefore satisfies

`Q_j(i,k)=p_j a_j(i)b_j(k)`

and

`Delta_j(i,k)=p_j [R_j(i,k)-a_j(i)b_j(k)]`.

Dividing cellwise by `sqrt(Q_j(i,k))` gives

`W_j(i,k)=sqrt(p_j) [R_j(i,k)-a_j(i)b_j(k)] / sqrt(a_j(i)b_j(k))`.

If

`S_j = D_(a_j)^(-1/2) (R_j-a_j b_j^T) D_(b_j)^(-1/2)`,

then

`boxed: W_j = sqrt(p_j) S_j`.

`S_j` is the standard correspondence-analysis matrix: the centered conditional contingency table after weighting rows and columns by the inverse square roots of their masses. Its squared Frobenius norm is the conditional Pearson chi-square inertia. The global weighted residual therefore decomposes exactly as

`||W||_F^2 = sum_j p_j ||S_j||_F^2`.

This is an exact identity, not an asymptotic approximation.

## Interaction subspace and contrast factorization

`VIS-024` derived the row/column-zero constraints on the unweighted residual:

`sum_k Delta_j(i,k)=0`,
`sum_i Delta_j(i,k)=0`.

Let `alpha_j=sqrt(a_j)` and `beta_j=sqrt(b_j)`, entrywise. Both are unit vectors because the conditional margins sum to one. The constraints become

`W_j beta_j = 0`,
`alpha_j^T W_j = 0`.

Thus `W_j` maps `beta_j^perp` into `alpha_j^perp` and vanishes on the two marginal directions. Choose isometries

`A_j : R^(s-1) -> alpha_j^perp`,
`B_j : R^(s-1) -> beta_j^perp`,

represented by `s x (s-1)` matrices with orthonormal columns. Since

`A_j A_j^T = I-alpha_j alpha_j^T`,
`B_j B_j^T = I-beta_j beta_j^T`,

we have exactly

`W_j = A_j A_j^T W_j B_j B_j^T = A_j C_j B_j^T`,

where

`C_j=A_j^T W_j B_j`.

The representation is unique once the two contrast bases are fixed. It gives `(s-1)^2` free coordinates, recovering the residual dimension in `VIS-024` and the Wilks degrees of freedom per middle state in `VIS-023`.

Because left/right multiplication by the isometries preserves Frobenius norm and nonzero singular values,

`||C_j||_F=||W_j||_F`

and

`singular_values(C_j)=nonzero_singular_values(W_j)`.

If another pair of orthonormal contrast bases is chosen, `A'_j=A_j O_A` and `B'_j=B_j O_B` for orthogonal `O_A,O_B`, then

`C'_j = O_A^T C_j O_B`.

Therefore the coordinate entries depend on the arbitrary contrast basis, but the singular values do not. A permutation of row or column bin labels likewise multiplies `W_j` by permutation matrices and leaves its singular spectrum unchanged.

## Relation to local likelihood information

`VIS-024` established on a fixed pair-marginal fiber that

`D(Q+Delta || Q)`
` = (1/2) sum Delta^2/Q`
`   + O(sum |Delta|^3/Q^2)`

when the relative perturbation is uniformly small. Since `D(P||Q)=I_P(X;Z|Y)` by `VIS-020`, the exact factorization above rewrites the quadratic term as

`2 I_P(X;Z|Y)`
` = sum_j ||C_j||_F^2 + higher-order terms`
` = sum_j sum_l sigma_(j,l)^2 + higher-order terms`.

So the local conditional-mutual-information geometry can be viewed as weighted correspondence-analysis inertia over the middle-state fibers. The exact Pearson energy is the sum of squared singular values; the equality with `2I` is only the already-stated local second-order KL approximation.

This distinction matters for the active zeta experiment. A large singular value says that one low-rank conditional-association mode dominates the Pearson geometry. It does not make that mode significant, arithmetic-specific, or stable under changing the partition.

## Visual consequence

The existing paired artifact

`research/visual_exploration/visualizations/three-gap-residual-whitening-geometry.md`

already shows why raw `Delta` and Pearson-weighted `W` answer different visual questions. The factorization here adds a third representation control without needing another visual claim: within each middle-state fiber, an SVD of `W_j` separates interaction **strength** from the arbitrary choice of row/column contrast coordinates.

For exploratory zeta-versus-CUE plots, the singular spectrum and cumulative inertia can therefore be used as bin-order/contrast-basis-invariant summaries alongside the full raw and Pearson residual maps. They should not replace those maps. Two residual tensors can have identical singular values while differing in singular vectors and hence in where the interaction lives.

The useful hierarchy is therefore:

- raw `Delta`: probability-mass localization;
- Pearson `W`: likelihood-sensitive localization;
- `C_j`: lossless interaction coordinates after removing the two marginal directions, but basis-dependent;
- singular values of `C_j`: basis/order-invariant interaction strengths, but orientation-losing.

Agreement across several of these deterministically related views is not independent evidence. Their purpose is to expose which apparent patterns are representation artifacts and which survive exact quotienting.

## Prior art and novelty assessment

Correspondence analysis is classical. Michael Greenacre, **Correspondence analysis**, *WIREs Computational Statistics* 2:5 (2010), 613–619, DOI `10.1002/wics.114`, describes CA as an SVD-based visualization of contingency tables in the chi-square metric. Marco Riani, Anthony C. Atkinson, Francesca Torti, and Aldo Corbellini, **Robust correspondence analysis**, *Journal of the Royal Statistical Society: Series C* 71:5 (2022), 1381–1401, DOI `10.1111/rssc.12580`, explicitly writes the standard matrix

`S=D_r^(-1/2)(P-r c^T)D_c^(-1/2)`

and performs its ordinary SVD.

Higher-way correspondence analysis is also established prior art. André Carlier and Pieter M. Kroonenberg, **Decompositions and Biplots in Three-Way Correspondence Analysis**, *Psychometrika* 61:2 (1996), 355–373, DOI `10.1007/BF02294344`, develops three-way correspondence-analysis decompositions of deviations from independence.

The present result does not claim a new correspondence-analysis method. It is the elementary **conditional specialization** relevant to Mathia's exact Markov closure: once the middle state is fixed, the residual from `VIS-020` is ordinary two-way conditional association, and the Pearson whitening from `VIS-024` is exactly `sqrt(p_j)` times the standard CA residual matrix. The useful durable result is the identification of which visual quantities are basis/order invariant and which information they discard.

## Boundary conditions and falsification

Full support is used so every `a_j(i)`, `b_j(k)`, and `Q_j(i,k)` is positive. With structural or sampling zeros, inverse-square-root weighting requires a reduced support and the interaction dimension can drop; deleting sparse cells after looking at the zeta data would invalidate the intended fixed-partition control.

The singular values are invariant under relabeling bins and orthogonal changes of contrast basis, but **not** under changing the bin boundaries, unfolding map, estimator, window, or middle-state partition. Those remain genuine representation choices and must be varied in the robustness analysis.

A singular spectrum also does not determine the residual matrix. Matching zeta and CUE singular values is weaker than matching the full residual law; conversely, a zeta-minus-CUE difference in one singular vector orientation can disappear if only singular values are retained. The spectrum is a robustness diagnostic, not a sufficient statistic for the empirical question.

Finally, empirical `W_hat` uses fitted pair marginals from overlapping triples. Standard iid cellwise CA uncertainty cannot be imported blindly. Significance still requires the matched finite-size process controls and process-level resampling already demanded by `VIS-024` and `CLUE-zeta-three-gap-conditional-residual`.

## Research consequence

`CLUE-zeta-three-gap-conditional-residual` remains live. Its empirical test can now report, for each fixed middle-state bin and for the aggregate over fibers, the raw residual, Pearson residual, CA singular values, and cumulative Pearson inertia under the **same** fixed partition for zeta and the matched finite-size CUE/arithmetic controls.

A candidate excess is more credible if it survives the move from cell coordinates to invariant interaction strength and reproduces across windows/heights, but the decisive evidence remains the zeta-minus-matched-control difference with correct finite-sample calibration. This finding supplies an exact representation quotient for that test; it does not predict that the quotient will contain an arithmetic signal.
