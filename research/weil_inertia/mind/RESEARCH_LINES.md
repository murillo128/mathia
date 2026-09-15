# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Use one-signedness before relaxing to the full supported spectral bottom

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-025-gamma-pole-self-consistency-forces-a-global-l1-mass-floor`.

WI-284 says a completely screened one-signed first-crossing null mode `v>=0` satisfies `q_arch(v)=0`. WI-286--WI-293 studied the harder relaxation obtained by minimizing the prime-deleted form over all signed functions on the same support; that route exposed a negative odd pole direction and led to Lambert-width/rare-host conditions.

WI-294 restores the sign constraint of the actual null vector and shows that the positive pole term forces a positive support-measure floor. WI-295 makes that floor exact at the density-cap level. With its exact gamma bathtub profile `H(mu)`, complete one-signed screening forces `mu_*<|{v>0}|<=log 2`, and separated positive-support pieces at distance `R` pay an exponentially small product bound on their `L^1` masses.

WI-296 closes a second piece of the same geometry by retaining the actual global mass `s=||v||_1^2` in the bathtub rather than replacing it by support measure. The exact null identity and positive pole factorization force

`H(s)+2s<0`.

If `sigma_*=inf{u>0:H(u)+2u<0}`, every hypothetical candidate obeys

`mu_* < sigma_* < ||v||_1^2 <= |{v>0}| <= log 2`

and `P_a(v)>2 sigma_*`. Complete screening therefore requires a fixed positive **global `L^1` budget** in addition to positive support measure and the separated-mass tariff.

The live many-component question is now spatial: can a normalized first null mode place the forced global `L^1` mass in a bounded core while maintaining arbitrarily weak remote satellites compatible with every screening constraint, or can source-side regularity/tightness combine the global mass floor and exponential separated-mass tariff into an `L^2` contradiction? Bounded-aperture cases, sign-changing first modes and incomplete screening remain separate branches.

## Keep constrained null-vector geometry and unrestricted spectral relaxation separate

WI-286--WI-293 remain valid for the unrestricted supported spectral bottom and useful as diagnostics of the relaxation gap. WI-294--WI-296 show why they cannot be substituted for the actual one-signed null vector: the sign constraint makes the pole positive, the exact gamma bathtub forces both support and global `L^1` mass floors, and separated pieces face an exponential mass tariff.

The earlier rare-host estimates are no longer load-bearing for the large one-signed two-island contradiction. The missing step is not existence of global mass but a bridge from that mass plus the separated-mass tariff to the spatial `L^2` geometry of the normalized first null mode.