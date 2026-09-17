# MI-049 — Physical locality walls have source-dependent index depth

**Evidence level:** exact synthesis from [AF-395](../../findings/AF-395-fixed-successor-radius-misses-disconnected-curvature-on-prime-log-meshes.md) through [AF-399](../../findings/AF-399-regular-variation-converts-physical-locality-walls-into-successor-resource-laws.md). The regular-variation conversion is exact within the stated asymptotic hypotheses; no detector theorem is transferred between source families.

A locality threshold should first be stated in the source's intrinsic physical coordinate and only then converted into a combinatorial index budget. If an increasing source scale `a_N` is regularly varying with index `rho>0`, then a fixed logarithmic reach `h` corresponds to successor depth

`B_N(h)/N -> exp(h/rho)-1`.

When the source admits a locally uniform second-order expansion

`log(a_floor(lambda N)/a_N)=rho log lambda + epsilon_N psi(lambda)+o(epsilon_N)`,

with `N epsilon_N -> infinity`, the same physical wall acquires the source-dependent correction

`B_N(h)=(lambda_*-1)N-[lambda_* psi(lambda_*)/rho]N epsilon_N+o(N epsilon_N)`,

where `lambda_*=exp(h/rho)`. Thus the physical wall is invariant while its index depth records the density law of the source coordinates.

The prime-log `PF_3` boundary is one specialization. For `a_N=p_N`, `rho=1`, `h=1` and the prime-density expansion, the fixed physical reach one becomes the `(e-1)N` successor wall with the `-eN/log N` and later prime-density corrections found in AF-396--AF-398. AF-397's one-mesh overhang remains the detector-side margin: the source-density law locates the wall, while the determinant argument decides how much physical overhang is sufficient to cross it.

The reusable rule is therefore: **do not treat successor count as an intrinsic locality resource**. State the physical relation first, then pull it back through the source coordinate map. Finer source density can change the number of indices needed to realize the same mathematical reach without changing the underlying locality threshold at all.

**Boundary.** AF-399 assumes fixed `h`, regular-variation index `rho>0`, and enough uniformity for the stated second-order expansion. It does not cover moving physical walls, rapidly varying or index-zero scales, supply a determinant detector by itself, or show that higher-order total-positivity problems have the same topological obstruction.