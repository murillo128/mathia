# MI-059 — Fixed complex single-center cancellation still pays the factor-two Wiener floor

**Evidence level:** exact synthesis from `RE-220`--`RE-221` and `RE-228`.

The positive-real single-center obstruction might appear to leave one obvious escape: move the expansion center off the real axis and let complex cancellation reduce the normalization cost. RE-228 closes that fixed-parameter route using the **true normalized polynomial**, not an absolute-value surrogate for its remainder.

Fix a contracting symmetric arc `|theta|<=alpha`, one nonzero complex center `a=rho e^(i phi)`, and linear truncation depth `N=lambda m+O(1)`. Write

`r=max_|theta|<=alpha |1-e^(-i theta)/a|<1`, `r_0=|1-1/a|`, and `nu=1+1/rho`.

Uniform prediction by the normalized negative-binomial polynomial forces the truncation ratio past a definite upper root `lambda_*`. The reason is that the derivative at the worst arc endpoint has exponential size governed by `g(lambda)+lambda log r`, while the exact DC denominator is bounded above by the negative-binomial sum with radius `r_0`. Since `r_0<r`, flatness is impossible before the upper root of

`g(lambda)+lambda log r+log(1-r_0)=0`.

The same denominator estimate goes in the useful direction for the Wiener norm: any cancellation in `Q(1)` only makes the normalized coefficient norm larger. Consequently

`liminf m^(-1) log ||F_m||_A >= lambda_* log(nu/r)`.

Complex endpoint geometry cannot lower this below the corresponding positive-real radial center. The resulting rate is strictly larger than `2 alpha`. Thus one fixed complex phase does not beat the factor-two Wiener floor even when both the remainder and the DC normalization are allowed their exact cancellation.

The numerical calibration is unusually sharp. At the explicit RE-218 arc/center, the exact-cancellation lower exponent is `5.995948...`, while the explicit construction has exponent `5.996380...`. The near-six cost at that point is therefore almost entirely geometric/representation-theoretic rather than an artifact of a crude absolute-tail estimate.

The reusable lesson is that **complex cancellation must be audited at the normalization map, not credited abstractly**. If the denominator is the only place where cancellation can create a discount, an upper bound on its modulus may turn that cancellation into a stronger lower bound on the normalized cost.

**Boundary.** RE-228 fixes `alpha`, the complex center and the asymptotic truncation ratio while `m` grows. It does not close drifting complex centers, a uniform complex-corridor class, multi-center/minimax recombination, rational predictors or other bases. It also does not improve the universal separated-prediction floor `C_sep>=1`.
