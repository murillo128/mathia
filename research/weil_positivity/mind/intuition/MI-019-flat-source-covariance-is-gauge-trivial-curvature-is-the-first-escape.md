# MI-019 — Flat source covariance is gauge-trivial; genuine escape starts at mixed-prime curvature

**Evidence level:** exact linear classification from [WP-295](../../findings/WP-295-hilbert-valued-prime-power-support-forces-one-mobius-direction.md), [WP-296](../../findings/WP-296-multiplicative-shift-equivariant-nonlocal-couplings-are-dirichlet-convolution.md), and [WP-297](../../findings/WP-297-flat-multiplicative-boundary-cocycles-are-gauge-trivial.md). This closes a representation class; it does not construct the non-flat geometry or prove Weil positivity.

Exact finite Weil localization is much more rigid than “use multiple channels” or “mix sites nonlocally.” WP-295 shows that a Hilbert-valued divisor convolution of the logarithmic carrier which vanishes off prime powers has only one visible direction:

`F(N)=u Lambda(N)`, `A(N)=u mu(N)`.

A positive channel norm can hide the sign after the fact, but the upstream inverse is still Möbius and its Dirichlet transform still contains `1/zeta`.

WP-296 closes the linear nonlocal equivariant escape. Every coefficientwise-continuous linear map commuting with multiplicative shifts is an operator-valued Dirichlet convolution,

`(Tf)(N)=sum_(d|N) K(d) f(N/d)`.

Finite stacks collapse to one effective kernel. Therefore linear depth and channel width do not enlarge the visible architecture as long as multiplicative translation symmetry is preserved; WP-295 applies to the composite.

WP-297 closes a natural site-dependent weakening. If the output fibers are transported by a flat multiplicative cocycle `C(m,n)`, then the rooted action at `1` trivializes it exactly:

`C(m,n)=G(mn)G(n)^(-1)`.

After the pointwise gauge `G`, every intertwiner is again an ordinary equivariant convolution. Unitary transport leaves the norm unchanged, and a positive metric parallel under the transport becomes one fixed metric after gauge. Exact Weil localization therefore forces the same visible Möbius direction.

The first genuine linear escape is consequently **non-flat mixed-prime incidence**. On a prime diamond the flat cocycle forces the two paths `n -> pn -> pqn` and `n -> qn -> pqn` to agree. A candidate outside the theorem must produce a canonical nontrivial holonomy/curvature there, or else break the category in another explicit way: a nonparallel source-forced metric, extra boundary topology/orbits, nonlinear support-sensitive geometry before scalarization, or a genuinely global finite--archimedean operation.

This is a stronger boundary than “nonlocal versus local.” Site dependence that is only parallel transport is not new arithmetic information; it is a coordinate choice. The useful question is whether the source supplies a gauge-invariant mixed-prime obstruction before positivity is formed.

**Boundary.** Nonzero curvature would only escape the no-go. It would still need to be canonical, distinguish the Riemann system from free generalized-prime clones, couple correctly to the real place, preserve exact Weil localization, and support an independent sign theorem.