# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Leave normalized magnetic spectra and test cycle packing or the exact torus constraint in the strictly subcritical regime

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`, `MI-011-finite-start-dephasing-is-priced-by-weighted-local-spacing`, `MI-012-cutoff-tuning-cannot-beat-the-four-form-pointwise-threshold`, `MI-013-autocorrelation-tapers-make-exact-difference-shells-noncancelling`, `MI-014-one-cancellation-shell-energy-is-an-anchor-gram-problem-and-thin-windows-diagonalize-it-exactly`, `MI-015-prime-phase-worst-starts-are-frustrated-torus-optimization`.

VIS-213 identifies the fixed-`(y,H)` worst start with the full unit-modulus quadratic optimum. VIS-214 identifies cycle holonomy as the exact gauge-invariant envelope obstruction, and VIS-215 accumulates it through fractional weighted cycle packing. VIS-216 adds the normalized magnetic-Laplacian relaxation.

VIS-217 shows that this spectral branch has a phase-independent dimension floor. On a connected component with `n` vertices and effective edge count `N_eff`,

`U_spec/sqrt(R(A)) >= sqrt(2 N_eff/(n-1))`.

VIS-218 now computes the actual prime-graph scale throughout `H log y/y -> 0`:

`W_1 asymp y/(H log y)`, `W_2 asymp 1/H`, and `N_eff asymp y^2/(H(log y)^2)`.

Since `n<=pi(y)`,

`N_eff/n >> y/(H log y) -> infinity`,

and therefore the normalized magnetic certificate exceeds the Haar-RMS scale by a diverging factor. This closes attempts to rescue the same relaxation through sharper magnetic eigenvalue estimates or clever edge phases in the strictly subcritical regime.

The remaining static questions are whether the stronger fractional cycle-packing certificate of VIS-215 can accumulate enough frustration on the actual prime graph, or whether the exact fixed-modulus torus constraint gives suppression that the variable-amplitude spectral relaxation necessarily loses. The constant critical transition `H asymp y/log y` is a separate scale. One-parameter access time to near-extremal torus regions remains separate from all static bounds.

## Keep representation closure, relaxation strength, exact torus optimization and access time separate

Cycle holonomy decides exact envelope attainability; cycle packing and magnetic spectra only certify lower bounds on frustration. VIS-218 is a decisive limitation of the normalized spectral relaxation, not of the exact torus problem. A weak or dimension-floor-limited magnetic certificate cannot be promoted into a lower bound on the true torus optimum without a separate theorem.