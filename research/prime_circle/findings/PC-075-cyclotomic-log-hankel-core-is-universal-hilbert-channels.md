# PC-075 — the cyclotomic-log Hardy coupling has universal Hilbert channels

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `NEGATIVE/OBSTRUCTION` + `PRIOR-ART-REDIRECTION`. The exact prime-circle specialization and trace-class block reduction below are derived here. The Hilbert-matrix spectrum, trace-class stability of the absolutely continuous part, multichannel Hankel framework, and finite Fourier analysis of Ramanujan matrices lie in classical operator/harmonic-analysis territory. No theorem-level novelty is claimed for those general ingredients.

PC-037 ruled out shell-independent rotation-invariant linear forms because they diagonalize mode by mode. A natural way to escape that theorem is to use the **canonical interior/exterior Hardy split** of the logarithmic cyclotomic potential and retain its off-diagonal coupling. This produces a genuinely nonlocal Hankel operator: Fourier modes are mixed through their sum rather than evaluated independently. The escape is real at the operator level, but its noncompact spectral core still collapses exactly to finitely many copies of the classical Hilbert matrix.

For every `n>2`, the essential spectrum is the universal interval `[-pi,pi]`; the positive and negative absolutely continuous channels each have multiplicity `phi(n)/2`. Thus the bare single-level Hardy/Hankel lift does not create a zeta-zero spectrum or a critical-line mechanism. The arithmetic that can still matter is confined to finite channel multiplicities and a trace-class remainder, so relative/discrete spectral data are not ruled out.

## 1. Intrinsic operator: interior-to-exterior coupling of the boundary potential

For `n>1`, inside the unit disk choose

\[
F_n(z)=\Log\Phi_n(z),\qquad F_n(0)=0.
\]

The exact Ramanujan expansion already used throughout the line is

\[
F_n(z)=-\sum_{m\ge1}\frac{c_n(m)}{m}z^m,
\qquad |z|<1,
\]

where `c_n(m)` is the Ramanujan sum of the primitive `n`-th roots. Its real boundary value, interpreted radially in `L^2`, is the logarithmic potential

\[
u_n(e^{it})=\log|\Phi_n(e^{it})|
=-\frac12\sum_{m\ge1}\frac{c_n(m)}{m}
\left(e^{imt}+e^{-imt}\right).
\]

The logarithmic singularities occur exactly at the primitive vertices. They are locally square-integrable.

Let

\[
L^2(S^1)=H^2_+\oplus H^2_-
\]

be the canonical Hardy interior/exterior decomposition, with

\[
H^2_+=\overline{\operatorname{span}}\{e^{ikt}:k\ge0\},
\qquad
H^2_-=\overline{\operatorname{span}}\{e^{-i(j+1)t}:j\ge0\}.
\]

On analytic trigonometric polynomials define the off-diagonal multiplication form

\[
\Gamma_n:=2P_-M_{u_n}P_+,
\]

and identify the standard bases of `H^2_+` and `H^2_-` with `ell^2(Z_{>=0})`. Its matrix is then exactly

\[
\boxed{
(\Gamma_n)_{jk}
=-\frac{c_n(j+k+1)}{j+k+1},
\qquad j,k\ge0.
}
\]

The formula itself will prove that this form extends to a bounded self-adjoint operator after the natural basis identification. Unlike PC-037, this operator is not diagonal in angular frequency: entry `(j,k)` couples an interior mode `k` to an exterior mode `-(j+1)` through the combined frequency `j+k+1`. It therefore genuinely retains information discarded by scalar or modewise evaluation.

The use of the Hardy split is not an arbitrary spectral parameterization: it is the canonical analytic interior/exterior decomposition already present in harmonic inversion on the circle. What is not forced is the decision to study this particular off-diagonal multiplication block, so the result below is a classification of a natural branch, not a no-go for all nonlocal operators.

## 2. Exact residue-class decomposition

Separate indices modulo `n`. Define the unitary

\[
W:\ell^2(\mathbb Z_{\ge0})
\longrightarrow
\bigoplus_{r=0}^{n-1}\ell^2(\mathbb Z_{\ge0}),
\qquad
(Wx)_r(a)=x_{na+r}.
\]

If `j=na+r` and `k=nb+s`, then periodicity of Ramanujan sums gives

\[
c_n(j+k+1)=c_n(r+s+1),
\]

while

\[
j+k+1=n\left(a+b+\frac{r+s+1}{n}\right).
\]

Hence the `(r,s)` block is

\[
\boxed{
(W\Gamma_nW^*)_{rs}
=-\frac{c_n(r+s+1)}{n}H_{\alpha_{rs}},
\qquad
\alpha_{rs}=\frac{r+s+1}{n},
}
\]

where

\[
(H_\alpha)_{ab}=\frac1{a+b+\alpha},
\qquad a,b\ge0.
\]

Thus the full infinite-dimensional problem has already reduced to an `n x n` matrix of generalized Hilbert operators.

## 3. Every generalized block differs from the same Hilbert matrix by trace class

Let

