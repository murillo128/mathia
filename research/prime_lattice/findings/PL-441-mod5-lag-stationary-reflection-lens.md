# PL-441 — The lag-stationary mod-5 dephasing gate is an exact reflection wedge–ellipse

**Evidence/status:** `EXACT-DERIVED + PRIOR-ART-AUDITED + THEOREM-SURFACE-NARROWING`; substantive reduction.

**Parent findings:** `PL-421`, `PL-438`, `PL-439`, `PL-440`; consistency checks against `PL-422`, `PL-423`.

## Claim

Assume the reduced-residue covariance on `U_5={1,2,3,4}` is real symmetric and depends only on the additive lag modulo `5` after restriction from `Z/5Z`:

\[
S_{ab}=\kappa(b-a),\qquad \kappa(-h)=\kappa(h).
\tag{1}
\]

Write

\[
d=\kappa(0),\qquad u=\kappa(1)=\kappa(4),\qquad v=\kappa(2)=\kappa(3).
\tag{2}
\]

In the natural residue order `(1,2,3,4)`, this is

\[
S=
\begin{pmatrix}
d&u&v&v\\
u&d&u&v\\
v&u&d&u\\
v&v&u&d
\end{pmatrix}.
\tag{3}
\]

The exact `p=5` local-factor image condition from `PL-421` is

\[
M:=S-\frac14\operatorname{Diag}(S)
=S-\frac d4 I_4\succeq0.
\tag{4}
\]

On the lag-stationary slice, reflection `a\mapsto-a mod 5` block-diagonalizes (4) into two explicit `2 x 2` blocks. If

\[
m=\frac{u+v}{2},\qquad f=u-v,
\tag{5}
\]

then (4) is equivalent to

\[
\boxed{\frac{3d}{4}-m\ge \frac{\sqrt5}{2}|f|}
\tag{6}
\]

and

\[
\boxed{\frac{3d}{4}+m\ge\frac12\sqrt{f^2+16m^2}}.
\tag{7}
\]

For nonzero variance scale `d>0`, let

\[
x=\frac md,\qquad y=\frac fd.
\tag{8}
\]

Then the exact feasible region is

\[
\boxed{-\frac14\le x\le\frac34,}
\tag{9}
\]

\[
\boxed{|y|\le\frac2{\sqrt5}\left(\frac34-x\right),}
\tag{10}
\]

and

\[
\boxed{y^2\le12\left(\frac34-x\right)\left(x+\frac14\right).}
\tag{11}
\]

Thus the lag-stationary cross-section of the full `PL-438` Schur cone is an explicit compact wedge–ellipse intersection in the normalized `(x,y)` plane. Under the same stationarity assumption, the `PL-440` reflection coordinate vanishes and its surviving signed probe is exactly

\[
\Delta_f=8f=8dy.
\tag{12}
\]

The arithmetic target is therefore sharper than merely asking whether the quadratic-character lag projection is small: its size has an exact admissible budget determined simultaneously by the diagonal variance `d` and the mean nonzero-lag correlation `m`.

No prime asymptotic, RH implication, or claim of new general matrix theory is contained in (1)--(12).

## 1. Reflection block decomposition

Let

\[
e_+=\frac{\delta_1+\delta_4}{\sqrt2},\qquad
f_+=\frac{\delta_2+\delta_3}{\sqrt2},
\tag{13}
\]

and

\[
e_-=\frac{\delta_1-\delta_4}{\sqrt2},\qquad
f_-=\frac{\delta_2-\delta_3}{\sqrt2}.
\tag{14}
\]

These are orthonormal bases for the even and odd subspaces under residue reflection. Applying them to (4) gives exactly

\[
M_+=
\begin{pmatrix}
\frac{3d}{4}+v & u+v\\
u+v & \frac{3d}{4}+u
\end{pmatrix},
\tag{15}
\]

and

\[
M_-=
\begin{pmatrix}
\frac{3d}{4}-v & u-v\\
u-v & \frac{3d}{4}-u
\end{pmatrix}.
\tag{16}
\]

