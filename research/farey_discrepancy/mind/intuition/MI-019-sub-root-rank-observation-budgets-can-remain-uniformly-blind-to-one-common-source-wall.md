# MI-019 — Sub-root-rank observation budgets can remain uniformly blind to one common source wall

**Evidence level:** exact probabilistic-method no-go theorem from [FD-143](../../findings/FD-143-sub-root-rank-observation-budgets-still-admit-a-common-hidden-wall.md), extending the fixed-alphabet wall of [FD-140](../../findings/FD-140-every-fixed-congruence-coordinate-alphabet-misses-a-finer-prime-color-wall.md) into a genuinely growing observation regime.

Let every parent in the observed squarefree domains have at least `r_T` prime factors. For `K_T` active primes, allow an arbitrary source-independent partition into at most `M_T` cells per prime. No congruence, additivity or regularity of the cells is required.

FD-143 proves that if

`K_T M_T = o(sqrt(r_T))`,

then one fixed infinite prime coloring and one fixed orientation admit a subsequence on which **every** observed prime-cell ancestry defect tends to zero, while the same coefficient source remains wrong on at least half of one fixed active-prime parent domain up to `o(1)`. In the central Farey regime `r_T~log log T`, the blind range is therefore

`K_T M_T=o(sqrt(log log T))`.

The mechanism is a capacity law rather than a coordinate-specific trick. For a parent with `k` prime factors, an ancestry defect can occur only when a Rademacher sum of length `k` hits one of the central lattice levels, whose point mass is `O(k^-1/2)`. Summing that anti-concentration cost over all prime-cell constraints gives the product `K_T M_T/sqrt(r_T)`. A sparse subsequence and Borel--Cantelli/Markov selection turn the finite-horizon random coloring into one common infinite source.

This complements MI-018 rather than contradicting it. MI-018 says one exact scalar with `Theta(log T)` source-identity bits can already reconstruct the squarefree source. FD-143 says the opposite end of the middle regime is still noncoercive even when the observation alphabet grows and its cells are arbitrary. **Noninjective is not the same as coercive, and growing is not the same as source-resolving.**

The live information question is now quantitative: what source-native observation law crosses the Rademacher anti-concentration budget while staying genuinely below source reconstruction? Candidate improvements must price effective cell/entropy complexity and provenance, not merely add coordinates or permit a slowly growing partition.

**Boundary.** The `sqrt(r_T)` scale is a proved lower-bound frontier, not a sharp threshold. FD-143 assumes the partitions are fixed independently of the hidden source and obtains one common source only along a subsequence. It does not show that `K_T M_T` of order `sqrt(r_T)` is sufficient for coercivity, nor that a source-dependent or structurally Farey-derived observation obeys the same bound.