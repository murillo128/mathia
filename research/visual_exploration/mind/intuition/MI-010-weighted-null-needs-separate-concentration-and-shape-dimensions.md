# MI-010 — Weighted prime-phase nulls have separate concentration, shape, support, leverage, complexity, and crowding-rate regimes

**Evidence level:** supported by weighted-Haar calculations and deterministic transfer/control theorems VIS-173--VIS-183.

For positive weights `w_p`, put

\[
W=\sum_pw_p,\qquad Q=\sum_pw_p^2,\qquad R=\sum_pw_p^4,
\]

with `D_2=W^2/Q` and `D_4=Q^2/R`. VIS-173 shows that these dimensions govern different aspects of the matched Haar null: `D_2` controls leading concentration/effective support while `D_4` controls standardized shape.

VIS-174--VIS-178 price deterministic continuous prime-log transfer. Fixed weighted moments transfer under explicit support/height conditions; square-summable weights have an infinite weighted-Haar limit, Lindeberg weights Gaussianize, and prime-power weights retain a positive polynomial-support wedge for every fixed moment order. Exceeding a sufficient wedge opens a proof gap, not source evidence.

VIS-179 shows that quadratic order is much better behaved than the generic character bound: every `y=o(H)` support law is variance-matched uniformly in interval start and arbitrary positive weights/subsets. VIS-180 gives the sharp warning at linear support for arbitrary sparse subsets: a bounded-gap two-prime support can leave an order-one slow beat.

VIS-181 shows that this sparse obstruction does not survive automatically in a diffuse full-prime profile. With

\[
L_y=\sum_{p\le y}p\,w_p^2,
\]

the linear-support error is bounded by `L_y/(H Q_y)+D_2(y)/H`. For the full prime set with `w_p=p^{-alpha}`, both terms vanish at `H asymp y` for every fixed `alpha>=1/2`.

VIS-182 then separates close-pair existence from **normalized gap-band mass**: every pre-fixed finite set of additive gaps contributes `o(1)` in the full prime prefix. VIS-183 strengthens this without importing a stronger sieve estimate. Diagonalizing those fixed-band limits gives a nondecreasing `D(y)->infinity`, below any prescribed diverging envelope if desired, for which the entire coefficient mass of `1<=q-p<=D(y)` is still `o(1)`. The time kernel cannot enlarge it.

Therefore a diverging crowding bandwidth is not itself a positive mechanism. The unresolved `alpha<1/2` region is a **rate problem**: one needs a uniform estimate for a specified band growth law or the natural kernel-weighted sum over all gaps, and must locate where it ceases to be negligible.

The reusable separation is now: weight concentration, limit-law shape, support scale, coefficient leverage, transfer horizon, functional order, local spacing, band breadth, and **band growth rate** are different currencies. A linear-support residual relative to independent Haar phases is meaningful only after the control preserves the same frequency geometry and coefficient profile.

**Boundary.** VIS-181--VIS-183 concern continuous second moments. VIS-183 is existential and nonquantitative; it does not show that every `D(y)->infinity` is negligible and does not settle any explicit polylogarithmic or polynomial gap window. Nothing here transfers automatically to discrete Gram sampling or higher moments.
