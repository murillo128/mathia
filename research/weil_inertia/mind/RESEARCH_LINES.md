# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Separate generic signed-source cancellation, distinguished-start quantifiers and covariance-scale norm control

**Linked intuitions:** `MI-036-riemann-siegel-source-scale-makes-the-direct-logarithmic-dual-noncontracting`, `MI-037-riemann-siegel-endpoint-normalization-does-not-imply-carrier-nonresonance`, `MI-038-signed-source-subtraction-kills-generic-cubic-resonance-but-not-exceptional-bows`, `MI-039-phase-uniform-almost-all-control-shares-one-exceptional-bow-start-set`.

WI-322 identifies the source-compatible scale of a distinguished bow from the Riemann--von Mangoldt count: the bow must lie at or below the Riemann--Siegel square-root length. WI-323 shows that the corresponding direct logarithmic dual is noncontracting at that scale. These remove sparsity and naive direct-duality contraction as generic escape mechanisms.

WI-324 constructs a cofinal family on which lattice aliasing leaves a coherent cubic block despite endpoint normalization. WI-325 shows that snapping the resonant height to an actual zeta-zero ordinate changes the phase too little to destroy the block. WI-326 then shows that positive raw von Mangoldt weights can preserve the same coherence on infinitely many starting positions. Endpoint normalization, zero-set membership and raw positivity are therefore individually insufficient nonresonance mechanisms.

WI-327 inserts the coefficient that the exact Gallagher/BOW source actually uses, `f_X=Lambda-Lambda_X^sharp`. On the same snapped cubic scale, existing almost-all short-interval PNT estimates imply that for all but `O_A(X log^(-A)X)` starts, the two positive pieces each have mass `L+o(L)` while their signed difference has untwisted mass `o(L)`. Since the carrier is uniformly close to one, the twisted signed residual is small on those typical starts. The exact source subtraction therefore destroys the generic raw-positivity resonance but leaves a distinguished-start quantifier gap.

WI-328 shows that keeping the exceptional start and the endpoint block `L asymp X^(1/3)` fixed while varying height across an entire still-live count-saturating bow changes the normalized signed sum by only `X^(2 theta-2/3+o(1))=o(1)` for every surviving `theta<=3943/12011`. Bow-internal averaging on the cubic block does not create independent samples.

WI-329 shows that at the first source length where height dephasing becomes order one, the matching modern almost-all theorem is already uniform over the bounded-complexity polynomial phase family. One common exceptional set of source starts therefore survives all bow heights; phase diversity alone does not create source-start diversity.

WI-331 identifies a lower-exponent regime where that location obstruction disappears entirely. The older all-interval nilsequence theorem applies once `J>=X^(5/8+epsilon)`. Since the natural bow length is `J=X^(1-2theta+o(1))`, every fixed `0<theta<3/16` lies in the all-start range. There the exact signed `Lambda-Lambda_X^sharp` source is controlled for **every** start `M~X`, uniformly over the relevant bow heights. Below `theta=3/16`, distinguished-start exceptionalism is therefore no longer the live obstruction.

This does not close the covariance problem. The available all-start estimate is still a linear-amplitude bound, far above the diagonal-scale `L^2` variance required by the exact WI-195 covariance after squaring. The surviving bow regime therefore splits. For `0<theta<3/16`, the live problem is principally **norm strengthening** from pointwise/linear-amplitude cancellation to the required variance scale. For `3/16<=theta<=3943/12011`, the all-start theorem no longer reaches the natural bow length, so the common exceptional-start problem remains in addition to the same `L^2` gap.

The next theorem must therefore change the norm, the arithmetic quantifier, or the source-position geometry in the regime where the quantifier is still open. Merely adding more bow heights or more polynomial phases at one start cannot help when the available theorem is already uniform over those phases.

## Keep density-one source cancellation, all-start source cancellation and pointwise Weil covariance separate

WI-327 does not prove the distinguished Weil covariance is small or exclude an off-line zero. WI-328 shows nearby bow ordinates are twist-frozen on the endpoint cubic block. WI-329 shows that moving to the first genuinely dephasing source scale still leaves one phase-uniform exceptional-start set under the almost-all theorem. WI-331 removes that exceptional-start issue for fixed `theta<3/16`, but leaves the variance norm gap intact.

The useful bridge is therefore regime-dependent. Below `3/16`, it must strengthen the exact signed source estimate to the `L^2` scale consumed by WI-195. Above `3/16`, it may also need pointwise control at the distinguished start, a mechanism forcing genuinely different source starts, or a source/bow incompatibility with the exceptional locus. In neither regime does more phase diversity at one arithmetic start suffice by itself.