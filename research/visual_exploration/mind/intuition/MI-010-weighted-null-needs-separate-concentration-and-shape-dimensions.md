# MI-010 — Weighted prime-phase nulls have separate concentration, shape, support, leverage, complexity, and crowding-band regimes

**Evidence level:** supported by weighted-Haar calculations and deterministic transfer/control theorems VIS-173--VIS-182.

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

At `H\asymp y`, the deterministic variance is Haar-matched whenever `L_y/(yQ_y)->0` and `D_2(y)/y->0`. For the full prime set with `w_p=p^{-\alpha}`, both conditions hold for every fixed `\alpha>=1/2`. At the critical-line amplitude `\alpha=1/2`, the variance defect is `O(1/(log y log log y))`. The sparse bounded-gap obstruction therefore does not survive the natural diffuse `p^{-1/2}` profile at quadratic order.

VIS-182 sharpens the unresolved `alpha<1/2` side by separating **existence of close pairs** from **normalized mass of a gap band**. For any fixed finite set `Delta` of nonzero integer shifts, the full-prime coefficient mass carried by pairs `q-p in Delta`, normalized by `Q_y`, satisfies

\[
C_\Delta(y)=O_{\alpha,\Delta}(1/\log y)\to0
\qquad(0\le\alpha<1/2),
\]

and at `alpha=1/2`,

\[
C_\Delta(y)=O_\Delta(1/\log\log y)\to0.
\]

This uses only the classical fixed-shift prime-pair upper-bound sieve and prime-counting asymptotics. Since the time-averaging kernel has modulus at most one, the entire off-diagonal contribution from any pre-fixed finite bounded-gap band is already `o(1)` in absolute coefficient mass. **A recurrent close gap can be an order-one obstruction for a sparse selected support and simultaneously disappear inside a diffuse full-prefix normalization.**

The unresolved full-prime region `alpha<1/2` must therefore involve a crowding scale that grows with `y`: expanding gap bands, increasingly many gap classes, or another distributed off-diagonal organization. VIS-182 gives no uniformity in `Delta`, so one cannot sum its fixed-gap bound over `D(y)->infinity`. The next boundary is to price the joint growth of gap-band breadth, coefficient mass, and time-kernel coherence.

The reusable separation is now: **weight concentration, limit-law shape, support scale, coefficient leverage, transfer horizon, functional order, local frequency spacing, and crowding-band breadth are different currencies**. A linear-support residual relative to independent Haar phases is meaningless unless the control preserves the same frequency geometry and coefficient profile. Conversely, failure of the sufficient leverage bound below `alpha=1/2` is not a positive residual; the actual growing-band off-diagonal asymptotic still has to be derived.

**Boundary.** VIS-181--VIS-182 concern continuous second moments. VIS-182 controls only fixed finite gap sets and supplies no uniform estimate for a growing band. Neither result proves a full weak law at linear support, settles `alpha<1/2`, or applies automatically to discrete Gram sampling. The coefficient thresholds are null/control boundaries, not evidence that the critical line is dynamically selected or that RH follows.