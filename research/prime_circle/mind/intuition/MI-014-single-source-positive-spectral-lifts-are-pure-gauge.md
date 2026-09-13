# MI-014 — Complete-domain spectralization quotients the source; truncation leaves only window placement

**Evidence level:** exact for fixed source-independent positive/Hermitian wrappers through [PC-278](../../findings/PC-278-single-source-dual-window-phase-spectra-are-diagonal-unitary-pure-gauge.md), complete-torus anchored nonlinearities through [PC-279](../../findings/PC-279-full-dual-torus-anchor-nonlinearities-are-source-blind-fourier-data.md), and the truncated-window classification through [PC-280](../../findings/PC-280-window-source-mismatch-is-a-cyclic-convolution-finite-section.md). Whether the surviving finite-section placement carries an arithmetic discriminator remains open.

For a fixed coefficient mask, the single-source dual phase field factorizes as `D_p A E_r`, so singular values, Schatten norms, rank and Gram spectrum are source-independent. PC-279 shows that arbitrary anchored pointwise nonlinearities remain equally blind on the complete coefficient torus: multiplication by `p,r` only permutes rows and columns, leaving a one-dimensional Fourier-magnitude spectrum.

PC-280 identifies exactly what survives when the coefficient domain is truncated. For a symmetric window `H_B` and profile `f`,

`M_(p,r;B)^f(h,k)=f(ph+rk)`

is, up to row/column permutation, the two-sided finite section

`E_(pH_B) C_f E_(rH_B)^*`

of one **source-independent cyclic convolution operator** `C_f`. After Fourier diagonalization it is unitarily equivalent to

`P_(p,B) D_f P_(r,B)`,

where `D_f` depends only on the profile and the source enters only through the two rank-`N` Dirichlet-kernel projections associated with the dilated windows.

This sharpens the surviving carrier. Truncation does not create a new source-dependent symbol or two-dimensional phase operator. It prevents the multiplicative source action from being quotiented out because the distinguished additive window is not invariant. The only source information left in this class is therefore **where the two source-dilated windows sit around a fixed convolution/Fourier multiplier**.

A viable positive spectral mechanism in this family must show that the concentration spectrum of `P_(p,B) D_f P_(r,B)` retains a source-specific residual after the strongest source-only matched control. Pure phases and the complete-window limit remain exact controls. Genuine coefficient-graph flux, cross-source/cross-level couplings and other constructions not reducible to this finite-section placement are separate escape classes.

**Boundary.** PC-280 does not make the truncated spectrum source-blind and does not solve the intermediate rational-microscopic scalar regime. It classifies the retained information channel so future work can attack window/source mismatch directly instead of adding more local nonlinear structure that only changes `D_f`.