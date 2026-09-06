---
id: CLUE-xi-flow-gaussian-reference-quotient-localizes-heat-without-zero-seams
type: research-clue
status: accepted
origin: independent-review
target_line: xi_flow
based_on:
  - research/xi_flow/findings/XF-051-horizontal-log-derivative-renormalizes-infinite-volterra-transport.md
  - research/xi_flow/findings/XF-067-periodic-vieta-coordinates-diagonalize-the-full-zero-heat-flow.md
  - research/xi_flow/findings/XF-071-guarded-log-vieta-quotient-blocks-ultra-infrared-repopulation.md
  - research/xi_flow/findings/XF-072-period-dilation-trades-interface-suppression-for-local-frame-dilution.md
---

# Can an explicitly divided Gaussian reference replace arbitrary zero-block periodization?

## Observation

XF-072 shows that moving an arbitrary zero-periodization seam farther away does not improve its error after restoring the local frame normalization. A different construction can preserve the heat equation exactly at the function level, but it must explicitly remove auxiliary zeros rather than declaring every periodic root a Xi zero.

Let `u(z,s)` solve `u_s=-u_zz`; eventually take `u(z,s)=H_s(T+z)`. Choose `sigma>0`, let `0<=t<sigma^2/2`, and set

\[
h(t)=1-2t/\sigma^2,\qquad
V(z,t)=h^{-1/2}\exp\!\left(-\frac{z^2}{2\sigma^2h}\right)\nu(z/h,t/h).
\tag{1}
\]

Direct differentiation gives `V_t=-V_zz`. This is a classical Gaussian/Appell heat symmetry, not a new identity. The corresponding Gaussian reference

\[
W(z,t)=h^{-1/2}\exp\!\left(-\frac{z^2}{2\sigma^2h}\right)
\]

solves the same equation. When the sums and differentiated sums converge normally on the required complex domains, periodize **these solutions**, not a selected zero block:

\[
V_L(z,t)=\sum_{m\in\mathbb Z}V(z+mL,t),\qquad
W_L(z,t)=\sum_{m\in\mathbb Z}W(z+mL,t).
\]

Both remain exact periodic backward-heat solutions. The reference quotient `R_L=V_L/W_L`, on a domain where `W_L` is nonzero, satisfies the exact forced equation

\[
\boxed{(R_L)_t=-(R_L)_{zz}-2\frac{(W_L)_z}{W_L}(R_L)_z.}
\tag{2}
\]

The drift is known independently of Xi. More importantly, it is exponentially close to the affine drift removed by undoing (1). Put `v=sigma^2 h` and `a=exp(-L^2/(4v))`. On the entire vertical strip `|Re z|<=L/4`,

\[
\left|\frac{W_L}{W}-1\right|\le\frac{2a}{1-a}.
\]

For `a<1/3`, this proves `W_L` is nonzero there and gives the explicit bound

\[
\boxed{
\left|\frac{(W_L)_z}{W_L}+\frac z v\right|
\le\frac{2L}{v}\frac{a}{(1-a)(1-3a)}.
}
\tag{3}
\]

To verify (3), divide each image by the central Gaussian. Its modulus is `exp(-(m^2 L^2+2mL Re z)/(2v))<=a^{|m|}` on the strip; its logarithmic derivative relative to the central term is `-mL/v`. Sum the geometric series and its derivative, then divide by `1+sum(images)`. No lower bound on a Xi zero gap enters this reference estimate.

There is already a decisive negative control against the **undivided** construction. With `u=1`, every root of `V_L=W_L` is artificial. In fact

\[
W_L\left(\frac L2+i\frac{\pi v}{L},t\right)=0,
\]

because the terms with indices `m` and `-m-1` cancel. Thus Gaussian periodization creates non-real seam zeros even from a zero-free heat solution. These zeros can approach the real axis when `L/v` grows. They must be divided out or excluded by an explicitly controlled interior quotient; counting them as transition defects would be false.

## Research question

Can the known-reference equation (2), with the exponentially small non-affine drift (3), be connected to the guarded, destination-weighted log-Vieta or local analytic state without reintroducing the full-period `1/R` dilution in XF-072? The candidate is an **interior relative/logarithmic comparison with a known reference**, not a claim that an infinite Fourier series is the finite-degree carrier of XF-067.

The first missing source estimate is for `V_L/V-1` on the moving zero-free contour, including derivatives and its dependence on `T`, `L`, `sigma`, and positive heat time. The second is a stability theorem in the actual destination norm for the forced equation after removing the affine drift. A finite Fourier truncation must pay for omitted harmonics, auxiliary roots, and normalization by any retained outer carrier. An unbounded backward-heat operator on an arbitrary norm is not an admissible shortcut.

