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

WI-318 removes finiteness as the generic loophole for the unit-window architecture. An arbitrary finite or infinite/adaptively selected family with uniformly bounded total `H^1` cost has uniform `O(1/|t|)` decay of the continuous localization error. Unit support simultaneously forces a uniform first-prime autocorrelation gap: translation by `log 2` is square-zero, so the Haagerup--de la Harpe numerical-radius bound gives `R(log 2)<=1/2` for every member. One common Kronecker recurrence sequence therefore defeats the entire family at once.

WI-319 quantifies exactly how far that recurrence obstruction extends. If `M_t` is the total derivative-energy/frequency-second-moment budget of a `t`-dependent unit-window localizer, then on the adversarial carrier

`|C_t| <= C[(1+sqrt(M_t))/|t| + M_t log(2+|t|)/t^2]`.

Hence every family with `M_t=o(t^2/log t)` still has vanishing continuous defect along the common recurrence sequence, and any selector claiming a fixed scalar contraction there must pay `M_(t_k) >= c t_k^2/log t_k`. This scale is sharp for the falsifier: an explicit three-window resonant family with `M_t=M_0+c t^2/log t` produces an order-one negative continuous defect and can defeat the recurrence witness itself.

The live theorem is therefore no longer merely “allow unbounded `H^1`.” Within the source-exact unit-window scalar-feedback architecture, escaping the known recurrence no-go requires an **almost-quadratic frequency budget** and then a new argument controlling the resonances that such a budget creates on all test vectors. Paying `t^2/log t` is necessary to escape this witness and sufficient only to invalidate this particular obstruction; it is not evidence of a global contraction. Cleaner alternatives remain a stronger localized arithmetic estimate, mode/prime-dependent or vector/matrix information, different support geometry, or a direct attack on the exact comparison sign.

## Track comparison coercivity, compact complexity and feedback information separately

WI-309 placed uniform-tail cost in endpoint singularity; WI-311 moves it into high carrier frequencies; WI-312 proves an anti-concentration/compact-complexity tradeoff. WI-313--WI-316 identify what that complexity ultimately buys: a source-preserving comparison whose fixed threshold and variational bottom converge to the actual compact-support sign problem. WI-317 adds a separate gate: finite localization can redistribute a scalar lower bound without strengthening it. WI-318 sharpens that gate to arbitrary adaptive unit-window portfolios with bounded total `H^1`. WI-319 makes the escape price quantitative and sharp for the recurrence falsifier: sub-`t^2/log t` second moment is still too compact, while resonant mass at that scale can create an order-one continuous correction.

Future estimates should keep endpoint regularity, modulation scale, frequency concentration, compact correction size, cap defect, fixed comparison defect, localization-portfolio size, **frequency-second-moment growth relative to `t^2/log t`**, the actual information fed into each localized piece, and any defect-contraction rule as separate resources. A shrinking source-negative margin is no longer independent, a shrinking comparison-floor error is no longer intermediate, a larger or infinite bounded-complexity localization portfolio is not new arithmetic information, and crossing the recurrence complexity threshold is not itself a sign theorem.

## Keep compact certificate design separate from full Weil positivity

Finite-dimensional trial-subspace optimization remains downstream of the source-valid information-retention question. The capped source-exact decomposition supplies bounded positive tail margin, while WI-315--WI-316 make its vanishing-cap cofinal semantics exact. Neither fact supplies a nontrivial fixed-defect contraction or the exact lower bound `Dhat >= -(1/2)I`; WI-317--WI-319 further show that scalar localization cannot manufacture that contraction from the same premise below the sharp recurrence complexity threshold, and that crossing the threshold merely removes this one falsifier.

## Preserve the signed-density quotient

Even a successful bounded-tail reserve-lifted architecture must eventually survive the exact density-one cancellation of WI-241. A large positive reserve or retained arithmetic mass is not yet the required sign-producing discrepancy theorem; the RH-relevant source variable remains the signed discrepancy after universal prime main density and pole cancellation.