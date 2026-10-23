# PF-347 — natural seam energy cannot regularize the bounded-band corridor Gram model

**Status:** EXACT-DERIVED + CLASSICAL-FORM-COMPARISON + CORRIDOR-MODEL-OBSTRUCTION + ACTUAL-DTN-ENDPOINT-OPEN.

PF-346 proves that transition shorting preserves the normalized correlations of the weighted cosine corridor Gram form, but an unspecified positive perturbation that is small relative to the raw corridor scale can change that answer. The **actual symmetric seam energy**, restricted to a fixed bounded physical frequency band, is too small to be such a perturbation. It is uniformly form-small relative to the entire Gram matrix, including on its least energetic combinations. This comparison survives elimination of the full growing transition band.

Thus adding the natural seam block to this corridor model preserves its nonvanishing edge correlation. This narrows the missing comparison to the other pant contributions and global assembly. It does **not** identify the model with the actual exterior DtN form or decide the transition-shorted flute angle.

## Finite model and precise comparison

Use the intrinsic cuff period `L=L_n`, logarithmic endpoint increment `h=h_n`, symmetric seam width `w=w_n`, and adjacent core-separation parameters `s_-=s_{n-1}, s_+=s_n` of PF-205/PF-216/PF-344. Define

\[
D=\frac{s_-^{-1}+s_+^{-1}}{L},\qquad
s_{\mathrm{eff}}=(s_-^{-1}+s_+^{-1})^{-1}.
\tag{1}
\]

Fix `K<infinity`. Let `J` be any finite set of distinct **positive** integers with `xi_j=2pi j/L<=K`. The coefficient vector is in the normalized physical cosine basis `sqrt(2/L) cos(xi_j t)`. In precisely the coefficient convention of PF-346, put

\[
G_{ij}=\int_{\mathbb R}\cos(\xi_i t)\cos(\xi_j t)
\operatorname{sech}t\,dt,\qquad F=DG.
\tag{2}
\]

`F` is a defined corridor model, not a claimed equality for a pant response. Fixed positive scalar multiples of `F` satisfy the same conclusions with altered constants.

Let `Q_J` be the symmetric seam form restricted to these normalized modes. PF-342/PF-344 give

\[
0\le Q_J\le C_K w I.
\tag{3}
\]

For the displayed strip convention, its eigenvalue is
`sqrt(1+xi^2) tanh(w sqrt(1+xi^2))`, bounded by `w(1+K^2)`; only (3) is needed. More generally the result holds for every positive matrix obeying (3), without requiring diagonal entries only.

Uniformly in `J`, including its growing dimension,

\[
\boxed{
F\le F+Q_J\le(1+\epsilon_n)F,\qquad
\epsilon_n=\frac{2C_Kw_ns_{\mathrm{eff},n}}
{\operatorname{sech}(L_n/2)}=O_K(P_n^{-19/40})\longrightarrow0.
}
\tag{4}
\]

Here `P_n` is the neighboring prime scale of PF-205/PF-216. Partition `J=X disjoint-union T` arbitrarily and eliminate **all** coordinates in `T`. If

\[
S_0=F^{/T},\qquad S_1=(F+Q_J)^{/T},
\]

then

\[
\boxed{S_0\le S_1\le(1+\epsilon_n)S_0.}
\tag{5}
\]

There is no fixed-rank assumption on `T` and no bound on its inverse is inserted into the proof.

## Full-period coercivity, with the correct Fourier normalization

For `v(t)=sum_(j in J) a_j cos(2pi j t/L)`, orthogonality over one full cuff period gives

\[
\int_{-L/2}^{L/2}|v(t)|^2\,dt=\frac L2\sum_{j\in J}|a_j|^2.
\]

Restricting the positive integral defining `G` to this period therefore proves

\[
\boxed{G\ge\frac L2\operatorname{sech}(L/2)I,\qquad
F\ge\frac{\operatorname{sech}(L/2)}{2s_{\mathrm{eff}}}I.}
\tag{6}
\]

This is a bound for **all coefficient combinations**, not just individual Gram diagonals. Although the traces used to interpret the coefficients are normalized by `sqrt(2/L)`, `G` in (2) uses the unnormalized cosines: their normalization has already been incorporated into `D`, as in PF-344 (13) and PF-346. Inserting an additional `1/L` into (6) would mix these conventions.

The exact cuff law in PF-032 is `exp(-L/2)=tanh(h/4)`. The hyperbolic double-angle identity gives

\[
\operatorname{sech}(L/2)=\tanh(h/2)\asymp h.
\tag{7}
\]

PF-205 has `w asymp P^(-1)` and `h asymp g/P`, with odd-prime gap `g>=2`; hence `w/h` is uniformly bounded. PF-216 gives `s_-,s_+=O(P^(-19/40))` from the Baker--Harman--Pintz bound. Consequently

\[
\epsilon_n\lesssim_K\frac{w_n}{h_n}s_{\mathrm{eff},n}
\lesssim_K P_n^{-19/40}.
\tag{8}
\]

Equations (3) and (6) prove (4). Qualitative convergence needs only `w_n/h_n=O(1)` and `s_eff,n -> 0`; the BHP exponent supplies a convenient unconditional rate, not the mechanism.

For any retained `x`, the positive Schur variational identity is

\[
\langle x,F^{/T}x\rangle
=\min_{t\in T}\langle x+t,F(x+t)\rangle.
\tag{9}
\]

Taking the two minima in (4) proves (5). In particular, (4) controls the cost of the minimizing transition compensator even when its coefficients are large; a bound only for the retained seam diagonal would not suffice.

## Stability after diagonal normalization

