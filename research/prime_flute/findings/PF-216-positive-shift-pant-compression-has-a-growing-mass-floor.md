# PF-216 — positive-shift pant compression has a growing mass-conductance floor

**Status:** `EXACT-DERIVED + ASYMPTOTIC-DERIVED + POSITIVE/BOUNDARY`. PF-215 shows that the energy-normalized exterior precision for the PF-205 simultaneous seam cut has divergent adjacent blocks on the low symmetric boundary modes. That divergence is not an isolated off-diagonal effect. On a growing but still embedded Fermi corridor in each thin one-cusp pant, the exact positive-shift Dirichlet energy separates into a same-sign channel with a uniform positive floor and an opposite-sign channel of size at least `s_n^{-1}`. After the exact PF-205 strip normalization, the raw low-symmetric compression of

\[
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}
\]

therefore has a diagonal mass floor of order

\[
\boxed{q_n^{-1}\asymp \frac{P_n}{\log P_n}},
\]

while its difference/conductance channel is even stronger. Thus PF-215's large normalized hopping is necessarily accompanied by large diagonal precision on the same constant sector. The remaining smooth-interface problem is no longer to discover this compensation in the raw pant form, but to prove that enough of it survives variational elimination of higher tangential modes before applying an inverse-locality argument to `D=(I+K)^{-1}`.

## Claim

Use the PF-205 natural-width simultaneous seam cut. Let `C_n,C_{n+1}` be adjacent distinguished cuffs bounding one one-cusp pant, let

\[
L_n=2a_n,
\qquad
s_n:=\operatorname{dist}(C_n,C_{n+1})=\frac{h_n+h_{n+1}}2,
\]

and let the signed Fermi-area halfwidths be

\[
w_j=\kappa d_j,
\qquad
\rho_j=\operatorname{arsinh}(w_j),
\qquad
d_j=a_j^+-a_j.
\]

After shrinking the fixed admissible `\kappa` if necessary, the PF-205 conclusions remain valid and the following statements hold after a finite head.

Let `E_n(a,b)` be the minimized `\Delta+1` energy on the remaining pant core when the two finite artificial boundary components carry constant values `a,b`. Then there are constants independent of `n` such that

\[
\boxed{
E_n(a,b)
\ge
c_0(a+b)^2+\frac{c_1}{s_n}(a-b)^2.
}
\tag{1}
\]

In particular, with

\[
E_{+,n}=E_n(1,1),
\qquad
E_{-,n}=E_n(1,-1),
\]

we have

\[
\boxed{c\le E_{+,n}\le 2\pi,\qquad E_{-,n}\ge c/s_n.}
\tag{2}
\]

Writing the constant-mode pant form as

\[
E_n(a,b)=A_na^2+2B_nab+C_nb^2,
\]

PF-215's negative cross term is therefore locked to the diagonal sum:

\[
\boxed{
\frac{A_n+C_n}{-B_n}
=2\frac{E_{-,n}+E_{+,n}}{E_{-,n}-E_{+,n}}
\longrightarrow2.
}
\tag{3}
\]

For the PF-205 strip module let `\mathbf 1_n` be the boundary vector equal to one on both sides and

\[
q_n:=\langle\mathbf1_n,\Lambda_{Q,n}\mathbf1_n\rangle.
\]

Then the exact translation-invariant strip problem gives

\[
\boxed{
q_n=2w_nL_n\bigl(1+O(w_n^2)\bigr)
\asymp\frac{\log P_n}{P_n}.
}
\tag{4}
\]

Consequently, if

\[
u_n:=\frac{\Lambda_{Q,n}^{1/2}\mathbf1_n}{\sqrt{q_n}}
\]

is the normalized low-symmetric module vector and `x=(x_n)` is finitely supported, then for

\[
f=\sum_nx_nu_n
\]

the quadratic form of the **raw** exterior precision satisfies

\[
\boxed{
\langle f,Kf\rangle
\ge c\sum_n\frac{|x_n|^2}{q_n}
\asymp
c\sum_n\frac{P_n}{\log P_n}|x_n|^2.
}
\tag{5}
\]

Equation (5) is a form-compression statement. It does not say that the low-symmetric subspace is invariant under `K`, and therefore does not by itself imply any decay estimate for `D=(I+K)^{-1}`.

## 1. A growing embedded corridor remains uniformly controlled

PF-215 uses the exact Fermi graph of the second cuff-axis over the first:

\[
\sinh r_s(t)
=
\frac{\sinh s}
{\sqrt{1-\cosh^2s\,\tanh^2t}}
=
\frac{\sinh s\cosh t}
{\sqrt{1-\sinh^2s\sinh^2t}}.
\tag{6}
\]

Fix a sufficiently small `0<\theta<1` and put

\[
T_s:=\operatorname{arsinh}\!\frac{\theta}{\sinh s}.
\tag{7}
\]

