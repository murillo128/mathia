# MI-028 — Global density rarity is not worst-cell coercivity

**Evidence level:** exact/literature-derived source boundary from [NB-141](../../findings/NB-141-selberg-density-makes-polynomial-confluence-cells-rare-but-not-forbidden.md), applied to the target-poor complex confluence geometry of [NB-140](../../findings/NB-140-complex-confluence-cells-remain-target-poor.md).

NB-140 identifies a local target obstruction: a logarithmic-rank packet of simple zeros inside a sufficiently small two-dimensional complex cell converges to a confluent state space whose normalized Nyman-target projection vanishes. The relevant local variable is whole-cell occupancy plus diameter, not minimum spacing or the conditioning of a chosen basis.

NB-141 asks what the actual zeta source laws already say about those cells. Selberg zero density implies that at fixed horizontal displacement `a`, the centers in `[G,2G]` whose radius-`Delta_G` cell contains `c log G` right-half zeros have measure

`|E_G| <<_(a,c) Delta_G G^(1-a/8)`.

For `Delta_G=G^-B`, their relative height measure is `O(G^(-B-a/8))`. Thus dangerous confluence cells are genuinely power-law rare in height.

That gain is still the wrong quantifier for the Nyman endpoint. A sparse sequence of exceptional cells is enough to preserve the target-poor obstruction, and NB-141 constructs a simple zeta-symmetric matched divisor satisfying the explicit global zero-count envelope, the same Selberg density envelope and the zero-free region while containing infinitely many logarithmic-rank polynomial cells. The construction is not asserted to be the actual zeta divisor; it proves that the currently imported global laws do not encode uniform local exclusion.

The reusable distinction is **population control versus worst-cell coercivity**. An upper density theorem can make bad configurations arbitrarily rare without making them impossible. If the downstream theorem takes a supremum, allows an exceptional subsequence, or can be defeated by one local packet at each of infinitely many heights, then average rarity is not a substitute for a uniform local law.

A stronger global density exponent changes the measure estimate but not this logical boundary. The source theorem needed by the present route must couple directly to local packet geometry: for example a uniform `o(log G)` occupancy bound on the forbidden cells, or a theorem that an actually crowded cell must carry nonvanishing Nyman-target projection. Merely improving the exponent in `N(sigma,T)` does not change the quantifier mismatch.

**Boundary.** NB-141 does not show that the actual zeta zeros realize the matched exceptional cells, and it does not prove that no global theorem can imply a local bound when combined with additional structure. The negative statement is only that the current zero-count, zero-density and zero-free envelopes, taken at their present information level, permit sparse target-poor cells. The missing resource may come from the Euler product, explicit-formula coupling, local zero interaction or another genuinely relational source law.