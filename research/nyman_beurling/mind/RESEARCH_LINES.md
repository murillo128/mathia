# Nyman--Beurling research lines

This file records the current mathematical questions that survive the Nyman--Beurling evidence. It is not a roadmap, task queue, status page, or history.

## Keep aggregate Ford coverage separate from Hardy coercivity

NB-264--NB-272 show that large aggregate Ford response can coexist with a vanishing positive Hardy quadratic signal. Resolved shell bands can carry order-one point residue while their projected `H^2` energy leaks with rank, and positive band-diagonal repairs need rank-growing strength to restore a uniform anchored floor. The live destination-side fork remains: either the canonical target quantities themselves stay order one in the moving regime, or a new exact source component supplies the missing rank-growing Gram strength.

## Determine the singular-spectrum transition after the exact projected-dilation plateau

NB-284--NB-299 separate the source-side dilation geometry from destination occupation. The ordinary finite-section gain is a Parseval mass on a neutralized future-null block; macroscopic source escape, strong multiplicative-band coercivity, or large principal-angle motion do not by themselves force the actual first-free datum to occupy the useful subspace. At fixed packets the full future tail still controls every baseline-free gain.

NB-300--NB-303 give the moving-cutoff source upper bound

`beta_(N+1)(m)^2 <= min(1, 10N^2/m + 20N^4/(3m^2))`,

so `m/N^2->infinity` forces generic projected-dilation overlap to zero. NB-304 shows that quadratic scale is power-sharp for universal support localization, while NB-305 proves that its explicit high-index adjacent-cancellation extremizer can nevertheless have vanishing normalized dilation self-overlap. Retained support mass and projected operator norm are therefore different resources.

The sharpened NB-306 identifies the exact opposite endpoint. For `U_N=span{g_2,...,g_N}`, normalized integer dilation `A_m`, `q=floor(N/m)`, and `T_(N,m)=P_(U_N)A_m|_(U_N)`, the finite-section intersection is exactly

`A_m U_N intersect U_N = A_m U_q`,

and the complete unit right-singular subspace is exactly `U_q`. Hence singular value `1` has multiplicity `max(floor(N/m)-1,0)` and

`beta_(N+1)(m)=1` if and only if `2m<=N`.

NB-307 now resolves the algebraic form of the spectrum immediately after quotienting that unit core. On `H_(N,m)=U_N minus-orthogonal U_q`, the defect `I-T_(N,m)^*T_(N,m)` is exactly the generalized residual-Gram pencil `(mR,S)`, and its determinant is bounded below by the canonical multiplicative pivot-survival product

`prod_(j=q+1)^N c_(m,j)^2`, with `c_(m,j)=sqrt(m) sigma_(mj)/sigma_j` from NB-290.

Consequently the least post-core defect obeys

`1-s_post(N,m)^2 >= prod_(j=q+1)^N c_(m,j)^2`.

In the first post-core strip `N/2<m<=N`, this is directly `1-beta_(N+1)(m)^2`. The unresolved source question is therefore no longer only to estimate an opaque cross-Gram norm: **one concrete route is to lower-bound multiplicative-band pivot survival, equivalently to control `sum_(j=q+1)^N -log c_(m,j)`, while the exact residual-Gram pencil remains available if the determinant certificate is too lossy.** NB-290 currently gives only the opposite-direction bound `c_(m,j)<=1`, so a quantitative rate still requires new arithmetic input.

Thus `m=N/2` is the exact end of the unit-norm plateau, and `m/N^2->infinity` is a sufficient decay regime, with canonical pivot survival now exposing a metric mechanism that can open a gap between them.

That source theorem is still not the destination theorem. After locating the strong singular subspaces one must propagate the actual moving first-free datum through the NB-298 sampling/null decomposition, lower-section conditioning and off-critical diagonal contraction. A large singular value that lives in a sample-null or unoccupied direction does not improve the Nyman target. The surviving destination question is therefore joint singular-spectrum **and target-occupation** control, not support mass, one-vector Rayleigh overlap, operator norm, or pivot survival alone.