# PC-164 — one-hole energy-dependent Feshbach family has only prime-blind Bloch and cyclotomic divisors

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for extracting a new-prime/RH-sensitive spectral divisor from the **energy-dependent Schur/Feshbach elimination of the one-hole old section**. PC-162 classified the zero-energy added Kron correction, and PC-163 classified the zero-energy full Kron pseudodeterminant while explicitly leaving energy-dependent Feshbach/scattering determinants open. For the canonical Feshbach family obtained by eliminating exactly the same old vertices at spectral energy `E`, the whole finite determinant is already the complete-fiber Bloch characteristic polynomial divided by the fixed-size old-block characteristic polynomial. Its zeros and poles are real, the formula holds for every coprime composite one-hole control as well as for new primes, and the fixed-base self-energy converges to a cyclotomic trace-class family whose energy divisor has only finitely many base-level zeros and poles.

Fix `d>=2`, put

\[
r:=\varphi(d),
\qquad (m,d)=1,
\qquad m\ge2,
\]

and use the one-hole semi-primitive geometry of PC-158--PC-163,

\[
S_{d,m}=\{x\bmod dm:(x,d)=1\},
\qquad
O_{d,m}=\{x\in S_{d,m}:m\mid x\},
\qquad
X_{d,m}=S_{d,m}\setminus O_{d,m}.
\tag{1}
\]

Thus `|S_{d,m}|=rm`, `|O_{d,m}|=r`, and `|X_{d,m}|=r(m-1)`. If `m=q` is prime with `q\nmid d`, then `X_{d,q}=U(dq)` is the genuine new primitive shell. For composite `m`, the same construction is the matched one-hole control already used in PC-158--PC-163.

Let

\[
M_{d,m}:=(dm)^{-2}L_{dm}[S_{d,m}]
\tag{2}
\]

be the normalized inverse-square chord Laplacian. Ordering the ambient vertices as `X_{d,m}\sqcup O_{d,m}`, write

\[
M_{d,m}
=
\begin{pmatrix}
A_{d,m}^{\rm hole}+\Delta_{d,m}&-B_{d,m}\\
-B_{d,m}^*&G_{d,m}
\end{pmatrix},
\tag{3}
\]

with the notation of PC-162/PC-163. The old block `G_{d,m}` is positive definite.

## 1. The full energy-dependent Feshbach determinant is exactly a Bloch quotient

For

\[
E\notin\operatorname{Spec}G_{d,m},
\]

define the spectral Schur/Feshbach map on the survivor by

\[
\boxed{
\mathfrak F_{d,m}(E)
:=A_{d,m}^{\rm hole}+\Delta_{d,m}-EI
-B_{d,m}(G_{d,m}-EI)^{-1}B_{d,m}^*.
}
\tag{4}
\]

At `E=0` this is exactly the full Kron response `R_{d,m}` of PC-163. For general `E`, ordinary block Gaussian elimination gives

\[
\boxed{
\det\mathfrak F_{d,m}(E)
=
\frac{\det(M_{d,m}-EI)}
{\det(G_{d,m}-EI)}.
}
\tag{5}
\]

This identity is meromorphic in `E`; at an old-block eigenvalue it is understood after the usual cancellation of common factors when one occurs.

The ambient operator is the complete cyclic `m`-fiber classified by PC-156 and used in PC-163. Hence

\[
M_{d,m}
\simeq
\bigoplus_{k=0}^{m-1}\mathcal P_d(k/m),
\qquad
\mathcal P_d(t)
=\frac1{d^2}
\left(
L_d^{\rm int}+\frac t2C_d-\frac{t^2}{2}I
\right),
\tag{6}
\]

where `C_d=H_d+J_d`. If

\[
D_d(t;E):=\det(\mathcal P_d(t)-EI),
\tag{7}
\]

then (5) becomes the exact finite formula

\[
\boxed{
\det\mathfrak F_{d,m}(E)
=
\frac{
\displaystyle\prod_{k=0}^{m-1}D_d(k/m;E)
}
{\det(G_{d,m}-EI)}.
}
\tag{8}
\]

Thus energy-dependent elimination creates no new characteristic function beyond two objects already present before elimination: the fixed base Bloch pencil sampled on the ordinary cyclic grid, and the `r\times r` old Dirichlet block.

## 2. Analytic continuation in energy has only a real divisor

PC-157/PC-160 imply

\[
0\preceq M_{d,m}\preceq\frac18I.
\tag{9}
\]

