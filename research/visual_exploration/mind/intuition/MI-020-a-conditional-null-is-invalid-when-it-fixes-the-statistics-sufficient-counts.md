# MI-020 — A conditional null is valid only if the tested observable lies outside its preserved sigma-field

**Evidence level:** exact finite counting obstruction from [VIS-232](../../findings/VIS-232-transition-conditioned-collision-controls-are-occupancy-degenerate.md), sharpened by the first-order-type/range-two separation in [VIS-233](../../findings/VIS-233-lag-two-returns-escape-first-order-markov-type.md)

For phase-cell labels `x_1,...,x_m`, the unordered same-cell collision count is

`S=sum_j binom(N_j,2)`,

where `N_j` are the occupancy counts. Thus any confirmation-sample surrogate that preserves the realized occupancy histogram has `Var(S | N_1,...,N_J)=0`: it has conditioned away the statistic rather than supplied a stronger null.

Exact first-order transition-count preservation is even more restrictive than this scalar example suggests. The transition row and column sums determine the occupancies once the endpoint is fixed; hence an endpoint-matched transition-table-preserving randomization fixes `S`. VIS-233 proves the corresponding structural statement for the whole additive range-one class: endpoints plus the transition counts determine every translation-invariant observable of the form

`F=h(endpoints)+sum_t f(x_t)+sum_t g(x_t,x_(t+1))`.

No reweighting of states or adjacent transitions can recover conditional variability inside that exact first-order type.

The first simple escape occurs one interaction order higher. The lag-two return count

`T_2=sum_(t=1)^(m-2) 1_{x_t=x_(t+2)}`

depends on length-three block counts and need not be fixed by the same first-order type. VIS-233 gives the exact binary example `00010,00100,01000`: identical endpoints and transition counts, but `T_2=2,1,2`, so the uniform conditional ensemble has variance `2/9`.

This separates two operations that can look like the same “dependence control.” Fitting a stochastic Markov law on independent calibration data and resampling from it leaves confirmation occupancies random, so the VIS-230/VIS-231 center and variance remain meaningful. Conditioning on the realized first-order type is different: it removes all additive range-one observables, so a valid confirmation statistic must live at range two or beyond.

The reusable admission rule is **the null's preserved sigma-field must not already contain the tested observable**. Moreover, the interaction order of the statistic must outrun the order of the exact local structure being conditioned on: preserving length-two block counts forces a move to genuinely length-three information, while preserving length-three counts would condition `T_2` away again.

**Boundary.** VIS-233 proves only a finite combinatorial information boundary and the existence of a nondegenerate lag-two statistic inside one first-order type. It does not establish that `T_2` is prime-specific, that its conditional law is asymptotically nondegenerate for the actual prime-phase types, or that any surviving residual controls the signed prime-phase energy or RH.