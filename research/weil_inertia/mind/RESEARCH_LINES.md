# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Turn first-crossing source order into unavoidable prime overlap

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`.

The source equation has already defeated finite-lag screening and generic positivity shortcuts. At a hypothetical first unrestricted crossing, the multiplier ground-state form is positive semidefinite and the nodal split imposes a signed compensation law. On a one-signed branch, every cut must be paid by positive prime-power overlap or positive short-range archimedean mass.

For an internal gap, the source sign-change length `h_0` gives a direct arithmetic exclusion beyond that width. Below `h_0`, [WI-273](../findings/WI-273-positive-tail-hankel-norm-sharpens-gap-screening-but-hits-the-carleman-wall.md) replaces the scalar tail budget by the exact positive-source Hankel norm `Theta(L)` and the collar masses that can actually couple across the gap. Complete screening requires enough collar concentration to overcome the proper-aperture firstness costs, and `Theta(L)` is strictly smaller than the Carleman coefficient for every positive gap.

The narrow-gap frontier is now sharper. `Theta(L)` tends exactly to `pi/2` as `L downarrow 0`, matching the half-Carleman norm. Therefore **no argument that only improves the positive-source global `L^2` operator norm can produce a uniform gapless gain**. On the one-signed branch, the next theorem must use structure that this norm forgets: simultaneous constraints from many cuts, local information about the null mode, or the distributional null equation. On sign-changing branches, the separate task remains to control long-range archimedean compensation using the PSD/nodal family and source domination.

## Treat activity, overlap, sign geometry and operator-norm screening as separate gates

Prime-translation support domination is weaker than positive autocorrelation. The PSD multiplier family is weaker than a sign theorem. One-signed gap tariffs do not apply to sign-changing modes. Within the one-signed branch, replacing a scalar `L^1` source budget by the exact `L^2` Hankel norm is a real quantitative gain for every positive gap, but WI-273 proves that this entire mass-only norm category has a sharp zero-gap wall. Further progress must change the information consumed, not merely tighten the same coefficient.