Since `G_{d,m}` is a positive principal block,

\[
0\prec G_{d,m}\preceq\frac18I.
\tag{10}
\]

Consequently every zero of the numerator in (5) lies in `[0,1/8]`, and every pole supplied by the denominator lies in `(0,1/8]`. After cancelling common factors, the meromorphic divisor of

\[
E\longmapsto\det\mathfrak F_{d,m}(E)
\]

is still entirely real. In particular the canonical spectral energy does not acquire a nonreal zero set, a critical strip, or a distinguished vertical line merely because the old variables are integrated out.

This is stronger than a bulk statement. Equation (8) controls the complete finite determinant, including sparse ambient modes. It also makes the matched-control obstruction exact: its derivation uses only `(m,d)=1`. When `m=q` is a new prime, the survivor is the actual primitive shell `U(dq)`; when `m` is composite, the same one-hole geometry has the same formula with the same base pencil. Primality of the fiber size does not enter the Feshbach law.

For fixed `d`, the zero set as `m` grows is therefore only a denser sampling of the fixed real Bloch bands

\[
\Sigma_d
:=
\bigcup_{0\le t\le1}
\operatorname{Spec}\mathcal P_d(t)
\subset[0,1/8],
\tag{11}
\]

while the `r` old-block poles converge to fixed base values described below. Away from `\Sigma_d`, the normalized logarithm is just the Riemann-sum limit

\[
\frac1m\log\det\mathfrak F_{d,m}(E)
\longrightarrow
\int_0^1\log D_d(t;E)\,dt,
\tag{12}
\]

on any simply connected compact energy domain where a continuous logarithm is chosen. The old-block denominator contributes only `O_d(1/m)` to (12). This is a fixed-base Bloch logarithmic potential, not a new-prime analytic continuation.

## 3. The energy-dependent self-energy has a prime-blind trace-class limit

The determinant quotient already closes the finite characteristic-polynomial route, but the operator-valued self-energy could in principle retain relational information not visible in (8). Define

\[
\Sigma_{d,m}(E)
:=
\Delta_{d,m}
-B_{d,m}(G_{d,m}-EI)^{-1}B_{d,m}^*,
\tag{13}
\]

so that

\[
\mathfrak F_{d,m}(E)
=A_{d,m}^{\rm hole}-EI+\Sigma_{d,m}(E).
\]

Use the same centered-offset embeddings and old-coordinate permutation as PC-161/PC-162. For `a\in U(d)`, recall

\[
E_a=\{h\in\mathbb Z\setminus\{0\}:(a+h,d)=1\},
\qquad
w_h=\frac1{4\pi^2h^2},
\]

\[
W_a=\operatorname{diag}_{h\in E_a}(w_h),
\qquad
v_a=(w_h)_{h\in E_a},
\qquad
s_a=\sum_{h\in E_a}w_h>0.
\tag{14}
\]

PC-162's proof gives, separately, trace-norm convergence of the survivor boundary diagonal, Hilbert--Schmidt convergence of the fixed-column old/new block, and operator-norm convergence

\[
G_{d,m}\longrightarrow
\operatorname{diag}_{a\in U(d)}(s_a).
\tag{15}
\]

Therefore the resolvent identity upgrades the zero-energy limit uniformly on every compact

\[
K\Subset\mathbb C\setminus\{s_a:a\in U(d)\}:
\]

\[
\boxed{
\sup_{E\in K}
\left\|
\Sigma_{d,m}(E)-\Sigma_{d,\infty}(E)
\right\|_1
\longrightarrow0,
}
\tag{16}
\]

where

\[
\boxed{
\Sigma_{d,\infty}(E)
=
\bigoplus_{a\in U(d)}
\left(
W_a-\frac1{s_a-E}v_av_a^*
\right).
}
\tag{17}
\]

The proof is a direct trace-ideal estimate. On `K`, the finite and limiting old resolvents are uniformly bounded; `B_{d,m}` converges in Hilbert--Schmidt norm; and products of two Hilbert--Schmidt factors with a bounded middle factor converge in trace norm. No prime property of `m` appears anywhere in this passage.

Thus the complete energy-dependent self-energy, not only its value at `E=0`, has the same fixed limit along primes and along coprime composite one-hole controls.

## 4. The limiting two-variable Fredholm determinant is only a cyclotomic logarithmic derivative pencil

For one limiting star define, exactly as in PC-162,

