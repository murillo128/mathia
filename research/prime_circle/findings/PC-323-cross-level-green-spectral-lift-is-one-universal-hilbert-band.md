# PC-323 — cross-level Green spectral lift is one universal Hilbert band

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most direct self-adjoint operator lift left open by PC-322.

PC-322 shows that the canonical downstream Green slice of the PC-316 cross-level field is the bilinear kernel

\[
X_{a,b}(k,l)=\frac{a(k)b(l)}{k+l},\qquad k,l\ge1,
\tag{1}
\]

with periodic Prime-Circle source sequences `a` and `b`. Scalar evaluation of this kernel gives the Mordell–Tornheim packet at `u=1`, but PC-322 deliberately leaves open the possibility that one should retain the full operator before taking a matrix coefficient or determinant.

The most direct such lift can be classified exactly. After grouping indices by a common period, `X_{a,b}` is a trace-class perturbation of a rank-one finite channel tensored with the classical Hilbert matrix. Its canonical self-adjoint dilation therefore has exactly one positive and one negative Hilbert absolutely-continuous branch. All detailed periodic source arithmetic lies in the trace-class defect; the essential and absolutely-continuous spectral core depends only on the two source RMS norms. For the canonical `(5,7)` packet this gives the universal band `[-pi sqrt(2/7), pi sqrt(2/7)]`.

Thus promoting the canonical Green kernel to an operator before scalarization does retain more information than the single matrix coefficient, but it does **not** produce a new Prime-Circle continuous spectral core. It also blocks an ordinary absolute Fredholm-determinant route: the operator is noncompact. The natural surviving spectral object is instead a determinant or scattering invariant **relative to** the universal Hilbert core.

## 1. Canonical self-adjoint lift of the cross-level Green kernel

Let `a` and `b` be bounded periodic sequences of periods `q` and `r`, respectively, and set

\[
(X_{a,b}x)_k
=\sum_{l\ge1}\frac{a(k)b(l)}{k+l}x_l.
\tag{2}
\]

Equivalently,

\[
X_{a,b}=D_a K_1D_b,
\qquad
(K_1)_{kl}=\frac1{k+l},
\tag{3}
\]

where `D_a,D_b` are bounded diagonal multipliers. Since `K_1` is bounded on `ell^2` by PC-322, so is `X_{a,b}`.

The canonical self-adjoint realization that preserves the full cross-level coupling is the dilation

\[
\boxed{
G_{a,b}=
\begin{pmatrix}
0&X_{a,b}\\
X_{a,b}^*&0
\end{pmatrix}
}
\tag{4}
\]

on `ell^2(N) direct-sum ell^2(N)`. This is source-forced by (1): no extra spectral parameter, fitted potential, or arbitrary diagonal wrapper has been introduced.

## 2. Exact residue decomposition leaves a rank-one Hilbert core

Put

\[
L=\operatorname{lcm}(q,r)
\tag{5}
\]

and regard both sequences as `L`-periodic. Write

\[
k=Lm+\rho,\qquad l=Ln+\sigma,
\qquad 1\le\rho,\sigma\le L,
\quad m,n\ge0.
\tag{6}
\]

Under the corresponding unitary identification

\[
\ell^2(\mathbb N)\cong
\bigoplus_{\rho=1}^{L}\ell^2(\mathbb N_0),
\tag{7}
\]

the `(rho,sigma)` block of `X_{a,b}` is exactly

\[
(X_{a,b})_{\rho\sigma}
=\frac{a_\rho b_\sigma}{L}
H_{(\rho+\sigma)/L},
\qquad
(H_\alpha)_{mn}=\frac1{m+n+\alpha}.
\tag{8}
\]

Every `alpha=(rho+sigma)/L` is positive. Moreover

\[
H_\alpha-H_1\in\mathcal S_1.
\tag{9}
\]

For completeness, this trace-class statement has a direct rank-one integral proof. With

\[
v_x=(1,x,x^2,\ldots),\qquad 0<x<1,
\tag{10}
\]

one has

\[
H_\alpha-H_1
=\int_0^1\bigl(x^{\alpha-1}-1\bigr)v_xv_x^*\,dx.
\tag{11}
\]

The trace norm is bounded by

