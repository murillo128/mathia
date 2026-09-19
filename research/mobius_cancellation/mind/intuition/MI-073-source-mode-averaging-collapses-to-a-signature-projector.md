# MI-073 — Formal averaging dimensions can collapse under exact regrouping, first-correlation separability, inversion and endpoint factorization

**Evidence level:** exact synthesis from [MC-397](../../findings/MC-397-source-mode-averaging-collapses-to-signature-projector.md), [MC-398](../../findings/MC-398-selberg-divisor-pair-lcm-fiber-collapse.md), [MC-399](../../findings/MC-399-lcm-retention-separates-from-source-qvdc-phase.md), [MC-400](../../findings/MC-400-twisted-lcm-hyperbola-transform-is-mobius-invertible.md), and [MC-401](../../findings/MC-401-full-lcm-endpoint-is-signed-gcd-energy.md), interpreted against the source-rank/codimension framework of MC-385--MC-396.

Suppose the surviving source modes form a vector space `W<=F_2^R` with common radical modulus `P`. MC-397 shows that uniform averaging of the squared source-mode observable collapses exactly to a nonnegative signature-subgroup projector. Source-mode multiplicity remains useful for rank/codimension and fourth-moment geometry, but the isolated mode label is not automatically an arithmetic averaging direction.

MC-398 supplies the same audit one layer later for the squared Selberg majorant. If `f(n)=(sum_(d|n)g(d))^2`, simultaneous divisibility depends on `(d_1,d_2)` only through `ell=[d_1,d_2]`; every arithmetic inner quantity that sees the pair only through this lcm can therefore be regrouped through one coefficient `C_g(ell)`. Pair labels supply coefficient multiplicity, not two arithmetic samples.

MC-399 shows that even a variable surviving regrouping may disappear before useful cancellation geometry forms. After source Fourier expansion, complete multiplicativity gives `chi_I(ell m)=chi_I(ell)chi_I(m)`, so the `ell`-dependent scalar vanishes at the first additive correlation in `m`. The lcm factor is not a retained Stadlmann-style mixed phase merely because it is visible in the uncorrelated formula.

MC-400 adds a fourth exact audit: surviving endpoint dependence can still be only an invertible coordinate system. With `c_chi(ell)=C_g(ell)chi(ell)`, the twisted majorant satisfies `f_chi=chi*c_chi` and `c_chi=(mu chi)*f_chi`. The summatory hyperbola transform has an exact Möbius inverse, so the moving endpoint `N/ell` does not itself add arithmetic information.

MC-401 adds a fifth audit at the complete endpoint. When `N=B^2`, the lcm cutoff is inactive and the entire quadratic form is exactly a signed gcd/divisor energy,

`A_chi(B^2)=sum_(k<=B) (mu *_D chi)(k) (sum_(k|d,d<=B) g(d)chi(d))^2`.

Thus even after retaining lcm coefficients and endpoint dependence, the full endpoint can collapse into a classical meet-incidence factorization. The unit-prime sign case is genuinely indefinite rather than positive, so the factorization is not itself a cancellation theorem; it identifies where the nontrivial source information would have to live.

The reusable test is therefore staged. Before crediting a formal index as a new cancellation dimension, perform every exact Fourier/regrouping reduction, then the first correlation/Cauchy step meant to exploit it, ask whether the surviving family is exactly invertible back to the original data, and finally test natural complete endpoints for a classical incidence factorization. **A variable counts only if it survives these audits with a source-specific relation that cannot be reconstructed or collapsed for free.**

For the present endpoint frame, the surviving information may lie in nontrivial structure of the signed coefficient/signature distribution `C_g(ell)chi_I(ell)`, in the incomplete hyperbola mask before `N=B^2`, or in a pre-quadratic representation whose divisor/source variable does not factor through lcm and remains nonseparable through the relevant correlation.

**Boundary.** MC-401 does not prove that the signed gcd energy is small, estimate the truncated endpoint, or rule out genuinely joint bilinear/pre-quadratic structure. MC-400 does not make the coefficient distribution analytically useless. These findings rule out only treating source-mode labels, divisor-pair multiplicity, the standard lcm phase, the invertible hyperbola coordinate, or the complete lcm endpoint as independent information without exhibiting an additional noncollapsing relation. No improved Möbius cancellation or RH consequence follows.