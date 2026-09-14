# MI-027 — Bounded overlap order cannot determine high-cardinality Page parity

**Evidence level:** exact matched-control obstruction from [MC-298](../../findings/MC-298-finite-order-endpoint-overlaps-do-not-control-page-parity.md). The construction is a generic finite endpoint system; it does not assert that actual Möbius/Legendre defect sets realize the controls.

For a selected family of `m` endpoint-defect sets, let `K(x)` be the number active at `x`. The Page sign is the top-order observable `(-1)^K`. In an exchangeable endpoint model, every symmetric `j`-fold intersection statistic is exactly a normalized factorial moment `E[(K)_j]`.

For every fixed `r<m`, the finite-difference vector

`v_k=(-1)^k binom(r+1,k)`

annihilates every polynomial in `k` of degree at most `r`, hence preserves all factorial moments through order `r`, while it changes the parity expectation because `sum v_k(-1)^k=2^(r+1)`. Small positive/negative perturbations of a strictly positive probability law therefore give two finite deterministic endpoint systems with identical overlap data through order `r` and different Page negative mass.

The useful conclusion is not merely that pair overlap is insufficient. **Any overlap hierarchy whose order stays bounded while the Page cardinality grows can remain blind to parity.** Adding one more fixed intersection level does not move the fundamental boundary.

A successful arithmetic route must therefore supply something outside unrestricted bounded-order marginals: interaction order growing with the selected cardinality, an exact arithmetic identity collapsing parity to lower-order data, structural restrictions excluding the moment-matched controls, or a different destination observable that sees the surviving modes directly.

**Boundary.** This is an information obstruction for generic endpoint systems, not a theorem about the actual Möbius defect geometry. Arithmetic structure could invalidate the controls; proving precisely such rigidity is now the point.