\[
\int_0^1
\frac{|x^{\alpha-1}-1|}{1-x^2}\,dx<\infty.
\tag{12}
\]

Near `x=1` the numerator vanishes linearly, and near `x=0` integrability follows from `alpha>0`. Hence the Bochner integral in (11) is trace class.

Since there are only finitely many residue blocks, (8) gives the exact decomposition

\[
\boxed{
X_{a,b}=A_{a,b}\otimes H_1+S,
\qquad S\in\mathcal S_1,
}
\tag{13}
\]

where

\[
A_{a,b}=\frac1L\,a_L b_L^{\mathsf T},
\qquad
a_L=(a_1,\ldots,a_L)^{\mathsf T},
\quad
b_L=(b_1,\ldots,b_L)^{\mathsf T}.
\tag{14}
\]

Thus the finite channel matrix forced by the **two-source cross-level kernel** is not an arbitrary residue matrix: it is rank one.

Its unique nonzero singular value is

\[
\boxed{
c_{a,b}
=\frac{\|a_L\|_2\|b_L\|_2}{L}
=\sqrt{\mu_a\mu_b},
}
\tag{15}
\]

with

\[
\mu_a=\frac1L\sum_{\rho=1}^{L}|a_\rho|^2,
\qquad
\mu_b=\frac1L\sum_{\sigma=1}^{L}|b_\sigma|^2.
\tag{16}
\]

All dependence on the detailed periodic phases and residue pattern has therefore left the leading Hilbert channel and entered the trace-class remainder `S`.

## 3. The self-adjoint spectrum has one universal Hilbert band

Let

\[
G_0=
\begin{pmatrix}
0&A_{a,b}\otimes H_1\\
A_{a,b}^*\otimes H_1&0
\end{pmatrix}.
\tag{17}
\]

By (13),

\[
G_{a,b}-G_0\in\mathcal S_1.
\tag{18}
\]

The finite self-adjoint dilation

\[
\begin{pmatrix}
0&A_{a,b}\\A_{a,b}^*&0
\end{pmatrix}
\tag{19}
\]

has exactly two nonzero eigenvalues, `+c_{a,b}` and `-c_{a,b}`. The remaining finite channels are zero. Magnus and Rosenblum give the classical Hilbert matrix `H_1` purely absolutely-continuous spectrum `[0,pi]` with multiplicity one. Therefore `G_0` has one positive and one negative Hilbert branch,

\[
[0,\pi c_{a,b}]
\quad\text{and}\quad
[-\pi c_{a,b},0],
\tag{20}
\]

with absolutely-continuous multiplicity one away from zero; the zero finite channels also give an infinite-dimensional zero subspace for `G_0` when `L>1`.

Now (18) makes the standard compact/trace-class perturbation theorems decisive. Weyl invariance of essential spectrum and Kato–Rosenblum invariance of the absolutely-continuous part give

\[
\boxed{
\sigma_{\rm ess}(G_{a,b})
=[-\pi c_{a,b},\pi c_{a,b}],
}
\tag{21}
\]

and the absolutely-continuous part of `G_{a,b}` is unitarily equivalent to the two nonzero Hilbert branches of `G_0`. In particular its multiplicity is one almost everywhere on each of

\[
(-\pi c_{a,b},0),
\qquad
(0,\pi c_{a,b}).
\tag{22}
\]

Equation (21) does **not** classify the complete spectrum. The trace-class defect can carry discrete eigenvalues outside the band and can affect singular spectral data. The exact statement is that the essential and absolutely-continuous core is universal up to the single scale `c_{a,b}`.

## 4. Canonical `(5,7)` consequence and matched control

For the canonical sources used in PC-316--PC-322, PC-322 computes

\[
\mu_{a_5}=\frac45,
\qquad
\mu_{b_7}=\frac5{14}.
\tag{23}
\]

Hence

\[
\boxed{
c_{5,7}=\sqrt{\frac27}}
\tag{24}
\]

and the full self-adjoint Green lift has

\[
\boxed{
\sigma_{\rm ess}(G_{5,7})
=
\left[-\pi\sqrt{\frac27},
\pi\sqrt{\frac27}\right].
}
\tag{25}
\]

