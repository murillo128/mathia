# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where signed moment-null packets can erase finite-order response. The decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Estimate the coefficient-weighted prime-ratio collision horizon

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`, `MI-011-finite-start-dephasing-is-priced-by-weighted-local-spacing`.

VIS-187--VIS-191 establish the sharp `y/log y` boundary for the absolute pair envelope. VIS-192 shows that signed cancellation is much better after long start averaging: distinct prime-ratio frequencies give exact Cesaro orthogonality and variance `asymp 1/H` in the diverging subcritical regime. VIS-193 turns that into a uniform deterministic finite-start theorem at the coarse worst-gap horizon `L=O(y^2)`.

VIS-194 replaces the global minimum spacing by the exact weighted Hilbert resource

`D_v(y,H) = [sum_lambda |c_lambda|^2/delta_lambda] / [sum_lambda |c_lambda|^2]`,

where `delta_lambda` is the individual nearest-neighbor spacing of each signed prime-ratio frequency. Uniformly in the start `T0`, the relative finite-window mean-square error is at most `3 pi D_v/L`. Thus `L>=C D_v` already gives the `O(1/H)` signed cancellation of VIS-192, and `L/D_v->infinity` recovers its Cesaro variance uniformly. The old `y^2` horizon is only the universal fallback `D_v<=y^2+1`.

The live theorem is now genuinely arithmetic: prove `D_v=o(y^2)` in a useful `(y,H)` regime by controlling the coefficient energy carried by near-colliding prime ratios, obtain a sharper weighted large-sieve/multiplicative-energy bound, or show that the downstream target supplies a deterministic start window that already dominates `D_v`. Reusing the single worst spacing cannot improve the horizon.

## Keep absolute resolution, Cesaro cancellation, worst-gap finite-window control and weighted effective horizon separate

VIS-191, VIS-192, VIS-193 and VIS-194 answer different questions. `D_v` is a sufficient weighted dephasing scale, not a proved necessary one; its improvement over `y^2` remains an arithmetic problem. A rare tiny gap matters only in proportion to the coefficient energy it carries.