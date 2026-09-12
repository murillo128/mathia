# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that one edge factor forces support-safe companions into a shrinking low-frequency channel where finite-CUE response can be cancelled by signed moment-null packets. The decisive evidence must come from the source-side lower-order term, not a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic polynomial/power selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Match coefficient leverage and close-frequency crowding at the linear-support boundary

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`.

VIS-161--VIS-178 calibrate collision complexity, weighted null shape, deterministic moment transfer, and prime-power effective dimension. VIS-179 then shows that quadratic statistics have a much larger collective null region than generic character separation suggests:

\[
\left|\frac1H\int_T^{T+H}S_y(t)^2\,dt-\frac18\right|
\ll\frac yH
\]

uniformly in interval start, arbitrary positive prime weights, and arbitrary prime subsets below `y`. Thus every `y=o(H)` support law is already variance-matched.

VIS-180 proves that the linear boundary is genuinely different for the broad arbitrary-subset class, but not in a source-sensitive way. Bounded prime gaps give sparse equal-weight two-prime supports with `y/H->1` and an `O(1)` slow-beat variance defect. The obstruction is deterministic close-frequency crowding.

VIS-181 now separates that sparse obstruction from the natural full-prime coefficient profile. Keeping the weighted Montgomery--Vaughan error gives

\[
\left|\frac1H\int_T^{T+H}S_y(t)^2dt-\frac18\right|
\le C\left(\frac{L_y}{HQ_y}+\frac{D_2(y)}H\right),
\]

where

\[
Q_y=\sum w_p^2,\qquad
D_2(y)=\frac{(\sum w_p)^2}{Q_y},\qquad
L_y=\sum p\,w_p^2.
\]

At `H\asymp y`, variance is therefore matched whenever `L_y/(yQ_y)->0` and `D_2(y)/y->0`. For the full prime set with `w_p=p^{-\alpha}`, both conditions hold for every fixed `\alpha\ge1/2`. At the critical profile `\alpha=1/2`,

\[
Q_y\sim\log\log y,
\qquad L_y\sim\frac y{\log y},
\qquad D_2(y)\sim\frac{4y}{(\log y)^2\log\log y},
\]

so the variance defect is only `O(1/(log y log log y))` uniformly in the interval start.

Thus merely moving the natural critical-line prime field to `y\asymp H` is now a matched quadratic null, not a source signal. The unresolved linear-support quadratic region begins with more diffuse full-prime profiles `\alpha<1/2` or other coefficient families for which the weighted leverage criterion does not vanish, and even there failure of the sufficient bound is not evidence of a defect. One must derive the actual crowding-aware off-diagonal asymptotic or use a matched deterministic control.

The stronger positive-power opportunities are now higher/growing complexity, genuinely discrete sampling, rare/shrinking or unbounded functionals, hybrid prime/zero information, or coefficient regimes outside the proven leverage null.

## Keep source corrections, clock mixing, weighted concentration, leverage, transfer horizon, functional order, and frequency crowding separate

Moment-null controls attack low-frequency source corrections; Gram selectors attack apparent phase mixing; weighted Haar controls calibrate concentration and shape. VIS-179 closes the strictly sublinear quadratic regime. VIS-180 shows that arbitrary sparse weights can retain linear-scale beats. VIS-181 shows that the natural full-prime `p^{-1/2}` profile suppresses that same channel strongly enough to restore the quadratic null at linear support.

A residual becomes arithmetic evidence only after it survives a matched control at the same weights, support law, sampling geometry, observation scale, functional complexity, target statistic, and local frequency-crowding geometry. **The coefficient leverage profile is part of the control.** Failure of a sufficient transfer bound is never positive source evidence by itself.