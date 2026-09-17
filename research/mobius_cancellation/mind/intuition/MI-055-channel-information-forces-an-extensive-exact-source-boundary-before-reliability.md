# MI-055 — Channel information forces an extensive exact source boundary and aggregate edge discrimination

**Evidence level:** exact synthesis of MC-340 and [MC-349](../../findings/MC-349-destination-relative-edge-kl-reliability.md) through [MC-351](../../findings/MC-351-transcript-information-forces-edge-kl-budget.md). The finite-source information/KL implication is exact for the declared reciprocal source; the analytic resource upper bound remains open.

The transcript channel itself defines a canonical source quotient: two source states are equivalent exactly when they induce the same transcript law. MC-350 shows that bounded-energy dephasing cannot hide behind a quotient with a tiny exact boundary. If the transcript carries the information required by MC-340, entropy of this channel-law quotient and Boolean-cube isoperimetry force its cut to cross a linear number of source directions on average.

MC-351 closes the quantitative loophole left by exact distinction. For the source-natural neighboring graph, let `mathfrak J` be the source-averaged symmetrized transcript KL. In even rank,

`mathfrak J_1 >= 2[I(X;Y)-Gamma_R]_+`, with `Gamma_R<2 log 2`,

and the odd-rank pair-flip source has the analogous linear lower bound up to an `O(1)` puncture defect. Because non-cut edges of the channel-law quotient have identical transcript laws, they contribute zero KL: the entire budget is already supported on the exact channel cut.

Thus bounded-energy constant-factor dephasing forces `mathfrak J=Omega(R)`, not merely `Omega(R)` distinct cut directions. Near the matched-filter information floor the transcript must spend asymptotically linear aggregate statistical separation across essentially every local source direction, and exact unit-energy dephasing makes neighboring channel rows mutually singular, giving infinite edge KL.

This changes the remaining problem from a lower-bound question to an **analytic affordability question**. The finite-source converse has already priced the required discrimination. A proposed Möbius/endpoint architecture must now upper-bound the same edge-KL budget using its actual coefficient energy, precision, bandwidth, regularity or other declared analytic resource. If that upper bound is sublinear, the architecture fails; if it is linear or larger, the information tariff alone does not exclude it.

The reusable lesson is that exact quotient geometry and quantitative distinguishability should be connected in that order. A high-information channel first forces a large exact boundary and then, on this source graph, mutual information itself forces an aggregate divergence budget on that boundary. One need not posit a raw-query model or a decoder for the quotient to obtain the local statistical tariff.

**Boundary.** The channel-law quotient is still not automatically the actual Möbius endpoint quotient. MC-351 is a finite-source converse and supplies no analytic upper bound on transcript KL from a proposed arithmetic construction. It does not estimate `M(x)` or prove RH. The live bridge is to show that the resources of the actual endpoint architecture cannot afford the forced source-edge KL, or else to identify a cheaper destination quotient honestly.