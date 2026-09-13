# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Convert the simultaneous-cut reserve into unavoidable arithmetic overlap

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`.

The first-crossing source equation has defeated finite-lag screening and generic positivity shortcuts. WI-273 sharpened one-signed positive-gap screening with the exact positive-source Hankel norm, but proved that every mass-only single-cut `L^2` refinement hits the half-Carleman wall as the gap closes.

[WI-274](../findings/WI-274-simultaneous-cuts-create-a-positive-saturated-source-reserve.md) uses the information that this norm discards. Integrating the **entire family of sharp cuts** counts each translated pair for exactly its lag and forces, for an arbitrary real first null mode,

`S_v >= 2 integral_(a/2)^a lambda_r dr > 0`.

The saturated endpoint source therefore retains a strictly positive reserve even though the single-radius lower bound can vanish at the crossing.

On a one-signed branch this yields the explicit screening condition

`P_v >= 2 integral_(a/2)^a lambda_r dr - K_+`.

The live one-signed theorem is now to make the spectral-area reserve exceed the finite archimedean budget, or to strengthen the integrated inequality using the null-mode equation. On sign-changing branches, use the PSD/nodal family to prevent prime and archimedean cancellation from hiding inside the positive total reserve.

## Treat endpoint firstness, integrated reserve, sign geometry and prime overlap as separate gates

A positive saturated source functional is stronger than the degenerating endpoint cut but weaker than positive prime overlap. The one-signed budget does not transfer to a sign-changing mode, and the existence of a spectral gap does not supply the needed sign. Future work should preserve the simultaneous-cut reserve while adding exactly the source/sign information needed to separate its prime and archimedean components.
