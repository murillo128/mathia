# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Use one-signedness before relaxing to the full supported spectral bottom

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-024-one-signed-complete-screening-imposes-a-support-measure-floor`.

WI-284 says a completely screened one-signed first-crossing null mode `v>=0` satisfies `q_arch(v)=0`. WI-286--WI-293 studied the harder relaxation obtained by minimizing the prime-deleted form over **all signed functions** on the same support; that route exposed a negative odd pole direction and led to Lambert-width/rare-host conditions.

WI-294 restores the sign constraint of the actual null vector and changes the asymptotic frontier. For nonzero `v>=0`, the pole term is strictly positive. Therefore `q_arch(v)=0` forces the gamma contribution negative. The support-measure uncertainty bound from WI-287 then gives an absolute floor

`|{v>0}| > mu_0 > 0`.

For symmetric two-island complete screening, the prime number theorem alone forces the island width, hence total support measure, to tend to zero at large aperture. This contradicts the floor. The large one-signed completely screened two-island branch is therefore closed without a Cramér-scale prime-gap theorem or rare-host incidence estimate.

The live complete one-signed question is now topological/measure-theoretic: can any many-component support retain a fixed positive total measure while avoiding every active prime-power translation and satisfying the null equation? Bounded-aperture two-island cases, sign-changing first modes and incomplete screening remain separate branches.

## Keep constrained null-vector geometry and unrestricted spectral relaxation separate

WI-286--WI-293 remain valid for the unrestricted supported spectral bottom and useful as diagnostics of the relaxation gap. WI-293 also remains a provenance warning: an unverified prime-gap headline cannot be imported merely because it would close a relaxed branch. But those rare-host estimates are no longer load-bearing for the large **one-signed** symmetric two-island contradiction after WI-294.
