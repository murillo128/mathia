# MI-017 — Diffuse one-profile boundary logs collapse to universal square-zero geometry down to their defect scale

**Evidence level:** exact asymptotic operator statement from [PC-295](../../findings/PC-295-diffuse-boundary-log-singular-spectrum-is-classical-green.md)--[PC-298](../../findings/PC-298-quantitative-square-zero-approximation-reaches-shrinking-pseudospectral-scales.md) under their diffuseness hypothesis. The conclusion remains one-profile and diffuse; joint/noncommuting and non-diffuse regimes remain open.

PC-295 shows that diffuse boundary-log matrices keep a nonzero deterministic Green singular spectrum. PC-296 simultaneously shows their eigenvalues collapse because the left and right low-Fourier frames become mutually orthogonal. PC-297 identifies the operator geometry: after an asymptotically negligible correction the dominant frames can be made exactly orthogonal, producing a square-zero approximant `S=UDW*` with `S^2=0` and `||S||->1/2`.

PC-298 replaces the qualitative compactness choice by an explicit defect rate. With `delta_q=sqrt(q beta_q/N)`,

`E ||T_q-S_q||_op <= C r_q`,
`r_q=delta_q^(1/3)+delta_q^(1/2)log q+(log q)/N`,

and `||S_q||=1/2+O(q^-3)`. The `delta_q^(1/3)` term comes from balancing growing low-frame error against the universal Green tail; it is not claimed sharp.

This quantitative rate pushes universality into shrinking resolution. If `epsilon_q->0` but `r_q/epsilon_q->0`, the `epsilon_q`-pseudospectrum, after its natural `epsilon_q^-1/2` rescaling, still converges to the same universal disk. Therefore “probe a smaller pseudospectral scale” is not by itself a surviving arithmetic route. The probe must resolve the actual square-zero defect, or retain relational information destroyed by the one-profile orthogonalization.

The surviving currency is now explicit: singular strength, eigenvalue loops and pseudospectral amplification above `r_q` are different projections of one universal square-zero geometry. Prime-specific information must live in the `O(r_q)` remainder (or a sharper subscale if `r_q` is improved), in several coupled profiles/levels, in source-coupled frame relations, or outside diffuseness.

**Boundary.** PC-298 proves universality only for shrinking scales satisfying `epsilon_q >> r_q`; it does not classify the critical/subdefect regime, prove `r_q` sharp, or classicalize joint noncommuting observables. Those are genuinely different questions.
