# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Leave simple-cycle packing and attack the exact fixed-modulus torus problem or a genuinely stronger certificate

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question`, `MI-010-weighted-null-needs-separate-concentration-and-shape-dimensions`, `MI-011-finite-start-dephasing-is-priced-by-weighted-local-spacing`, `MI-012-cutoff-tuning-cannot-beat-the-four-form-pointwise-threshold`, `MI-013-autocorrelation-tapers-make-exact-difference-shells-noncancelling`, `MI-014-one-cancellation-shell-energy-is-an-anchor-gram-problem-and-thin-windows-diagonalize-it-exactly`, `MI-015-prime-phase-worst-starts-are-frustrated-torus-optimization`.

VIS-213 identifies the fixed-`(y,H)` worst start with the full unit-modulus quadratic optimum. VIS-214 identifies cycle holonomy as the exact gauge-invariant envelope obstruction, VIS-215 accumulates it through fractional weighted simple-cycle packing, and VIS-216 adds the normalized magnetic-Laplacian relaxation.

VIS-217--VIS-218 close the normalized spectral branch throughout `H log y/y->0`: the actual prime graph has `N_eff/n->infinity`, forcing the magnetic certificate above Haar-RMS scale by a diverging factor regardless of edge phases.

VIS-219 prices the stronger cycle-packing certificate in destination units. If `P=min(P_+,P_-)`, then exactly

`(B-P)/sqrt(R) = sqrt(2 N_eff) (1-P/B)`.

Thus Haar-RMS certification would require near-total weighted-envelope saturation, with relative deficit `O(N_eff^-1/2)`.

VIS-220 now proves that such saturation is structurally impossible for the `VIS-215` relaxation before any arithmetic phase information is used. For support-graph girth `g`, every simple-cycle reward and the edge-capacity packing constraint give

`P_+,P_- <= (2/g^2) B`.

For an ordinary simple graph `g>=3`, so `P_+,P_-<=2B/9`, the residual obeys `B-min(P_+,P_-)>=7B/9`, and

`D_pack >= (7/9)sqrt(2N_eff)`.

Hence `D_pack->infinity` throughout the strictly subcritical prime regime. The packing clue is resolved negatively: adding more cycles or optimizing the same LP cannot fix a ceiling built into its reward/capacity geometry.

The live static object is therefore the **exact fixed-modulus torus optimization** from VIS-213, or a genuinely stronger certificate that retains interactions discarded by both the magnetic and fractional simple-cycle relaxations. Failure of those relaxations is not a lower bound on the exact torus optimum. One-parameter orbit access time remains separate and matters only after a useful static pointwise bound exists.

## Keep representation closure, relaxation strength, certificate ceilings, exact torus optimization and access time separate

Cycle holonomy decides exact envelope attainability; magnetic spectra and simple-cycle packing only certify bounds. VIS-218 gives a destination-scale limitation of the normalized spectral relaxation. VIS-220 gives a universal limitation of the simple-cycle packing relaxation. Neither result says the exact unit-modulus optimum is large.

Future work should therefore test any new relaxation against its own best possible destination-normalized ceiling before investing in arithmetic phase structure. A certificate family that cannot in principle leave `O(sqrt(R))` residual when `N_eff` diverges is exhausted even if its local geometric interpretation is genuine.