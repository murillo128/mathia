# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Use the actual arithmetic perturbation, not another scalar regularity envelope

**Linked intuitions:** `MI-010-pair-correlation-slack-is-a-shared-exceptional-budget`, `MI-050-full-localized-weil-energy-turns-any-rh-failure-into-a-finite-radius-first-crossing`, and `MI-051-local-threshold-continuity-does-not-bootstrap-cofinally-from-an-energy-budget-alone`.

WI-355 makes any RH failure a finite first crossing of Suzuki's full localized Weil form. WI-356--WI-357 identify the correct local threshold topology: a newly activated prime channel is large in ambient operator norm but form-small on actual normalized null states because the null equation controls logarithmic energy and bounded log-energy gives an inverse-log autocorrelation modulus.

WI-358 shows that this scalar energy budget cannot be iterated cofinally. Allowed normalized tests can change an already-present source autocorrelation by order one between consecutive prime-power thresholds. The witnesses are not actual null states, so local threshold continuity survives; what fails is uniform cofinal control on the whole energy ball.

WI-359 closes the obvious stronger generic repair. Retaining the principal operator graph norm and imposing an **exact abstract zero-mode equation** still does not help if the arithmetic perturbation is compressed to a scalar norm envelope. The threshold-resolving witnesses have only `||T_0u_j||=O(a_j)` graph cost and can be made exact zero modes of rank-at-most-two self-adjoint perturbations of size `O(a_j)`, while the natural coefficientwise source envelope for Suzuki's actual remainder is exponentially larger, `U(a)>=(4+o(1))e^a`.

The remaining gate is therefore the **specific structure of the true `K_a`**. Any successful cofinal argument must use information destroyed by replacement with an arbitrary bounded self-adjoint perturbation of the same size: coupling among the von-Mangoldt translation channels, the archimedean kernel, signed-source identities, first-crossing structure, or a source-specific coercive reserve. Improving generic graph regularity or optimizing a scalar norm estimate attacks a comparison class WI-359 has already shown to be too large.

## Keep local state selection, generic graph regularity and source-specific coherence distinct

A singular ambient channel can be harmless on the physical null-state class, but local state-selected continuity is not a global positivity theorem. Conversely, the failure of generic scalar envelopes does not show that Suzuki's actual ground states jump; the counterperturbations deliberately discard the arithmetic translation geometry.

A future first-crossing exclusion should therefore state exactly which relation among the actual source channels prevents the WI-358/WI-359 oscillatory comparison states. The next useful theorem is a source-structured identity or reserve, not another topology that can be expressed solely through `||T_0w||`, `||K_a||` or an abstract zero-mode equation.