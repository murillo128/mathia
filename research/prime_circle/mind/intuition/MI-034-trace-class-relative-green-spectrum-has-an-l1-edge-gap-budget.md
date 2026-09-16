# MI-034 — Trace-class relative Green spectrum has an `ell^1` edge-gap budget

**Evidence level:** exact synthesis from [PC-323](../../findings/PC-323-cross-level-green-operator-is-hilbert-plus-trace-class.md) and [PC-326](../../findings/PC-326-relative-green-determinant-has-summable-edge-gap-divisor.md), with [PC-325](../../findings/PC-325-green-relative-spectrum-is-phase-gauge-and-autocorrelation-only.md) fixing the source quotient carried by the same relative pair.

The canonical cross-level Green operator survives the absolute trace-class obstruction by being noncompact: after removing its universal Hilbert channel one has a self-adjoint pair

`G = G_0 + V`, with `V` trace class and `sigma(G_0)=[-E,E]`.

That does not make the relative determinant an unrestricted zero carrier. Its zeros off the Hilbert band are exactly the discrete eigenvalues of `G`, and self-adjoint trace-class perturbation theory gives the fixed-source budget

`sum_(lambda_j notin [-E,E]) dist(lambda_j,[-E,E]) <= ||V||_1`.

An infinite relative zero sequence can therefore exist only by approaching the two continuum edges with summable gaps. This is the intrinsic density law of the surviving spectral object.

The comparison with the Riemann divisor is then immediate. The Riemann--von Mangoldt density implies `sum gamma_j^(-alpha)=infinity` for every `0<alpha<=1`. Hence no direct identification and no edge compactification whose gap is comparable to `gamma^(-alpha)` with `alpha<=1` can turn the PC-323 relative determinant into the full Riemann-zero divisor. In particular the natural reciprocal/Cayley scale `1/gamma` remains too dense.

This is not the earlier PC-107 trace-class determinant obstruction in different notation. PC-107 constrains zeros in an unbounded determinant variable through reciprocal eigenvalue summability. Here the operator has a noncompact Hilbert band and the relevant invariant is **summability of distance from the continuum**. Moving to a relative determinant changes the spectral geometry but does not remove its trace-ideal density budget.

Together with PC-325, the fixed-conductor Green branch is doubly constrained: its source dependence factors through autocorrelation, and any off-band relative divisor is `ell^1` at the band edge. A useful continuation must change one of those structural facts rather than reparameterize the same spectrum.

**Boundary.** The argument does not exclude a source-derived singular conductor/cross-level limit in which the trace norm diverges, a non-trace-class comparison defect, or a genuinely different nonseparable operator. Nor does it prohibit a faster-than-reciprocal edge coordinate if that coordinate is independently forced by the geometry. It rules out treating an arbitrary nonlinear compactification as mathematical content.