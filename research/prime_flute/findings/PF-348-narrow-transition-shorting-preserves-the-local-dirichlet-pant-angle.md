# PF-348 — narrow transition shorting preserves the local Dirichlet pant angle

**Status:** EXACT-DERIVED + LOCAL-PDE-FORM-COMPARISON + NARROW-BAND-OBSTRUCTION + GLOBAL-TRANSITION-ANGLE-OPEN.

For a sufficiently narrow but **fixed positive-width** physical transition band, the actual two-pant Dirichlet module retains an order-one normalized edge correlation after eliminating every transition cosine on that module. This includes its nonsingular pant energy and natural symmetric seam term, rather than just PF-346's solvable corridor model.

The boundary condition is essential: all other cuff data are held at zero, and the local relaxation stays in the symmetric cosine channel. This is not the Schur complement obtained by freeing transition data throughout the flute, nor by freeing the other seam-parity channel. It therefore does not establish noncompactness of the globally completed angle. It closes the local-Dirichlet version of the narrow-band repair and identifies precisely where a different global answer must enter.

## Object and claim

Use PF-205/PF-216's natural seam cut, PF-341's centered physical cuff coordinate, and PF-344's positive shifted energy. Let `M=Q+Lambda_E` be the complete raw positive seam form. Let `M_n^D` be its restriction to boundary traces supported on cuff module `n`, equal on its two faces and even in the common zero-twist coordinate. Every other boundary trace is zero. Thus `M_n^D` contains the two exact adjacent pant self-DtN forms, with zero Dirichlet datum on their other finite boundaries, plus the actual symmetric seam form. It is not an exterior Schur complement over neighboring cuffs.

Use the normalized symmetric cosine basis of PF-344; its fixed two-face normalization factors are absorbed into constants below. Write

\[
L=L_n,\qquad d=2\pi/L,\qquad
D=D_n=\frac{s_{n-1}^{-1}+s_n^{-1}}L,\qquad b_0=19/80.
\tag{1}
\]

Fix `kappa>0` and set `K=kappa+1`. There exists `eta_0>0`, independent of `n`, such that for every fixed `0<eta<eta_0` the following holds after a finite head (which may depend on `eta`). Define

\[
\alpha_n=d\lfloor\kappa/d\rfloor,\qquad
\beta_n=d\lceil(\kappa+\eta)/d\rceil,
\]
\[
J_n=\{\alpha_n,\alpha_n+d,\ldots,\beta_n\},\quad
X_n=\{\alpha_n,\beta_n\},\quad T_n=J_n\setminus X_n.
\tag{2}
\]

The set `T_n` is exactly the full positive cosine lattice in the open physical interval `(kappa,kappa+eta)`. It has `eta L/(2pi)+O(1)` elements. Both endpoints are nonconstant for large `n`. Let

\[
H_n=(M_n^D)_{J_nJ_n},\qquad
S_n^D=H_n^{/T_n}
=H_{XX}-H_{XT}H_{TT}^{-1}H_{TX}.
\tag{3}
\]

All these matrices are finite and strictly positive. The claim is

\[
\boxed{\quad
\rho_n^D:=\frac{|(S_n^D)_{12}|}
{\sqrt{(S_n^D)_{11}(S_n^D)_{22}}}\ge\frac12
\quad\text{for all sufficiently large }n.\quad}
\tag{4}
\]

No bounded-rank replacement of `T_n` is made. The same proof applies to either individual adjacent pant self-DtN form with its other finite boundary fixed at zero, replacing `D` by `1/(sL)`.

## 1. A narrow Fourier cluster has a controllable Gram conditioning exponent

For the consecutive frequencies `xi_i` in `J_n`, define exactly as in PF-346

\[
G_{ij}=\int_{\mathbb R}\cos(\xi_i t)\cos(\xi_jt)
\operatorname{sech}t\,dt
=\frac{\pi\sqrt{(x_i+1)(x_j+1)}}{x_i+x_j},
\qquad x_i=\cosh(\pi\xi_i).
\tag{5}
\]

