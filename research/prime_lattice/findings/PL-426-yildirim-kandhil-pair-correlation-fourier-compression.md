# PL-426 — Yıldırım–Kandhil mixed zero pair correlation is only a Fourier-diagonal compression

**Evidence/status:** `LITERATURE + EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-REPRESENTATION-OBSTRUCTION`.

**Parent findings:** `PL-415`, `PL-424`, `PL-425`.

## Claim

`PL-425` leaves a precise analytic target: transfer the near-character-diagonal mod-5 singular-series covariance to the actual deterministically source-subtracted prime covariance with enough **matrix-valued** control to preserve the `PL-421` lower spectral floor. The most directly relevant Dirichlet-`L` pair-correlation literature does contain mixed pairs of characters internally, but the quantity for which Yıldırım and, more recently, Kandhil--Languasco--Moree prove estimates is a lossy Fourier compression of that full mixed matrix.

Under the GRH convention used by Kandhil--Languasco--Moree, let

\[
G(x,T)=\bigl(G_{\chi,\psi}(x,T)\bigr)_{\chi,\psi\bmod5}
\tag{1}
\]

be their mixed zero-correlation matrix, where

\[
G_{\chi,\psi}(x,T)
=
\sum_{\substack{|\gamma_\chi|\le T\\|\gamma_\psi|\le T}}
 x^{i(\gamma_\chi-\gamma_\psi)}
 \frac{4}{4+(\gamma_\chi-\gamma_\psi)^2}.
\tag{2}
\]

For every reduced residue `a mod 5`, their global pair-correlation observable is

\[
F_5(x,T;a)
=
\sum_{\chi,\psi\bmod5}
\overline{\chi(a)}\psi(a)G_{\chi,\psi}(x,T).
\tag{3}
\]

Order the four reduced residues as `a_r=2^r mod 5` and the four characters as `chi_j(2)=exp(2 pi i j/4)`, and put

\[
W_{rj}:=\frac12\overline{\chi_j(a_r)}.
\tag{4}
\]

Then `W` is the unitary `C_4` Fourier matrix and (3) becomes the exact matrix identity

\[
\boxed{
F_5(x,T;a_r)
=4\,(WG(x,T)W^*)_{rr}.
}
\tag{5}
\]

Thus knowing `F_5(x,T;a)` for **every** reduced residue gives only the diagonal of the Fourier-conjugated matrix `WGW*`. Equivalently, if `rho` runs over the four characters and

\[
B_\rho(x,T)
:=\sum_{\chi\bmod5}G_{\chi,\chi\rho}(x,T),
\tag{6}
\]

then

\[
\boxed{
F_5(x,T;a)
=\sum_{\rho\bmod5}\rho(a)B_\rho(x,T).
}
\tag{7}
\]

Varying `a` recovers the four cyclic diagonal sums `B_rho`, not the sixteen matrix entries. This is exactly the kind of group-averaged/twirled information that `PL-424` showed cannot determine the local dephasing image-cone verdict.

The loss persists even after adding positivity, the natural conjugation symmetry of Dirichlet characters, and the four individual self-correlations `G_{chi,chi}`. There are explicit positive-semidefinite matched controls with identical values of all of those data but radically different mixed coherence. Therefore the published all-residue estimates for `F_5` do **not** supply the unsymmetrized mixed-character operator-norm estimate required by `PL-425`.

This is a representation obstruction, not a claim that the actual zero-correlation matrix has large off-diagonal entries. A stronger theorem controlling the individual `G_{chi,psi}`, or another tomographically complete family of quadratic forms, remains a viable route.

## 1. The literature object already contains the mixed matrix, then compresses it

Kandhil, Languasco and Moree define `G_{chi_1,chi_2}(x,T)` precisely to measure correlations between zeros of two Dirichlet `L`-functions. They then form, for each reduced residue `a`,

\[
F_q(x,T;a)
=
\sum_{\chi_1,\chi_2\bmod q}
\overline{\chi_1(a)}\chi_2(a)
G_{\chi_1,\chi_2}(x,T).
\tag{8}
\]

Their equation (7) gives the positive representation

\[
F_q(x,T;a)
=
\int_{-\infty}^{\infty}
|\Sigma(x,T,v;q,a)|^2e^{-2|v|}\,dv,
\tag{9}
\]

where

\[
\Sigma(x,T,v;q,a)
=
\sum_{\chi\bmod q}\overline{\chi(a)}
\sum_{|\gamma_\chi|\le T}x^{i\gamma_\chi}e^{iv\gamma_\chi}.
\tag{10}
\]

The same paper records Yıldırım's earlier upper-half-plane analogue `F_q^+` and his GRH asymptotic, uniform in every reduced residue `a`. Kandhil--Languasco--Moree prove, again under GRH, both uniform upper bounds for `F_q,F_q^+` and an asymptotic

\[
F_q(x,T;a)
\sim
\frac{\varphi(q)}{\pi}T\log x
\tag{11}
\]

in their Theorem 3 over the stated `q,x,T` range, uniformly for every reduced residue `a`.

