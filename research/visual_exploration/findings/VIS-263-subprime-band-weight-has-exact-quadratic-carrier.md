# VIS-263 — a subprime-band Rodgers weight has exact quadratic carrier `1/(2 pi^2)`

## Claim

Use the fixed-margin smooth pair-correlation setting and notation of `VIS-260`--`VIS-262`. Adopt the Fourier convention

`hat f(xi)=integral_R f(u) exp(-2*pi*i*xi*u) du`.

Put

`eta = log(2)/(4*pi)`

and define the even compactly supported bump

`hat omega_*(xi) = exp(1 - 1/(1-(xi/eta)^2))` for `|xi|<eta`,

with `hat omega_*(xi)=0` for `|xi|>=eta`.

Then `hat omega_*` is real, even, `C^infinity`, compactly supported, and `hat omega_*(0)=1`. Its inverse Fourier transform `omega_*` is therefore a fixed real even Schwartz weight in Rodgers' admissible class.

Let

`F(u)=tilde Q_t(u)-K_t(u)`

be the exact `t`-independent Bogomolny--Keating-minus-naive-GUE source kernel used in `VIS-262`,

`F(u)=(1/(2*pi^2))[Re((zeta'/zeta)'(1+iu)-B(iu))+1/u^2]`,

with the removable cancellation at `u=0` understood continuously. Define

`C_2(omega_*) = integral_R u^2 omega_*(u) F(u) du`.

Then

`C_2(omega_*) = 1/(2*pi^2)`.

The reason is exact frequency separation. If `psi(u)=u^2 omega_*(u)`, then

`hat psi(xi)=-(1/(4*pi^2)) hat omega_*''(xi)`,

so `hat psi` is supported in `[-eta,eta]`. Every nonconstant Dirichlet frequency in `(zeta'/zeta)'` has magnitude at least

`log(2)/(2*pi)=2 eta`,

and every frequency in Rodgers' `B` term has magnitude at least

`2 log(2)/(2*pi)=4 eta`.

Hence both arithmetic oscillatory series pair to zero against `psi`; only the pole-compensating `1/u^2` term survives. Since `integral omega_*=hat omega_*(0)=1`, the displayed coefficient follows exactly.

Combining this explicit weight with the sharp quadratic cusp packet of `VIS-257` and the fixed-margin transfer of `VIS-260`--`VIS-262` gives, under the same RH-conditional zeta-transfer hypotheses,

`integral [P_T(alpha)-GUE_T(alpha)] dnu_b(alpha)`
` = -(1/(4*pi^2))(log T)^2 + o((log T)^2)`