For `|t|\le T_s`, the denominator in (6) is bounded away from zero and

\[
r_s(t)\asymp s\cosh t,
\qquad
r_s(t)\le R_\theta,
\tag{8}
\]

with constants independent of small `s`. Moreover

\[
T_s\sim\log(1/s),
\quad
\int_{-T_s}^{T_s}s\cosh t\,dt\asymp1,
\quad
\int_{-T_s}^{T_s}\frac{dt}{s\cosh t}\asymp s^{-1}.
\tag{9}
\]

This growing window still lies in one cuff fundamental segment. Indeed PF-032 gives

\[
a_n=-\log\tanh(h_n/4),
\qquad s_n\ge h_n/2,
\]

so `T_{s_n}<a_n` after a finite head for fixed `\theta<1`.

The PF-205 artificial boundaries do not destroy (8). In the hyperboloid model the signed-distance function from the second geodesic along a first-cuff Fermi ray may be represented by

\[
F_t(r)=\sinh s\cosh r\cosh t-\cosh s\sinh r.
\tag{10}
\]

At `r=r_s(t)`,

\[
|\partial_rF_t(r_s(t))|
=\sqrt{1-\sinh^2s\sinh^2t}
\ge\sqrt{1-\theta^2}.
\tag{11}
\]

Hence moving the second boundary inward by normal distance `\rho_{n+1}` moves its intersection with these rays by only `O(\rho_{n+1})`, uniformly on the corridor. Since PF-205 gives `\rho_j=O(P_j^{-1})`, while odd-prime gaps and the exact cuff law give `s_n\gtrsim P_n^{-1}`, a fixed smaller admissible `\kappa` makes both seam-strip removals a fixed small fraction of the corridor thickness. If `\ell_n(t)` is the remaining core-ray length, then

\[
\boxed{
c\,s_n\cosh t\le\ell_n(t)\le C\,s_n\cosh t\le C_\theta}
\tag{12}
\]

through `|t|\le T_{s_n}`.

## 2. The positive shift supplies both mass and conductance

For an interval of length `\ell` with endpoint values `a,b`, the exact minimum of

