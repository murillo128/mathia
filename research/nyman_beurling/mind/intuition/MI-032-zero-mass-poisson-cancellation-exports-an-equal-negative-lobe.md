# MI-032 — Cancelling the Hadamard log budget creates a sign debt; compact sublogarithmically conditioned samplers cannot isolate a logarithmic packet

**Evidence level:** exact signed-kernel conservation from [NB-148](../../findings/NB-148-cancelling-the-hadamard-log-budget-forces-an-equal-mass-negative-poisson-lobe.md), sharpened by the Jordan obstruction [NB-149](../../findings/NB-149-jordan-domination-reinstates-the-positive-poisson-log-budget.md), mesoscopic actual-zero occupation [NB-150](../../findings/NB-150-mesoscopic-horizontal-differencing-makes-both-poisson-lobes-logarithmically-zero-occupied.md), the fixed-scale two-point theorem [NB-151](../../findings/NB-151-fixed-scale-horizontal-differencing-forces-a-neighboring-logarithmic-adverse-packet.md), the bounded-variation many-point extension [NB-152](../../findings/NB-152-bounded-variation-fixed-horizontal-samplers-cannot-isolate-a-logarithmic-zero-packet.md), and the compact two-dimensional conditioning tradeoff [NB-153](../../findings/NB-153-compact-two-dimensional-samplers-export-zero-debt-on-the-conditioning-radius.md).

A zero-mass signed exterior sampler can cancel the universal leading Hadamard `(1/2)log G` term, but NB-148 shows the exact price: its zero-side Poisson kernel has zero vertical integral, so positive integrated mass is accompanied by equal negative integrated mass. Cancelling the scalar budget exchanges it for a **sign debt**. NB-149 shows that controlling this debt by Jordan or total variation merely re-enters the positive cone and restores a `Theta(log G)` budget.

NB-150 closes the obvious mesoscopic location strategy for a two-point horizontal difference: when `1<<L_G=o(G)`, ordinary zero density fills both lobes with logarithmic actual-zero mass while a target packet inside `o(L_G)` is diluted. NB-151 then closes the fixed-scale two-point geometry for a logarithmic target packet: exact horizontal `xi'/xi` conservation forces matching adverse zero charge into a bounded neighboring ordinate window.

NB-152 proves that the two-point factorization is not essential. For any zero-mass signed measure on a fixed compact horizontal interval, bounded coefficient variation per unit target charge `V_G/q_G` still forces `Omega(q_G log G)` adverse charge and `Omega(log G)` adverse zeros at bounded distance.

NB-153 closes two remaining loopholes simultaneously. Let the sampler live on any fixed compact set `K` of complex offsets with `Re w>0`, so bounded vertical as well as horizontal geometry is allowed, and put

`C_G=||mu_G||_TV/q_G`.

Zero mass still cancels the common completed-function background, compactness still gives quadratic ordinate decay, and the total signed zero charge remains `O_K(V_G)`. For a target packet of rank at least `kappa log G`, every family with `C_G=o(log G)` therefore carries

`A_G^- >= q_G(kappa log G-O_K(C_G))`.

A fixed fraction of this adverse debt lies within ordinate radius `O(C_G)`, and that window contains at least `Omega(log G/C_G)` adverse zeros. Bounded vertical offsets do not help; worsening conditioning merely trades adverse **population** for **displacement**. To reduce this conservation-forced population to `O(1)` while staying in a fixed compact exterior geometry requires at least `C_G=Omega(log G)`.

The relevant resource is thus the coefficient-variation budget per unit useful target charge. Adding more points, passing to continuous or genuinely two-dimensional compact clouds, or allowing sublogarithmic ill-conditioning does not evade the obstruction. The first conditioning scale not ruled out by this argument is logarithmic, but NB-153 does not say logarithmic conditioning is sufficient.

The surviving signed route must spend a genuinely different currency: logarithmic-or-worse conditioning together with source-side cancellation that keeps it useful, support that approaches `Re s=1`, horizontal/vertical support diameter that grows with height, or a target-aware Nyman/Euler coupling that preserves sign before the zero-side charges are separated.

**Boundary.** NB-150 is mesoscopic and density-driven. NB-151--NB-153 are target-conditioned completed-function conservation theorems. NB-153 assumes a fixed compact exterior offset set and gives a necessary conditioning/displacement tradeoff, not a sufficient construction at `C_G~log G`; it does not classify growing support, boundary-approaching clouds or signed prime/Nyman coupling, and assumes neither RH nor local zero-spacing asymptotics.
