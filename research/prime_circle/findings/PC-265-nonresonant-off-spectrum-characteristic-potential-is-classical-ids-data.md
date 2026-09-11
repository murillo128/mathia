# PC-265 — nonresonant off-spectrum characteristic potential is classical IDS data

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the off-spectrum shifted-determinant/resolvent channel left open by PC-262--PC-264.

Let

\[
2<p_n<r_n<q_n,
\qquad
\frac{p_n}{q_n}\to\alpha,
\qquad
\frac{r_n}{q_n}\to\beta,
\qquad
0<\alpha<\beta<1,
\]

with `1,alpha,beta` linearly independent over `Q`, exactly as in PC-262--PC-264. Write

\[
\Delta_n=\frac{D_{p_n,r_n;q_n}}{q_n\sqrt{p_nr_n}}
\]

for the natively normalized shared-upper defect and form its self-adjoint symmetric dilation

\[
\mathscr H_n=
\begin{pmatrix}
0&\Delta_n\\
\Delta_n^T&0
\end{pmatrix}.
\tag{1}
\]

Let

\[
P_n(z)=\det(zI-\mathscr H_n).
\tag{2}
\]

PC-262 gives a deterministic nonresonant limit `nu_{alpha,beta}` for the empirical distribution of the squared singular values of `Delta_n`, while PC-264 gives

\[
\|\Delta_n\|\to\Lambda(\alpha,\beta).
\tag{3}
\]

Then the entire **off-spectrum normalized characteristic potential** is already fixed by those classical torus data. For every

\[
z\in\mathbb C\setminus[-\Lambda(\alpha,\beta),\Lambda(\alpha,\beta)],
\]

one has

\[
\boxed{
\frac{1}{p_n+r_n}\log|P_n(z)|
\longrightarrow
\mathcal F_{\alpha,\beta}(z)
}
\tag{4}
\]

locally uniformly off the limiting spectral interval, where

\[
\boxed{
\mathcal F_{\alpha,\beta}(z)
=
\frac{\beta-\alpha}{\alpha+\beta}\log|z|
+
\frac{\alpha}{\alpha+\beta}
\int
\log|z^2-x|\,d\nu_{\alpha,\beta}(x).
}
\tag{5}
\]

Likewise the normalized logarithmic derivative has the locally uniform limit

