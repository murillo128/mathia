# VIS-129 — pair-correlation effective size fixes a concrete tent-capacity scale and exposes a calibration-resolution gate

## Claim

Let

`L_T = log(T/(2*pi))`.

The finite-size Riemann-zero/CUE literature used elsewhere in this line supplies a concrete classical effective-size candidate obtained by matching the pair-correlation expansion:

`N_e(T) = rho_* L_T`,

with

`rho_* = 1/sqrt(12 Lambda)`,

`Lambda = 1.573151071...`.

Numerically,

`rho_* = 0.230156986...`,

so

`2*pi*rho_* = 1.44611899...`.

If this pair-correlation-matched effective size is adopted as the predeclared finite-CUE null for the bounded-tent support-edge thread, the single-connected-arc capacity condition from `VIS-128`

`H_src < 2*pi*rho`

becomes the explicit design condition

`H_src < 1.44611899...`.

This removes one arbitrary free scaling parameter from the current null candidate. It does **not** prove that the pair-correlation effective size transfers unchanged to the weighted, tapered, continuous support-edge statistic.

There is also a quantitative reason that this transfer precision matters. `VIS-123` gives the normalized continuous-CUE edge ripple, at fixed centered edge coordinate `v` and `N=rho L_T`,

`E_rho(v;L_T)`
` = -[sin^2(pi*rho*v)/(pi^2*rho)] [log(rho L_T)/L_T]`
`   + O_v(1/L_T)`

for fixed positive `rho` away from the exceptional integer-mode cancellations. Write

`a(rho,v) = -sin^2(pi*rho*v)/(pi^2*rho)`.

Then a perturbation `rho -> rho + delta_rho` changes the displayed log-enhanced universal term by

`delta_rho * partial_rho a(rho,v) * [log L_T/L_T]`

up to lower-order terms in the same expansion, where

`partial_rho a(rho,v)`
` = [sin^2(pi*rho*v) - pi*rho*v*sin(2*pi*rho*v)]/(pi^2*rho^2)`.

At generic predeclared edge coordinates this derivative is nonzero. Therefore a ratio uncertainty of order

`delta_rho = Theta(1/log L_T)`

already produces a universal null displacement of order `1/L_T`, exactly the scale on which the current thread hopes to resolve an arithmetic residual after removing larger universal effects.

Consequently, **leading proportionality `N(T) ~ rho_* L_T` alone is not enough to identify a generic `1/L_T` post-null residual**. The support-edge transfer must either justify the effective-size ratio to `o(1/log L_T)` at the chosen coordinates, or carry the remaining effective-size uncertainty as part of the null/covariance and show that the candidate residual is distinguishable from it.

**Evidence/status:** `LITERATURE+DERIVED + EXACT DESIGN CONSEQUENCE + CALIBRATION OBSTRUCTION + NO-NOVELTY-CLAIM`.

No new effective-matrix-size theorem, CUE form-factor theorem, zeta pair-correlation theorem, arithmetic residual, or implication toward RH is claimed.

## 1. Pair-correlation matching supplies a non-fitted candidate for `rho`

Nishigaki's 2026 finite-size analysis records the Riemann-zero kernel expansion and the effective CUE size

`N_e(T)=L_T/sqrt(12 Lambda)`,

explicitly stating that this identification is deduced by matching the pair-correlation function. The arithmetic constant `Lambda=1.573151071...` arises from prime sums. This is the same finite-size Riemann-zero/CUE literature family already used as a baseline in `SOURCES.md` and in the consecutive-spacing findings.

Thus the present support-edge experiment does not need to choose `rho=N/L_T` by inspecting a residual. A natural source-derived null candidate already exists:

`rho=rho_* = 1/sqrt(12 Lambda)`.

That is valuable precisely because the visual-search discipline forbids tuning representation parameters on confirmation data.

The logical direction matters. The literature formula was obtained from a lower-order pair-correlation match. It is a principled candidate for the support-edge null, not evidence that every finite-height statistic has exactly the same effective-size transfer.

## 2. The candidate effective size fixes the bounded-tent capacity ceiling

`VIS-128` writes the unfolded tent support as

`M = H_src L_T/(2*pi)`

and shows that, for `N/L_T -> rho`, a single connected non-wrapping CUE arc has asymptotic capacity only when

`M/N -> H_src/(2*pi*rho) < 1`.

Substituting `rho_*` gives

`H_src < 2*pi/sqrt(12 Lambda)`

or numerically

`H_src < 1.44611899...`.

This is a design ceiling, not an optimal-window theorem. A practical frozen experiment should keep a nonvanishing margin below it rather than operate at equality. A wider physical support would require a different arc/periodization model instead of silently reusing the same single-circle construction.

The value `1.446...` is therefore not a newly discovered Riemann constant. It is just the pair-correlation effective-size coefficient translated through the exact capacity dictionary of `VIS-128`.

## 3. Effective-size uncertainty can masquerade as a `1/L_T` residual

`VIS-123` gives, with `tau=(N/L_T)v=rho v`,

`R_N(tau)/N`
` = -[sin^2(pi*tau)/pi^2] [log N/N] + O_tau(1/N)`.

Replacing `N` by `rho L_T` yields the displayed coefficient `a(rho,v)`. For a nearby ratio `rho+delta_rho`, Taylor expansion of the explicit log-enhanced term gives

