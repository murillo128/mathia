---
id: CLUE-analytic-frontier-gaussian-xi-source-periodization-relative-error
type: research-clue
status: proposed
origin: independent-review
target_line: analytic_frontier
based_on:
  - research/xi_flow/findings/XF-072-period-dilation-trades-interface-suppression-for-local-frame-dilution.md
  - research/xi_flow/clues/CLUE-gaussian-reference-quotient-localizes-heat-without-zero-seams.md
---

# Does a relative Gaussian Xi periodization estimate supply the missing source interface?

## Observation

The destination line needs a source-faithful interior comparison, not an absolute approximation whose denominator is exponentially small. This clue states the transferred question independently; the Xi paths in `based_on` are provenance, not required reading for the destination watch.

In the Rodgers–Tao coordinate, `H_0(z)` is a nonzero constant multiple of `xi(1/2+i z/2)`. Fix `sigma_0>1`, put `a=2 sigma_0-1`, and use the source contour `z=x+i a`. By the functional equation, the relevant xi argument is `sigma_0-i(T+x)/2`. Define

\[
U_T(z)=H_0(T+z),\qquad
V(z)=e^{-z^2/(2w^2)}U_T(z),\qquad
V_L(z)=\sum_{m\in\mathbb Z}V(z+mL).
\]

There is a direct candidate **relative** estimate at this fixed source line. For fixed `sigma_0>1`, Euler-product/Dirichlet-series bounds give

\[
\zeta(\sigma_0)^{-1}\le|\zeta(\sigma_0+i y)|\le\zeta(\sigma_0).
\]

Combining these with the xi prefactor and two-sided Stirling bounds, extended over bounded `y` by continuity, gives constants depending only on `sigma_0` such that

\[
|\xi(\sigma_0+i y)|\asymp_{\sigma_0}
(1+|y|)^p e^{-\pi|y|/4},\qquad
p=(\sigma_0+3)/2.
\tag{1}
\]

In particular, uniformly in real `T,x` and integer `m`,

\[
\left|\frac{U_T(x+mL+i a)}{U_T(x+i a)}\right|
\le C_{\sigma_0}(1+|m|L)^p e^{\pi|m|L/8}.
\tag{2}
\]

The denominator is nonzero because the reflected argument has real part greater than one. No assumption about critical-line zeros is needed.

For `|x|<=L/4`, the Gaussian image ratio satisfies

\[
\left|\exp\!\left(-\frac{(z+mL)^2-z^2}{2w^2}\right)\right|
\le e^{-m^2L^2/(4w^2)}\qquad(m\ne0).
\]

Therefore

\[
\boxed{
\left|\frac{V_L(x+i a)}{V(x+i a)}-1\right|
\le 2C_{\sigma_0}\sum_{m\ge1}(1+mL)^p
\exp\!\left(-\frac{m^2L^2}{4w^2}+\frac{\pi mL}{8}\right).
}
\tag{3}
\]

If `L>=pi w^2`, this is bounded by

\[
\boxed{2C_{\sigma_0}\sum_{m\ge1}(1+mL)^p
 e^{-m^2L^2/(8w^2)}.}
\tag{4}
\]

For example, at fixed `sigma_0`, taking `w=log T` and `L=(log T)^3` gives a super-polynomially small error in `log T`: the leading exponential is `exp(-(log T)^4/8)` and the prefactor is only polynomial in `log T`. This is an initial-source-line comparison, not a transported Xi theorem. Constants cannot be treated as fixed when `sigma_0` is allowed to move with `T`.

## Research question

Can (1)–(4) be independently established with the explicit uniformity and derivative control needed by a moving-line Xi selector, and then expressed in its normalized weighted source norm? In particular, determine a compatible moving `sigma_0(T)`, contour thickness, Gaussian width, and period for which the full relative/logarithmic comparison remains little-o after the destination frame normalization.

On a fixed contour neighborhood staying inside the reflected half-plane `Re s>1`, Cauchy estimates should transfer a uniform analytic bound for `V_L/V-1` to any fixed number of derivatives, after shrinking the interior horizontal interval. The necessary uniformity over that neighborhood must be proved; a pointwise bound on one line alone is insufficient.

## Why it may matter

This calculation uses the actual Euler product and Gamma factor rather than a generic zero-counting envelope. The exponentially small quantity is already relative to the original Xi function, so it does not hide an exponentially small denominator. It supplies a plausible source-side entry into a construction that periodizes a heat-compatible Gaussian transform and divides out a known Gaussian reference.

The reference division is essential. Even periodizing a bare Gaussian creates auxiliary non-real zeros near the artificial seam. Those zeros must not be counted as Xi transition defects. The source estimate here only compares the interior analytic functions; the dynamical line must separately prove stability of its reference-divided state and preserve the relevant transition signal.

## Decisive test

Re-derive the xi prefactor power `p=(sigma_0+3)/2` and the exponential shift cost `pi |m|L/8` in the stated `z/2` normalization. Prove normally convergent image and differentiated-image sums and obtain constants on a nonzero-width source strip. Then track the actual dependence on `sigma_0(T)` rather than importing a fixed-strip asymptotic without uniformity.

For the prime part of the selector, a Gaussian window of width `w` has the exact elementary bound, uniformly in ordinate center `Y` and `|omega|<=omega_0<log 2`,

\[
\left|\int_{\mathbb R}e^{-(y-Y)^2/(2w^2)}
\left(-\frac{\zeta'}\zeta(\sigma_0+i y)\right)e^{i\omega(y-Y)}dy\right|
\le\sqrt{2\pi}w\left(-\frac{\zeta'}\zeta(\sigma_0)\right)
 e^{-w^2(\log 2-\omega_0)^2/2}.
\tag{5}
\]

This follows by integrating the absolutely convergent von Mangoldt Dirichlet series term by term. Subtract the Gamma/elementary carrier explicitly and convert the ordinate frequency to the `z/2` convention; its first prime frequency is then `log 2/2`. Check that replacing a compact Fourier cutoff by this Gaussian leakage does not change the required coercivity or support hypothesis without payment.

A positive outcome is one explicit source-normalized theorem on compatible scales. A negative outcome is a demonstrated incompatibility of the moving contour, relative image cost, source leakage, or destination conditioning. Neither outcome requires proving the full heat transport here.

## Evidence boundary

Equations (1)–(5) are candidate derivations included for independent reconstruction, not an accepted line finding or a certified explicit-constant computation. The fixed-half-plane inputs are classical: the xi functional equation and Euler-product bounds, together with the Gamma asymptotics in NIST DLMF sections 25.2, 25.4, and 5.11. No novelty is claimed for those ingredients. The proposed line-specific gain is the source-faithful relative periodization bound and its compatibility with a heat-localization construction.

No bound for positive-time `H_t` is inferred from the Euler product of `H_0`. In particular, no positive-time Euler product is assumed. The reference-divided heat transport, finite-band or analytic stability, and the implication from a positive-Lambda transition to a nonvanishing retained destination state remain separate unproved steps. Even a successful estimate (4) does not close them.
