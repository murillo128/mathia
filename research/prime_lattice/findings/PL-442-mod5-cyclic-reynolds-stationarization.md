# PL-442 — Cyclic mod-5 stationarization preserves covariance positivity while the restricted Frobenius fit can fail

**Evidence/status:** `EXACT-DERIVED + PRIOR-ART-AUDITED + THEOREM-SURFACE-NARROWING`; corrected transfer certificate preserving the core stationarization claim.

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

Equation (9) is an exact full-group anisotropy energy, but it is **not** a usable transfer budget for the restricted `4 x 4` arithmetic covariance: the zero-extended residue-`0` row and column impose an unavoidable positive error floor. For every nonzero positive-semidefinite `S`, the sufficient inequality obtained by comparing (9) directly with the `PL-441` perturbative margin is impossible.

The arithmetic-facing transfer must instead use the actual compressed residual `E_R=S-S_cyc`. Its exact Frobenius norm is derived in Section 4, and the resulting corrected certificate has nonempty feasibility (for example `S=I_4`). Thus a covariance-respecting stationary surrogate still exists canonically, but the full-group Reynolds error is only a diagnostic of the zero-extended group action; the compressed residual is the relevant perturbation budget on `U_5`.

There is one further exact strengthening. Because the dephasing cone is positively homogeneous, the relevant stationary object is not only the fixed normalization `S_cyc` but the positive ray `c S_cyc`, `c>0`. Optimizing the transfer certificate along that ray removes purely radial mismatch without changing the normalized stationary coordinates. The optimal scale is explicit, the trace-matching scale `c=5/4` already improves the normalized residual strictly for every nonzero covariance, and the full five-dimensional Reynolds residual remains universally unusable even after arbitrary positive rescaling because the artificial residue-zero row/column leaves a scale-invariant error floor.

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

## 4. Full-group anisotropy, its vacuity floor, and the compressed transfer certificate

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

This proves (9). The crucial correction is that (9) measures the error in the **five-dimensional zero-extended space**, including the artificial residue-`0` row and column.

Let

\[
S_{\rm cyc}=T(d_R,u_R,v_R)
\tag{37}
\]

be the `U_5` compression of `C`, and define the arithmetic-facing residual

\[
E_R=S-S_{\rm cyc}.
\tag{38}
\]

Directly from (2), (6), and the multiplicities of the stationary patterns,

\[
\langle S,S_{\rm cyc}\rangle_F
=d_R D+2u_R U+2v_R V
=\frac{D^2+2U^2+2V^2}{5},
\tag{39}
\]

while

\[
\|S_{\rm cyc}\|_F^2
=4d_R^2+6u_R^2+6v_R^2
=\frac{4D^2+6U^2+6V^2}{25}.
\tag{40}
\]

Hence

\[
\boxed{
\|E_R\|_F^2
=
\|S\|_F^2-
\frac{6D^2+14U^2+14V^2}{25}.
}
\tag{41}
\]

Subtracting (41) from the full-group error (9) gives the exact cost of the artificial coordinate:

\[
\boxed{
\|\widetilde S-C\|_F^2-\|E_R\|_F^2
=
\frac{D^2+4U^2+4V^2}{25}.
}
\tag{42}
\]

Thus the omitted contribution is not arithmetic anisotropy among the four nonzero residue channels; it is exactly the row/column introduced by zero extension.

Write

\[
\eta=\lambda_{\min}(\Phi(S_{\rm cyc})).
\tag{43}
\]

For `E_R`, the perturbative estimate from `PL-441` gives

\[
\|\Phi(E_R)\|_{\rm op}
\le\frac54\|E_R\|_{\rm op}
\le\frac54\|E_R\|_F.
\tag{44}
\]

Consequently, if `\eta>0` and

\[
\boxed{
\|S\|_F^2-
\frac{6D^2+14U^2+14V^2}{25}
<
\left(\frac{4\eta}{5}\right)^2,
}
\tag{45}
\]

then

\[
\Phi(S)\succ0.
\tag{46}
\]

The same argument gives the obstruction version: if
`\lambda_{\min}(\Phi(S_{\rm cyc}))\le-\eta<0` and the left side of (45) is smaller than `(4\eta/5)^2`, then `\Phi(S)` still has a negative eigenvalue.

