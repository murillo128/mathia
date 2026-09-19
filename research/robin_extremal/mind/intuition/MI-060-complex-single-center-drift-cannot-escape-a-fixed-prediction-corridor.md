# MI-060 — Complex single-center drift cannot escape a fixed prediction corridor

**Evidence level:** exact synthesis from [RE-229](../../findings/RE-229-bounded-complex-single-center-vanishing-arcs-have-divergent-wiener-rate.md) and [RE-230](../../findings/RE-230-unbounded-complex-single-centers-force-corridor-blowup.md), extending RE-223--RE-228.

The remaining single-center loophole after the fixed-parameter analysis was to let the complex center drift with scale. RE-229 closes the bounded-modulus vanishing-arc branch: arbitrary phase drift does not prevent the normalized negative-binomial predictor from paying a divergent Wiener rate in the relevant contracting regime.

RE-230 closes the complementary unbounded-center branch inside every fixed delay corridor. If `|a_m|->infinity` and

`eta_m=N_m/(m|a_m-1|)->0`,

then on the microscopic angular scale `theta=u/m` the normalized predictor converges uniformly on compact `u`-intervals to the raw delay `e^(-iu)`. The off-center correction has become too weak to flatten the original `z^m` phase. Hence prediction on arcs with `m alpha_m->infinity` is impossible in this regime.

Any unbounded-center sequence that does predict must therefore satisfy a necessary lower bound

`liminf N_m/(m|a_m-1|)>0`.

In a fixed delay corridor `N_m/m<=Lambda`, this cannot coexist with `|a_m|->infinity`. The would-be large-center escape is paid for by corridor width: keeping it alive forces `N_m/m` to diverge at least proportionally to the center modulus.

Together, RE-229 and RE-230 change the quantifier audit. Merely allowing the center to depend on scale is not a new geometry if the whole family remains inside the same fixed single-center delay architecture. A viable escape now needs a genuine category change such as widening corridors, multi-center/minimax cancellation, rational or different approximation bases, or another representation whose microscopic normal form is not the raw delay.

**Boundary.** RE-229 and RE-230 cover complementary regimes under their stated single-center negative-binomial hypotheses; they do not prove the universal separated-measure constant, classify the transition `N/(m|a-1|)=Theta(1)` in widening corridors, or address multi-center and other predictor classes.