Let `x,y` be any retained coordinate vectors and let `rho_i` be their scalar canonical correlation in `S_i`. Write `Delta=S_1-S_0`. By (5), `0<=Delta<=epsilon_n S_0`. Positivity gives

\[
|\Delta_{xy}|\le\epsilon_n\sqrt{(S_0)_{xx}(S_0)_{yy}},
\qquad
(S_0)_{jj}\le(S_1)_{jj}\le(1+\epsilon_n)(S_0)_{jj}.
\]

Thus, when `rho_0>epsilon_n`,

\[
\frac{\rho_0-\epsilon_n}{1+\epsilon_n}
\le\rho_1\le\rho_0+\epsilon_n.
\tag{10}
\]

There is also a dimension-independent block statement. Split `X=Lset disjoint-union Hset` and write the blocks of `S_i` as `A_i,B_i,C_i`, with normalized angle `Z_i=A_i^(-1/2) B_i C_i^(-1/2)`. Put

\[
H_L=A_0^{-1/2}A_1A_0^{-1/2},\quad
H_H=C_0^{-1/2}C_1C_0^{-1/2},\quad
E=A_0^{-1/2}(B_1-B_0)C_0^{-1/2}.
\]

Then `I<=H_L,H_H<=(1+epsilon_n)I` and `||E||<=epsilon_n`. The latter follows from Cauchy--Schwarz for the positive form `Delta` and its diagonal bounds. By polar decomposition, `Z_1` is left/right unitarily equivalent to

\[
\widetilde Z_1=H_L^{-1/2}(Z_0+E)H_H^{-1/2}.
\]

Since `||Z_0||<=1`,

\[
\|\widetilde Z_1-Z_0\|
\le2\left(1-(1+\epsilon_n)^{-1/2}\right)+\epsilon_n
\le2\epsilon_n.
\tag{11}
\]

Every corresponding singular value therefore changes by at most `2epsilon_n`, with no factor depending on the number of retained or eliminated modes.

For a fixed positive-width transition interval `(kappa_-,kappa_+)`, take its full positive Fourier lattice and the two exterior edge modes, all below a fixed `K>kappa_+`. PF-346 gives

\[
\rho_0\longrightarrow
\rho_*=
\frac{2\sqrt{\cosh(\pi\kappa_-)\cosh(\pi\kappa_+)}}
{\cosh(\pi\kappa_-)+\cosh(\pi\kappa_+)}>0.
\tag{12}
\]

Equation (10) proves the **same limit** for the model with `Q_J` added before transition elimination. The seam contribution cannot regularize this bounded-band model's correlation, even through a badly conditioned transition block.

## Prior art and evidence

The full-period estimate is the elementary Fourier quadratic-form mechanism behind classical Toeplitz eigenvalue bounds; see R. M. Gray, *Toeplitz and Circulant Matrices: A Review*, Section 4.2, Lemma 4.1 ([author text](https://ee.stanford.edu/~gray/toeplitz.pdf)). The cosine Gram matrix is a Toeplitz-plus-Hankel compression rather than a generic Toeplitz matrix; (6) is proved directly and does not require a spectral asymptotic theorem. Monotonicity and positive homogeneity of shorting are classical, as developed in W. N. Anderson, Jr. and G. E. Trapp, *Shorted Operators. II*, SIAM J. Appl. Math. 28 (1975), 60–71 ([DOI](https://doi.org/10.1137/0128007)); (9) supplies the complete finite-dimensional argument here.

No new Fourier, Schur-complement, or matrix perturbation theorem is claimed. The project-specific conclusion is that the **prescribed seam width and exact cuff law** put the symmetric seam in a uniformly small relative-form regime for PF-346's entire lattice Gram model. Its arbitrary `o(D_n)` perturbation counterexample cannot be specialized to this seam block. PF-032, PF-205, PF-216, PF-342/PF-344 and PF-346 supply the geometric scales, seam bound and model-correlation identity; S6 supplies the already-used prime-gap rate.

As supplementary numerical checks, 80-digit decimal arithmetic on the nonprime balanced controls `L=12,24,48`, `h=4 atanh(exp(-L/2))`, `s_-=s_+=h`, `w=h/100`, and `K=2.6` verified (6), both inequalities in (5), and (10). The transition interval was `(1,2)` and the full positive bounded bands had dimensions `4,9,19`. These finite controls check normalization and algebra; the proofs above establish the assertions, and these controls supply no pant-PDE evidence.

## Boundaries and consequence

- The lower bound (6) belongs to the **full weighted Gram model**. PF-344 uses that integral as an upper trial estimate for the actual pant. Restricting it to a full period does not create a lower bound for the actual DtN energy: the controlled thin corridor may cover less than that period.
- This result includes the seam on the eliminated transition modes, but excludes the nonsingular pant energy, changes to the corridor kernel, and transition couplings through other modules. PF-344's coefficient-dependent remainder is not bounded by (3). Those effects remain capable of changing the residual normalized angle.
- `K` is fixed. The proof does not control the unbounded high sector, an antisymmetric seam block of size `w^(-1)`, global shorting on the actual flute, or an infinite-section limiting operator. In particular it supplies no new noncompactness theorem for that operator.
- Fourier-lattice orthogonality and the common physical period are essential to (6). PF-346's arbitrary real-frequency statement does not automatically carry this perturbation bound.
- The argument applies to any geometric controls satisfying the same cuff law, bounded `w/h`, collapsing `s_eff`, and bounded-band seam estimate. The BHP rate instantiates it on the prime flute; it is not a new prime-specific invariant or an RH implication.

The live transition-band clue therefore cannot be settled by adding only the natural symmetric seam block to the solvable corridor model. A different answer for the actual flute must use the remaining pant structure or global transition elimination, with its effect measured after shorting and diagonal normalization.
