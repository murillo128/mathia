# MI-030 — The sharp PNT prime-block edge is essential, so only noncompact completion can suppress it

**Evidence level:** exact synthesis from [PL-339](../../findings/PL-339-outer-source-shell-carries-unit-gap-coercivity.md), [PL-340](../../findings/PL-340-pnt-endpoint-jump-coercivity-ceiling.md), [PL-341](../../findings/PL-341-sharp-pnt-prime-block-half-mass-spectrum.md), and [PL-342](../../findings/PL-342-sharp-prime-block-essential-spectrum.md), using the endpoint modes constructed in PL-051. The conclusion concerns the bounded prime/jump block and compact completion terms, not the spectrum of the full completed Weil operator.

PL-339 proved that the accumulated positive jump sector has the total-source lower bound

`J_a >= (1-o(1)) W_a I`.

Since the exact prime block is `P_a=J_a-2W_a I`, one remaining hope was that compatibility among many positive jump forms might drive the lower edge of `J_a` all the way toward `2W_a`, asymptotically neutralizing the scalar compensation.

PL-340 ruled out that jump-only mechanism with explicit PNT endpoint states, and PL-341 identified the whole leading ordinary spectral picture. For the weighted compressed-shift sum `K_a`,

`sup sigma(K_a)=e^a(1+o(1))`,

`inf sigma(K_a)=-e^a(1+o(1))`,

while `W_a=2e^a(1+o(1))`. Therefore the isolated prime block `P_a=-K_a` has asymptotic normalized edges `-1/2` and `+1/2`, and the jump sector `J_a=2W_a I-K_a` has edges `3/2` and `5/2`. The favorable jump edge remains exactly one half-source-mass below the scalar-cancellation threshold.

PL-342 strengthens this from an ordinary spectral statement to a topological one. The same endpoint Rayleigh values can be reproduced on weakly-null high-frequency modulations. At every fixed aperture only finitely many prime logarithms occur, and Kronecker recurrence lets one choose arbitrarily large modulation frequencies that simultaneously restore all active prime-power translation phases. Consequently

`sup sigma_ess(K_a)=e^a(1+o(1))`,

`inf sigma_ess(K_a)=-e^a(1+o(1))`.

The sharp half-mass prime edge is therefore already present in the Calkin quotient. It is not a finite-dimensional surplus carried only by a few smooth endpoint modes.

This makes the completion boundary precise. The zeta-pole operator at fixed aperture has rank at most two, and the bounded continuous completion remainder is compact, so neither can change the essential spectrum of the bounded prime block. The smooth PNT cancellation of PL-059 and the essential edge of PL-342 are compatible: the pole cancels the fixed smooth endpoint mode, while compact terms vanish on the weakly-null recurrent sequence.

The genuinely unresolved completion is the unbounded logarithmic principal operator. The recurrence sequence that preserves the prime-block Rayleigh value does so by sending frequency to infinity, and the logarithmic principal symbol grows along the same sequence. The full localized completed-Weil operator has compact resolvent, so PL-342 does **not** imply essential spectrum or a negative direction for that full operator. Instead it isolates a same-state competition: recurrent prime translation gain versus archimedean/logarithmic frequency cost.

The matched-control warning also strengthens. The leading mass scale comes from the PNT law, and the promotion to essential spectrum uses finite rational independence of the active logarithmic frequencies. A generalized-prime source with the same PNT-scale mass and corresponding independent frequencies reproduces the mechanism. Neither the ordinary half-mass edge nor its Calkin persistence is by itself rational-prime RH rigidity.

The reusable lesson is that **compact or finite-rank completion cannot repair a bounded source obstruction that already survives on weakly-null recurrent states; the only possible repair must act in a noncompact/unbounded channel on those same states**. Here that channel is the logarithmic principal operator. A future result must compare its frequency cost with the recurrent prime edge on the relevant moving branch, rather than further refine the bounded PNT geometry.

**Boundary.** PL-342 determines the essential spectral edges of the bounded prime block and their invariance under compact completion. It does not prove branch persistence, identify the completed low spectrum, control the scalar part, or produce a negative direction for the completed Weil form. The unbounded principal term is load-bearing, and any RH-facing gain must enter through its same-state interaction with source-selective branch structure.
