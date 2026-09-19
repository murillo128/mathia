# Weil-positivity research lines

This file holds the current mathematical questions suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Find a genuinely noncentral finite--archimedean sign mechanism beyond componentwise and Hecke-equivariant Whittaker scale traps

**Linked intuitions:** `MI-039-enriched-semigroups-inherit-obstructed-scalar-shadows-or-universal-lifts` through `MI-054-index-adapted-whittaker-sampling-has-one-critical-scale-and-it-factorizes`.

WP-356--WP-357 classify the finite constant-mode Hecke route: cusp-boundary defects reduce to universal interval-overlap/Brownian geometry, so finite arithmetic operator structure survives before positivity but becomes nonselective after positive closure.

WP-358 shows that nonconstant Fourier modes retain genuine arithmetic information. For prime `p`, the angular range projection is exactly divisibility by `p`. Yet the sharp boundary square scalarizes that information to density `1/p`; the desired Weil coefficient has critical half-density `p^(-1/2)`. The canonical positive quadratic form therefore squares the critical amplitude rather than preserving it.

WP-359--WP-365 classify scalar/smooth and Rankin--Selberg repairs. The desired Mangoldt half-density can be recovered by importing the completed logarithmic derivative, but inherited positivity is lost; canonical finite and finite--archimedean positive Grams either vanish, diverge or acquire indefinite critical geometry.

WP-366 retains genuine finite--archimedean incidence at fixed physical height through `lambda_r(n)K_(ir)(2 pi nY)`, but canonical positive scalar dilation-covariant globalization forces a power-Haar measure and Mellin-separates the construction back into Rankin--Selberg/Bessel geometry. WP-367 broadens this to any common positive-semidefinite radial form with exact dilation homogeneity. WP-368 closes the opposite fixed-scale escape: a bounded positive readout supported on `Y>=Y_*>0` preserves literal `nY` incidence only while the Whittaker tail exponentially erases large arithmetic indices.

WP-369 tests the natural remaining repair: move the source height toward the cusp with the Fourier index. For normalized modes

`w_(r,n)(Y_n)=lambda_r(n)n^(-1/2) Psi_r(nY_n)`.

For the power law `Y_n=c n^(-alpha)`, there is a sharp trichotomy. If `alpha<1`, the formal half-density is killed by stretched-exponential Whittaker decay. If `alpha>1`, the amplitude is subcritical (up to one logarithm at `r=0`). The unique unsuppressed critical power law is `alpha=1`, but then `nY_n=c` is constant and the finite--archimedean incidence factorizes exactly:

`w_(r,n)(c/n)=B_r(c) lambda_r(n)n^(-1/2)`.

Ordinary positive boundary `L^2` then squares the half-density to `|lambda_r(n)|^2/n` and the resulting Rankin--Selberg sum diverges.

WP-370 now tests whether the intrinsic Hecke correspondence can **force** a more interesting nonconstant transition sequence. For a diagonal sampler `(R_Ya)_n=a_n(Y_n)`, exact intertwining with every prime Hecke operator on the smooth finite-Fourier cusp core,

`R_Y T_p = H_p R_Y`,

holds if and only if

`Y_(pm)=Y_m/p`.

Equivalently `t_(pm)=t_m` for `t_n=nY_n`; prime factorization therefore forces `Y_n=c/n` and `t_n=c`. Hecke naturality selects exactly the critical ray of WP-369 and simultaneously freezes the mixed coordinate. The sampled Whittaker mode factorizes, and ordinary positive boundary `L^2` returns to the same divergent `|lambda_r(n)|^2/n` geometry.

The route is now trapped by four complementary componentwise failures: **common homogeneous globalization erases incidence; fixed bounded scale preserves incidence but kills the tail; pure power-law index adaptation has one critical scale and that scale factorizes; and exact diagonal Hecke equivariance itself forces that same factorized critical ray.** A source-forced nonconstant transition sequence must therefore break exact diagonal Hecke equivariance or arise from a genuinely cross-index/operator-valued construction whose naturality and sign theorem are formulated at a different level.

## Keep arithmetic content, local positivity, tensorization, scale globalization, Hecke naturality, tail survival and critical sign coercivity separate

The current audit distinguishes finite Hecke structure, nonconstant divisibility projections, finite--archimedean incidence, common versus cross-index radial geometry, exact dilation homogeneity, fixed-scale boundedness, cusp approach rate, the transition coordinate `nY`, arithmetic-index tail size, diagonal Hecke intertwining, critical half-density, diagonal Hilbert squaring and sign coercivity.

WP-365--WP-370 show that seeing the right `n^(-1/2)` prefactor is not enough. One must ask whether the remaining Whittaker profile still carries source-specific incidence, whether the scale law was source-forced rather than chosen to fit the desired exponent, what naturality requirement generated that law, and what positivity does after the half-density is exposed. At `Y_n=c/n`, the exponent is correct but the mixed coordinate is constant and the canonical positive norm is both quadratic and divergent; WP-370 shows that exact prime-Hecke equivariance does not supply a richer diagonal section, because it forces precisely that ray.

Any next proposal should state where the `(log p)p^(-1/2)` carrier lives before closure, how `t_n=nY_n` is generated, which Hecke covariance is required or deliberately broken, what cross-index degrees of freedom survive, whether the form remains finite, and what theorem fixes the required orientation independently of the divisor being constrained. More elaborate componentwise positivity on a homogeneous global scale, a bounded fixed scale, a pure power-law moving scale, or an exactly Hecke-equivariant diagonal sampler is now calibration rather than a new route.