This spectral band does not see the detailed Prime-Circle source geometry. Any pair of non-arithmetic periodic controls with the same two RMS means `(4/5,5/14)` has the same `c` and therefore the same essential and absolutely-continuous spectrum. Detailed source arithmetic survives only in the trace-class relative perturbation.

This is stronger than the scalar matched-control observation of PC-322: even after retaining the full two-dimensional cross-level Green operator, the continuous spectral core is fixed by a single elementary norm product.

## 5. Absolute determinant route is blocked; a relative determinant survives

Because `c_{a,b}>0` for nonzero sources, (21) contains a nontrivial essential interval. Thus `G_{a,b}` is noncompact and in particular

\[
G_{a,b}\notin\mathcal S_p
\qquad\text{for every finite }p.
\tag{26}
\]

Consequently the standard absolute Fredholm determinant `det(I-zG_{a,b})` is not available, nor are the usual Schatten regularized determinants `det_p(I-zG_{a,b})`. An absolute determinant of this canonical operator would require an additional noncanonical renormalization and cannot be treated as source-forced evidence by itself.

There is, however, a canonical narrower possibility. Since `G_{a,b}-G_0` is trace class, for spectral parameters `z` outside the spectrum of `G_0` the relative perturbation

\[
(G_{a,b}-G_0)(G_0-z)^{-1}
\tag{27}
\]

is trace class, so the relative perturbation determinant

\[
\boxed{
\Delta_{a,b}(z)
=
\det\!\left(
I+(G_{a,b}-G_0)(G_0-z)^{-1}
\right)
}
\tag{28}
\]

is well-defined there. Equation (28), or equivalent relative scattering/spectral-shift data, is therefore the operator-theoretic information that can still depend nontrivially on the Prime-Circle residue pattern after the universal Hilbert channel has been removed.

No claim is made here that this relative determinant has a zeta divisor, a functional equation, or critical-line control. The result only identifies it as the first determinant-like object in this Green-operator branch that is not already forced by the universal continuous core.

## 6. Prior art and no-churn boundary

The load-bearing operator facts are classical and already anchored in `research/prime_circle/SOURCES.md`: Magnus and Rosenblum for the Hilbert matrix spectrum, together with the generalized-Hilbert reduction used in PC-075. The trace-class stability statement is the standard Kato–Rosenblum theorem; PC-075 already uses the same theorem for finite Hilbert channels. Directed prior-art search around periodically weighted/generalized Hilbert and Hankel operators returns this classical spectral framework rather than a distinct Prime-Circle mechanism. No novelty is claimed for Hilbert spectral theory, trace-class perturbation theory, or self-adjoint dilation.

The durable line-local content is the exact specialization forced by the PC-316/PC-322 cross-level Green kernel: its two periodic source masks produce the separable residue matrix (14), hence **one** Hilbert singular channel, and the entire detailed source pattern is trace-class relative to that channel. This differs from PC-075, where a one-index cyclotomic Hankel numerator produces a finite channel matrix with several arithmetic modes. Here the genuinely cross-level separability `a(k)b(l)` collapses the leading channel matrix to rank one.

Accordingly this finding closes the direct implication

\[
\text{retain the full canonical }u=1\text{ Green operator}
\longrightarrow
\text{new Prime-Circle continuous spectrum or absolute determinant}
\longrightarrow
\text{RH mechanism}.
\tag{29}
\]

It does **not** rule out discrete eigenvalues of `G_{a,b}`, singular relative data, the relative determinant (28), source-forced operators not reducible to the Green kernel (1), or genuinely cross-level nonlinear constructions whose residue channel is not separable rank one. Those are materially different questions and should not be classified by this result without a new derivation.

## Audit tests

The claim fails if any of the following fails: residue grouping must give exactly (8); the integral estimate (12) must put every generalized-Hilbert offset in the same trace-class class as `H_1`; the finite residue matrix in (14) must be rank one; its singular value must equal (15); the self-adjoint dilation must reduce to the signed Hilbert branches in (20); and a matched arbitrary periodic source with the same two RMS means must reproduce (21). The determinant conclusion requires only the nonzero essential interval and trace-class relative defect. Passing these checks establishes the operator classicalization and relative-determinant boundary above, not a theorem about Riemann zeros.