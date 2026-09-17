# MI-044 — Fixed positive scalarization cannot rescue stationary operator-valued transport

**Evidence level:** exact/classical-mechanism synthesis from [WP-341](../../findings/WP-341-cross-prime-stationary-hilbert-transport-contains-the-arithmetic-log-square.md) and [WP-342](../../findings/WP-342-positive-scalarization-does-not-let-stationary-operator-valued-transport-escape-the-arithmetic-log-square.md), complementary to the source/readout obstruction in MI-041.

WP-341 classifies stationary scalar/Hilbert transport on the prime-exponent group `Gamma=direct_sum_p Z e_p`: a translation-invariant CND cost can dominate the arithmetic displacement square `L(alpha)^2`, with `L(alpha)=sum_p alpha_p log p`, only when its Levy--Khinchin quadratic sector already contains that rank-one logarithmic direction.

WP-342 shows that replacing the scalar cost by a stationary operator-valued order-CND map does not evade this classification when the eventual Weil-facing observable is a fixed positive linear readout. Let `Psi:Gamma->A_sa` be such a map and let `phi:A->C` be positive. Then

`psi_phi(alpha)=phi(Psi(alpha))`

is itself a scalar CND function. If for sufficiently large arithmetic displacement

`psi_phi(alpha) >= a L(alpha)^2`,

WP-341 applies directly to `psi_phi`: its scalar Levy--Khinchin quadratic sector already satisfies `q_phi(alpha)>=aL(alpha)^2` everywhere. Equivalently, in a Hilbert realization `q_phi(alpha)=||D_phi alpha||^2`, the arithmetic logarithm factors as

`L(alpha)=<D_phi alpha,w>`

for a bounded covector `w`.

Thus **operator-valued stationary enrichment that is consumed only through a fixed positive scalarization cannot manufacture the missing arithmetic log-square**. A state, trace or density-matrix expectation may hide a rich operator-valued kernel upstream, but once the sign-relevant observable is the scalar CND shadow, the same quadratic-drift requirement reappears. The operator structure is useful only if some genuinely nonseparable operator-level positivity or mixed relation is exploited before that reduction.

This is distinct from MI-041. MI-041 concerns exact-law-preserving operator-valued noise and the visibility/faithfulness dichotomy of its fluctuation ideal. WP-342 instead applies to stationary operator-valued negative-type transport itself: even when the operator-valued object is legitimate and visible, a fixed positive linear scalar readout collapses the relevant tail-control question to the scalar stationary classification.

The surviving categories are therefore explicit. One may seek operator-level positivity before scalarization, a nonlinear or state-dependent scalar response whose sign is not inherited from scalar CND geometry, nonstationary/basepoint-dependent transport, a genuinely noncommutative source domain, or an independent arithmetic theorem that directly controls the required quadratic logarithmic displacement. Merely lifting the same stationary geometry into an operator algebra and applying a positive functional at the end is not a new sign mechanism.

**Boundary.** WP-342 does not rule out nonlinear spectral readouts such as determinants or extremal eigenvalues, state-dependent scalarization, non-positive functionals accompanied by a separate sign theorem, nonstationary geometry, or genuinely noncommutative domain structure. It also does not prove Weil positivity. The conclusion is specifically a no-escape theorem for stationary operator-valued CND transport whose destination is a fixed positive linear scalar shadow.