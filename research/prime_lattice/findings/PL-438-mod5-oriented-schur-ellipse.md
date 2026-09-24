# PL-438 — The rank-two mod-5 defect has an exact source-adapted Schur ellipse

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-REFINEMENT + STRICT-CERTIFICATION-STRENGTHENING`.

**Parent findings:** `PL-421`, `PL-425`, `PL-428`, `PL-437`.

## Claim

`PL-437` reduces the genuinely oriented uncertainty in the `p=5` local-factor cone test to two real coordinates

\[
s=\Im(K_{01}+K_{21}),\qquad f=\Im K_{13},
\]

and gives the sufficient Weyl certificate

\[
\lambda_{\min}(H_{\rm known})\ge \sqrt{s^2+f^2}.
\tag{1}
\]

The residual is more structured than an arbitrary norm-bounded perturbation. In residue coordinates it couples one fixed antisymmetric residue direction only to a two-dimensional visible plane. After using the same real-product data and residue diagonal already present in the `PL-421` gate, the full cone condition admits an exact two-stage Schur reduction.

Write the real symmetric residue covariance, in the established order `(1,2,4,3)`, as

\[
S=
\begin{pmatrix}
D_0&x_{01}&x_{02}&x_{03}\\
x_{01}&D_1&x_{12}&x_{13}\\
x_{02}&x_{12}&D_2&x_{23}\\
x_{03}&x_{13}&x_{23}&D_3
\end{pmatrix},
\qquad
D=\operatorname{Diag}(S),
\tag{2}
\]

and let

\[
M:=S-\frac14D.
\tag{3}
\]

By `PL-421`, `M\succeq0` is exactly the normalized `p=5` local-factor image-cone condition. Define the orthonormal basis

\[
h=\frac1{\sqrt2}(0,-1,0,1)^T,
\quad e_0=(1,0,0,0)^T,
\quad e_2=(0,0,1,0)^T,
\quad q=\frac1{\sqrt2}(0,1,0,1)^T.
\tag{4}
\]

Then the two oriented coordinates become the residue-asymmetry vector

\[
\boxed{
g=
\begin{pmatrix}
(x_{03}-x_{01})/\sqrt2\\
(x_{23}-x_{12})/\sqrt2
\end{pmatrix}
=
\frac1{\sqrt2}
\begin{pmatrix}
s-f\\s+f
\end{pmatrix},
\qquad \|g\|^2=s^2+f^2.}
\tag{5}
\]

All remaining entries below are determined by the real-product sector together with the residue diagonal. Put

\[
u=\frac{x_{01}+x_{03}}2,
\qquad
v=\frac{x_{12}+x_{23}}2,
\qquad
c=x_{02},
\qquad
e=x_{13},
\tag{6}
\]

and

\[
\begin{aligned}
a&=\frac38(D_1+D_3)-e,\\
w&=\frac38(D_3-D_1),\\
\gamma&=\frac38(D_1+D_3)+e,\\
A&=
\begin{pmatrix}
3D_0/4&c\\c&3D_2/4
\end{pmatrix},\\
b&=\sqrt2\,(u,v)^T.
\end{aligned}
\tag{7}
\]

If `U=[h,e_0,e_2,q]`, direct multiplication gives the exact normal form

\[
\boxed{
U^TMU=
\begin{pmatrix}
a&g^T&w\\
g&A&b\\
w&b^T&\gamma
\end{pmatrix}.}
\tag{8}
\]

Hence on the strict visible branch `\gamma>0`, define

\[
E=A-\frac{bb^T}{\gamma},
\qquad
\mu=\frac{w}{\gamma}b,
\qquad
\alpha=a-\frac{w^2}{\gamma}.
\tag{9}
\]

A first Schur complement in the `q` direction yields

\[
M\succeq0
\iff
\gamma>0,
\quad
\begin{pmatrix}
\alpha&(g-\mu)^T\\
g-\mu&E
\end{pmatrix}\succeq0.
\tag{10}
\]

On the further strict branch `E\succ0`, this is exactly

\[
\boxed{
M\succeq0
\iff
\gamma>0,
\quad E\succ0,
\quad
(g-\mu)^TE^{-1}(g-\mu)\le\alpha.}
\tag{11}
\]

Thus the feasible oriented fiber is an **exact source-adapted ellipse**, not merely the Euclidean Weyl disk. Its axes are the visible eigen-directions of `E`, and its center

\[
\boxed{\mu=\frac{3(D_3-D_1)}{8\gamma}\,b}
\tag{12}
\]

is itself visible. In particular, when `D_1=D_3`, the ellipse is centered at the origin; when the two residue variances differ, the correct target need not be to make `(s,f)` small. The oriented source can instead compensate the known diagonal-imbalance coupling by placing `g` near `\mu` in the `E^{-1}` metric.

This is a strict strengthening of the certification surface, not an RH result. There are admissible covariance matrices for which the exact ellipse passes while the `PL-437` Weyl certificate fails. Conversely, nothing here proves that the actual prime covariance satisfies the visible branch conditions or the ellipse inequality at the source scales required by the line.

## 1. The oriented character coordinates are two residue asymmetries

Let `F` be the normalized `C_4` Fourier matrix used in `PL-428` and `PL-437`, and let

\[
K=F^*SF.
\tag{13}
\]

With the same Fourier convention,

\[
\begin{aligned}
\Im K_{01}
&=\frac{-D_1+D_3-x_{01}+x_{03}-x_{12}+x_{23}}4,\\
\Im K_{21}
&=\frac{ D_1-D_3-x_{01}+x_{03}-x_{12}+x_{23}}4,\\
\Im K_{13}
&=\frac{x_{01}-x_{03}-x_{12}+x_{23}}2.
\end{aligned}
\tag{14}
\]

Therefore the diagonal-visible coordinate from `PL-437` is recovered exactly as

\[
r:=\Im K_{21}-\Im K_{01}=\frac{D_1-D_3}{2},
\tag{15}
\]

while

\[
\begin{aligned}
s&:=\Im K_{01}+\Im K_{21}
=\frac{-x_{01}+x_{03}-x_{12}+x_{23}}2,\\
f&:=\Im K_{13}
=\frac{x_{01}-x_{03}-x_{12}+x_{23}}2.
\end{aligned}
\tag{16}
\]

Adding and subtracting gives

\[
s-f=x_{03}-x_{01},
\qquad
s+f=x_{23}-x_{12},
\tag{17}
\]

which is precisely (5). This makes the residual geometry particularly transparent: the two blind character phases are just the failure of the first and third residue coordinates to couple symmetrically to the two members of the conjugate residue pair.

The averages `u,v` in (6) are the complementary symmetric couplings. They are already determined by the real part of the character covariance. Thus the decomposition into `(u,v)` and `g` is not adding measurements; it separates the visible and genuinely oriented combinations of the same four residue cross terms.

## 2. Exact `1+2+1` block normal form

The gate matrix is

\[
M=
\begin{pmatrix}
3D_0/4&x_{01}&x_{02}&x_{03}\\
x_{01}&3D_1/4&x_{12}&x_{13}\\
x_{02}&x_{12}&3D_2/4&x_{23}\\
x_{03}&x_{13}&x_{23}&3D_3/4
\end{pmatrix}.
\tag{18}
\]

The basis (4) splits the `(1,3)` residue pair into its antisymmetric vector `h` and symmetric vector `q`. Elementary inner products give

\[
\begin{aligned}
h^TMh&=\frac38(D_1+D_3)-x_{13}=a,\\
q^TMq&=\frac38(D_1+D_3)+x_{13}=\gamma,\\
h^TMq&=\frac38(D_3-D_1)=w,\\
h^TMe_0&=\frac{x_{03}-x_{01}}{\sqrt2}=g_1,\\
h^TMe_2&=\frac{x_{23}-x_{12}}{\sqrt2}=g_2,\\
q^TMe_0&=\sqrt2\,u,\\
q^TMe_2&=\sqrt2\,v.
\end{aligned}
\tag{19}
\]

Together with the obvious `(e_0,e_2)` block, these identities prove (8). In this basis the `PL-437` rank-two residual is literally

\[
\begin{pmatrix}
0&g^T&0\\
g&0_{2\times2}&0\\
0&0&0
\end{pmatrix},
\tag{20}
\]

whose nonzero eigenvalues are `\pm\|g\|=\pm\sqrt{s^2+f^2}`. The formal rank-two result is therefore not merely a small-rank label: it identifies exactly where the unresolved arithmetic information enters the cone.

The visible diagonal imbalance `r=(D_1-D_3)/2` appears only through `w=-3r/4`. Hence after the first reduction there is a clean separation between the already-observed diagonal asymmetry and the two still-oriented cross-residue asymmetries.

## 3. Two Schur complements give the exact ellipse

Assume first `\gamma>0`. Since `U` is orthogonal, `M\succeq0` iff the matrix in (8) is positive semidefinite. Taking the Schur complement of the lower-right scalar `\gamma` gives

\[
\begin{pmatrix}
a&g^T\\g&A\end{pmatrix}
-\frac1\gamma
\begin{pmatrix}w\\b\end{pmatrix}
\begin{pmatrix}w&b^T\end{pmatrix}
=
\begin{pmatrix}
\alpha&(g-\mu)^T\\
g-\mu&E
\end{pmatrix},
\tag{21}
\]

which proves (10). If `E\succ0`, a second Schur complement gives (11).

The singular boundary does not create a new mathematical mechanism. The standard generalized Schur-complement theorem replaces inverses by Moore--Penrose inverses together with the appropriate range condition. For the present line the strict branch (11) is the useful certification surface because it is the regime in which the visible block has a quantitative margin. No claim below relies on silently extending `E^{-1}` through a singular matrix.

Geometrically, diagonalizing `E=Q\operatorname{diag}(\lambda_1,\lambda_2)Q^T` with `\lambda_j>0` turns (11) into

\[
\frac{y_1^2}{\alpha\lambda_1}
+
\frac{y_2^2}{\alpha\lambda_2}
\le1,
\qquad
y=Q^T(g-\mu),
\tag{22}
\]

when `\alpha>0`. The semiaxes are therefore `\sqrt{\alpha\lambda_j}`. A small eigenvalue of the visible block penalizes only the oriented direction aligned with that eigenvector; the Weyl disk instead spends the smallest margin in every direction.

## 4. The Schur ellipse is strictly less conservative than the PL-437 Weyl disk

The gain is not merely possible for an abstract block matrix. Consider the exact residue covariance

\[
S_*=
\begin{pmatrix}
1&-1/4&0&1/4\\
-1/4&1&0&1/2\\
0&0&1&0\\
1/4&1/2&0&1
\end{pmatrix},
\qquad D=I_4.
\tag{23}
\]

In the basis (4),

\[
U^T\left(S_*-\frac14I\right)U
=
\begin{pmatrix}
1/4&\sqrt2/4&0&0\\
\sqrt2/4&3/4&0&0\\
0&0&3/4&0\\
0&0&0&5/4
\end{pmatrix}.
\tag{24}
\]

The matrix obtained by setting the oriented vector to zero has smallest eigenvalue `1/4`, while

\[
\|g\|=\frac{\sqrt2}{4}=\frac1{2\sqrt2}>\frac14.
\tag{25}
\]

Thus the sufficient Weyl test (1) fails. The exact Schur budget, however, is

\[
\alpha-g^TE^{-1}g
=\frac14-\frac{1/8}{3/4}
=\frac1{12}>0.
\tag{26}
\]

Indeed the exact gate matrix has eigenvalues

\[
\boxed{
\left\{
\frac{2-\sqrt3}{4},\frac34,
\frac{2+\sqrt3}{4},\frac54
\right\},}
\tag{27}
\]

all positive. Since `S_*=(S_*-I/4)+I/4\succ0`, this is an admissible positive covariance, not an indefinite toy control. The exact source-adapted ellipse therefore certifies strictly more of the actual `PL-421` cone than the Euclidean norm condition of `PL-437`.

The older `PL-428` matched-control family does not display this gain. For `S_t=I+tA_1`, the visible known part is `3I/4` and the residual has norm `\sqrt2|t|`, so both Weyl and the exact Schur criterion reduce to

\[
|t|\le\frac{3}{4\sqrt2}.
\tag{28}
\]

This is a useful adversarial control: the new criterion is not automatically looser on every fiber. It gains precisely when the visible geometry is anisotropic or coupled in a way that Weyl's single smallest eigenvalue discards.

## 5. What the source now has to control

Equations (5)--(12) make the certification target fully source-adapted. On the strict visible branch, every coefficient of

\[
\gamma,\ E,\ \alpha,\ \mu
\tag{29}
\]

is determined by the residue diagonal and the real-product sector. The only unresolved vector is

\[
g=\frac1{\sqrt2}(s-f,s+f)^T.
\tag{30}
\]

Therefore the oriented arithmetic theorem needed for this representation step can be stated as the single scalar inequality

\[
\boxed{
(g-\mu)^TE^{-1}(g-\mu)\le\alpha,}
\tag{31}
\]

plus the visible positivity hypotheses. It need not prove a uniform lower-frame estimate for every complex direction, and it need not separately force `s` and `f` to be smaller than `\lambda_{\min}(H_{\rm known})`.

This distinction is potentially relevant for the direct source route. If the actual arithmetic covariance produces a predictable relation between the oriented asymmetries and the visible diagonal imbalance, then cancellation against `\mu` can be useful; a theorem that bounds only `\sqrt{s^2+f^2}` throws that relation away. Conversely, if the source is approximately residue-symmetric, then `D_1-D_3` and hence `\mu` are small, and (31) reduces to a centered anisotropic bound.

`PL-425` supplies exactly such a calibration at the singular-series-model level: its mod-5 two-term model is character-diagonal up to square-root error, with equal diagonal structure at main order. In that idealized model the center is asymptotically zero and the oriented defect is already suppressed. The unresolved issue remains transfer to the actual deterministically centered prime covariance at variance scale. Nothing in the present finite-dimensional reduction supplies that transfer.

## 6. Prior art and novelty audit

The Schur complement and its positive-semidefinite criterion are classical. The singular extension by Moore--Penrose inverse and range conditions goes back, in a standard general form, to David Carlson, Emilie V. Haynsworth and Thomas L. Markham, **“A Generalization of the Schur Complement by Means of the Moore--Penrose Inverse,”** *SIAM Journal on Applied Mathematics* **26**(1) (1974), 169--175, DOI `10.1137/0126013`. No novelty is claimed for Schur complements, ellipsoids from positive quadratic forms, orthogonal changes of basis, or the generalized boundary criterion.

The line-specific delta is the exact specialization of that classical machinery to the already-proved `PL-437` mod-5 residual. The useful facts are simultaneous: the blind sector is rank two, the gate's own diagonal data determine the third nominally blind coordinate, the remaining defect occupies only the `h`-to-`(e_0,e_2)` block, and all other block coefficients are visible from the declared source observables. Targeted searches around Schur complements, covariance matrices, fixed-modulus Dirichlet-character variances, and mod-5 prime correlations did not locate this specific reduction or the arithmetic ellipse (31). That absence is only a novelty audit; it is not a claim that no equivalent finite-dimensional observation exists elsewhere.

The strict-improvement example (23)--(27) is an exact Mathia control demonstrating that the specialization changes the theorem surface. The generic Schur theorem by itself does not say that the `PL-437` Weyl target was unnecessarily strong for an admissible residue covariance.

## 7. Adversarial audit and boundaries

1. **The ellipse is exact only after its visible branch hypotheses are checked.** Formula (11) assumes `\gamma>0` and `E\succ0`. Singular cases require the generalized Schur complement and range conditions. An arithmetic proof cannot simply divide by a vanishing visible margin.
2. **Visible does not mean presently controlled by an unconditional theorem.** The statement that `a,w,A,b,\gamma` are determined from the declared real-product/diagonal data is representational. `PL-436` already shows that currently audited scalar lower-bound theorems do not automatically provide all of that data with the required variance-scale precision.
3. **The oriented vector remains genuinely arithmetic.** `PL-428` gives positive-semidefinite fixed-visible-data families whose cone verdict changes. The Schur reduction cannot infer (31) from covariance positivity alone.
4. **A shifted center is not an automatic gain.** If `g` and `\mu` are unrelated, replacing `\|g\|` by `\|g-\mu\|_{E^{-1}}` may be analytically harder. The value is that (31) is the exact scalar budget; whether the source supplies the needed relation is a separate theorem.
5. **The strict example is a representation control, not the prime source.** It proves that the Weyl certificate is genuinely conservative inside the admissible covariance cone. It does not show that the actual mod-5 prime covariance lies in the newly exposed part.
6. **Kuperberg's singular-series model is not the actual prime covariance.** Its near-diagonality is calibration only. The source-model replacement gap from `PL-425`, `PL-434`, and `PL-436` remains.
7. **No analytic continuation or RH implication is used.** Everything through (31) is finite-dimensional covariance algebra. RH relevance enters only through the already-established source-transfer program of the parent findings.

## Consequence for the line

The live mod-5 arithmetic target can be weakened one more step. After the real-product sector and residue diagonal have been controlled, it is unnecessary to demand the isotropic estimate

\[
\sqrt{s^2+f^2}\le\lambda_{\min}(H_{\rm known}).
\]

On the quantitative interior of the visible block, the exact remaining requirement is the source-adapted scalar Schur budget (31). It can exploit anisotropy and a visible nonzero center, and the admissible example (23) proves that this is strictly less conservative than the previous Weyl disk.

The next arithmetic question is therefore precise: **can the actual fixed-mod-5 short-prime covariance control `(g-\mu)^TE^{-1}(g-\mu)` at the variance scale required by `PL-421`, without importing RH/GRH or an equivalent full complex lower-frame estimate?** Until such a theorem is proved or falsified, the Schur ellipse is a sharper representation target rather than a solution of the source problem.
