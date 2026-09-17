# MI-037 — Endpoint normalization, zero membership and positive raw prime weights do not imply carrier nonresonance

**Evidence level:** exact/source-compatible negative synthesis from [WI-322](../../findings/WI-322-distinguished-twist-bow-needs-riemann-siegel-scale.md), [WI-323](../../findings/WI-323-riemann-siegel-bow-makes-direct-logarithmic-dual-noncontracting.md), [WI-324](../../findings/WI-324-riemann-siegel-endpoint-has-explicit-lattice-resonance.md), [WI-325](../../findings/WI-325-endpoint-carrier-resonance-survives-snapping-to-actual-zero-ordinates.md), and [WI-326](../../findings/WI-326-raw-von-mangoldt-weights-preserve-cubic-snapped-zero-resonance.md).

WI-322 identifies the square-root Riemann--Siegel scale as the source-compatible location of any distinguished bow, and WI-323 shows that the direct logarithmic dual is noncontracting there. Those facts make the endpoint geometrically plausible, but they do not provide the cancellation required by a distinguished-twist argument.

WI-324 gives an explicit endpoint control. At

`U_M=2pi M(M+1/2)`, `X_M=M`,

the ratio `U_M/X_M^2` approaches `2pi` from above, yet the phase lattice is resonant. The first two Taylor jets cancel by aliasing and a coherent block of length `asymp M^(1/3)` remains. Riemann--Siegel normalization by itself therefore does not force nonresonance of the bare logarithmic carrier.

WI-325 closes the first arithmetic repair. Genuine zeta-zero membership is still too coarse: an actual zero ordinate `gamma_M=U_M+O(1)` can be chosen near each resonant height, and the resulting phase perturbation is only `O(M^(-2/3))` across the cubic block. Coherence survives after snapping to the zero set.

WI-326 closes the next weak repair. Positive raw von Mangoldt weights do not automatically destroy the snapped resonance. By averaging ordinary PNT mass over starting positions, infinitely many resonant cubic blocks contain total raw von Mangoldt mass `asymp M^(1/3)`. On the WI-325 sector the phase has positive real part, so

`|sum_(j<=ell) Lambda(M+j) exp(i gamma_M log((M+j)/M))| >> M^(1/3)`.

After square-root normalization the coherent square is `>>M^(-1/3)`, while the diagonal energy of the same block is `<<M^(-2/3) log^2 M`. Their ratio therefore tends to infinity at least like `M^(1/3)/log^2 M`. Raw positive prime weighting can reinforce rather than suppress the exceptional block.

The conceptual boundary is now sharply source-specific. Endpoint scale, actual zero-ordinate membership and positive raw prime mass are all compatible with the resonance. A successful distinguished-twist theorem must consume structure that WI-326 deliberately omits: the signed subtraction `Lambda-Lambda^sharp`, an additional source factor from the exact BOW reduction, necessary cancellation with the rest of the natural window, or a bow-specific relation that distinguishes the selected off-critical configuration from an arbitrary nearby zero ordinate.

This is also a normalization warning. Comparing a source-weighted twisted block only with its diagonal `L^2` mass cannot by itself prove cancellation: the coherent contribution can parametrically exceed that scale on the control family. The missing theorem must act on the actual signed/full-window source, not merely on positivity of prime weights.

**Boundary.** WI-326 does not prove that the full Gallagher/BOW coefficient is resonant, does not produce an off-critical bow, and does not lower-bound the complete distinguished Weil covariance. Terms outside the cubic block or the signed subtraction may cancel it. The result only rules out the progressively weaker claims that source-compatible scale, zero-set membership or positive raw von Mangoldt weighting automatically supply the required nonresonance.