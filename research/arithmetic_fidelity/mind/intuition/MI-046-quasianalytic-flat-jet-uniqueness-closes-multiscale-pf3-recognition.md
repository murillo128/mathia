# MI-046 — Quasianalytic flat-jet uniqueness is a sufficient source-class closure, not the exact smooth `PF_3` boundary

**Evidence level:** exact/literature-backed synthesis from [AF-385](../../findings/AF-385-sampled-solid-minor-hierarchy-certifies-continuum-fixed-order-total-nonnegativity.md), [AF-389](../../findings/AF-389-multiscale-solid-pf3-excludes-all-finite-order-boundary-contact.md), [AF-390](../../findings/AF-390-quasianalytic-curvature-closes-multiscale-pf3-recognition.md), and [AF-394](../../findings/AF-394-connected-curvature-support-completes-smooth-pf3-fidelity.md).

For a positive smooth profile `f`, write `q=-(log f)''`. If the same profile has nonnegative solid Toeplitz minors of orders two and three on meshes `h_n -> 0`, AF-389 forces `q>=0` and makes every zero of `q` infinitely flat. The multiscale observation has therefore recovered the complete finite jet of the lower-order boundary defect.

AF-390 identifies one source-class route from that recovered jet to the target. Assume flat-zero unique continuation for `q`: if `q^(m)(x_0)=0` for every `m`, then `q≡0`. Then the sampled hierarchy leaves only two branches. Either `q>0` everywhere, so the strict lower-order recognition theorem upgrades the solid order-three generators to all continuum order-three placements, or `q≡0`, so `f=e^(ax+b)` and the translation kernel has rank one. Real analyticity and suitable Denjoy--Carleman classes are examples of this mechanism.

AF-394 shows that this source rigidity is stronger than the exact smooth target requirement. For positive `C^4` profiles the full order-three condition is

`q>=0`, `{q>0}` is an interval, and `(log q)''<=2q` on `{q>0}`.

Under the shrinking solid hierarchy the first and third conditions are already present. Thus flat-zero unique continuation closes the problem because it forces an especially simple connectedness dichotomy, not because every infinitely-flat zero is incompatible with `TN_3`. A nonquasianalytic boundary zero can be perfectly admissible when the positive-curvature set remains one interval.

The conceptual point survives in a sharper form: **regularity is useful only after the observation has recovered the invariant that the regularity can rigidify, but the imposed source rigidity should be compared with the exact target fibre before being credited as necessary information**. Here quasianalyticity collapses the residual fibre more than needed; connected component topology is the exact remaining resource.

This also separates source rigidity from target reconstruction. The observation need not identify `f`; it only needs to make the admissible source fibre target-pure. Quasianalyticity is one way to do that, while AF-394 proves that retaining the connectedness of `{q>0}` is enough in the full smooth category.

**Boundary.** Flat-zero unique continuation remains a valid sufficient source hypothesis, but it is not necessary for smooth `TN_3` recognition. None of these results derives curvature connectivity or the sampled generator signs from a Riemann-associated source, extends the exact classification to higher determinant order, or supplies a zero-selection theorem.