# MI-900 — Early-shell inversion makes projected-dilation source compression polynomial

**Evidence level:** proved source-compression bounds from [NB-300](../../findings/NB-300-reciprocal-cell-periodicity-gives-explicit-moving-cutoff-source-compression.md) and the stronger [NB-301](../../findings/NB-301-early-shell-mobius-inversion-gives-cubic-moving-cutoff-source-compression.md), combined with the exact projected-dilation factorization of NB-297--NB-299.

The large-dilation obstruction is not tied to the exponential reciprocal-cell period. For `U_N=span{g_2,...,g_N}`, NB-301 uses the first `N` harmonic shells and finite Möbius inversion to recover every coefficient of `u=sum a_jg_j`. The resulting uniform embedding

`sum_(j=2)^N |a_j| <= sqrt(6) N^(3/2)||u||_2`,

`||u||_infinity <= sqrt(6) N^(3/2)||u||_2`

implies both the source-Gram floor `lambda_min(G_N^(src))>=1/(6N^3)` and the dilation-overlap bound

`beta_(N+1)(m)^2=||P_(U_N)A_m|_(U_N)||^2 <= min(1,6N^3/m)`.

Thus the sufficient separation condition from NB-300, `m/P_N -> infinity` with `P_N=lcm(2,...,N)`, is far from intrinsic. Source compression already vanishes whenever

`m/N^3 -> infinity`.

In the first-free notation with old section `V_(n-1)`, put

`epsilon_cub(m,n)=min(1,sqrt(6(n-1)^3/m))`.

For a finite off-critical packet `Z`, the exact NB-299 factorization then gives

`||Xi_(m,n,Z)|| <= ||K_(n-1,Z)|| (m^(-delta_Z)+epsilon_cub(m,n))^2/[1-epsilon_cub(m,n)^2]`

whenever `epsilon_cub<1`. Consequently

`m/(n-1)^3 -> infinity` and `delta_Z log m -> infinity`

force `||Xi||/||K|| -> 0`, even while the section depth moves. Large source-space escape therefore cannot support persistent normalized destination occupation throughout the super-cubic dilation regime.

This sharpens the joint-scale frontier from NB-298--NB-300. A surviving projected-dilation mechanism must remain at or below cubic dilation scale, let the off-critical damping `delta_Z log m` stay weak, or rely on the separate sample-conditioning/target-occupation factors. The bound does **not** control `m=O(n^3)`, does not prove that `Xi` is small relative to the unresolved future-tail Gram `E`, and does not eliminate a moving packet whose condition number overwhelms the normalized estimate.

The reusable point is that the source-side conditioning escape is now polynomially priced by the actual canonical Nyman coordinates rather than by a common-period surrogate. What remains is genuinely destination-side: moving-packet sampling, off-critical displacement and occupation of the future representer/null tail.