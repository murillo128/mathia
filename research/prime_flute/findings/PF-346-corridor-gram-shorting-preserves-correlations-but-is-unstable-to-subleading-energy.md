# PF-346 — corridor Gram shorting preserves normalized correlations, but subleading energy can change the answer

**Status:** EXACT-DERIVED + CLASSICAL-CAUCHY-IDENTITY + CORRIDOR-MODEL-OBSTRUCTION + ACTUAL-DTN-ENDPOINT-OPEN.

The weighted cosine norm in PF-344's actual pant **upper trial** has an exactly solvable Gram matrix. Eliminating any finite set of transition cosines from this Gram matrix preserves all low/high canonical correlations on the retained frequency sets. In particular, its exponentially small shorted energies do not yield a small normalized angle. Moreover, a positive perturbation that is `o(D_n)` in the original coefficient-space operator norm can change an order-one residual correlation into a vanishing one.

This is a result about the specific corridor Gram form already used in PF-344/PF-345. It is **not** a noncompactness theorem for the transition-shorted prime-flute DtN operator. It identifies the scale at which a comparison with that operator must be proved; a leading raw-energy approximation is insufficient.

## Exact finite claim

For distinct nonnegative physical frequencies, define

\[
G(\alpha,\beta)=\int_{\mathbb R}
\cos(\alpha t)\cos(\beta t)\operatorname{sech}t\,dt,
\qquad x_\alpha=\cosh(\pi\alpha).
\tag{1}
\]

Partition a finite frequency set into retained sets `L,H` and an eliminated set `T`, and put `X=L union H`. All nodes are distinct; no negative-frequency duplicate of a cosine is included. Then

\[
G(\alpha,\beta)
=\frac{\pi\sqrt{(x_\alpha+1)(x_\beta+1)}}{x_\alpha+x_\beta}.
\tag{2}
\]

Every finite Gram matrix is strictly positive. Its exact Schur complement is

\[
\boxed{G^{/T}=B_T G_{XX}B_T,\qquad
B_T=\operatorname{diag}_{\alpha\in X}b_T(x_\alpha),\qquad
b_T(x)=\prod_{\tau\in T}\frac{x-x_\tau}{x+x_\tau}.}
\tag{3}
\]

In particular, for distinct retained frequencies,

\[
\boxed{
\frac{|G^{/T}(\alpha,\beta)|}
{\sqrt{G^{/T}(\alpha,\alpha)G^{/T}(\beta,\beta)}}
=\frac{2\sqrt{x_\alpha x_\beta}}{x_\alpha+x_\beta}.
}
\tag{4}
\]

The right side is independent of the number and locations of eliminated nodes. The **sign** need not be preserved: if every transition frequency lies strictly between `alpha` and `beta`, the residual mixed entry has sign `(-1)^{|T|}`. All singular values of the block-normalized `L/H` angle of `G^{/T}` equal those of `G_XX` with the same retained split. They are not asserted equal to those of a larger split containing `T`.

## Derivation and classical algebra

With `u=exp(2t)` and `z=(1+i omega)/2`, Euler's beta integral and reflection formula give

\[
\int_{\mathbb R}e^{i\omega t}\operatorname{sech}t\,dt
=\int_0^\infty\frac{u^{z-1}}{1+u}\,du
=\frac{\pi}{\sin\pi z}
=\pi\operatorname{sech}(\pi\omega/2).
\tag{5}
\]

Here `Re z=1/2`, so the integral converges absolutely. The cosine product identity yields

\[
G(\alpha,\beta)=\frac\pi2\left[
\operatorname{sech}\frac{\pi(\alpha-\beta)}2+
\operatorname{sech}\frac{\pi(\alpha+\beta)}2\right],
\tag{6}
\]

which simplifies to (2). Thus `G=W C W`, where
`C(x,y)=1/(x+y)` and `W_alpha=sqrt(pi(x_alpha+1))`.
The Cauchy matrix is strictly positive because

\[
C(x,y)=\int_0^\infty e^{-xr}e^{-yr}\,dr
\tag{7}
\]

and finitely many exponentials with distinct positive exponents are linearly independent.

