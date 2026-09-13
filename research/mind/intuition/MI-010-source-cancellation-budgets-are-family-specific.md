# MI-010 — Exact simplification can move the endpoint cost into depth, locality or packet transport

**Evidence level:** cross-line synthesis supported by Farey Discrepancy through [FD-103](../../farey_discrepancy/findings/FD-103-power-dense-record-ladders-saturate-the-logarithmic-source-budget.md), Möbius Cancellation through [MC-274](../../mobius_cancellation/findings/MC-274-negative-witness-conditioning-fourier-depth-tax.md), and Prime Flute through [PF-331](../../prime_flute/findings/PF-331-completed-low-polar-factor-has-uniform-gap-and-cannot-amplify-locality-defects.md). No common quantitative invariant is claimed.

Several recent exact reductions do not merely shrink an error term; they **relocate the remaining cost into another mathematical resource**.

Farey Discrepancy removes carrier identity from the deterministic source-neutral budget. FD-102 gives an adaptive potential depending only on horizon and sampled source quotient, so retagging cannot reset the budget for free. FD-103 then proves the logarithmic depth is sharp on actual record ladders. The remaining theorem is no longer carrier bookkeeping: it is whether enough packet strength survives uniformly for `c log H` steps, with a polynomial projective tax.

Möbius Cancellation gives a rowwise algebraic collapse with the opposite trade. MC-273 turns every nonblind Christoffel row into a homogeneous shell once a negative witness is known. MC-274 proves that exact witness conditioning through depth `J` raises the source/Walsh degree from `2m` to `2m+J`; atomwise resolution naturally needs `J` of order `log C`. Simpler conditioned rows can therefore cost substantially more ensemble source depth.

Prime Flute removes amplitude loss as the explanation for packet disappearance. PF-330 preserves total packet mass exactly under completed normalization, while PF-331 shows polar extraction cannot amplify locality defects. The unresolved cost is spatial: control the locality of the concrete completed DtN square-root factor, not another scalar packet norm.

The durable lesson is precise: after an exact reduction, ask **where the conserved difficulty went**. It may move from carrier identity to logarithmic transport depth, from mixed degree to conditioning/query depth, or from packet amplitude to spatial locality. Continuing to optimize the old coordinate can then be mathematically irrelevant even when that optimization is correct.

**Boundary.** These are line-specific conservation-of-difficulty phenomena, not a theorem that every exact simplification preserves a universal complexity. The relocated resource must be derived in each construction and compared with its own destination budget.