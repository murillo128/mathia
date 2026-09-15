# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Move to the transition, optimizer structure and access time: the subcritical static scale is closed

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-019-markov-collision-variance-is-controlled-by-three-and-four-time-return-tensors`.

VIS-213--VIS-226 reduce the subcritical static problem and prove `I_abs(B_(y,H)) asy y/(H log y)`, with the exact torus and real SDP objectives of the same order. The strictly subcritical static scale is therefore closed up to constants.

VIS-227 identifies the deterministic balanced-occupancy floor for critical phase-cell collisions. VIS-228 shows that subtracting this floor is insufficient under independent uniform allocation. VIS-229 gives the exact independent nonuniform baseline: the center uses `q_2=sum p_j^2`, while the variance also uses `q_3=sum p_j^3`; one-point heterogeneity alone can create a false residual.

VIS-230 closes the next centering shortcut. For a stationary Markov control with the same one-point law, the exact center is

`E[S]=sum_(r=1)^(m-1)(m-r)c_r`, `c_r=P(X_0=X_r)`,

not `binom(m,2)q_2`.

VIS-231 closes the corresponding covariance calculation for every specified finite-state stationary first-order Markov null. Squaring the collision U-statistic shows that overlapping pair indicators require the triple-return tensor `T_(r,s)`, while disjoint pairs require three four-time pair-pair tensors `D1,D2,D3`; the resulting finite sum is the exact `Var(S)`. The independent categorical formula of VIS-229 is recovered when `P` has rank one.

The critical pair-collision question now begins only after **choosing and justifying the dependence model itself**. For an admitted Markov null, center and finite-sample variance are no longer missing. A standardized prime residual must survive that exact calibration, parameter-estimation uncertainty and representation perturbations before any coupling to the signed prime-phase Hamiltonian is meaningful. If the intended control is renewal, higher-order, nonstationary or scale-dependent, its own three-/four-time structure must be calibrated rather than forced into the Markov formula.

## Keep static scale, deterministic floor, marginal baseline, dependence baseline, covariance structure, optimizer recovery and dynamical access separate

VIS-226 fixes the strictly subcritical static supremum scale but not the exact optimizer, sharp constant or recurrence/access time. VIS-227 fixes the deterministic balls-in-cells minimum. VIS-228 fixes the uniform independent stochastic baseline. VIS-229 shows that nonuniform independent fluctuations require second and third power sums of the one-point law. VIS-230 shows that dependent centering additionally requires the lag-return profile. VIS-231 shows that dependent variance requires three- and four-time joint return tensors beyond that center.

These are separate currencies. A critical statistic must remove the universal deterministic constraint, calibrate the admitted one-point law, dependence center and higher joint covariance, and only afterward ask whether a surviving residual influences the Ising/torus/SDP objective or the physical prime-log orbit.