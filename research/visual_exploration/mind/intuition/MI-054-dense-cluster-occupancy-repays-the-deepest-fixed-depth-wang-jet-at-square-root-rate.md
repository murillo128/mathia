# MI-054 — Dense cluster occupancy repays the deepest fixed-depth Wang jet at square-root rate

**Evidence level:** exact finite-dimensional synthesis from [VIS-358](../../findings/VIS-358-dense-cluster-occupancy-width-floor.md), interpreted against the square-anchor packing collapse of VIS-357. Polynomial sampling, Vandermonde conditioning and finite-dimensional Gram convergence are classical; the line-specific content is the quantitative full-map boundary for the canonical compact Wang cluster.

At fixed asymptotic depth `q`, take `N` equally spaced inverse scales in a cluster of width `2epsilon` around a positive center, with the current unweighted Euclidean coefficient norm. For the full rectangular Wang moment map `A_(N,epsilon)`,

`s_q(A_(N,epsilon)) asymp sqrt(N) epsilon^(q-1)`.

Equivalently, the smallest positive Gram eigenvalue is of order `N epsilon^(2(q-1))`. The factor `epsilon^(q-1)` is the deepest available cluster jet: a degree-`q-1` polynomial can vanish at the cluster center to exactly that order. Dense occupancy then contributes the compensating `sqrt(N)` sampling factor.

This separates square-anchor collapse from full quotient collapse. Every fixed `q`-column anchor can degenerate as `epsilon->0`, yet the full map remains uniformly conditioned when `N epsilon^(2(q-1))` stays bounded below and can become better conditioned when that product grows. Raw pairwise collision or loss of every square minor is therefore only a warning, not a compact escape mechanism.

The next compact question is no longer the regular one-cluster width/count tradeoff. A genuine degeneration must come from something VIS-358 does not control: an irregular scaled sampling cloud whose fixed-degree Gram degenerates, several clusters with a nontrivial allocation of jet orders, nonuniform weights or a changed coefficient norm/topology. Those resources must be stated explicitly because they replace `N` by a different effective sampling mass.

**Boundary.** The theorem is canonical and finite-dimensional: one equally spaced cluster, fixed `q`, fixed positive center, fixed invertible tail scaling, and the existing Euclidean bank norm. It does not classify arbitrary irregular or multicluster banks, growing `q`, scale escape, weighted topologies, or infinite-dimensional limits.