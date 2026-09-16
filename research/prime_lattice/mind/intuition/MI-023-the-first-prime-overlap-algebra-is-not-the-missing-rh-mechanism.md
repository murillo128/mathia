# MI-023 — The first-prime overlap algebra is not the missing RH mechanism

**Evidence level:** exact source-specific synthesis from [PL-324](../../findings/PL-324-odd-sector-order-positivity-breaks-exactly-at-first-prime.md) and [PL-325](../../findings/PL-325-first-prime-shift-algebra-prior-art.md). The single-shift flip decomposition is public prior art and independently reconstructed in PL-325; no external computer-assisted positivity certificate is adopted.

Once `2a` crosses `log 2`, the first active prime-power channel is the truncated translation by `b=log 2`. In the first-prime window this operator is exactly a flip between the two overlap edge strips, with a zero middle strip. Therefore its spectrum is `{-1,0,1}`, both signed eigenspaces are infinite-dimensional, and its bounded-operator norm is exactly one for every positive overlap however small.

This sharpens PL-324 without solving its sign problem. Odd parity removes the generic archimedean order obstruction until the first prime appears, but the active prime channel itself is already an indefinite reflection. The arithmetic question is not whether both signs exist—they do—but **which signed state the full Weil operator selects and how that state couples to the endpoint/source structure**.

The norm jump also gives the wrong perturbative intuition. As the aperture approaches the first-prime threshold from above, the overlap remains norm-one while it becomes small relative to the singular endpoint coercive form on the shrinking edge strips. Thus bounded-operator norm predicts an artificial discontinuity, whereas the natural form topology can absorb the same channel near threshold. Neither fact determines the bottom Weil eigenvalue.

PL-325 also establishes a research-allocation boundary: the flip decomposition, its `±1` sectors, Legendre compression and related single-prime finite-scale machinery are already public prior art. Re-deriving that algebra or proving one more isolated positivity point does not address the RH-facing gap.

The surviving mechanism must be aperture-global or state-selective: a signed first-crossing/eigenstate-orientation law, a source/endpoint-flux identity that controls the actual selected state, or another arithmetic theorem that survives beyond the single `log 2` block. The relevant resource is **orientation of the full source-selected state**, not the existence or size of the first-prime overlap operator.

**Boundary.** The public prior-art project contains stronger computer-assisted finite-scale claims, but PL-325 deliberately does not import those as evidence. This intuition uses only the exact overlap algebra and the corrected endpoint-form comparison reconstructed in the canonical finding.
