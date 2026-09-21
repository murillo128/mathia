# MI-067 — Fixed-gap log-determinants cannot amplify a vanishing-density Kron contrast sector

**Evidence level:** exact/asymptotic spectral synthesis from [PC-392](../../findings/PC-392-fixed-gap-log-determinants-cannot-amplify-the-thin-multi-deletion-contrast-sector.md), sharpening the exceptional-observable escape left by PC-391.

PC-391 isolates the irreducible simultaneous-deletion correction as a positive semidefinite contrast operator `Delta_T` of rank at most `k-1`. A determinant could still have amplified that thin sector even when its rank fraction vanished. PC-392 shows that this does not happen for normalized log-determinants at a fixed positive spectral gap.

With `G_lambda=L_ind+lambda I` and the contrast factorization `Delta_T=U C U^*`, the determinant ratio reduces exactly to the deleted contrast space:

`det(L_red+lambda I)/det(L_ind+lambda I) = det(I + C^(1/2) U^* G_lambda^(-1) U C^(1/2))`.

For the positive normalized inverse-power chord kernels, positivity also gives `tr Delta_T=O(k)`. Hence on every fixed polynomial primorial window,

`0 <= (1/|S|) log(det(L_red+lambda_p I)/det(L_ind+lambda_p I)) <= O(log p/(p lambda_p))`.

Therefore every fixed `lambda>0`, and more generally every `lambda_p >> (log p)/p`, forces the normalized log-determinant correction to vanish. Taking a determinant does not create an extensive carrier that was absent from the contrast sector itself; the nonlinear wrapper remains limited by the sector's trace mass and density.

The determinant route is now confined to the singular edge: `lambda_p=O((log p)/p)` or smaller, the unregularized pseudodeterminant/mean-zero spectrum, unnormalized exceptional contributions, or cross-level evolution of the contrast subspaces. Those regimes require genuine small-eigenvalue or dynamical information rather than another fixed-gap determinant transform.

**Boundary.** The estimate uses positivity, the normalized prime-circle chord kernel, Laplacian Schur complementation and fixed polynomial windows. It does not control the singular pseudodeterminant regime, individual outliers, signed or indefinite kernels, nonlinear elimination, or non-Schur state spaces. No zeta-zero or critical-line mechanism is supplied.