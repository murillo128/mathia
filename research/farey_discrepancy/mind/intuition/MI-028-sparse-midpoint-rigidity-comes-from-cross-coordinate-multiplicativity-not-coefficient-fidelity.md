# MI-028 — Sparse midpoint rigidity comes from quantitative cross-coordinate multiplicativity, not near-maximal coefficient fidelity

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-180](../../findings/FD-180-subpolynomial-deletion-sources-pay-an-exact-prime-extension-defect-floor.md). The quantitative rigidity statement is proved only for the deletion-only class with physical prime coefficients; extension to signed perturbations or moving prime data remains open.

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while sparse geometric horizons become target-rigid inside the genuinely multiplicative squarefree source class. FD-175--FD-179 show that this rigidity is not explained by knowing primes, signs, low multiplicative ranks, or even coordinatewise agreement through essentially the entire squarefree-rank range.

For the dyadic ladder, deletion-only sources `a(n) in {0,mu(n)}` can match every sampled midpoint while agreeing with Möbius outside a subpolynomial defect set confined to an exceptionally thin high-rank shell. FD-179 pushes the protected region to the exact maximal-rank boundary minus an `o(first-correction)` cap. Coordinate fidelity can therefore be almost maximal while the product law is still false.

FD-180 identifies the first quantitative relational separator for that escape. If all prime coefficients remain physical and the deletion set `S` is subpolynomial, then the prime-extension defect boundary satisfies

`B_a(x) = (C_S+o(1)) x/log x`,  where  `C_S=sum_(n in S) 1/n`.

Since the full squarefree prime-extension graph has size `~ x loglog x / zeta(2)`, the normalized finite-`L^q` multiplicativity defect is

`((zeta(2) C_S+o(1))/(log x loglog x))^(1/q)`.

Thus **full multiplicativity is stronger than necessary in this source class**. It already suffices to demand prime-extension consistency that beats the natural sparse-boundary scale: an `o((log x loglog x)^(-1/q))` normalized defect forces `S` empty and hence `a=mu`. Conversely, merely requiring average multiplicativity to tend to zero is still too weak, because the permanent dyadic-null source does exactly that at the boundary rate.

The reusable lesson is now quantitative. A relational law should be priced by the boundary it forces a sparse repair to emit, not by the number or extremal rank of individually correct coefficients. Sparse coordinate errors may be invisible to the observation operator yet unavoidable on a much larger relation graph.

**Boundary.** FD-180 is source-class specific. Arbitrary signed perturbations can cancel relation defects, prime coefficients may themselves move, and a different relation graph can have a different boundary scale. Even perfect source identification does not prove the Franel--Landau RH-critical estimate. The next structural step is to find a comparably quantitative relation that survives a broader admissible source class and then show that its coercivity reaches the discrepancy destination rather than only reconstructing the source.