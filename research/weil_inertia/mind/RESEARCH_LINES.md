# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Use one-signedness and pole dispersion before relaxing to the full supported spectral bottom

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-026-pole-mgf-self-consistency-forces-an-aperture-independent-l2-core`.

WI-284 says a completely screened one-signed first-crossing null mode `v>=0` satisfies `q_arch(v)=0`. WI-286--WI-293 studied the harder relaxation obtained by minimizing the prime-deleted form over all signed functions on the same support; that route exposed a negative odd pole direction and led to Lambert-width/rare-host conditions.

WI-294 restores the sign constraint of the actual null vector and shows that the positive pole term forces a positive support-measure floor. WI-295 makes that floor exact at the density-cap level. WI-296 retains the actual global mass `s=||v||_1^2` in the same bathtub and forces

`H(s)+2s<0`,

hence a fixed positive global `L^1` budget `s>sigma_*` in addition to the support floor and separated-mass tariff.

WI-297 now retains the exponential-moment imbalance that WI-296 discarded. For the probability law `dnu=v(x)dx/||v||_1`, complete screening gives

`E exp(X/2) E exp(-X/2) < kappa_*`,

so `Var_nu(X)<4(kappa_*-1)` and the normalized `L^1` measure has uniform exponential tails after recentering. A fixed interval of aperture-independent radius captures more than half of the `L^1` mass and at least a universal `q_*>0` of the normalized `L^2` mass.

The sparse-satellite escape is therefore no longer a question of whether the global mass can remain in a bounded core: a nonvanishing core is forced. The live theorem is **local-to-global propagation**. Can the exact first-crossing/null identities force a fixed positive amount of `L^1` or `L^2` mass to cross successive distant cuts when the mode has full essential span? Any such propagation law would collide with the exponential pole-tail budget and close the one-signed complete-screening branch. Bounded aperture, sign-changing first modes and incomplete screening remain separate.

## Keep constrained null-vector geometry and unrestricted spectral relaxation separate

WI-286--WI-293 remain valid for the unrestricted supported spectral bottom and useful as diagnostics of the relaxation gap. WI-294--WI-297 show why they cannot be substituted for the actual one-signed null vector: positivity of the pole yields support and global-mass floors, and the full pole MGF further forces variance/tail control and an aperture-independent `L^2` core.

The earlier rare-host estimates are no longer load-bearing for the large one-signed branch. The missing step is not another scalar uncertainty bound but a source-specific propagation theorem connecting the forced core to the distant support required by firstness/full span.