# MI-028 — Exact zero incidence is thinner than stable access

**Evidence level:** exact for saturated equal-weight finite Dirichlet sums on the imaginary axis through AF-308, with the prime-support exact classification still open for `k>=5`.

For a saturated `k`-term equal-weight Dirichlet sum, quotient the common phase and write the frequency differences as `nu in R^(k-1)`. AF-308 identifies the exact-zero condition with incidence of the one-parameter orbit `t nu` with the lifted equilateral-polygon zero locus. The latter has local dimension `k-3`; adjoining the free hit-time scale gives an exceptional frequency cone `E_k` of Hausdorff dimension at most `k-2`. Thus for every `k>=3`, exact zero frequencies occupy a Lebesgue-null subset of the ambient `(k-1)`-dimensional frequency space.

This does not create a stable margin. Rational independence makes the corresponding torus orbit dense, so it approaches the polygon-zero locus arbitrarily closely and `inf_t |F_nu(t)|=0` even when no exact hit occurs. Almost every frequency vector therefore has the combination **exactly zero-free but arbitrarily close to zero**.

Prime-log differences are rationally independent by unique factorization, so every fixed prime support lies on the zero-margin side. But generic measure-zero reasoning cannot decide whether the special arithmetic vector lies in `E_k`. AF-307 settles `k=3,4` negatively by stronger exact arguments; from `k>=5` onward the missing theorem is an arithmetic incidence/resonance theorem for logarithms of prime ratios, not another density theorem.

The reusable distinction is sharp: closure access to the failure locus, exact membership in the failure locus, and positive distance from the failure locus are separate properties. A representation can be exact-failure-free while remaining maximally ill-conditioned, and generic codimension does not classify a structured arithmetic family.

**Boundary.** The cone estimate is generic in continuous frequency space and says nothing by itself about a given prime tuple. It does not classify unequal weights, nonzero real part, nonlinear/vector observations, or infinite supports.