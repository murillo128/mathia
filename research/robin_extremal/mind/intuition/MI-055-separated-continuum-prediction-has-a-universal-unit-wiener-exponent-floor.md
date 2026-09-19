# MI-055 — Separated continuum prediction has a universal unit floor, while single-center absolute tails have a phase-blind factor-two floor

**Evidence level:** exact synthesis from [RE-217](../../findings/RE-217-separated-continuum-prediction-has-a-unit-wiener-norm-floor.md) through [RE-220](../../findings/RE-220-complex-single-centers-do-not-improve-absolute-tail-wiener-cost.md), using the continuous Kaiser coercive test of RE-215 and the ordinary-prime realization through RE-208.

Let `mu` be any finite complex measure supported on `[H,infinity)`, `H>0`, whose Fourier transform approximates the constant one on `[-T,T]` with error `epsilon<1`. RE-217 upgrades the signed-prefix obstruction to a direct total-variation bound

`||mu||_TV >>_H (1-epsilon) e^(HT)/(HT log(HT))`.

For a finite exponential predictor this is exactly a lower bound for `sum_j |b_j|`. Thus at logarithmic height `T_Q=c log Q`, every separated predictor with coefficient variation `Q^(kappa+o(1))` satisfies the spectral floor `kappa>=Hc`. If `C_sep` is the optimal leading Wiener exponent among fixed-corridor separated predictors with vanishing uniform error, RE-218 gives

`1 <= C_sep <= 5.996390`.

RE-219 shows that the gap above one is not removable by further scalar tuning inside the current constructive proof architecture. For the single-positive-real-center negative-binomial family used by RE-216--RE-218, if the discarded tail is certified by summing absolute term magnitudes, uniformly vanishing tail error forces a coefficient `ell^1` exponent at least two. Hence

`2 <= C_(1c,abs,R+) <= 5.996390`.

RE-220 closes the obvious complex-center escape **inside that same certificate class**. For any nonzero complex center `a`, let `rho=|a|`. On the symmetric observed arc, radialization to the positive real center `rho` weakly improves the worst-case contraction factor:

`r(rho,alpha) <= r(a,alpha)`.

At the same time the exact truncated-polynomial Wiener norm is unchanged. After re-expanding the negative-binomial terms in monomials, every contribution to a fixed output degree has the common phase `(-1)^j a^(-m-j)`, so there is no hidden coefficient cancellation from `arg a`. Therefore

`||P_(m,N,a)||_A = ||P_(m,N,rho)||_A`.

The termwise absolute-tail certificate is likewise no worse after radialization. Every complex single-center predictor certified by this argument has a positive-real comparator with the same Wiener cost and no larger certified error. Consequently

`2 <= C_(1c,abs,C) <= 5.996390`.

The factor-two floor is thus **phase-blind within the single-center absolute-tail representation**. Complexifying one Taylor center changes neither side of the error-versus-Wiener tradeoff because symmetry makes the radial center minimax at fixed modulus and the center phase factors out coefficientwise. This is stronger than saying the tested complex parameter failed numerically: the entire complex one-center class reduces exactly to the positive-real class for the quantities consumed by the proof.

The distinction remains crucial. RE-217 prices every separated measure through a source-independent coercive test. RE-219--RE-220 price only one approximation/certificate architecture. They do **not** improve the universal lower bound `C_sep>=1`. Several centers can interfere after coefficient collection, other approximation bases need not have the same radialization, and a cancellation-sensitive tail estimate is not controlled by the termwise absolute comparison.

RE-208 already realizes every regular discrete predictor with strict coefficient exponent below `1/2`, so a construction with global `C_sep=1` would still reach every fixed `c<1/(2H)`, the leading bounded-prime carrier-capacity ceiling. The constructive search must therefore leave the now-complete single-center absolute-tail architecture: use genuinely multi-center/minimax geometry, a different basis, or a remainder argument that retains complex cancellation.

**Boundary.** The global interval remains `1<=C_sep<=5.996390`. RE-220 depends on the symmetric frequency window and the termwise absolute-tail certificate; it does not say that complex centers are useless on asymmetric arcs or under cancellation-sensitive analytic estimates. Nor does it rule out several-center constructions. The contribution is to separate the universal Wiener floor from a stricter representation floor and to show that complex phase alone does not alter that floor.