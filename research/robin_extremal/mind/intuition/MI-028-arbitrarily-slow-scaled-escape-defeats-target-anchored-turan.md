# MI-028 — Arbitrarily slow scaled escape defeats target-anchored Turán

**Evidence level:** exact matched-control obstruction from [RE-144](../../findings/RE-144-one-sided-slowly-diverging-clusters-defeat-target-anchored-turan-with-one-rightward-mode.md), sharpening the target-anchored reduction of [RE-143](../../findings/RE-143-target-anchored-first-main-theorem-localizes-cancellation-to-a-thin-left-slab.md).

RE-143 removes the rightmost-transfer penalty by anchoring Turán's First Main Theorem at the original algebraically strong target. Zeros far enough to the left are algebraically damped, leaving a shrinking one-sided near-left cancellation slab. RE-144 shows that shrinking physical width alone is not coercive.

There exists a matched formal simple spectrum with attained finite right edge and strong target atoms such that the retained packet on or to the right of each target contains exactly one mode—the target itself—while the complete Robin packet is nevertheless `o(M_0(U))` on the fixed-relative observation window. The cancellation is carried entirely by a near-left cluster.

The decisive scale is reciprocal. For **any** prescribed `W(U)->infinity`, however slowly, the active cluster can be placed inside

`U(beta_0-beta) <= W(U)`,  `U|gamma-gamma_0| <= W(U)`.

Thus even `W(U)=log log log U` permits hiding. This does not contradict the fixed-box visibility theorem RE-135: bounded scaled radius has a uniform visibility floor, while any unbounded scaled radius remains an available matched-control escape.

The construction also prices local complexity. With `B=2^j` active atoms, scaled radius `O(j)=O(log B)` already supports polynomial suppression of the target through a product cancellation mechanism. At the same time the complete spectrum can obey an arbitrarily slowly diverging one-level off-critical counting envelope. Global sparsity therefore does not control the rare local cardinality that matters.

The reusable frontier is sharper than “control the `O(log U/U)` slab.” A source-faithful theorem must keep the target-relative cluster in a uniformly bounded reciprocal box, bound how many actual zeros can occupy a growing box strongly enough to beat the cancellation law, or impose phase/sign structure incompatible with the product mechanism. Minimal rightward complexity and a physically vanishing slab are insufficient.

**Boundary.** RE-144 is a matched formal spectrum satisfying the source envelopes stated in that finding; it is not a theorem that actual zeta zeros form such clusters. It proves that the currently imported upper counting/density/symmetry information does not exclude the obstruction. A stronger source-specific local law may still do so.