\[
H:=H_1=\left(\frac1{a+b+1}\right)_{a,b\ge0}
\]

be the classical Hilbert matrix. For every `alpha>0`,

\[
(H_\alpha-H)_{ab}
=
\int_0^1x^{a+b}\bigl(x^{\alpha-1}-1\bigr)\,dx.
\]

If `0<alpha<1`, this is a positive moment matrix; if `alpha>1`, its negative is positive. In either case its trace norm is finite because

\[
\sum_{a\ge0}
\left|
\frac1{2a+\alpha}-\frac1{2a+1}
\right|<\infty,
\]

with summand `O(a^{-2})`. Therefore

\[
\boxed{H_\alpha-H\in\mathcal S_1\quad(\alpha>0).}
\]

There are only `n^2` residue blocks. Define the finite real symmetric matrix

\[
C_n=\bigl(c_n(r+s+1)\bigr)_{0\le r,s<n}.
\]

Replacing every `H_{alpha_rs}` by `H` consequently gives the exact trace-class reduction

\[
\boxed{
W\Gamma_nW^*
=-\frac1n C_n\otimes H+T_n,
\qquad T_n\in\mathcal S_1.
}
\]

This also proves boundedness of the original Hardy-coupling form.

## 4. The finite Ramanujan channel matrix has only `+n`, `-n`, and `0`

Let

\[
\omega=e^{2\pi i/n},
\qquad
e_k(r)=n^{-1/2}\omega^{kr},
\qquad 0\le k<n.
\]

Using

\[
c_n(t)=\sum_{u\in(\mathbb Z/n\mathbb Z)^\times}\omega^{ut},
\]

one obtains directly

\[
\begin{aligned}
(C_ne_k)(r)
&=\frac1{\sqrt n}
\sum_{s=0}^{n-1}\sum_{u\in U(n)}
\omega^{u(r+s+1)}\omega^{ks}\\
&=n\,\mathbf 1_{(k,n)=1}\,\omega^{-k}e_{-k}(r).
\end{aligned}
\]

Therefore

\[
\boxed{
C_n^2e_k=
\begin{cases}
n^2e_k,&(k,n)=1,\\
0,&(k,n)>1.
\end{cases}}
\]

For `n>2`, no unit residue is fixed by `k -> -k`, so the unit Fourier modes pair into two-dimensional blocks. Consequently

\[
\boxed{
\operatorname{spec}(C_n/n)
=
\{+1^{(\varphi(n)/2)},
-1^{(\varphi(n)/2)},
0^{(n-\varphi(n))}\},
\qquad n>2.
}
\]

For `n=2`, `spec(C_2/2)={-1,0}`.

This finite Fourier calculation is closely adjacent to classical Ramanujan-sum matrix theory. In particular, Ushiroya studies spectra of finite matrices built from `c_q(m-n)` and related Ramanujan-sum combinations. The reversal/Hankel indexing here changes the matrix presentation but not the fact that the primitive Fourier support is classical finite-group harmonic analysis.

## 5. Universal essential and absolutely continuous spectrum

Magnus proved that the classical Hilbert matrix has spectrum `[0,pi]` and no eigenvalues; Rosenblum's diagonalization identifies its continuous spectrum as multiplicity-one absolutely continuous spectrum. Modern Hilbert-matrix treatments reproduce the same result.

The model operator

\[
M_n:=-\frac1nC_n\otimes H
\]

therefore consists, for `n>2`, of

- `phi(n)/2` copies of `+H`,
- `phi(n)/2` copies of `-H`, and
- `n-phi(n)` zero channels.

Because `Gamma_n-M_n` is trace class, Weyl stability gives identical essential spectra, while the Kato-Rosenblum theorem makes their absolutely continuous parts unitarily equivalent. Hence

\[
\boxed{
\sigma_{\rm ess}(\Gamma_n)=[-\pi,\pi],
\qquad n>2,
}
\]

and, away from the zero threshold,

\[
\boxed{
\operatorname{mult}_{\rm ac}(\lambda;\Gamma_n)
=\frac{\varphi(n)}2,
\qquad
\lambda\in(-\pi,0)\cup(0,\pi).
}
\]

For `n=2`,

\[
\boxed{\sigma_{\rm ess}(\Gamma_2)=[0,\pi],}
\]

with one positive absolutely continuous channel. This special case is also visible directly from

\[
(\Gamma_2)_{jk}=\frac{(-1)^{j+k}}{j+k+1},
\]

which is a diagonal-unitary conjugate of `H`.

Trace-class perturbation alone does **not** rule out isolated eigenvalues or other relative spectral information carried by `T_n`; no claim is made here that the complete point spectrum is universal. The exact statement is about the noncompact/absolutely-continuous core.

## 6. Prior-art and novelty audit

The closest operator-theoretic neighborhood is classical.