Let `N=|J_n|`, `m=N-1`. For large `n`, all frequencies belong to `[kappa/2,K]`. Put

\[
R=\cosh(\pi K),\quad v=\pi\sinh(\pi\kappa/2)>0,
\quad B=2R/v.
\]

Then `x_i+x_j<=2R` and `|x_i-x_j|>=vd|i-j|`. PF-346's exact Cauchy shorting formula, eliminating every node except `i`, gives the inverse diagonal identity

\[
(G^{-1})_{ii}
=\frac{2x_i}{\pi(x_i+1)}
\prod_{j\ne i}\left(\frac{x_i+x_j}{x_i-x_j}\right)^2.
\tag{6}
\]

Index `i=0,...,m`. Since

\[
i!(m-i)!=\frac{m!}{\binom mi}\ge\frac{(m/e)^m}{2^m},
\]

we obtain

\[
(G^{-1})_{ii}\le\frac2\pi
\left(\frac{2eB}{dm}\right)^{2m}.
\]

Positivity gives `||G^{-1}||<=Tr(G^{-1})`, so

\[
\boxed{\lambda_{\min}(G)\ge
\frac{\pi}{2N}\left(\frac{dm}{2eB}\right)^{2m}.}
\tag{7}
\]

Here `dm=beta_n-alpha_n=eta+O(L^{-1})`. Consequently, with

\[
a(\eta)=\frac\eta\pi\log\frac{2eB}{\eta},
\tag{8}
\]

for every fixed `a>a(eta)` we have

\[
\lambda_{\min}(G)\ge e^{-aL}
\tag{9}
\]

after a finite head. The important limit is `a(eta)->0` as `eta->0`. The estimate controls **all coefficient combinations**, including minimizing transition compensators. Individual Gram diagonals would not suffice.

Choose `eta` small enough that `a(eta)<b_0`, and fix `a` strictly between them. This choice will be narrowed once more in Section 3.

## 2. The actual Dirichlet module is uniformly comparable to the whole Gram form

For coefficients `z=(z_i)` put `v_z(t)=sum_i z_i cos(xi_i t)`. PF-216 gives a growing corridor in each adjacent pant with

\[
T_s=\operatorname{arsinh}(\theta/\sinh s),\qquad
\ell_s(t)\asymp s\cosh t\quad (|t|\le T_s),
\tag{10}
\]

where `theta>0` is fixed and the comparison constants are uniform after the natural strip removal. Since the other finite boundary has **zero** datum, dropping the tangential and mass energies and applying Cauchy--Schwarz along each Fermi ray gives, for arbitrary coefficients,

\[
\mathcal E_{A(s,L)}(\sqrt{2/L}\,v_z)
\ge\frac{c}{sL}\int_{-T_s}^{T_s}|v_z(t)|^2
\operatorname{sech}t\,dt.
\tag{11}
\]

This is the PF-341 raywise lower argument applied to the complete trace, not just its fixed test pair. Its constants do not depend on the number of frequencies. The zero-twist identification makes it valid at the same origin in both adjacent pants.

Let `T_*=min(T_{s_{n-1}},T_{s_n})` and let `G_*` be (5) with the integral restricted to `[-T_*,T_*]`. The seam energy is nonnegative, hence

\[
H_n\ge c_1D G_*.
\tag{12}
\]

The canonical prime-flute scales in PF-216/PF-344, using the established Baker--Harman--Pintz input, give

\[
T_*\ge b_0L-C,\qquad D\ge c e^{b_0L}/L,\qquad w_n=O(1).
\tag{13}
\]

Indeed `s_{n-1},s_n<=C P_n^{-19/40}`, `L<=2 log P_n+O(1)`, and `T_s=log(1/s)+O(1)`. No bound on a ratio of adjacent prime gaps is required.

The missing part of the Gram integral is bounded as a form by

