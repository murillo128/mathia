# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Move to the transition, optimizer structure and access time: the subcritical static scale is closed

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-017-critical-collision-counts-need-the-balanced-occupancy-baseline`.

VIS-213--VIS-224 reduce fixed-`(y,H)` worst starts to a midpoint-gauged real signed ratio-shell Hamiltonian and compare the binary Ising optimum, exact torus optimum and real correlation SDP within universal constants.

VIS-225 proves a coherent-block lower bound throughout `H log y/y ->0`; VIS-226 supplies the matching upper bound. Consequently

`I_abs(B_(y,H)) asy y/(H log y)`,

and the exact torus and real SDP objectives have the same order. Since `R_v(y,H) asy 1/H`, all three Haar-normalized objectives have scale `y/(sqrt(H) log y)` up to constants. The strictly subcritical static question is therefore closed at the coarse scale.

VIS-227 identifies the deterministic balanced-occupancy floor for critical phase-cell collisions. VIS-228 shows that subtracting this floor is insufficient even for independent uniform allocation: the expected excess is `Theta(J)` while the standard deviation is `Theta(sqrt(J))` at fixed positive occupancy density.

VIS-229 now gives the exact independent **nonuniform** baseline. For cell probabilities `(p_j)`, with `q_2=sum p_j^2` and `q_3=sum p_j^3`,

`E[S]=binom(m,2)q_2`,

`Var(S)=binom(m,2)(q_2-q_2^2)+6binom(m,3)(q_3-q_2^2)`.

The extra term satisfies `q_3-q_2^2=Var(p_X)>=0`; it is present without pair dependence and vanishes only when all positive-probability cells are equiprobable. Matching an effective cell count or collision mean alone can therefore create a false critical residual from one-point heterogeneity.

The critical pair-collision question begins only after centering and scaling against an admitted one-point law and then testing stronger dependent controls that preserve the intended logarithmic-gap structure. The current local clue should treat the `(q_2,q_3)` categorical law as the minimal independent baseline, not the final null. If the residual disappears there or under a gap-preserving dependent control, the next statistic must carry genuinely different information such as multiscale persistence or direction-sensitive phase structure.

## Keep static scale, deterministic floor, stochastic baseline, optimizer recovery and dynamical access separate

VIS-226 fixes the strictly subcritical static supremum scale but not the exact optimizer, sharp constant or recurrence/access time. VIS-227 fixes the deterministic balls-in-cells minimum. VIS-228 fixes the uniform independent stochastic baseline. VIS-229 shows that the nonuniform independent baseline already needs both the second and third power sums of the one-point cell law.

These are separate currencies. A critical statistic must first remove the universal deterministic constraint, then calibrate the admitted one-point stochastic law including its heterogeneity-driven variance, then account for dependence preserved by stronger controls, and only afterward ask whether any surviving residual influences the Ising/torus/SDP objective or the physical prime-log orbit.
