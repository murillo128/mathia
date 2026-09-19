# MI-056 — Fixed-corridor real single-center rate two is forced into the vanishing-arc limit

**Evidence level:** exact synthesis from [RE-221](../../findings/RE-221-exact-single-center-remainder-retains-factor-two-floor.md) through [RE-225](../../findings/RE-225-fixed-corridor-contraction-boundary-forces-vanishing-arc.md), interpreted against the universal separated-prediction floor of RE-204--RE-218.

RE-221 shows that exact complex cancellation in the finite incomplete-beta remainder does not remove the factor-two Wiener obstruction for fixed positive-real center, fixed arc and fixed truncation ratio. RE-222 extends this uniformly over every compact subset of the interior contracting parameter domain: a real single-center family can approach normalized Wiener rate two only by leaving every such compact set.

RE-223 removes truncation collapse in a fixed delay corridor. RE-224 then uses the exact normalized finite polynomial to rule out unbounded real centers and approach to the upper arc edge. Before RE-225 this localized every putative rate-two sequence to two apparent singular geometries: `alpha_m->0` or contraction degeneration `r(alpha_m,a_m)->1`.

RE-225 proves that the second geometry is not independent. If `lambda_m=N_m/m` remains in a compact positive interval and uniform prediction holds, then for every fixed `alpha_0>0`,

`limsup_(alpha_m>=alpha_0) r(alpha_m,a_m) < 1`.

Equivalently,

`r_m -> 1  =>  alpha_m -> 0`.

At the rate-two frontier RE-223 already bounds `lambda_m` away from zero and the fixed corridor bounds it above. If `alpha_m` also stayed away from zero, RE-225 would keep `r_m` away from one and the remaining parameters would lie in a compact interior set, contradicting RE-222. Therefore every fixed-corridor positive-real single-center sequence approaching Wiener rate two must satisfy

`alpha_m -> 0`.

If the contraction boundary is approached inside that limit, the exact identity for `1-r_m^2` and boundedness of the center further force `a_m->1/2`. The former “contraction escape” therefore collapses into the corner `(alpha,a)->(0,1/2)` of the same vanishing-arc regime.

The reusable consequence is that the exact-remainder frontier is now genuinely localized. Interior retuning, truncation collapse, unbounded centers, upper-arc drift and fixed-width contraction degeneration are all nondecisive. The remaining real single-center question is the uniform small-arc incomplete-beta asymptotic, including the `(0,1/2)` corner.

**Boundary.** This is representation-local, not a universal lower bound `C_sep>1`. Broad corridors, complex centers, multi-center/minimax predictors, non-binomial bases and other representations remain outside the theorem; the global separated-prediction interval remains `1<=C_sep<=5.996390`.
