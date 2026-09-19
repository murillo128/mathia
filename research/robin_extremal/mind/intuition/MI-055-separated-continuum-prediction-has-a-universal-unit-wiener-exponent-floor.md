# MI-055 — Separated continuum prediction has a universal unit Wiener-exponent floor

**Evidence level:** exact synthesis from [RE-217](../../findings/RE-217-separated-continuum-prediction-has-a-unit-wiener-norm-floor.md) and [RE-218](../../findings/RE-218-explicit-off-center-retuning-pushes-the-separated-wiener-exponent-below-six.md), using the continuous Kaiser coercive test of RE-215 and the ordinary-prime realization through RE-208.

Let `mu` be any finite complex measure supported on `[H,infinity)`, `H>0`, whose Fourier transform approximates the constant one on `[-T,T]` with error `epsilon<1`. RE-217 upgrades the signed-prefix obstruction to a direct total-variation bound

`||mu||_TV >>_H (1-epsilon) e^(HT)/(HT log(HT))`.

For a finite exponential predictor this is exactly a lower bound for `sum_j |b_j|`. Thus at logarithmic height `T_Q=c log Q`, every separated predictor with coefficient variation `Q^(kappa+o(1))` satisfies the spectral floor `kappa>=Hc`.

If `C_sep` is the optimal leading Wiener exponent among fixed-corridor separated predictors with vanishing uniform error, RE-218 improves the constructive endpoint without changing the lower argument. Its explicit off-center retuning `alpha=13/25`, `a=2.29`, `lambda=3.992` gives

`1 <= C_sep <= 5.996390`.

The fact that the upper endpoint moved from `6.081` to below six while the arithmetic realization stayed fixed is itself informative: the constant above one is still prediction geometry, not a prime-capacity invariant. At `H=log 8` the same retuning increases the currently certified ordinary-prime hiding range to `c<0.0400989...`.

RE-208 already realizes every regular discrete predictor with strict coefficient exponent below `1/2`, so a spectral construction with `C_sep=1` would let the existing arithmetic interface reach every fixed `c<1/(2H)`, exactly the leading bounded-prime carrier-capacity ceiling isolated by RE-214--RE-215. The remaining gap is therefore quantitatively localized to the continuum predictor.

The same floor cannot be hidden by spreading mass over a polylogarithmic or other subexponential number of shells. If the predictor has `J` atoms and `log J=o(HT)`, some coefficient already has exponential rate one. Increasing low-complexity shell count therefore does not trade away the instability; only a genuinely different approximation geometry can change the leading Wiener constant.

The reusable lesson is that **spectral predictor conditioning and arithmetic carrier capacity are independent currencies until an exact theorem connects them**. Improvements in `C_sep` should be credited as analytic prediction improvements, while the unit lower floor and the half-logarithmic carrier ceiling remain separate constraints.

**Boundary.** RE-218 does not prove `C_sep=1`, construct a near-floor predictor or rule out `C_sep>1`. Its numerical parameter choice is an explicit upper bound, not an optimality theorem. The relevant next question remains the exact or sharper value of `C_sep` under support geometry compatible with the RE-208 arithmetic realization.