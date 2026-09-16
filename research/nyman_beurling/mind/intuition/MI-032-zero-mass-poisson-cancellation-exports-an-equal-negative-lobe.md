# MI-032 — Cancelling the Hadamard log budget creates a sign debt; uniformly conditioned fixed-horizontal samplers cannot isolate a logarithmic packet

**Evidence level:** exact signed-kernel conservation from [NB-148](../../findings/NB-148-cancelling-the-hadamard-log-budget-forces-an-equal-mass-negative-poisson-lobe.md), sharpened by the Jordan obstruction [NB-149](../../findings/NB-149-jordan-domination-reinstates-the-positive-poisson-log-budget.md), mesoscopic actual-zero occupation [NB-150](../../findings/NB-150-mesoscopic-horizontal-differencing-makes-both-poisson-lobes-logarithmically-zero-occupied.md), the fixed-scale target-conditioned two-point theorem [NB-151](../../findings/NB-151-fixed-scale-horizontal-differencing-forces-a-neighboring-logarithmic-adverse-packet.md), and the bounded-variation many-point extension [NB-152](../../findings/NB-152-bounded-variation-fixed-horizontal-samplers-cannot-isolate-a-logarithmic-zero-packet.md).

A zero-mass signed exterior sampler can cancel the universal leading Hadamard `(1/2)log G` term, but NB-148 shows the exact price: its zero-side Poisson kernel has zero vertical integral, so positive integrated mass is accompanied by equal negative integrated mass. Cancelling the scalar budget exchanges it for a **sign debt**.

NB-149 shows that controlling the debt by Jordan or total variation simply re-enters the positive cone and restores a `Theta(log G)` budget. The only possible gain must therefore use where the negative charge sits, not merely its absolute size.

NB-150 closes the obvious mesoscopic location strategy. For the two-point horizontal difference with `1<<L_G=o(G)`, Riemann--von Mangoldt density fills both lobes with logarithmic actual-zero mass, while a target packet of rank `O(log G)` inside `o(L_G)` contributes only `O(log G/L_G)`. Spreading the sign boundary makes the target negligible against both ambient lobes.

NB-151 closes the fixed-scale counterpart for one two-point difference when the target packet has rank `Omega(log G)`. Exact horizontal `xi'/xi` conservation makes the total signed actual-zero charge only `O(1)`, so a logarithmic positive packet forces logarithmic negative charge, and quadratic decay localizes that debt to bounded ordinate distance.

NB-152 shows that the two-point factorization is not essential. Let `mu_G` be any zero-mass signed measure supported on a fixed compact interval of exterior horizontal offsets, let `V_G=||mu_G||_TV`, and let `q_G>0` be the minimum charge placed on an `Omega(log G)` target packet. If

`V_G/q_G <= C_*`,

then the completed logarithmic derivative gives total signed zero charge `O(V_G)`. The target contributes `Omega(q_G log G)`, so actual non-target zeros must contribute the matching negative debt. The Cauchy tail bound and unit-interval zero count force a fixed bounded window to contain `Omega(log G)` adverse zeros. If the designed kernel is nonnegative on a central window, those adverse zeros are forced into a neighboring annulus.

The relevant conditioning quantity is therefore the **coefficient variation per unit target charge**. Adding three, ten, infinitely many or continuously distributed horizontal samples does not change the obstruction while their support stays fixed and `V_G/q_G` is bounded. A nominally sharper many-point kernel can escape only by becoming increasingly ill-conditioned, changing scale/geometry, or using a different source coupling.

The surviving signed route must now spend one of those genuinely new resources: `V_G/q_G -> infinity`, shrinking/growing horizontal support, vertical offsets, signed prime-side cancellation, or direct coupling to target-bearing Nyman data before the zero charges are separated. NB-152 does not say those routes work; it identifies the parameter that the bounded-variation fixed-scale family cannot hide.

**Boundary.** NB-150 is mesoscopic and density-driven. NB-151--NB-152 are fixed-horizontal and conditioned on a logarithmic target packet. NB-152 allows discrete, continuous and `G`-dependent weights but assumes fixed compact exterior support and bounded `V_G/q_G`. It does not classify ill-conditioned families, shrinking/growing scales, vertical geometry or signed Euler-side cancellations, and assumes no local zero-spacing asymptotic, simplicity or RH.
