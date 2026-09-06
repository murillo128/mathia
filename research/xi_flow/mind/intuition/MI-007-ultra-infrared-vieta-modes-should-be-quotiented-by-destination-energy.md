# MI-007 — Ultra-infrared Vieta modes should be quotiented by destination energy rather than forced source-small

**Evidence level:** exact periodic/source-band comparison and matched-control evidence through XF-069, using the destination third-difference geometry of XF-062--XF-066

## Core intuition

A source theorem should not be required to control state directions that the destination theorem is already insensitive to. In the Xi/Vieta bridge, the moving-line selector sees a broad growing band of positive frequencies but cannot reach the finitely many ultra-infrared Vieta modes. Those fixed modes are also barely damped by fixed positive heat time. Nevertheless an explicit periodic control shows that they can remain order one while the normalized third-difference transition energy tends to zero.

The correct nonlinear state is therefore not the raw vector of all low Vieta coefficients. It should be a **weighted or quotient Vieta state whose norm matches the destination transition energy**, so source control is demanded only in directions capable of contributing at the required scale.

## Strongest justified principle

XF-069 converts periodic Vieta index `k` to selector frequency `xi_k=pi k/q^2`. The source band of XF-059 reaches `k` only above a power-growing infrared cutoff; no fixed choice of its resolution parameter reaches `k=O(1)`. Thus fixed Vieta modes are genuinely outside the current source selector rather than merely omitted by a loose estimate.

Positive heat time does not remove them: the exact XF-067 damping exponent for fixed `k` is `Theta(k/q)` and tends to zero. Requiring all raw low power sums to be small would therefore create a source obligation that neither the selector nor the heat semigroup supplies.

The matched periodic perturbation in XF-069 separates this raw-coordinate issue from destination relevance. Its first power sum stays order one, while the XF-062/XF-066 third-difference energy is `O(q^{-4})`. The same mode is source-unresolved, heat-undamped, and asymptotically harmless for the transition observable. This proves that raw low-mode smallness is strictly stronger than the destination geometry requires.

## What remains possible

A useful weighted Vieta norm must preserve the exact diagonal heat evolution, suppress the ultra-infrared sector with a quantified `o(1)` contribution, and retain enough of the source-visible band to control the XF-065--XF-066 transition state. The nonperiodic Xi-to-periodic interface estimate must then be proved in that same weighted resource.

It remains possible that an actual positive de Bruijn--Newman transition forces a low-mode contribution through a mechanism not seen by the present third-difference controls. Such a theorem would change the correct quotient and must be derived rather than assumed.

## Status / novelty

The Fourier scaling and finite-difference suppression are elementary once the periodic coordinates are fixed. The durable synthesis is destination-relative: **uncontrolled coordinates should be removed when exact controls show they lie in an asymptotic null sector of the final observable, rather than promoted to artificial source hypotheses.**

## Falsification criterion

Show that a fixed ultra-infrared mode can contribute order-one normalized XF-062/XF-066 transition energy under the stated scaling, invalidate XF-069's explicit matched control, or prove that every relevant Xi transition necessarily couples the source-visible band to those fixed modes with a non-negligible destination contribution.
