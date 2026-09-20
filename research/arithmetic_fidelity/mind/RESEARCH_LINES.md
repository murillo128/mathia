# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`, `MI-057-paired-sign-cubes-transfer-banach-type-to-source-relative-mixture-fidelity`, `MI-058-boundary-geometry-can-protect-anchored-fidelity-without-pairwise-fidelity`.

AF-451--AF-457 identify the completed source-law secant carrier and the target-category obstruction: full-simplex TV fidelity under bounded linear/barycentric observation requires an `ell^1` copy in the target, while Hilbert sparse-mixture gain falls at the sharp `Theta(k^(-1/2))` scale. AF-458--AF-461 transfer that obstruction to restricted sources through paired-cube completion and show that bounded finite-rank laws and regular finite-dimensional `C^1` equality fibers remain cube-complete.

AF-462 identifies a real but one-sided boundary escape. At a finite-support simplex law `mu_0`, anchored directions may be negative only on `supp(mu_0)`, giving `D_k >= (1-s/k)_+` for `s=|supp(mu_0)|`; the canonical one-hot Hilbert embedding has exact anchored TV gain `1/sqrt(s)`.

AF-463 now classifies why that escape cannot be promoted to arbitrary nearby pairs inside a convex source class. For convex `C`, the moving-secant paratingent cone at every base point is

`T_C^P = closure(span(C-C)) =: L_C`,

and for every bounded linear `F` and every relative neighborhood `W`,

`kappa_W(F;C) = inf_(0 != v in L_C) ||Fv||/||v||`.

Thus convex boundary inequalities contribute no extra pairwise local linear fidelity beyond the affine direction space. On the countable simplex the zero-sum `ell^1` direction space has zero lower modulus under the canonical `ell^1 -> ell^2` inclusion, so the pairwise collapse holds around every source law, not only the finite-support witness of AF-462.

The live arithmetic question must therefore state which comparison the downstream theorem actually consumes. If it is anchored, a distinguished finite-support or otherwise one-sided physical source can still matter. If it is pairwise under a bounded linear destination, stronger convex positivity is no longer an escape: one needs a genuinely smaller nonconvex/singular paratingent carrier, a different source metric, a destination bounded below on the affine direction space, or nonlinear/relational information whose local behavior is not one fixed linear map.

## Keep identifiability, anchored provenance and pairwise stability separate

Exact injectivity, atom separation and anchored discrimination can each coexist with zero pairwise inverse margin. AF-462 shows that a convex boundary can stay macroscopically far from large paired cubes for anchored directions; AF-463 shows that moving two comparison points symmetrizes the same convex boundary back to its full affine direction space.

A fidelity theorem must therefore state the source metric, admissible comparison class, whether the claim is anchored or pairwise, the completed secant/paratingent carrier, target/operator category and the positive lower gain actually consumed downstream. Cube-poorness of an anchored cone is not pairwise stability, while pairwise failure for a convex linear model does not negate a genuinely anchored theorem.