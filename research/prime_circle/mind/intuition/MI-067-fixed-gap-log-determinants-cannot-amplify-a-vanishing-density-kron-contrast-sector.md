# MI-067 — Thin Kron contrast cannot create extensive normalized determinant mass, even at the singular edge

**Evidence level:** exact/asymptotic spectral synthesis from [PC-392](../../findings/PC-392-fixed-gap-log-determinants-cannot-amplify-the-thin-multi-deletion-contrast-sector.md) and [PC-393](../../findings/PC-393-complete-survivor-connectivity-closes-the-singular-normalized-determinant-edge.md), sharpening the exceptional-observable escape left by PC-391.

PC-391 isolates the irreducible simultaneous-deletion correction as a positive semidefinite contrast operator `Delta_T` of rank at most `k-1`. PC-392 showed that at positive regularization the determinant ratio reduces exactly to this contrast space and cannot produce an extensive normalized log-determinant whenever `lambda_p>>(log p)/p`.

PC-393 closes the apparent singular loophole. Both the independent-star and true Kron Laplacians have the same constant zero mode, and `Delta_T 1=0`, so the determinant contrast lives entirely on the mean-zero subspace. The surviving boundary graph is complete and positive; on a fixed polynomial window `H=p^u`, every direct survivor edge has weight at least `c H^(-2 alpha)`. Hence

`lambda_2(L_ind) >= c |S| H^(-2 alpha)`.

Combining this intrinsic mean-zero conditioning floor with `rank Delta_T<=k-1`, `tr Delta_T=O(k)`, and `k/|S|=O(log p/p)` gives the uniform estimate

`sup_(lambda>=0) (1/|S|) log(det_lambda(L_red)/det_lambda(L_ind)) = O((log p)^2/p) -> 0`,

where `lambda=0` is interpreted through pseudodeterminants. Thus no nonnegative regularization scale, including the exact pseudodeterminant endpoint, turns the thin multi-deletion contrast into a nonzero normalized free-energy density in this positive complete chord-Laplacian family.

The important correction is conceptual as well as quantitative. The `lambda^(-1)` divergence in PC-392 was a bound on the full space and therefore saw the common constant zero mode. That mode is orthogonal to the source-sensitive contrast carrier. Once the carrier is restricted first, the singularity disappears and the remaining inverse grows only polynomially with the window, too slowly to overcome the vanishing contrast-rank fraction after the logarithm.

The determinant branch is therefore not reopened merely by taking `lambda_p` smaller. What remains are genuinely nonextensive or different-category observables: unnormalized determinant changes, individual outliers, cross-level evolution of the `k-1` contrast subspaces, or signed/indefinite/non-complete operators where positivity and the direct complete-edge floor fail.

**Boundary.** The conclusion uses the normalized positive inverse-power chord kernel, complete survivor connectivity, Laplacian Schur complementation and fixed polynomial primorial windows. It does not show that the unnormalized determinant ratio tends to one, does not rule out exceptional eigenvalues or cross-level dynamics, and does not extend by assertion to signed or non-complete operator categories. No zeta-zero or critical-line mechanism is supplied.