# MI-058 — Diagonal closure upgrades a familywise Wiener gap to a class gap

**Evidence level:** exact synthesis from `RE-226`--`RE-227` and elementary diagonal extraction.

RE-226 proves that every individual fixed-corridor positive-real single-center predicting family has normalized Wiener-rate liminf strictly larger than two, but its statement leaves open a logical loophole: perhaps differently tuned families have positive gaps `eta_j` that tend to zero.

RE-227 observes that the admissible class is sequentially closed under diagonal extraction. Fix a corridor ratio `R`. If families with gaps tending to zero existed, then from the `j`-th family one could choose one sufficiently late predictor with prediction error below `1/j`, prediction scale above `j`, corridor excess below `1/j`, and normalized rate below `2+2/j`. Those selected predictors form one new `R`-admissible family whose normalized rate tends to at most two.

That diagonal family is forbidden by RE-226. Therefore there exists a single constant `eta_R>0`, depending only on the fixed corridor ratio, such that every admissible family in this representation satisfies

`liminf log ||F||_A /(m alpha) >= 2+eta_R`.

The reusable principle is that **sequential strictness becomes a uniform class gap when the admissibility conditions survive diagonal extraction**. Before treating a family-wise positive margin as potentially nonuniform, check whether near-extremizers from different families can themselves be assembled into an admissible sequence. If they can, a vanishing sequence of margins would contradict the original sequential theorem.

**Boundary.** The argument gives existence, not a numerical value, of `eta_R`. Fixing `R` is essential; allowing the corridor ratio to diverge can leave the theorem class. The result is specific to the positive-real single-center representation and does not raise the universal separated-prediction floor `C_sep>=1`. Complex centers, multi-center/minimax predictors and other bases remain outside it.
