# MI-026 — Zero-count fidelity is projective distance to failure, with separate radial and effective-dimension bills

**Evidence level:** proved for finite Dirichlet-polynomial zero-count geometry by AF-290--AF-298; transfer from acquisition remains conditional on the actual coefficient-orbit error.

AF-290 identifies the exact robustness radius for the zero count inside a fixed zero-free Jordan contour `Gamma`: the coefficient-space distance from `b` to the boundary-zero discriminant. AF-295 shows that, because this discriminant is a complex cone,

`dist_gap([b], P Delta) = dist(b,Delta)/||b||`.

Thus the normalized margin is exactly intrinsic projective separation from failure after quotienting global complex amplitude and phase. AF-291 shows that this margin can still collapse with breadth even while eta truncations converge correctly on the contour.

AF-292--AF-294 close positive diagonal Hilbert reweighting, bounded-condition dense Hilbert mixing, and uniformly quasisymmetric nonlinear transport as free repairs. AF-296--AF-297 classify target-radial conformal repair: if the radial density `phi(r)` is integrable at zero, a collapsing raw margin still collapses; if it is nonintegrable, failure is moved to an infinite-distance ideal boundary. A finite order-one repair at raw scale `r_N` must reach density at least `c/r_N` somewhere in the collapsing layer.

AF-298 then tests a genuinely anisotropic but still target-observation-generated class. For

`G_(mu,N)=int_Gamma r_z r_z^* dmu(z)`,

with leverage

`K_(mu,N)(z)=r_z^* G_(mu,N)^(-1) r_z`,

the exact zero-count margin is

`delta_(mu,N)=min_z |eta_N(z)| / (||eta_N||_(L2(mu)) sqrt(K_(mu,N)(z)))`.

The trace identity

`int_Gamma K_(mu,N)(z) dmu(z)=N`

forces `sup_z K_(mu,N)(z)>=N` for every full-rank boundary weighting. Conversely a `D`-optimal design equalizes the maximum leverage at `N`. Hence, uniformly over all `N`-dependent positive boundary-observation Gram metrics,

`sup_mu delta_(mu,N) asymp_Gamma N^(-1/2)`.

This separates two conditioning bills that the raw coefficient norm had conflated. Target-aligned anisotropy can remove the extra evaluation-growth factor `H_N(alpha)`, but a full-rank scalar boundary-observation family still pays an irreducible `sqrt(N)` effective-dimension bill. Reweighting sensitivity is not the same as reducing target-relevant dimension.

The surviving geometric route is therefore precise. To beat the `N^(-1/2)` ceiling one must justify a target-null quotient that lowers effective dimension, use a richer coupled/vector/nonlocal observable whose failure kernels differ from the scalar evaluation discriminant, or inject source-derived arithmetic information not already contained in positive averages of the same boundary evaluations.

**Boundary.** AF-298 does not rule out arbitrary source-derived SPD forms, singular quotients proved target-null, derivative/vector observations, nonlinear coupled observables, enriched source data, or another target category. It rules out the canonical hope that unrestricted anisotropic `L^2` reweighting of the same scalar contour observations can make zero-count fidelity breadth-uniform.