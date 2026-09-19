# MI-038 — Fixed root-filter families have an exact annular spectral dichotomy

**Evidence level:** exact synthesis from [FD-210](../../findings/FD-210-fixed-signed-root-filters-have-a-supercritical-spectral-blind-annulus.md) and [FD-211](../../findings/FD-211-annulus-free-gcd-makes-fixed-root-filter-families-square-root-complete.md), building on the root increment and binary-prefix inversion of FD-206--FD-209.

Let

`Delta(n)=A(2n)-A(n)`, `A(N)=sum_(m<=N) u_m`, `|u_m|<=C`, and `(TF)(n)=F(2n)`.

For a fixed finite family of nonzero polynomial root filters `P_1(T),...,P_r(T)`, write `G=gcd(P_1,...,P_r)`. The physical bounded-source problem has a sharp spectral split at the annulus

`sqrt(2)<|rho|<=2`.

FD-210 supplies the blind direction. If the family has a common characteristic root `rho` in that annulus, there exists a bounded source, even with coefficients in `{-1,0,1}`, whose summatory function grows like `N^alpha` for some `alpha>1/2` while every filtered observable `P_i(T)Delta(n)` remains bounded. Critical random cost therefore does not imply source completeness; a fixed filter can be spectrally blind in the physical growth range.

FD-211 proves the converse. If `G` has no zero in the annulus, square-root-plus-epsilon bounds for all `P_i(T)Delta(n)` force

`A(N)=O_epsilon(N^(1/2+epsilon))`

for every bounded source. The proof uses a source property that an arbitrary dyadic sequence need not have: every fixed polynomial transform of `Delta` has a uniformly bounded binary sibling defect. Factoring `G` into linear terms then gives two stable inversion regimes. Roots with `|rho|<=sqrt(2)` are inverted down the binary ancestor tree at square-root cost, while roots with `|rho|>2` are inverted forward using the linear source bound. The open annulus between those regimes is exactly where the FD-210 blind modes live.

For `u_m=mu(m)`, this becomes a precise theorem-surface statement. If the gcd is annulus-free, pointwise square-root-plus-epsilon control of the fixed filter family is equivalent to RH; if the gcd has an annular root, the family is not even complete on the larger class of bounded sources.

The reusable point is that **fixed signed root filtering has no intermediate spectral regime**. A fixed finite family either has a common physical supercritical blind root, or its critical pointwise control already reconstructs the square-root destination. Adding finitely many filters helps only by removing common roots; once the common annular zero disappears, the family has become destination-complete rather than merely more informative.

The surviving escape must therefore alter one of the hypotheses that makes the dichotomy exact: let the filter vary with scale, let degree grow, weaken or average the observation norm, break pointwise coherence along binary ancestors, or use a non-polynomial/non-fixed structure whose physical inverse is not represented by one fixed gcd.

**Boundary.** The dichotomy is for fixed finite polynomial families acting on the physical root increment of bounded sources and pointwise `n^(1/2+epsilon)` control. It does not classify scale-dependent filters, growing-degree families, averaged inequalities, diagonal `q(n)` observations, or collective structures that never yield one fixed polynomial family on a binary-prefix window. The RH equivalence is specific to the Möbius source after this bounded-source inversion theorem is established.
