# Weil-positivity research lines

This file holds the current mathematical questions suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Find a global finite--archimedean sign mechanism beyond diagonal scale traps and local scalar Toeplitz completion

**Linked intuitions:** `MI-039-enriched-semigroups-inherit-obstructed-scalar-shadows-or-universal-lifts` through `MI-055-centered-prime-power-toeplitz-positivity-pays-a-divergent-diagonal-tax`.

WP-356--WP-357 classify the finite constant-mode Hecke route: cusp-boundary defects reduce to universal interval-overlap/Brownian geometry, so finite arithmetic operator structure survives before positivity but becomes nonselective after positive closure.

WP-358 shows that nonconstant Fourier modes retain genuine arithmetic information. For prime `p`, the angular range projection is exactly divisibility by `p`. Yet the sharp boundary square scalarizes that information to density `1/p`; the desired Weil coefficient has critical half-density `p^(-1/2)`. The canonical positive quadratic form therefore squares the critical amplitude rather than preserving it.

WP-359--WP-365 classify scalar/smooth and Rankin--Selberg repairs. The desired Mangoldt half-density can be recovered by importing the completed logarithmic derivative, but inherited positivity is lost; canonical finite and finite--archimedean positive Grams either vanish, diverge or acquire indefinite critical geometry.

WP-366--WP-370 classify componentwise Whittaker scale repairs. Common positive homogeneous globalization Mellin-separates the finite--archimedean construction; a bounded fixed scale preserves incidence only while the Whittaker tail kills large indices; moving `Y_n=c n^(-alpha)` has one unsuppressed critical power `alpha=1`, but there `nY_n=c` is constant and the carrier factorizes. Exact diagonal prime-Hecke equivariance itself forces the same law `Y_n=c/n`. Ordinary positive boundary `L^2` then squares the half-density to `|lambda_r(n)|^2/n` and diverges.

WP-371 tests the most canonical translation-invariant non-diagonal repair. On a prime-power ray let

`C_r=sum_(k>=1) r^k(U^k+U^(-k))`, `r=p^(-1/2)`.

Its nonzero Fourier coefficients are exactly the critical prime-power half-density pattern after multiplication by `log p`. But `C_r` is the **centered** Poisson kernel, with symbol minimum `-2r/(1+r)`, so it is indefinite. More strongly, every scalar diagonal completion preserving those nonzero coefficients,

`a I + C_r`,

is positive if and only if

`a >= 2r/(1+r)`.

At prime `p`, the least positive-completion tax is therefore

`2 log p/(sqrt(p)+1)`,

and its sum over primes diverges. The ordinary positive Poisson kernel pays an even larger diagonal. Subtracting this accumulated zero mode after applying local positivity simply reintroduces an indefinite counterterm outside the sign theorem.

The surviving operator-valued route is consequently stricter than “couple different translates before squaring.” A viable form must assemble finite primes with an archimedean/global sector, or use a genuinely matrix/cross-prime/source-constrained operator, **before positivity is asserted**, so that the divergent local diagonal direction is cancelled or quotiented inside one source-forced global sign structure. A direct sum of independently positive local Poisson blocks followed by baseline subtraction is closed.

## Keep arithmetic content, local positivity, tensorization, scale globalization, Hecke naturality, diagonal tax and critical sign coercivity separate

The current audit distinguishes finite Hecke structure, nonconstant divisibility projections, finite--archimedean incidence, common versus cross-index radial geometry, exact dilation homogeneity, fixed-scale boundedness, cusp approach rate, transition coordinate `nY`, arithmetic-index tail size, diagonal Hecke intertwining, critical half-density, diagonal Hilbert squaring, translation-invariant prime-power coupling, zero-mode completion cost and sign coercivity.

WP-365--WP-371 show that seeing the right `n^(-1/2)` or `p^(-k/2)` coefficient is not enough. One must ask which mixed coordinate still carries source-specific incidence, which naturality law generated the scale, what positivity adds on the diagonal, and whether a local positive completion survives global assembly without an infinite counterterm. At the critical Whittaker ray the mixed coordinate freezes; at the critical Toeplitz ray the desired carrier is precisely the centered indefinite part of a positive harmonic kernel.

Any next proposal should state where the `(log p)p^(-1/2)` carrier lives before closure, how finite and archimedean sectors are coupled, which diagonal/zero-mode directions are quotiented or compensated, why that compensation is intrinsic rather than a post-hoc subtraction, and what theorem fixes the required orientation independently of the divisor being constrained. More elaborate componentwise positivity, diagonal Hecke-equivariant sampling, or scalar prime-by-prime Toeplitz completion is now calibration rather than a new route.
