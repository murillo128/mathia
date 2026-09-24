# PL-442 — Cyclic mod-5 stationarization preserves covariance positivity while the restricted Frobenius fit can fail

**Evidence/status:** `EXACT-DERIVED + PRIOR-ART-AUDITED + THEOREM-SURFACE-NARROWING`; substantive refinement.

**Parent findings:** `PL-421`, `PL-440`, `PL-441`.

## Claim

`PL-441` reduced the current `p=5` local-factor gate to a lag-stationary covariance model but left the phrase “best lag-stationary approximation” deliberately unspecified. There are at least two natural projections, and they have materially different structural behavior.

For a real symmetric covariance

\[
S=(S_{ab})_{a,b\in U_5},\qquad U_5=\{1,2,3,4\},\qquad S\succeq0,
\tag{1}
\]

set

\[
D=\sum_{a=1}^4 S_{aa},\qquad
U=S_{12}+S_{23}+S_{34},\qquad
V=S_{13}+S_{14}+S_{24}.
\tag{2}
\]

The lag-stationary family from `PL-441` is

\[
T(d,u,v)=
\begin{pmatrix}
d&u&v&v\\
u&d&u&v\\
v&u&d&u\\
v&v&u&d
\end{pmatrix}.
\tag{3}
\]

The ordinary Frobenius projection of `S` onto this three-dimensional family is

\[
\boxed{d_F=\frac D4,\qquad u_F=\frac U3,\qquad v_F=\frac V3.}
\tag{4}
\]

It is the unique least-squares fit in the restricted `4 x 4` model, but it need not remain positive semidefinite even when `S` is a covariance.

There is a second, line-specific stationarization canonically induced by the zero-extension to `Z/5Z` already used in `PL-440`. Extend `S` to a `5 x 5` matrix `\widetilde S` by inserting a zero row and column at residue `0`, let `R` be the cyclic shift on `Z/5Z`, and define the Reynolds average

\[
C=\frac15\sum_{t=0}^4R^t\widetilde S R^{-t}.
\tag{5}
\]

Then `C` is a real symmetric positive-semidefinite circulant matrix. Its principal `U_5` compression has the form (3), with

\[
\boxed{d_R=\frac D5,\qquad u_R=\frac U5,\qquad v_R=\frac V5.}
\tag{6}
\]

Thus this cyclic stationarization preserves covariance positivity exactly. If

\[
m=\frac{u+v}{2},\qquad f=u-v,
\tag{7}
\]

and `D>0`, the normalized coordinates of the two fits satisfy the deterministic contraction

\[
\boxed{
\left(\frac{m_R}{d_R},\frac{f_R}{d_R}\right)
=
\frac34
\left(\frac{m_F}{d_F},\frac{f_F}{d_F}\right).
}
\tag{8}
\]

The factor `3/4` is not a fitted constant. It comes exactly from the missing residue `0`: the diagonal orbit contains four nonzero entries out of five, whereas each nonzero-lag orbit contains only three.

Finally, the same Reynolds projection gives a canonical quantitative anisotropy defect. Since (5) is the Frobenius-orthogonal projection of `\widetilde S` onto the cyclic fixed-point algebra,

\[
\boxed{
\|\widetilde S-C\|_F^2
=
\|S\|_F^2-
\frac{D^2+2U^2+2V^2}{5}.
}
\tag{9}
\]

Combining (9) with the perturbative gate in `PL-441` yields an explicit sufficient certificate for transferring the stationary dephasing condition to the actual covariance. This removes an ambiguity in the live theorem surface: a covariance-respecting stationary surrogate exists canonically, but positivity of that surrogate is strictly weaker than the required dephasing positivity.

No prime asymptotic, RH implication, or claim of new circulant-matrix theory is contained in this finding.

## 1. The restricted Frobenius fit

The stationary family (3) is a linear subspace of real symmetric `4 x 4` matrices. The diagonal pattern occurs four times, while the `u` and `v` patterns each occur in three unordered off-diagonal pairs, hence six matrix entries. Orthogonal projection in Frobenius norm therefore gives

