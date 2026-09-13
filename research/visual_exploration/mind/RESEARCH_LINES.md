# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where signed moment-null packets can erase finite-order response. The decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Cross the one-cancellation scale or upgrade typical-start control to uniform control

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`, `MI-011-finite-start-dephasing-is-priced-by-weighted-local-spacing`, `MI-012-cutoff-tuning-cannot-beat-the-four-form-pointwise-threshold`, `MI-013-autocorrelation-tapers-make-exact-difference-shells-noncancelling`.

VIS-203--VIS-207 identify positive autocorrelation shell energy with a two-sample close-pair probability and show that fixed and growing noncancelling windows dilute. VIS-208 now prices the **actual finite-start sinc kernel** rather than the unweighted shell mass. The cumulative bound

`S_(y,H)(A)/R^2 << H A^(2+4 alpha)(log y)^2/y^2`

holds uniformly all the way to `A<=kappa y` for fixed `kappa<1/2`, even when its right-hand side is not small. Abel/Stieltjes summation against `sinc^2` then gives, for `0<alpha<1/2`,

`W_kappa << H y^(2+4 alpha)(log y)^2/L^2`,

with the corresponding logarithmic endpoint correction at `alpha=0`. Under the stated window conditions this makes the entire noncancelling determinant band negligible in long-start Cesaro mean square and hence for a density-one set of starts.

The positive-shell frontier has therefore moved to two genuinely different questions. First, understand the **one-cancellation-and-above** shells where the bounded-multiplicity determinant model changes. Second, determine whether the start-averaged gain can be upgraded to uniform-in-`T0` control, or whether rare coherent starts carry a real obstruction. Reopening the subcritical noncancelling band without one of these new ingredients no longer addresses the surviving problem.

## Keep unweighted shell mass, sinc-weighted destination energy and uniform start control separate

VIS-207's dilution condition is sufficient for the raw cumulative shell mass itself to be small. VIS-208 shows the destination can be much cheaper: even when that raw bound grows, the sinc kernel suppresses wider shells strongly enough to make the long-start energy vanish. But an `L^2`-in-start conclusion still does not imply a uniform pointwise bound.

Future claims should therefore state which of three currencies they control: cumulative shell mass, sinc-weighted Cesaro energy, or worst-start amplitude. A failure of the strongest currency is not automatically a failure of the weaker destination.