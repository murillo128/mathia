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

VIS-213--VIS-226 close the strictly subcritical static scale up to constants. VIS-227--VIS-231 then identify the deterministic, independent-uniform, independent-nonuniform and finite-state Markov baselines for the critical collision statistic `S`.

VIS-232 adds the model-admission gate: `S=sum_j binom(N_j,2)`, so any confirmation randomization preserving the realized occupancy histogram fixes `S`. Exact transition-count preservation plus endpoints also fixes the histogram and therefore gives zero conditional variance.

VIS-233 makes the escape criterion structural. Endpoints plus first-order transition counts determine every translation-invariant additive range-one observable, while the lag-two return statistic

`T_2=sum_(t=1)^(m-2) 1_(x_t=x_(t+2))`

can vary inside one endpoint-matched first-order type. VIS-234 supplies the exact finite admission test: a recursion on unused transition counts and the current two-state suffix gives the complete conditional PGF `Z_(C;s,t)`, and `T_2` is nondegenerate exactly when `Z` is not a monomial.

VIS-235 now separates cheap exact calibration from the full-law recursion. Marking a return `u,v,u` and deleting its two transitions gives the exact mean

`E[T_2 | C,s,t] = [sum_(u,v) a_u(C^(u,v);t) W(C^(u,v);s,t)] / W(C;s,t)`,

where each `W` is an ordinary fixed-transition Markov-type cardinality. Whittle's determinant formula therefore evaluates the conditional center using at most one reduced-type count per ordered pair, without exploring the full remaining-transition state space. Because every numerator term is nonnegative, the same deletion sum gives a cheap exact zero-support gate. A positive mean still does **not** prove nondegeneracy; constant-positive types require the VIS-234 support/variance/PGF check.

The live exact-control route is therefore staged. For the actual predeclared critical prime-phase first-order type, first compute the Whittle deletion center and zero-support gate. If it survives, compute exact support/variance or the full VIS-234 law, or validate any conditional sampler against that recursion on tractable reductions. Only after the conditional law is frozen should the observed prime-phase value be compared with it and tested for representation stability and relevance to the signed prime-phase kernel.

## Keep static scale, occupancy baseline, dependence law, conditional sigma-field and observable interaction order separate

The deterministic floor, one-point law, lag-return center, higher-return covariance, preserved sigma-field and interaction order are distinct objects. VIS-232 shows that matching more realized structure is not monotonically safer; VIS-233 identifies the first interaction-order escape; VIS-234 proves that escape must be checked on the realized type; VIS-235 shows that some exact moments can be computed much more cheaply than the full conditional law.

A critical observable must declare both the stochastic model and what is conditioned on. If the null is strengthened to preserve length-three block counts, `T_2` is conditioned away and the statistic must move outward again. Source sensitivity must survive parameter estimation, representation perturbations and the exact conditional sigma-field; efficient calibration does not lower that scientific standard.