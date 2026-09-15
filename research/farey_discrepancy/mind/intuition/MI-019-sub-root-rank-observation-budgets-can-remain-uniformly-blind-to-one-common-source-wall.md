# MI-019 — Sublinear-rank observation budgets can remain uniformly blind to one common source wall

**Evidence level:** exact probabilistic-method no-go theorem from [FD-144](../../findings/FD-144-min-wise-prime-selectors-defeat-sublinear-rank-ancestry-observation-budgets.md), sharpening the growing-observation obstruction of [FD-143](../../findings/FD-143-sub-root-rank-observation-budgets-still-admit-a-common-hidden-wall.md).

Let every observed squarefree parent have at least `r_T` prime factors. For `K_T` active primes, allow arbitrary source-independent normalized nonnegative tests with total per-prime complexity bounded by `M_T`. FD-144 constructs one fixed infinite prime coloring and a subsequence on which every such observed ancestry defect tends to zero whenever

`K_T M_T=o(r_T)`,

while one fixed orientation of the same source remains macroscopically wrong on an active-prime parent domain. In the central Farey regime `r_T~log log T`, the blind range is therefore `o(log log T)` rather than the earlier `o(sqrt(log log T))` range.

The mechanism is no longer Rademacher central anti-concentration. A min-priority selector assigns the defect event to the least-ranked prime in the parent support; for a parent with `k` prime factors, a fixed active prime is selected with probability `1/k` up to the orientation factor. Summing this `O(1/r_T)` exposure over the source-independent observation budget and applying the common-source selection argument leaves one infinite coloring that defeats all tests along a subsequence.

This sharpens the information-capacity lesson. A growing observation family can remain noncoercive almost up to the natural multiplicative-rank scale. The relevant question is not whether the alphabet grows, but whether the source-native observation budget reaches and structurally uses enough independent rank information without becoming an indirect label for the squarefree parent.

The live theorem must therefore use information not covered by this matched family: at least linear-rank effective observation complexity, source-dependent/Farey-derived structure, signed constraints outside the normalized nonnegative class, or a theorem excluding the matched prime-color source for the physical coefficients. None of those is supplied merely by increasing coordinate count.

**Boundary.** `o(r_T)` is a proved blind regime, not a sharp coercivity threshold. FD-144 keeps the observation family source-independent and obtains one common source along a subsequence. It does not show that `Theta(r_T)` tests suffice, does not cover every possible signed/source-adaptive observable, and does not weaken the separate circularity warning that sufficiently precise observations can reconstruct the source outright.