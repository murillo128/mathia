---
id: WP-366
title: Dilation-covariant Whittaker boundary averaging collapses to Rankin--Selberg
branch: weil_positivity
status: supported
kind: whittaker-boundary-dilation-covariance-obstruction
claim_strength: exact positive-globalization classification with unconditional critical diagonal divergence
created: 2026-09-19
related: [WP-363, WP-364, WP-365]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - Uniqueness of Haar measure on the locally compact multiplicative group of positive reals
  - Audrey Terras, The Chowla-Selberg Method for Fourier Expansion of Higher Rank Eisenstein Series, Canadian Mathematical Bulletin 28 (1985), 280--294, doi:10.4153/CMB-1985-034-1
  - Bibekananda Maji, Pritam Naskar, and Sumukha Sathyanarayana, A series associated to Rankin-Selberg L-function and modified K-Bessel function, International Journal of Number Theory 21 (2025), 695--714, doi:10.1142/S1793042125500356
---

# WP-366 — Dilation-covariant Whittaker boundary averaging collapses to Rankin--Selberg

## Claim

The literal fixed-height Whittaker--Hecke boundary feature

\[
v_r(Y)_n=\lambda_r(n)K_{ir}(2\pi nY)
\tag{1}
\]

does produce an honest positive finite--archimedean coupling. For every fixed `Y>0`, its Gram kernel is positive, and the arithmetic index `n` is coupled nonseparably to the archimedean scale through `nY`.

However, if that height is globalized by a positive locally finite measure homogeneous under dilation, the measure is forced to be a power of multiplicative Haar measure. The Mellin change of variables then separates the `nY` incidence and reproduces exactly the finite Rankin--Selberg Gram times the archimedean Bessel Gram isolated in `WP-365`. At the critical half-density `q=1/2`, the diagonal is infinite because the nonnegative Rankin--Selberg diagonal series already diverges at `s=1`.

Thus this most literal non-product Whittaker boundary route cannot simultaneously retain positivity, remove the arbitrary height scale by dilation covariance, and reach the critical Weil weighting.

**Classification:** `CLASSICAL-HAAR-UNIQUENESS + CLASSICAL-WHITTAKER-MELLIN + EXACT-DERIVED + FIXED-HEIGHT-NONPRODUCT-GRAM + POSITIVE-DILATION-COVARIANT-GLOBALIZATION + MELLIN-SEPARATION + RANKIN-SELBERG-REDUCTION + CRITICAL-DIAGONAL-DIVERGENCE + MATCHED-CONTROL + DECISIVE-NARROWING + NO-NOVELTY-CLAIM-FOR-CLASSICAL-INGREDIENTS`.

## 1. A fixed-height non-product positive form exists

For `Y>0`, define

\[
B_Y(r,u)=\sum_{n\ge1}\lambda_r(n)\lambda_u(n)
K_{ir}(2\pi nY)K_{iu}(2\pi nY).
\tag{2}
\]

Equivalently, with (1),

\[
B_Y(r,u)=\langle v_r(Y),v_u(Y)\rangle_{\ell^2}.
\tag{3}
\]

For real `r`, the Eisenstein Hecke coefficients `lambda_r(n)` have at most divisor-type growth. For fixed `Y>0`, the exponential large-argument decay of `K_{ir}(2 pi nY)` therefore dominates the coefficient growth, so `v_r(Y)` belongs to `ell^2`. Consequently, for every finite set of real spectral parameters `r_j` and coefficients `c_j`,

\[
\sum_{j,k}\overline{c_j}c_k B_Y(r_j,r_k)
=
\sum_{n\ge1}\left|\sum_j c_j\lambda_{r_j}(n)K_{ir_j}(2\pi nY)\right|^2
\ge0.
\tag{4}
\]

This is stronger than merely multiplying a finite-place Gram by an archimedean scalar. At fixed height the arithmetic coordinate and the real-place geometry occur in the same feature coordinate through `nY`; the kernel is genuinely nonseparable before height integration.

## 2. Positive dilation covariance uniquely fixes the height measure

Let `mu_q` be a positive locally finite Borel measure on `(0,infinity)` satisfying

\[
\mu_q(aE)=a^q\mu_q(E)
\tag{5}
\]

for every Borel set `E` and every `a>0`. Weighting by `Y^{-q}` converts (5) to invariance under multiplication by `a`. By uniqueness of Haar measure on the locally compact group `R_{>0}` under multiplication,

\[
d\mu_q(Y)=cY^q\frac{dY}{Y},
\qquad c\ge0.
\tag{6}
\]

Thus exact positive scalar dilation covariance leaves no freedom to choose a special cutoff profile or fitted scale kernel.

Globalize (2) by

\[
G_q(r,u)=\int_0^\infty B_Y(r,u)\,d\mu_q(Y).
\tag{7}
\]

For `q>1`, absolute convergence justifies interchanging the sum and integral. Put

\[
H_q(r,u)=\int_0^\infty K_{ir}(x)K_{iu}(x)x^{q-1}\,dx.
\tag{8}
\]

The substitution `x=2 pi nY` gives

\[
\int_0^\infty K_{ir}(2\pi nY)K_{iu}(2\pi nY)
Y^q\frac{dY}{Y}
=(2\pi n)^{-q}H_q(r,u).
\tag{9}
\]

Therefore

\[
\boxed{
G_q(r,u)
=
c(2\pi)^{-q}H_q(r,u)
\sum_{n\ge1}\frac{\lambda_r(n)\lambda_u(n)}{n^q}
}
\tag{10}
\]

for `q>1`. The last factor is exactly the finite Rankin--Selberg Gram `K_q^fin` used in `WP-365`. Hence