1. Wilhelm Magnus, *On the Spectrum of Hilbert's Matrix* (1950), gives the classical `[0,pi]` Hilbert spectrum and absence of eigenvalues. Rosenblum's 1958 papers give an explicit spectral representation and multiplicity-one continuous/absolutely-continuous description.
2. Pushnitski and Yafaev's multichannel theory for self-adjoint Hankel operators with piecewise-continuous symbols makes the general phenomenon explicit: jumps produce independently propagating absolutely continuous bands, with explicit model Hankel operators and asymptotically complete wave operators. The finite oscillatory `1/m` channels occurring here sit squarely next to that theory.
3. Ushiroya's work on matrices of Ramanujan sums confirms that finite Fourier spectral analysis of Ramanujan-sum matrices is established territory.
4. Brevig, Perfekt, Seip, Siskakis and Vukotic's multiplicative Hilbert matrix is a particularly important RH-adjacent warning: a natural Hankel/Hilbert operator built directly from a zeta reproducing kernel already has the classical continuous band `[0,pi]`. Thus neither a Hilbert band nor the coexistence of Hankel structure and zeta arithmetic is by itself a new RH mechanism.

A directed search for periodic/oscillatory Hilbert matrices, root-of-unity Hankel operators, Ramanujan-sum Hankel matrices, and piecewise-continuous Hankel spectra found the surrounding ingredients and multichannel mechanism in established operator theory. I did not find this exact `c_n(j+k+1)/(j+k+1)` prime-circle specialization stated as such, but absence of that wording is not a novelty claim.

The durable contribution is the exact **classification inside this research object**: the canonical Hardy interior/exterior coupling of the full cyclotomic logarithmic potential is not a hidden Hilbert-Pólya operator. Its extensive spectral core is universal Hilbert scattering data, with only a totient channel count surviving at leading spectral type.

## 7. Why this does not produce the critical line

The result is stronger than saying that a scalar transform recovers a known Dirichlet series. `Gamma_n` is a genuine infinite-dimensional, nonlocal, mode-mixing operator. Nevertheless its essential spectrum is a fixed compact real interval independent of the detailed arithmetic of `n`; `n` changes only the finite multiplicity `phi(n)/2` of the two open half-bands.

There is no intrinsic complex parameter `s`, no distinguished `Re(s)=1/2`, no gamma factor, no `s <-> 1-s` functional equation, and no discrete compact-resolvent spectrum that could be identified with the ordinates of Riemann zeros. Adding such structure to the universal Hilbert core would therefore require genuinely new input.

This also shows why the route is different from PC-037 but ultimately suffers another universality collapse:

\[
\text{cyclotomic log field}
\to
\text{Hardy interior/exterior coupling}
\to
\text{Hankel mode mixing}
\to
\text{universal Hilbert channels modulo }\mathcal S_1.
\]

The first two arrows preserve nonlocal information that PC-037 intentionally excluded; the last arrow is the new obstruction.

## 8. Boundary of the obstruction

This finding does **not** close several materially different routes.

- The trace-class remainder `T_n` contains the exact residue offsets `alpha_rs=(r+s+1)/n` and Ramanujan coefficients. Relative determinants, isolated eigenvalues, threshold behavior, or other trace-class invariants could still carry arithmetic. They require a separate analysis rather than being inferred from the universal essential spectrum.
- Cross-level operators coupling different `n` before the residue decomposition are not covered.
- Shell-dependent Hardy geometries or weights forced by refinement are not covered.
- Nonlinear operations on the Hankel blocks are not covered.
- The extensive old/new cotangent coupling of PC-047 is a different operator and is not reduced by this result.
- The global nonlinear uniformization/monodromy branch rooted in PC-017 remains outside this linear Hardy analysis.

Conversely, merely taking the bare single-level cyclotomic Hankel operator and interpreting its continuous band as a new spectral avatar of RH is ruled out: the band is classical Hilbert data.

## 9. Audit and falsification surface

The exact reduction can be falsified at four concrete points.

1. **Hardy matrix coefficient:** direct Fourier projection must give
   `-(c_n(j+k+1))/(j+k+1)` after the stated factor-two normalization.
2. **Residue decomposition:** grouping indices modulo `n` must give the block
   `-(c_n(r+s+1)/n) H_{(r+s+1)/n}`.
3. **Trace class:** for every `alpha>0`, the diagonal trace sum of the signed positive moment difference `H_alpha-H_1` must converge.
4. **Finite spectrum:** discrete Fourier vectors must satisfy
   `C_n e_k = n 1_{(k,n)=1} omega^{-k} e_{-k}`.

Failure of any item invalidates the spectral conclusion. If all four hold, the essential-spectrum statement follows from standard Hilbert-matrix spectral theory and compact/trace-class perturbation theorems.

## Research consequence

A genuinely nonlocal operator that preserves the full logarithmic cyclotomic field has now been tested beyond the scalar/Fourier-diagonal regime. The result is negative at the leading spectral level:

\[
\boxed{
\text{the canonical single-shell Hardy/Hankel coupling has only universal Hilbert a.c. channels,}
}
\]

with arithmetic entering that core only through `phi(n)` multiplicity. Any viable Prime-Circle spectral mechanism must therefore live in **relative/trace-class data, cross-level structure, shell-dependent/nonlinear operators, or genuinely different global geometry**, rather than in the bare Hankel band's essential spectrum.