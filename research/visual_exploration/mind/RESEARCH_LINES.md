# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where signed moment-null packets can erase finite-order response. The decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Compress the finite-start dephasing horizon or expose genuinely pointwise coherent starts

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`, `MI-011-finite-start-dephasing-is-priced-by-weighted-local-spacing`, `MI-012-cutoff-tuning-cannot-beat-the-four-form-pointwise-threshold`, `MI-013-autocorrelation-tapers-make-exact-difference-shells-noncancelling`, `MI-014-one-cancellation-shell-energy-is-an-anchor-gram-problem-and-thin-windows-diagonalize-it-exactly`.

VIS-203--VIS-209 reduce the only nonzero one-cancellation layer in the exact pair-difference expansion to a positive prime-anchor Gram kernel. VIS-211 proves, for the autocorrelation taper and every diverging strictly subcritical scale `H log y/y -> 0`,

`||Psi||_op=o(H^(-1/2))`

and hence `E_1=o(R_v^2)` in long-start mean square.

The exact VIS-204 boundary remains important: zero cancellations give the four-prime shells, one cancellation gives the prime/prime family now suppressed, and two cancellations give only `xi=0`, the removed diagonal. There is **no further nonzero higher-cancellation shell** to attack inside this representation.

VIS-212 now makes the start variable quantitative without taking an unspecified infinite Cesaro limit. Distinct symmetric prime-ratio frequencies are separated by at least `y^-2`, so Montgomery--Vaughan gives, uniformly in the interval location `T_0`,

`L^(-1) int_(T_0)^(T_0+L) |M_v(y;H,T)-1|^2 dT = R_v(y,H)[1+O(y^2/L)]`.

Thus every sliding window with `L>=c y^2` already has mean square `O(R_v)` and therefore density-one cancellation when `H->infinity`. This is a deterministic finite-start baseline, not a pointwise theorem and not a claim that the quadratic horizon is optimal.

The live frontier therefore has two distinct parts. First, compress the `y^2` worst-spacing baseline by exploiting the **coefficient-weighted** geometry of small determinants `|qr-ps|` rather than global frequency separation; the earlier weighted-local-spacing/sieve route shows that such compression is possible in substantial subcritical corridors. Second, decide genuinely pointwise worst-start behavior or construct rare coherent starts that survive all averaged estimates. The critical scale `H asymp y/log y` remains separate.

A future higher-moment or higher-degree observable may create a new cancellation hierarchy, but that is a different mathematical object. It requires a fresh exact representation and shell classification rather than reusing the pair-difference terminology.

## Keep representation closure, averaging horizon and pointwise coherence separate

VIS-211 closes the one-cancellation Gram frontier only in the stated strictly subcritical averaged regime. VIS-212 replaces infinite Cesaro averaging by a uniform quadratic finite window, but still does not prove pointwise-in-start cancellation. Conversely, the absence of another nonzero pair-difference cancellation class is exact. Any improvement below the quadratic start window must come from weighted frequency-collision structure, while any worst-start theorem must control coherent phases rather than merely shorten an averaging interval.
