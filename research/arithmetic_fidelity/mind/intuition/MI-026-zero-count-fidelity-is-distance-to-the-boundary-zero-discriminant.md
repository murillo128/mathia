# MI-026 — Zero-count fidelity is projective distance to failure; unrestricted linear dimension reduction collapses that distance

**Evidence level:** proved for finite Dirichlet-polynomial zero-count geometry by AF-290--AF-299; transfer from acquisition remains conditional on the actual coefficient-orbit error.

AF-290 identifies the exact robustness radius for the zero count inside a fixed zero-free Jordan contour `Gamma`: the coefficient-space distance from `b` to the boundary-zero discriminant. AF-295 shows that, because this discriminant is a complex cone,

`dist_gap([b], P Delta) = dist(b,Delta)/||b||`.

Thus the normalized margin is exactly intrinsic projective separation from failure after quotienting global complex amplitude and phase. AF-291 shows that this margin can still collapse with breadth even while eta truncations converge correctly on the contour.

AF-292--AF-294 close positive diagonal Hilbert reweighting, bounded-condition dense Hilbert mixing, and uniformly quasisymmetric nonlinear transport as free repairs. AF-296--AF-297 classify target-radial conformal repair: if the radial density `phi(r)` is integrable at zero, a collapsing raw margin still collapses; if it is nonintegrable, failure is moved to an infinite-distance ideal boundary. A finite order-one repair at raw scale `r_N` must reach density at least `c/r_N` somewhere in the collapsing layer.

AF-298 tests a genuinely anisotropic but still target-observation-generated class. For `G_(mu,N)=int_Gamma r_z r_z^* dmu(z)`, with leverage `K_(mu,N)(z)=r_z^* G_(mu,N)^(-1) r_z`, the exact zero-count margin is `delta_(mu,N)=min_z |eta_N(z)| / (||eta_N||_(L2(mu)) sqrt(K_(mu,N)(z)))`. The trace identity `int_Gamma K_(mu,N)(z) dmu(z)=N` forces `sup_z K_(mu,N)(z)>=N`, while a `D`-optimal design attains maximum leverage `N`. Positive boundary-observation Gram metrics can therefore remove the extra evaluation-growth bill but not the irreducible `sqrt(N)` effective-dimension bill.

AF-299 then tests whether one can pay less simply by making that metric singular or quotienting coefficient space. Let `Delta=union_a ker ell_a` and `C=intersection_a ker ell_a`. A linear quotient `q` with kernel `K` preserves failure membership exactly only when `K subset C`; if `K not subset C`, then `q(Delta)=q(V)`. For the Dirichlet boundary evaluations `ell_z(c)=P_c(z)`, the identity theorem and independence of finite Dirichlet sums give `C={0}`. Therefore every nontrivial additive linear quotient sends the boundary-zero discriminant onto the whole quotient, and every rank-deficient PSD metric has zero failure margin.

So “effective dimension `r<N`” is not a coordinate choice. On the unrestricted coefficient class it needs an actual mathematical reason that removes directions **before** the quotient: a source-restricted manifold/class whose fibers cannot hit failure, a genuine nonlinear/projective symmetry, or a different coupled/source-derived observable with a different failure geometry. Merely projecting coefficients, choosing a low-rank Gram matrix, or observing that the final statistic is low-dimensional destroys the exact discriminator.

**Boundary.** AF-299 concerns global additive linear quotients of the full finite coefficient space. It does not rule out source-restricted families, projective/nonlinear symmetries, derivative/vector/nonlocal observations, or source-derived information. AF-298--AF-299 together say that reweighting the same scalar evaluations leaves a `sqrt(N)` bill, while deleting their coefficient directions without a prior target-null theorem makes the failure margin exactly zero.
