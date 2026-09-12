# MI-010 — Weighted prime-phase nulls have separate concentration, shape, support-transfer, and complexity regimes

**Evidence level:** supported by weighted-Haar calculations and deterministic transfer theorems VIS-173--VIS-179.

For positive weights `w_j`, put

\[
W=\sum_jw_j,\qquad Q=\sum_jw_j^2,\qquad R=\sum_jw_j^4,
\]

and

\[
D_2=\frac{W^2}{Q},\qquad D_4=\frac{Q^2}{R}.
\]

VIS-173 shows that `D_2` and `D_4` control different parts of the matched Haar null. `D_2` governs leading concentration/effective support, while `D_4` governs whether standardized shape Gaussianizes. The bulk can concentrate while heavy low-prime coordinates keep a non-Gaussian law.

VIS-174 transfers fixed moments of the matched Haar law to deterministic continuous prime-log averaging. VIS-177 sharpens its character geometry: after balancing positive and negative multiplicities, every nonzero character in the `k`th moment has

\[
|\lambda|\ge\frac1{2y^{\lfloor k/2\rfloor}},
\]

so the elementary deterministic/Haar discrepancy is controlled at scale

\[
\frac{y^{\lfloor k/2\rfloor}D_2(y)^{k/2}}H.
\]

VIS-175 and VIS-176 turn the weight geometry into full weak-law regimes. In the square-summable phase the limit is the infinite weighted Haar convolution under its transfer gate. In the Lindeberg phase, vanishing maximal normalized weight plus transfer of every fixed moment gives `N(0,1/8)`. For prime-power weights, VIS-177 already extends that Gaussian conclusion to every subpolynomial cutoff `y(H)=H^{o(1)}`.

VIS-178 shows that a fixed positive-power support law is not automatically outside the null either. For `w_p=p^{-\alpha}`, `0\le\alpha<1/2`, one has `D_2(y)\asymp y/\log y` with the explicit constant recorded there, while at `\alpha=1/2`, `D_2(y)\asymp y/((\log y)^2\log\log y)`. If `e_k=\lfloor k/2\rfloor+k/2`, the `k`th deterministic moment still matches Haar for `y=H^\delta` throughout the sufficient wedge

\[
\delta\le1/e_k.
\]

VIS-179 shows that **quadratic order is much better behaved than this generic character bound suggests**. For

\[
S_y(t)=Q_y^{-1/2}\sum_{p\in P_y}w_p\left(\sin^2\frac{t\log p}{2}-\frac12\right),
\]

write `A_y(t)=\sum_{p\in P_y}w_pp^{it}`. The identity for `S_y(t)^2` reduces its variance to the ordinary Dirichlet-polynomial mean square plus a nonconjugated square term. Montgomery--Vaughan then gives, uniformly in the interval start and for arbitrary positive weights and prime subsets below `y`,

\[
\left|\frac1H\int_T^{T+H}S_y(t)^2\,dt-\frac18\right|
\ll \frac yH.
\]

Therefore **every strictly sublinear support law `y=o(H)` is variance-matched**, including every polynomial `y=H^\delta` with `\delta<1`. The region `1/2<\delta<1`, which lay beyond the generic `k=2` VIS-178 wedge, is not a new quadratic source-sensitive regime.

This stronger conclusion is deliberately only quadratic. It does not upgrade higher fixed moments, establish a full weak law at any fixed positive `\delta`, control growing moment order, or cover Gram/discrete sampling, shrinking/rare events, unbounded functionals, hybrid prime/zero observables, or the transition `y\asymp H`. The null boundary is indexed by the **actual functional complexity**: variance has a near-linear collective mean-value theorem, while higher statistics retain their own transfer costs unless a stronger collective theorem is proved.

A source-sensitive statistic must therefore leave the relevant matched class in a mathematically declared way. At quadratic order under continuous averaging, `y=o(H)` is closed. For higher fixed order, exceeding the VIS-178 sufficient wedge only opens a proof gap, not evidence of separation. Genuine opportunities require higher or growing complexity, stronger functional classes, different sampling, hybrid source variables, rare/shrinking events, or behavior at/above the linear support scale with a separately justified control.

**Boundary.** VIS-179 controls only the second moment and its `O(y/H)` estimate is a sufficient matching theorem, not a sharp transition statement at `y\asymp H`. None of VIS-173--VIS-179 proves a zeta-versus-control separation or an RH consequence.