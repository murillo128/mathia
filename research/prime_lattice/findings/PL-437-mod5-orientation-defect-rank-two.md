# PL-437 — The mod-5 orientation defect is rank two, and residue diagonals reduce the unresolved fiber to two parameters

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-REFINEMENT + THEOREM-SURFACE-NARROWING`.

**Parent findings:** `PL-421`, `PL-424`, `PL-428`, `PL-431`, `PL-432`, `PL-436`.

## Claim

`PL-428` identifies three real coherence coordinates that are invisible to every real scalar/product variance in the mod-5 character basis,

\[
b:=\Im K_{01},\qquad d:=\Im K_{21},\qquad f:=\Im K_{13}.
\]

Those three coordinates do **not** form a generic three-parameter Hermitian perturbation. The reality constraint inherited from the four real residue channels forces their imaginary covariance to have rank at most two. More precisely, if

\[
K=A+iB,\qquad A=\Re K,
\]

then

\[
B=
\begin{pmatrix}
0&b&0&-b\\
-b&0&-d&f\\
0&d&0&-d\\
b&-f&d&0
\end{pmatrix},
\tag{1}
\]

and

\[
\boxed{
\operatorname{spec}(iB)=
\left\{
+\sigma,-\sigma,0,0
\right\},
\qquad
\sigma^2=2b^2+2d^2+f^2.
}
\tag{2}
\]

There is a second reduction that matters for the `PL-421` cone test. The cone already uses the four residue variances

\[
D=\operatorname{Diag}(S),
\qquad S=FKF^*,
\tag{3}
\]

with the `C_4` Fourier matrix of `PL-428`. Once `A=Re K` and `D` are known, one linear combination of the three nominally blind coordinates is determined exactly:

\[
\boxed{r:=d-b.}
\tag{4}
\]

Writing

\[
s:=b+d,
\tag{5}
\]

leaves only the two genuinely unresolved oriented coordinates

\[
\boxed{(s,f).}
\tag{6}
\]

After the known `r` contribution is separated, the remaining invisible Hermitian perturbation has operator norm

\[
\boxed{\sqrt{s^2+f^2}.}
\tag{7}
\]

Thus the sufficient full-complex coercivity target stated in `PL-436` is stronger than the finite-dimensional representation itself requires. Given real-product quadratic information and the residue diagonal already present in the gate, the arithmetic problem is only to control a **two-parameter rank-two oriented defect**. This does not solve that problem: `PL-428` already supplies positive-semidefinite matched controls with the same real-product data and the same residue diagonal for which the cone verdict changes.

## 1. Reality forces a Pfaffian-zero imaginary covariance

Order reduced residues as `(1,2,4,3)` and use

\[
F_{rj}=\frac12(-i)^{rj},
\qquad
A(y)=F^*R(y),
\qquad
K=\int A(y)A(y)^*\,dy.
\tag{8}
\]

Because the residue signal `R(y)` is real,

\[
A_0,A_2\in\mathbb R,
\qquad
A_3=\overline{A_1}.
\tag{9}
\]

Consequently

\[
K_{03}=\overline{K_{01}},
\qquad
K_{23}=\overline{K_{21}},
\tag{10}
\]

while `K_13` may have an independent imaginary part. This gives exactly (1).

For a `4 x 4` skew-symmetric matrix the Pfaffian is

\[
\operatorname{pf}(B)
=B_{01}B_{23}-B_{02}B_{13}+B_{03}B_{12}.
\tag{11}
\]

Substituting (1),

\[
\operatorname{pf}(B)
=b(-d)-0\cdot f+(-b)(-d)=0.
\tag{12}
\]

Hence

\[
\det B=\operatorname{pf}(B)^2=0.
\tag{13}
\]

The rank of a real skew-symmetric matrix is even, so every nonzero matrix in this three-dimensional blind family has rank exactly two rather than four. Moreover,

\[
\operatorname{tr}(B^TB)
=2\sum_{j<k}B_{jk}^2
=2(2b^2+2d^2+f^2).
\tag{14}
\]

A real rank-two skew matrix has one nonzero singular value with multiplicity two. Therefore its singular value is `sigma` from (2), and multiplication by `i` turns the conjugate imaginary pair into the Hermitian eigenvalues `+sigma,-sigma`, proving (2).

This rank collapse is not an extra arithmetic hypothesis. It follows from the real-residue Fourier symmetry already assumed in `PL-428`.

## 2. The residue diagonal exposes `d-b`

The hidden character perturbation is `iB`. Transforming it back to residue coordinates gives the exact real-symmetric matrix

\[
F(iB)F^*
=
\begin{pmatrix}
0&(-b-d+f)/2&0&(b+d-f)/2\\
(-b-d+f)/2&-b+d&(-b-d-f)/2&0\\
0&(-b-d-f)/2&0&(b+d+f)/2\\
(b+d-f)/2&0&(b+d+f)/2&b-d
\end{pmatrix}.
\tag{15}
\]

In particular,

\[
\boxed{
\operatorname{Diag}\!\bigl(F(iB)F^*\bigr)
=(0,d-b,0,b-d).
}
\tag{16}
\]

Let

\[
D^{(0)}:=\operatorname{Diag}(FAF^*).
\tag{17}
\]

Since `S=F(A+iB)F^*`, equations (3) and (16) imply

\[
D-D^{(0)}=(0,r,0,-r),
\qquad r=d-b.
\tag{18}
\]

Thus, once `A` is reconstructed from all real quadratic probes as in `PL-428`, the residue variances required by the cone test themselves recover `r`. The three-dimensional kernel of the real-product map therefore intersects the fixed-residue-diagonal fiber in only two dimensions.

This can also be seen directly from the kernel basis displayed in `PL-428`: two independent combinations have zero residue diagonal, whereas the third changes the second and fourth residue variances with opposite signs.

## 3. Canonical split into one visible and two invisible oriented coordinates

Introduce

\[
r=d-b,
\qquad
s=b+d,
\tag{19}
\]

so that

\[
b=\frac{s-r}{2},
\qquad
d=\frac{s+r}{2}.
\tag{20}
\]

Then (2) becomes

\[
\boxed{
\sigma^2=s^2+r^2+f^2.
}
\tag{21}
\]

Split

\[
B=B_r+B_{s,f},
\tag{22}
\]

where `B_r` is obtained by setting `s=f=0` and `B_{s,f}` by setting `r=0`. The first term is known once `A` and `D` are known through (18). The second satisfies

\[
\operatorname{Diag}\!\bigl(F(iB_{s,f})F^*\bigr)=0
\tag{23}
\]

and

\[
\boxed{
\|iB_{s,f}\|_{\mathrm{op}}
=\sqrt{s^2+f^2}.
}
\tag{24}
\]

So the residual oriented uncertainty after using the gate's own diagonal data is a two-dimensional Euclidean disk in the coordinates `(s,f)`, represented by a rank-two Hermitian perturbation. The known coordinate `r` is not merely bounded by the residue variances; it is algebraically determined by them after subtracting the `A` contribution.

Equivalently, two genuinely complex polarization measurements suffice to finish reconstruction once `A` and `D` are known. One may take observables that recover

\[
\Im(K_{01}+K_{21})=s
\tag{25}
\]

and

\[
\Im K_{13}=f.
\tag{26}
\]

The third individual imaginary coherence is then fixed by `(r,s)`. This narrows the three-coherence tomography surface left by `PL-428`; it does not make either of the two remaining oriented observables real-product variances.

## 4. A weaker sufficient certification of the `PL-421` cone

At `p=5`, `PL-421` asks for

\[
S-\frac14D\succeq0.
\tag{27}
\]

Conjugating by `F` gives the equivalent character-space condition

\[
K-\frac14F^*DF\succeq0.
\tag{28}
\]

Using (22), define the part determined by `A` and `D`,

\[
H_{\mathrm{known}}
:=A+iB_r-\frac14F^*DF.
\tag{29}
\]

Then exactly

\[
K-\frac14F^*DF
=H_{\mathrm{known}}+iB_{s,f}.
\tag{30}
\]

Weyl's elementary eigenvalue perturbation bound and (24) give

\[
\lambda_{\min}\!\left(K-\frac14F^*DF\right)
\ge
\lambda_{\min}(H_{\mathrm{known}})
-\sqrt{s^2+f^2}.
\tag{31}
\]

Therefore the quantitative condition

\[
\boxed{
\lambda_{\min}(H_{\mathrm{known}})
\ge \sqrt{s^2+f^2}
}
\tag{32}
\]

is sufficient for local-factor image admission. More generally, any theorem proving a visible margin `eta` together with

\[
\sqrt{s^2+f^2}\le\eta
\tag{33}
\]

closes the finite-dimensional cone gate.

Equation (32) is intentionally only sufficient, not necessary. The important point is the theorem surface: one need not obtain a full arbitrary-complex-direction covariance asymptotic merely to certify the cone. A real-sector lower bound plus the residue diagonal plus a norm estimate for **two** oriented coordinates is enough.

For the quarter-turn route of `PL-431`--`PL-432`, this means the representation-theoretic burden can likewise be compressed. After the residue diagonal has fixed `r`, vertical-shift tomography need only recover or bound the combinations `(s,f)`, not three independent imaginary entries.

## 5. Why the remaining two-dimensional fiber is genuine

The reduction from three parameters to two must not be confused with automatic positivity. `PL-428` already gives

\[
S_t=I_4+tA_1,
\tag{34}
\]

where `A_1` has zero diagonal and lies in the real-product blind kernel. Hence every `S_t` in that family has the same residue diagonal and the same scalar variance for every real character coefficient vector, while the `PL-421` cone verdict changes when `t` crosses the exact threshold recorded there.

In the parameterization above that example lies inside the `r=0` fixed-diagonal fiber. Thus the residual two-dimensional sector is not a bookkeeping artifact: at least one of its directions can already move a positive-semidefinite covariance across the dephasing image boundary while all the newly declared visible data remain fixed.

No argument here shows that the actual prime source realizes a large `(s,f)`. The point is the opposite: any successful arithmetic theorem now has a smaller and more explicit object to control.

## 6. Prior-art and novelty audit

The ingredients used in the derivation are standard finite-dimensional facts: conjugate symmetry of the DFT of a real signal, the Pfaffian identity `det B = pf(B)^2` for even skew-symmetric matrices, even rank of real skew-symmetric matrices, and the operator-norm/Weyl perturbation bound. No novelty is claimed for any of them.

`PL-428` already identified the three imaginary coherences and exhibited a three-dimensional kernel for real product probes. `PL-421` already made the residue diagonal part of the exact local-factor cone test. Targeted repository and literature searches did not locate the **combined line-specific reduction** derived here: imposing the mod-5 reality pattern on the `PL-428` blind sector forces Pfaffian zero and rank two, while intersecting that sector with the residue-diagonal data of `PL-421` removes one coordinate exactly and leaves the two-parameter disk `(s,f)`.

The durable delta is therefore not a new Fourier or Pfaffian theorem. It is the exact reduction of the live arithmetic certification problem from an apparently three-component complex covariance defect, or a full arbitrary-complex-direction matrix lower bound, to a two-coordinate rank-two perturbation problem after all data already required by the gate are used.

## 7. Adversarial audit and boundaries

1. **Exact residue diagonal is part of the reduction.** If an arithmetic argument only bounds `D` rather than determines it to the precision needed in (18), the uncertainty in `r` must be added back to the error budget. The algebraic dimension reduction does not manufacture an estimate for `D`.
2. **Real-product data are idealized complete data here.** Existing unconditional scalar lower-bound theorems audited in `PL-436` do not automatically reconstruct all of `A`. This finding reduces the representation target; it does not improve the available number theory.
3. **Rank two does not mean small.** The residual norm `sqrt(s^2+f^2)` can be of the same order as the visible covariance. The matched family from `PL-428` prevents any inference that fixed diagonal plus real-product data alone imply the cone condition.
4. **The Weyl test is sufficient only.** Failure of (32) does not imply failure of the exact cone test. A sharper argument may exploit the orientation of the rank-two perturbation relative to `H_known`.
5. **The parameter names depend on the Fourier convention.** Reordering residue classes or replacing the generator of `U_5` changes signs/coordinates, but the invariant statements—rank at most two, one diagonal-visible combination, and a two-dimensional fixed-diagonal blind fiber—do not depend on that convention.
6. **Positive semidefiniteness of `K` adds constraints but does not collapse the residual fiber.** `PL-428` supplies an explicit PSD path inside a fixed visible-data fiber whose local admission changes.
7. **No RH implication is claimed.** The missing step remains an unconditional or genuinely weaker-than-RH arithmetic estimate proving enough visible coercivity and controlling `(s,f)` at the source parameters required by the line.

## Consequence for the line

The next arithmetic search should not be phrased as requiring an unconditional theorem for the entire `4 x 4` complex covariance matrix. The finite mod-5 geometry is more economical. After real-sector information and the residue variances are incorporated, the genuinely oriented obstruction is a rank-two perturbation determined by only

\[
\boxed{
\Im(K_{01}+K_{21})
\quad\text{and}\quad
\Im K_{13}.
}
\tag{35}
\]

A direct prime-side estimate, a quarter-turn scalar theorem, or another non-circular mechanism that controls those two combinations strongly enough relative to the visible spectral margin would suffice for the representation step. Conversely, any proposed scalar route that still cannot see these two combinations remains information-theoretically incomplete even after all residue variances are supplied.