Eliminating one node `a>0` gives the elementary identity

\[
\frac1{x+y}-\frac{2a}{(x+a)(y+a)}
=\frac1{x+y}\frac{x-a}{x+a}\frac{y-a}{y+a}.
\tag{8}
\]

Positive Schur complements can be taken successively. Diagonal congruence commutes with this elimination on the retained block; the scaling of an eliminated coordinate cancels between its two cross factors and its inverse pivot. Induction in (8) proves (3), independently of elimination order. Equation (4) follows by canceling the nonzero factors `|b_T|` and `W` against the two diagonal square roots.

For the block statement, let the raw retained blocks be `A,C` with mixed block `F`, and let `B_L,B_H` be the invertible diagonal restrictions of `B_T`. Set

\[
U_L=(B_LAB_L)^{-1/2}B_LA^{1/2},\qquad
U_H=(B_HCB_H)^{-1/2}B_HC^{1/2}.
\tag{9}
\]

These are orthogonal matrices, including when the diagonal scalings have negative entries. The shorted normalized angle is exactly

\[
U_L(A^{-1/2}FC^{-1/2})U_H^*.
\tag{10}
\]

This proves equality of its singular values with those of the unshorted **retained principal block**.

## Exponential raw suppression coexists with an order-one angle

Fix `0<kappa_-<kappa_+<K`. For cuff period `L_n` take all positive transition frequencies on the lattice `2pi k/L_n` strictly between the cutoffs. Their number is

\[
m_n=\frac{\kappa_+-\kappa_-}{2\pi}L_n+O(1).
\tag{11}
\]

For any retained and transition frequencies in `[0,K]`, set

\[
R=\cosh(\pi K)>1,\qquad r=\frac{R-1}{R+1}<1.
\]

All Cauchy nodes lie in `[1,R]`, so every factor in (3) has magnitude at most `r`. Since `G(alpha,alpha)<=pi`,

\[
G^{/T}(\alpha,\alpha)\le\pi r^{2m_n},\qquad
|G^{/T}(\alpha,\beta)|\le\pi r^{2m_n}.
\tag{12}
\]

A retained bounded-frequency set with `N_n=O(L_n)` nodes therefore has positive shorted trace at most `pi N_n r^{2m_n}`, exponentially small in `L_n`. But (4) is bounded below by

\[
\rho_K=\frac{2\sqrt R}{1+R}>0.
\tag{13}
\]

For the two exterior edge modes tending to `kappa_-` and `kappa_+`, its limit is explicitly

\[
\rho_*=
\frac{2\sqrt{\cosh(\pi\kappa_-)\cosh(\pi\kappa_+)}}
{\cosh(\pi\kappa_-)+\cosh(\pi\kappa_+)}>0.
\tag{14}
\]

Multiplying the entire Gram form by any `D_n>0` preserves these normalized conclusions. The Fourier normalization `sqrt(2/L_n)` on nonconstant cosines is likewise a harmless diagonal congruence. Thus this model exhibits the very combination at issue in PF-344/PF-345: growing-rank exponentially small raw trace relative to the corridor scale, with a nonvanishing normalized angle. This does not contradict their upper bounds for the actual geometry.

## A subleading positive term can reverse the model conclusion

Retain just the two exterior modes and all transition modes above. Compare the positive matrices

\[
M_n^{(0)}=D_nG_n,\qquad
M_n^{(1)}=D_nG_n+\delta_n P_X,\qquad
\delta_n=D_n r^{m_n},
\tag{15}
\]

where `P_X` is the coefficient-space orthogonal projection onto the two retained coordinates. Their difference has operator norm `delta_n=o(D_n)`. Since it changes neither the transition block nor its couplings,

\[
(M_n^{(1)})^{/T}=D_nG_n^{/T}+\delta_n I_X.
\tag{16}
\]

Its mixed entry is unchanged, while both diagonal entries are at least `delta_n`. Equations (12) and (16) give

\[
\rho_n^{(1)}\le\pi r^{m_n}\longrightarrow0,
\qquad \rho_n^{(0)}\longrightarrow\rho_*>0.
\tag{17}
\]