Hence the four eigenvalues of `M` are

\[
\lambda_{-,\pm}
=\frac{3d}{4}-m\pm\frac{\sqrt5}{2}|f|,
\tag{17}
\]

and

\[
\lambda_{+,\pm}
=\frac{3d}{4}+m
\pm\frac12\sqrt{f^2+16m^2}.
\tag{18}
\]

Positivity of the smaller eigenvalue in each block gives (6)--(7). No approximation enters this reduction.

## 2. Normalized feasible lens

From (6),

\[
x\le\frac34,
\qquad
|y|\le\frac2{\sqrt5}\left(\frac34-x\right).
\tag{19}
\]

From (7), the left side must be nonnegative. Squaring then gives

\[
4\left(\frac34+x\right)^2\ge y^2+16x^2,
\tag{20}
\]

or equivalently

\[
y^2\le12\left(\frac34-x\right)\left(x+\frac14\right).
\tag{21}
\]

The right side of (21) is nonnegative only for

\[
-\frac14\le x\le\frac34,
\tag{22}
\]

which subsumes the sign requirement used before squaring. Equations (19), (21), and (22) therefore give the exact gate, with no extraneous branch introduced by squaring.

On the reflection-neutral axis `f=0`, the entire condition collapses to the interval

\[
\boxed{-\frac14\le\frac md\le\frac34.}
\tag{23}
\]

This immediately gives two useful endpoint controls. A raw rank-one/common-mode covariance has `u=v=d`, hence `m/d=1`, and fails the gate, matching the obstruction in `PL-422`. By contrast, exact isotropic common-mode centering in four coordinates has `u=v=-d/3`, hence `m/d=-1/3`, and also fails the gate, matching the over-centering obstruction isolated in `PL-423`.

Thus even on the maximally symmetric slice the dephasing condition does not reward either extreme. It requires an intermediate correlation window, and any nonzero oriented mode `f` consumes part of that window according to the exact linear and quadratic budgets (10)--(11).

## 3. Relation to the `PL-440` signed probe

`PL-440` showed that, after zero-extension to `Z/5Z`, the stationary part of the two orientation probes splits as

\[
\Delta_s^{\rm stat}=0,
\qquad
\Delta_f^{\rm stat}=8\bigl(\kappa(1)-\kappa(2)\bigr).
\tag{24}
\]

With (2) and (5), this is simply

\[
s=0,
\qquad
\Delta_f=8f.
\tag{25}
\]

The present calculation therefore closes the finite-dimensional algebraic loop between the lag-character projection and the local-factor positivity cone. Under exact lag stationarity, the full `p=5` gate is determined by three real numbers `(d,m,f)`, not by a generic covariance matrix, and the unresolved signed probe is the same scalar `f` appearing in the reflection-odd eigenvalue gap (17).

This is stronger than a statement of the form `f` should be small. For example, when `m/d` approaches the upper endpoint `3/4`, (10) forces `f/d` to zero linearly; near either endpoint of the ellipse (11), the permitted `f/d` also collapses. Conversely, in the interior there is a strictly positive stability margin, so exact cancellation of the quadratic-character channel is not required.

## 4. Stability under approximate stationarity

The exact lag-stationary hypothesis is stronger than what is presently known for the prime source. However, the image gate is stable in operator norm away from its boundary.

Let

\[
\Phi(A)=A-\frac14\operatorname{Diag}(A)
\tag{26}
\]

and decompose an actual Hermitian covariance as

\[
S=S_{\rm stat}+E,
\tag{27}
\]

where `S_stat` has the form (3). Since

\[
\|\operatorname{Diag}(E)\|_{\rm op}
=\max_i|E_{ii}|
\le\|E\|_{\rm op},
\tag{28}
\]

one has

\[
\boxed{\|\Phi(E)\|_{\rm op}\le\frac54\|E\|_{\rm op}.}
\tag{29}
\]

If

\[
\eta:=\lambda_{\min}(\Phi(S_{\rm stat}))>0
\tag{30}
\]

and

