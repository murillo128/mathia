# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where signed moment-null packets can erase finite-order response. The decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Convert start-averaged signed cancellation into the start control actually consumed by the target

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`.

VIS-187--VIS-191 establish a sharp absolute-resolution boundary for a fixed endpoint-zero taper. The complete absolute off-diagonal vanishes above `y/log y` and has an order-one floor below that scale because ordinary consecutive-prime gaps remain kernel-unresolved.

VIS-192 shows that this absolute barrier is **not** the signed barrier. Long Cesàro averaging in the interval start `T` gives an exact frequency-orthogonality identity for the signed off-diagonal variance. For every diverging `H<=y`,

`R_v(y,H) << 1/H`,

and in the strictly subcritical regime `H log y/y -> 0` the scale is sharp: `R_v(y,H) asymp 1/H`. Thus the signed quadratic off-diagonal has start-RMS size `H^(-1/2)` even while the absolute pair mass remains order one; at `H asymp y/log y` the start-averaged signed variance already tends to zero.

The live theorem inside this observable is therefore no longer simply “prove signed cancellation among unresolved short gaps.” It is to upgrade the long-start Cesàro statement to the **start regime actually available to the target**: a uniform-in-start estimate, control on deterministic finite start windows tied to `y`, or a theorem showing that the target legitimately consumes only an averaged/density-one start statement. If none is available, the observable must change.

## Keep absolute resolution, signed start-average cancellation and deterministic start control separate

VIS-191 says unresolved near-zero frequencies keep the absolute envelope macroscopic below `y/log y`; VIS-192 says exact phase orthogonality nevertheless makes their signed energy small after long start averaging as soon as `H->infinity`. These are compatible. The remaining resource is not extra taper smoothness but how arithmetic/start geometry converts an averaged signed statement into the deterministic observation required downstream.
