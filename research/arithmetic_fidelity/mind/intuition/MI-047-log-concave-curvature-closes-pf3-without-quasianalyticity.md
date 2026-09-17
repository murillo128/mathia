# MI-047 — Curvature mass plus connected positive-curvature support exactly characterizes smooth `PF_3`

**Evidence level:** exact synthesis from [AF-388](../../findings/AF-388-shrinking-solid-pf3-excludes-quadratic-boundary-contact.md) through [AF-394](../../findings/AF-394-connected-curvature-support-completes-smooth-pf3-fidelity.md).

For a positive `C^4` profile `f`, write `q=-(log f)''`. AF-392 expresses continuum order-three total positivity through every adjacent pair of curvature-mass windows. AF-393 shows that on the stratum `q>0` those finite-window conditions contain no information beyond the local inequality

`(log q)'' <= 2q`.

The right coordinate is curvature mass. If `dQ=q dt` and `r=(log q)'`, then the condition is simply

`dr/dQ <= 2`.

The AF-392 adjacent-window inequality is its integrated form, and shrinking the windows differentiates it back. Thus positive-curvature local and finite-window recognition are the same intrinsic constraint written at different scales.

AF-394 supplies the missing global piece. The translation kernel `K_f(x,y)=f(x-y)` is `TN_3` exactly when

1. `q>=0`;
2. `{q>0}` is an interval, allowing the empty and unbounded cases;
3. `(log q)''<=2q` on `{q>0}`.

The zero-curvature boundary therefore contributes one qualitatively different resource: **component topology**. Local differential information controls the shape inside each positive-curvature region, but it cannot say whether two such regions are parts of one component separated by a zero. A separating zero, even an infinitely-flat one, creates a nonlocal order-three obstruction; a boundary zero of one connected component is allowed.

This completes the multiscale interpretation of AF-388--AF-393. Under shrinking solid `PF_2/PF_3` consistency, `q>=0` and the differential inequality are already forced. The exact residual question is not another Taylor coefficient or another finite-window inequality: continuum `TN_3` holds iff the positive-curvature set is connected.

AF-390 and AF-391 now sit in the correct hierarchy. Quasianalytic flat-jet uniqueness and log-concavity of `q` are sufficient closures because they force an admissible connected topology, but they are not the recognition variable itself. The target permits broader nonquasianalytic behavior as long as the positive-curvature region remains one interval and the intrinsic slope bound holds.

The reusable lesson is concrete. A hierarchy of arbitrarily fine local certificates can recover the complete differential cone relevant to a target and still lose a global discriminator that lives only in **which local regions belong to the same component**. Any compressed arithmetic construction using such certificates must retain or derive that topology explicitly; local resolution cannot manufacture it afterward.

**Boundary.** The characterization is an order-three, source-independent recognition theorem. It does not produce the required solid signs or curvature connectedness from prime data, does not claim novelty over the classical `PF_3` literature, does not extend automatically to higher `PF_k`, and does not provide a Riemann-zero selector.