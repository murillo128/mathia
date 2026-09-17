---
id: WP-353
title: Finite-order reciprocal phase gauge is only an exponential normalization
branch: weil_positivity
status: supported
kind: finite-order-phase-gauge-classification
claim_strength: exact classical factorization plus arithmetic-cusp normalization and matched growth/category controls
created: 2026-09-17
related: [WP-165, WP-241, WP-345, WP-348, WP-351, WP-352]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - classical Hadamard factorization theorem for entire functions of finite order
  - classical uniqueness of normalized scaling matrices for finite-area cusps up to translation
  - C. R. Graham and M. Zworski, Scattering matrix in conformal geometry, Invent. Math. 152 (2003), 89-118
---

# WP-353 — Finite-order reciprocal phase gauge is only an exponential normalization

## Claim

`WP-352` exhibited the zero-free reciprocal matched control

\[
c_a(s)=e^{a(s-1/2)},\qquad a\in\mathbb R,
\tag{1}
\]

which preserves critical-line unitarity and the complete zero/pole divisor while shifting the scalar logarithmic phase derivative by an additive constant. Under the natural finite-order hypothesis relevant to completed zeta/scattering normalizers, this is not merely one convenient control: it is the **entire zero-free order-one control family**.

More precisely, let `c` be entire and nowhere zero, of finite order at most one, and assume

\[
c(1-s)=c(s)^{-1},\qquad
|c(1/2+it)|=1,\qquad
c(1/2)=1.
\tag{2}
\]

Then necessarily

\[
\boxed{c(s)=e^{a(s-1/2)}\quad\text{for a unique }a\in\mathbb R.}
\tag{3}
\]

Thus the residual scalar phase ambiguity isolated in `WP-352` is exactly one real normalization parameter once finite order is imposed.

For a standard finite-area arithmetic cusp, however, the usual scaling matrix is normalized so that the cusp stabilizer becomes the unit translation group. After that normalization the scaling matrix is unique only up to right translation, not positive dilation; the Eisenstein series and its constant scattering coefficient are insensitive to that residual translation. Hence the arithmetic source normalization can fix the real exponential gauge that remains in (3).

This does **not** produce Weil positivity. If two scalar meromorphic normalizers of order at most one have the same zero/pole divisor, their quotient is an entire nowhere-zero function of order at most one. After imposing the reciprocal, unitary and source-normalization conditions above, that quotient is fixed. The scalar normalizer is therefore determined by its divisor plus normalization. A scalar phase anchor at this level turns the remaining problem into canonical-product/divisor reconstruction; it supplies no independent geometric sign theorem. The surviving Mathia route must still introduce a noncentral finite--archimedean/global coupling before scalarization, or an independently positive larger geometric object whose projection yields the Weil form.