Those are genuine mixed-zero results: the sum (8) contains all pairs `(chi_1,chi_2)`. But the theorem controls the **sum after projection onto one residue-character vector**, not the entries of the mixed matrix separately. At fixed `q=5`, uniformity in all `a` supplies four quadratic forms, not a `4 x 4` covariance matrix.

The primary modern source is Neelam Kandhil, Alessandro Languasco and Pieter Moree, “Pair correlation of zeros of Dirichlet L-functions: a possible path towards the conjectures of Chowla, Elliott-Halberstam and Montgomery,” *Mathematische Annalen* **394** (2026), Article 43, DOI `10.1007/s00208-026-03383-y`; the historical source is C. Yalcin Yıldırım, “The pair correlation of zeros of Dirichlet L-functions and primes in arithmetic progressions,” *Manuscripta Mathematica* **72** (1991), 325--334. Both are already registered as sources 107 and 105 in `research/prime_lattice/SOURCES.md`.

## 2. Exact Fourier compression at modulus 5

For `U_5=(Z/5Z)^times`, character orthogonality makes the matrix `W` in (4) unitary. Directly from (3),

\[
\begin{aligned}
(WGW^*)_{rr}
&=
\frac14
\sum_{j,k}
\overline{\chi_j(a_r)}
\chi_k(a_r)
G_{\chi_j,\chi_k}\\
&=\frac14F_5(x,T;a_r),
\end{aligned}
\tag{12}
\]

which proves (5).

There is another useful form of the same loss of information. In (3), put

\[
\rho=\psi\chi^{-1}.
\tag{13}
\]

Then

\[
\overline{\chi(a)}\psi(a)=\rho(a),
\tag{14}
\]

so regrouping the sixteen terms gives (6)--(7). Fourier inversion on `U_5` can therefore recover every `B_rho` from the four values `F_5(a)`, but each `B_rho` is only a **sum along one multiplicative diagonal of `G`**.

In particular, even exact knowledge of all four functions `a -> F_5(a)` leaves a twelve-complex-dimensional linear kernel before Hermitian constraints are imposed. Positivity shrinks the admissible set but does not restore injectivity, as the next section shows explicitly.

## 3. The zero-side matrix is positive, but positivity does not repair the compression

The kernel

\[
\omega(u)=\frac4{4+u^2}
\tag{15}
\]

has the Fourier representation used by Kandhil--Languasco--Moree,

\[
\omega(u)
=
\int_{-\infty}^{\infty}e^{ivu}e^{-2|v|}\,dv.
\tag{16}
\]

For each character define

\[
Z_\chi(v)
:=
\sum_{|\gamma_\chi|\le T}
 x^{i\gamma_\chi}e^{iv\gamma_\chi}.
\tag{17}
\]

Then (2) gives

\[
\boxed{
G_{\chi,\psi}(x,T)
=
\int Z_\chi(v)\overline{Z_\psi(v)}e^{-2|v|}\,dv,
}
\tag{18}
\]

so `G(x,T)` is a Hermitian positive-semidefinite Gram matrix. Equation (9) is simply (18) tested on the character vector `(̅chi(a))_chi`.

Nevertheless, the map

\[
G\longmapsto
\bigl((WGW^*)_{00},\ldots,(WGW^*)_{33}\bigr)
\tag{19}
\]

is not injective even on the PSD cone and even if `Diag(G)` is supplied separately. Reuse the biunimodular vector isolated in `PL-424`,

\[
v=(1,i,1,-i)^T,
\qquad
Wv=(1,1,1,-1)^T.
\tag{20}
\]

Set

\[
G_{\rm good}=I_4,
\qquad
G_{\rm bad}=vv^*.
\tag{21}
\]

Both are PSD and

\[
\operatorname{Diag}(G_{\rm good})
=
\operatorname{Diag}(G_{\rm bad})
=(1,1,1,1).
\tag{22}
\]

Moreover

\[
\operatorname{Diag}(WG_{\rm good}W^*)
=
\operatorname{Diag}(WG_{\rm bad}W^*)
=(1,1,1,1),
\tag{23}
\]

because every coordinate of `Wv` has modulus one. Hence both controls give

\[
\boxed{F_5(a)=4\quad\text{for every }a\in U_5}
\tag{24}
\]

and the same four character self-correlations, while `G_good` has rank four and `G_bad` has rank one with maximal off-diagonal coherence.

The example also respects the basic Dirichlet conjugation involution. With the character order `(chi_0,chi_1,chi_2,chi_3)` and `overline{chi_1}=chi_3`, one has

\[
v_0,v_2\in\mathbb R,
\qquad
v_3=\overline{v_1}.
\tag{25}
\]

Thus `G_bad` satisfies the corresponding conjugation/reversal symmetry, as does `I_4`. The ambiguity is not an artifact of allowing arbitrary non-Hermitian or conjugation-incompatible matrices.

This matched control is not asserted to arise from actual Dirichlet zero sets. Its role is information-theoretic: no implication from the data `(Diag(G), F_5(a):a in U_5)` to small unsymmetrized mixed coherence can follow from positivity, character orthogonality and conjugation symmetry alone.