\[
F_a(z)
:=\det(I+zW_a)
=\prod_{h\in E_a}(1+zw_h),
\qquad
F_a'(0)=s_a.
\tag{18}
\]

Apply the rank-one determinant lemma to the `a`-block of (17). Since

\[
\frac{F_a'(z)}{F_a(z)}
=
\sum_{h\in E_a}
\frac{w_h}{1+zw_h},
\tag{19}
\]

and

\[
z\sum_{h\in E_a}
\frac{w_h^2}{1+zw_h}
=s_a-rac{F_a'(z)}{F_a(z)},
\tag{20}
\]

one obtains the exact entire-in-`z`, meromorphic-in-`E` identity

\[
\boxed{
\det\!\left[
I+z\left(W_a-\frac1{s_a-E}v_av_a^*\right)
\right]
=
\frac{F_a'(z)-E F_a(z)}{s_a-E}.
}
\tag{21}
\]

For the full limiting self-energy,

\[
\boxed{
\det(I+z\Sigma_{d,\infty}(E))
=
\prod_{a\in U(d)}
\frac{F_a'(z)-E F_a(z)}{s_a-E}.
}
\tag{22}
\]

At `E=0`, (21) is exactly PC-162's formula `F_a'(z)/F_a'(0)`. The energy variable adds only the linear pencil `F_a'-E F_a`.

For fixed generic `z`, equation (22) has at most `r` energy zeros and `r` energy poles. Whenever `F_a(z)\ne0`, the corresponding zero is simply

\[
\boxed{
E=\frac{F_a'(z)}{F_a(z)}
=
\sum_{h\in E_a}
\frac{w_h}{1+zw_h},
}
\tag{23}
\]

and the pole is `E=s_a`. PC-162 already gives the explicit cyclotomic/hyperbolic representation

\[
F_a(z)
=
\frac{2d^2}{z}
\frac{
Q_{d,a}(\cosh(\sqrt z/d))
}{Q_{d,a}'(1)},
\tag{24}
\]

with `Q_{d,a}` a real projection of the fixed cyclotomic polynomial `\Phi_d`. Hence even the full two-variable limiting Fredholm family contains no refining-prime divisor: its entire energy dependence is a finite collection of fixed-base cyclotomic logarithmic derivatives.

For real `E` away from the poles, every block in (17) is self-adjoint trace class. Therefore the zeros in the Fredholm variable `z` are real as well. A complex critical-line pattern can only be manufactured by an external reparameterization of either variable, exactly the wrapper failure already isolated in PC-162.

## 5. The zero-energy derivative recovers PC-163 exactly

There is a useful normalization check because `\mathfrak F_{d,m}(0)=R_{d,m}` is singular. Let `\mathbf1_X` and `\mathbf1_O` denote the constant vectors on the survivor and old section. Since the full ambient Laplacian annihilates constants, the lower block of (3) gives

\[
G_{d,m}^{-1}B_{d,m}^*\mathbf1_X
=\mathbf1_O.
\tag{25}
\]

Differentiating (4) at zero yields

\[
\mathfrak F_{d,m}'(0)
=-I-B_{d,m}G_{d,m}^{-2}B_{d,m}^*.
\]

Hence the derivative of the simple zero eigenvalue along the normalized survivor constant is

\[
\frac{
\langle\mathbf1_X,
\mathfrak F_{d,m}'(0)\mathbf1_X\rangle
}{\|\mathbf1_X\|^2}
=
-\frac{r(m-1)+r}{r(m-1)}
=
-\frac m{m-1}.
\tag{26}
\]

Differentiating (5) at `E=0` therefore gives

\[
-\frac m{m-1}\det'R_{d,m}
=-\frac{\det'M_{d,m}}{\det G_{d,m}},
\]

or

\[
\boxed{
\det'R_{d,m}
=\frac{m-1}{m}
\frac{\det'M_{d,m}}{\det G_{d,m}},
}
\tag{27}
\]

which is exactly PC-163. The energy-dependent family therefore extends the previous zero-energy formula with no hidden normalization factor.

For the minimal exact audit `d=2`, the base Bloch pencil and old block are scalar:

\[
\mathcal P_2(t)=\frac{t(1-t)}8,
\qquad
G_{2,m}=\frac{m^2-1}{48m^2}.
\tag{28}
\]

Thus for every odd `m`, prime or composite,

\[
\boxed{
\det\mathfrak F_{2,m}(E)
=
\frac{
\displaystyle\prod_{k=0}^{m-1}
\left(\frac{k(m-k)}{8m^2}-E\right)
}
{\frac{m^2-1}{48m^2}-E}.
}
\tag{29}
\]

The limiting star has `s_1=1/48` and

\[
F_1(z)
=
\left[
\frac{\sinh(\sqrt z/4)}{\sqrt z/4}
\right]^2,
\]

so (21) becomes

\[
\boxed{
\det(I+z\Sigma_{2,\infty}(E))
=
\frac{F_1'(z)-E F_1(z)}{1/48-E}.
}
\tag{30}
\]

This one-dimensional control already displays both parts of the classification: finite energy zeros are ordinary real Bloch samples, while the eliminated-center self-energy has only one fixed base pole and one cyclotomic/hyperbolic logarithmic-derivative zero.

## 6. Prior-art and novelty audit

The abstract mechanisms are classical. Energy-dependent elimination is the standard Schur/Feshbach map; the determinant factorization (5) is ordinary block Gaussian elimination, within the Schur-complement framework already anchored in `research/prime_circle/SOURCES.md` by Crabtree--Haynsworth and Dörfler--Bullo. Modern Feshbach--Schur perturbation theory likewise treats this spectral reduction as standard operator technology; for example G. Dusson, I. M. Sigal and B. Stamm, **The Feshbach--Schur map and perturbation theory**, EMS Press (2021), DOI `10.4171/ECR/18-1/5`. Rank-one secular/determinant formulas for graph Laplacians are also established; a nearby modern reference is S. Klee and M. T. Stamps, **Eigenvalues of Graph Laplacians Via Rank-One Perturbations**, *Quarterly Journal of Mathematics* 73:2 (2022), 609--616, DOI `10.1093/qmath/haab045`.

The circle-specific ingredients are also already classified internally: PC-156 supplies the exact complete-fiber Bloch pencil; PC-161/PC-162 supply the trace-class star localization and cyclotomic product `F_a`; PC-159/PC-160 control the real Bloch symmetry and positivity. Directed searches across Feshbach--Schur maps, cyclic/Bloch graph determinants, rank-one star secular equations, and roots-of-unity inverse-square Laplacians did not locate the exact combined formulas (8), (16), and (21)--(24). That absence is not evidence of historical priority, and no new general theorem about Feshbach maps, Schur complements, rank-one determinants, or Bloch theory is claimed.

The durable content is the Prime-Circle classification boundary: the most canonical spectral-parameter extension of the one-hole harmonic elimination does **not** rescue a complex or prime-specific spectral divisor. Its finite zeros/poles come from real Bloch/Dirichlet spectra, and its fixed-base operator-valued self-energy converges to a finite product of fixed cyclotomic logarithmic-derivative pencils along both prime and composite controls.

## 7. RH consequence, boundary, and falsification surface

This closes the route

\[
\boxed{
\text{new-prime one-hole old/new geometry}
\to
\text{energy-dependent Feshbach elimination}
\to
\text{complex resonance/determinant divisor}
\to
\text{new RH mechanism}
}
\tag{31}
\]

for the canonical fixed-base Schur family (4). Adding a spectral parameter does not restore information lost at zero energy: at finite `m` it only exposes the already-existing real spectrum of the complete cyclic ambient operator relative to the old block, and at fixed base its self-energy is the prime-blind cyclotomic family (17)--(24).

The statement is deliberately narrower than a classification of every possible scattering construction. It does **not** cover a true composite primitive refinement with several missing residue sections, simultaneous growth of `d` and `m`, external leads or boundary conditions not forced by Prime Circle, nonlinear/growing-support cross-level couplings, or the global uniformization/monodromy branch. Nor does it classify arbitrary functions imposed on the Feshbach family after the fact. Those remain outside the hypotheses rather than being ruled out rhetorically.

The result is directly falsifiable. A finite `(d,m)` violating the determinant quotient (5) or Bloch product (8) breaks the exact derivation. Any nonreal zero or pole of the reduced finite determinant would contradict the self-adjoint quotient in (5). A compact energy set away from `{s_a}` on which the trace-norm convergence (16) fails would break the star-resolvent limit. Finally, one value of `(a,z,E)` for which (21) fails would contradict the rank-one determinant lemma and the logarithmic-derivative identity. Under the stated one-hole fixed-base hypotheses, the canonical energy-dependent Feshbach repair is therefore exhausted.