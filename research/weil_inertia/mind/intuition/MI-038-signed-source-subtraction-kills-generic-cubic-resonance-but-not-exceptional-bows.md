# MI-038 — Signed source subtraction kills generic cubic resonance, but bow-internal height variation does not de-exceptionalize it

**Evidence level:** literature-backed exact synthesis from [WI-324](../../findings/WI-324-endpoint-normalization-does-not-imply-logarithmic-carrier-cancellation.md), [WI-325](../../findings/WI-325-zero-set-snapping-preserves-cubic-endpoint-resonance.md), [WI-326](../../findings/WI-326-von-mangoldt-weighting-preserves-snapped-cubic-resonance.md), [WI-327](../../findings/WI-327-signed-source-subtraction-suppresses-cubic-resonance-on-density-one-starts.md), and [WI-328](../../findings/WI-328-surviving-bows-are-twist-frozen-on-the-endpoint-cubic-signed-block.md).

The cubic endpoint resonance survives three weak controls: correct Riemann--Siegel scaling, snapping the height to an actual zeta-zero ordinate, and inserting positive raw `Lambda` weights. WI-327 shows that the exact arithmetic source changes the conclusion because Gallagher/BOW uses the signed coefficient `Lambda-Lambda_X^sharp`, not `Lambda` alone.

On the snapped cubic block, the carrier is uniformly close to the constant phase `1`. Almost-all short-interval prime number theorems give, for a density-one set of integer starts, mass `L+o(L)` for each positive source `Lambda` and `Lambda_X^sharp` but only `o(L)` for their signed difference. Consequently the twisted signed residual is bounded by `(pi/384+o(1))L`, far below the fully coherent `L` scale. The generic resonance is therefore an artifact of omitting the source subtraction.

WI-328 tests the most obvious way to remove the remaining exceptional-set quantifier: use the many neighboring zero ordinates inside one surviving bow as many nearby twists. That does not work on the endpoint cubic block. For fixed start `M asymp X` and block length `L asymp X^(1/3)`, the exact signed sum is Lipschitz in height with normalized variation bounded by

`X^(2 theta-2/3+o(1))`

across a count-saturating bow at `T asymp X^2`. Every still-live bow exponent satisfies `theta<=3943/12011<1/3`, so this tends to zero by a fixed power. A macroscopic exceptional value at one ordinate remains macroscopic throughout the bow; an `o(L)` value remains `o(L)` throughout the bow. The neighboring ordinates are therefore **not independent twist samples** for this source block.

The scale comparison identifies the first place where vertical dephasing could even become nontrivial. A source interval of length `J` needs `H_bow J/X` of order one. At the largest surviving bow exponent this requires

`J >= X^(4125/12011+o(1))`,

strictly longer than the current `X^(1/3)` block by exponent `364/36033`. This is only a necessary coherence threshold, not a theorem of cancellation on longer blocks.

The remaining obstruction is consequently sharper than “almost-all is not pointwise.” The exact signed source cancels the generic cubic resonance, but the bow itself does not supply enough vertical motion to average away one exceptional start at the same cubic scale. De-exceptionalization must come from pointwise arithmetic information at the distinguished start, a theorem coupling bow geometry to the exceptional set, cross-scale source information, or control of a genuinely longer source interval beyond the twist-coherence threshold.

The reusable lesson is that repeated observations do not buy independent information when the source observable is frozen on their natural variation scale. Before using a family of nearby spectral parameters to defeat an exceptional set, compare the family diameter with the intrinsic coherence window of the exact signed source observable, not merely with zero spacing or observation count.

**Boundary.** WI-328 does not prove the distinguished start is exceptional, does not control the full Gallagher norm, and does not say a longer block will cancel. It closes only bow-internal height averaging as an automatic de-exceptionalization mechanism for the current endpoint cubic block. No unconditional simple-critical-zero proportion or RH conclusion changes.