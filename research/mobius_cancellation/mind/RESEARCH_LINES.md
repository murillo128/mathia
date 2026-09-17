# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Match compulsory reverse discrimination to the actual endpoint channel

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-060-total-variation-prices-source-edge-discrimination-without-breaking-at-singular-endpoints`.

The reciprocal endpoint problem has been reduced from syntactic complexity to invariant source discrimination. Bounded coefficient energy with nontrivial all-mode dephasing forces linear joint source information. On the natural source graph, destination-relative reliability charges only edges that cross the relevant quotient, while the canonical channel-law quotient itself must have an extensive exact boundary.

MC-351--MC-353 identify the compulsory local currency in the regular regime: neighboring source states must carry a nontrivial half-Jeffreys/privacy-loss budget. MC-354 prices that budget for additive log-smooth readouts through mean displacement and noise curvature. MC-355 closes the Gaussian location-scale side-channel escape, and MC-356 extends the accounting to finite-dimensional regular exponential families through integrated Fisher action.

MC-357 closes fixed-component mixtures, while MC-358 closes the generic move-the-components escape for an actual common latent architecture. If

`Theta~nu_x`, `Y|Theta=theta~K_x(.|theta)`

and `Q_x(dtheta,dy)=nu_x(dtheta)K_x(dy|theta)`, then the KL chain rule and marginal data processing give

`b_e(Y) <= (1/2)J(Q_x,Q_x') = b_e(Theta)+c_e(K)`.

Source discrimination may move between selector and conditional components, but it cannot disappear. This divergence ledger is sharp for regular channels but becomes infinite at the deterministic/singular endpoint.

MC-359 adds the bounded interpolation needed there. With `t_e=TV(P_x,P_x')` and normalized source-edge budget

`T_1=(2/m) sum_e t_e`,

one has

`I(X;Y) <= (log 2) T_1 + 2(R-1)log 2/m`.

Hence bounded-energy constant-factor dephasing forces `T_1/R` to stay bounded away from zero. In the matched-filter limit the ratio tends to its maximal value, and at exact unit-energy dephasing every surviving source edge has TV one. The source graph therefore remains quantitatively expensive even when KL/Jeffreys has blown up and ceased to be a useful finite metric.

The most actionable form is coupling-based. If the real architecture has source-independent shared randomness `Y=F(x,U_0)`, then

`TV(P_x,P_x') <= P(F(x,U_0) != F(x',U_0))`.

A one-source flip must therefore alter the complete transcript on a positive fraction of common random seeds on average if the architecture is to realize fixed nontrivial bounded-energy dephasing. This creates a finite upper-theorem surface for randomized or nearly deterministic constructions: expose the actual shared seed/branch structure and bound how often one source edge can change the transcript.

The live bridge is architecture-specific rather than family-classification-specific. For an actual Möbius endpoint construction, prove that its adjacent TV/common-seed change budget is too small, prove a finite lifted Jeffreys/Fisher upper bound where regularity permits it, or identify the singular/high-change source path that genuinely pays the compulsory budget. Hidden adaptive branches, random seeds, metadata or side channels must be included in the lifted transcript before any upper theorem is applied.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

Probabilistic proxies remain secondary until their conditioning is arithmetically consistent and their observables survive exact multiplicative simplification. A model that becomes degenerate after conditioning on an exact arithmetic stratum, or whose auxiliary statistic collapses algebraically to `M(x)`, has not created an independent cancellation mechanism.

## Keep the resource ledger explicit

The current invariant chain distinguishes source loading, coefficient energy, exact source quotient, joint transcript information, destination-cut geometry, aggregate edge KL, privacy-loss distribution, inverse distinguishability, mean displacement, covariance deformation, Fisher action, latent mixing-law divergence, conditional component divergence, lifted joint divergence, total-variation edge budget, common-seed change probability, support singularity, score curvature/noise scale and side-channel structure. These are different resources.

A useful Möbius endpoint theorem must close the loop in both directions: the destination must force enough neighboring-state discrimination, and the concrete arithmetic channel must be shown unable to afford that discrimination at the relevant scale. MC-354--MC-358 price progressively broader regular/lifted architectures; MC-359 adds a bounded source-edge currency that survives singularity. The remaining problem is no longer to name a more complicated generic statistical family, but to prove a source-edge upper theorem for the actual Möbius-derived transcript or exhibit the source-dependent high-change/singular channel that defeats such an upper bound.
