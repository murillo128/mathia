# WP-220 — Doubly commuting mixed-prime restrictions preserve the Bost–Connes Weil defect

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-GRAM + FINITE-MIXED-PRIME + MANDREKAR-SETO + TOEPLITZ-COMPRESSION-RIGIDITY + ADMISSIBLE-SUBSPACE-NO-GO + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-219` proves that a nonzero admissible subspace on one Bost–Connes prime-power Hardy ray cannot repair the critical finite-Weil sign if it remains invariant under the source prime shift: Beurling's theorem makes every such compression exactly unitarily equivalent to the original Toeplitz defect. The obvious escape is to couple several prime rays before restricting.

A substantial natural class of that escape is also sign-inert. Fix a finite prime set

\[
F=\{p_1,\ldots,p_d\},
\qquad
\mathcal H_F=H^2(\mathbb D^d)\simeq \ell^2(\mathbb N_0^d),
\]

and let `S_j=M_{z_j}` be the coordinate shift representing multiplication by the source isometry at `p_j`. At the Bost–Connes critical point put

\[
r_j=p_j^{-1/2},
\qquad
G_j=T\!\left(P_{r_j}(\theta_j)\right),
\]

where `G_j` acts in the `j`-th prime coordinate and

\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}.
\]

The zero-mode-subtracted finite-prime Weil operator forced by the one-prime rays of `WP-216` and the finite cosine comb of `WP-217` is

\[
\boxed{
W_F=\sum_{j=1}^d (\log p_j)(I-G_j)
=T(w_F),
}
\]

with

\[
w_F(\theta)
=\sum_{j=1}^d (\log p_j)\bigl(1-P_{r_j}(\theta_j)\bigr).
\]

Its nonzero Fourier coefficient at `k e_j`, `k\ne0`, is exactly

\[
-(\log p_j)p_j^{-|k|/2}.
\]

Now let `0\ne M\subset H^2(\mathbb D^d)` be closed and invariant under every coordinate shift, and write

\[
R_j=S_j|_M.
\]

Assume that the source shifts remain **pairwise doubly commuting on the restricted space**,

\[
R_iR_j^*=R_j^*R_i
\qquad(i\ne j).
\]

The multivariable Mandrekar–Seto theorem then forces

\[
\boxed{M=\Theta H^2(\mathbb D^d)}
\]

for a scalar inner function `Theta`. Multiplication by `Theta` is unitary from the full Hardy module onto `M`. Because `|Theta|=1` almost everywhere on the distinguished boundary, compression of every bounded scalar Toeplitz form is unchanged:

\[
\boxed{
U_\Theta^*\bigl(P_MT(w)|_M\bigr)U_\Theta=T(w).
}
\]

Consequently

\[
\boxed{
U_\Theta^*\bigl(P_MW_F|_M\bigr)U_\Theta=W_F,
}
\]

so the mixed-prime restriction cannot remove any part of the sign defect. In particular `P_MW_F|_M` is indefinite whenever `F` is nonempty.

This is stronger than the one-prime result in one important respect: `Theta` may depend jointly on several prime coordinates, so the theorem allows genuinely nonseparable **mixed-prime Beurling-type coupling before restriction**. What it does not cover is equally important. Joint shift invariance alone does not imply double commutation after compression in several variables. A surviving source-derived restriction must therefore leave the scalar Beurling/Mandrekar class: it must destroy pairwise double commutation, introduce higher multiplicity/operator-valued module structure, couple to the archimedean sector before the restriction is formed, or otherwise change the finite-prime Hardy module itself.

The accepted Bost–Connes completion clue therefore remains unresolved, but its admissible-test-space escape is narrower than after `WP-219`: **neither one-prime covariance nor finite mixed-prime covariance with doubly commuting restricted shifts can change the critical Weil orientation.**

## 1. Exact finite-prime operator

`WP-216` derives the critical Bost–Connes conditional Gram

\[
G_1(m,n)=\frac{\gcd(m,n)}{\sqrt{mn}}.
\]

On a single `p_j`-axis this is the Toeplitz kernel

\[
G_j(a,b)=r_j^{|a-b|},
\qquad r_j=p_j^{-1/2},
\]

with Poisson symbol `P_{r_j}`. The desired zero-diagonal Weil orientation on that ray is

\[
W_j=(\log p_j)(I-G_j).
\]

On the finite exponent lattice `\mathbb N_0^d`, embed each `W_j` in its own coordinate and sum:

\[
W_F=\sum_jW_j.
\tag{1}
\]

This is not the defect of the product Gram `I-\prod_jG_j`; that operation would create mixed Fourier modes absent from the finite Mangoldt comb. Equation (1) is instead exactly the additive prime-axis operator whose nonconstant Fourier support is the finite-prime part identified in `WP-217`.

Since

\[
P_{r_j}(\theta_j)
=1+\sum_{k\ne0}r_j^{|k|}e^{ik\theta_j},
\]

we obtain

\[
w_F(\theta)
=\sum_j(\log p_j)(1-P_{r_j}(\theta_j))
\tag{2}
\]

and therefore

\[
\widehat w_F(k e_j)=-(\log p_j)p_j^{-|k|/2},
\qquad k\ne0.
\tag{3}
\]

The scalar zero mode of (2) is zero. Thus `W_F` is only the sign-sensitive finite-prime defect; it is **not** being claimed to include the Euler-pole normalization, the archimedean Gamma term, or the completed Weil functional.

## 2. The finite-prime operator is exactly indefinite

No spectral theorem is needed to see the bad sign. Fix any `j` and take

\[
f_t=1+t z_j,
\qquad t\in\mathbb R.
\]

On `\operatorname{span}\{1,z_j\}`, the `j`-th Poisson Gram has matrix

\[
\begin{pmatrix}
1&r_j\\
r_j&1
\end{pmatrix},
\]

so

\[
\langle f_t,(I-G_j)f_t\rangle=-2r_j t.
\tag{4}
\]

For `q\ne j`, the vector is constant in the `q`-coordinate and

\[
\langle f_t,(I-G_q)f_t\rangle=0.
\]

Hence

\[
\boxed{
\langle f_t,W_Ff_t\rangle
=-2t(\log p_j)p_j^{-1/2}.
}
\tag{5}
\]

Choosing `t>0` and `t<0` gives both signs. Thus `W_F` is indefinite for every nonempty finite `F`.

The same conclusion follows from the continuous symbol (2), which is negative on an open neighborhood of the torus origin and positive in other directions, but (5) is an exact finite-dimensional witness.

## 3. Double commutation forces Beurling type even after mixed-prime coupling

Let `M` be a nonzero closed subspace invariant under every `S_j`. Since the coordinate multipliers are isometries and commute, the restricted tuple

\[
R=(R_1,\ldots,R_d),
\qquad R_j=S_j|_M,
\]

is a commuting tuple of isometries. Unlike in one variable, arbitrary joint invariance does **not** force a scalar-inner submodule. The additional condition here is pairwise double commutation:

\[
R_iR_j^*=R_j^*R_i,
\qquad i\ne j.
\tag{6}
\]

Mandrekar's theorem gives the bidisc statement: a nonzero invariant subspace of `H^2(\mathbb D^2)` is of Beurling type `Theta H^2` exactly when its two restricted shifts doubly commute. Bergqvist's 2023 proofs explicitly note that the reproducing-kernel argument extends to `H^2(\mathbb D^d)`; the `d`-variable theorem had already been obtained by Seto, using the multivariable doubly commuting Wold decomposition. Thus (6) gives

\[
M=\Theta H^2(\mathbb D^d)
\tag{7}
\]

for an inner `Theta\in H^\infty(\mathbb D^d)`, with

\[
|\Theta|=1
\quad\text{a.e. on }\mathbb T^d.
\tag{8}
\]

This is the precise point at which the result narrows rather than eliminates mixed-prime restrictions. Condition (6) is an additional structural hypothesis on the compressed source shifts; it is not automatic from joint invariance.

## 4. Every scalar Toeplitz form survives the restriction unchanged

Define

\[
U_\Theta:H^2(\mathbb D^d)\to M,
\qquad U_\Theta f=\Theta f.
\]

By (8), `U_Theta` is unitary. Let `w\in L^\infty(\mathbb T^d)` be real and `T(w)=P_+M_w|_{H^2}`. For `f,g\in H^2(\mathbb D^d)`,

\[
\begin{aligned}
\langle U_\Theta f,\,P_MT(w)U_\Theta g\rangle
&=\langle \Theta f,T(w)\Theta g\rangle\\
&=\int_{\mathbb T^d}w\,\overline{\Theta f}\,\Theta g\,dm\\
&=\int_{\mathbb T^d}w\,\overline f g\,dm\\
&=\langle f,T(w)g\rangle.
\end{aligned}
\tag{9}
\]

The outer projection in the Toeplitz operator disappears when paired with `Theta f\in H^2`, and the third equality uses the unimodular boundary values of `Theta`. Therefore

\[
U_\Theta^*\bigl(P_MT(w)|_M\bigr)U_\Theta=T(w).
\tag{10}
\]

Applying (10) to (2) proves

\[
U_\Theta^*\bigl(P_MW_F|_M\bigr)U_\Theta=W_F.
\tag{11}
\]

Equations (5) and (11) immediately imply

\[
P_MW_F|_M\not\succeq0.
\tag{12}
\]

Indeed the full bounded self-adjoint compression, not merely its essential spectrum, is unitarily equivalent to the unrestricted finite-prime defect.

## 5. Why this genuinely tests a mixed-prime escape

The conclusion is not limited to product restrictions such as

\[
\Theta_1(z_1)\cdots\Theta_d(z_d)H^2(\mathbb D^d).
\]

The scalar inner function in (7) may depend jointly on several coordinates. Hence the admissible space can encode nonseparable finite mixed-prime information before the compression while still satisfying the source-compatible doubly commuting module condition. Unimodularity then makes that entire Beurling-type coupling invisible to every scalar Toeplitz quadratic form.

This is the multivariable analogue of the rigidity in `WP-219`, but the hypothesis is necessarily stronger. In one variable every nonzero shift-invariant Hardy subspace is Beurling type. In several variables the invariant-subspace lattice is much richer. The Mandrekar–Seto theorem identifies double commutation as exactly the boundary on which the one-variable rigidity persists.

Therefore a source-derived test-space rescue must exhibit a mathematically meaningful reason that the restricted prime isometries cease to doubly commute. Merely saying that the admissible condition is "global" or "mixed-prime" is insufficient; if its compressed source tuple remains in the Mandrekar–Seto class, the Weil defect is unchanged.

## 6. Matched controls

Nothing in the proof is specific to the arithmetic values `r_j=p_j^{-1/2}` or `\log p_j`. Replace them by arbitrary parameters

\[
0<r_j<1,
\qquad c_j>0,
\]

and define

\[
W=\sum_jc_j\bigl(I-T(P_{r_j}(\theta_j))\bigr).
\]

The same test vector proves indefiniteness and the same inner-multiplier identity proves exact compression rigidity on every nonzero jointly invariant subspace whose restricted coordinate shifts doubly commute.

This generalized-product survival is appropriate for a negative classification result: the obstruction comes from Hardy-module geometry, not from a hidden Riemann theorem. Conversely, any positive survivor must introduce additional source structure that fails these controls in an explainable way before the desired arithmetic sign is read off.

## 7. Prior-art and novelty audit

The invariant-subspace theorem used here is classical operator/function theory.

- V. Mandrekar, **“The validity of Beurling theorems in polydiscs,”** *Proceedings of the American Mathematical Society* **103** (1988), 145–148, DOI `10.1090/S0002-9939-1988-0938659-7`, proves the bidisc Beurling-type characterization by double commutation.
- Michio Seto, **“Invariant Subspaces on T^N and R^N,”** *Canadian Mathematical Bulletin* **47** (2004), no. 1, gives the `N`-dimensional doubly commuting extension.
- Linus Bergqvist, **“Alternative proofs of Mandrekar's theorem,”** *Proceedings of the American Mathematical Society, Series B* **10** (2023), 46–55, DOI `10.1090/bproc/156`, gives modern reproducing-kernel/Toeplitz proofs and explicitly explains the extension to `H^2(\mathbb D^n)`.

No novelty is claimed for Mandrekar–Seto theory, inner multipliers, multivariable Toeplitz compression, or the Bost–Connes system. The Mathia-specific result is their exact application to the finite-prime critical Bost–Connes Weil operator singled out by `WP-216` and `WP-217`: **every finite mixed-prime admissible restriction whose source tuple remains doubly commuting is sign-inert.**

A targeted literature search found the classical invariant-subspace classifications and later generalizations of doubly commuting/mixed invariant subspaces, but no source asserting this Bost–Connes/Weil consequence. This should not be confused with Nyman–Beurling totality, Connes–Consani semilocal compression, Sonin spaces, or arbitrary adelic restrictions. Those constructions need not be scalar Beurling submodules of this finite prime polydisc and are not covered by (6)–(12).

## 8. Boundary and research disposition

The theorem is exact but deliberately finite and conditional. It does **not** rule out:

- jointly shift-invariant subspaces on which the compressed prime shifts fail pairwise double commutation;
- higher-multiplicity or operator-valued Hardy modules;
- an unbounded/non-Toeplitz source form with a different domain;
- a finite–archimedean coupling formed before the admissible space;
- a genuinely global semilocal/adelic restriction whose intersection with the finite prime module is not of the form considered here.

Nor does it provide the Gamma or polar terms. Its role is to classify one substantial part of the noncompact test-space escape left by `WP-218` and `WP-219`.

The excluded implication is

\[
\boxed{
\begin{gathered}
\text{critical finite Bost--Connes Weil defect}\\
+\ \text{joint prime-shift invariant admissible space}\\
+\ \text{pairwise doubly commuting restricted source shifts}
\end{gathered}
\not\Rightarrow
\text{positive Weil form}.
}
\]

The live Bost–Connes route must now cross a sharper structural boundary. If it uses test-space restriction rather than changing the operator itself, the source must force **non-doubly-commuting mixed-prime geometry (or a still larger finite–archimedean module) before positivity is invoked**. That extra relation must then generate the completed Gamma/polar sectors and survive generalized-product controls. Merely coupling primes inside a scalar inner Beurling submodule does not change the Weil orientation.