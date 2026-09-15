# MI-020 — A conditional null is valid only if the tested observable lies outside its preserved sigma-field and remains nondegenerate inside the realized type

**Evidence level:** exact finite counting obstruction from [VIS-232](../../findings/VIS-232-transition-conditioned-collision-controls-are-occupancy-degenerate.md), sharpened by the first-order-type/range-two separation in [VIS-233](../../findings/VIS-233-lag-two-returns-escape-first-order-markov-type.md) and the exact type-conditional generating recursion [VIS-234](../../findings/VIS-234-markov-type-lag-two-pgf-recursion.md)

For phase-cell labels `x_1,...,x_m`, the unordered same-cell collision count is

`S=sum_j binom(N_j,2)`,

where `N_j` are the occupancy counts. Thus any confirmation-sample surrogate that preserves the realized occupancy histogram has `Var(S | N_1,...,N_J)=0`: it has conditioned away the statistic rather than supplied a stronger null.

Exact first-order transition-count preservation is even more restrictive than this scalar example suggests. The transition row and column sums determine the occupancies once the endpoint is fixed; hence an endpoint-matched transition-table-preserving randomization fixes `S`. VIS-233 proves the corresponding structural statement for the whole additive range-one class: endpoints plus the transition counts determine every translation-invariant observable of the form

`F=h(endpoints)+sum_t f(x_t)+sum_t g(x_t,x_(t+1))`.

No reweighting of states or adjacent transitions can recover conditional variability inside that exact first-order type.

The first simple escape occurs one interaction order higher. The lag-two return count

`T_2=sum_(t=1)^(m-2) 1_{x_t=x_(t+2)}`

depends on length-three block counts and need not be fixed by the same first-order type. VIS-233 gives the exact binary example `00010,00100,01000`: identical endpoints and transition counts, but `T_2=2,1,2`.

VIS-234 turns that existential escape into a type-specific admission theorem. For fixed first-order transition counts `C` and endpoints `s,t`, let `R` be the unused transition matrix and `(u,v)` the current suffix. The exact generating polynomial of additional lag-two returns satisfies

`F_(0;u,v)(q)=1_{v=t}`

and

`F_(R;u,v)(q)=sum_(w:R_vw>0) q^(1_{u=w}) F_(R-E_vw;v,w)(q)`.

Summing over the first transition gives `Z_(C;s,t)(q)`, whose coefficient of `q^k` is exactly the number of compatible state sequences with `T_2=k`. Therefore `T_2` is conditionally nondegenerate **if and only if `Z` is not a monomial**. Support, mean and variance can be propagated by the same finite state recursion, so one does not have to infer admissibility from a generic example or from an asymptotic Markov approximation.

This separates three operations that can look like the same “dependence control.” Fitting a stochastic Markov law on independent calibration data leaves confirmation occupancies random. Conditioning on the realized first-order type removes every additive range-one observable. Moving to a range-two statistic escapes that sigma-field only provisionally: the **actual realized type** may still make the statistic degenerate, and VIS-234 supplies the exact check.

The reusable admission rule is therefore two-stage. First, the null's preserved sigma-field must not algebraically contain the tested observable. Second, after passing that structural test, the observable must have nontrivial support under the **specific conditioned type used in the experiment**. Increasing interaction order is necessary when more local structure is preserved, but it is not sufficient until the realized-type recursion shows actual conditional variation.

**Boundary.** VIS-234 is a finite combinatorial calibration theorem, not evidence that `T_2` is prime-specific or asymptotically nondegenerate for the critical prime-phase types. The uniform conditional law on compatible state sequences is one explicit null; a scientifically justified nonuniform null requires the corresponding weighted recursion. Passing the nondegeneracy gate also does not show that a residual controls the signed prime-phase energy or RH.
