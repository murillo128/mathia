# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders, and a growing-complexity diagonal selector can pass every fixed finite-prime finite-order Haar test. A useful theorem needs a predeclared joint complexity/height growth law or source information outside the sampled phase-clock state.

## Make the critical dependence null nondegenerate before testing prime specificity

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-020-a-conditional-null-is-invalid-when-it-fixes-the-statistics-sufficient-counts`.

VIS-213--VIS-226 close the strictly subcritical static scale up to constants. VIS-227--VIS-229 then identify the deterministic, independent-uniform and independent-nonuniform baselines for the critical collision statistic `S`.

VIS-230--VIS-231 close centering and finite-sample variance for any specified finite-state stationary first-order Markov null. The center uses the lag-return profile; the variance additionally needs three- and four-time return tensors.

VIS-232 adds a model-admission gate that is logically prior to those formulas. Since

`S=sum_j binom(N_j,2)`,

any confirmation-sample randomization preserving the realized occupancy histogram fixes `S`. Exact transition-count preservation plus endpoints also fixes the histogram and therefore gives zero conditional variance.

VIS-233 makes the escape criterion exact. Endpoints plus first-order transition counts determine **every translation-invariant additive range-one observable**, not just `S`. The lag-two return statistic

`T_2=sum_(t=1)^(m-2) 1_{x_t=x_(t+2)}`

is the first simple counterexample: it depends on length-three block counts and can vary inside one endpoint-matched first-order type. The explicit binary type `00010,00100,01000` has identical transition counts but `T_2=2,1,2`.

The live critical test therefore has two honest routes. Either fit a stochastic dependence model from independent calibration information and allow confirmation occupancies to fluctuate, carrying estimation uncertainty into the VIS-230/VIS-231 standardization; or preserve realized first-order structure and predeclare a **range-two-or-higher** observable such as `T_2`, first proving that it has nonzero conditional variance on the actual critical prime-phase type. Only after that admission gate is passed is a prime-specific residual meaningful.

## Keep static scale, occupancy baseline, dependence law, conditional sigma-field and observable interaction order separate

The deterministic floor, one-point law, lag-return center, higher return covariance, conditional randomization class and interaction order of the tested statistic are distinct objects. VIS-232 shows that matching more realized structure is not monotonically safer; VIS-233 sharpens this into a hierarchy: preserving length-two block counts fixes the entire additive range-one class, while a length-three statistic may still survive.

A critical observable must therefore declare both the stochastic model and what is conditioned on. If the null is strengthened to preserve length-three block counts, `T_2` is conditioned away and the statistic must move outward again. Source sensitivity must survive parameter estimation, representation perturbations and the exact conditional sigma-field before any bridge to the signed prime-phase Hamiltonian, optimizer geometry or physical prime-log orbit is interpreted.