\[
d_F=\frac14\sum_aS_{aa}=\frac D4,
\tag{10}
\]

\[
u_F=\frac13(S_{12}+S_{23}+S_{34})=\frac U3,
\tag{11}
\]

and

\[
v_F=\frac13(S_{13}+S_{14}+S_{24})=\frac V3.
\tag{12}
\]

This is the exact unrestricted least-squares solution inside the `PL-441` model. It does **not** inherit the positive-semidefinite cone.

Take

\[
x=(1,0,1,0)^T,
\qquad
S=xx^T\succeq0.
\tag{13}
\]

Then

\[
D=2,\qquad U=0,\qquad V=1,
\tag{14}
\]

so

\[
d_F=\frac12,\qquad u_F=0,\qquad v_F=\frac13,
\tag{15}
\]

and

\[
m_F=\frac16,\qquad f_F=-\frac13.
\tag{16}
\]

The smallest eigenvalue of the stationary matrix itself is

\[
d_F-m_F-\frac{\sqrt5}{2}|f_F|
=
\frac{2-\sqrt5}{6}<0.
\tag{17}
\]

Thus even a rank-one covariance can have a Frobenius-best restricted stationary fit that is not a covariance. The phrase “best stationary approximation” cannot therefore be interpreted as unconstrained `4 x 4` least squares if positivity is meant to be preserved automatically.

This counterexample does not rule out a constrained nearest positive-semidefinite stationary approximation. It only separates that nonlinear problem from the natural linear projection.

## 2. Cyclic Reynolds stationarization

Embed `S` into `Z/5Z` by

\[
\widetilde S_{ab}=
\begin{cases}
S_{ab},&a,b\in U_5,\\
0,&a=0\text{ or }b=0.
\end{cases}
\tag{18}
\]

If `S\succeq0`, then `\widetilde S\succeq0`. Every cyclic conjugate in (5) is therefore positive semidefinite, so

\[
\boxed{C\succeq0.}
\tag{19}
\]

The average commutes with `R`, hence is circulant. Its diagonal coefficient is the mean over the five diagonal positions,

\[
d_R=\frac15\sum_{a\in U_5}S_{aa}=\frac D5.
\tag{20}
\]

For lag `1`, only the pairs `(1,2)`, `(2,3)`, `(3,4)` survive the zero extension, giving

\[
u_R=\frac15(S_{12}+S_{23}+S_{34})=\frac U5.
\tag{21}
\]

For lag `2`, the surviving pairs are `(1,3)`, `(2,4)`, and `(4,1)`, giving

\[
v_R=\frac15(S_{13}+S_{24}+S_{14})=\frac V5.
\tag{22}
\]

The principal `U_5` submatrix of `C` is therefore exactly `T(d_R,u_R,v_R)`, and as a principal submatrix of a positive matrix it is positive semidefinite.

For the Frobenius fit,

\[
\frac{m_F}{d_F}=\frac{2(U+V)}{3D},
\qquad
\frac{f_F}{d_F}=\frac{4(U-V)}{3D}.
\tag{23}
\]

For the cyclic fit,

\[
\frac{m_R}{d_R}=\frac{U+V}{2D},
\qquad
\frac{f_R}{d_R}=\frac{U-V}{D}.
\tag{24}
\]

Equations (23)--(24) give (8) exactly.

The contraction is therefore a finite-group boundary effect caused by deleting residue `0`, not an arithmetic cancellation theorem. In particular, it is present for every positive-semidefinite input matrix, independently of whether that matrix comes from primes.

## 3. Positivity of the cyclic surrogate is weaker than the dephasing gate

The full circulant `C` has first row `(d_R,u_R,v_R,v_R,u_R)`. Its discrete Fourier eigenvalues are

\[
\lambda_0=d_R+4m_R,
\tag{25}
\]

\[
\lambda_{1,4}=d_R-m_R+\frac{\sqrt5}{2}f_R,
\tag{26}
\]

and

\[
\lambda_{2,3}=d_R-m_R-\frac{\sqrt5}{2}f_R.
\tag{27}
\]

Thus, with

\[
x_R=\frac{m_R}{d_R},\qquad y_R=\frac{f_R}{d_R},
\tag{28}
\]

