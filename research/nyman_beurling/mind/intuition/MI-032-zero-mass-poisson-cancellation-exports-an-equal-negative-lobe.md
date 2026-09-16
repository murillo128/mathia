# MI-032 — Cancelling the Hadamard log budget creates a sign debt; boundary approach and sublinear vertical spread only move its conditioning radius

**Evidence level:** exact signed-kernel conservation from [NB-148](../../findings/NB-148-cancelling-the-hadamard-log-budget-forces-an-equal-mass-negative-poisson-lobe.md), sharpened by the Jordan obstruction [NB-149](../../findings/NB-149-jordan-domination-reinstates-the-positive-poisson-log-budget.md), mesoscopic actual-zero occupation [NB-150](../../findings/NB-150-mesoscopic-horizontal-differencing-makes-both-poisson-lobes-logarithmically-zero-occupied.md), the fixed-scale two-point theorem [NB-151](../../findings/NB-151-fixed-scale-horizontal-differencing-forces-a-neighboring-logarithmic-adverse-packet.md), the bounded-variation many-point extension [NB-152](../../findings/NB-152-bounded-variation-fixed-horizontal-samplers-cannot-isolate-a-logarithmic-zero-packet.md), the compact two-dimensional conditioning tradeoff [NB-153](../../findings/NB-153-compact-two-dimensional-samplers-export-zero-debt-on-the-conditioning-radius.md), the moving-boundary renormalization [NB-154](../../findings/NB-154-boundary-approach-renormalizes-signed-conditioning-by-the-line-one-gap.md), and the growing-vertical-support extension [NB-155](../../findings/NB-155-sublinear-vertical-support-growth-only-enlarges-the-adverse-localization-radius.md).

A zero-mass signed exterior sampler can cancel the universal leading Hadamard `(1/2)log G` term, but NB-148 shows the exact price: its zero-side Poisson kernel has zero vertical integral, so positive integrated mass is accompanied by equal negative integrated mass. Cancelling the scalar budget exchanges it for a **sign debt**. NB-149 shows that controlling this debt by Jordan or total variation merely re-enters the positive cone and restores a `Theta(log G)` budget.

NB-150 closes the obvious mesoscopic location strategy for a two-point horizontal difference: when `1<<L_G=o(G)`, ordinary zero density fills both lobes with logarithmic actual-zero mass while a target packet inside `o(L_G)` is diluted. NB-151 then closes the fixed-scale two-point geometry for a logarithmic target packet: exact horizontal `xi'/xi` conservation forces matching adverse zero charge into a bounded neighboring ordinate window.

NB-152 proves that the two-point factorization is not essential. For any zero-mass signed measure on a fixed compact horizontal interval, bounded coefficient variation per unit target charge `V_G/q_G` still forces `Omega(q_G log G)` adverse charge and `Omega(log G)` adverse zeros at bounded distance.

NB-153 closes bounded two-dimensional compact geometry. On a fixed compact exterior set, with

`C_G=||mu_G||_TV/q_G`,

zero mass cancels the common completed-function background, compactness gives quadratic ordinate decay, and every `C_G=o(log G)` family still exports `Omega(q_G log G)` adverse charge. A fixed fraction lies within ordinate radius `O(C_G)` and requires at least `Omega(log G/C_G)` adverse zeros. Ill-conditioning can trade adverse **population** for **displacement**, but below logarithmic order it cannot remove the debt.

NB-154 shows that shrinking the horizontal gap does not by itself evade this mechanism. Let `a_G` be the minimum distance of the support from `Re w=0` and define the gap-normalized condition number

`D_G=C_G/a_G=||mu_G||_TV/(a_G q_G)`.

The Euler-product remainder grows like `V_G/a_G`, and the pointwise Poisson charge is bounded on the same scale. Thus boundary amplification increases useful target charge, source-side remainder and maximum adverse charge together. Whenever `D_G=o(log G)`, the sampler still exports `Omega(q_G log G)` adverse charge and needs at least `Omega(log G/D_G)` adverse zeros.

NB-155 removes the bounded-vertical-diameter qualifier. Let the support have vertical half-width `B_G=o(G)` while retaining horizontal width bounded by a fixed `A`. The completed-function cancellation remains

`sum_rho Q_G(rho)=O_A(V_G/a_G)`,

so the same `D_G=o(log G)` threshold forces the same logarithmic adverse charge. The only change is where the debt can be hidden: for a constant `M=M(A,kappa)`, a fixed fraction lies inside

`|gamma-G| <= R_G`,  with  `R_G=2B_G+4+M C_G=o(G)`,

and that window still contains `Omega(log G/D_G)` adverse zeros. **Sublinear vertical spreading transports the sign debt by `O(B_G)` but does not dilute its population or improve the gap-normalized conditioning threshold.**

The resource is therefore not raw proximity to `Re s=1`, raw coefficient variation, or merely allowing the sampler cloud to widen. It is coefficient variation after normalization by boundary amplification, together with the ordinate scale on which compensation can be displaced. A family with `D_G=O(1)` remains effectively well-conditioned even if `B_G->infinity` sublinearly, and still forces logarithmically many adverse zeros inside an `o(G)` window.

The surviving signed route must spend a genuinely different currency: logarithmic-or-worse `D_G`, vertical support on a scale no longer `o(G)`, signed prime-side cancellation sharper than the absolute Euler bound, or a target-aware Nyman/Euler coupling that preserves sign before the zero-side charges are separated. The thresholds `D_G~log G` and `B_G~G` are boundaries of these arguments, not evidence that an isolating sampler exists there.

**Boundary.** NB-150 is mesoscopic and density-driven. NB-151--NB-155 are target-conditioned completed-function conservation theorems. NB-155 permits the compact support to approach `Re w=0` and its vertical diameter to grow sublinearly in `G`, but keeps bounded horizontal extent and uses the absolute `1/a_G` Euler estimate. It does not classify order-`G` vertical spread, logarithmically gap-conditioned constructions, sharper signed prime-side cancellation, or direct target-bearing Nyman/prime coupling, and assumes neither RH nor local zero-spacing asymptotics.
