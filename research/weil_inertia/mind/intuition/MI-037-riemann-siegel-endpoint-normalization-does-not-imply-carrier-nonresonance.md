# MI-037 — Endpoint normalization and zero-ordinate membership do not imply carrier nonresonance

**Evidence level:** exact/source-compatible negative synthesis from [WI-322](../../findings/WI-322-distinguished-twist-bow-needs-riemann-siegel-scale.md), [WI-323](../../findings/WI-323-riemann-siegel-bow-makes-direct-logarithmic-dual-noncontracting.md), [WI-324](../../findings/WI-324-riemann-siegel-endpoint-has-explicit-lattice-resonance.md), and [WI-325](../../findings/WI-325-endpoint-carrier-resonance-survives-snapping-to-actual-zero-ordinates.md).

WI-322 identifies the square-root Riemann--Siegel scale as the source-compatible location of any distinguished bow. WI-323 shows that the direct logarithmic dual is noncontracting there. Those facts make the endpoint geometrically plausible, but they do not provide the cancellation required by a distinguished-twist argument.

WI-324 gives an explicit endpoint control. At

`U_M=2pi M(M+1/2)`, `X_M=M`,

the ratio `U_M/X_M^2` approaches `2pi` from above, yet the phase lattice is resonant. The first two Taylor jets cancel by aliasing and a coherent block of length `asymp M^(1/3)` remains. Thus Riemann--Siegel normalization by itself does not force nonresonance of the bare logarithmic carrier.

WI-325 closes the most immediate arithmetic repair. The explicit Riemann--von Mangoldt error implies that every sufficiently high interval of fixed length two contains a zeta zero ordinate. Choose `gamma_M` with

`gamma_M=U_M+O(1)`.

Across the WI-324 coherent block, changing the height by `O(1)` perturbs the carrier phase by only `O(M^(-2/3))`. A sector argument therefore preserves a coherent sum of order `M^(1/3)`. The resonant family can be snapped to **actual zeta zero ordinates** without losing the endpoint obstruction.

The conceptual boundary is now sharper. “Use the actual zero height” is not yet source-specific enough: zero ordinates are dense on the `O(1)` scale relevant to this perturbation, while the resonance is stable under that amount of motion. A successful distinguished-twist theorem must use finer information than set membership — for example bow-specific off-critical geometry, weighted von-Mangoldt cancellation, local zero configuration at a scale that resolves the resonance, or another source-fixed observable not shared by arbitrary nearby critical-line zeros.

This also prevents a common overinterpretation. WI-325 does not say actual zeta zeros are resonant in general; it constructs a cofinal subsequence of zero ordinates close enough to an explicit resonant lattice family that the bare carrier cannot distinguish them. Therefore any universal nonresonance theorem based only on endpoint scaling plus zero-ordinate membership is false.

**Boundary.** WI-324--WI-325 concern the bare logarithmic carrier. They do not produce an off-critical bow, prove a large signed Weil covariance, or show that the von-Mangoldt-weighted source sum fails to cancel. They isolate the extra information a closure theorem must genuinely use: source-weighted or bow-specific arithmetic structure beyond normalization and membership in the zero set.