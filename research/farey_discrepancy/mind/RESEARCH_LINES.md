# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Define the growing-block switched quotient before testing block-Mertens positivity

**Linked intuition:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-233 makes vanishing negative-capacity density necessary and sufficient for a positive lift inside a nontrivial switched-response class, and FD-234 identifies the canonical source-forced correction as `tilde c_N=-(1/2)(1*U_N)` modulo a capacity-negligible rounding term. FD-235 shows that the fixed-profile quotient is too coarse for this representative: for every fixed `N`, `tilde c_N` itself is switched-blind because its switched response is only `O_N(2^j)=o(4^j)`. Its affine class therefore contains zero and the fixed-`N` negative-capacity infimum is exactly zero.

The live coefficient question must use the same quantifier order as the growing reservoir construction. What source-derived normalization `L_N` and triangular blind class on `0<=j<J(N)` capture harmless adjustments uniformly while not automatically quotienting out the canonical block-Mertens repair? Once that class is fixed, does the normalized correction have a positive one-sided distance from the nonnegative cone, or can a uniformly blind family make its negative capacity negligible? A lower bound after freezing `N` cannot answer this question.

## Separate family-level coefficient positivity from discrete source realization

Even a nontrivial triangular positive lift would not construct an admissible prime occupancy. Integer multiplicities, finite reservoir capacities and the exact source-side constraints would still have to be realized. Conversely, failure of those discrete gates should not be folded into the coefficient-level question. The first task is to formulate a non-vacuous coupled `N,J(N)` quotient; only after that quotient survives the FD-235 control does its one-sided capacity distance become an arithmetic obstruction worth transporting to the discrete source.
