# Robin Extremal

## Research mandate

### Primary object

The line studies Robin's divisor-sum criterion for the Riemann hypothesis through the extremal arithmetic of

\[
R(n)=\frac{\sigma(n)}{n\log\log n},
\]

with special attention to superabundant and colossally abundant integers, their prime-exponent vectors, transition structure, and the mechanisms controlling maxima of normalized divisor sums.

The intrinsic discrete state is the factorization vector

\[
n=\prod_p p^{a_p},
\]

with finitely many nonzero exponents, together with the multiplicative contribution of each exponent to `sigma(n)/n` and the global `log log n` normalization.

### Objective

Find structural control of extremal normalized divisor sums that goes beyond finite verification or the known equivalence to RH: monotonicity or convexity along extremal transitions, rigorous restrictions on admissible counterexample exponent profiles, or a source-specific mechanism forcing Robin's inequality for all sufficiently large extremal integers.

A useful result should reduce or constrain the infinite extremal search by a theorem about prime-exponent geometry, not merely enumerate larger verified ranges.

### Priority questions

- Can consecutive colossally abundant or closely related extremal exponent profiles be connected by local moves with a monotone potential controlling `R(n)`?
- Is there a convex/variational formulation in logarithmic prime-exponent coordinates that identifies all possible near-maximizers and quantifies their distance from the Robin boundary?
- Can known prime-distribution estimates control the cumulative error between the optimal continuous exponent profile and the discrete prime-supported profile strongly enough to yield a new unconditional inequality?
- Are hypothetical Robin counterexamples forced into a progressively narrower family of exponent transitions that can be excluded by an independent arithmetic estimate?
- Can sensitivity of `R(n)` to adding/removing one prime power be expressed as a stable local criterion whose global accumulation is tractable?
- Which geometric or numerical patterns of extremal exponent vectors disappear under matched synthetic prime sequences, thereby isolating genuinely prime-specific information?

### Scope and exclusions

This line owns Robin-type normalized divisor-sum extremality and the discrete geometry of its extremal integer families. It does not own generic prime-distribution estimates once detached from the divisor-sum objective, nor other RH-equivalent inequalities unless they provide an exact bridge to this extremal structure.

Do not count finite verification, rediscovery of superabundant/colossally abundant reductions, or asymptotic maximal-order formulas as progress unless they produce a new infinite constraint relevant to the universal inequality.

### Line-specific falsification controls

Verify every claimed reduction to an extremal subsequence with an exact theorem; numerical observation that maxima occur on a familiar sequence is insufficient. Distinguish continuous relaxations from integer exponent vectors and bound the rounding/discretization error rather than assuming it is negligible.

Test candidate potentials against synthetic increasing prime-like sequences with comparable density. If the same monotonicity follows only from generic spacing and multiplicativity, it may not carry enough zeta-specific information. When importing prime-number-theorem error bounds, check whether the required strength is already RH-equivalent.

### Prior-art domains

- Robin's criterion and Gronwall maximal-order theory;
- superabundant and colossally abundant numbers;
- Alaoglu–Erdős-style extremal divisor-sum structure;
- explicit estimates for Chebyshev functions and prime distribution;
- multiplicative optimization and discrete/continuous variational methods;
- Lagarias and neighboring divisor-sum RH criteria when structurally relevant.

### Relationship to other lines

`analytic_frontier` can supply prime-distribution and explicit analytic estimates that may control errors in the extremal profile. `prime_lattice` and `prime_circle` may offer alternative representations of prime-supported exponent structure, but a transfer is relevant only if it yields an exact inequality for the Robin functional.

`visual_exploration` may inspect exponent-vector transitions and extremal landscapes as clue generators; canonical divisor-sum claims remain owned here.