positive semidefiniteness of the group-averaged covariance only forces

\[
\boxed{x_R\ge-\frac14,}
\tag{29}
\]

and

\[
\boxed{|y_R|\le\frac2{\sqrt5}(1-x_R).}
\tag{30}
\]

This is broader than the `PL-441` dephasing wedge–ellipse, which requires positivity of

\[
\Phi(T)=T-\frac14\operatorname{Diag}(T)
\tag{31}
\]

rather than positivity of `T` itself.

The rank-one example (13) makes the gap explicit. The cyclic surrogate has

\[
d_R=\frac25,\qquad u_R=0,\qquad v_R=\frac15,
\tag{32}
\]

so

\[
m_R=\frac1{10},\qquad f_R=-\frac15,
\qquad
(x_R,y_R)=\left(\frac14,-\frac12\right).
\tag{33}
\]

It is positive semidefinite by construction, but the smaller reflection-odd eigenvalue of the dephased matrix is

\[
\frac{3d_R}{4}-m_R-\frac{\sqrt5}{2}|f_R|
=
\frac{2-\sqrt5}{10}<0.
\tag{34}
\]

Hence group averaging cannot prove the local-factor image condition by positivity alone. The arithmetic still has to place the stationary coordinates inside the stricter lens of `PL-441`.

## 4. A canonical anisotropy energy and transfer certificate

The Reynolds average (5) is idempotent and self-adjoint for the Frobenius inner product. Therefore

\[
\|\widetilde S-C\|_F^2
=
\|\widetilde S\|_F^2-\|C\|_F^2.
\tag{35}
\]

Zero extension preserves the Frobenius norm, so `\|\widetilde S\|_F=\|S\|_F`. Since each row of `C` contains one `d_R`, two `u_R`, and two `v_R`,

\[
\|C\|_F^2
=5(d_R^2+2u_R^2+2v_R^2)
=\frac{D^2+2U^2+2V^2}{5}.
\tag{36}
\]

This proves (9).

Let

\[
S_{\rm cyc}=T(d_R,u_R,v_R)
\tag{37}
\]

be the `U_5` compression of `C`, and put

\[
E=S-S_{\rm cyc}.
\tag{38}
\]

Because `E` is a principal compression of `\widetilde S-C`,

\[
\|E\|_{\rm op}
\le\|\widetilde S-C\|_{\rm op}
\le\|\widetilde S-C\|_F.
\tag{39}
\]

Write

\[
\eta=\lambda_{\min}(\Phi(S_{\rm cyc})).
\tag{40}
\]

`PL-441` proved

\[
\|\Phi(E)\|_{\rm op}\le\frac54\|E\|_{\rm op}.
\tag{41}
\]

Consequently, if `\eta>0` and

\[
\boxed{
\|S\|_F^2-rac{D^2+2U^2+2V^2}{5}
<\left(\frac{4\eta}{5}\right)^2,
}
\tag{42}
\]

then

\[
\Phi(S)\succ0.
\tag{43}
\]

There is an equally useful obstruction version. If

\[
\lambda_{\min}(\Phi(S_{\rm cyc}))\le-\eta<0
\tag{44}
\]

and the left side of (42) is smaller than `(4\eta/5)^2`, then `\Phi(S)` still has a negative eigenvalue.

Equation (42) is only a sufficient Frobenius-control criterion; it is not asserted to be sharp in operator norm. Its value is structural: the live `PL-441` requirement “stationary margin plus small anisotropic remainder” now has a canonical covariance-preserving surrogate and an exactly computable anisotropy energy.

For reference, the stationary margin in (40) is explicitly

\[
\eta=
\min\left\{
\frac{3d_R}{4}-m_R-\frac{\sqrt5}{2}|f_R|,
\frac{3d_R}{4}+m_R-\frac12\sqrt{f_R^2+16m_R^2}
\right\}.
\tag{45}
\]

Thus every quantity in (42) is determined directly by the original covariance matrix.

## 5. Prior-art and adversarial audit