The original attempt to use the full-group error (9) in place of (41) is universally vacuous on nonzero covariances. Indeed, Cauchy--Schwarz on the four diagonal entries and separately on each group of three off-diagonal entries gives

\[
\|S\|_F^2
\ge
\frac{D^2}{4}+\frac23(U^2+V^2).
\tag{47}
\]

Therefore the full-group error satisfies

\[
\|\widetilde S-C\|_F^2
\ge
\frac{D^2}{20}+\frac4{15}(U^2+V^2)
\ge\frac{D^2}{20}.
\tag{48}
\]

On the positive-margin branch, `\operatorname{tr}\Phi(S_{\rm cyc})=3D/5`, so

\[
\eta\le\frac{3D}{20}
\quad\Longrightarrow\quad
\left(\frac{4\eta}{5}\right)^2
\le\frac{9D^2}{625}
<
\frac{D^2}{20}
\le
\|\widetilde S-C\|_F^2.
\tag{49}
\]

For every nonzero positive-semidefinite `S`, one has `D>0`; hence a certificate obtained by substituting the full-group error (9) into the perturbative inequality can never pass. The implication itself was formally correct, but its sufficient hypothesis was unattainable.

The exact rational control `S=I_4` shows that the compressed repair is nonvacuous. Here

\[
D=4,\qquad U=V=0,\qquad
\eta=\frac35,
\]

and

\[
\|\widetilde S-C\|_F^2=\frac45,
\qquad
\|E_R\|_F^2=\frac4{25}
<
\left(\frac{4\eta}{5}\right)^2
=
\frac{144}{625}.
\]

Thus the full-group criterion fails while the corrected compressed criterion succeeds.

There is also a distinct norm-optimal restricted surrogate. If

\[
S_F=T(d_F,u_F,v_F),
\]

then orthogonal projection in the restricted `4 x 4` stationary family gives

\[
\boxed{
\|S-S_F\|_F^2
=
\|S\|_F^2-\frac{D^2}{4}-\frac23(U^2+V^2).
}
\tag{50}
\]

This residual is no larger than `\|E_R\|_F`, because `S_F` is the Frobenius-best point in the same three-dimensional family. Section 1 shows, however, that `S_F` can fail to be positive semidefinite. The two surrogates therefore serve different purposes: `S_{\rm cyc}` is the canonical covariance-preserving stationarization, whereas `S_F` is the optimal restricted Frobenius approximation. A perturbative transfer may use either surrogate when its own dephasing margin is positive, but only the Reynolds surrogate preserves covariance positivity automatically.

For reference, the stationary margin in (43) is explicitly

\[
\eta=
\min\left\{
\frac{3d_R}{4}-m_R-\frac{\sqrt5}{2}|f_R|,
\frac{3d_R}{4}+m_R-\frac12\sqrt{f_R^2+16m_R^2}
\right\}.
\tag{51}
\]

Thus every quantity in the corrected certificate (45) is determined directly by the original covariance matrix.

### Scale-free positive-ray strengthening

The target cone is homogeneous: for every `c>0`,

\[
\Phi(cS_{\rm cyc})=c\Phi(S_{\rm cyc}),
\tag{52}
\]

so the normalized stationary coordinates `(x_R,y_R)` are unchanged while the stationary margin becomes `c\eta`. It is therefore natural to optimize the perturbative certificate over the positive ray generated by `S_{\rm cyc}`, rather than fixing the Reynolds normalization `c=1`.

Write

\[
N=\|S\|_F^2,\qquad R=U^2+V^2,
\qquad Q=D^2+2R,
\qquad P=4D^2+6R.
\tag{53}
\]

Equations (39)--(40) give

\[
\langle S,S_{\rm cyc}\rangle_F=\frac Q5,
\qquad
\|S_{\rm cyc}\|_F^2=\frac P{25}.
\tag{54}
\]

For `c>0`, define the scale-normalized compressed residual

\[
\rho(c)^2
:=\frac{\|S-cS_{\rm cyc}\|_F^2}{c^2}
=\frac{N}{c^2}-\frac{2Q}{5c}+\frac P{25}.
\tag{55}
\]

The transfer argument (44) now reads

\[
\boxed{\rho(c)<\frac{4\eta}{5}\quad\Longrightarrow\quad \Phi(S)\succ0.}
\tag{56}
\]

