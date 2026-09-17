# MI-030 — PNT endpoint modes cap jump-only coercivity before it can cancel the scalar compensation

**Evidence level:** exact synthesis from [PL-339](../../findings/PL-339-outer-source-shell-carries-unit-gap-coercivity.md), [PL-340](../../findings/PL-340-pnt-endpoint-jump-coercivity-ceiling.md), and [PL-341](../../findings/PL-341-sharp-pnt-prime-block-half-mass-spectrum.md), using the endpoint modes constructed in PL-051. The conclusion concerns the isolated prime/jump block, not the completed Weil operator.

PL-339 proved that the accumulated positive jump sector has the total-source lower bound

`J_a >= (1-o(1)) W_a I`.

Since the exact prime block is `P_a=J_a-2W_a I`, one remaining hope was that compatibility among many positive jump forms might drive the lower edge of `J_a` all the way toward `2W_a`, asymptotically neutralizing the scalar compensation.

PL-340 ruled out that jump-only mechanism with explicit PNT endpoint states, giving the sharp upper ceiling `limsup inf sigma(J_a)/W_a <= 3/2`. PL-341 now identifies the whole leading spectral picture rather than only the ceiling. For the weighted compressed-shift sum `K_a`,

`sup sigma(K_a)=e^a(1+o(1))`,

`inf sigma(K_a)=-e^a(1+o(1))`,

while `W_a=2e^a(1+o(1))`. Therefore the isolated prime block `P_a=-K_a` has asymptotic spectral edges

`inf sigma(P_a)/W_a -> -1/2`, `sup sigma(P_a)/W_a -> 1/2`,

and the jump sector `J_a=2W_a I-K_a` has edges

`inf sigma(J_a)/W_a -> 3/2`, `sup sigma(J_a)/W_a -> 5/2`.

The positive jump bulk is therefore genuinely coercive, but its best lower edge remains exactly one half-source-mass below the `2W_a` scalar cancellation threshold. More positive channels or better compatibility inside the same PNT-scale prime block cannot remove that deficit.

The result is also a matched-control warning. The leading edges use only positive PNT mass plus the compressed-shift geometry, and a generalized-prime source with the same PNT-scale weight reproduces the constants. The macroscopic half-mass spectrum is therefore **PNT-universal**, not a rational-prime discriminator. PL-059 still shows that the zeta-pole completion cancels the universal negative endpoint mode at leading order, so the sharp prime-block edge is not evidence that the completed Weil operator has a macroscopic negative direction.

The reusable lesson is that **coercive positive pieces cannot be credited toward a signed destination until the compensation/completion at the same scale is included**. PL-341 makes this quantitative and sharp: the isolated prime/jump decomposition has a universal leading spectrum with a fixed `W_a/2` deficit at its favorable edge. The next theorem must work with the completed/centered object or with a rational-prime-specific branch invariant that survives the universal PNT cancellation.

**Boundary.** PL-341 determines the leading spectral edges of the isolated PNT prime/jump block, but it does not prove branch persistence, identify the completed low spectrum, or produce a negative direction for the completed Weil form. Completion remains essential, and any RH-facing gain must enter through source-selective completion/coupling or branch information absent from the universal PNT block.