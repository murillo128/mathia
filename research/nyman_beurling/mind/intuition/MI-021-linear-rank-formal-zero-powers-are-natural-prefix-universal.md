# MI-021 — Linear-rank formal zero powers make fixed natural-prefix data height-blind

**Evidence level:** exact Vandermonde interpolation and vertical-translation obstruction from [NB-130](../../findings/NB-130-linear-rank-formal-zero-power-packets-interpolate-arbitrary-natural-prefix-data.md) and [NB-131](../../findings/NB-131-exact-natural-prefix-data-remain-noncoercive-for-formal-burnol-mass.md)

Finite recurrence and zero-power analyticity become nonrestrictive on a length-`R` natural prefix when the formal packet is allowed rank `R`. NB-130 chooses distinct exponents

`rho_j = beta + i(T+j delta)`, `0<=j<R`,

with `1/2<beta<1` and `delta` small enough that the nodes `n^(i delta)`, `1<=n<=R`, are distinct. After factoring common row weights, evaluation on the prefix is an ordinary Vandermonde matrix. Hence **every** vector in `C^R` is represented exactly by these `R` simple right-half zero powers, even with arbitrarily high ordinate and arbitrarily narrow ordinate support.

NB-131 shows that absolute height does not restore coercivity. Translate one invertible support shape by an arbitrary vertical shift `S`. The natural-prefix evaluation matrix changes only by a unitary row modulation `V(S)=D_S V`, so the same prescribed prefix is recovered exactly for every `S` with

`c(S)=V^-1 D_S^-1 y`,

and both the singular values of `V(S)` and the coefficient bound in terms of `||V^-1||` are independent of `S`. Meanwhile the formal finite-packet Burnol defect decays like `O(S^-2)`. Thus **exactly identical finite natural-prefix data can coexist with arbitrarily small formal Burnol mass without paying any new conditioning cost merely from height**.

Along simultaneous phase-return heights, even the re-solved coefficient vector and any fixed collection of continuous periodic multibase recurrence descriptors return to their original values while the Burnol mass still tends to zero. Therefore a height-blind finite descriptor built from exact fixed-prefix data, coefficients, and finitely many periodic recurrence observables cannot supply a positive universal lower bound for the formal Burnol defect.

The cost remains rank and conditioning, not absolute height. The Vandermonde inverse may deteriorate catastrophically as `R` grows or the internal spacing shrinks; NB-131 does not remove that gate. Nor can actual zeta zeros be vertically translated at will. The durable separator is therefore quantitative and source-specific: **effective rank versus visible depth, uniform coefficient/model-space conditioning, or actual-zero geometry must enter.** Analyticity, finite recurrence, fixed natural-prefix equality, high ordinate, narrow support, and any fixed amount of height-blind recurrence data do not suffice on their own.
