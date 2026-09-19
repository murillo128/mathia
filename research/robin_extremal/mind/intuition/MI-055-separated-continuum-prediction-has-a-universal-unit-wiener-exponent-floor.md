# MI-055 — Separated continuum prediction has a universal unit floor, while real single-center escapes are forced to genuine boundary regimes

**Evidence level:** exact synthesis from [RE-217](../../findings/RE-217-separated-continuum-prediction-has-a-unit-wiener-norm-floor.md) through [RE-223](../../findings/RE-223-narrow-separated-corridors-incur-a-superoscillatory-wiener-surcharge.md), using the continuous Kaiser coercive test of RE-215 and the ordinary-prime realization through RE-208.

Let `mu` be any finite complex measure supported on `[H,infinity)`, `H>0`, whose Fourier transform approximates the constant one on `[-T,T]` with error `epsilon<1`. RE-217 gives the source-independent lower bound

`||mu||_TV >>_H (1-epsilon) e^(HT)/(HT log(HT))`.

For a finite exponential predictor this is exactly a lower bound for the coefficient Wiener norm. If `C_sep` is the optimal leading exponent among fixed-corridor separated predictors with vanishing uniform error, RE-218 supplies the current global interval

`1 <= C_sep <= 5.996390`.

The factor two that appears in the explicit single-center construction is representation-local rather than global. RE-219 proves it for arbitrary positive-real parameter drift when the discarded negative-binomial tail is certified termwise in absolute value. RE-220 shows that a complex center phase does not help inside that certificate class: radialization weakly improves the worst-case contraction on the symmetric arc while preserving the exact truncated-polynomial Wiener norm.

RE-221 removes the triangle-inequality explanation for fixed real parameters. For fixed positive-real center, fixed symmetric arc and `N=lambda m+O(1)`, the exact truncated predictor is a regularized incomplete-beta polynomial. Even if the **actual complex polynomial remainder** is used, uniform prediction forces

`liminf log ||F_m||_A/(m alpha) >= 2`.

RE-222 shows that ordinary parameter drift is not an escape either. On every compact subset `K` of the interior contracting parameter domain, the same exact-remainder geometry is locally uniform and yields a strict margin

`liminf log ||F_m||_A/(m alpha_m) >= 2 + eta_K`, `eta_K>0`.

Thus any real single-center family approaching the factor-two boundary must leave every compact interior parameter set. Combined with RE-219, a hypothetical sub-two real single-center construction needs **both** a genuine degeneration and cancellation of the exact finite remainder that cannot be replaced by absolute-tail control.

RE-223 prices one degeneration without using the single-center algebra. If any finite complex repair measure is supported in `[H,RH]`, then a phase-aligned finite-difference operator gives

`||mu||_TV >= (1-epsilon) q_R^(-n)`,

`q_R=cos(pi/(R+1))`, `n=floor((R+1)HT/pi)`.

Hence

`C_sep(R) >= max(1,B(R))`,

`B(R)=((R+1)/pi) log sec(pi/(R+1))`.

The function `B` diverges as `R->1+`. It equals the universal unit floor at `R=1.430264606...`. For the negative-binomial single-center support ratio `R=1+lambda+o(1)`, any family with leading rate at most two must satisfy

`liminf lambda >= 0.062422318...`.

So `lambda->0` cannot be the singular route through the factor-two wall. In a fixed finite corridor, the truncation ratio of any putative rate-two real single-center escape can now be confined to a compact positive interval. The remaining degeneracy must occur in the arc/center geometry—such as `alpha->0`, approach to the contraction boundary, or an unbounded/endpoint center—while still using exact remainder cancellation. Several centers, minimax constructions and different approximation bases remain outside this classification.

The reusable separation is now precise. The **global** separated-measure problem pays at least exponent one. Fixed/interior real single-center exact-remainder predictors pay strictly more than two. Narrow support corridors pay an additional representation-independent superoscillatory surcharge. These costs constrain different classes and must not be conflated into one universal constant.

**Boundary.** The global interval remains `1<=C_sep<=5.996390`. RE-222 does not cover genuine boundary/infinite parameter regimes or exact complex-center cancellation. RE-223 depends only on finite support corridor `[H,RH]` and total variation, so it rules out corridor collapse but does not improve the global floor for broad support. No result here closes multi-center/minimax predictors or proves a new Robin inequality directly.