\[
G_q(r,u)=c(2\pi)^{-q}H_q(r,u)K_q^{\mathrm{fin}}(r,u).
\tag{11}
\]

The genuinely non-product fixed-height incidence has disappeared: the unique positive scalar dilation-covariant globalization Mellin-separates it into the same finite-times-archimedean tensor class already tested in `WP-365`.

## 3. The critical half-density has infinite diagonal

The critical exponent required by this route is `q=1/2`. On the diagonal, the integrand in (7) is nonnegative, so Tonelli applies even if the result is infinite. Equations (6)--(9) yield

\[
G_{1/2}(r,r)
=
c(2\pi)^{-1/2}H_{1/2}(r,r)
\sum_{n\ge1}\frac{\lambda_r(n)^2}{n^{1/2}}.
\tag{12}
\]

For real `r`, `H_{1/2}(r,r)` is finite and strictly positive. `WP-363` and `WP-365` identify the diagonal Rankin--Selberg Dirichlet series with nonnegative coefficients and its pole at `s=1`; in particular,

\[
\sum_{n\ge1}\frac{\lambda_r(n)^2}{n}=\infty.
\tag{13}
\]

Since `n^{-1/2} >= n^{-1}` termwise,

\[
\sum_{n\ge1}\frac{\lambda_r(n)^2}{n^{1/2}}=\infty.
\tag{14}
\]

Therefore every nonzero positive dilation-covariant scalar globalization has

\[
\boxed{G_{1/2}(r,r)=+\infty.}
\tag{15}
\]

This obstruction is prior to any zero-location question. It uses neither RH nor inserted zero data.

## 4. Matched control and trilemma

Replace `lambda_r(n)` by any coefficient family `a_r(n)` of polynomial growth. The fixed-height feature remains in `ell^2` because the Bessel factor supplies exponential decay, and the same homogeneous positive averaging still Mellin-separates the `nY` coupling into an archimedean Mellin factor times a Dirichlet kernel. Thus the erasure of non-product incidence is structural, not peculiar to zeta.

The arithmetic-specific part is the critical divergence in (14), supplied here by the Rankin--Selberg diagonal pole. The route therefore has a sharp trilemma:

1. At fixed `Y`, one has an honest non-product positive Gram but retains an arbitrary height scale.
2. Positive scalar dilation-covariant globalization removes that arbitrary scale, but uniqueness of the measure forces Mellin separation back to the `WP-365` tensor class and gives an infinite critical diagonal.
3. Analytically continuing the separated expression beyond its positive Hilbert domain abandons the inherited positive-form theorem and re-enters the critical-zero obstruction of `WP-365`.

This is not a claim that all possible finite--archimedean couplings fail. It classifies the most direct attempt to globalize the literal Whittaker boundary incidence while retaining a positive scalar measure and exact scale covariance.

## 5. Prior-art and novelty audit

All analytic ingredients used above are classical. Haar-measure uniqueness supplies (6). Whittaker/K-Bessel Fourier expansions and Mellin transforms are standard in Eisenstein and Rankin--Selberg theory; Terras's Chowla--Selberg treatment is representative of the classical connection between Eisenstein Fourier coefficients, Hecke data, and K-Bessel functions. Maji--Naskar--Sathyanarayana study modern Rankin--Selberg/K-Bessel series and their relation to zeta zeros, confirming that such series themselves are established analytic-number-theory objects.

A targeted search for Whittaker height averaging, K-Bessel Gram kernels, dilation-covariant averaging, and Rankin--Selberg positivity did not locate a source claiming the Mathia-specific classification proved here. That search is not a historical novelty proof. No novelty is claimed for Haar uniqueness, Mellin separation, Rankin--Selberg identities, Bessel decay, or the diagonal pole.

The substantive result is narrower: `WP-365` left open the possibility that the missing sign might survive if finite and archimedean data were coupled **before** scalar factorization. Equations (1)--(4) realize exactly such a source-defined positive `nY` coupling. Equations (5)--(11) then show that the canonical positive scale-covariant globalization necessarily destroys that coupling by Mellin separation, while (12)--(15) show that the critical half-density is not even a finite Hilbert Gram.

## Representation audit

The construction begins with the actual Whittaker coordinate `nY` and Eisenstein Hecke coefficients, not with zeta zeros or a desired Weil kernel. Positivity at fixed height is a direct squared-norm theorem. Dilation covariance is imposed as a geometric scale-removal symmetry before any arithmetic sign is inspected, and its measure is then uniquely determined rather than fitted.

The Rankin--Selberg factorization is a derived consequence of the Mellin substitution, not an input used to define the Gram. The critical obstruction is tested only after the representation is fixed. It is witnessed by divergence of a nonnegative coefficient series and therefore does not import RH, a zero spectrum, or an RH-equivalent positivity functional.

The surviving escape is correspondingly precise. A successful Mathia construction must obtain essential finite--archimedean interaction from something that is not erased by positive scalar dilation averaging: for example, a source-defined absolute scale, an intrinsically non-Haar or operator-valued scale coupling forced by geometry, additional global degrees of freedom, or an indefinite/intersection/cohomological sign theorem rather than an ordinary Hilbert Gram.

## Verdict

**Supported exact negative.** The fixed-height Whittaker--Hecke family supplies the literal non-product positive boundary geometry that `WP-365` did not test. But exact positive scalar dilation covariance uniquely forces power-Haar averaging, and Mellin scaling then turns that geometry back into the `WP-365` Rankin--Selberg tensor product. At the Weil half-density the resulting diagonal is already infinite.

Do not spend further search budget on positive scalar power-Haar averaging of this fixed-height Whittaker Gram. Any surviving Maaß--Selberg/Whittaker route must keep a source-forced coupling across scales or use a different independent sign theorem before the arithmetic and archimedean sectors separate.