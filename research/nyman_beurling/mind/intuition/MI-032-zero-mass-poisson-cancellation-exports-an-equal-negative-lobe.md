# MI-032 — Cancelling the Hadamard log budget creates a sign debt; boundary approach only rescales the conditioning bill

**Evidence level:** exact signed-kernel conservation from [NB-148](../../findings/NB-148-cancelling-the-hadamard-log-budget-forces-an-equal-mass-negative-poisson-lobe.md), sharpened by the Jordan obstruction [NB-149](../../findings/NB-149-jordan-domination-reinstates-the-positive-poisson-log-budget.md), mesoscopic actual-zero occupation [NB-150](../../findings/NB-150-mesoscopic-horizontal-differencing-makes-both-poisson-lobes-logarithmically-zero-occupied.md), the fixed-scale two-point theorem [NB-151](../../findings/NB-151-fixed-scale-horizontal-differencing-forces-a-neighboring-logarithmic-adverse-packet.md), the bounded-variation many-point extension [NB-152](../../findings/NB-152-bounded-variation-fixed-horizontal-samplers-cannot-isolate-a-logarithmic-zero-packet.md), the compact two-dimensional conditioning tradeoff [NB-153](../../findings/NB-153-compact-two-dimensional-samplers-export-zero-debt-on-the-conditioning-radius.md), and the moving-boundary renormalization [NB-154](../../findings/NB-154-boundary-approach-renormalizes-signed-conditioning-by-the-line-one-gap.md).

A zero-mass signed exterior sampler can cancel the universal leading Hadamard `(1/2)log G` term, but NB-148 shows the exact price: its zero-side Poisson kernel has zero vertical integral, so positive integrated mass is accompanied by equal negative integrated mass. Cancelling the scalar budget exchanges it for a **sign debt**. NB-149 shows that controlling this debt by Jordan or total variation merely re-enters the positive cone and restores a `Theta(log G)` budget.

NB-150 closes the obvious mesoscopic location strategy for a two-point horizontal difference: when `1<<L_G=o(G)`, ordinary zero density fills both lobes with logarithmic actual-zero mass while a target packet inside `o(L_G)` is diluted. NB-151 then closes the fixed-scale two-point geometry for a logarithmic target packet: exact horizontal `xi'/xi` conservation forces matching adverse zero charge into a bounded neighboring ordinate window.

NB-152 proves that the two-point factorization is not essential. For any zero-mass signed measure on a fixed compact horizontal interval, bounded coefficient variation per unit target charge `V_G/q_G` still forces `Omega(q_G log G)` adverse charge and `Omega(log G)` adverse zeros at bounded distance.

NB-153 closes bounded two-dimensional compact geometry. On a fixed compact exterior set, with

`C_G=||mu_G||_TV/q_G`,

zero mass cancels the common completed-function background, compactness gives quadratic ordinate decay, and every `C_G=o(log G)` family still exports `Omega(q_G log G)` adverse charge. A fixed fraction lies within ordinate radius `O(C_G)` and requires at least `Omega(log G/C_G)` adverse zeros. Ill-conditioning can trade adverse **population** for **displacement**, but below logarithmic order it cannot remove the debt.

NB-154 shows that shrinking the horizontal gap does not by itself evade this mechanism. Let `a_G` be the minimum distance of the support from `Re w=0` and define the gap-normalized condition number

`D_G=C_G/a_G=||mu_G||_TV/(a_G q_G)`.

The Euler-product remainder grows like `V_G/a_G`, and the pointwise Poisson charge is bounded on the same scale. Thus the boundary amplification that can increase useful target charge also increases the source-side remainder and maximum adverse charge. Whenever `D_G=o(log G)`, the sampler still exports `Omega(q_G log G)` adverse charge, a fixed fraction remains within ordinate radius `O(1+C_G)`, and at least `Omega(log G/D_G)` adverse zeros are needed.

The resource is therefore not raw proximity to `Re s=1`, nor raw coefficient variation, but coefficient variation **after normalization by the available boundary amplification**. A family with `C_G=O(a_G)` remains effectively well-conditioned (`D_G=O(1)`) and still forces logarithmically many nearby adverse zeros. The first boundary-normalized scale not ruled out by this argument is `D_G~log G`, but that is a boundary of the method, not evidence of an isolating sampler.

The surviving signed route must spend a genuinely different currency: logarithmic-or-worse gap-normalized conditioning together with useful source-side cancellation, support diameter that grows with height, or a target-aware Nyman/Euler coupling that preserves sign before the zero-side charges are separated.

**Boundary.** NB-150 is mesoscopic and density-driven. NB-151--NB-154 are target-conditioned completed-function conservation theorems. NB-154 allows the compact support to approach `Re w=0` but keeps horizontal width and vertical diameter uniformly bounded and uses the absolute `1/a_G` Euler estimate. It does not classify growing support, logarithmically gap-conditioned constructions, or sharper signed prime-side cancellation, and assumes neither RH nor local zero-spacing asymptotics.
