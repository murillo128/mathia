# MI-023 — Unbounded exact Farey horizons rigidify a permanent source but do not provide stability

**Evidence level:** exact synthesis from [FD-164](../../findings/FD-164-one-horizon-complete-farey-field-leaves-dense-orientation-kernel.md), [FD-165](../../findings/FD-165-polylogarithmic-horizon-bundles-leave-dense-orientation-kernels.md), and [FD-166](../../findings/FD-166-unbounded-exact-farey-horizons-rigidify-a-permanent-source.md).

Finite-cutoff and permanent-source ambiguity are different questions. FD-164 shows that one complete Farey discrepancy field can be matched exactly while changing a dense fraction of squarefree Möbius orientations. FD-165 extends this to large finite horizon bundles: whenever `J_T M_beta(T)=o(T)`, one source chosen for that finite bundle can still retain a dense high-coordinate orientation kernel.

FD-166 shows why those controls cannot converge to a distinct permanent exact source. The quotient set exposed by one complete horizon `H` contains every consecutive integer through `floor(sqrt(H))`. Exact equality of complete fields therefore forces

`A(r)=M(r)` and `a(r)=mu(r)` for every `r<=floor(sqrt(H))`.

If one fixed source matches the physical complete field on any unbounded set of horizons, however sparse, these forced prefixes exhaust every finite coordinate and the source is exactly Möbius. Equivalently, a permanent source whose first defect is at `n_0` cannot match any complete field once `H>=n_0^2`.

The finite-bundle kernels of FD-164--FD-165 are therefore **noncompact in source coordinates**. Their altered orientations must migrate outward as the cutoff grows. More horizons help only when the compatibility requirement binds them to one permanent latent source; no critical density of exact complete horizons is needed once the hierarchy is unbounded.

This exact rigidity does not solve the useful analytic problem. The inversion from a complete Farey field to the quotient Mertens staircase may be badly conditioned under approximate data, and a partial/coarsened observation may no longer expose a consecutive square-root prefix. The live question is quantitative stability and economical observation: how accurately and how sparsely can one observe the field while still forcing enough coefficient information to affect the Franel--Landau destination?

**Boundary.** FD-166 is an exact information theorem, not a cancellation estimate. It does not show that approximate complete fields determine an approximate Möbius prefix at a useful norm/scale, and it does not imply that recovering coefficients yields the RH-critical discrepancy bound.