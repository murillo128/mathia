# Weil-positivity research lines

This file holds the current mathematical questions suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Find a non-scalar finite--archimedean sign mechanism before critical positive geometry collapses

**Linked intuitions:** `MI-039-enriched-semigroups-inherit-obstructed-scalar-shadows-or-universal-lifts` through `MI-052-rankin-selberg-positive-grams-die-at-the-weil-half-density`.

WP-356--WP-357 classify the finite constant-mode Hecke route: cusp-boundary defects reduce to universal interval-overlap/Brownian geometry, so finite arithmetic operator structure survives before positivity but becomes nonselective after positive closure.

WP-358 shows that nonconstant Fourier modes do retain genuine arithmetic information. For prime `p`, the angular range projection is exactly divisibility by `p`. Yet the sharp boundary square scalarizes that information to density `1/p`; the desired Weil coefficient has critical half-density `p^(-1/2)`. The canonical positive quadratic form therefore **squares the critical amplitude** rather than preserving it.

WP-359 closes the fixed smooth-height repair, WP-360 shows the all-prime critical amplitudes fail ordinary `l2` completion, and WP-361 shows that the globally correlated Eisenstein eigenline is maximally scalar: finite Hecke packets act through one multiplier and positive Maaß--Selberg averages pull back to another admissible scalar test.

WP-362 tests the canonical scalar analytic completion. The Eisenstein Hecke Dirichlet series is exactly `zeta(s+ir)zeta(s-ir)`, and its completed central value is a modulus square. Taking the logarithmic derivative recovers the exact Mangoldt half-density on every prime power, but simultaneously imports the zeta divisor as poles and loses inherited positivity.

WP-363 shows that moving from a one-parameter scalar completion to the canonical **two-parameter Rankin--Selberg Gram** does not repair the critical sign. For `s>1`,

`K_s(r,u)=sum_n lambda_r(n)lambda_u(n)n^(-s)`

is genuinely positive semidefinite and factors exactly into four zeta factors divided by `zeta(2s)`. At the Weil exponent `s=1/2`, the denominator pole forces the entire Gram kernel to vanish identically. Its first nonzero jet is entrywise nonnegative but indefinite, and the logarithmic derivative again exposes the desired linear Mangoldt half-density only after positivity has disappeared and the divisor has entered the meromorphic readout.

WP-364 closes the most canonical objection to that collapse: quotient out the common norm before continuation. The normalized projective overlap

`C_s(r,u)=K_s(r,u)/sqrt(K_s(r,r)K_s(u,u))`

cancels the universal `1/zeta(2s)` factor exactly for `s>1`, so projectivization genuinely removes WP-363's scalar zero without a hand-picked counterterm. But the critical continuation is

`C_*(r,u)=F(r+u)F(r-u)/(F(0)sqrt(F(2r)F(2u)))`, `F(t)=|zeta(1/2+it)|^2`.

Near any unconditional critical-line zero ordinate `gamma`, generic fixed `u` gives `|C_*(r,u)| -> infinity` as `r -> gamma/2` through regular points, violating the projective Cauchy--Schwarz bound `|C|<=1`. The Fubini--Study pullback gives the infinitesimal version: `g_*(r)=(log F)''(2r)-(log F)''(0) -> -infinity` near the same zero. Scalar Gamma/completion factors cannot repair either failure because projective geometry is invariant under nonzero scalar gauges.

The direct level-one Hecke/Eisenstein positivity route is therefore classified more tightly than before. It is not enough to remove the critical scalar collapse by normalization or intrinsic projectivization: the continued cross-parameter geometry itself ceases to be Hilbert-positive. A viable continuation must change the **nonseparable finite--archimedean geometry before critical specialization**—for example through a source-forced orthogonal feature sector, boundary response, intersection/cohomological form, or genuinely noncentral operator coupling—and must derive its sign independently of the divisor being constrained.

## Keep arithmetic content, convergence category, critical survival and sign coercivity separate

The current audit distinguishes finite Hecke algebra, nonconstant divisibility projections, smooth-orbit interference, strong all-prime completion, Eisenstein eigenline coherence, canonical Euler completion, Rankin--Selberg Gram positivity, critical collapse, first-jet indefiniteness, projective scalar removal, projective overlap blowup, negative Fubini--Study continuation and logarithmic-derivative divisor readout. Each stage retains some genuine arithmetic information, but none by itself supplies Weil positivity.

A proposal should therefore state where the critical `p^(-1/2)` or `(log p)p^(-1/2)` amplitude lives **before** positive closure, what completion/domain makes the object meaningful, which noncentral degrees of freedom survive at `s=1/2`, and what theorem fixes their orientation independently of the target RH sign. If the construction becomes a modulus square, a rank-one pullback, a `1/p` projection density, a kernel killed by `1/zeta(2s)`, an indefinite first jet, or a projective metric that turns negative at the critical specialization, it has crossed back into a classified nonselective closure.