Finite-group Reynolds averaging, conditional expectation onto a fixed-point algebra, Fourier diagonalization of circulant matrices, and Frobenius-nearest circulant approximations are classical. In particular, the nearest-circulant/preconditioning literature already treats Frobenius projection onto circulant algebras and its positivity behavior; a standard anchor is T. F. Chan, “An Optimal Circulant Preconditioner for Toeplitz Systems,” *SIAM Journal on Scientific and Statistical Computing* **9**(4) (1988), 766–771, DOI `10.1137/0909051`. No novelty claim is made for any of those general constructions.

The line-specific content is the comparison forced by the incomplete residue set `U_5` and the zero-extension convention already present in `PL-440`: the restricted `4 x 4` least-squares fit and the `Z/5Z` Reynolds fit differ by the exact normalized factor `3/4`; the former can leave the covariance cone; the latter cannot; and its full-group Frobenius residual gives the explicit transfer certificate (42) for the dephasing lens of `PL-441`.

The prior-art audit searched finite cyclic stationary covariance, nearest circulant/circulant preconditioner theory, positive conditional expectations under finite group actions, residue-class covariance, Dirichlet-character covariance, and prime short-interval variance. It found the general projection machinery but no arithmetic theorem implying the required `p=5` lens margin or controlling (9) at the needed covariance scale. The generic matrix theory is therefore calibration, not evidence for the unresolved prime estimate.

The main adversarial control is (34): even the positivity-preserving canonical average can lie outside the dephasing image cone. Any argument that replaces the actual arithmetic problem by “average the covariance, which stays positive” loses exactly the stronger positivity that matters.

## 6. Boundaries and falsification conditions

1. **Zero extension is bookkeeping, not a hidden fifth arithmetic channel.** The residue `0 mod 5` coordinate is inserted with zero covariance because this is the extension used to expose the lag characters in `PL-440`. The Reynolds average is canonical relative to that convention, not canonical among every conceivable embedding.

2. **The cyclic surrogate is not claimed to be operator-norm nearest.** It is the exact group average in the `5 x 5` zero-extended space. The restricted Frobenius fit (4) solves a different projection problem in the `4 x 4` space.

3. **The Frobenius counterexample has a narrow meaning.** It shows only that unconstrained restricted least squares can destroy positivity. It does not prove that the nearest positive-semidefinite stationary fit is far away or hard to compute.

4. **Covariance positivity is not the target positivity.** Equations (25)--(30) describe the ordinary PSD cone of the cyclic surrogate. The dephased gate is strictly smaller, as (34) shows.

5. **The residual bound is sufficient, not optimal.** Passing from operator norm to Frobenius norm in (39) can be wasteful. Failure of (42) says nothing by itself about failure of the true gate.

6. **No arithmetic estimate has been supplied.** The finding identifies `D,U,V` and the residual energy (9) as exact observables to estimate. It does not show that the canonical prime covariance has positive margin `\eta` or small anisotropy.

7. **No RH consequence follows from this finite-dimensional reduction alone.** Any RH-relevant progress still requires independently controlled signed prime correlation at the covariance scale, in accordance with the line mandate.

## Consequence for the line

The immediate `PL-441` program can now be made unambiguous. Instead of speaking generically about a “best stationary approximation,” first form the `Z/5Z` cyclic Reynolds surrogate (5). It preserves the covariance cone, exposes the same quadratic-lag coordinate `f` as `PL-440`, and yields the exact normalized point `(x_R,y_R)` to test against the `PL-441` wedge–ellipse.

Then measure anisotropy by the exact residual energy (9). A positive stationary dephasing margin together with (42) certifies the full gate; a robustly negative stationary margin plus the same small-residual condition certifies failure. If neither inequality is available, the remaining problem is no longer finite-dimensional linear algebra: it is precisely the arithmetic task of controlling the start-residue anisotropy and the signed lag imbalance at the natural variance scale.

This narrows the next theorem surface to two quantitative observables derived directly from the canonical covariance: the dephasing margin of the cyclic surrogate and the Reynolds residual. Any future prime estimate that does not control one of these, or an operator-norm substitute of comparable strength, cannot close the current local-factor gate.
