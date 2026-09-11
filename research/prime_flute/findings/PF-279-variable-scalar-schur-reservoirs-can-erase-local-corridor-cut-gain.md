# PF-279 — variable scalar Schur reservoirs can erase the local corridor cut gain

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + OPERATOR-THEORETIC + NEGATIVE/ROUTE-NARROWING`. PF-229 proves that a translation-invariant scalar serial completion preserves the isolated PF-228 corridor transmission scale up to a fixed factor. That conclusion does **not** extend from positivity and scalarity alone to variable serial completions. There is an explicit positive Jacobi precision family in which the isolated defect-edge transmission is `O(w/s)`, while the norm of the complete half-chain cut converges to a strictly positive constant because the two background reservoirs acquire diverging extension mass.

The correct scalar interface is an exact Weyl/Schur identity. If `A_L(eta),A_R(eta)` are the two positive half-chain compressions, including the diagonal contribution of the cut edge, `e_L,e_R` are their endpoint vectors, and `c>0` is the crossing conductance, define

\[
\beta_L(\eta)=\langle e_L,A_L(\eta)^{-1}e_L\rangle^{-1},
\qquad
\beta_R(\eta)=\langle e_R,A_R(\eta)^{-1}e_R\rangle^{-1}.
\]

For `A_{L/R}(eta)=A_{L/R}(0)+eta I`, the full cut block satisfies

\[
\boxed{
\|1_RM_\eta^{-1}1_L\|
=\frac{c\sqrt{\beta_L'(\eta)\beta_R'(\eta)}}
{\beta_L(\eta)\beta_R(\eta)-c^2}.
}
\]

Thus boundary impedance alone is not enough to control a complete cut. Its spectral derivative, equivalently the squared norm of the endpoint-normalized harmonic extension, is part of the exact invariant. This identifies a concrete missing quantity for the PF-222 nested-cut problem: before extrapolating PF-228/PF-229 to a variable flute, one needs control of the left/right extension Gram forms, or a proof that the physical `P/H` projections eliminate their amplification.

## Claim

### 1. Exact two-reservoir cut formula

Let `H_L,H_R` be Hilbert spaces, let `A_L(eta),A_R(eta)` be strictly positive self-adjoint operators with bounded inverses, and let `e_L,e_R` be unit endpoint vectors. Assume

\[
A_L(\eta)=A_L+\eta I,
\qquad
A_R(\eta)=A_R+\eta I.
\tag{1}
\]

Couple the two reservoirs by one scalar edge,

\[
M_\eta=
\begin{pmatrix}
A_L(\eta)&-c\,|e_L\rangle\langle e_R|\\
-c\,|e_R\rangle\langle e_L|&A_R(\eta)
\end{pmatrix}>0.
\tag{2}
\]

Put

\[
g_L(\eta)=\langle e_L,A_L(\eta)^{-1}e_L\rangle,
\qquad
g_R(\eta)=\langle e_R,A_R(\eta)^{-1}e_R\rangle,
\qquad
\beta_{L/R}=g_{L/R}^{-1}.
\tag{3}
\]

Then the right-left block of `M_eta^{-1}` is rank one and

\[
1_RM_\eta^{-1}1_L
=
\frac{c}{1-c^2g_Lg_R}
A_R(\eta)^{-1}|e_R\rangle\langle e_L|A_L(\eta)^{-1}.
\tag{4}
\]

The resolvent derivative gives

\[
-g_L'(\eta)=\|A_L(\eta)^{-1}e_L\|^2,
\tag{5}
\]

and therefore

\[
\boxed{
\beta_L'(\eta)
=\frac{\|A_L(\eta)^{-1}e_L\|^2}{g_L(\eta)^2},
}
\qquad
\boxed{
\beta_R'(\eta)
=\frac{\|A_R(\eta)^{-1}e_R\|^2}{g_R(\eta)^2}.
}
\tag{6}
\]

Taking the norm in (4) yields

\[
\boxed{
\|1_RM_\eta^{-1}1_L\|
=\frac{c\sqrt{\beta_L'(\eta)\beta_R'(\eta)}}
{\beta_L(\eta)\beta_R(\eta)-c^2}.
}
\tag{7}
\]

Equation (6) has the direct extension interpretation: `A_L^{-1}e_L/g_L` is the left harmonic extension normalized to endpoint value one, so `beta_L'` is exactly its squared Hilbert norm, and similarly on the right.

