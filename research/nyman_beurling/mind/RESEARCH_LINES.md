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

NB-310 supplies the complementary upper construction just beyond the exact core. If `h=m(q+1)-N` is the overrun of the first product index beyond the finite section, the next canonical innovation gives a near-isometric post-core vector whenever `h^2 log(N+h)/m -> 0`. In the first post-core strip this already shows that the first integer steps past `m=N/2` have vanishing gap.

NB-311 shows that the square-root-width appearance in NB-310 was mainly a triangle-inequality loss. Keeping the exact endpoint remainder cancellation gives

`dist(g_(N+h),U_N)^2 << h/(N+h)^2 * (1+log(N/h))`

and hence the post-core bound

`0 < 1-s_post(N,m)^2 <= min(1, (2 pi^2/3) (h/m) (6H_(floor(N/h))+8+pi^2))`.

Therefore every moving family with `(h/m)(1+H_(floor(N/h)))->0` is post-core near-isometric. In the first post-core strip `N/2<m<=N`, this widens all the way to every sublinear additive overrun: `h=2m-N=o(N)` implies `beta_(N+1)(m)->1`. The exact unit plateau still ends sharply at `2m=N`; NB-311 does not extend the plateau, give an asymptotic formula for the gap, or control the target datum.

NB-312 adds a different lower mechanism that survives throughout the entire internal-dilation region. Testing `A_m g_2` against the in-section generator `g_m` gives

`beta_(N+1)(m) >= rho_m >= 1/(24 sqrt(log(2)(1+pi^2/6))) > 0.0307`

for every `2<=m<=N`, while

`rho_m -> (log(pi)-gamma)/(2 sqrt(log(2)(log(2pi)-gamma))) = 0.303553...`

as `m->infinity`. Thus no moving family with `m<=N` can have projected-dilation norm tending to zero; for macroscopic internal dilations the explicit anchored channel itself stays above about `0.30355`. This does not say that the top singular value stays near `1`.

NB-313 extends anchored non-decay beyond the finite-section boundary. For every `N>=32` and every external dilation `m>=N`, testing the same source anchor `g_2` against the edge generator `g_N` gives

`beta_(N+1)(m) >= c_ext sqrt(N/m)`,

where `c_ext=1/(32 sqrt(log(2)(1+pi^2/6))) > 0.0230`. The proof pulls the cross-correlation back to `(0,1]`; the first reciprocal shell alone forces a universal positive fractional-part integral, while the canonical neutralization term contributes only `O(1/N)`. More sharply, if `m/N->lambda` with finite `lambda>=1`, the normalized anchored correlation converges to a strictly positive profile `B(lambda)`. Hence any moving family with `beta_(N+1)(m)->0` must satisfy the necessary condition `m/N->infinity`.

NB-314 identifies the eventual external shape at each fixed section. If `mu_N` is reciprocal-period averaging and `p_N=P_(U_N)1`, then

`sqrt(m) T_(N,m) -> R_N`, with `R_N v = <v,p_N> r_N`,

where `r_N` represents `mu_N`. Hence `L_N:=||R_N||=||P_(U_N)1|| ||mu_N||`, so the far-external coefficient factors exactly into captured Nyman-target energy and reciprocal-shell mean susceptibility. The fixed-section proof alone is nonuniform because its elementary averaging argument sees the large common period `lcm(2,...,N)`.

NB-315 removes that lcm loss at the already-known superquadratic frontier. Farey control of centered shell partial sums gives the uniform primitive estimate `||G_u||_infinity=O(N^(5/2)||u||)`, and therefore

`||sqrt(m) T_(N,m)-R_N|| <= C_mix N^(5/2)/m`, with `C_mix<11`.

Because NB-314 also gives `L_N >> sqrt(N)`, this strengthens to the relative estimate

`||sqrt(m) T_(N,m)-R_N|| / L_N < 80 N^2/m`.

Thus every moving family with `m/N^2->infinity` satisfies `sqrt(m) beta_(N+1)(m)/L_N -> 1`, and the normalized projected-dilation operator itself converges to the normalized rank-one channel. The superquadratic region of NB-303 is therefore asymptotically rank one, not merely small. This does not lower the sufficient decay threshold: absolute operator error requires the stronger `m/N^(5/2)->infinity`, while the rank-one shape at quadratic scale is a relative statement against `L_N`.

Thus NB-309 and NB-311 still bracket the staircase boundary layer near the exact plateau edge, while NB-312 and NB-313 answer the separate question of complete source-overlap collapse across every bounded linear dilation scale. The post-core gap from `1` is always nonzero and has a polynomial lower bound internally; it can tend to zero throughout an `o(N)` neighborhood of the first plateau edge; deeper inside and just beyond the finite section the operator norm may move a macroscopic distance below `1`, but it cannot collapse to zero while `m/N` remains bounded.

Accordingly `m=N/2` is the exact end of the unit-norm plateau, NB-311 gives the current widest explicit vanishing-gap regime near staircase edges, NB-309 prevents superpolynomial collapse of the first internal post-core gap, and NB-312--NB-313 show that complete source-overlap decay requires a genuinely superlinear dilation `m/N->infinity`. `m/N^2->infinity` remains the sufficient full-decay regime, now sharpened by NB-314--NB-315 to a target-weighted rank-one asymptotic there. The unresolved source-side transition is whether that mixing/decay picture can be pushed into the genuinely intermediate window `N<<m<=O(N^2)`, or whether coherent centered shell modes survive and obstruct it.

That source theorem is still not the destination theorem. After locating the strong singular subspaces one must propagate the actual moving first-free datum through the NB-298 sampling/null decomposition, lower-section conditioning and off-critical diagonal contraction. A large singular value that lives in a sample-null or unoccupied direction does not improve the Nyman target. The surviving destination question is therefore joint singular-spectrum **and target-occupation** control, not support mass, one-vector Rayleigh overlap, operator norm, or pivot survival alone.