for `b=T^(-beta)` whenever `0<2 beta<delta<epsilon/2` in the same fixed support margin.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-BRIDGED + EXPLICIT FIXED-WEIGHT CALIBRATION + NEGATIVE APPLICATION CONTROL + NO-NOVELTY-CLAIM`.

This is an exact calibration result for Rodgers' fixed smooth test class. It does not establish that the bounded-tent/Montgomery support-edge observable uses this weight, does not provide moving-edge uniformity, and does not solve the four-level covariance problem of the original edge--edge statistic.

## 1. The weight is explicit and admissible

The function

`rho(x)=exp(1-1/(1-x^2))`, `|x|<1`,

extended by zero outside `[-1,1]`, is the standard even `C^infinity` bump with `rho(0)=1`. Thus

`hat omega_*(xi)=rho(xi/eta)`

has support strictly inside the first nonzero Dirichlet frequency of the zeta logarithmic derivative.

Because `hat omega_*` is real and even, `omega_*` is real and even. Because its Fourier transform is smooth and compactly supported, `omega_*` is Schwartz. No zero data, fitted frequency, height-dependent support, or optimized parameter enters the definition.

Multiplication by `u^2` differentiates the Fourier transform twice:

`hat psi(xi)=hat{u^2 omega_*}(xi)=-(1/(4*pi^2))hat omega_*''(xi)`.

Differentiation does not enlarge support, so

`supp(hat psi) subset [-eta,eta]`.

This support statement is the only property needed for the exact filtering below.

## 2. All nonzero zeta and `B` frequencies are filtered out

For `sigma>1`, absolute convergence gives

`(zeta'/zeta)'(sigma+iu)`
` = sum_(n>=2) Lambda(n) log(n) n^(-sigma) exp(-iu log n)`.

In the chosen Fourier convention, the term indexed by `n` lies at frequency

`xi_n=log(n)/(2*pi)`.

Since `n>=2`, `xi_n>=log(2)/(2*pi)=2 eta`. Therefore

`integral_R psi(u) Re((zeta'/zeta)'(sigma+iu)) du = 0`

for every `sigma>1`.

Let `sigma` decrease to `1`. Near `u=0`, write

`(zeta'/zeta)'(s)=1/(s-1)^2+H(s)`

with `H` holomorphic locally. The factor `u^2` in `psi` cancels the boundary double pole: for `epsilon=sigma-1`,

`|u^2 Re[(epsilon+iu)^(-2)]| <= 1`.

Away from the origin the boundary passage is ordinary, while the Schwartz decay of `psi` dominates the standard logarithmic/polynomial growth of the zeta logarithmic derivative on the zero-free line `Re(s)=1`. Thus the same pairing survives the boundary limit:

`integral_R u^2 omega_*(u) Re((zeta'/zeta)'(1+iu)) du = 0`.

Rodgers' second source term has the absolutely convergent expansion

`B(iu)`
` = sum_p [log(p)^2/(p^(1+iu)-1)^2]`
` = sum_p sum_(m>=2) (m-1) log(p)^2 p^(-m) exp(-i m u log p)`.

Its smallest frequency is

`2 log(2)/(2*pi)=4 eta`,

so the same support argument gives exactly

`integral_R u^2 omega_*(u) Re B(iu) du = 0`.

No asymptotic cancellation is being used in either step. The test function has simply been placed below every nonzero prime-power frequency present in these two series.

## 3. The surviving coefficient is exactly the pole-compensating channel

Insert the two vanishing pairings into Rodgers' exact kernel:

`C_2(omega_*)`
` = (1/(2*pi^2)) integral_R u^2 omega_*(u)`
`     [Re((zeta'/zeta)'(1+iu)-B(iu))+1/u^2] du`
` = (1/(2*pi^2)) integral_R omega_*(u) du`.

Fourier normalization gives

`integral_R omega_*(u) du = hat omega_*(0)=1`,

hence

`C_2(omega_*)=1/(2*pi^2)`.

This also identifies what the explicit carrier is measuring. For this subprime-band weight the coefficient is **not** produced by resolving individual prime or prime-power oscillations: those frequencies have been removed exactly. The nonzero quadratic carrier comes from the zero-frequency pole-compensation channel in the Bogomolny--Keating correction.

That is useful as a calibration and also as a negative interpretation control. A nonzero `C_2` in Rodgers' admissible class does not by itself certify that a proposed support-edge statistic is seeing detailed prime-frequency structure.

## 4. Consequence for the sharp quadratic packet

`VIS-262` shows for any fixed admissible weight that

`R_T''(0)=-(log T)^2 C_2(omega)+O(T^(-delta)(log T)^2)`

through the fixed-margin Rodgers reduction. For the present explicit weight,

`R_T''(0)=-(1/(2*pi^2))(log T)^2+O(T^(-delta)(log T)^2)`.

The sharp symmetric quadratic packet of `VIS-257` has zero mass, exact sine-kernel-cusp cancellation, unit quadratic moment, and total variation `8b^(-2)`. The Taylor reduction of `VIS-261` therefore gives the prediction-side main term

`-(1/(4*pi^2))(log T)^2`.

Its Taylor remainder is `O(b^2(log T)^4)`. Under RH, the actual-zeta transfer supplied by Rodgers and quantified in `VIS-260` contributes `O(T^(-delta)b^(-2))`. With

`b=T^(-beta)`, `0<2 beta<delta<epsilon/2`,

both errors are lower order than `(log T)^2`, giving the claimed fixed-margin actual pair-statistic asymptotic.

This consequence uses exactly the same fixed-test/fixed-margin regime as `VIS-260`--`VIS-262`; no changing weight or shrinking theorem-support margin is introduced.

## 5. Prior art and novelty boundary

The load-bearing external source remains Brad Rodgers, **Macroscopic Pair Correlation of the Riemann Zeroes for Smooth Test Functions**, *Quarterly Journal of Mathematics* 64:4 (2013), 1197--1219, DOI `10.1093/qmath/has024`, arXiv `1203.3275`. Rodgers supplies the RH-conditional smooth-test comparison, the `Q_t` to `tilde Q_t` reduction, and the exact `t`-independent kernel `F=tilde Q_t-K_t` used here.

The facts that a compact Fourier support annihilates separated Dirichlet frequencies, that multiplication by `u^2` differentiates the Fourier transform, and that the displayed bump is a Schwartz-admissible inverse transform are standard Fourier/Dirichlet-series analysis. A targeted literature check found no reason to classify that filtering step as a new general theorem.

The Mathia-specific contribution is the composition with the already established cusp-packet conditioning chain `VIS-257`--`VIS-262`: it replaces the abstract existence weight of `VIS-262` by one explicit frozen admissible weight, computes its quadratic coefficient exactly, and simultaneously exposes that this easiest nonzero carrier lives below the first prime frequency.

No novelty is claimed for Rodgers' arithmetic correction, the Bogomolny--Keating prediction, Fourier filtering of Dirichlet series, or the smooth bump construction.

## 6. Boundary and falsification

The weight `omega_*` is an **explicit calibration weight**, not yet the support-edge application weight requested by the current research frontier. Its Fourier support was deliberately chosen below `log(2)/(2*pi)`; consequently it suppresses every direct prime and prime-power oscillatory mode occurring in the displayed source terms.

A claimed dictionary to the bounded-tent/Montgomery edge observable must therefore be proved, not inferred from the existence of the nonzero coefficient. If the intended application requires a weight whose Fourier support reaches prime frequencies, a moving support edge, or an `L`-dependent source taper, the present exact calculation does not transfer automatically.

Conversely, the calculation is falsified if any supposedly surviving zeta or `B` frequency can lie inside `[-eta,eta]` under the stated Fourier convention, or if the adopted Rodgers test class excludes the fixed real even Schwartz weight with smooth compactly supported Fourier transform constructed above. Neither occurs under the conventions and admissible class recorded in `VIS-262`.

The result also remains two-level. It says nothing about the four-level cross-window covariance required by the original disjoint edge--edge statistic, and it does not supply the moving-margin uniformity needed to take a support edge toward Montgomery's boundary.

No untouched confirmation-zero data are used.

## Research consequence

The fixed-margin branch now has a fully explicit calibration point:

`C_2(omega_*)=1/(2*pi^2)`.

This closes the purely existential part of the quadratic-carrier question without numerical fitting. It also sharpens the next question: **does a mathematically faithful weight for the original bounded-tent/Montgomery support-edge observable retain a nonzero quadratic carrier for a reason that survives beyond this zero-frequency pole-compensation control?**

Answering that requires a new application-dictionary calculation. It is a separate coherent research step and is intentionally left for a later invocation rather than extending the present fixed-weight result.