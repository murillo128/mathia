# MI-004 — Pointed positivity can regularize the Mangoldt trace without keeping it coupled to the critical positive bulk

**Evidence level:** supported by exact positive constructions and obstructions from WP-067--WP-079, strengthened by the canonical cyclotomic Hardy-space control [WP-378](../../findings/WP-378-cyclotomic-hardy-positivity-factorizes-primewise-and-mangoldt-is-an-unbounded-boundary-trace.md) and the pointed half-turn control [WP-379](../../findings/WP-379-critical-pointed-half-turn-gram-is-universal-and-mangoldt-contrast-vanishes.md).

The finite arithmetic package is stronger than merely having a formal Mangoldt label. In pointed local Dirichlet geometry, intrinsic covers force the critical half-weight, a positive trace-class cocycle supplies `log n`, and Möbius extraction gives the exact scalar coefficient `Lambda(n)/sqrt(n)`. WP-072--WP-079 show that topology can therefore regularize a boundary selector which is singular in the natural rotation-invariant Hardy geometry. The unresolved issue is whether that selector remains coupled to a source-specific positive bulk through the critical limit and global completion.

WP-378 sharpens the first half of the warning. For `F_n(z)=log Phi_n(z)` in `H^2(D)`, the positive Gram kernel has genuine cross-prime terms but factorizes exactly into local Euler factors. Its diagonal depends only on `rad(n)`, assigns positive energy to mixed shells and forgets the prime-power exponent. The exact selector survives only at the boundary,

`F_n(1)=log Phi_n(1)=Lambda(n)`,

while evaluation at `1` is unbounded in `H^2`; prime-power shell norms stay bounded even as the desired value grows like `log p`.

WP-379 tests whether pointing fixes that mismatch in the most economical two-channel way. For odd degree `N`, let `A_N` be the full-root logarithmic shell and `B_N=A_N(-z)` its half-turn. In the pointed local Dirichlet form, after the critical `N^(-1/2)` cover normalization,

`N^(-1) Gram(A_N,B_N) -> [[C,(C-log 2)/2],[(C-log 2)/2,log 2]]`.

The limit is positive definite, so the point really breaks the rotation-invariant blindness. But it is **universal across every odd degree**, prime or composite. At the same time `A_N(1)=log N` and `B_N(1)=0`, so on prime shells the arithmetic contrast becomes `log p/sqrt(p)` and vanishes. The positive bulk and the exact selector are both present at finite scale, yet the critical normalization sends them to incompatible asymptotic currencies.

This separates three gates that are easy to conflate: **selector regularity**, **positive incidence**, and **destination-scale coupling**. A topology can make the selector legitimate without making it load-bearing in the limiting positive form. Conversely, a nondegenerate positive Gram can retain mixed geometry while a matched composite control reproduces its entire limit and the arithmetic distinction escapes into a vanishing boundary channel.

A surviving route must therefore derive a source-forced topology or finite--archimedean assembly in which the linear Mangoldt selector remains quantitatively coupled to the positive bulk at the critical destination. Possibilities left open include singular/renormalized boundary geometry, genuinely multi-place incidence before scalarization, or an indefinite intermediate pairing whose final global completion proves the sign. Merely replacing radial or Hardy positivity by the canonical pointed Gram is not enough.

**Boundary.** WP-378 rules out the canonical unweighted Hardy Gram and fixed bounded `H^2` background readouts. WP-379 rules out only the canonical critical pointed half-turn completion: it does not rule out pointed Dirichlet geometry with additional source-forced couplings, singular boundary terms, archimedean completion, or topologies in which trace and bulk remain coupled. Neither result proves global Weil positivity or RH.