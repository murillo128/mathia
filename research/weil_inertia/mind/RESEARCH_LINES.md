# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Use one-signedness before relaxing to the full supported spectral bottom

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-024-one-signed-complete-screening-imposes-a-support-measure-floor`.

WI-284 says a completely screened one-signed first-crossing null mode `v>=0` satisfies `q_arch(v)=0`. WI-286--WI-293 studied the harder relaxation obtained by minimizing the prime-deleted form over all signed functions on the same support; that route exposed a negative odd pole direction and led to Lambert-width/rare-host conditions.

WI-294 restores the sign constraint of the actual null vector and shows that the positive pole term forces a positive support-measure floor. WI-295 makes that floor exact at the density-cap level. With

`H(mu)=(mu/(2pi)) int_(-pi/mu)^(pi/mu) [Re psi(1/4+iz/2)-log pi] dz`,

the exact gamma multiplier makes `H` strictly decreasing with one positive zero `mu_*`, and complete one-signed screening forces

`mu_*<|{v>0}|<=log 2`.

WI-295 also adds an amplitude constraint unavailable to support packing alone. If two positive-support pieces are separated by distance `R`, their `L^1` masses obey

`M_1(A)M_1(B) < -H(mu)/(4 cosh(R/2))`.

Thus large separation forces exponential amplitude imbalance. Remote satellites can preserve total support measure only by becoming weak in `L^1` relative to the rest of the null vector.

The live complete one-signed question is now quantitative rather than merely topological: can many-component complete screening reconcile the fixed positive support-measure budget with the exponential separated-mass tariff and `L^2` normalization, or can source-side regularity convert that tariff into a contradiction? Bounded-aperture cases, sign-changing first modes and incomplete screening remain separate branches.

## Keep constrained null-vector geometry and unrestricted spectral relaxation separate

WI-286--WI-293 remain valid for the unrestricted supported spectral bottom and useful as diagnostics of the relaxation gap. WI-294--WI-295 show why they cannot be substituted for the actual one-signed null vector: the sign constraint makes the pole positive, which in turn forces both negative gamma energy and a support/amplitude budget.

The earlier rare-host estimates are no longer load-bearing for the large one-signed two-island contradiction, and support topology alone is no longer the full frontier for many-component escapes. The missing step is a bridge from the exact `L^1` separated-mass tariff plus positive support measure to the `L^2` geometry of the normalized first null mode.
