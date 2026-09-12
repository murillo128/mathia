# MI-010 — Weighted prime-phase nulls have separate concentration, shape, support, leverage, complexity, and crowding regimes

**Evidence level:** supported by weighted-Haar calculations and deterministic transfer/control theorems VIS-173--VIS-181.

For positive weights `w_p`, put

\[
W=\sum_pw_p,\qquad Q=\sum_pw_p^2,\qquad R=\sum_pw_p^4,
\]

with `D_2=W^2/Q` and `D_4=Q^2/R`. VIS-173 shows that these dimensions govern different aspects of the matched Haar null: `D_2` controls leading concentration/effective support while `D_4` controls whether standardized shape Gaussianizes.

VIS-174--VIS-178 then price deterministic continuous prime-log transfer. Fixed weighted moments transfer under explicit support/height conditions; square-summable weights have an infinite weighted-Haar limit, Lindeberg weights Gaussianize, and prime-power weights retain a positive polynomial-support wedge for every fixed moment order. Exceeding one such sufficient wedge opens a proof gap, not evidence of a source signal.

VIS-179 shows that quadratic order is much better behaved than the generic character bound. For the normalized additive prime-log cosine field,

\[
\left|\frac1H\int_T^{T+H}S_y(t)^2dt-\frac18\right|
\ll\frac yH
\]

uniformly in interval start and for arbitrary positive weights and prime subsets below `y`. Hence every strictly sublinear support law `y=o(H)` is variance-matched.

VIS-180 identifies a real limitation for that **uniform arbitrary-subset** statement at the linear boundary. Bounded prime gaps yield equal-weight two-prime supports with `H\asymp y` whose slow beat leaves an `O(1)` deterministic variance defect. Crossing from sublinear to linear support can therefore expose close-frequency crowding without exposing arithmetic source information.

VIS-181 shows that support scale alone is still too coarse. Keep the coefficient-sensitive Montgomery--Vaughan quantity

\[
L_y=\sum_{p\le y}p\,w_p^2.
\]

Then

\[
\left|\frac1H\int_T^{T+H}S_y(t)^2dt-\frac18\right|
\le C\left(\frac{L_y}{HQ_y}+\frac{D_2(y)}H\right).
\]

At `H\asymp y`, the deterministic variance is Haar-matched whenever

\[
\frac{L_y}{yQ_y}\to0,
\qquad
\frac{D_2(y)}y\to0.
\]

For the full prime set with `w_p=p^{-\alpha}`, both conditions hold for every fixed `\alpha\ge1/2`. At the critical-line amplitude `\alpha=1/2`,

\[
Q_y\sim\log\log y,
\quad L_y\sim y/\log y,
\quad D_2(y)\sim\frac{4y}{(\log y)^2\log\log y},
\]

so the variance defect is `O(1/(log y log log y))`. The sparse bounded-gap obstruction therefore does **not** survive the natural diffuse `p^{-1/2}` profile at quadratic order.

The reusable separation is now: **weight concentration, limit-law shape, support scale, coefficient leverage, transfer horizon, functional order, and local frequency crowding are different currencies**. A linear-support residual relative to independent Haar phases is meaningless unless the control preserves the same frequency geometry and coefficient profile. Conversely, a failure of the sufficient leverage bound below `\alpha=1/2` is not a positive residual; the actual off-diagonal asymptotic still has to be derived.

For higher fixed order, the VIS-178 wedge remains only a sufficient transfer regime and stronger collective mean-value theorems may enlarge it. For Gram/discrete sampling, rare/shrinking events, unbounded functionals, hybrid prime/zero observables, and diffuse profiles outside the leverage criterion, the appropriate matched control must be established separately.

**Boundary.** VIS-181 is a continuous second-moment theorem. It does not prove a full weak law at linear support, does not settle `\alpha<1/2`, and does not apply automatically to discrete Gram sampling. The threshold `\alpha=1/2` is a threshold of this coefficient-sensitive quadratic null, not evidence that the critical line is dynamically selected or that RH follows.