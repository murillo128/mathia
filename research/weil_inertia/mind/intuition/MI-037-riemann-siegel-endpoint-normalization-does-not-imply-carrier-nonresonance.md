# MI-037 — Riemann--Siegel endpoint normalization does not imply carrier nonresonance

**Evidence level:** exact synthesis from [WI-322](../../findings/WI-322-exact-rvm-normalization-forces-bow-prime-scale-below-riemann-siegel-length.md), [WI-323](../../findings/WI-323-riemann-siegel-duality-makes-source-compatible-bow-transform-noncontracting.md), and [WI-324](../../findings/WI-324-riemann-siegel-endpoint-still-admits-cubic-carrier-resonance.md).

WI-322--WI-323 pin a source-compatible bow to the noncontracting side of Riemann--Siegel scale: `U/X_*^2 >= 2pi(1-o(1))`, while the direct logarithmic dual has length at least the source length and preserves the relative bandwidth and square-root normalization. That removes sparsity and direct-duality contraction as generic escape mechanisms.

WI-324 shows that this sharpened scale information still does not imply short-block cancellation of the bare logarithmic carrier. There is an explicit cofinal family

`U_M=2pi M(M+1/2)`, `X_M=M`,

for which `U_M/X_M^2 -> 2pi` from above and the direct dual length is only `M+1/2`, yet the lattice phases have an exact arithmetic alias: the linear and quadratic Taylor contributions to `A_M log(1+j/M)` are integers on integer `j` after the appropriate combination. The visible phase begins at the residual quadratic/cubic scale, leaving a coherent block of length `asymp M^(1/3)`.

Thus **endpoint saturation and noncontracting duality do not furnish Diophantine nonresonance**. Even arbitrarily close to the exact Riemann--Siegel boundary, the scalar ratio and smooth phase geometry permit coherent lattice resonances. A theorem that de-exceptionalizes the distinguished bow twist must consume information not present in those variables.

The missing information could come from the actual arithmetic location of the distinguished zeta height, signed structure of the von-Mangoldt coefficients, a norm-matched dispersion theorem, or another source-fixed observable that rules out or neutralizes the resonant lattice configurations. Merely sharpening `U/X_*^2`, reapplying stationary phase, or invoking smooth logarithmic curvature cannot provide it.

**Boundary.** The resonant family is a control compatible with the scale/count constraints; it is not asserted to occur at actual zeta bows and does not estimate the distinguished covariance. It rules out a generic implication from endpoint normalization to carrier cancellation, not the possibility that additional zeta-specific arithmetic information makes the true distinguished twist nonresonant.