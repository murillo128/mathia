# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Match compulsory reverse discrimination to the actual endpoint channel

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-061-hellinger-affinity-tensorizes-the-bounded-source-edge-tariff`.

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

Hence bounded-energy constant-factor dephasing forces `T_1/R` to stay bounded away from zero. In a genuine shared-randomness architecture `Y=F(x,U_0)`, TV is bounded by the probability that a one-source flip changes the complete transcript under the common seed. This gives a finite architecture-specific upper-theorem surface even when KL/Jeffreys is singular.

MC-360 adds a **compositional bounded currency**. If `h_e^2=H^2(P_x,P_x')` and `H_1=(2/m)sum_e h_e^2`, then

`I(X;Y) <= H_1 + 2(R-1)/m`,

so bounded-energy nontrivial dephasing forces an extensive average Hellinger boundary. More importantly, for a genuine source-dependent latent law followed by conditionally independent components, Hellinger affinity factorizes and yields

`H^2(P_x,P_x') <= H^2(nu_x,nu_x') + sum_j int sqrt(r_x r_x') h_(e,j)^2 d kappa`.

Thus source discrimination cannot disappear by being split among a latent selector and many weak product components. With source-independent latent randomness this becomes an extensive weighted source-coordinate incidence tariff. Hellinger fills the gap between the TV/common-seed interpretation and the regular Jeffreys/Fisher ledger: it remains bounded at singularity and composes naturally across conditional products.

MC-361 sharpens the **destination-side capacity curve** independently of which architecture later pays it. For binary source phases with posterior means `b_i=E[X_i|Y]` and average squared predictability `rho^2=R^(-1)sum_i E b_i^2`, posterior entropy obeys

`H(X|Y) <= R h((1+rho)/2)`,

so

`I(X;Y) >= H(X)-R h((1+rho)/2)`.

Combined with the endpoint energy/dephasing inequality, normalized energy at most one and dephasing error at most `epsilon` force

`I(X;Y) >= H(X)-R h(epsilon/2)`.

MC-362 first showed that the permanent `log 2` endpoint slack in the direct `JS<=H^2` route was not architectural: passing through the endpoint-sharp TV tariff and then transferring TV to Hellinger already forces `H_1/R -> 1` as `epsilon->0`.

MC-363 now removes the logarithmic quantitative loss of that detour while staying entirely in the compositional Hellinger currency. If `z=H^2(P,Q)` and

`Phi(z)=log 2-h((1-sqrt(1-(1-z)^2))/2)`,

then the sharp distribution-free envelope is

`JS(P,Q) <= Phi(z)`.

`Phi` is increasing and concave and equality is attained by a binary-symmetric experiment. Inserting this envelope directly into the punctured source-cube aggregation gives

`I(X;Y) <= R q_R Phi(H_1/(R q_R)) + 2(R-1)log 2/m`.

At matched-filter energy, dephasing error `epsilon` therefore forces

`liminf H_1/R >= 1-sqrt(2 epsilon-epsilon^2)`

along the even-rank endpoint sequence. The Hellinger deficit is now `O(sqrt(epsilon))`, rather than the `O(sqrt(epsilon log(1/epsilon)))` deficit left by the TV-mediated conversion in MC-362. The same sharp lower bound transfers through MC-360 to the source-independent latent/product incidence ledger. Splitting the transcript into many weak components cannot hide in the metric-conversion slack.

The live bridge is therefore architecture-specific rather than family-classification-specific. For an actual Möbius endpoint construction, expose its complete transcript including adaptive branches, random seeds, metadata and side channels, then use the finite currency matching its architecture. A common-seed construction invites a TV change-probability upper bound; a latent/product construction invites a Hellinger latent/component-incidence upper bound; a regular channel may admit a sharper lifted Jeffreys/Fisher theorem. Near the deterministic endpoint, MC-363 says that a Hellinger/product upper theorem must beat an almost-maximal per-direction tariff with the sharp `sqrt(epsilon)` deficit. The task remains to prove that the actual arithmetic channel cannot afford that boundary, or identify the genuine source-dependent component that pays it.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

Probabilistic proxies remain secondary until their conditioning is arithmetically consistent and their observables survive exact multiplicative simplification. A model that becomes degenerate after conditioning on an exact arithmetic stratum, or whose auxiliary statistic collapses algebraically to `M(x)`, has not created an independent cancellation mechanism.

## Keep the resource ledger explicit

The current invariant chain distinguishes source loading, coefficient energy, exact source quotient, joint transcript information, posterior entropy/predictability, destination-cut geometry, aggregate edge KL, privacy-loss distribution, inverse distinguishability, mean displacement, covariance deformation, Fisher action, latent mixing-law divergence, conditional component divergence, lifted joint divergence, total-variation edge budget, common-seed change probability, Hellinger edge budget, affinity-weighted component incidence, support singularity, score curvature/noise scale and side-channel structure. These are different resources.

A useful Möbius endpoint theorem must close the loop in both directions: the destination must force enough neighboring-state discrimination, and the concrete arithmetic channel must be shown unable to afford that discrimination at the relevant scale. MC-354--MC-358 price progressively broader regular/lifted architectures; MC-359 adds a bounded source-edge currency that survives singularity; MC-360 adds the bounded product/latent ledger needed to prevent source sensitivity from disappearing by component splitting; MC-361 sharpens the compulsory binary transcript-information curve; MC-362 proves endpoint sharpness survives transfer into Hellinger; MC-363 makes that transfer quantitatively sharp in the Hellinger coordinate itself. The remaining problem is no longer to name a more complicated generic statistical family, but to prove a source-edge or transcript-information upper theorem for the actual Möbius-derived architecture in the currency native to it.
