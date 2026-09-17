# MI-055 — Channel information forces an extensive exact source boundary and reverse-discrimination budget

**Evidence level:** exact synthesis of MC-340 and [MC-349](../../findings/MC-349-destination-relative-edge-kl-reliability.md) through [MC-352](../../findings/MC-352-edge-likelihood-ratio-stability-dephasing-barrier.md). The finite-source information/KL/likelihood implication is exact for the declared reciprocal source; the analytic reverse-sensitivity upper bound remains open.

The transcript channel itself defines a canonical source quotient: two source states are equivalent exactly when they induce the same transcript law. MC-350 shows that bounded-energy dephasing cannot hide behind a quotient with a tiny exact boundary. If the transcript carries the information required by MC-340, entropy of this channel-law quotient and Boolean-cube isoperimetry force its cut to cross a linear number of source directions on average.

MC-351 closes the quantitative loophole left by exact distinction. For the source-natural neighboring graph, let `mathfrak J` be the source-averaged symmetrized transcript KL. In even rank,

`mathfrak J_1 >= 2[I(X;Y)-Gamma_R]_+`, with `Gamma_R<2 log 2`,

and the odd-rank pair-flip source has the analogous linear lower bound up to an `O(1)` puncture defect. Because non-cut edges of the channel-law quotient have identical transcript laws, they contribute zero KL: the entire budget is already supported on the exact channel cut.

MC-352 supplies the matching upper currency. For an edge `e={x,x'}`, let

`epsilon_e = ess sup |log(dP_x/dP_x')|`

with `epsilon_e=+infinity` when the neighboring transcript laws are not mutually absolutely continuous, and put `psi(u)=u tanh(u/2)`. The symmetrized edge divergence obeys the sharp bound

`b_e <= psi(epsilon_e)`,

with `psi(u)=u^2/2+O(u^4)` and `psi(u)<=u^2/2`. Thus the extensive KL tariff cannot coexist with uniformly vanishing source-edge likelihood contrast. Under bounded coefficient energy, any nontrivial asymptotic dephasing forces a nonvanishing weighted average of `psi(epsilon_e)`; exact matched-energy dephasing drives the relevant neighboring transcript laws to mutual singularity.

This sharpens the remaining problem from generic “analytic affordability” to **reverse statistical sensitivity of the actual observation law**. A proposed Möbius/endpoint architecture must upper-bound the source-edge likelihood-ratio radius, or a suitable averaged/exceptional-tail version of the same `psi` budget, using coefficient energy, analytic bandwidth, precision, regularity or another genuinely available resource. Forward smoothness of the encoding is not such a bound: it can coexist with exponentially fine inverse distinguishability.

The reusable lesson is that exact quotient geometry and quantitative distinguishability should be connected in both directions. Information first forces a large exact boundary and an extensive aggregate edge divergence; a concrete analytic architecture can defeat that lower bound only by proving that neighboring source states remain statistically too similar in the **reverse** likelihood sense. Counting coordinates, bounding forward derivatives, or postulating a noise model without controlling the induced transcript likelihoods does not close the loop.

**Boundary.** The channel-law quotient is still not automatically the actual Möbius endpoint quotient. MC-352 supplies an exact conversion from edge likelihood-ratio stability to an upper KL budget, but no theorem yet bounds those likelihood ratios for a concrete Möbius architecture from its analytic resources. It does not estimate `M(x)` or prove RH. The live bridge is to prove a source-natural reverse-sensitivity estimate strong enough to make the compulsory extensive discrimination unaffordable, or else identify a cheaper destination quotient honestly.