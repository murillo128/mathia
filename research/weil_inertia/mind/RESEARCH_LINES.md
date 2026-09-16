# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Find genuinely intermediate coercivity rather than an RH-equivalent vanishing threshold error or scalar self-bootstrap

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-035-finite-localization-portfolios-cannot-self-contract-a-scalar-defect`.

WI-304--WI-306 classify the frozen-reserve tail-dropped comparison and show that its first active prime creates an essential negative band. WI-307 changes the architecture by lifting the exterior reserve, leaving only a finite discrete negative sector at fixed aperture. WI-308 restores the omitted source exactly with a positive clipped tail multiplier.

WI-309--WI-312 separate the costs of endpoint concentration, high carrier frequency and compact-sector complexity. WI-313 gives a moving-floor sign statistic with no false negatives but possible `[0,delta)` contamination. WI-314 gives the complementary fixed-cap statistic `N_Q(-delta) <= N_D_hat(-1/2) <= N_Q(0)`.

WI-315 uses the actual nested domains `D_L=C_c^infty((-L,L))` to remove the changing-source margin loophole: every cofinal sequence with `L_j->infinity` and cap defect `delta_j->0` is sign-complete, because any compactly supported negative witness retains a fixed negative margin once it enters the windows.

WI-316 sharpens this at the variational floor. Writing `Dhat_j+(1/2)I=Q+E_j` with `0<=E_j<=delta_j I`, the comparison floor differs from the physical window floor by at most `delta_j`. Cofinal window floors converge to the global compact-support Weil floor, hence the capped comparison bottoms converge to that same floor. Therefore a cofinal bound

`Dhat_j >= -(1/2+epsilon_j) I`, with `epsilon_j->0`,

is already RH-equivalent when combined with the source-exact vanishing-cap identity. An `o(1)` threshold loss is not an easier approximation target.

WI-317 closes the most direct fixed-defect bootstrap. For any fixed finite portfolio of source-exact smooth localization identities at a fixed aperture, feeding only the same scalar semibound `Q(h)>=-c||h||^2` back into the localized pieces cannot produce a uniform improvement `c -> c-kappa`. High-frequency modulation and simultaneous recurrence give a weakly-null sequence on which every active prime-power localization error in the whole portfolio is nonnegative (or all source defects vanish before the first prime activates), so even choosing the best localizer after seeing the test vector cannot force the negative error required for contraction.

WI-318 removes finiteness as the generic loophole for the unit-window architecture. An arbitrary finite or infinite/adaptively selected family with uniformly bounded total `H^1` cost has uniform `O(1/|t|)` decay of the continuous localization error. Unit support simultaneously forces a uniform first-prime autocorrelation gap: translation by `log 2` is square-zero, so the Haagerup--de la Harpe numerical-radius bound gives `R(log 2)<=1/2` for every member. One common Kronecker recurrence sequence therefore defeats the entire family at once. Reusing only the same scalar semibound cannot contract the defect even with an infinite adaptive portfolio as long as its frequency second moment stays uniformly bounded.

The live theorem must therefore add information or pay a genuinely noncompact complexity bill. Within the source-exact unit-window scalar-feedback architecture, an escape requires unbounded derivative energy/frequency second moment; merely adding infinitely many or adaptive localizers is not enough. WI-318 does not say such spectral noncompactness is sufficient, and WI-311--WI-312 already show that high-carrier escape can move the difficulty into compact complexity. The cleaner alternatives remain a stronger localized arithmetic estimate, a mode/prime-dependent or vector/matrix invariant, a different support geometry, or a direct attack on the exact comparison sign.

## Track comparison coercivity, compact complexity and feedback information separately

WI-309 placed uniform-tail cost in endpoint singularity; WI-311 moves it into high carrier frequencies; WI-312 proves an anti-concentration/compact-complexity tradeoff. WI-313--WI-316 identify what that complexity ultimately buys: a source-preserving comparison whose fixed threshold and variational bottom converge to the actual compact-support sign problem. WI-317 adds a separate gate: finite localization can redistribute a scalar lower bound without strengthening it. WI-318 sharpens that gate to arbitrary adaptive unit-window portfolios with bounded total `H^1`: portfolio cardinality is still not new information, and escaping the recurrence obstruction while reusing the same scalar premise requires spectral noncompactness.

Future estimates should keep endpoint regularity, modulation scale, frequency concentration, compact correction size, cap defect, fixed comparison defect, localization-portfolio size, **uniform derivative/frequency-moment budget**, the actual information fed into each localized piece, and any defect-contraction rule as separate resources. A shrinking source-negative margin is no longer independent, a shrinking comparison-floor error is no longer intermediate, and a larger or infinite bounded-complexity localization portfolio is not new arithmetic information when every piece is controlled only by the same scalar semibound.

## Keep compact certificate design separate from full Weil positivity

Finite-dimensional trial-subspace optimization remains downstream of the source-valid information-retention question. The capped source-exact decomposition supplies bounded positive tail margin, while WI-315--WI-316 make its vanishing-cap cofinal semantics exact. Neither fact supplies a nontrivial fixed-defect contraction or the exact lower bound `Dhat >= -(1/2)I`; WI-317--WI-318 further show that neither a fixed finite portfolio nor an arbitrary uniformly `H^1`-bounded adaptive unit-window family can manufacture that contraction from the same scalar premise.

## Preserve the signed-density quotient

Even a successful bounded-tail reserve-lifted architecture must eventually survive the exact density-one cancellation of WI-241. A large positive reserve or retained arithmetic mass is not yet the required sign-producing discrepancy theorem; the RH-relevant source variable remains the signed discrepancy after universal prime main density and pole cancellation.
