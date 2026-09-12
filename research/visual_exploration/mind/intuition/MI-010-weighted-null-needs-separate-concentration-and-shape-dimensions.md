# MI-010 — Weighted prime-phase nulls have separate concentration, shape, support-transfer, complexity, and crowding regimes

**Evidence level:** supported by weighted-Haar calculations and deterministic transfer/control theorems VIS-173--VIS-180.

For positive weights `w_j`, put

\[
W=\sum_jw_j,\qquad Q=\sum_jw_j^2,\qquad R=\sum_jw_j^4,
\]

and `D_2=W^2/Q`, `D_4=Q^2/R`. VIS-173 shows that these dimensions govern different aspects of the matched Haar null: `D_2` controls leading concentration/effective support while `D_4` controls whether standardized shape Gaussianizes.

VIS-174--VIS-178 then price deterministic continuous prime-log transfer. Fixed weighted moments transfer under explicit support/height conditions; square-summable weights have an infinite weighted-Haar limit, Lindeberg weights Gaussianize, and prime-power weights retain a positive polynomial-support wedge for every fixed moment order. Exceeding one such sufficient wedge opens a proof gap, not evidence of a source signal.

VIS-179 shows that quadratic order is much better behaved than the generic character bound. For the normalized additive prime-log cosine field,

\[
\left|\frac1H\int_T^{T+H}S_y(t)^2dt-\frac18\right|
\ll\frac yH
\]

uniformly in interval start and for arbitrary positive weights and prime subsets below `y`. Hence every strictly sublinear support law `y=o(H)` is variance-matched, including every polynomial `H^\delta` with `\delta<1`.

VIS-180 identifies the correct limitation at the linear boundary. Bounded prime gaps yield infinitely many fixed-gap pairs `q=p+d`. On the equal-weight two-prime support `{p,q}` with `H=p` and `y=q`, the beat frequency `\log(q/p)` satisfies `H\log(q/p)\to d`, and the deterministic variance tends to

\[
\frac18+\frac18\frac{\sin d}{d}\ne\frac18.
\]

Therefore the uniform arbitrary-subset quadratic null cannot extend through `y\asymp H` with an `o(1)` error. But the obstruction is itself a **matched representation effect**: slow deterministic beating of close prime-log frequencies. Crossing the sublinear/linear support boundary is a real control transition, not automatically a source-sensitive transition.

The reusable separation is now: **weight concentration, limit-law shape, transfer horizon, functional order, support scale, and local frequency crowding are different currencies**. A linear-support second-moment residual relative to independent Haar phases is meaningless unless the control preserves the same close-frequency geometry, or the natural coefficient profile is proved to suppress it.

For higher fixed order, the VIS-178 wedge remains only a sufficient transfer regime and stronger collective mean-value theorems may enlarge it. For Gram/discrete sampling, rare/shrinking events, unbounded functionals, hybrid prime/zero observables, and natural full-support linear/superlinear statistics, the appropriate matched control must be established separately.

**Boundary.** VIS-180 is existential inside the broad arbitrary-subset class. It does not show a persistent linear-support defect for the full prime set or for the natural zeta-facing weight profile, and it proves no zeta-versus-control separation or RH consequence.