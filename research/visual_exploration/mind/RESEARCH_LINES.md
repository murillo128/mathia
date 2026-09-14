# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Determine the real-elliptope scale on the centered symmetric-taper prime matrices

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`, `MI-011-finite-start-dephasing-is-priced-by-weighted-local-spacing`, `MI-012-cutoff-tuning-cannot-beat-the-four-form-pointwise-threshold`, `MI-013-autocorrelation-tapers-make-exact-difference-shells-noncancelling`, `MI-014-one-cancellation-shell-energy-is-an-anchor-gram-problem-and-thin-windows-diagonalize-it-exactly`, `MI-015-prime-phase-worst-starts-are-frustrated-torus-optimization`.

VIS-213 identifies the fixed-`(y,H)` worst start with the full unit-modulus quadratic optimum. VIS-214 identifies cycle holonomy as the exact gauge-invariant envelope obstruction, VIS-215 accumulates it through fractional weighted simple-cycle packing, and VIS-216 adds the normalized magnetic-Laplacian relaxation.

VIS-217--VIS-220 close the normalized magnetic and simple-cycle certificate branches: both remain on the coefficient-envelope scale in the strictly subcritical prime regime. VIS-221 opens the full correlation SDP, and VIS-222 makes its objective scale decisive through the complex symmetric Grothendieck inequality:

`M_abs(A) <= U_abs(A) <= K_gamma^C M_abs(A)`, `K_gamma^C<=8/pi-1`.

Thus the SDP is a universal constant-factor surrogate for the exact torus objective, not merely an upper certificate of unknown multiplicative quality.

VIS-223 then removes a representation degree of freedom for the canonical symmetric tapers. Writing the taper around its midpoint gives

`kappa_v(u)=exp(iu/2)[C_v(u)+iS_v(u)]`.

The factor `exp(iu/2)` is pure vertex gauge. If `v(x)=v(1-x)`, then `S_v=0`, so after diagonal switching the canonical Hermitian matrix becomes a **real symmetric signed ratio-shell matrix** `B`. For every real symmetric objective, taking the real part of a complex correlation matrix preserves positive semidefiniteness and the diagonal, hence

`U_abs(A)=U_abs(B)=max_(X in E_n^R)|Tr(BX)|`.

The SDP therefore lives exactly in the ordinary real elliptope for midpoint-symmetric tapers. The torus variables remain continuous `U(1)` phases; only the coefficient matrix and SDP relaxation become real. For the quadratic taper the remaining edge signs are explicit shells determined by the zeros of `12[2 sin(u/2)-u cos(u/2)]/u^3`, and cycle holonomy reduces from general `U(1)` phase to `+-1` sign parity.

The live static question is now the prime-specific asymptotic scale of this **real signed elliptope value** relative to `sqrt(R_v)`. A generic complex-phase null is not representation-matched to the symmetric-taper branch because it injects continuous edge phase that midpoint centering removes. Useful controls should preserve edge magnitudes and the signed ratio-shell class before randomizing arithmetic organization.

## Keep representation gauge, coefficient sign geometry, relaxation strength, optimizer recovery and access time separate

Cycle holonomy decides exact envelope attainability; magnetic spectra, simple-cycle packing and the correlation SDP are progressively stronger static objects. VIS-218 and VIS-220 prove ceilings only for the first two certificate families. VIS-222 proves that the full SDP objective is constant-factor equivalent to the exact unit-modulus optimum for every Hermitian matrix.

VIS-223 adds a representation audit. For symmetric tapers the apparent continuous edge phase is mostly observation-origin gauge; after centering, the coefficient matrix is real signed and the complex SDP collapses exactly to the real elliptope. High SDP rank can still block exact phase recovery, but generic complex edge-phase frustration is no longer a matched description of this branch. One-parameter prime-log access time remains a separate problem and matters only when converting static torus information into quantitative finite-time recurrence.