For later sanity checks, if `A(eta)>=eta I` and `||e||=1`, then

\[
1\le\beta'(\eta)\le\frac{\beta(\eta)}{\eta}.
\tag{8}
\]

The lower bound is Cauchy--Schwarz; the upper bound follows from `A^{-2}<=eta^{-1}A^{-1}`. These inequalities already show why a boundary impedance estimate by itself does not determine the extension mass sharply enough.

### 2. An explicit positive variable-corridor reservoir

Use the exact scalar PF-228 straight-corridor coefficients with one common seam halfwidth `w` and tangential parameter `mu>=1`. For an edge of length `ell`, set

\[
t=\tanh(\mu w),
\qquad
m(\ell)=\frac{\tanh(\mu\ell/2)}{t},
\qquad
c(\ell)=\frac{\operatorname{csch}(\mu\ell)}{t},
\tag{9}
\]

and

\[
K_\ell=
\begin{pmatrix}
m(\ell)+c(\ell)&-c(\ell)\\
-c(\ell)&m(\ell)+c(\ell)
\end{pmatrix}>0.
\tag{10}
\]

Assemble `M=I+sum K_ell` on the scalar bi-infinite chain. Let the cut edge `(0,1)` have length `S` with `mu S=1`, and let every other edge have length `kw`, where `k>0` is fixed. Write

\[
\varepsilon=\frac wS=\mu w,
\quad
m_1=m(S),\ c_1=c(S),
\quad
m_0=m(kw),\ c_0=c(kw).
\tag{11}
\]

For either constant background half-chain define

\[
H_0=1+2m_0,
\qquad
R_0=\sqrt{H_0(H_0+4c_0)},
\qquad
r_0=\frac{2c_0}{H_0+2c_0+R_0},
\tag{12}
\]

so its endpoint-normalized decaying extension is `r_0^j`. After eliminating both backgrounds the two cut endpoints have effective diagonal

\[
\alpha=m_1+\frac{1+R_0}{2},
\tag{13}
\]

and the complete prefix-to-tail block is rank one with

\[
\boxed{
\|X\|
=\frac{c_1}{\alpha(\alpha+2c_1)(1-r_0^2)}.
}
\tag{14}
\]

By contrast, the isolated two-interface transmission of the same defect edge is

\[
\boxed{
x_{\rm loc}
=\frac{c_1}{(1+m_1)(1+m_1+2c_1)}.
}
\tag{15}
\]

Let

\[
a=\tanh(1/2),
\qquad b=\operatorname{csch}(1),
\qquad q=\sqrt{\frac{k+1}{k}}.
\tag{16}
\]

As `epsilon -> 0`,

\[
m_0\to\frac k2,
\qquad
c_0\sim\frac1{k\varepsilon^2},
\qquad
\alpha\sim\frac{a+q}{\varepsilon},
\qquad
1-r_0^2\sim2\varepsilon\sqrt{k(k+1)}.
\tag{17}
\]

Consequently

\[
\boxed{
x_{\rm loc}
\sim
\varepsilon\frac{b}{a(a+2b)}\longrightarrow0,}
\tag{18}
\]

while

\[
\boxed{
\|X\|\longrightarrow
\frac{b}
{2\sqrt{k(k+1)}(a+q)(a+q+2b)}>0.
}
\tag{19}
\]

For `k=4`, the limit in (19) is approximately `0.01834455759`. Direct high-precision evaluation of (14) at `epsilon=0.1,0.03,0.01,0.003,0.001` gives respectively about `0.0262686,0.0206082,0.0190859,0.0185655,0.0184181`, providing a numerical audit of the asymptotic algebra rather than additional evidence.

The mechanism is entirely scalar and positive. The boundary Green coefficient retains the small local scale, but the two endpoint-normalized background extensions have norms of order `(1-r_0^2)^(-1/2)`, and their product exactly cancels the local `O(epsilon)` gain.

### 3. Two adjacent defect corridors do not remove the mechanism

The canonical PF corridor scale uses neighboring gaps, so a single exceptional gap can affect two adjacent lengths. Replace both edges `(0,1)` and `(1,2)` by length `S` while keeping the same constant backgrounds. After eliminating the backgrounds, the three central nodes carry

\[
B_3=
\begin{pmatrix}
\alpha+c_1&-c_1&0\\
-c_1&1+2m_1+2c_1&-c_1\\
0&-c_1&\alpha+c_1
\end{pmatrix},
\qquad G=B_3^{-1}.
\tag{20}
\]