\[
0\le G-G_*\le4N e^{-T_*}I.
\tag{14}
\]

To see this, use `|v_z(t)|^2<=N||z||_2^2` and
`integral_(|t|>T_*) sech(t) dt<=4e^{-T_*}`. Combining (9), (13) and (14) yields

\[
0\le G-G_*\le\delta_n G,\qquad
\delta_n\le C N e^{-(b_0-a)L}\longrightarrow0.
\tag{15}
\]

This is a **relative** justification of the full Gram lower bound on the specified narrow cluster. It does not assume that the geometric corridor covers an entire cuff period.

In the other direction, the actual two-pant trial PF-344 (13) gives

\[
z^*H_nz\le C_1D z^*Gz+C_2(1+w_n)\|z\|_1^2
\le C_1D z^*Gz+C_3N\|z\|_2^2.
\tag{16}
\]

Thus its nonsingular chart/seam cost is also relatively small:

\[
\frac{C_3N}{D\lambda_{\min}(G)}
\le C NL e^{-(b_0-a)L}\longrightarrow0.
\tag{17}
\]

Equations (12), (15)--(17) prove that there are fixed `0<c<C<infinity` such that

\[
\boxed{cDG\le H_n\le CDG.}
\tag{18}
\]

These constants can be chosen independently of every sufficiently small fixed `eta`: the geometric and trial constants use the common fixed band `[0,K]`, and the two relative errors are eventually at most fixed numerical tolerances. Only the starting tail depends on `eta`.

This differs from an asymptotic identification `H_n=DG+o(DG)`. The leading geometric comparison may retain a nonunit constant ratio `C/c`. That is sufficient for the narrow-angle argument below.

## 3. Shorting preserves the comparison, and a small model angle survives it

Let `S_0=(DG)^{/T_n}`. The variational minimum for a positive Schur complement, applied to (18), gives

\[
cS_0\le S_n^D\le CS_0.
\tag{19}
\]

PF-346 gives its scalar canonical correlation exactly:

\[
\rho_{0,n}=\frac{2\sqrt{x_{\alpha_n}x_{\beta_n}}}
{x_{\alpha_n}+x_{\beta_n}}
\longrightarrow
\rho_*(\eta)=
\frac{2\sqrt{\cosh(\pi\kappa)\cosh(\pi(\kappa+\eta))}}
{\cosh(\pi\kappa)+\cosh(\pi(\kappa+\eta))}.
\tag{20}
\]

The mixed sign of `S_0` may alternate with `|T_n|`; use that sign in the following comparison. Rescale and sign the two retained coordinate vectors to obtain `u,v` with `S_0[u]=S_0[v]=1` and `S_0[u,v]=rho_(0,n)>0`. Then

\[
S_n^D[u-v]\le2C(1-\rho_{0,n}),\qquad
S_n^D[u],S_n^D[v]\ge c.
\]

For `A=S_n^D[u]`, `B'=S_n^D[v]`, polarization and
`A+B'>=2sqrt(AB')` imply