\[
\boxed{
\frac{1}{p_n+r_n}\frac{P_n'(z)}{P_n(z)}
\longrightarrow
\frac{\beta-\alpha}{\alpha+\beta}\frac1z
+
\frac{2\alpha z}{\alpha+\beta}
\int\frac{d\nu_{\alpha,\beta}(x)}{z^2-x}.
}
\tag{6}
\]

Thus every fixed complex shift that stays off the limiting spectrum, together with its normalized resolvent trace, is a deterministic transform of the same induced-torus integrated density of states. Admissible pairwise-coprime rational-partition controls with the same limiting ratios have the same limits. No independent prime-specific long-cocycle datum survives in this channel.

## 1. Exact finite characteristic factorization

Let

\[
\sigma_{n,1},\ldots,\sigma_{n,p_n}
\]

be all singular values of `Delta_n`, including zeros. Because `Delta_n` is `p_n x r_n` with `p_n<r_n`, the standard singular-value decomposition of the symmetric dilation gives the exact spectrum

\[
\operatorname{Spec}(\mathscr H_n)
=
\{\pm\sigma_{n,j}:1\le j\le p_n\}
\cup
\{0\}^{r_n-p_n}.
\tag{7}
\]

Consequently

\[
\boxed{
P_n(z)
=z^{r_n-p_n}
\prod_{j=1}^{p_n}
\bigl(z^2-\sigma_{n,j}^2\bigr).
}
\tag{8}
\]

This is an identity before any asymptotics or ergodic interpretation. If

\[
\nu_n=\frac1{p_n}
\sum_{j=1}^{p_n}\delta_{\sigma_{n,j}^2}
\tag{9}
\]

is PC-262's singular-square empirical measure, then for every `z` outside the finite spectrum,

\[
\frac{1}{p_n+r_n}\log|P_n(z)|
=
\frac{r_n-p_n}{p_n+r_n}\log|z|
+
\frac{p_n}{p_n+r_n}
\int\log|z^2-x|\,d\nu_n(x).
\tag{10}
\]

Differentiating the exact polynomial factorization gives

\[
\frac{1}{p_n+r_n}\frac{P_n'(z)}{P_n(z)}
=
\frac{r_n-p_n}{p_n+r_n}\frac1z
+
\frac{2p_nz}{p_n+r_n}
\int\frac{d\nu_n(x)}{z^2-x}.
\tag{11}
\]

Equation (11) is equivalently the normalized resolvent trace

\[
\frac1{p_n+r_n}
\operatorname{tr}(zI-\mathscr H_n)^{-1}.
\tag{12}
\]

Hence the shifted determinant and resolvent do not probe a hidden transfer state that was discarded by PC-262; off spectrum they are explicit transforms of the same finite empirical measure.

## 2. PC-262 and PC-264 give local uniform convergence

PC-262 proves

\[
\nu_n\Longrightarrow\nu_{\alpha,\beta},
\tag{13}
\]

and PC-264 proves (3). Fix a compact set

\[
K\subset
\mathbb C\setminus[-\Lambda(\alpha,\beta),\Lambda(\alpha,\beta)].
\]

Its distance from the limiting interval is positive. By (3), for all sufficiently large `n` the whole spectrum of `mathscr H_n` lies in a slightly larger real interval still separated from `K`. Therefore both kernels

\[
(z,x)\mapsto\log|z^2-x|
\]

and

\[
(z,x)\mapsto\frac{2z}{z^2-x}
\]

are uniformly bounded and uniformly continuous on the relevant compact product set. Weak convergence (13), together with

\[
\frac{p_n}{p_n+r_n}\to\frac{\alpha}{\alpha+\beta},
\qquad
\frac{r_n-p_n}{p_n+r_n}
\to\frac{\beta-\alpha}{\alpha+\beta},
\tag{14}
\]

then yields (4)--(6) uniformly on `K`.

Equivalently, define the empirical eigenvalue measure of the symmetric dilation by

\[
\mu_n
=\frac1{p_n+r_n}
\left[
(r_n-p_n)\delta_0
+
\sum_{j=1}^{p_n}
(\delta_{\sigma_{n,j}}+\delta_{-\sigma_{n,j}})
\right].
\tag{15}
\]

Then

\[
\mu_n\Longrightarrow
\mu_{\alpha,\beta}
=
\frac{\beta-\alpha}{\alpha+\beta}\delta_0
+
\frac{\alpha}{\alpha+\beta}
\left[
(\sqrt{\cdot})_\#\nu_{\alpha,\beta}
+(-\sqrt{\cdot})_\#\nu_{\alpha,\beta}
\right],
\tag{16}
\]

and (4) is simply the logarithmic potential of this deterministic limiting spectral measure,

\[
\mathcal F_{\alpha,\beta}(z)
=
\int\log|z-\lambda|\,d\mu_{\alpha,\beta}(\lambda).
\tag{17}
\]

Equation (6) is its Stieltjes/resolvent transform. No additional asymptotic input is available to the off-spectrum characteristic polynomial once (16) is fixed.

## 3. Matched controls give exactly the same characteristic potential

PC-262 proves that admissible pairwise-coprime rational-partition controls with the same irrational limiting ratios have the same limiting singular-square measure `nu_{alpha,beta}`. PC-264 proves that their top spectral edge has the same limit `Lambda(alpha,beta)`. The finite identities (8)--(12) use only the dimensions and singular values.

Therefore the controls have exactly the same limiting functions (5)--(6). In particular, no criterion based on any of the following can distinguish the prime-linked carrier from the matched nonprime carrier in this nonresonant regime:

- the exponential rate of `|det(zI-mathscr H_n)|` at any fixed off-spectrum complex shift;
- a finite collection or compact family of such off-spectrum shifts;
- the normalized trace of the resolvent or its derivatives away from the limiting spectrum;
- any analytic quantity obtained continuously from these limiting transforms.

The spectral parameter `z` is genuine for the finite characteristic polynomial, but the resulting off-spectrum complex dependence is ordinary logarithmic-potential/IDS structure. It does not create a source-forced analogue of the zeta functional equation, a critical-line normalization, or a new zero detector.

## 4. Prior-art and novelty audit

The abstract mechanism is classical. Passing from empirical spectral measures to logarithmic potentials and Stieltjes transforms is standard spectral/potential theory, and the relation between density of states, characteristic growth, and Lyapunov-type quantities is the setting of the classical Thouless framework. The deterministic-IDS literature already used in PC-262 and the multiplicative-ergodic boundary emphasized in PC-263 are the relevant prior-art neighborhood.

A targeted literature check around finite-volume determinants, integrated density of states, logarithmic potentials, Thouless formulas, and quasiperiodic Jacobi/Schrodinger cocycles found the expected established theory rather than a Prime-Circle-specific mechanism. No novelty is claimed for (17), Stieltjes transforms, finite-volume characteristic determinants, or Thouless-type logarithmic potentials.

The project-local content is narrower and exact: equations (8)--(11) show that the **specific shifted characteristic determinant explicitly left open after PC-262/PC-263 collapses off spectrum once PC-264 supplies control of the moving spectral edge**. This closes a named escape channel for the native Prime-Circle shared-upper carrier without importing a new operator.

The result must not be overread as a top-Lyapunov theorem. PC-257's fixed-width transfer recursion may be block-valued, singular, or projective in ways not covered by the scalar Jacobi Thouless identity. Equations (4)--(6) classify the determinant/logarithmic-potential and resolvent channels; they do not prove that every norm of a long transfer product is determined by `nu_{alpha,beta}`.

## 5. Strict surviving boundary

PC-263 already handles the singular zero-energy **positive pseudodeterminant** by exploiting its special exact factorization. PC-265 now handles every fixed shift separated from the limiting spectrum. The unresolved shifted-determinant region is therefore restricted to parameters entering or approaching the limiting spectrum, where `log|z-lambda|` is singular and microscopic eigenvalue placement can matter.

Accordingly the remaining nonresonant long-cocycle frontier is narrower:

- top Lyapunov or projective growth not reducible to the determinant/Lyapunov sum;
- rotation or winding data of the transfer recursion;
- fine eigenvalue spacing and subleading edge fluctuations;
- characteristic/determinant scaling when the spectral parameter approaches the limiting spectrum at an `n`-dependent rate;
- resonant limits, where PC-261 already shows that ratio-only universality fails.

Any proposed RH mechanism based on a fixed off-spectrum `z` is now ruled out at the native normalized level: it sees only the classical induced-torus spectral measure already shared by matched controls.

## 6. Falsification audit

The finding can fail only if one of the following concrete steps fails.

1. **Finite factorization:** exhibit a native `p x r` defect whose symmetric dilation violates (7)--(8).
2. **Bulk input:** produce a nonresonant sequence satisfying the PC-262 hypotheses for which `nu_n` has a different limit.
3. **Edge input:** violate PC-264 by producing spectral mass that remains a fixed distance outside `[-Lambda,Lambda]`.
4. **Transform convergence:** find a compact off-spectrum set on which the kernels in (10)--(11) fail to be uniformly separated from their singularities despite (3).
5. **Matched control:** construct a control with the same limiting ratios, `nu_{alpha,beta}`, and `Lambda(alpha,beta)` but a different limit in (4) or (6), contrary to the exact finite formulas.

Absent such a failure, the off-spectrum characteristic potential and normalized resolvent are not independent Prime-Circle invariants.