# MI-056 — Fixed-corridor real single-center prediction can approach rate two only through two singular geometries

**Evidence level:** exact synthesis from [RE-221](../../findings/RE-221-exact-single-center-remainder-retains-factor-two-floor.md) through [RE-224](../../findings/RE-224-fixed-corridor-exact-single-center-prediction-excludes-unbounded-centers.md), interpreted against the universal separated-prediction floor of RE-204--RE-218.

RE-221 shows that exact complex cancellation in the finite incomplete-beta remainder does not remove the factor-two Wiener obstruction for fixed positive-real center, fixed arc and fixed truncation ratio. RE-222 extends the obstruction uniformly over every compact subset of the interior contracting parameter domain: a real single-center family can approach normalized Wiener rate two only by leaving every such compact set.

RE-223 removes one obvious degeneration independently of the single-center formula. Any repair measure supported in a finite corridor `[H,RH]` pays a corridor-dependent superoscillatory floor `B(R)`, and within the single-center corridor `R=1+lambda+o(1)` a rate-two sequence must keep the truncation ratio bounded away from zero.

RE-224 removes two more apparent escape directions using the **exact normalized finite polynomial**, before any absolute-tail or incomplete-beta asymptotic estimate. For

`F_(m,N,a)(z)=Q_(m,N,a)(z)/Q_(m,N,a)(1)`

with positive real center `a>1`, uniform prediction on `|theta|<=alpha_m` and `m alpha_m -> infinity` forces

`(((m-1)-N/(a-1))_+) / (m+N/(a-1)) -> 0`.

If `lambda_m=N_m/m` is bounded above, this implies

`limsup a_m <= 1 + limsup lambda_m`.

Thus a fixed-corridor exact predictor cannot send its real expansion center to infinity. Combined with the contraction condition, the observed arc also stays uniformly away from `pi/2`.

At the rate-two frontier RE-223 already bounds `lambda_m` away from zero, while the fixed corridor bounds it above. RE-224 then bounds the center above; contraction bounds it below. If both the arc width `alpha_m` stayed away from zero and the contraction ratio `r(alpha_m,a_m)` stayed away from one, the parameters would remain in a compact interior set and RE-222 would force a uniform gap above two. Therefore every putative fixed-corridor positive-real single-center rate-two sequence must satisfy, along a subsequence,

`alpha_m -> 0`  **or**  `r(alpha_m,a_m) -> 1`.

This is a strong localization of the representation-specific frontier. Unbounded centers, approach to the upper arc endpoint, truncation collapse and ordinary interior retuning are no longer independent possibilities. Exact-remainder analysis only needs to understand two singular geometries and their interaction.

The next useful object is a uniform incomplete-beta normal form in those regimes. If the exact normalized remainder still carries a strict Wiener gap above two as `alpha->0` and/or `r->1` within a fixed corridor, the entire positive-real single-center route is closed. If one regime reaches rate two, the mechanism must come from genuinely singular boundary cancellation rather than ordinary parameter optimization.

**Boundary.** This is a representation-local statement, not a universal lower bound `C_sep>1`. Broad corridors with `lambda->infinity`, complex centers, multi-center or minimax predictors, non-binomial bases and other representations remain outside it. The global separated-prediction interval remains `1<=C_sep<=5.996390`.