## Why it may matter

The artificial boundary force is no longer an unspecified consequence of how a zero block was continued. Part of it is an explicit theta/Gaussian reference with the proved candidate bound (3). This separates a controllable geometric error from the genuine Xi-dependent initial comparison and from the destination's stability cost. The Gaussian transformation is collision-safe at the function level and does not require all source roots to be real.

There is also an elementary route to a Gaussian source selector rather than insisting on a compact Fourier cutoff. For `sigma_0>1`, `w>0`, and `|omega|<=omega_0<log 2`, define

\[
A(Y,\omega)=\int_{\mathbb R}e^{-(y-Y)^2/(2w^2)}
\left(-\frac{\zeta'}\zeta(\sigma_0+iy)\right)e^{i\omega(y-Y)}\,dy.
\]

Absolute convergence of the Dirichlet series and the Gaussian transform give

\[
A(Y,\omega)=\sqrt{2\pi}w\sum_{n\ge2}\frac{\Lambda(n)}{n^{\sigma_0}}
 e^{-iY\log n}e^{-w^2(\log n-\omega)^2/2},
\]

hence the unconditional uniform bound

\[
\boxed{|A(Y,\omega)|\le\sqrt{2\pi}w
\left(-\frac{\zeta'}\zeta(\sigma_0)\right)
 e^{-w^2(\log 2-\omega_0)^2/2}.}
\tag{4}
\]

This controls the prime contribution only. The Gamma/elementary carrier must be subtracted in the actual Xi normalization; when using the Rodgers–Tao `z` coordinate, account explicitly for the factor of two in the ordinate and in the first prime frequency. Equation (4) does not control a periodized quotient or its transported state by itself.

## Decisive test

First independently verify (1)–(4), including heat sign, time reparametrization, differentiated normal convergence, and the exact artificial-zero control. Symbolic substitution into `(partial_t+partial_z^2)V` was performed for the collision polynomial `u(z,s)=z^2+b^2-2s` and for `u(z,s)=exp(omega^2 s+i omega z)`, yielding zero residuals. These checks do not replace the general chain-rule proof or establish a Xi estimate.

Then seek one parameter regime on the actual Xi moving-line source in which the Gaussian prime leakage, the **relative** periodization error, the drift contribution, and any finite-band amplification are all little-o of the destination signal **after its frame normalization**. Preserve the contour separation and explicitly control division by the reference. A useful first result is a source-normalized bound on `V_L/V-1`; an absolute exponentially small numerator is not enough when the denominator is also exponentially small.

Kill the proposed bridge if every admissible parameter choice loses the gain to the outer-carrier conditioning, backward-heat amplification, reference poles entering the relevant domain, or restored local-frame normalization. A positive result must still show that a hypothetical positive-Lambda Xi transition creates nonvanishing mass in the retained destination quotient; function-level localization alone does not prove that transition statement.

## Evidence boundary

This is a proposed source/transport bridge with elementary candidate calculations, not a proved Xi interface theorem. The heat symmetry is classical; see Amalia Torre, *Appell Transformation and Canonical Transforms*, SIGMA 7 (2011), 072, DOI 10.3842/SIGMA.2011.072. The source Gaussian estimate is standard Dirichlet-series/Fourier algebra. The line-specific question is whether reference division plus the quantified interior drift can bypass the exact seam/frame tradeoff while retaining source-faithful transition information. No new bound on Lambda, RH result, or global real-rootedness of the periodic surrogate is claimed.

## Research disposition

Accepted for active investigation. Independent reconstruction verifies the chain-rule Appell transform in (1), the quotient equation (2), the strip/nonvanishing estimate and logarithmic-drift bound (3), the explicit paired artificial zero of the undivided Gaussian periodization, and the Gaussian Dirichlet-series estimate (4). The literature check also confirms that the caloric Appell transformation and Gaussian/theta heat-kernel structure are classical; no novelty is assigned to those ingredients.

The proposal is not blocked by XF-072's aspect-ratio obstruction because it changes the localization architecture rather than merely enlarging the period of a selected zero block: it periodizes exact heat solutions and removes a known reference before asking for an interior relative estimate. The precise unresolved gate is now to prove a source-normalized Xi bound for `V_L/V-1` and its needed derivatives on a moving zero-free contour, together with stability of the forced quotient in the destination-weighted norm, in one parameter regime where reference drift, prime leakage, finite-band amplification, and normalization losses are all `o(1)`. Positive-`Lambda` transition nontriviality in that quotient remains a separate downstream obligation. Acceptance records only that this route is technically coherent and worth pursuing, not that those Xi-specific estimates hold.