# MI-083 — Sparse relational asymmetry can preserve full factor-state capacity without carrying source diversity

**Evidence level:** exact group-action and canonical-order synthesis from [MC-433](../../findings/MC-433-sparse-relational-asymmetry-retains-bell-capacity.md) and [MC-434](../../findings/MC-434-canonical-prime-order-rigid-zero-source-type-diversity.md). Burnside/orbit bounds, graph automorphisms and finite-order rigidity are classical; the line-specific content is the separation of internal factor addressability from source-varying arithmetic information.

Let `R` be a retained relation on the `r` distinct prime coordinates of a squarefree integer and `G=Aut(R)`. If `Pi(P)` is the Bell family of unordered prime-block factorizations, the surviving states after forgetting literal labels but retaining `R` are `Pi(P)/G`, so

`B_r/|G| <= Q_R <= B_r`.

With `A(R)=log(r!/|Aut(R)|)`, Bell asymptotics imply that `|Aut(R)|=exp(o(r log r))` already preserves near-full primorial-scale Bell capacity. Thus edge count, bounded degree or a finite relation alphabet are not standalone information budgets: a sparse rigid relation can individualize every prime coordinate.

MC-434 adds a distinct gate that the automorphism count does not see. Order the prime divisors canonically and retain only the directed successor relation. This relation has `Aut=1`, hence preserves all `B_r` factor partitions, but for fixed `r` every such successor structure is isomorphic to every other one. Its **conditional source-type diversity is exactly one**. Rigidity measures addressability inside one source instance; it does not measure how much the relational isomorphism type varies as the arithmetic source changes.

The distinction survives the Möbius-facing projection. Factorwise Möbius signs depend on block cardinalities, not on the rank positions supplied by the universal successor scaffold. The canonical order can therefore pass both the Bell-capacity test and the “generated canonically from the source” test while contributing no source-specific variation to the signed observable.

The durable audit for a relational lift now has three separate gates: internal addressability after the actual automorphism quotient; conditional source diversity after coarse invariants such as `omega(n)` are fixed; and post-projection survival of that varying datum in the signed analytic quantity. A construction only earns arithmetic information credit after all three are visible.

**Boundary.** A universal rank scaffold can still be useful coordinates, and weighted or decorated successor relations are not ruled out. Their gaps, ratios, residues, labels or edge weights must themselves supply nontrivial source-varying isomorphism data and that variation must survive the Möbius-facing operation. Passing the representation-capacity test is necessary but is not analytic progress by itself.