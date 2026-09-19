# MI-055 — Separated continuum prediction has a universal unit floor, while fixed single-center architectures retain a factor-two representation floor

**Evidence level:** exact synthesis from [RE-217](../../findings/RE-217-separated-continuum-prediction-has-a-unit-wiener-norm-floor.md) through [RE-221](../../findings/RE-221-fixed-real-single-center-cancellation-retains-the-factor-two-wiener-floor.md), using the continuous Kaiser coercive test of RE-215 and the ordinary-prime realization through RE-208.

Let `mu` be any finite complex measure supported on `[H,infinity)`, `H>0`, whose Fourier transform approximates the constant one on `[-T,T]` with error `epsilon<1`. RE-217 upgrades the signed-prefix obstruction to a direct total-variation bound

`||mu||_TV >>_H (1-epsilon) e^(HT)/(HT log(HT))`.

For a finite exponential predictor this is exactly a lower bound for `sum_j |b_j|`. Thus at logarithmic height `T_Q=c log Q`, every separated predictor with coefficient variation `Q^(kappa+o(1))` satisfies the spectral floor `kappa>=Hc`. If `C_sep` is the optimal leading Wiener exponent among fixed-corridor separated predictors with vanishing uniform error, RE-218 gives

`1 <= C_sep <= 5.996390`.

RE-219 shows that the gap above one is not removable by scalar tuning inside the current constructive proof architecture when the discarded tail is certified in absolute value. For the single-positive-real-center negative-binomial family used by RE-216--RE-218, uniformly vanishing tail error forces a coefficient `ell^1` exponent at least two:

`2 <= C_(1c,abs,R+) <= 5.996390`.

RE-220 closes the obvious complex-center escape **inside that same certificate class**. For any nonzero complex center `a`, radialization to `rho=|a|` weakly improves the worst-case contraction factor on the symmetric observed arc, while the exact truncated-polynomial Wiener norm is unchanged because every contribution to a fixed output degree has one common center phase. The termwise absolute-tail certificate is no worse after radialization. Therefore

`2 <= C_(1c,abs,C) <= 5.996390`.

RE-221 tests a different possible weakness of RE-219: perhaps the factor two came from taking absolute values of the discarded Taylor tail rather than from the finite predictor itself. For fixed real center `a>0`, fixed symmetric arc `0<alpha<pi/2`, and `N=lambda m+O(1)`, the exact truncated polynomial can be written as the regularized incomplete-beta polynomial

`Q_(m,N,a)(z)=I_(z/a)(m,N+1)`.

After exact DC normalization `F_m(z)=Q_(m,N,a)(z)/Q_(m,N,a)(1)`, assume the **actual complex polynomial** predicts uniformly on the arc, without replacing its remainder by a triangle-inequality tail bound. RE-221 proves that this already forces

`liminf_(m->infinity) log ||F_m||_A/(m alpha) >= 2`.

Under the physical scaling `m alpha=HT+O(1)`, the same factor-two lower exponent follows for the predictor total variation. Thus the absolute-tail proof in RE-219 was sufficient, but for fixed positive-real parameters it was not the mathematical source of the obstruction: exact cancellation inside the truncated remainder still cannot beat exponent two.

The representation audit must therefore keep three statements separate. The global separated-measure problem has only the universal floor `C_sep>=1`. A complex phase does not help the single-center class when the certificate is termwise absolute. And even with the **exact cancellation-sensitive remainder**, a fixed real center with fixed arc/truncation ratio still has the factor-two floor. None of these statements rules out all single-center asymptotics or all cancellation-sensitive constructions.

The surviving design space has narrowed to mechanisms that change something more structural: asymptotically drifting or degenerate single-center parameters, genuinely complex-center cancellation not reducible by RE-220's absolute certificate, several centers, minimax polynomials, or a different approximation basis. Any claimed improvement should be priced by the exact Wiener norm of the produced predictor rather than by a formal increase in parameter freedom.

**Boundary.** The global interval remains `1<=C_sep<=5.996390`. RE-221 is fixed-parameter and positive-real; it does not rule out drifting `a`, `alpha` or `lambda`, genuinely complex-center exact-remainder cancellation, several-center constructions, minimax approximants or other bases. RE-220 remains certificate-specific. The cross-cutting point is only that two obvious enrichments—center phase under absolute-tail control and exact finite-remainder cancellation at fixed real parameters—do not lower the representation-local factor-two cost.
