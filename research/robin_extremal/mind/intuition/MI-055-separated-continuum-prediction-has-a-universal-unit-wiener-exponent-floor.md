# MI-055 — Separated continuum prediction has a universal unit Wiener-exponent floor

**Evidence level:** exact synthesis from [RE-217](../../findings/RE-217-separated-continuum-prediction-has-a-unit-wiener-norm-floor.md), using the continuous Kaiser coercive test of RE-215 and the constructive predictor/prime-realization interface through RE-216.

Let `mu` be any finite complex measure supported on `[H,infinity)`, `H>0`, whose Fourier transform approximates the constant one on `[-T,T]` with error `epsilon<1`. RE-217 upgrades the signed-prefix obstruction to a direct total-variation bound:

`||mu||_TV >>_H (1-epsilon) e^(HT)/(HT log(HT))`.

For a finite exponential predictor this is exactly

`sum_j |b_j| >>_H (1-epsilon) e^(HT)/(HT log(HT))`.

Thus at logarithmic height `T_Q=c log Q`, every separated predictor with coefficient variation `Q^(kappa+o(1))` satisfies the **spectral lower floor**

`kappa >= Hc`.

This isolates a clean continuum approximation constant. If `C_sep` is the optimal leading Wiener exponent among fixed-corridor separated predictors with vanishing uniform error, current results give

`1 <= C_sep <= 6.081`.

The lower endpoint is universal RE-217 coercivity; the upper endpoint is the explicit off-center binomial family of RE-216. The interval is no longer mixed with the prime-placement problem. RE-208 already realizes every regular discrete predictor with strict coefficient exponent `kappa<1/2`, so a spectral construction with `C_sep=1` would let the existing arithmetic interface reach every fixed `c<1/(2H)`, exactly the leading bounded-prime carrier-capacity ceiling isolated by RE-214--RE-215.

The same floor cannot be hidden by spreading mass over a polylogarithmic or other subexponential number of shells. If the predictor has `J` atoms and `log J=o(HT)`, some coefficient already has exponential rate one: `log max_j |b_j| >= HT-o(HT)`. Increasing low-complexity shell count therefore does not trade away the instability; only a genuinely different approximation geometry could change the leading Wiener constant.

The reusable lesson is that **spectral predictor conditioning and arithmetic carrier capacity are independent currencies until an exact theorem connects them**. The earlier constant `6.081` is not a source-capacity theorem; it is an upper bound on a pure causal approximation constant. Conversely, the unit floor is not an RH or prime-distribution obstruction. The constructive gap is now localized to the continuum predictor itself.

**Boundary.** RE-217 does not prove `C_sep=1`, construct a near-floor predictor, or rule out `C_sep>1`. Classical Chebyshev/Newton band-limited predictors establish related prediction mechanisms but their qualitative convergence does not determine the uniform-error Wiener norm at depth `HT`. The relevant next question is the exact or sharper value of `C_sep` under support geometry compatible with the RE-208 arithmetic realization.