Thus even an **operator-norm** `o(D_n)` error in a leading raw corridor model is insufficient to determine the normalized transition-shorted angle. The perturbation is a positive mathematical control, not a claim that this precise diagonal term is realized by the flute.

A sufficient comparison scale can be stated without an inverse transition-block estimate. Let `S_0=D_nG_n^{/T}` on the selected pair, `A_n=diag(sqrt((S_0)_{11}),sqrt((S_0)_{22}))`, and let `S_act` be the pair compression of the **actual globally shorted** finite-section form. If

\[
\|A_n^{-1}(S_{\rm act}-S_0)A_n^{-1}\|\le\epsilon_n,
\tag{18}
\]

then its scalar canonical correlation obeys

\[
\rho_{\rm act}\ge
\frac{\rho_n^{(0)}-\epsilon_n}{1+\epsilon_n}
\quad\text{whenever }\epsilon_n<\rho_n^{(0)}.
\tag{19}
\]

Indeed, (18) bounds the scaled mixed-entry error by `epsilon_n` and both scaled diagonals above by `1+epsilon_n`. Condition (18) is **not established** for the flute. It requires errors measured against the much smaller shorted energies containing `b_T(x)^2`, not just against `D_n`.

## Prior art, novelty, and audit

The beta integral and reflection formula in (5) are classical; see NIST DLMF [5.12.3](https://dlmf.nist.gov/5.12.E3) and [5.5.3](https://dlmf.nist.gov/5.5.E3). Cauchy structure under Schur elimination is classical structured linear algebra: Gohberg, Kailath and Olshevsky, *Fast Gaussian Elimination with Partial Pivoting for Matrices with Displacement Structure*, Mathematics of Computation 64 (1995), 1557–1576, Sections 1–2, [author manuscript](https://www2.math.uconn.edu/~olshevsky/papers/geppdsam.pdf), DOI 10.1090/S0025-5718-1995-1312096-X. Normalizing Schur complements to obtain partial correlations is also standard; see Forrester and Zhang, *Parametrising correlation matrices*, Journal of Multivariate Analysis 178 (2020), 104619, equations (2.6)–(2.7), [arXiv:1812.07685](https://arxiv.org/abs/1812.07685).

No new Cauchy theorem, correlation theorem, or arithmetic structure is claimed. The project-specific consequence is the identification of PF-344's weighted cosine form with this exact class, and the resulting failure of a raw leading-kernel comparison to decide the active normalized-angle question. The explicit positive perturbation (15) demonstrates the missing stability requirement rather than merely warning that a denominator might be small.

As an exact algebraic sign check, for Cauchy nodes `1,2,4`, eliminate `2` and retain `1,4`. The residual diagonal entries are `1/18,1/72` and the mixed entry is `-1/45`; the squared correlation remains `16/25`. Exact rational Gaussian inversion on nodes `1,2,3,5,8,13`, over all 62 nonempty proper transition subsets, agreed with (3) in all 636 retained entries. These finite checks supplement the induction proof; they are not evidence about the pant PDE.

## Boundary and consequence for the line

PF-344 supplies a weighted upper trial plus a coefficient-dependent nonsingular cost. It does not identify the full `Q+Lambda_E` with `D_nG_n`, even to a two-sided accuracy on growing transition spaces. Global transition elimination also introduces couplings between modules. Neither its effect nor the nonsingular pant/seam terms may be dropped after the residual energy has become exponentially small. The model's block congruence does not supply an infinite-section inverse or justify transferring separated-module noncompactness from PF-342.

The result uses arbitrary real frequency sets and any positive scale `D_n`; primality plays no role. It is therefore a control on an intrinsic geometric approximation, not a prime-specific spectral invariant. It makes no assertion about the unbounded high-frequency sector, global weak trace class, scattering, zeta zeros, or RH.

For the active transition-band clue, pure weighted-corridor approximation is now an exact negative control: it preserves normalized correlations. A positive result for the actual flute must quantitatively use terms beyond this Gram form or prove a different normalized comparison. Conversely, transferring the model obstruction requires an estimate such as (18) for the same globally shorted finite sections and separate control of global assembly. The actual transition-shorted endpoint remains open.
