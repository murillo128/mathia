# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Determine the full correlation-SDP scale on the canonical prime matrices

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`, `MI-011-finite-start-dephasing-is-priced-by-weighted-local-spacing`, `MI-012-cutoff-tuning-cannot-beat-the-four-form-pointwise-threshold`, `MI-013-autocorrelation-tapers-make-exact-difference-shells-noncancelling`, `MI-014-one-cancellation-shell-energy-is-an-anchor-gram-problem-and-thin-windows-diagonalize-it-exactly`, `MI-015-prime-phase-worst-starts-are-frustrated-torus-optimization`.

VIS-213 identifies the fixed-`(y,H)` worst start with the full unit-modulus quadratic optimum. VIS-214 identifies cycle holonomy as the exact gauge-invariant envelope obstruction, VIS-215 accumulates it through fractional weighted simple-cycle packing, and VIS-216 adds the normalized magnetic-Laplacian relaxation.

VIS-217--VIS-218 close the normalized spectral branch throughout `H log y/y->0`: the actual prime graph has `N_eff/n->infinity`, forcing the magnetic certificate above Haar-RMS scale by a diverging factor regardless of edge phases. VIS-219 prices the stronger cycle-packing certificate, and VIS-220 proves a phase-independent ceiling: for support-graph girth `g`, `P_+,P_- <= (2/g^2)B`, so every simple graph leaves at least `7B/9` residual. The simple-cycle LP is therefore exhausted regardless of how many cycles are enumerated.

VIS-221 opens the full correlation SDP

`U_abs(A)=max_(X>=0,diag(X)=1)|Tr(A X)|`.

It retains all pair correlations and contains the old magnetic certificate as a restricted dual ansatz. A stationary torus point is a certified global maximizer with rank-one SDP tightness when its full stress matrix `Diag(conj(z_i)(Az)_i)-A` is positive semidefinite.

VIS-222 then changes the role of the SDP completely. The complex symmetric Grothendieck inequality gives, for every finite Hermitian `A`,

`M_abs(A) <= U_abs(A) <= K_gamma^C M_abs(A)`, `K_gamma^C<=8/pi-1`.

Thus the SDP is a universal constant-factor surrogate for the exact torus objective, not merely an upper certificate of unknown multiplicative quality. For the canonical prime matrices, `M_abs` is exactly the fixed-parameter worst-start supremum by VIS-213. Consequently `U_abs/sqrt(R_v)` is bounded iff the exact torus/worst-start ratio is bounded, and it diverges iff the exact ratio diverges.

The live static question is therefore the prime-specific asymptotic scale of `U_abs(A_(y,H))/sqrt(R_v(y,H))`. An RMS-scale SDP value proves the exact worst-start amplitude is RMS-scale. A divergent SDP ratio proves the exact worst-start ratio diverges as well, within the universal Grothendieck factor. Rank-one stress remains useful only for recovering the exact finite optimizer/value rather than for deciding asymptotic objective scale.

## Keep representation closure, relaxation strength, optimizer recovery and access time separate

Cycle holonomy decides exact envelope attainability; magnetic spectra, simple-cycle packing and the correlation SDP are progressively stronger static objects. VIS-218 and VIS-220 prove ceilings only for the first two certificate families. VIS-221 shows the full SDP retains interactions they discard, and VIS-222 proves that its **optimal value** is nevertheless constant-factor equivalent to the exact unit-modulus optimum for every Hermitian matrix.

High SDP rank therefore has a narrower meaning than before: it can block exact phase recovery or rank-one certification, but it cannot explain away a parametrically large SDP objective. Conversely, an RMS-scale SDP upper bound already transfers to the exact torus objective without rank-one tightness. One-parameter prime-log access time remains a separate problem and matters only when converting static torus information into quantitative finite-time recurrence.