# MI-054 — Reliability is priced by the destination cut, not output size

**Evidence level:** exact synthesis from [MC-348](../../findings/MC-348-source-graph-divergence-is-the-invariant-reliability-tariff.md) and [MC-349](../../findings/MC-349-destination-quotient-cut-reliability.md).

MC-348 prices reliable recovery of the full reciprocal source vector by the symmetrized transcript divergence carried across the natural neighboring-state graph. MC-349 identifies the exact destination-relative refinement: if the downstream quantity is a quotient `q(X)`, only source edges across which `q` changes belong to the unavoidable reliability bill.

Let `E_q` be the destination cut, `kappa_q` its source-averaged degree, `Delta_q` its maximum degree, and `mathfrak J_q` the source-averaged symmetrized KL divergence accumulated over cut edges. If a decoder estimates `q(X)` with error probability `p_q`, then

`p_q >= (kappa_q/(4 Delta_q)) exp(-mathfrak J_q/kappa_q)`,

or equivalently

`mathfrak J_q >= kappa_q [log(kappa_q/(4 Delta_q p_q))]_+`.

The important point is that **output cardinality is not reliability complexity**. A one-bit destination can still require extensive divergence when its cut crosses `Theta(R)` independent source directions. Conversely, a high-dimensional source does not force the full-vector tariff when the destination is constant along most neighboring directions. The invariant object is the geometry of the destination cut inside the admissible source graph.

This sharpens the acquisition ledger. Before charging raw coordinate recovery, query count or full source entropy, identify the actual destination quotient and ask which admissible source perturbations cross it. Only then should analytic access be tested for enough edge discrimination to pay the required reliability tariff.

**Boundary.** MC-349 does not identify the correct quotient for the actual Möbius endpoint, and it does not upper-bound `mathfrak J_q` for any proposed analytic transcript. Those are now the live arithmetic tasks. The theorem also does not say that every sparse cut is cheap: the transcript may still pay large divergence on the few decisive edges.