## 4. Why this matters for the PL-425 transfer target

`PL-425` shows that Kuperberg's **singular-series model** is already character-diagonal up to square-root error. To transfer that structure to actual prime fluctuations through a zero-explicit-formula route, one would naturally seek estimates for mixed Dirichlet spectral channels. The Yıldırım--Kandhil observable is close enough to look like exactly the missing input, because it explicitly sums `G_{chi,psi}` over distinct characters.

Equations (5) and (19) show the mismatch. Published control of `F_5(a)` gives the diagonal of `WGW*`, which is the zero-side analogue of controlling a variance separately in each residue channel. It does not bound the off-diagonal entries of `G`, nor the off-diagonal entries of `WGW*`, nor an operator norm such as

\[
\left\|G-\operatorname{Diag}(G)\right\|_{\rm op}.
\tag{26}
\]

Even adding exact separate knowledge of all four diagonal entries `G_{chi,chi}` would not fix this, by (21)--(24).

This mirrors the source-side obstruction of `PL-424`: diagonal variances in two Fourier-dual bases can agree while the full covariance geometry differs drastically. Here the same phenomenon is already built into the principal pair-correlation object used to connect Dirichlet zeros to primes in arithmetic progressions. The fact that the literature calls (8) a mixed pair-correlation quantity is therefore not enough for the matrix transfer required by `PL-425`.

Yıldırım and Kandhil--Languasco--Moree successfully use these aggregate observables to obtain or motivate mean-square/error estimates for primes in arithmetic progressions. That application is not contradicted. A mean square for one residue class is exactly the sort of diagonal quadratic form that (8) is designed to control. The present line needs more: enough joint information across residue/character channels to preserve a **least-eigenvalue inequality**.

## 5. Prior-art and novelty audit

No novelty is claimed for Dirichlet-`L` pair correlation, character orthogonality, Fourier diagonalization on `U_5`, Gram positivity, or biunimodular vectors. The key literature facts are prior art in sources 105 and 107, and the matched `C_4` control itself was already isolated abstractly in `PL-424`.

The durable contribution here is the line-specific audit: when the exact Yıldırım--Kandhil observable is written as a matrix map, it retains precisely a Fourier-diagonal compression of the full mixed-character zero covariance. Therefore the most obvious existing pair-correlation theorem does not close the specific matrix-valued transfer gap identified by `PL-425`.

A targeted literature check around Yıldırım's theorem, Kandhil--Languasco--Moree's 2026 refinement, Dirichlet-`L` pair-correlation work, and recent distinct-`L` zero comparisons did not locate a theorem providing the required fixed-modulus **individual** bounds for every `G_{chi,psi}` or a comparable operator-norm estimate in the moving range relevant to the short-interval transfer. This is an absence-of-located-prior-art statement only; it is not a proof that no such theorem exists.

## 6. Adversarial audit and scope

1. **The modern pair-correlation results quoted above assume GRH.** Kandhil--Languasco--Moree state that convention before defining (2), and Yıldırım's asymptotic is also stated under GRH. No such hypothesis is imported into the `prime_lattice` target; the finite Fourier-compression identity (5) is algebraic once the matrix is defined.

2. **The matched PSD matrices are controls, not zero statistics.** Actual Dirichlet zero sets may satisfy additional identities strong enough to control the missing coherences. A theorem exploiting such identities would survive this obstruction.

3. **The result does not prove that off-diagonal `G_{chi,psi}` are large.** It proves only that the available aggregate estimates do not determine them. Small individual mixed correlations remain plausible and would be useful if proved.

4. **Uniformity in every residue does not repair the loss.** At modulus `5` there are only four residue vectors, and (5) shows exactly what their four quadratic forms recover. One needs additional test vectors or direct matrix-entry estimates for tomography.

5. **The pair-correlation ranges are not silently transferred to the short-interval range.** This finding is a representation audit before any quantitative explicit-formula transfer. Range matching would be a separate gate even if the full matrix were controlled.

6. **No implication toward RH is claimed.** Even a successful full-matrix transfer would only address the local positive-image gate in the longer `PL-407`--`PL-425` chain; the source-replacement, continuation and final localization gates would remain.

## Consequence for the research line

The next step after `PL-425` should **not** be to invoke the known all-residue estimates for `F_5(x,T;a)` as though they were a mixed-character covariance theorem. They are not tomographically complete for the matrix needed here.

A viable zero-side continuation must instead prove something genuinely stronger, for example individual fixed-character estimates

\[
G_{\chi,\psi}(x,T)=\text{controlled main term}+o(\text{diagonal scale})
\qquad(\chi\ne\psi),
\tag{27}
\]

with enough uniformity to survive the explicit-formula transfer, or an operator-norm estimate for the complete `4 x 4` matrix. Alternatively, one can bypass zero-pair correlation and attack the actual short-interval prime covariance directly. The current published aggregate pair-correlation machinery is structurally too compressed to certify the `PL-421` least-eigenvalue gate by itself.