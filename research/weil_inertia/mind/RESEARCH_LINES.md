# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Separate generic signed-source cancellation from de-exceptionalization at the distinguished twist

**Linked intuitions:** `MI-036-riemann-siegel-source-scale-makes-the-direct-logarithmic-dual-noncontracting`, `MI-037-riemann-siegel-endpoint-normalization-does-not-imply-carrier-nonresonance`, `MI-038-signed-source-subtraction-kills-generic-cubic-resonance-but-not-exceptional-bows`.

WI-322 identifies the source-compatible scale of a distinguished bow from the Riemann--von Mangoldt count: the bow must lie at or below the Riemann--Siegel square-root length. WI-323 shows that the corresponding direct logarithmic dual is noncontracting at that scale. These remove sparsity and naive direct-duality contraction as generic escape mechanisms.

WI-324 constructs a cofinal family on which lattice aliasing leaves a coherent cubic block despite endpoint normalization. WI-325 shows that snapping the resonant height to an actual zeta-zero ordinate changes the phase too little to destroy the block. WI-326 then shows that positive raw von Mangoldt weights can preserve the same coherence on infinitely many starting positions. Endpoint normalization, zero-set membership and raw positivity are therefore individually insufficient nonresonance mechanisms.

WI-327 inserts the coefficient that the exact Gallagher/BOW source actually uses:

`f_X(n)=Lambda(n)-Lambda_X^sharp(n)`.

On the same snapped cubic scale, existing almost-all short-interval PNT estimates imply that for all but `O_A(X log^(-A)X)` integer starts in `[X,3X/2]`, both positive pieces have mass `L+o(L)` while their signed difference has untwisted mass `o(L)`. Since the snapped carrier is uniformly within `pi/768+o(1)` of `1` on the block, the twisted signed sum is at most

`(pi/384+o(1)) L`.

Thus the exact signed subtraction destroys the **generic** raw-positivity resonance by cancellation between two individually coherent positive sources. This materially validates the source correction omitted by WI-326.

The remaining problem is also sharper. The distinguished source-compatible bow is not a typical start; a single relevant start can lie forever in the thin exceptional set left by the almost-all theorem. The live route is therefore **de-exceptionalization**: obtain pointwise signed control at the distinguished start, prove that bow geometry cannot inhabit the exceptional set, or use full-window/source structure that couples the distinguished twist to the density-one cancellation theorem.

## Keep density-one source cancellation separate from pointwise Weil covariance

WI-327 does not prove the distinguished Weil covariance is small, exclude an off-line zero, or upgrade an almost-all short-interval theorem to a selected sequence. It says that the previously observed cubic resonance is not a generic obstruction once the exact signed arithmetic coefficient is restored.

The next theorem must address the quantifier mismatch directly. Repeating positive-weight carrier controls, zero-set snapping or typical-start averaging cannot close a pointwise exceptional problem. A useful bridge must either control the signed `Lambda-Lambda^sharp` source at the selected bow start, show that the selected starts have enough distribution relative to the exceptional sets, or exploit an exact BOW constraint that makes exceptional membership incompatible with the bow.