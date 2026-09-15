# MI-032 — Cancelling the Hadamard log budget creates a sign debt; mesoscopic horizontal spreading makes both lobes background-dominated

**Evidence level:** exact signed-kernel conservation law from [NB-148](../../findings/NB-148-cancelling-the-hadamard-log-budget-forces-an-equal-mass-negative-poisson-lobe.md), sharpened by the Jordan-method obstruction [NB-149](../../findings/NB-149-jordan-domination-reinstates-the-positive-poisson-log-budget.md) and the source-specific mesoscopic occupation theorem [NB-150](../../findings/NB-150-mesoscopic-horizontal-differencing-makes-both-poisson-lobes-logarithmically-zero-occupied.md), complementing the positive reflection-closure classification NB-147.

Positive exterior Poisson sampling has a rigid advantage: every zero contributes with one sign, but the universal Hadamard/archimedean term consumes a leading `(1/2)log G` budget. A zero-mass signed exterior sampler can cancel that universal term.

NB-148 gives the exact price. The associated zero-side Poisson kernel has zero vertical integral, so any positive lobe of integrated mass `A` is accompanied by exactly `A` negative mass. Cancelling the universal logarithmic budget exchanges a scalar budget for a **sign debt**; it does not create net positive zero mass.

NB-149 classifies the most immediate repair. If the adverse contribution is bounded by the negative Jordan part or the whole signed expression by total variation, the argument re-enters the positive Poisson cone. Under the cheap-exterior scaling, that majorant restores a genuine `Theta(log G)` zero budget. Taking absolute values after cancellation therefore forfeits the gain.

NB-150 asks whether location sensitivity can instead make the negative lobe harmless by separating two horizontal sample points on a growing scale `1<<L_G=o(G)`. For the favorable sampler

`delta_(1+L+iG) - delta_(1+cL+iG)`,

the rescaled signed zero profile is

`q_c(x)=1/(1+x^2)-c/(c^2+x^2)`.

Its positive and negative Lebesgue masses are equal, but more importantly the **actual zeta zero set fills both lobes at mean density**:

`sum_rho (Q_G(rho))_+ = (A_c/(2pi)+o(1)) log G`,

`sum_rho (Q_G(rho))_- = (A_c/(2pi)+o(1)) log G`.

At the same time a target packet of rank `O(log G)` contained in `o(L_G)` receives only `O(log G/L_G)` total unnormalized charge. Multiplying the sampler to restore order-one target charge scales the two background lobes by the same factor. Thus mesoscopic horizontal spreading does not repay the sign debt; it makes the desired packet negligible against both signs of the ambient zero density.

The live source question is consequently narrower. A successful signed route must stay at fixed or shrinking ordinate scales where the `O(log G)` zero-count remainder can compete with the mean density, use a kernel whose sign placement is tied to exceptional zero information, exploit genuinely signed/correlated von Mangoldt contributions, or couple positive and negative pieces directly to the Nyman target before lobe separation. Neither Jordan domination nor mesoscopic smoothing supplies the missing resource.

**Boundary.** NB-150 is a two-point horizontal mesoscopic theorem. It does not classify fixed-scale samplers, many-point signed kernels, vertical differencing or zero-spacing-scale localization. The result is unconditional and uses only Riemann--von Mangoldt density; it does not prove that every signed route is background-dominated.