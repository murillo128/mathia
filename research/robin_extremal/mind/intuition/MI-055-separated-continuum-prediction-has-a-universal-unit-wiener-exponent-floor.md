# MI-055 — Separated continuum prediction has a universal unit floor, while single-center absolute tails have a factor-two floor

**Evidence level:** exact synthesis from [RE-217](../../findings/RE-217-separated-continuum-prediction-has-a-unit-wiener-norm-floor.md) through [RE-219](../../findings/RE-219-single-center-absolute-tail-prediction-has-a-factor-two-wiener-floor.md), using the continuous Kaiser coercive test of RE-215 and the ordinary-prime realization through RE-208.

Let `mu` be any finite complex measure supported on `[H,infinity)`, `H>0`, whose Fourier transform approximates the constant one on `[-T,T]` with error `epsilon<1`. RE-217 upgrades the signed-prefix obstruction to a direct total-variation bound

`||mu||_TV >>_H (1-epsilon) e^(HT)/(HT log(HT))`.

For a finite exponential predictor this is exactly a lower bound for `sum_j |b_j|`. Thus at logarithmic height `T_Q=c log Q`, every separated predictor with coefficient variation `Q^(kappa+o(1))` satisfies the spectral floor `kappa>=Hc`. If `C_sep` is the optimal leading Wiener exponent among fixed-corridor separated predictors with vanishing uniform error, RE-218 gives

`1 <= C_sep <= 5.996390`.

RE-219 shows that the gap above one is not removable by further scalar tuning inside the current constructive proof architecture. Consider the whole single-positive-real-center negative-binomial family used by RE-216--RE-218, and require the discarded tail to be controlled by summing the absolute values of its terms. Uniformly vanishing tail error forces truncation beyond the positive exponential mode; at the first asymptotically admissible truncation, the coefficient `ell^1` exponent is strictly greater than twice the observed arc width. Consequently the optimal leading exponent in this subclass satisfies

`2 <= C_(1c,abs) <= 5.996390`.

This factor two is pointwise in the admissible center/arc/truncation parameters, so letting them drift with `T` can approach but not cross the boundary. It is also representation-local. It does **not** improve the universal lower bound `C_sep>=1`, because several centers, complex centers, different approximation bases or cancellation-sensitive remainder estimates lie outside the theorem.

The distinction is reusable: **a lower bound can belong to the approximation certificate rather than to the underlying prediction problem**. RE-217 prices every separated measure through a source-independent coercive test. RE-219 prices only one way of constructing and certifying a predictor, and therefore tells us where optimization effort inside that representation becomes futile without claiming a stronger physical/source obstruction.

RE-208 already realizes every regular discrete predictor with strict coefficient exponent below `1/2`, so a construction with global `C_sep=1` would still reach every fixed `c<1/(2H)`, the leading bounded-prime carrier-capacity ceiling. RE-219 says that such a construction cannot come from single-center absolute-tail negative-binomial prediction. The constructive search must change approximation geometry or preserve analytic cancellation in the tail.

**Boundary.** The global interval remains `1<=C_sep<=5.996390`. RE-219 neither proves `C_sep>=2` nor rules out near-unit predictors outside its representation class. Its contribution is to separate the universal Wiener floor from a stricter proof-architecture floor and to identify exactly which ingredient must change before the remaining leading-order gap can close.