**Classification:** `EXACT-DERIVED + HADAMARD-CLASSICALIZATION + RESIDUAL-GAUGE-EXHAUSTED + ARITHMETIC-CUSP-NORMALIZATION-TESTED + DIVISOR-RECONSTRUCTION-REDIRECT + MATCHED-GROWTH-CONTROL + MATCHED-SCATTERING-CATEGORY-CONTROL + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

## 1. Hadamard factorization exhausts the zero-free order-one gauge

Put `z=s-1/2`. Because `c` is entire, zero-free and has finite order at most one, Hadamard factorization has no canonical-product factor and gives

\[
c(1/2+z)=e^{Az+B}
\tag{4}
\]

for constants `A,B\in\mathbb C`.

Reciprocity gives

\[
e^{-Az+B}=e^{-Az-B},
\tag{5}
\]

so `e^{2B}=1`. The central normalization `c(1/2)=1` gives `e^B=1`, and hence the function itself reduces to

\[
c(1/2+z)=e^{Az}.
\tag{6}
\]

On the critical line `z=it`,

\[
|c(1/2+it)|=|e^{iAt}|=e^{-t\operatorname{Im}A}.
\tag{7}
\]

Unit modulus for every real `t` forces `\operatorname{Im}A=0`. Writing `A=a\in\mathbb R` proves (3). Uniqueness follows by differentiation at `s=1/2`.

The logarithmic phase generator therefore transforms exactly as in `WP-352`:

\[
q_{cg}(t)=q_g(t)+a.
\tag{8}
\]

There is no additional nonlinear zero-free order-one reciprocal rephasing hidden behind that matched control.

## 2. The growth hypothesis is essential

The finite-order bound cannot be dropped. For example,

\[
c(s)=\exp\!\big((s-1/2)^3\big)
\tag{9}
\]

is entire, nowhere zero, satisfies `c(1-s)=c(s)^{-1}` and `c(1/2)=1`, and has unit modulus on `s=1/2+it`, because `(it)^3` is purely imaginary. It is not of the linear-exponential form (3).

More generally odd real polynomials in `s-1/2` give further reciprocal unitary controls of higher finite order. Therefore the exhaustive statement is specifically an **order-at-most-one** theorem. This is the correct regime for the scalar completed-zeta/scattering normalizers tested here; it is not a growth-free statement about arbitrary meromorphic scattering families.

Zeros and poles are a separate escape. Once they are allowed in the control, genuine inner/CDD factors survive; `WP-345` and `WP-348` already show why such factors cannot be silently identified with an independently forced arithmetic sign mechanism. The present result closes only the zero-free gauge.

## 3. Arithmetic cusp normalization fixes the dilation parameter

For a finite-area cusp `\mathfrak a`, choose a scaling matrix `\sigma_\mathfrak a` satisfying

\[
\sigma_\mathfrak a^{-1}\Gamma_\mathfrak a\sigma_\mathfrak a
=\Gamma_\infty,
\tag{10}
\]

with `\Gamma_\infty` generated by unit translation. Once this width-one normalization is imposed, another admissible scaling matrix differs by right translation (and the harmless projective sign), not by an arbitrary positive diagonal dilation. Right translation leaves the imaginary part entering the Eisenstein definition unchanged and changes only the horizontal Fourier coordinate at the target cusp; the constant term, and hence the scalar scattering coefficient, is unchanged.

So in the standard arithmetic Eisenstein problem the geometric source does contain an independent convention that can remove the real scale parameter `a` in (3). This is a genuine correction to the stronger claim that every arithmetic cusp scattering problem necessarily retains an arbitrary exponential phase gauge.

But removing a normalization ambiguity is not a positivity theorem. After it is removed, the scalar phase is fixed because the divisor plus finite-order normalization fixes the meromorphic function, not because a Mathia-native positive pairing has forced the Weil quadratic form to be nonnegative.

## 4. Matched category control: conformally compact scattering retains exactly this gauge

The arithmetic cusp conclusion is not a generic fact about geometric scattering. In conformally compact scattering, Graham--Zworski conformal covariance gives, under a change of boundary representative `\widehat h=e^{2\Upsilon}h`,

\[
\widehat S(s)=e^{-s\Upsilon}S(s)e^{(n-s)\Upsilon}.
\tag{11}
\]

For constant `\Upsilon` and one-dimensional conformal boundary this contributes the scalar factor

\[
e^{(1-2s)\Upsilon}
= e^{-2\Upsilon(s-1/2)},
\tag{12}
\]

which is exactly family (1). Thus the exponential gauge has a genuine geometric realization as boundary-scale covariance in the broader scattering category. Width-normalized arithmetic cusps are stricter precisely because their source normalization removes the dilation.

This matched control matters: the phase anchor is not forced by abstract scattering geometry alone. It is supplied by the extra arithmetic cusp normalization.

## 5. Same divisor plus source normalization is reconstruction, not independent positivity

Suppose `g_1` and `g_2` are scalar meromorphic functions of order at most one with the same zeros and poles, including multiplicities, and with quotient

\[
c=g_1/g_2.
\tag{13}
\]

Then `c` is entire and nowhere zero; standard finite-order estimates keep it in the finite-order class. If the two normalizers obey the same reciprocal symmetry, critical-line unitarity and central/source normalization, Sections 1 and 3 force `c\equiv1`.

Consequently, after the arithmetic normalization has fixed the one real zero-free gauge, the scalar normalizer contains no new curvature/energy datum independent of its divisor. Recovering its phase is mathematically legitimate but it is a canonical-product reconstruction of spectral/divisor data. Under the `weil_positivity` contract, that cannot count as the sought geometric source of sign.

The surviving target is sharper than after `WP-352`: a successful construction must force positivity **before** this scalar reconstruction stage. It must either create noncentral cross-place coupling whose sign theorem is independent of the zeta divisor, or derive the scalar Weil observable as a projection/trace of a larger independently positive geometric object while surviving the matched CDD and growth controls.

## Prior-art audit

The factorization used in Section 1 is the classical Hadamard factorization theorem, and the uniqueness of width-normalized cusp scaling matrices up to translation is standard automorphic spectral theory. Equation (11) is the standard conformal covariance of the Graham--Zworski scattering operator. None of these ingredients is new.

The Mathia-specific contribution is the structural boundary obtained by combining them with `WP-352`: its exponential control is exhaustive in the relevant zero-free order-one class; arithmetic cusp normalization can remove that gauge; and once it does, scalar phase recovery has collapsed to divisor-plus-normalization reconstruction rather than an independent positivity mechanism. This is therefore a **prior-art classicalization and decisive narrowing**, not a claim of a new entire-function or scattering theorem.

## Limitations

This finding does not rule out higher-order scattering normalizers, controls with zeros or poles, matrix-valued/noncentral scattering, cohomological or adelic couplings, or a positive geometric theorem acting before scalarization. It also does not derive the finite-prime and archimedean terms of the Weil explicit formula from one positive form. The result only closes the residual zero-free finite-order scalar phase-gauge escape and clarifies exactly what arithmetic cusp normalization can and cannot buy.