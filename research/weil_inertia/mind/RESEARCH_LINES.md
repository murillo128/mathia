# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Separate source-compatible scale from genuine nonresonance of the distinguished twist

**Linked intuitions:** `MI-036-riemann-siegel-source-scale-makes-the-direct-logarithmic-dual-noncontracting`, `MI-037-riemann-siegel-endpoint-normalization-does-not-imply-carrier-nonresonance`.

WI-322 identifies the source-compatible scale of a distinguished bow from the Riemann--von Mangoldt count: the bow must lie at or below the Riemann--Siegel square-root length. WI-323 then shows that the corresponding direct logarithmic dual is noncontracting at that scale. These remove sparsity and a naive direct-duality contraction as generic escape mechanisms.

WI-324 proves that endpoint normalization still does not imply cancellation of the bare logarithmic carrier. There is an explicit cofinal family `U_M=2pi M(M+1/2)`, `X_M=M` approaching the exact ratio `U/X^2=2pi` from above for which lattice aliasing cancels the first two Taylor jets and leaves a coherent block of length `asymp M^(1/3)`.

WI-325 strengthens this control in the direction that mattered most: **membership in the actual zeta zero-ordinate set does not by itself remove the resonance.** The explicit Riemann--von Mangoldt error guarantees a zero ordinate in every sufficiently high interval of fixed length two. Snapping each resonant `U_M` to such a zero `gamma_M=U_M+O(1)` changes the carrier phase by only `O(M^(-2/3))` across the coherent block, so the sector lower bound survives and the bare sum remains of order `M^(1/3)`.

The surviving distinguished-twist problem therefore needs more than endpoint scale and more than the statement “the height is a zeta zero.” A useful theorem must consume structure that distinguishes the actual bow-selected/off-critical configuration or the weighted von-Mangoldt source from an arbitrary nearby critical-line zero ordinate: for example a source-weighted dispersion estimate, a local zero-configuration constraint tied to the bow construction, or another arithmetic observable that directly rules out the resonant block. Reapplying stationary phase, smooth logarithmic curvature or scalar Riemann--Siegel normalization cannot supply that missing information.

## Keep bare-carrier controls separate from the weighted Weil covariance

WI-324--WI-325 are controls on the unweighted logarithmic carrier compatible with the source scale and, after snapping, with actual zero ordinates. They do not show that the distinguished Weil covariance is large, produce an off-line bow, or control the signed von-Mangoldt coefficients. The next result must therefore state exactly which extra source weight or bow-specific constraint destroys the control family before any cancellation claim is promoted to a Weil-inertia mechanism.