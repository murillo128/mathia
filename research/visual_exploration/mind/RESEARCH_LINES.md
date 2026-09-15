# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Calibrate critical dependence on a representation-matched monotone object

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-020-a-conditional-null-is-invalid-when-it-fixes-the-statistics-sufficient-counts`.

VIS-213--VIS-226 close the strictly subcritical static scale up to constants. VIS-227--VIS-231 then identify deterministic, independent-uniform, independent-nonuniform and finite-state Markov baselines for the critical collision statistic `S`.

VIS-232 adds the sigma-field admission gate: `S=sum_j binom(N_j,2)`, so any confirmation randomization preserving the realized occupancy histogram fixes `S`; exact transition-count preservation plus endpoints also fixes that histogram. VIS-233--VIS-235 show that in a generic first-order Markov type a range-two statistic such as

`T_2=sum_(t=1)^(m-2) 1_(x_t=x_(t+2))`

can escape the preserved range-one sigma-field, with an exact type-conditional PGF and a cheaper deletion formula for its mean.

VIS-236 now closes that generic escape for the **actual ordered prime-coordinate cells**. Because primes and interval cells are both ordered, the label sequence is nondecreasing. Hence `T_2=sum_j(N_j-2)_+`, and the endpoint-matched first-order transition table admits exactly one compatible label sequence. The exact PGF is always a monomial; numerical evaluation of the VIS-234 recursion on the actual type cannot resurrect variability that the representation forbids.

The live critical question is therefore to choose a dependence model on geometry that genuinely varies while remaining inside the representation support: ordered cell counts, normalized prime gaps, within-cell point locations, or another increasing-point-process object. Before any prime-specific test, freeze such a model/statistic independently, prove that the statistic remains nondegenerate under the admitted monotone sample space, and verify stability under the allowed cell-origin/representation perturbations. Only then ask whether a residual survives and couples back to the signed prime-phase kernel.

## Keep stochastic law, conditional sigma-field, interaction order and representation support separate

The deterministic floor, one-point law, lag-return center, higher-return covariance, preserved sigma-field, interaction order and structural support of the representation are distinct objects. VIS-232 shows that matching more realized structure can condition the statistic away. VIS-233--VIS-235 show that increasing interaction order can escape a generic first-order type. VIS-236 shows that this is not enough when the actual representation occupies a much smaller monotone subset of that type space.

A critical observable must therefore declare both the stochastic model and the geometric support on which it acts. A statistically nondegenerate null is invalid if it creates label revisits/backtracking unavailable to the prime-coordinate cells; conversely a support-faithful null is uninformative if it fixes the tested statistic. Source sensitivity must survive both gates, parameter estimation and representation perturbations before any arithmetic interpretation is made.