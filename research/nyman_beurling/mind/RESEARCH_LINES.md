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

NB-307 identifies the spectrum after quotienting that exact unit core with a generalized residual-Gram pencil `(mR,S)`. Its determinant is bounded below by the canonical multiplicative pivot-survival product `prod_(j=q+1)^N c_(m,j)^2`, where `c_(m,j)=sqrt(m) sigma_(mj)/sigma_j` comes from NB-290. NB-308 then uses reciprocal-shell Möbius inversion to prove the pointwise pivot floor `sigma_n >= sqrt(3/2)/(pi n)`, making the determinant certificate explicit but only factorially/exponentially small across an `O(N)` band.

NB-309 shows that this tiny determinant bound is principally an artifact of multiplying pointwise pivot floors. Stacking the same shell coefficient extractors and exploiting their divisibility sparsity with a Schur bound gives the direct residual-Gram estimate

`1-s_post(N,m)^2 >= 1 / (5(1+sqrt(2)) m N^2 H_(mN) (H_N-H_q))`.

Consequently the first singular value below the exact core is separated from `1` by at least a polynomial amount; uniformly for `2<=m<=N`, the squared gap is `Omega(1/(N^3 log^2 N))`.

NB-310 supplies the complementary upper construction and resolves the first branch of the transition question. Let `h=m(q+1)-N` be the overrun of the first product index beyond the finite section. The next canonical innovation after the exact core gives

`0 < 1-s_post(N,m)^2 <= min(1, (2 pi^2/3) h^2 C_(N+h)/m)`,

with `C_n=O(log n)`. Hence `h^2 log(N+h)/m -> 0` forces `s_post(N,m)->1`. In the first post-core strip, at `m=floor(N/2)+1`, the overrun is only `1` or `2` and

`1-beta_(N+1)(m)^2 = O(log N/N)`.

Thus explicit post-core near-isometries really do sit immediately beyond the exact unit plateau. NB-309 and NB-310 are compatible: the residual singular gap is nonzero and polynomially bounded below, yet it can still vanish polynomially along staircase boundary layers. The live source discriminator is now **where those near-isometric boundary layers end and whether the residual-Gram pencil develops a macroscopic lower edge deeper in the linear-to-quadratic transition**. One must classify the width and geometry of the staircase layers rather than ask whether post-core near-isometries exist at all.

Accordingly `m=N/2` is the exact end of the unit-norm plateau, NB-310 gives an explicit vanishing-gap regime just beyond staircase edges, NB-309 prevents superpolynomial collapse of the first post-core gap, and `m/N^2->infinity` is a sufficient full-decay regime. The unresolved source transition lies between these quantitative regions; neither the pivot floor nor one boundary-layer test vector determines its interior spectrum.

That source theorem is still not the destination theorem. After locating the strong singular subspaces one must propagate the actual moving first-free datum through the NB-298 sampling/null decomposition, lower-section conditioning and off-critical diagonal contraction. A large singular value that lives in a sample-null or unoccupied direction does not improve the Nyman target. The surviving destination question is therefore joint singular-spectrum **and target-occupation** control, not support mass, one-vector Rayleigh overlap, operator norm, or pivot survival alone.