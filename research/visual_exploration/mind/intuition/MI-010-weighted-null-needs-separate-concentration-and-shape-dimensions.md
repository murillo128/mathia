# MI-010 — Weighted prime-phase nulls have separate concentration, shape, support, leverage, complexity, and crowding-rate regimes

**Evidence level:** supported by weighted-Haar calculations and deterministic transfer/control theorems VIS-173--VIS-184.

For positive weights `w_p`, put

\[
W=\sum_pw_p,\qquad Q=\sum_pw_p^2,\qquad R=\sum_pw_p^4,
\]

with `D_2=W^2/Q` and `D_4=Q^2/R`. VIS-173 shows that these dimensions govern different aspects of the matched Haar null: `D_2` controls leading concentration/effective support while `D_4` controls standardized shape.

VIS-174--VIS-178 price deterministic continuous prime-log transfer. Fixed weighted moments transfer under explicit support/height conditions; square-summable weights have an infinite weighted-Haar limit, Lindeberg weights Gaussianize, and prime-power weights retain a positive polynomial-support wedge for every fixed moment order. Exceeding a sufficient wedge opens a proof gap, not source evidence.

VIS-179 shows that quadratic order is much better behaved than the generic character bound: every `y=o(H)` support law is variance-matched uniformly in interval start and arbitrary positive weights/subsets. VIS-180 gives the sharp warning at linear support for arbitrary sparse subsets: a bounded-gap two-prime support can leave an order-one slow beat.

VIS-181 shows that this sparse obstruction does not survive automatically in a diffuse full-prime profile. VIS-182 then separates close-pair existence from normalized gap-band mass by killing every fixed finite additive-gap family. VIS-183 strengthens this qualitatively: some diverging gap windows, even below any prescribed diverging envelope, remain null.

VIS-184 supplies the missing explicit first rate. For the full prime prefix with `w_p=p^{-alpha}`, fixed `0<=alpha<1/2`, the normalized coefficient mass `C_D(y)` of all pairs with gap at most `D(y)` obeys

\[
C_D(y)
\ll_\alpha
\frac{D(y)}{\log y}
+
D(y)y^{-(1-2\alpha)/2}.
\]

Consequently every predeclared `D(y)=o(log y)` band is negligible. Because the interval kernel has modulus at most one, no phase argument is even needed: coefficient-mass dilution alone kills the whole sublogarithmic near-diagonal channel uniformly at linear support.

This turns “crowding rate” into a quantitative currency. A bounded-gap obstruction on a sparse support and a diverging-gap band on the full prime prefix live in different regimes. For the diffuse full-prime profile, a candidate quadratic mechanism must reach at least logarithmic gap breadth before the present null estimate ceases to force disappearance.

The logarithmic scale is only the **first unresolved rate**, not evidence of survival. At `D(y) asymp log y` the current upper bound becomes order one, but stronger cancellation, a sharper sieve estimate, or the actual oscillatory kernel may still force a null. The live object is therefore the kernel-weighted distributed off-diagonal aggregate, with the `log y` band as the first explicit local frontier.

The reusable separation is: weight concentration, limit-law shape, support scale, coefficient leverage, transfer horizon, functional order, local spacing, band breadth, and quantitative band-growth rate are different currencies. A residual is meaningful only after the matched control preserves the same frequency geometry and coefficient profile.

**Boundary.** VIS-181--VIS-184 concern continuous second moments. VIS-184 uses full-prime power weights with fixed `alpha<1/2` and proves only a one-sided null for sublogarithmic gaps. It does not establish survival at logarithmic breadth and transfers neither to discrete Gram sampling nor to higher moments.