\[
J_\ell(v)=\int_0^\ell(|v'|^2+|v|^2)\,dr
\]

is

\[
\boxed{
J_\ell^{\min}(a,b)
=\frac{(a^2+b^2)\cosh\ell-2ab}{\sinh\ell}
=\frac12\tanh(\ell/2)(a+b)^2
+\frac12\coth(\ell/2)(a-b)^2.
}
\tag{13}
\]

For `0<\ell\le C_\theta`, this is bounded below by

\[
c_\theta\left(\ell(a+b)^2+\ell^{-1}(a-b)^2\right).
\tag{14}
\]

On the corridor the hyperbolic Fermi metric is `dr^2+\cosh^2r\,dt^2` with uniformly bounded `r`. Dropping the nonnegative tangential energy, applying (14) on each ray, and using (9),(12) gives (1).

The upper bound `E_{+,n}\le2\pi` is the constant trial function already used in PF-215. Thus (2) follows. Since

\[
A_n+C_n=\frac{E_{-,n}+E_{+,n}}2,
\qquad
-B_n=\frac{E_{-,n}-E_{+,n}}4,
\]

and `E_{-,n}\to\infty` while `E_{+,n}=O(1)`, equation (3) follows. The large negative cross conductance isolated by PF-215 therefore cannot occur without a comparably large diagonal-sum precision on this constant sector.

## 3. The symmetric strip normalization is asymptotically exact

In PF-205's signed Fermi-area coordinate `x=\sinh r`, one seam strip has

\[
g=\frac{dx^2}{1+x^2}+(1+x^2)ds^2,
\qquad d\mu=dx\,ds.
\tag{15}
\]

For boundary value one on both sides, Fourier orthogonality in the periodic cuff coordinate shows that the minimizer is tangentially constant. Its energy per unit cuff length is

\[
I_w
=\min_{u(-w)=u(w)=1}
\int_{-w}^{w}\left((1+x^2)|u'|^2+|u|^2\right)dx.
\tag{16}
\]

The constant trial gives `I_w\le2w`. Conversely write `u=1-v`, `v(\pm w)=0`. Poincare and Cauchy--Schwarz give

\[
2\left|\int_{-w}^wv\,dx\right|
\le Cw^{3/2}\|v'\|_2
\le\frac12\|v'\|_2^2+Cw^3,
\]

so

\[
\boxed{2w-Cw^3\le I_w\le2w.}
\tag{17}
\]

Therefore `q_n=L_nI_{w_n}` gives the first equality in (4). PF-205 has `w_n\asymp P_n^{-1}`. Also

\[
a_n=-\log\tanh(h_n/4),
\qquad h_n\asymp g_n/P_n,
\]

and Baker--Harman--Pintz gives `g_n=O(P_n^{0.525})`, while odd-prime gaps give `g_n\ge2`. Hence `a_n\asymp\log P_n`, and the second comparison in (4) follows.

## 4. Raw normalized low-mode compression has a growing mass floor

For finitely supported `x`, applying `\Lambda_Q^{-1/2}` to `f=\sum x_nu_n` produces constant boundary value

\[
t_n=\frac{x_n}{\sqrt{q_n}}
\]

on both sides of module `n`. The exterior is the direct sum of the one-cusp pant cores, hence

\[
\langle f,Kf\rangle
=\sum_nE_n(t_n,t_{n+1}).
\tag{18}
\]

Since `s_n\to0`, equations (1) and

\[
(a+b)^2+(a-b)^2=2(a^2+b^2)
\]

give, after a finite head,

\[
\langle f,Kf\rangle
\ge c\sum_n(t_n^2+t_{n+1}^2)
\ge c'\sum_n\frac{|x_n|^2}{q_n},
\]

which is (5). The conductance part actually carries the larger coefficient `s_n^{-1}`; (5) records only the robust onsite floor needed to expose the correct scale.

## 5. What this changes — and what it does not

PF-214's uniform-hopping sufficient condition was deliberately absolute-scale. PF-215 shows it fails because normalized neighboring cross terms diverge. PF-216 shows why that failure is not evidence against inverse locality: on the raw low-symmetric compression the same thin-pant mechanism creates a growing diagonal mass and a difference penalty at the same time. The natural question is therefore relative/coercive, not whether individual normalized blocks stay bounded.

However the constant sector is not known to reduce the full pant DtN map, and `K` is naturally controlled first as a positive quadratic form. Let `P` be the orthogonal projection onto the low-symmetric module vectors and `Q=I-P`. For the closed positive form

\[
\mathfrak a[f]=\|f\|^2+\mathfrak k[f]
\]

associated with `I+K`, define its effective low form variationally on finite-support low vectors by

\[
\boxed{
\mathfrak s_{\rm low}[x]
:=\inf_{y\in Q\operatorname{Dom}(\mathfrak a)}
\mathfrak a[x+y].
}
\tag{19}
\]

This is the appropriate form-level Schur/shorting operation and needs no unproved boundedness of the raw block operators. Whenever a compatible operator-block realization exists, (19) is the usual Schur complement

\[
P(I+K)P-PKQ\,[Q(I+K)Q]^{-1}\,QKP.
\tag{20}
\]

Because `y=0` is admissible, the elimination can only lower the raw low-sector energy and can in principle erode the mass/conductance floor. PF-216 therefore does **not** prove PF-213's decay hypothesis, compactness of the Schur factor, weak trace class of the full first relative resolvent, or any RH consequence.

The next decisive gate is sharper: use the PF-207--PF-212 frequency/interface estimates to prove that the effective form (19) retains a quantitative fraction of the raw low-symmetric floor, or construct an actual high-mode cancellation mechanism showing that it does not. Only after this survival question is settled is a weighted Green-kernel, Agmon, Combes--Thomas, or related inverse estimate on the effective low sector justified.

## Prior-art and novelty audit

The one-dimensional formula (13), thin-channel conductance picture, Schur complementation, and graph/network interpretation of DtN maps are classical. Close-neck elliptic DtN asymptotics are represented, for example, by Borcea--Gorb--Wang, *Asymptotic Approximation of the Dirichlet to Neumann Map of High Contrast Conductive Media*, Multiscale Modeling & Simulation 12 (2014), 1494--1532, DOI `10.1137/140960761`. Riemann-surface DtN gluing and degeneration to weighted graph structure with an external potential are represented by Wentworth, *A Meyer-Vietoris formula for the determinant of the Dirichlet-to-Neumann operator on Riemann surfaces*, arXiv:2209.11863.

Neither source treats the PF-205 prime-flute seam geometry, the exact positive-shift constant-mode compression above, or the high-mode Schur-survival problem in (19). No novelty is claimed for the general DtN/network mechanism. The project-specific contribution is the exact specialization showing that the PF-215 divergent hopping is paired with a growing normalized mass/conductance floor and that the live reassembly gate is high-mode Schur survival rather than raw-hopping boundedness.

## Decisive falsification test

Compute or bound the effective low form (19) on the actual PF-205/PF-207 module decomposition. A positive continuation must prove a uniform tail inequality of the form

\[
\mathfrak s_{\rm low}[x]\ge c\,\mathfrak m_{\rm PF216}[x]
\]

for a fixed `c>0` and for a raw mass/conductance form `\mathfrak m_{\rm PF216}` quantitatively implied by (1),(5), or another comparably strong coercive inequality sufficient to control the effective Green kernel. A negative result should exhibit high-mode boundary data whose minimizing contribution in (19) cancels an asymptotically non-negligible fraction of that floor. Merely observing large entries of `K`, or merely bounding high modes separately without their coupling to the symmetric sector, does not decide the gate.
