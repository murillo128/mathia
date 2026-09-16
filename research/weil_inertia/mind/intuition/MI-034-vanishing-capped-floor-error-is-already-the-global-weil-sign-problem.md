# MI-034 — Vanishing capped-floor error is already the global Weil sign problem

**Evidence level:** exact synthesis from [WI-311](../../findings/WI-311-modulated-pair-reserve-lift.md), [WI-315](../../findings/WI-315-nested-weil-windows-make-vanishing-cap-diagonals-inertia-complete.md), and [WI-316](../../findings/WI-316-capped-comparison-bottoms-converge-to-global-weil-floor.md), using elementary variational/min--max monotonicity and Weil's criterion.

For the source-exact capped decomposition on a cofinal compact-support sequence,

`Dhat_j + (1/2)I = Q + E_j`, with `0 <= E_j <= delta_j I` and `delta_j->0`.

If `lambda_j` is the Rayleigh infimum of `Q` on `C_c^infty((-L_j,L_j))` and `lambdahat_j` that of `Dhat_j+(1/2)I`, then

`lambda_j <= lambdahat_j <= lambda_j+delta_j`.

Because the physical windows are nested restrictions of one global Weil form, every compact test eventually belongs to every cofinal sequence. Thus `lambda_j` converges to the global compact-support variational floor `lambda_c`, and the comparison bottoms converge to the same `lambda_c`.

This changes the meaning of “approximate positivity.” A bound

`Dhat_j >= -(1/2+epsilon_j) I`, with `epsilon_j->0`,

forces `lambda_c>=0` and therefore RH. Conversely, if RH fails, one fixed compact witness has a fixed negative Rayleigh margin and eventually forces the comparison bottom a fixed distance below zero despite `delta_j->0`. Failure cannot hide in a vanishing threshold defect.

Hence **a cofinal `o(1)` comparison-floor error is not an intermediate theorem**. A genuinely weaker target must retain a nonzero defect and supply an independent source-valid contraction/iteration mechanism, or control a narrower class whose improvement can later be propagated. Otherwise the apparently soft asymptotic estimate has merely restated the full sign problem in the comparison coordinates.

**Boundary.** This conclusion uses the source-exact cap identity, vanishing cap error and cofinal nested compact-support domains. A fixed nonzero lower-floor defect yields only semiboundedness and can still be a meaningful intermediate result. No norm-resolvent convergence, eigenvector convergence or global self-adjoint realization is required.
