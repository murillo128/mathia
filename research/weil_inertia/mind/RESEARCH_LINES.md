# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Use the actual arithmetic perturbation and retain noncompact source information

**Linked intuitions:** `MI-010-pair-correlation-slack-is-a-shared-exceptional-budget`, `MI-029-post-threshold-compact-positivity-needs-noncompact-tail-retention-not-a-canonical-finite-rank-correction`, `MI-050-full-localized-weil-energy-turns-any-rh-failure-into-a-finite-radius-first-crossing`, and `MI-051-local-threshold-continuity-does-not-bootstrap-cofinally-from-an-energy-budget-alone`.

WI-355 makes any RH failure a finite first crossing of Suzuki's full localized Weil form. WI-356--WI-357 identify the correct local threshold topology: a newly activated prime channel is large in ambient operator norm but form-small on actual normalized null states because the null equation controls logarithmic energy and bounded log-energy gives an inverse-log autocorrelation modulus.

WI-358 shows that this scalar energy budget cannot be iterated cofinally. Allowed normalized tests can change an already-present source autocorrelation by order one between consecutive prime-power thresholds. The witnesses are not actual null states, so local threshold continuity survives; what fails is uniform cofinal control on the whole energy ball.

WI-359 closes the obvious stronger generic repair. Retaining the principal operator graph norm and imposing an exact abstract zero-mode equation still does not help if the arithmetic perturbation is compressed to a scalar norm envelope. The threshold-resolving witnesses have only `||T_0u_j||=O(a_j)` graph cost and can be made exact zero modes of rank-at-most-two self-adjoint perturbations of size `O(a_j)`, while the natural coefficientwise source envelope for Suzuki's actual remainder is exponentially larger.

WI-360 closes a complementary localization shortcut with a source-specific witness. Once `L>log(8)/2`, a two-bump test whose autocorrelation isolates the `log 8` channel and whose modulation locks its phase makes the tail-dropped localized comparison converge to

`1/16 - log(2)/(2 sqrt(2)) < -1/8`.

Every fixed compact self-adjoint repair vanishes on that weakly-null high-frequency sequence. Thus a unit-window lower comparison cannot be propagated past the activation of `8` by discarding the exterior/source tail and replacing it with a fixed compact correction. A viable scheme must retain noncompact frequency coercivity, source-exact active-channel information, or a genuine first-crossing/null-state restriction that excludes the witness.

The remaining gate is therefore the **specific structure of the true `K_a` together with the noncompact information discarded by generic localization**. Any successful cofinal argument must use information destroyed by scalar norm compression or fixed compact replacement: coupling among the von-Mangoldt translation channels, the archimedean/exterior tail, signed-source identities, first-crossing structure, or a source-specific coercive reserve.

## Keep local state selection, generic graph regularity, compact repair and source-specific coherence distinct

A singular ambient channel can be harmless on the physical null-state class, but local state-selected continuity is not a global positivity theorem. Conversely, the failure of generic scalar envelopes or compact repairs does not show that Suzuki's actual ground states jump; the counterexamples deliberately discard arithmetic translation geometry or actual null-state selection.

A future first-crossing exclusion should therefore state exactly which relation among the actual source channels prevents both classes of comparison state: the threshold-resolving graph/norm witnesses of WI-358--WI-359 and the high-frequency prime-eight coherent witness of WI-360. The next useful theorem is a source-structured identity, noncompact tail estimate or first-state reserve, not another topology expressible solely through `||T_0w||`, `||K_a||`, or a fixed compact correction.