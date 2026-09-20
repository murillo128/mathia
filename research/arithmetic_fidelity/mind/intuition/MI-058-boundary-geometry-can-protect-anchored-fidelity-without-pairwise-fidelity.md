# MI-058 — Boundary geometry can protect anchored fidelity without improving convex pairwise linear fidelity

**Evidence level:** exact source-geometry synthesis from [AF-462](../../findings/AF-462-finite-support-simplex-boundaries-separate-anchored-from-pairwise-hilbert-fidelity.md) and [AF-463](../../findings/AF-463-convex-boundaries-do-not-improve-pairwise-linear-fidelity-beyond-affine-hull.md), interpreted against the paired-cube obstruction of AF-459--AF-461. The anchored statement is a finite-support simplex result; the pairwise classification is for convex sources and bounded linear destinations in the ambient norm.

At a probability law `mu_0` with finite support `S`, positivity makes the anchored feasible directions genuinely one-sided: negative coordinates can occur only inside `S`, while positive mass may move onto fresh coordinates. If `s=|S|`, AF-462 proves the paired-cube defect bound

`D_k >= (1-s/k)_+`,

and the canonical one-hot Hilbert embedding has exact anchored TV gain `1/sqrt(s)`. So a convex boundary can carry real source provenance when every comparison is made against one distinguished anchor.

AF-463 identifies the exact pairwise geometry once both source points may move. For every convex source class `C`,

`T_C^P(x_bar) = closure(span(C-C)) =: L_C`

at every base point. Moreover, for a bounded linear map `F:X->Y` and any relative neighborhood `W` of `x_bar`,

`kappa_W(F;C) = inf_(0 != v in L_C) ||Fv||/||v||`.

Thus moving comparisons symmetrize every one-sided active-face restriction: convex boundary information cannot improve the pairwise local linear modulus beyond the closed affine direction space. For the countable simplex, `L_C` is the zero-sum subspace of `ell^1`; diffuse signed directions have fixed `ell^1` norm and vanishing `ell^2` norm, so the canonical `ell^1 -> ell^2` pairwise gain is zero in every neighborhood of every source law. The fresh-support construction of AF-462 is one witness of this general paratingent fact.

The reusable distinction is therefore exact: **one-sided provenance can protect an anchored discriminator, while convexity itself removes that protection from arbitrary pairwise linear recovery**. If the physical task is pairwise, a source-side escape must change the paratingent geometry rather than merely strengthen convex inequalities, or else change the metric/operator category.

**Boundary.** The sharp anchored modulus `1/sqrt(s)` is specific to the finite-support anchor and canonical one-hot Hilbert embedding. The pairwise identity uses convexity, bounded linearity and the ambient norm; nonconvex/singular source classes, nonlinear or relational destinations, and different intrinsic source metrics are not classified by AF-463. No arithmetic conclusion follows until the actual physical source and comparison class are identified.