# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Find genuinely intermediate coercivity rather than an RH-equivalent vanishing threshold error

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-034-vanishing-capped-floor-error-is-already-the-global-weil-sign-problem`.

WI-304--WI-306 classify the frozen-reserve tail-dropped comparison and show that its first active prime creates an essential negative band. WI-307 changes the architecture by lifting the exterior reserve, leaving only a finite discrete negative sector at fixed aperture. WI-308 restores the omitted source exactly with a positive clipped tail multiplier.

WI-309--WI-312 separate the costs of endpoint concentration, high carrier frequency and compact-sector complexity. WI-313 gives a moving-floor sign statistic with no false negatives but possible `[0,delta)` contamination. WI-314 gives the complementary fixed-cap statistic `N_Q(-delta) <= N_D_hat(-1/2) <= N_Q(0)`.

WI-315 uses the actual nested domains `D_L=C_c^infty((-L,L))` to remove the changing-source margin loophole: every cofinal sequence with `L_j->infinity` and cap defect `delta_j->0` is sign-complete, because any compactly supported negative witness retains a fixed negative margin once it enters the windows.

WI-316 sharpens this at the variational floor. Writing `Dhat_j+(1/2)I=Q+E_j` with `0<=E_j<=delta_j I`, the comparison floor differs from the physical window floor by at most `delta_j`. Cofinal window floors converge to the global compact-support Weil floor, hence the capped comparison bottoms converge to that same floor. Therefore a cofinal bound

`Dhat_j >= -(1/2+epsilon_j) I`, with `epsilon_j->0`,

is already RH-equivalent when combined with the source-exact vanishing-cap identity. An `o(1)` threshold loss is not an easier approximation target.

The live theorem must therefore expose a **nonvanishing defect with a source-valid contraction mechanism**, or restrict to a genuinely smaller mode/source class whose improvement can later be propagated, or attack the exact comparison sign with new arithmetic structure. Merely proving `-1/2-o(1)` by softer operator estimates would already contain the missing RH-level information.

## Track comparison coercivity and compact complexity separately

WI-309 placed uniform-tail cost in endpoint singularity; WI-311 moves it into high carrier frequencies; WI-312 proves an anti-concentration/compact-complexity tradeoff. WI-313--WI-316 identify what that complexity ultimately buys: a source-preserving comparison whose fixed threshold and variational bottom converge to the actual compact-support sign problem.

Future estimates should keep endpoint regularity, modulation scale, frequency concentration, compact correction size, cap defect, fixed comparison defect and any defect-contraction rule as separate resources. A shrinking source-negative margin is no longer independent, and a shrinking comparison-floor error is no longer intermediate.

## Keep compact certificate design separate from full Weil positivity

Finite-dimensional trial-subspace optimization remains downstream of the source-valid information-retention question. The capped source-exact decomposition supplies bounded positive tail margin, while WI-315--WI-316 make its vanishing-cap cofinal semantics exact. Neither fact supplies a nontrivial fixed-defect contraction or the exact lower bound `Dhat >= -(1/2)I`; those are now the decisive arithmetic/operator gates.

## Preserve the signed-density quotient

Even a successful bounded-tail reserve-lifted architecture must eventually survive the exact density-one cancellation of WI-241. A large positive reserve or retained arithmetic mass is not yet the required sign-producing discrepancy theorem; the RH-relevant source variable remains the signed discrepancy after universal prime main density and pole cancellation.