Across the first defect edge the complete cut norm satisfies

\[
\|X_{\rm pair}\|^2
=
\frac{|G_{10}|^2+|G_{20}|^2/(1-r_0^2)}{1-r_0^2}.
\tag{21}
\]

With `p=a+q+b`, direct inversion and the same asymptotics give

\[
\boxed{
\|X_{\rm pair}\|\longrightarrow
\frac{b^2}
{4\sqrt{k(k+1)}\,p\big((a+b)p-b^2\big)}>0.
}
\tag{22}
\]

Thus the simplest incidence correction does not restore the frozen PF-229 comparison. Equation (22) is still a matched scalar control, not an arithmetic realization by consecutive prime gaps.

## Relation to PF-228, PF-229, and PF-222

PF-228 is unchanged: its isolated straight-corridor Schur dressing really has the favorable `w/s` scale. PF-229 is unchanged: repeating one fixed normalized corridor really does preserve that scale globally. PF-279 shows that the inference

`isolated w/s gain + scalar positivity + serial geometry => global variable-chain w/s gain`

is false. The missing datum is the mass of the left/right Poisson extensions, encoded exactly by `beta_L'` and `beta_R'` in (7).

For PF-222 this changes the quantitative target. A one-cut estimate based only on the local crossing coefficient or endpoint Weyl impedance can miss reservoir amplification. A viable variable-chain estimate must control the extension Gram forms as well, or exploit the actual physical `P/H` projections, frequency population, reciprocal-prime jump, or another canonical PF structure that suppresses the amplified tails.

This does **not** refute weak trace class for the true PF commutator. The scalar control is unprojected. If a scalar mode has the same physical low/high classification in every module, the mixed `P[D,E_j]H` block may vanish. Nor does the construction show that consecutive prime gaps realize a long enough background reservoir with the required scale.

## Prior-art and novelty audit

The mathematical ingredients are classical. Gerald Teschl's *Jacobi Operators and Completely Integrable Nonlinear Lattices* (AMS Mathematical Surveys and Monographs 72, 2000) develops the discrete Weyl--Titchmarsh theory and Jacobi Green functions used here. Florian Dörfler and Francesco Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks*, IEEE Transactions on Circuits and Systems I 60 (2013), 150--163, DOI `10.1109/TCSI.2012.2215780`, treats Schur/Kron elimination and sensitivity as standard network operations.

No novelty is claimed for Schur complements, Weyl functions, the resolvent derivative, or the rank-one inverse formula. The project-specific contribution is the exact matched-control consequence for the PF-228 coefficient family: **variable reservoir extension mass can erase the local `w/s` gain even though the frozen PF-229 scalar completion cannot**, and the exact quantity that must be retained is the derivative/Gram part of the Weyl data rather than impedance alone.

## Falsification and boundary conditions

A challenge to the exact scalar theorem should attack one of (4)--(7), the background recurrence (12)--(14), or the asymptotics (17)--(22). The formulas are finite/rank-one algebra plus a constant-coefficient Jacobi recurrence; no prime-distribution theorem enters them.

A challenge to its PF relevance has a different burden. It is enough to show that the canonical variable corridor supplies a uniform bound on the endpoint-normalized extension Gram forms, that the physical `P/H` projections annihilate the reservoir component, or that prime-gap incidence/arithmetic prevents reservoirs from persisting at the needed scale. Any of those would kill the obstruction **for the real PF geometry** while leaving this matched control correct.

Conversely, an unprojected scalar reservoir does not establish failure of the PF weak-`S_1` target. One must still preserve the exact physical projections, canonical seam normalization, actual neighboring-pant geometry, reciprocal-prime weighting, and the nested rather than orthogonal cut reassembly.

## Consequence for the research line

The next useful variable-corridor test is no longer a universal scalar extrapolation of PF-229. It is to compute or bound the canonical endpoint extension Gram forms (operator-valued analogues of `beta'`) and then test them after the physical `P/H` split. If those forms remain calibrated to the cut corridor, PF-279 becomes a killed matched control. If they can realize the reservoir amplification while surviving the projections and reciprocal-prime weighting, the weak-trace reassembly route needs a different global currency.

PF-279 therefore narrows the open endpoint problem without claiming a failure of the prime flute itself, any wave-operator conclusion, prime/clone separation, a zeta-zero mechanism, or RH.