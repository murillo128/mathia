# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Validate the L=0.8 compact-window certificate before spending more effort on the first-prime endpoint certificate

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-027-rearrangement-collapses-one-signed-complete-screening-to-the-first-prime-aperture`.

WI-284 says a completely screened one-signed first-crossing null mode satisfies the prime-deleted identity `q_arch(v)=0`. WI-294--WI-297 then use positivity of the pole term to force support measure, global `L^1` mass, exponential-moment control and an aperture-independent `L^2` core.

WI-298 makes the branch substantially simpler. Complete screening by the first-prime powers gives support measure at most `log 2`. Symmetric decreasing rearrangement compresses any nonnegative screened mode into radius `r_2=(log 2)/2`, decreases the gamma part, preserves the pole term, and makes all prime-power translations vanish. Hence the rearranged test satisfies

`Q_W^(r_2)(v^*)<=0`.

If `v` is the first unrestricted crossing mode, firstness therefore forces `a_*<=r_2`. WI-299 removes the smooth-kernel domain gap: its residual estimate is valid throughout `a<=r_2`, so the analytic tail is no longer the obstruction to an endpoint certificate.

WI-300 changes the shortest verification target. Zhu's recent compact-window preprint reports a certified all-complex lower bound

`Q(f) >= 8.9e-18 ||f||_2^2`

for every `f` supported in `[-0.8,0.8]`. The form dictionary in WI-300 identifies this theorem surface with Suzuki's localized Weil form. **If the published v2 certificate is independently replayed and validated**, then `lambda_0.8>0`; monotonicity gives `a_*>0.8`, contradicting the exact complete-screening requirement `a_*<=r_2<0.8`. One validated certificate would therefore eliminate the entire one-signed completely screened first-crossing branch without separately proving `lambda_(r_2)>0`.

The current evidence boundary is crucial: WI-300 establishes this implication and the dictionary, not the numerical certificate itself as independently verified Mathia evidence. The live theorem is therefore the bounded replay/audit of the `L=0.8` certificate — matrix construction, quadrature enclosure, tail/coupling estimates, verified positive-definiteness step, parity extension and normalization — rather than further optimization of the first-prime endpoint architecture. If the replay fails, `lambda_(r_2)>0` remains the independent fallback target supplied by WI-298--WI-299.

## Keep structural reduction, external/computer-assisted positivity and unrestricted Weil positivity separate

WI-286--WI-293 remain valid diagnostics for the unrestricted supported spectral bottom, while WI-294--WI-297 explain why that relaxation cannot replace the actual nonnegative null vector. WI-298 adds a structural reduction by rearrangement, and WI-299 adds a uniform analytic tail estimate through the exact first-prime aperture.

WI-300 introduces a different kind of input: a finite computer-assisted compact-window positivity theorem from recent prior art. Its usefulness is branch-specific because WI-298 has already reduced complete one-signed screening to a finite threshold contradiction. Even a validated `lambda_0.8>0` would not prove unrestricted positivity at larger apertures, would not address sign-changing or incompletely screened first-crossing modes, and would not make the pointwise-envelope certificate architecture scalable to RH.

The program should therefore keep three statements distinct: the exact rearrangement theorem that forces the screened branch below `r_2`; the independent validity of the fixed `L=0.8` numerical certificate; and any theorem about the unrestricted large-aperture Weil form. The first is current canonical evidence, the second is the decisive verification gate exposed by WI-300, and the third remains a much broader problem.