Since `S\neq0` and `S\succeq0` imply `D>0`, one has `Q>0`. Setting `t=1/c` turns (55) into a strictly convex quadratic `Nt^2-(2Q/5)t+P/25`. Hence the unique positive optimum is

\[
\boxed{c_*=\frac{5N}{Q}=\frac{5\|S\|_F^2}{D^2+2U^2+2V^2},}
\tag{57}
\]

with

\[
\boxed{
\rho_*^2
=\frac1{25}\left(P-\frac{Q^2}{N}\right)
=\frac{N(4D^2+6U^2+6V^2)-(D^2+2U^2+2V^2)^2}{25N}.
}
\tag{58}
\]

Thus (56) can be replaced by the scale-free sufficient condition `\rho_*<4\eta/5`. Nonnegativity of (58) is just Cauchy--Schwarz applied to `S` and `S_{\rm cyc}`; equality means that `S` itself lies on the positive ray generated by the Reynolds surrogate.

A particularly simple universal representative of that ray is the trace-matching scale

\[
 c_0=\frac54,
\qquad
\operatorname{tr}(c_0S_{\rm cyc})=D=\operatorname{tr}S.
\tag{59}
\]

It strictly improves the normalized residual relative to the unscaled choice for every nonzero covariance. Indeed,

\[
\rho(1)^2-\rho(5/4)^2
=\frac{9N-2Q}{25}.
\tag{60}
\]

Using (47),

\[
9N-2Q
\ge \frac{D^2}{4}+2(U^2+V^2)>0.
\tag{61}
\]

For the exact control `S=I_4`, `S_{\rm cyc}=(4/5)I_4`, so `c_0S_{\rm cyc}=I_4` and the compressed residual vanishes exactly. The improvement is therefore not merely formal.

Positive rescaling does **not** rescue the full five-dimensional Reynolds residual. Let `C` be the full circulant average from (5) and set

\[
\rho_{\rm full}(c)^2
:=\frac{\|\widetilde S-cC\|_F^2}{c^2}.
\tag{62}
\]

The artificial residue-zero row and column give the exact scale-independent gap

\[
\boxed{
\rho_{\rm full}(c)^2-\rho(c)^2
=\frac{D^2+4U^2+4V^2}{25}
\ge\frac{D^2}{25}.
}
\tag{63}
\]

But `\eta\le3D/20`, so `(4\eta/5)^2\le9D^2/625<D^2/25`. Consequently **no positive scale `c` can make the full-group residual satisfy the perturbative transfer criterion**. The obstruction in (49) is therefore not an artifact of having fixed `c=1`; it comes from the zero-extension coordinate itself.

## 5. Prior-art and adversarial audit

Finite-group Reynolds averaging, conditional expectation onto a fixed-point algebra, Fourier diagonalization of circulant matrices, and Frobenius-nearest circulant approximations are classical. In particular, the nearest-circulant/preconditioning literature already treats Frobenius projection onto circulant algebras and its positivity behavior; a standard anchor is T. F. Chan, “An Optimal Circulant Preconditioner for Toeplitz Systems,” *SIAM Journal on Scientific and Statistical Computing* **9**(4) (1988), 766–771, DOI `10.1137/0909051`. No novelty claim is made for any of those general constructions.

Tyrtyshnikov's later distinction between optimal and superoptimal circulant preconditioners is useful calibration for the scale-free refinement: the former minimizes an absolute Frobenius residual, while the latter minimizes a relative residual of the form `||I-C^{-1}A||_F`. The scalar-ray optimization (55)--(58) is only an elementary one-dimensional analogue adapted to the present dephasing transfer problem; its formulas and the zero-extension floor (63) are not attributed to that preconditioning literature.

The line-specific content is the comparison forced by the incomplete residue set `U_5` and the zero-extension convention already present in `PL-440`: the restricted `4 x 4` least-squares fit and the `Z/5Z` Reynolds fit differ by the exact normalized factor `3/4`; the former can leave the covariance cone; the latter cannot; the full-group Reynolds residual has the exact vacuity floor (48)--(49); and the compressed residual (41) gives the corrected transfer certificate (45) for the dephasing lens of `PL-441`.

