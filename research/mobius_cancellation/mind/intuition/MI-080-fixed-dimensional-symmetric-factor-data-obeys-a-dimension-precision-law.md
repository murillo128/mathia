# MI-080 — Fixed-dimensional symmetric factor data obeys a dimension–precision law

**Evidence level:** exact combinatorial synthesis from [MC-429](../../findings/MC-429-fixed-dimensional-vector-factor-quotient-precision-threshold.md), extending the scalar permutation-quotient threshold MC-428. The weighted vector-partition estimate is classical in type; the line-specific content is the precision tariff after factor-slot symmetry is quotiented.

Suppose each active factor is retained through a nonnegative `k`-vector and the downstream observable is invariant under factor permutations. If the total `l1` weight of the unordered vector multiset is at most `S`, MC-429 proves

`N_(k,sym)(S,r) <= (r+1) exp(C_k S^(k/(k+1)))`.

For `k` fixed nonnegative additive factor channels whose total masses are `O(log X)`, quantized at mesh `eta`, one has `S=O(log X/eta)`. Consequently every regime

`eta^(-1) <= (log X)^(delta+o(1))`, `delta<1/k`,

still carries only `X^(o(1))` symmetric states. Conversely, polynomial orbit-state capacity forces

`eta^(-1) >= c (log X)^(1/k)`.

Thus adding finitely many scalar coordinates is a genuine escape from the one-dimensional inverse-log precision threshold, but only through an explicit dimension–precision tradeoff. A fixed `k` cannot turn constant or sub-`(log X)^(1/k)` resolution into polynomial source capacity after the slot quotient.

The durable accounting rule is to price retained dimension and retained precision jointly **after** every symmetry quotient used by the destination. Raw coordinate count is not an independent bandwidth currency, but increasing dimension can lower the required precision in the quantified way above.

**Boundary.** This is a state-count obstruction, not a cancellation estimate. It assumes fixed `k`, nonnegative additive channel budgets of order `log X`, a common quantization scale and permutation-invariant readout. Growing-dimensional summaries, exact factor identity, nonadditive relations and intrinsic ordered roles remain outside the bound.