# Weil-positivity research lines

This file holds the current mathematical questions suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Find a genuinely noncentral finite--archimedean sign mechanism that survives both globalization and fixed-scale suppression

**Linked intuitions:** `MI-039-enriched-semigroups-inherit-obstructed-scalar-shadows-or-universal-lifts` through `MI-053-fixed-positive-whittaker-scale-exponentially-suppresses-arithmetic-index`.

WP-356--WP-357 classify the finite constant-mode Hecke route: cusp-boundary defects reduce to universal interval-overlap/Brownian geometry, so finite arithmetic operator structure survives before positivity but becomes nonselective after positive closure.

WP-358 shows that nonconstant Fourier modes retain genuine arithmetic information. For prime `p`, the angular range projection is exactly divisibility by `p`. Yet the sharp boundary square scalarizes that information to density `1/p`; the desired Weil coefficient has critical half-density `p^(-1/2)`. The canonical positive quadratic form therefore squares the critical amplitude rather than preserving it.

WP-359--WP-365 classify scalar/smooth and Rankin--Selberg repairs. The desired Mangoldt half-density can be recovered by importing the completed logarithmic derivative, but inherited positivity is lost; canonical finite and finite--archimedean positive Grams either vanish, diverge or acquire indefinite critical geometry.

WP-366 retains genuine finite--archimedean incidence at fixed physical height through `lambda_r(n)K_(ir)(2 pi nY)`, but canonical positive scalar dilation-covariant globalization forces a power-Haar measure and Mellin-separates the construction back into Rankin--Selberg/Bessel geometry. WP-367 broadens this: any common positive-semidefinite radial form applied componentwise with exact dilation homogeneity factors the finite cutoff into an archimedean scalar times the same finite Rankin--Selberg kernel. At critical half-density its diagonal is null or divergent.

WP-368 now closes the most obvious opposite escape. Keep a fixed source scale away from the cusp so that `nY` incidence survives, and apply an arbitrary **bounded positive operator** there. The Whittaker tail then gives an exponential arithmetic-index bound of the form

`q_A(F_(r,n)) <= C_(r,A,Y_*) n^(-1) exp(-4 pi (n-1)Y_*)`

for support bounded below by `Y_*>0`. Polynomial or logarithmic Hecke factors cannot compensate for that decay, and the same suppression persists in cross-spectral pairings. A bounded fixed-scale positive readout therefore preserves incidence only by exponentially erasing the large arithmetic indices whose half-density is needed by the Weil criterion.

The route is now trapped between two exact positive failures. **Exact common scale globalization loses finite--archimedean incidence; bounded positive localization away from the cusp keeps incidence but kills the arithmetic tail exponentially.** A viable construction must break at least one premise on both sides: couple Fourier index to scale so the support can approach `Y=0`, use an unbounded but canonically controlled positive form, introduce cross-index/cohomological/intersection structure, or provide another sign theorem that does not reduce to either componentwise regime.

## Keep arithmetic content, local positivity, tensorization, scale globalization, tail survival and critical sign coercivity separate

The current audit distinguishes finite Hecke structure, nonconstant divisibility projections, finite--archimedean incidence, common versus cross-index radial geometry, exact dilation homogeneity, fixed-scale boundedness, proximity to the cusp, arithmetic-index tail size, critical overlap blowup and sign coercivity.

WP-365 removes the objection that the previous failure came from omitting archimedean Hilbert geometry. WP-366 removes the objection that literal `nY` coupling by itself survives canonical scalar averaging. WP-367 removes the broader objection that one merely needs a more sophisticated common positive radial norm. WP-368 removes the mirror objection that one can simply refuse globalization and keep a bounded positive source-localized scale: that retains the coupling but suppresses the high-index carrier exponentially.

A proposal should therefore state where the critical `p^(-1/2)` or `(log p)p^(-1/2)` amplitude lives before positive closure, how the auxiliary scale depends on Fourier index, whether the form is bounded on the retained scale, what happens as support approaches the cusp, which non-product degrees of freedom survive, and what theorem fixes their orientation independently of the divisor being constrained. More elaborate componentwise positivity on either a homogeneous global scale or a bounded fixed scale is now classified rather than a new route.