The prior-art audit searched finite cyclic stationary covariance, nearest circulant/circulant preconditioner theory, positive conditional expectations under finite group actions, residue-class covariance, Dirichlet-character covariance, and prime short-interval variance. It found the general projection machinery but no arithmetic theorem implying the required `p=5` lens margin or controlling (9) at the needed covariance scale. The generic matrix theory is therefore calibration, not evidence for the unresolved prime estimate.

The main adversarial control is (34): even the positivity-preserving canonical average can lie outside the dephasing image cone. Any argument that replaces the actual arithmetic problem by “average the covariance, which stays positive” loses exactly the stronger positivity that matters.

## 6. Boundaries and falsification conditions

1. **Zero extension is bookkeeping, not a hidden fifth arithmetic channel.** The residue `0 mod 5` coordinate is inserted with zero covariance because this is the extension used to expose the lag characters in `PL-440`. The Reynolds average is canonical relative to that convention, not canonical among every conceivable embedding.

2. **The cyclic surrogate is not claimed to be operator-norm nearest.** It is the exact group average in the `5 x 5` zero-extended space. The restricted Frobenius fit (4) solves a different projection problem in the `4 x 4` space.

3. **The Frobenius counterexample has a narrow meaning.** It shows only that unconstrained restricted least squares can destroy positivity. It does not prove that the nearest positive-semidefinite stationary fit is far away or hard to compute.

4. **Covariance positivity is not the target positivity.** Equations (25)--(30) describe the ordinary PSD cone of the cyclic surrogate. The dephased gate is strictly smaller, as (34) shows.

5. **The compressed residual certificate is sufficient, not optimal.** Passing from operator norm to Frobenius norm in (44) can be wasteful. Failure of (45) says nothing by itself about failure of the true gate. The full-group residual (9) must not be substituted into this transfer test: (49) shows that doing so makes the sufficient hypothesis vacuous for every nonzero covariance.

6. **No arithmetic estimate has been supplied.** The finding identifies `D,U,V` and the compressed residual (41) as the exact arithmetic-facing observables to estimate. The full-group energy (9) remains a valid group-action diagnostic, but not the perturbative transfer budget. Nothing here shows that the canonical prime covariance has positive margin `\eta` or small compressed anisotropy.

7. **No RH consequence follows from this finite-dimensional reduction alone.** Any RH-relevant progress still requires independently controlled signed prime correlation at the covariance scale, in accordance with the line mandate.

## Consequence for the line

The immediate `PL-441` program can now be made unambiguous. Instead of speaking generically about a “best stationary approximation,” first form the `Z/5Z` cyclic Reynolds surrogate (5). It preserves the covariance cone, exposes the same quadratic-lag coordinate `f` as `PL-440`, and yields the exact normalized point `(x_R,y_R)` to test against the `PL-441` wedge–ellipse.

Then measure transfer anisotropy by the exact compressed residual (41), not by the full zero-extended energy (9). A positive stationary dephasing margin together with (45) certifies the full gate; a robustly negative stationary margin plus the same small-compressed-residual condition certifies failure. The full-group quantity (9) remains a useful diagnostic of departure from the cyclic fixed-point algebra, but (49) proves that it cannot itself satisfy the perturbative transfer inequality for a nonzero covariance.

The restricted Frobenius residual (50) is even smaller and is optimal within the stationary `4 x 4` family, but its surrogate can leave the covariance cone. The Reynolds and restricted-Frobenius stationarizations should therefore not be conflated.

Because the cone is homogeneous, the strongest Reynolds-ray certificate should use the optimized scale (57), or at minimum the universally better trace-matching representative `c=5/4`, rather than treating the raw Reynolds normalization as geometrically distinguished. This changes only the radial normalization: the `PL-441` lens coordinates remain fixed. By contrast, no positive rescaling can make the full zero-extended residual into a viable transfer budget, by (63).

If neither corrected inequality is available, the remaining problem is no longer finite-dimensional linear algebra: it is precisely the arithmetic task of controlling the start-residue anisotropy and the signed lag imbalance at the natural variance scale. This narrows the next theorem surface to two quantitative observables derived directly from the canonical covariance: the dephasing margin of a declared stationary surrogate and the corresponding **compressed** residual. Any future prime estimate that controls only the artificial zero-extended error floor cannot close the current local-factor gate.
