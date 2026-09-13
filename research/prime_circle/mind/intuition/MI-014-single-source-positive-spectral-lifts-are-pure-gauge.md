# MI-014 — Complete-domain spectralization quotients the source; regular finite sections transport to Li-grid controls

**Evidence level:** exact for fixed source-independent positive/Hermitian wrappers through [PC-278](../../findings/PC-278-single-source-dual-window-phase-spectra-are-diagonal-unitary-pure-gauge.md), complete-torus anchored nonlinearities through [PC-279](../../findings/PC-279-full-dual-torus-anchor-nonlinearities-are-source-blind-fourier-data.md), the truncated-window classification through [PC-280](../../findings/PC-280-window-source-mismatch-is-a-cyclic-convolution-finite-section.md), and regular-profile whole-spectrum transport through [PC-281](../../findings/PC-281-regular-window-spectra-are-li-grid-reproducible.md). Microscopic/sharp profiles and non-single-phase constructions remain open.

For a fixed coefficient mask, the single-source dual phase field factorizes as `D_p A E_r`, so singular values, Schatten norms, rank and Gram spectrum are source-independent. PC-279 shows that arbitrary anchored pointwise nonlinearities remain equally blind on the complete coefficient torus: multiplication by `p,r` only permutes rows and columns, leaving a one-dimensional Fourier-magnitude spectrum.

PC-280 identifies exactly what survives when the coefficient domain is truncated. For a symmetric window `H_B` and profile `f`,

`M_(p,r;B)^f(h,k)=f(ph+rk)`

is, up to row/column permutation, the two-sided finite section

`E_(pH_B) C_f E_(rH_B)^*`

of one source-independent cyclic convolution operator `C_f`. After Fourier diagonalization it is unitarily equivalent to

`P_(p,B) D_f P_(r,B)`,

where `D_f` depends only on the profile and the source enters only through the two rank-`N` Dirichlet-kernel projections associated with the dilated windows. Truncation therefore retains only **window placement around a fixed multiplier**, not a new source-dependent symbol.

PC-281 now closes a broad part of that escape. If the phase profile is sampled from a bounded Lipschitz function `F_q` on the circle, the complete normalized ordered singular spectrum obeys

`||Sigma(x,y)-Sigma(x',y')||_infinity <= B L_q (d(x,x')+d(y,y'))`.

Combining this deterministic perturbation bound with the PC-277 prime-to-Li denominator-`q` transport shows that the **entire** spectral law is reproduced by the matched Li-grid control whenever the explicit transport error tends to zero; in particular for bounded amplitude and `B L_q=exp(o(sqrt(log q)))`. Smooth chord profiles, mollified anchor potentials and other regular Fourier multipliers therefore cannot produce an order-one prime-specific spectral residual in that regime.

This sharpens the surviving carrier again. It is not enough that truncation breaks the complete-domain permutation quotient. The retained placement information must vary at a scale too sharp for the classical source transport to follow, or the construction must leave the one-profile finite-section category entirely. Viable cases include exact microscopic selectors, the unsmoothed logarithmic anchor singularity, transition widths/Lipschitz constants large enough to defeat the PC-281 bound, source-dependent profiles, or genuinely cross-level/cross-source operators.

The intermediate rational-microscopic scalar window remains a separate unresolved channel. PC-281 does not close it merely by closing regular finite-section spectra.

**Boundary.** PC-281 is a no-go for regular profiles in its quantitative transport regime, not a theorem that every truncated spectrum is source-blind. Exact selectors and singular profiles deliberately fall outside its Lipschitz hypothesis. A future positive spectral claim must state both which complete-domain symmetry was broken and why the surviving sharp structure is not transported by the strongest matched source control.
