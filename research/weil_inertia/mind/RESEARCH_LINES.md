# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Reduce the one-signed complete-screening branch to a finite low-mode positivity certificate at the first-prime aperture

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-027-rearrangement-collapses-one-signed-complete-screening-to-the-first-prime-aperture`.

WI-284 says a completely screened one-signed first-crossing null mode satisfies the prime-deleted identity `q_arch(v)=0`. WI-294--WI-297 then use positivity of the pole term to force support measure, global `L^1` mass, exponential-moment control and an aperture-independent `L^2` core.

WI-298 makes the branch substantially simpler. Complete screening by the first-prime powers gives support measure at most `log 2`. Symmetric decreasing rearrangement compresses any nonnegative screened mode into radius `r_2=(log 2)/2`, decreases the gamma part, preserves the pole term, and makes all prime-power translations vanish. Hence the rearranged test satisfies

`Q_W^(r_2)(v^*)<=0`.

If `v` is the first unrestricted crossing mode, firstness therefore forces `a_*<=r_2`. The former large-aperture remote-satellite/local-to-global problem is no longer load-bearing for the completely screened one-signed branch: rearrangement eliminates it before tail propagation is needed.

WI-299 removes the remaining smooth-kernel domain gap. Its exact defect estimate is valid for the full first-prime aperture `|s|<=log 2` and gives `||R_a||<=0.353143 a^2` for every `a<=r_2`. Thus the analytic tail estimate itself reaches the structural endpoint; sharpening that tail further is not the live theorem unless it changes the finite certificate.

The live theorem is now sharply finite-scale: prove a rigorous strict bound

`lambda_(r_2)>0`

for the exact supported Weil form by certifying the remaining low-mode/interval-Schur block at the endpoint. A nearby numerical sign or an uncertified extension from `a<r_2` is not evidence for the required positivity. That single exact-aperture certificate would rule out the entire nonnegative completely screened first-crossing branch.

## Keep constrained null-vector geometry, rearrangement, smooth-tail control and finite low modes separate

WI-286--WI-293 remain valid diagnostics for the unrestricted supported spectral bottom, while WI-294--WI-297 explain why that relaxation cannot replace the actual nonnegative null vector. WI-298 adds a structural reduction by rearrangement, and WI-299 adds a uniform analytic tail estimate that now reaches the same exact aperture.

These operations solve different pieces. Rearrangement removes distant-support freedom; the smooth estimate controls the kernel tail; neither proves the finite low-mode sign that remains at `r_2`. This conclusion is branch-specific and does not transfer to sign-changing modes, incomplete screening, or arbitrary supported spectral minimizers.