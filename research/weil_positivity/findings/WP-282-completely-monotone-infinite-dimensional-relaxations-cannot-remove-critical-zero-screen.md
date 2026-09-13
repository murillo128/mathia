---
id: WP-282
title: Completely monotone infinite-dimensional relaxations cannot remove the critical zero screen
branch: weil_positivity
status: supported
kind: infinite-dimensional-positive-relaxation-obstruction
claim_strength: exact favorable-RH no-go for every normalized positive mixture of exponential relaxations applied after the canonical local regularizer
created: 2026-09-13
related: [WP-279, WP-280, WP-281]
prior_art:
  - Hausdorff-Bernstein-Widder representation of completely monotone kernels as positive mixtures of exponentials
  - A. H. Zemanian, Relaxive Hilbert Ports, SIAM Journal on Control 12 (1974), no. 1, 106-123, DOI 10.1137/0312010
  - Rene L. Schilling, Renming Song, and Zoran Vondracek, Bernstein Functions: Theory and Applications, 2nd ed., De Gruyter Studies in Mathematics 37 (2012), chapters 1-2
  - classical Bohr almost-periodic-function theory
---

# WP-282 — Completely monotone infinite-dimensional relaxations cannot remove the critical zero screen

## Claim

`WP-281` shows that fixed finite-dimensional logarithmic-scale dynamics cannot extract the central Gamma mode from the critical Chebyshev residual: after one stable local regularizer, the RH residual is a constant plus a uniformly almost-periodic field carrying every nontrivial-zero frequency, while every finite-state transfer function is rational and therefore cannot vanish at all those frequencies.

The most immediate infinite-dimensional escape is to replace the finite state by a positive self-adjoint relaxation continuum: an arbitrary positive mixture of exponential decays, equivalently a normalized Stieltjes/relaxive response. That entire class also fails, for a stronger reason than rationality. Its boundary transfer has **strictly positive real part at every finite nonzero frequency**, so it cannot annihilate even one surviving zeta-zero mode.

Let `Y_a` be the one-state regularized critical source from `WP-281`. Under RH, used only as a favorable falsification control,

\[
Y_a(E)=C_\Gamma+A_a(E)+r_a(E),
\qquad r_a(E)\to0,
\tag{1}
\]

with

\[
A_a(E)
=-\sum_{\rho=1/2+i\gamma}
\frac{a}{(i\gamma)(a+i\gamma)}e^{i\gamma E}
\tag{2}
\]

absolutely and uniformly convergent.

Let `nu` be any probability measure on `(0,infinity)` and define the causal positive relaxation kernel

\[
k_\nu(t)=\int_{(0,\infty)} b e^{-bt}\,d\nu(b),
\qquad t>0.
\tag{3}
\]

Then `k_nu>=0`, `int_0^infinity k_nu(t)dt=1`, and its transfer function is

\[
H_\nu(z)
=\int_{(0,\infty)}\frac{b}{b+z}\,d\nu(b).
\tag{4}
\]

For every real `gamma`,

\[
\Re H_\nu(i\gamma)
=\int_{(0,\infty)}
\frac{b^2}{b^2+\gamma^2}\,d\nu(b)>0.
\tag{5}
\]

Hence

\[
\boxed{H_\nu(i\gamma)\ne0\quad\text{for every finite }\gamma,}
\tag{6}
\]

while `H_nu(0)=1`, so the Gamma constant is preserved.

If `Y_a` is passed through this relaxation with zero initial memory,

\[
Z_{a,\nu}(E)
=\int_{E_0}^{E}k_\nu(E-u)Y_a(u)\,du,
\tag{7}
\]

then

\[
Z_{a,\nu}(E)
=C_\Gamma+A_{a,\nu}(E)+o(1),
\tag{8}
\]

where

\[
A_{a,\nu}(E)
=-\sum_{\rho=1/2+i\gamma}
\frac{aH_\nu(i\gamma)}{(i\gamma)(a+i\gamma)}e^{i\gamma E}
\tag{9}
\]

is again a nonconstant uniformly Bohr almost-periodic function. Therefore

\[
\boxed{
\lim_{E\to\infty}Z_{a,\nu}(E)\text{ does not exist, even under RH.}
}
\tag{10}
\]

The measure `nu` may have continuous support and the corresponding realization may be genuinely infinite-dimensional and nonrational. Thus merely replacing finite state by an infinite positive relaxation bath does not cross the boundary left open by `WP-281`.

