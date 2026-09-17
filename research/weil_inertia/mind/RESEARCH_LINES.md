# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Separate generic signed-source cancellation from de-exceptionalization at the distinguished twist

**Linked intuitions:** `MI-036-riemann-siegel-source-scale-makes-the-direct-logarithmic-dual-noncontracting`, `MI-037-riemann-siegel-endpoint-normalization-does-not-imply-carrier-nonresonance`, `MI-038-signed-source-subtraction-kills-generic-cubic-resonance-but-not-exceptional-bows`, `MI-039-phase-uniform-almost-all-control-shares-one-exceptional-bow-start-set`.

WI-322 identifies the source-compatible scale of a distinguished bow from the Riemann--von Mangoldt count: the bow must lie at or below the Riemann--Siegel square-root length. WI-323 shows that the corresponding direct logarithmic dual is noncontracting at that scale. These remove sparsity and naive direct-duality contraction as generic escape mechanisms.

WI-324 constructs a cofinal family on which lattice aliasing leaves a coherent cubic block despite endpoint normalization. WI-325 shows that snapping the resonant height to an actual zeta-zero ordinate changes the phase too little to destroy the block. WI-326 then shows that positive raw von Mangoldt weights can preserve the same coherence on infinitely many starting positions. Endpoint normalization, zero-set membership and raw positivity are therefore individually insufficient nonresonance mechanisms.

WI-327 inserts the coefficient that the exact Gallagher/BOW source actually uses, `f_X=Lambda-Lambda_X^sharp`. On the same snapped cubic scale, existing almost-all short-interval PNT estimates imply that for all but `O_A(X log^(-A)X)` starts, the two positive pieces each have mass `L+o(L)` while their signed difference has untwisted mass `o(L)`. Since the carrier is uniformly close to one, the twisted signed residual is small on those typical starts. The exact source subtraction therefore destroys the generic raw-positivity resonance but leaves a distinguished-start quantifier gap.

WI-328 shows that keeping the exceptional start and the endpoint block `L asymp X^(1/3)` fixed while varying height across an entire still-live count-saturating bow changes the normalized signed sum by only `X^(2 theta-2/3+o(1))=o(1)` for every surviving `theta<=3943/12011`. Bow-internal averaging on the cubic block does not create independent samples.

WI-329 now closes the natural longer-window version of that escape. The first dephasing scale is `J asymp X^(1-2theta)`, and at every surviving fixed `theta` this exponent lies inside the published `1/3+epsilon` almost-all nilsequence range. On such a natural source interval, the logarithmic carrier for all bow heights `|U| lesssim X^2` is uniformly approximated by fixed-degree polynomial phases. The matching theorem takes a supremum over all such polynomial nilsequences **before** declaring the good starts, so one common density-one set controls the entire bow.

Height dephasing therefore changes the phases without splitting the exceptional source locus. If the distinguished start is exceptional, sampling more ordinates at the natural dephasing scale still does not force a good arithmetic instance. Moreover the available linear-amplitude bound remains far above the diagonal-scale `L^2` variance required by the exact WI-195 covariance after squaring.

The live route is narrower again: obtain pointwise signed control at the distinguished start; prove an exact incompatibility between source-compatible bow geometry and the common exceptional-start set; force sufficiently separated **source starts** rather than merely many heights; or obtain arithmetic information strong enough for the WI-195 `L^2` gate. More Archimedean phase diversity at one start is no longer a de-exceptionalization mechanism under the present theorem.

## Keep density-one source cancellation separate from pointwise Weil covariance

WI-327 does not prove the distinguished Weil covariance is small or exclude an off-line zero. WI-328 shows nearby bow ordinates are twist-frozen on the endpoint cubic block. WI-329 shows that moving to the first genuinely dephasing source scale still leaves one phase-uniform exceptional-start set and does not close the variance norm gap.

The next theorem must therefore change the arithmetic quantifier or the norm, not merely the phase family. Repeating positive-weight carrier controls, zero-set snapping, typical-start averaging, cubic bow-height averaging, or natural-scale phase dephasing at the same distinguished start cannot close the pointwise problem. A useful bridge must control the exact signed `Lambda-Lambda^sharp` source on the selected configuration, move to independently constrained source starts, or prove a source/bow coupling that makes exceptional membership impossible.