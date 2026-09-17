# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Separate generic signed-source cancellation from de-exceptionalization at the distinguished twist

**Linked intuitions:** `MI-036-riemann-siegel-source-scale-makes-the-direct-logarithmic-dual-noncontracting`, `MI-037-riemann-siegel-endpoint-normalization-does-not-imply-carrier-nonresonance`, `MI-038-signed-source-subtraction-kills-generic-cubic-resonance-but-not-exceptional-bows`.

WI-322 identifies the source-compatible scale of a distinguished bow from the Riemann--von Mangoldt count: the bow must lie at or below the Riemann--Siegel square-root length. WI-323 shows that the corresponding direct logarithmic dual is noncontracting at that scale. These remove sparsity and naive direct-duality contraction as generic escape mechanisms.

WI-324 constructs a cofinal family on which lattice aliasing leaves a coherent cubic block despite endpoint normalization. WI-325 shows that snapping the resonant height to an actual zeta-zero ordinate changes the phase too little to destroy the block. WI-326 then shows that positive raw von Mangoldt weights can preserve the same coherence on infinitely many starting positions. Endpoint normalization, zero-set membership and raw positivity are therefore individually insufficient nonresonance mechanisms.

WI-327 inserts the coefficient that the exact Gallagher/BOW source actually uses, `f_X=Lambda-Lambda_X^sharp`. On the same snapped cubic scale, existing almost-all short-interval PNT estimates imply that for all but `O_A(X log^(-A)X)` starts, the two positive pieces each have mass `L+o(L)` while their signed difference has untwisted mass `o(L)`. Since the carrier is uniformly close to one, the twisted signed residual is at most `(pi/384+o(1))L`. The exact source subtraction therefore destroys the generic raw-positivity resonance.

WI-328 closes the most immediate de-exceptionalization escape. Keeping the exceptional start and the endpoint block `L asymp X^(1/3)` fixed while varying height across an entire still-live count-saturating bow changes the normalized signed sum by only

`X^(2 theta-2/3+o(1))=o(1)`

for every surviving `theta<=3943/12011`. Thus all neighboring zero ordinates in one bow see asymptotically the same twist on that block: a macroscopic exceptional residual remains macroscopic throughout the bow. Bow-internal averaging does not generate independent samples.

The first source length where height dephasing can even become order one is `J>=X^(4125/12011+o(1))` at the largest surviving bow exponent, strictly above the cubic scale. This is a necessary coherence threshold only; controlling the signed source on such longer intervals is a new arithmetic problem.

The live route is therefore narrower. Obtain pointwise signed control at the distinguished start; prove an exact incompatibility between bow geometry and the exceptional-start set; use cross-scale/full-window constraints that move beyond one frozen cubic block; or develop signed control on source intervals long enough for bow-height dephasing to become genuinely nontrivial. Merely sampling more ordinates inside the same bow no longer counts as a de-exceptionalization mechanism.

## Keep density-one source cancellation separate from pointwise Weil covariance

WI-327 does not prove the distinguished Weil covariance is small, exclude an off-line zero, or upgrade an almost-all short-interval theorem to a selected sequence. WI-328 adds that the zero ordinates already present in a surviving bow do not repair this quantifier mismatch automatically: on the endpoint cubic block they are twist-frozen.

The next theorem must therefore address the exceptional source start or change source scale. Repeating positive-weight carrier controls, zero-set snapping, typical-start averaging, or bow-internal height averaging at the same cubic length cannot close the pointwise problem. A useful bridge must control the exact signed `Lambda-Lambda^sharp` source at the selected configuration or prove a source/bow coupling that makes exceptional membership impossible.