\[
\|E\|_{\rm op}<\frac45\eta,
\tag{31}
\]

then Weyl's inequality implies

\[
\lambda_{\min}(\Phi(S))>0.
\tag{32}
\]

The same estimate is two-sided as an obstruction: if the stationary model has `lambda_min(Phi(S_stat))<=-eta` and (31) holds, then the actual covariance still fails the gate.

Therefore an approximate-stationarity program has a concrete quantitative target. It is enough to place the stationary triple `(d,m,f)` inside the wedge–ellipse with a margin and control the anisotropic remainder in operator norm below `4/5` of that margin. Conversely, a stationary approximation lying outside by a robust spectral margin cannot be repaired by a smaller anisotropic perturbation.

## 5. Prior-art and adversarial audit

The reflection decomposition itself is classical finite-dimensional linear algebra: real symmetric matrices commuting with a reflection, and centrosymmetric matrices more generally, split into even and odd blocks. Likewise, diagonalizing circulant or lag-stationary kernels by finite Fourier methods is standard. No novelty claim is made for those facts, for the `2 x 2` eigenvalue formula, or for Weyl stability.

The line-specific content is narrower: equations (6)--(12) give the exact lag-stationary cross-section of the `PL-421` dephasing image cone and identify its unique oriented coordinate with the already-derived `PL-440` quadratic-lag signed probe. Searches across centrosymmetric-matrix theory, finite cyclic stationary covariance, prime short-interval covariance, fixed-modulus Dirichlet-character variance, and singular-series covariance did not locate this specific dephasing specialization or an arithmetic theorem that supplies the required covariance-scale bounds.

The external arithmetic literature therefore remains calibration rather than proof support. In particular, function-field variance analogues, Selberg-integral estimates in progressions, almost-all short-interval results, and averaged singular-series cancellation do not establish (1) for the canonical prime source and cannot be substituted for control of the anisotropic error `E` in (27).

## 6. Boundaries and falsification conditions

1. **Lag stationarity is a hypothesis, not an inherited symmetry.** The reduced set `U_5` is not closed under additive translation, and the zero-at-residue-0 extension used in `PL-440` is bookkeeping. The local prime `5`, interval boundaries, and source centering can all create start-residue dependence.

2. **`s=0` does not imply stationarity.** Vanishing of the reflection/start-residue probe removes one scalar anisotropy channel only. A nonstationary covariance can have `s=0` while remaining far from the three-parameter form (3).

3. **The quadratic-character identification is algebraic, not a cancellation theorem.** Equation (25) tells which mode survives the stationary projection. It gives no bound on `f/d` at the variance scale.

4. **A good scalar fit is insufficient.** To transfer positivity from the stationary model to the actual covariance through (29)--(32), the anisotropic remainder must be small in operator norm, not merely in one signed probe or entrywise on average.

5. **The critical test is quantitative.** If computations or arithmetic estimates place `(x,y)` robustly outside (9)--(11), or if the anisotropic operator norm is comparable to the stationary gate margin, this stationary reduction cannot establish the local-factor condition.

6. **No RH consequence follows from the reduction alone.** The result only sharpens one accepted local positivity target inside the existing line. The unresolved step remains to derive the needed covariance geometry from the actual arithmetic source without importing RH-strength cancellation.

## Consequence for the line

The immediate arithmetic target can now be phrased without a generic `4 x 4` covariance. First estimate the best lag-stationary approximation to the canonical reduced-residue covariance and its normalized coordinates

\[
\left(\frac md,\frac fd\right).
\tag{33}
\]

Then compare them directly with the exact wedge–ellipse (9)--(11), while bounding the nonstationary remainder in operator norm at the same covariance scale. This separates two falsifiable questions: whether the stationary component itself lies in the dephasing image cone, and whether the actual prime source is close enough to that component for positivity to survive.

That is a strictly narrower theorem surface than bounding `Delta_f` alone. It also explains why both the raw common-mode model and the perfectly isotropic centered model fail: the viable stationary geometry, if it exists arithmetically, must occupy the intermediate reflection lens rather than either symmetric extreme.