`E_(rho+delta_rho)-E_rho`
` = delta_rho * partial_rho a(rho,v) * [log L_T/L_T]`
`   + O(delta_rho/L_T)`
`   + O(delta_rho^2 log L_T/L_T)`

at fixed `v`, apart from the underlying `O(1/L_T)` remainder already present in the finite-size expansion.

Hence, whenever `partial_rho a(rho,v) != 0`, an uncertainty `delta_rho` merely of order `1/log L_T` shifts the universal null by the candidate arithmetic scale `1/L_T`.

This is not an argument that `rho_*` is uncertain by that amount. It is a **resolution requirement** on the transfer. The pair-correlation derivation fixes a leading effective-size rule for the statistic from which it was obtained; the present weighted+tapered continuous support-edge observable still needs a theorem, exact matched construction, or uncertainty propagation showing what precision survives that transfer.

The derivative vanishes at special coordinates, including some symmetry/integer-mode situations. Those isolated cancellations are not a safe escape: `VIS-123` already shows that integer-mode sampling can hide the continuous edge ripple. A robust frozen test should use multiple predeclared nondegenerate edge coordinates or otherwise verify its sensitivity explicitly rather than choosing a zero-derivative coordinate after inspection.

## 4. Integerization is a separate and smaller bookkeeping issue at the log-enhanced level

The effective size `N_e(T)=rho_* L_T` is generally not an integer, whereas a literal `CUE_N` ensemble has integer dimension. If the exact finite-CUE null is implemented with a predeclared nearest-integer rule, then

`N_int - N_e = O(1)`

and therefore

`delta_rho = (N_int-N_e)/L_T = O(1/L_T)`.

For the explicit log-enhanced term above, this changes the ripple by only

`O(log L_T/L_T^2)`,

which is `o(1/L_T)` at generic fixed `v`. Thus ordinary integer rounding does not create the same first-order calibration danger as an unresolved `Theta(1/log L_T)` ambiguity in the effective-size ratio.

This statement concerns the explicit `VIS-123` log-enhanced edge term only. The final exact finite-`N` composed null should still use one fixed integerization/interpolation convention and compute all remaining `O(1/L_T)` structure rather than infer it from this asymptotic argument.

## Prior-art and novelty assessment

Shinsuke M. Nishigaki, **Distributions of Consecutive Level Spacings of Circular Unitary Ensemble and Their Ratio: Finite-Size Corrections and Riemann zeta Zeros**, *Progress of Theoretical and Experimental Physics* 2026:2 (2026), 023A02, DOI `10.1093/ptep/ptag006`, records in Eq. (42)

`N_e(T)=log(T/(2*pi))/sqrt(12 Lambda)`

with `Lambda=1.573151071...`, stating that this effective size is deduced from pair-correlation matching. The paper also documents the finite-size Riemann-zero/CUE agreement inherited from earlier work by Bogomolny et al., Forrester--Mays, and Bornemann--Forrester--Mays.

`VIS-123` already imports the exact continuous-time finite-`N` CUE support-edge ripple from Sohail, Huang, and Wei and establishes the phase dictionary `tau=(N/L_T)v`. `VIS-128` already establishes the bounded-tent capacity condition `H_src<2*pi*rho`.

The present finding claims novelty for neither ingredient. Its Mathia-specific role is to compose them into a pre-registration control: the classical pair-correlation effective size fixes one non-fitted capacity scale, while the explicit support-edge dependence on `rho` shows how accurately that transfer must be controlled before a `1/L_T` residual can be called arithmetic.

## Boundary and falsification

The numerical ceiling `1.44611899...` is conditional on using the classical pair-correlation effective-size candidate as the finite-CUE support-edge null. If the exact weighted+tapered statistic derives a different source-grounded `N(T)`, recompute the capacity ceiling from that rule rather than preserving this number.

The sensitivity estimate is generic in `v`. At isolated coordinates where `partial_rho a=0`, the first-order term vanishes and a higher-order analysis is needed. Such coordinates cannot be selected post hoc as a way to suppress calibration sensitivity.

The `O(1/L_T)` remainder in `VIS-123` is already as large as the desired residual scale. This finding does not remove it. The final null must evaluate the exact finite-`N` weighted+tapered CUE statistic, including diagonal/arc conventions and covariance, rather than use the displayed leading ripple as the baseline.

Nothing here establishes that the pair-correlation effective-size formula transfers with the required precision. Failure to justify that transfer would not refute random-matrix universality or the literature effective-size model; it would only mean that the current support-edge residual is not identified at the desired scale.

## Research consequence

The accepted Montgomery support-edge clue can now replace an unconstrained free `rho` with a concrete first candidate: `rho_* = 1/sqrt(12 Lambda)`. Under the single-circle bounded-tent construction, freeze `H_src` strictly below `1.44611899...` and use a predeclared integerization convention for the finite-CUE null.

Before fresh zero confirmation, evaluate the exact composed null `P_L*Q_M^tent*K_N` at that effective-size rule and quantify sensitivity to any theoretically unresolved transfer error in `rho`. If admissible effective-size variation can move the null by `Theta(1/L_T)` at the predeclared edge coordinates, then a same-scale residual is not yet distinguishable from calibration. Only after that nuisance direction is eliminated or propagated into the covariance does an arithmetic lower-order amplitude become a well-posed next test.
