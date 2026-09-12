# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where signed moment-null packets can erase finite-order response. The decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Push uniform finite-start dephasing below the worst-case prime-ratio spacing scale

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`.

VIS-187--VIS-191 establish the sharp `y/log y` boundary for the **absolute** pair envelope. VIS-192 shows that signed cancellation is much better after long start averaging: distinct prime-ratio frequencies give exact Cesaro orthogonality and variance `asymp 1/H` in the diverging subcritical regime.

VIS-193 converts that infinite-start statement into a deterministic finite-window theorem. Distinct signed frequencies `+/-log(q/p)` are separated by at least `log(1+y^(-2))`, so Montgomery--Vaughan gives, uniformly in every start `T0`,

`|R_(v,L)(T0;y,H)-R_v(y,H)| <= 2 pi (y^2+1) R_v(y,H)/L`.

Hence every window of length `L>=C y^2` already has the same uniform `O(1/H)` mean-square cancellation, and `L/y^2->infinity` recovers the Cesaro variance asymptotically. The deterministic-start existence gap is therefore closed at a coarse universal horizon.

The live theorem is now **weighted frequency geometry**. The `y^2` scale comes from the single worst spacing among all prime-ratio frequencies and ignores the tapered coefficient mass. Improve it by controlling the energy carried by near-colliding ratios, proving a weighted large-sieve/nonharmonic-Fourier bound, or showing that the target consumes a start window whose available length already dominates the relevant weighted spacing scale. No further extension of the same worst-gap estimate will reveal the optimal horizon.

## Keep absolute resolution, Cesaro cancellation, uniform finite-window control and optimal start horizon separate

VIS-191 says unresolved near-zero frequencies keep the absolute envelope macroscopic below `y/log y`; VIS-192 says their signed Cesaro energy is small for every diverging `H`; VIS-193 says a deterministic start window of order `y^2` suffices uniformly. None of this proves pointwise-in-start cancellation or that `y^2` is necessary. The remaining resource is the coefficient-weighted geometry of frequency near-collisions and the actual start budget consumed downstream.
