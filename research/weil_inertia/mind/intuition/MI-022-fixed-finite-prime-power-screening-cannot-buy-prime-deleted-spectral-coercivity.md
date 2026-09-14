# MI-022 — Fixed finite prime-power screening cannot buy prime-deleted spectral coercivity

**Evidence level:** exact obstruction from [WI-285](../../findings/WI-285-fixed-finite-prime-power-screening-cannot-control-prime-deleted-inertia.md), sharpening the support-sensitive target of [WI-284](../../findings/WI-284-complete-screening-forces-a-prime-deleted-critical-support.md). No statement is made for screening by the full aperture-growing active prime family.

WI-284 turns complete one-signed screening into an operator-domain condition: on the positivity support `E`, all active prime translations disappear from the whole supported form domain, so the prime-deleted gamma-plus-pole form must be nonnegative with bottom exactly zero. This makes support-sensitive spectral exclusion the correct target.

WI-285 now identifies what kind of support information cannot prove that exclusion. Fix any finite set of prime bases. One can choose arbitrarily small, full-span two-component supports whose separation avoids **every positive power of every chosen prime**, so every corresponding autocorrelation is screened exactly. Yet the same support contains an odd direction whose prime-deleted Rayleigh quotient tends to `-infinity` as the component separation grows.

The mechanism is exact. Avoiding finitely many lattices `k log p` costs only a small measure fraction of possible separations. On the resulting separated support, the gamma multiplier contribution stays uniformly bounded under translation, while the odd pole term grows exponentially negative because the two components are weighted oppositely by `e^(x/2)`. Support sparsity, full span, and fixed-family distance avoidance therefore coexist with arbitrarily bad prime-deleted energy.

This rules out a broad finite-information shortcut. **No argument using only a fixed finite collection of prime-power lattices, support measure/span, or the associated packing constraints can force the WI-284 zero-criticality condition.** Even the maximal support-domination topology for that fixed lag family can be added without removing the negative direction.

The exact boundary is the growing arithmetic family. In the actual first-crossing problem, the active prime bases increase with the aperture. The finite-lattice avoidance count that builds the counterexample is not uniform in that regime. A successful theorem must therefore exploit the collective diversity of the aperture-growing prime family, quantitative amplitudes from the null equation, or another source-specific coupling that prevents the separated odd pole instability.

The reusable distinction is **finite screening versus growing-family rigidity**. Screening arbitrarily many powers of finitely many generators can still leave huge geometric freedom; what may matter is the number and arithmetic diversity of independent base lattices growing with scale, not depth along a fixed finite family.

**Boundary.** WI-285 does not construct a completely screened Suzuki null mode and does not refute the WI-284 route. It shows only that finite-base shadows of complete screening are too weak. Any use of this obstruction must preserve that quantifier distinction.