# MI-038 — Signed source subtraction kills generic cubic resonance but not exceptional bows

**Evidence level:** literature-backed exact synthesis from [WI-324](../../findings/WI-324-endpoint-normalization-does-not-imply-logarithmic-carrier-cancellation.md), [WI-325](../../findings/WI-325-zero-set-snapping-preserves-cubic-endpoint-resonance.md), [WI-326](../../findings/WI-326-von-mangoldt-weighting-preserves-snapped-cubic-resonance.md), and [WI-327](../../findings/WI-327-signed-source-subtraction-suppresses-cubic-resonance-on-density-one-starts.md).

The cubic endpoint resonance survives three weak controls: correct Riemann--Siegel scaling, snapping the height to an actual zeta-zero ordinate, and inserting positive raw `Lambda` weights. WI-327 shows that the exact arithmetic source changes the conclusion because Gallagher/BOW uses the signed coefficient `Lambda-Lambda_X^sharp`, not `Lambda` alone.

On the snapped cubic block, the carrier is uniformly close to the constant phase `1`. Almost-all short-interval prime number theorems give, for a density-one set of integer starts, mass `L+o(L)` for each positive source `Lambda` and `Lambda_X^sharp` but only `o(L)` for their signed difference. Consequently the twisted signed residual is bounded by

`(pi/384+o(1))L`,

far below the fully coherent `L` scale. The generic resonance is therefore an artifact of omitting the source subtraction: two coherent positive contributions nearly cancel when the actual signed source is restored.

The result does **not** solve the distinguished problem because the desired bow selects a particular sequence of starts. A density-one theorem permits a thin exceptional set, and one selected bow could remain inside that set at every scale. The remaining obstruction is no longer generic carrier resonance but a quantifier mismatch between almost-all source cancellation and pointwise exclusion of the distinguished configuration.

This suggests a precise hierarchy for source corrections. First test the exact signed arithmetic coefficient before interpreting a positive-weight resonance. Once that correction cancels generically, the next resource to seek is not another average but a mechanism that de-exceptionalizes the selected sequence: a pointwise short-interval estimate, distribution theorem for the bow starts, or an exact geometric/source constraint incompatible with exceptional membership.

**Boundary.** WI-327 neither excludes off-critical zeros nor proves signed cancellation at a distinguished bow. It uses an almost-all short-interval theorem and therefore leaves zero-density exceptional starts untouched. Its durable content is that the exact signed source removes the previously found cubic resonance generically and isolates de-exceptionalization as the next genuine barrier.