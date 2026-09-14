# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Test the full correlation SDP before returning to the exact fixed-modulus torus problem

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`, `MI-011-finite-start-dephasing-is-priced-by-weighted-local-spacing`, `MI-012-cutoff-tuning-cannot-beat-the-four-form-pointwise-threshold`, `MI-013-autocorrelation-tapers-make-exact-difference-shells-noncancelling`, `MI-014-one-cancellation-shell-energy-is-an-anchor-gram-problem-and-thin-windows-diagonalize-it-exactly`, `MI-015-prime-phase-worst-starts-are-frustrated-torus-optimization`.

VIS-213 identifies the fixed-`(y,H)` worst start with the full unit-modulus quadratic optimum. VIS-214 identifies cycle holonomy as the exact gauge-invariant envelope obstruction, VIS-215 accumulates it through fractional weighted simple-cycle packing, and VIS-216 adds the normalized magnetic-Laplacian relaxation.

VIS-217--VIS-218 close the normalized spectral branch throughout `H log y/y->0`: the actual prime graph has `N_eff/n->infinity`, forcing the magnetic certificate above Haar-RMS scale by a diverging factor regardless of edge phases. VIS-219 prices the stronger cycle-packing certificate, and VIS-220 proves a phase-independent ceiling: for support-graph girth `g`, `P_+,P_- <= (2/g^2)B`, so every simple graph leaves at least `7B/9` residual. The simple-cycle LP is therefore exhausted regardless of how many cycles are enumerated.

VIS-221 opens a strictly stronger certificate rather than returning immediately to the nonconvex torus problem. For the Hermitian coefficient matrix `A`, the correlation SDP

`U_+(A)=max Tr(AX)` subject to `X>=0`, `X_ii=1`

and its analogue for `-A` upper-bound both signed torus optima. The old magnetic certificate is exactly a restricted feasible dual ansatz inside this SDP, so VIS-218 does not close the larger class. A stationary torus point `z` is certified as a global maximizer, with rank-one SDP tightness, whenever its stress matrix

`S_z = Diag(conj(z_i)(Az)_i) - A`

is positive semidefinite.

The destination calibration remains severe. With `B=2 sum_e w_e`, `R=2 sum_e w_e^2` and `N_eff=(sum_e w_e)^2/(sum_e w_e^2)`, the signed SDP deficit must satisfy

`U_abs/sqrt(R) = sqrt(2N_eff) [1-min(Delta_+^SDP,Delta_-^SDP)/B]`.

Thus Haar-RMS certification requires `min(Delta_+^SDP,Delta_-^SDP)=B-O(sqrt(R))`; a constant-fraction envelope improvement is still useless when `N_eff` diverges. The live static test is now whether the **canonical prime matrices** achieve this scale in the full correlation SDP. If the SDP is bounded at RMS scale, the desired static upper bound follows. If it is rank-one with PSD stress, the exact finite torus optimum is certified. If it diverges only through high-rank relaxation, the SDP certificate has failed but the exact torus optimum remains open.

## Keep representation closure, relaxation strength, rank-one exactness and access time separate

Cycle holonomy decides exact envelope attainability; magnetic spectra, simple-cycle packing and the correlation SDP are progressively stronger upper-bound mechanisms. VIS-218 and VIS-220 prove universal ceilings only for the first two relaxations. VIS-221 proves that the correlation SDP retains interactions discarded by those certificates, but does not prove asymptotic tightness on the prime matrices.

A large high-rank SDP value is not a lower bound on the exact torus objective. Conversely, an RMS-scale SDP upper bound is already sufficient even without rank-one tightness. One-parameter orbit access time remains a separate problem and matters only after a useful static pointwise bound or exact torus characterization exists.