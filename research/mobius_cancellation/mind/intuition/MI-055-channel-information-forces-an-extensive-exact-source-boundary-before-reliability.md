# MI-055 — Channel information forces an extensive exact source boundary before reliability

**Evidence level:** exact synthesis of MC-340, MC-349 and [MC-350](../../findings/MC-350-channel-quotient-entropy-forces-extensive-source-cut.md). The entropy/cut implication is exact for the declared reciprocal hypercube source; the quantitative reliability step remains open.

The transcript channel itself defines a canonical source quotient: two source states are equivalent exactly when they induce the same transcript law. MC-350 shows that bounded-energy dephasing cannot hide behind a quotient with a tiny exact boundary. If the transcript carries the information required by MC-340, entropy of this channel-law quotient and Boolean cube isoperimetry force its cut to cross a linear number of source directions on average.

In particular, near the matched-filter information floor the normalized exact cut degree tends to one. The transcript must therefore distinguish source states across essentially every local source direction. This closes one possible escape from MC-349: a successful dephasing architecture cannot first compress the reciprocal source into a quotient whose boundary is only subextensive and then hope to pay reliability on a few exceptional edges.

But **exact distinction is not reliable distinction**. Two transcript laws on a crossing edge can be different while having arbitrarily small symmetrized KL divergence. MC-349 prices destination reliability by divergence accumulated on the destination cut, not by the number of exact quotient classes. MC-350 therefore establishes the geometry of a compulsory extensive boundary before it establishes the information strength carried across that boundary.

The useful next quantity is aggregate edge discrimination on this forced cut. A successful lower bound must connect the dephasing information requirement to `mathfrak J_q`-type divergence rather than merely to channel quotient entropy.

**Boundary.** The quotient in MC-350 is the transcript/channel-law quotient, not yet the actual Möbius endpoint quotient. The theorem uses the even-rank punctured reciprocal cube and gives no uniform lower bound on pairwise KL, Hellinger distance, total variation or final endpoint error.