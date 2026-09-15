# MI-032 — Cancelling the Hadamard log budget creates a sign debt that Jordan domination cannot repay cheaply

**Evidence level:** exact signed-kernel conservation law from [NB-148](../../findings/NB-148-cancelling-the-hadamard-log-budget-forces-an-equal-mass-negative-poisson-lobe.md), sharpened by the source-specific method obstruction [NB-149](../../findings/NB-149-jordan-domination-reinstates-the-positive-poisson-log-budget.md), complementing the positive reflection-closure classification NB-147.

Positive exterior Poisson sampling has a rigid advantage: every zero contributes with one sign, but the universal Hadamard/archimedean term consumes a leading `(1/2)log G` budget. A zero-mass signed exterior sampler can cancel that universal term.

NB-148 gives the exact price. The associated zero-side Poisson kernel has zero vertical integral, so any positive lobe of integrated mass `A` is accompanied by exactly `A` negative mass. Cancelling the universal logarithmic budget exchanges a scalar budget for a **sign debt**; it does not create net positive zero mass.

NB-149 now classifies the most immediate repair. If the adverse contribution is bounded by the negative Jordan part, `(K_nu)_- <= K_(nu_-)`, or the whole signed expression is bounded by total variation, `|K_nu| <= K_|nu|`, the argument re-enters the positive Poisson cone. For a zero-mass sampler, `nu_+` and `nu_-` have equal total mass. Under the cheap-exterior regime, the Jordan majorant therefore carries a genuine logarithmic zero budget again; in the natural normalization `nu_+(Omega_G)=nu_-(Omega_G)=1`, the negative-piece bound costs `(1/2+o(1))log G`.

The same issue appears on the prime side: replacing the signed logarithmic-derivative combination by an absolute-value majorant discards the cancellation that removed the common Hadamard term. Thus **signed cancellation is useful only while the subsequent argument remains signed or location-sensitive**. Taking absolute values after cancellation forfeits the gain.

The live source question is now precise. A successful signed route must show that the actual zeta zeros sample the negative lobe unusually weakly, exploit cancellation/correlation in the von Mangoldt series, or couple positive and negative pieces directly to the Nyman target before any Jordan or triangle-inequality domination. Oscillatory coefficients alone are not a resource once their adverse part is estimated by positive machinery.

**Boundary.** NB-149 is a method obstruction, not a lower bound on the true negative contribution. Actual zeros may miss most of the negative lobe, and a genuinely signed prime-side identity may still compensate it. Those possibilities are exactly what the Jordan bound cannot see.