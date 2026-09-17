# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Separate source-compatible scale from genuine nonresonance of the distinguished twist

**Linked intuitions:** `MI-036-riemann-siegel-source-scale-makes-the-direct-logarithmic-dual-noncontracting`, `MI-037-riemann-siegel-endpoint-normalization-does-not-imply-carrier-nonresonance`.

WI-322 identifies the source-compatible scale of a distinguished bow from the Riemann--von Mangoldt count: the bow must lie at or below the Riemann--Siegel square-root length. WI-323 then shows that the corresponding direct logarithmic dual is noncontracting at that scale. These remove sparsity and a naive direct-duality contraction as generic escape mechanisms.

WI-324 proves that endpoint normalization still does not imply cancellation of the bare logarithmic carrier. There is an explicit cofinal family `U_M=2pi M(M+1/2)`, `X_M=M` approaching the exact ratio `U/X^2=2pi` from above for which lattice aliasing cancels the first two Taylor jets and leaves a coherent block of length `asymp M^(1/3)`.

WI-325 strengthens the control in the direction that mattered most: **membership in the actual zeta zero-ordinate set does not by itself remove the resonance.** The explicit Riemann--von Mangoldt error guarantees a zero ordinate in every sufficiently high interval of fixed length two. Snapping each resonant `U_M` to such a zero `gamma_M=U_M+O(1)` changes the carrier phase by only `O(M^(-2/3))` across the coherent block, so the sector lower bound survives.

WI-326 now closes the next weak source-weight repair. Positive raw von Mangoldt weights can preserve the snapped cubic coherence. PNT averaging supplies infinitely many resonant starting positions whose cubic block carries total `Lambda` mass `asymp M^(1/3)`, and the WI-325 sector converts that positive mass directly into a weighted coherent sum of the same order. After square-root normalization its coherent square is `>>M^(-1/3)`, while the diagonal energy of the block is `<<M^(-2/3)log^2 M`. The coherent/diagonal ratio therefore diverges.

The surviving distinguished-twist problem now needs structure absent from **all three** controls: endpoint normalization, zero-set membership and positive raw prime weighting. The clean source-side discriminator is the actual signed coefficient `Lambda-Lambda^sharp` and the rest of the exact Gallagher/BOW source geometry. A useful theorem must show either that this subtraction destroys the snapped cubic coherence, that the full natural window necessarily cancels every such coherent subblock, or that bow-specific off-critical geometry imposes a stronger nonresonance condition than proximity to an arbitrary zero ordinate.

## Keep positive-weight carrier controls separate from the signed/full-window Weil covariance

WI-324--WI-326 do not show that the distinguished Weil covariance is large, produce an off-line bow, or control the actual signed BOW coefficient. WI-326 is deliberately a negative test of a weaker route: even raw prime weighting does not make the cubic endpoint control disappear, and comparison with the same block's diagonal `L^2` energy is insufficient.

The next result must therefore retain the feature omitted by the control family. The most direct source test is the signed `Lambda-Lambda^sharp` mass on the same snapped cubic blocks. A different admissible route is a rigorous full-window cancellation theorem showing that the remainder outside every coherent cubic subblock necessarily offsets it at the distinguished twist. Reapplying stationary phase, smooth logarithmic curvature, scalar Riemann--Siegel normalization, zero-set membership or positivity of raw prime weights cannot supply that missing information.