# MI-020 — A conditional null must leave the observable variable inside the actual representation support

**Evidence level:** exact finite counting and representation-support obstruction from [VIS-232](../../findings/VIS-232-transition-conditioned-collision-controls-are-occupancy-degenerate.md) through [VIS-236](../../findings/VIS-236-ordered-prime-coordinate-cells-make-first-order-type-degenerate.md).

For phase-cell labels `x_1,...,x_m`, the unordered same-cell collision count is

`S=sum_j binom(N_j,2)`,

where `N_j` are the occupancy counts. Thus any confirmation-sample surrogate that preserves the realized occupancy histogram has `Var(S | N_1,...,N_J)=0`: it has conditioned away the statistic rather than supplied a stronger null.

Exact first-order transition-count preservation is even more restrictive. The transition row and column sums determine the occupancies once the endpoint is fixed; hence an endpoint-matched transition-table-preserving randomization fixes `S`. VIS-233 proves the corresponding structural statement for the whole additive range-one class: endpoints plus transition counts determine every translation-invariant observable of the form

`F=h(endpoints)+sum_t f(x_t)+sum_t g(x_t,x_(t+1))`.

In a **generic** first-order type, moving one interaction order higher can escape that preserved sigma-field. The lag-two return

`T_2=sum_(t=1)^(m-2) 1_(x_t=x_(t+2))`

need not be fixed by the same transition counts. VIS-234 supplies the exact type-conditional generating polynomial `Z_(C;s,t)(q)`, so `T_2` is conditionally nondegenerate exactly when `Z` is not a monomial; VIS-235 gives a cheaper exact mean and zero-support gate by two-step deletion.

VIS-236 shows why this algebraic escape criterion is still insufficient for the actual prime-coordinate representation. The coherence cells are ordered intervals and the primes are listed increasingly, so the realized labels are nondecreasing. Every occupied cell occurs in one contiguous block. Consequently

`T_2=sum_j (N_j-2)_+`,

and the exact endpoint-matched transition table has only one compatible label sequence. Its conditional PGF is therefore a monomial for structural reasons at every finite scale, not merely for an unlucky numerical instance.

This exposes a third admission gate beyond “the statistic is outside the preserved sigma-field” and “the realized conditional law has nonzero variance”: **the null sample space itself must respect the support of the representation being tested**. A generic Markov type may contain revisits and backtracking that an ordered prime-coordinate path can never realize. Enlarging the sample space until `T_2` varies would manufacture null freedom rather than calibrate the actual geometry.

The reusable admission rule is therefore representation-relative. First identify what the null preserves and verify that the statistic is not algebraically measurable from it. Then verify nondegeneracy inside the specific conditional type. Finally verify that the conditional/randomized configurations are themselves realizable within the representation's structural support. Failure at any stage invalidates the proposed confirmation test.

For the current critical prime-coordinate cells, this moves the live object away from permutations of cell labels. A representation-matched dependence control must randomize something that can genuinely vary while preserving monotonicity: the ordered occupancy/count process, normalized prime gaps, within-cell point locations, or another increasing-point-process description. Any proposed statistic must prove its own variability under that support before prime specificity is tested.

**Boundary.** VIS-236 does not invalidate the generic Markov-type combinatorics of VIS-233--VIS-235 and does not show that all phase representations are monotone. It closes the exact first-order-type/lag-two-label route only for the ordered prime-coordinate interval representation. A different justified representation may have a nontrivial type class, and a monotone gap/count statistic may still carry a source-specific residual. No such residual or RH consequence is established here.