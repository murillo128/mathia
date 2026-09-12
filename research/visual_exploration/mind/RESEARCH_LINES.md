# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that one edge factor forces support-safe companions into a shrinking low-frequency channel where finite-CUE response can be cancelled by signed moment-null packets. The decisive evidence must come from the source-side lower-order term, not a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic polynomial/power selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Resolve the growing-gap aggregate at the full-prime linear-support boundary

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`.

VIS-161--VIS-178 calibrate collision complexity, weighted null shape, deterministic moment transfer, and prime-power effective dimension. VIS-179 then shows that quadratic statistics have a much larger collective null region than generic character separation suggests:

\[
\left|\frac1H\int_T^{T+H}S_y(t)^2\,dt-\frac18\right|
\ll\frac yH
\]

uniformly in interval start, arbitrary positive prime weights, and arbitrary prime subsets below `y`. Thus every `y=o(H)` support law is already variance-matched.

VIS-180 proves that the linear boundary is genuinely different for the broad arbitrary-subset class, but not in a source-sensitive way. Bounded prime gaps give sparse equal-weight two-prime supports with `y/H->1` and an `O(1)` slow-beat variance defect. The obstruction is deterministic close-frequency crowding.

VIS-181 separates that sparse obstruction from the natural full-prime coefficient profile. Keeping the weighted Montgomery--Vaughan error gives

\[
\left|\frac1H\int_T^{T+H}S_y(t)^2dt-\frac18\right|
\le C\left(\frac{L_y}{HQ_y}+\frac{D_2(y)}H\right),
\]

where `Q_y=sum w_p^2`, `D_2(y)=(sum w_p)^2/Q_y`, and `L_y=sum p w_p^2`. At `H\asymp y`, variance is matched whenever `L_y/(yQ_y)->0` and `D_2(y)/y->0`. For the full prime set with `w_p=p^{-\alpha}`, both conditions hold for every fixed `\alpha>=1/2`; in particular the critical `p^{-1/2}` profile is already a linear-support quadratic null.

VIS-182 now removes the simplest candidate explanation for the unresolved full-prime region `0<=alpha<1/2`. For every **fixed finite** set of nonzero additive gaps `Delta`, the normalized coefficient mass of prime pairs in those gap classes obeys

\[
C_\Delta(y)\to0,
\]

with `C_\Delta(y)=O(1/\log y)` for `alpha<1/2` and `O(1/\log\log y)` at `alpha=1/2`. The input is only the classical fixed-shift Brun--Selberg upper-bound sieve plus prime-counting asymptotics. Thus the sparse two-prime bounded-gap mechanism of VIS-180 is diluted when the denominator is the whole prime prefix: **no pre-fixed finite bounded-gap band can carry an order-one normalized off-diagonal variance defect**.

The open linear-support quadratic question is therefore a **growing-band problem**. If the full-prime `alpha<1/2` field has a real defect, it must use gap scales `d=d(y)` tending to infinity, an increasing family `1<=d<=D(y)`, or another distributed off-diagonal organization. The fixed-gap sieve bound is not uniform enough to sum over such a band, so VIS-182 does not close the region. The decisive next calculation is to combine coefficient mass with time-kernel coherence over a growing near-diagonal window, rather than infer a defect from failure of the coarse leverage upper bound.

The stronger positive-power opportunities remain higher/growing complexity, genuinely discrete sampling, rare/shrinking or unbounded functionals, hybrid prime/zero information, or coefficient regimes outside the proven quadratic nulls.

## Keep source corrections, clock mixing, weighted concentration, leverage, transfer horizon, functional order, and frequency-crowding bandwidth separate

Moment-null controls attack low-frequency source corrections; Gram selectors attack apparent phase mixing; weighted Haar controls calibrate concentration and shape. VIS-179 closes the strictly sublinear quadratic regime. VIS-180 shows that arbitrary sparse weights can retain linear-scale beats. VIS-181 shows that the natural full-prime `p^{-1/2}` profile suppresses that same channel strongly enough to restore the quadratic null at linear support. VIS-182 shows that even below the leverage threshold, any **fixed finite** bounded-gap family is too dilute in the full prime prefix to explain an order-one defect.

A residual becomes arithmetic evidence only after it survives a matched control at the same weights, support law, sampling geometry, observation scale, functional complexity, target statistic, and local frequency-crowding geometry. The relevant crowding variable now includes the **breadth of the near-diagonal gap band**, not just the existence of close prime pairs. Failure of a sufficient transfer bound is never positive source evidence by itself.