\[
\frac{S_n^D[u,v]}{\sqrt{AB'}}
\ge1-\frac{C}{c}(1-\rho_{0,n}).
\tag{21}
\]

In particular this signed correlation is positive whenever the right side is. Since `rho_*(eta)->1` as `eta->0`, choose `eta_0` small enough that, in addition to the conditioning requirement,

\[
(C/c)(1-\rho_*(\eta))<1/4\qquad(0<\eta<\eta_0).
\tag{22}
\]

Equation (21) is then greater than `1/2` for all sufficiently large `n`, proving (4). The bound does not assert that the actual correlation equals the model's limit.

## Why this does not decide global transition shorting

The Dirichlet condition in (11) is lost when neighboring cuff transition data are freed. Then the singular ray energy controls the **difference of two boundary traces**, and a neighbor may follow the selected trace. Equations (12) and (18) have not been proved on that larger space.

More relaxation gives `S_global<=S_local` on the same retained pair, but normalized correlation is not monotone under this order. An exact finite control makes the logical gap explicit. For `0<r<1`, consider

\[
\mathcal M=\begin{pmatrix}
1&r&\sqrt r\\ r&1&\sqrt r\\ \sqrt r&\sqrt r&1
\end{pmatrix}>0.
\tag{23}
\]

Fixing the third coordinate at zero leaves correlation `r`; freeing it gives the Schur complement `(1-r)I_2`, with correlation zero. Positivity follows from this strictly positive Schur complement and the positive final pivot. Thus even a large local correlation need not survive one additional relaxation coordinate.

No example is asserted to realize (23) on the flute. It demonstrates why neither positivity nor separated local witnesses permit a global noncompactness conclusion here. The unrestricted transition problem also includes other parity variables; those have not been eliminated in (3).

## Prior art, audit, and evidence boundary

Cauchy inversion and structured Schur elimination are classical. The diagonal identity (6) follows directly from PF-346's proved product formula; nearby primary literature is Gohberg, Kailath and Olshevsky, *Fast Gaussian Elimination with Partial Pivoting for Matrices with Displacement Structure* (1995), [author manuscript](https://www2.math.uconn.edu/~olshevsky/papers/geppdsam.pdf), already S23. No new Cauchy identity is claimed. Equations (7)--(9) are the elementary factorial specialization needed here.

Angle distortion between comparable positive forms is classical generalized Wielandt theory; see Lin and Sinnamon, *The Generalized Wielandt Inequality in Inner Product Spaces*, Theorem 2.4, [arXiv:1201.6294](https://arxiv.org/abs/1201.6294). Equation (21) is a weaker bound proved above without importing that theorem. Shorting monotonicity is the classical S24 principle. For wider geometric context, Wentworth's [DtN gluing and degeneration work](https://arxiv.org/abs/2209.11863) studies a different determinant problem and supplies no missing global transition estimate here.

The project-specific delta is the conditioning exponent `a(eta)->0`: it lets the actual corridor truncation and nonsingular pant cost be controlled **on every combination in a growing transition cluster**, using the existing prime-flute geometric growth exponent. This establishes a two-sided local-PDE comparison that PF-346/PF-347 explicitly lacked. It is distinct from PF-343, which does not eliminate transition variables, and PF-310, which frees a many-module low-frequency reservoir for a different constant-mode question. No broad novelty claim or new arithmetic theorem is made.

The proof uses PF-216's ray geometry, PF-344's uniform trial for bounded-frequency sums, and PF-346's exact Gram algebra. As supplementary checks, 320-digit arithmetic on the six lattice bands with `kappa=0.8`, `L in {200,600,1200}` and `eta in {0.04,0.1}` verified (6), (7), and (20); their dimensions were `3,5,6,11,10,21`. On each band, eight positive forms built as `chol(G) W chol(G)^*`, with diagonal entries of `W` drawn from `[0.4,3]` using seed `348`, verified the shorted sandwich (19) and angle bound (21): 48 controls passed. These checks test the algebra at finite precision; they do not certify the unknown geometric cutoff `eta_0`, solve the pant PDE, or independently validate its geometric inputs.

A falsification would require failure of the arbitrary-trace ray lower bound with the other finite boundary fixed to zero, failure of PF-344's coefficient-dependent upper trial, or failure of the uniform narrow-cluster conditioning estimate. The cutoff is fixed away from zero; the proof does not establish the same estimate at the zero-frequency degeneracy, for a wide fixed band, for a shrinking-width limit without renewed uniformity, for unbounded frequencies, or for the full parity/global relaxation.

The result applies equally to nonprime controls with the same corridor geometry, trial bound, and positive exponential growth margins in (13). Primality supplies those margins here; this is not a prime-specific spectral invariant or an RH implication. For the active clue, a sufficiently narrow local transition band cannot erase the normalized Dirichlet-module witness through its nonsingular pant terms alone. The remaining decisive question is what the additional parity and intermodule transition freedoms do to that witness.
