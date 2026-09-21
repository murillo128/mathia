# MI-067 — Thin positive Kron contrast cannot create extensive mass, and summable deleted-layer coupling kills its unscaled outliers

**Evidence level:** exact/asymptotic spectral synthesis from [PC-392](../../findings/PC-392-fixed-gap-log-determinants-cannot-amplify-the-thin-multi-deletion-contrast-sector.md), [PC-393](../../findings/PC-393-complete-survivor-connectivity-closes-the-singular-normalized-determinant-edge.md), [PC-394](../../findings/PC-394-summable-deleted-layer-coupling-closes-the-kron-outlier-window.md), and [PC-395](../../findings/PC-395-jacobsthal-gap-control-closes-all-summable-kron-outlier-windows.md), sharpening the exceptional-observable escape left by PC-391.

PC-391 isolates the irreducible simultaneous-deletion correction as a positive semidefinite contrast operator `Delta_T` of rank at most `k-1`. PC-392 shows that positive-regularized determinant ratios reduce exactly to this thin sector and cannot create an extensive normalized log-determinant. PC-393 closes the apparent singular loophole: the common constant zero mode lies outside the contrast carrier, complete survivor connectivity gives a mean-zero spectral floor, and the same normalized determinant conclusion persists through the exact pseudodeterminant endpoint.

PC-394 then controls amplitude. Writing

`Delta_T = P Q P^*`, with `0<=Q<=K`,

where `K` is the internal deleted-layer Laplacian and the columns of `P` are normalized incidence profiles, gives `||Delta_T||_op<=tr K`. On a fixed polynomial primorial window `H=p^u`, coarse spacing of the deleted vertices yields

`||Delta_T||_op = O(p^(u-1-2 alpha)/log p)`

for inverse-power chord exponent `alpha>1/2`. This already closed every unscaled outlier throughout `2<u<=1+2 alpha`, including `2<u<=3` for inverse square.

PC-395 removes the apparent longer-window escape from the same positive summable phase. The deleted layer is `q`-separated, while Jacobsthal gap control places every deleted point within `J(q)` of a survivor. The normalized incidence map therefore satisfies a local overlap bound of order `1+J(q)/q`, while the internal deleted-layer Laplacian satisfies `||K||_op<<q^(-2 alpha)`. Combining these estimates gives

`||Delta_T||_op << (1+J(q)/q) q^(-2 alpha)`.

The classical bound `J(q)<<q^2` then implies `||Delta_T||_op=O(q^(1-2 alpha))->0` for every `alpha>1/2`, independently of the deletion count and hence independently of the fixed polynomial window exponent `u`, provided the local-arc regime `H=o(M)` is maintained. The threshold `u=1+2 alpha` from PC-394 was therefore a proof boundary, not a spectral phase transition.

The reusable distinction is between **thin rank**, **nonlinear amplification**, **operator amplitude**, and **local overlap geometry**. Vanishing rank alone does not rule out an exceptional eigenvalue; determinant control alone does not either. Here the source-forced coarse deleted-layer spacing plus local survivor covering bounds the norm of the entire irreducible contrast and closes every fixed-polynomial-window unscaled outlier in the positive summable regime.

The positive linear-Kron branch can no longer survive merely by taking a longer fixed polynomial primorial window. A genuinely different mechanism must change the resource: nonsummable interactions `alpha<=1/2`, a source-justified renormalized observable, cross-level orientation/evolution of contrast subspaces, signed or indefinite kernels, nonlinear elimination, or state information not exhausted by positive graph-Laplacian Schur complementation.

**Boundary.** PC-395 uses positive inverse-power chord conductances with `alpha>1/2`, successive primorial deletion, the local-arc condition needed for the geometric comparison, and classical Jacobsthal gap control. It does not rule out rescaled observables whose normalization is independently justified, nonsummable kernels, signed/indefinite operators, nonlinear state spaces or cross-level information. None of the Kron results supplies a zeta-zero mechanism.
