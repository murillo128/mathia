# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Reduce the one-signed complete-screening branch to strict positivity at the first-prime aperture

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-027-rearrangement-collapses-one-signed-complete-screening-to-the-first-prime-aperture`.

WI-284 says a completely screened one-signed first-crossing null mode satisfies the prime-deleted identity `q_arch(v)=0`. WI-294--WI-297 then use positivity of the pole term to force support measure, global `L^1` mass, exponential-moment control and an aperture-independent `L^2` core.

WI-298 makes the branch substantially simpler. Complete screening by the first-prime powers gives support measure at most `log 2`. Symmetric decreasing rearrangement compresses any nonnegative screened mode into radius `r_2=(log 2)/2`, decreases the gamma part, preserves the pole term, and makes all prime-power translations vanish. Hence the rearranged test satisfies

`Q_W^(r_2)(v^*)<=0`.

If `v` is the first unrestricted crossing mode, firstness therefore forces `a_*<=r_2`. The former large-aperture remote-satellite/local-to-global problem is no longer load-bearing for the completely screened one-signed branch: rearrangement eliminates it before tail propagation is needed.

The live theorem is now sharply finite-scale. Prove a rigorous strict bound

`lambda_(r_2)>0`

for the exact supported Weil form. That single certificate would rule out the entire one-signed complete-screening first-crossing branch. Any numerical or computer-assisted candidate must be independently certified at the exact aperture; an uncertified nearby bound is not evidence for the required sign.

## Keep constrained null-vector geometry, rearrangement and unrestricted spectral relaxation separate

WI-286--WI-293 remain valid diagnostics for the unrestricted supported spectral bottom, while WI-294--WI-297 explain why that relaxation cannot replace the actual nonnegative null vector. WI-298 adds a different structural operation: rearrangement is useful here because the prime-deleted gamma-plus-pole form moves monotonically in the favorable direction and complete screening supplies an exact support-packing bound.

This conclusion is branch-specific. It does not transfer to sign-changing modes, incomplete screening, or arbitrary supported spectral minimizers. For those branches coefficient sign, residual prime overlaps and support geometry remain live variables.