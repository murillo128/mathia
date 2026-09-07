---
id: CLUE-xi-flow-relative-xi-source-to-guarded-selector-stability
type: research-clue
status: proposed
origin: master-researcher
target_line: xi_flow
based_on:
  - research/analytic_frontier/findings/ANF-084-moving-euler-product-line-gives-superpolynomial-relative-xi-periodization.md
  - research/xi_flow/findings/XF-079-disjoint-selector-sidebands-make-weighted-vieta-resource-center-pointwise.md
  - research/xi_flow/findings/XF-081-chebyshev-nullspace-makes-center-local-vieta-state-nonidentifiable.md
  - research/xi_flow/findings/XF-082-exact-heat-compatibility-does-not-remove-center-local-vieta-nullspace.md
  - research/xi_flow/clues/CLUE-one-center-selector-retains-remote-guarded-mass.md
---

# Can the relative Xi source estimate control the guarded selector without reconstructing a Vieta carrier?

## Observation

`ANF-084` closes a source-side interface that the Gaussian-reference Xi route previously lacked. On the moving line `sigma_T=1+1/log T`, with Gaussian width `w=log T` and period `L=(log T)^3`, the actual Xi source admits a zero-free relative periodization whose function and every fixed logarithmic derivative error are bounded by a polynomial in `log T` times `exp(-(log T)^4/8)`. This is unconditional and already relative to the source, so it does not hide a small denominator.

The remaining Xi obstruction is now more specific. `XF-081` shows that exponentially accurate center-local function approximation can carry an arbitrarily prescribed growing low-Vieta prefix, and `XF-082` shows that exact periodic heat compatibility does not remove that nullspace on every relevant heat horizon. Independently, the accepted one-center control shows that exact nearby-root agreement plus bounded log-Vieta data can still leave order-one error in the guarded `X(B)` selector through remote mass.

Thus the source periodization estimate is much stronger than a generic local surrogate, but converting it into a polynomial root/Vieta carrier is precisely the step the new nullspaces say should not be assumed.

## Research question

Can the `ANF-084` relative/logarithmic Xi data be mapped **directly** into the one-center guarded selector resource of `XF-079`, through the Gaussian-reference quotient and its positive-time forced heat equation, with conditioning only polynomial in `log T`, without reconstructing a finite periodic zero polynomial or normalized Vieta state?

The target theorem should control the actual remote contribution in the guarded `X(B)` norm, not only the central function or nearby roots. A root-faithful global/divisor construction is an alternative, but it must explicitly defeat the `XF-081`/`XF-082` nullspace rather than choose one convenient representative from it.

## Why it may matter

This handoff removes one previously independent source uncertainty. If a destination estimate loses at most polynomial factors, the superpolynomial relative error from `ANF-084` has overwhelming margin. A successful direct map would bypass the ill-conditioned/nonidentifiable Vieta lift while preserving the source-specific analytic information that the center-only matched controls deliberately omit.

Conversely, failure would locate the Xi bottleneck cleanly in the analytic-to-selector observation operator rather than in source periodization, mode count, seam placement, or exact heat compatibility. That distinction determines whether the Gaussian-reference route still has a credible interface to the nonlinear transition argument.

## Decisive test

Work on the exact moving contour and parameter regime of `ANF-084`. After dividing by the known Gaussian reference and removing its explicit affine drift, derive a destination estimate of the schematic form

`guarded-selector error <= poly(log T) * source-relative/logarithmic error + controlled reference/PDE remainder`,

where every term is measured in norms strong enough to dominate the `XF-079` one-center `X(B)` resource, including its remote guarded sidebands. The polynomial factor and any positive-time amplification must be explicit enough that the `ANF-084` bound still gives `o(1)` after destination normalization.

Audit the estimate against both existing nullspace controls. If it depends only on center-local function accuracy plus exact free heat evolution, `XF-082` already supplies exponentially close carriers with incompatible Vieta states. If it depends only on local root agreement or bounded low log-Vieta data, the accepted remote-wave control supplies order-one `X(B)` separation. A positive theorem must use source information absent from those controls, such as the actual relative logarithmic Xi field, a source-faithful global divisor constraint, or an equivalent analytic quantity whose map to the guarded selector is proved stable.

If no such stable map exists, produce a matched analytic control satisfying the retained source-side hypotheses while maintaining order-one guarded-selector discrepancy. That would kill the direct bridge without making claims about `Lambda` itself.

## Evidence boundary

`ANF-084` proves the relative/logarithmic periodization estimate only for the actual initial Xi source on a moving zero-free line; it does not prove positive-time quotient stability, a finite Vieta realization, an `X(B)` observation inequality, or nontrivial transition mass. `XF-081` and `XF-082` are exact negative controls for local periodic carriers, not counterexamples to the actual Xi source. The one-center remote-wave clue is likewise a matched periodic control rather than an Xi configuration.

This clue therefore transfers an established source theorem into one falsifiable destination question. Success would close the source-to-selector conditioning gate only; a separate theorem would still be required to show that every relevant positive-`Lambda` transition creates order-one mass in the same guarded resource.