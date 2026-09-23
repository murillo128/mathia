# MI-099 — Endpoint-only cross-root bias has a square-root-conductor resolution floor

**Evidence level:** supported by the factorization and completion chain [MC-493](../../findings/MC-493-repeated-residue-multiplicity-factorizes-before-jacobi-interference.md), [MC-494](../../findings/MC-494-complete-pair-sieve-weights-aggregate-before-jacobi-interference.md), [MC-495](../../findings/MC-495-incomplete-two-root-blocks-reduce-to-weighted-rational-character-bias.md), and [MC-496](../../findings/MC-496-endpoint-only-cross-root-bias-has-a-square-root-conductor-threshold.md).

MC-493--MC-495 show that repeated-residue multiplicities and complete pair-sieve factors aggregate before the Jacobi interference is formed. After those positive or factorized pieces are removed, an incomplete two-root block reduces to a weighted rational-character discrepancy. This sharply identifies where a surviving sign can still enter: through incompleteness, through source-dependent weights, or through signed/complex structure that survives before aggregation.

MC-496 quantifies the first possibility when the only asymmetry is the interval endpoint. Classical completion gives an endpoint discrepancy of size `O(sqrt(p) log p)` at conductor `p`, leading to a relative bound of the form

`O(p^(-1/2) + sqrt(p) log(p)/L_x)`

for block length `L_x`. Hence once

`L_x >> sqrt(p) log(p) omega(p)`

with `omega(p) -> infinity`, endpoint truncation alone is `o(1)` and cannot sustain an order-one negative cross-root bias.

This creates a quantitative resolution floor for the cross-root route. Above the square-root-conductor scale, merely making a complete character pattern slightly incomplete is not enough. Any macroscopic signed effect must be carried by internal sieve/source weights, by a coefficient that remains signed or complex before the aggregation step, or by a different source-faithful correlation that is not reduced to endpoint discrepancy.

The conclusion strengthens MI-098: incompleteness is not a generic reservoir of cancellation. Its geometric endpoint component has a classical square-root threshold, so a successful continuation must identify a source-dependent survivor rather than attributing the needed sign to truncation in the abstract.

**Boundary.** The completion estimate controls endpoint-only incompleteness in the stated rational-character reduction. It does not prove that the remaining source or sieve weights generate the desired bias, and it does not exclude other pre-aggregation signed structures whose conductor or geometry differs from the MC-496 model.