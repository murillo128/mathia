# MI-019 — Flat covariance and faithful site metrics cannot create Weil support; escape starts at curvature or source-forced nullspace

**Evidence level:** exact linear classification from [WP-295](../../findings/WP-295-hilbert-valued-prime-power-support-forces-one-mobius-direction.md), [WP-296](../../findings/WP-296-multiplicative-shift-equivariant-nonlocal-couplings-are-dirichlet-convolution.md), [WP-297](../../findings/WP-297-flat-multiplicative-boundary-cocycles-are-gauge-trivial.md), and [WP-298](../../findings/WP-298-faithful-nonparallel-site-metrics-cannot-evade-mobius-support-rigidity.md). This closes a representation class; it does not construct the surviving geometry or prove Weil positivity.

Exact finite Weil localization is rigid under fixed positive channels and equivariant linear depth. WP-295 forces one visible direction `u Lambda` with upstream kernel `u mu`; WP-296 shows finite multiplicative-equivariant linear networks collapse to one operator-valued Dirichlet convolution.

WP-297 shows that flat site-dependent transport is only gauge. A multiplicative cocycle has

`C(m,n)=G(mn)G(n)^(-1)`,

so after the pointwise gauge the architecture returns to ordinary equivariance. A metric parallel under that transport becomes fixed.

WP-298 shows that **dropping metric parallelity is still not enough**. After the flat gauge reduction, take arbitrary invertible `G(N)` and arbitrary positive-semidefinite pointwise metrics `Q_N`. If `Q_N` is faithful at every mixed composite and the scalar readout is exactly `Lambda(N)`, positivity implies the vector response itself vanishes at every mixed composite. WP-295 then forces the same Möbius direction.

The support-changing datum of a pointwise positive metric is therefore not its orientation or conditioning but its nullspace. In general exact mixed-composite deletion requires

`B(N) in G(N)^(-1) ker Q_N`.

A non-Möbius pointwise escape must contain genuine source-forced degeneracy. This is necessary but not automatically meaningful: an arbitrary moving kernel can program the Mangoldt support directly, so its zero directions must be derived independently from the geometry and survive matched generalized-prime controls.

The first genuine linear transport escape remains **non-flat mixed-prime incidence**. A prime diamond must carry nontrivial holonomy/curvature so that the two paths to `pqn` cannot be gauged into agreement. Other category changes include extra boundary topology/orbits, nonlinear support-sensitive structure before scalarization, genuinely nonlocal positive forms coupling sites, or finite--archimedean geometry.

The reusable test is now two-stage. First quotient removable gauge freedom and ask whether a closed-loop invariant survives. If transport is flat, pointwise positive site variation still cannot change exact support unless it becomes degenerate. Second, if degeneracy appears, ask whether its kernel is source-forced rather than an encoded selector.

**Boundary.** Curvature or a canonical moving nullspace only escapes the localization no-go. Either must still reproduce the archimedean/polar terms and support an independent positivity theorem; neither by itself implies Weil positivity or RH.