**Classification:** `EXACT-DERIVED + DECISIVE-NEGATIVE-FOR-COMPLETELY-MONOTONE-INFINITE-DIMENSIONAL-RELAXATION + FAVORABLE-RH-MATCHED-CONTROL + STIELTJES-POSITIVE-REAL-BOUNDARY + ALMOST-PERIODIC-ZERO-SCREEN-SURVIVES + INFINITE-SUPPORT-ALLOWED + PRIOR-ART-CLASSICALIZED-INGREDIENTS + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Positive relaxation is an infinite-dimensional category, not disguised finite state

The kernel (3) is the canonical scalar completely monotone relaxation density. Tonelli's theorem gives

\[
\int_0^\infty k_\nu(t)\,dt
=\int_{(0,\infty)}
\left(\int_0^\infty b e^{-bt}\,dt\right)d\nu(b)
=1.
\tag{11}
\]

The Hausdorff--Bernstein--Widder theorem is the classical representation principle behind this class: completely monotone responses are positive mixtures of exponential modes. When `nu` has finite support, (3) is a finite parallel bank of first-order relaxations. When `nu` has infinite or continuous support, the transfer (4) is generally nonrational and requires an infinite-dimensional realization.

There is also a direct Hilbert-space realization. Let `B>=0` be a positive self-adjoint operator and let `v` be a unit boundary vector with spectral measure `nu` supported in `(0,infinity)`. Then

\[
k_\nu(t)=\langle v,Be^{-tB}v\rangle,
\qquad
H_\nu(z)=\langle v,B(B+z)^{-1}v\rangle.
\tag{12}
\]

Thus the class already includes positive self-adjoint diffusion/relaxation continua, not just ad hoc scalar kernels. Zemanian's relaxive Hilbert-port theory gives the corresponding operator-valued classical setting: completely monotone Hilbert-port responses are represented by Stieltjes transforms of positive operator measures.

The obstruction below is therefore genuinely beyond the rational-transfer argument of `WP-281`.

## 2. Strict positive real part forbids zero-frequency notches

At a real frequency `gamma`,

\[
\frac{b}{b+i\gamma}
=
\frac{b^2}{b^2+\gamma^2}
-i\frac{b\gamma}{b^2+\gamma^2}.
\tag{13}
\]

Integrating (13) against the positive probability measure `nu` proves (5). No moment hypothesis is needed: the integrand is bounded in modulus by one. For `gamma!=0`, every integrand in the real part is strictly positive because `b>0`; at `gamma=0`, `H_nu(0)=1`.

In the Hilbert realization this is

\[
\Re H_\nu(i\gamma)
=
\langle v,
B^2(B^2+\gamma^2)^{-1}v\rangle>0.
\tag{14}
\]

The significance is sharper than “a generic filter will not know the zeros.” A normalized positive relaxation response **cannot have an imaginary-axis transmission zero at all**. Infinite dimension supplies infinitely many decay rates, but positivity locks their phases into the same open right half-plane and prevents destructive cancellation.

This is precisely the property needed for the current frontier. Preserving the constant Gamma mode asks for nonzero DC gain. Suppressing the critical zero screen asks for a notch at every `gamma`. The Stieltjes geometry makes those requirements incompatible before any zeta-specific spacing information is used.

## 3. Every critical zero mode survives the relaxation continuum

Because (2) is absolutely and uniformly convergent,

\[
\sum_\rho
\left|\frac{a}{(i\gamma)(a+i\gamma)}\right|<\infty.
\tag{15}
\]

Also `|H_nu(i gamma)|<=1`. Hence the series (9) is absolutely and uniformly convergent. It is a Bohr almost-periodic function, and its Fourier--Bohr coefficient at each distinct nontrivial-zero ordinate is

\[
-\frac{aH_\nu(i\gamma)}{(i\gamma)(a+i\gamma)},
\tag{16}
\]

which is nonzero by (6).

It remains only to justify the finite-start convolution in (7). For a single mode,

\[
\int_{E_0}^{E}
k_\nu(E-u)e^{i\gamma u}\,du
=e^{i\gamma E}
\int_0^{E-E_0}k_\nu(t)e^{-i\gamma t}\,dt.
\tag{17}
\]

The final integral tends to `H_nu(i gamma)`. More importantly, its tail error is bounded by

\[
\int_{E-E_0}^\infty k_\nu(t)\,dt,
\tag{18}
\]

independently of `gamma`. Multiplying by the absolutely summable coefficients in (15) therefore lets the limit pass uniformly through the whole almost-periodic series.

The constant part tends to `C_Gamma` by (11), and convolution of the bounded remainder `r_a(E)->0` with the fixed `L^1` kernel also tends to zero. This proves (8)--(9).

A nonconstant Bohr almost-periodic function cannot have a limit at `+infinity`; `WP-281` records the short recurrence proof. Since every coefficient (16) survives, `A_{a,nu}` is nonconstant. Equation (10) follows.

## 4. Why positivity, not finite dimensionality, is now the obstruction

`WP-281` used a cardinality mismatch: a rational finite-state transfer has only finitely many zeros, while the zeta zero field has infinitely many frequencies. That argument deliberately left nonrational infinite-dimensional responses open.

The present class is nonrational when `nu` is not finitely supported, so cardinality is no longer relevant. The failure comes instead from order positivity. Positive relaxation weights force

\[
H_\nu(i\mathbb R)\subset\{z:\Re z>0\},
\tag{19}
\]

and hence forbid even a single notch. Increasing the dimension, making the relaxation spectrum continuous, or allowing arbitrarily slow modes near zero does not alter this half-plane constraint.

This matters for the primary `weil_positivity` question because positive self-adjoint semigroup relaxation is one of the most natural ways to try to make the missing sign theorem intrinsic to geometry. Here that very positivity prevents the response from separating the Gamma center from the arithmetic zero field.

## 5. Aggressive falsification and matched controls

The theorem is intentionally not stated for every infinite-dimensional passive system. Several escapes survive, and they identify exactly what new structure would be required.

First, signed or complex mixtures of exponential modes can cancel at selected frequencies. That abandons the positive-measure/Stieltjes mechanism responsible for (5); if the signs or weights are chosen to notch the zeta ordinates, the construction also inserts the target divisor and fails the independence criterion.

Second, oscillatory conservative or RLC-type dynamics are not completely monotone relaxation. Infinite-dimensional wave/scattering systems can have transmission zeros. They remain logically open, but their sign cannot be attributed to the simple positive self-adjoint relaxation theorem used here; the arithmetic selection and positivity would need an independent global explanation.

Third, an arbitrary nonrational transfer can be built with zeros at all `i gamma`. This is exactly why `WP-281` stopped at finite state. The present result does not close that analytic possibility. It shows only that the most canonical **positive** infinite-dimensional enlargement does not realize it. A zero set forced by a source-independent geometric symmetry would be different evidence; a zero set copied from `xi` would be circular.

Fourth, the growing-window logarithmic primitive of `WP-280` is not a fixed convolution kernel of the form (3). Its memory scale grows with `E`, and Suzuki's theorem gives the separate obstruction: the exact limiting Gamma extraction is RH-equivalent.

Fifth, nonlinear energies, determinants, quotients, or finite--archimedean couplings formed before the scalar residual (1) are outside this theorem. They remain subject to the line's usual bridge, sign, matched-control, and prior-art gates.

Finally, the result grants RH rather than deriving it. This is a deliberately favorable control: if the positive infinite-dimensional relaxation cannot isolate the already-known Gamma center even when every critical zero is placed exactly on the line, it cannot be the missing independent Weil-positivity mechanism by itself.

## 6. Prior-art and novelty boundary

Nothing is claimed as new about completely monotone kernels or Stieltjes responses. The Hausdorff--Bernstein--Widder theorem classically identifies completely monotone functions with Laplace transforms of positive measures. Schilling--Song--Vondracek give a standard modern treatment of completely monotone and Stieltjes function classes. Zemanian's 1974 `Relaxive Hilbert Ports` extends this positive-mixture representation to infinite-dimensional Hilbert-port systems and explicitly represents their frequency-domain system functions by Stieltjes transforms of positive operator measures.

A targeted literature search found these general representation theorems and passive/relaxive interpretations, but did not locate a zeta-specific theorem applying the strict positive-real boundary property to the critical weighted-Chebyshev almost-periodic residual. No novelty is claimed from that absence. The Mathia-specific contribution is the exact frontier combination: `WP-281` supplies a canonically regularized field with one nonzero Fourier--Bohr coefficient at every zeta-zero ordinate, while the positive relaxation representation forces every one of those coefficients to remain nonzero even in infinite dimension.

Accordingly this is a derived search-narrowing result, not a new theorem in control theory or analytic number theory.

## Consequence for `weil_positivity`

The category boundary after `WP-281` is now sharper. The missing architecture cannot be obtained merely by replacing a finite collection of stable boundary states with an arbitrary positive continuum of self-adjoint relaxation modes. Such a continuum is nonrational but still has a Stieltjes transfer with strictly positive real boundary values, so the critical zero screen survives intact while the Gamma DC mode is preserved.

The remaining infinite-dimensional escape must therefore be qualitatively different: an oscillatory/non-Stieltjes global response whose arithmetic structure is independently forced, a genuinely scale-nonlocal mechanism, a nonlinear sign-bearing construction, or a finite--archimedean coupling made before the zero field is scalarized. The burden remains the same one imposed by the canonical mandate: the geometry must generate both the arithmetic bridge and the sign without being tuned to the zero divisor or importing an RH-equivalent criterion.
