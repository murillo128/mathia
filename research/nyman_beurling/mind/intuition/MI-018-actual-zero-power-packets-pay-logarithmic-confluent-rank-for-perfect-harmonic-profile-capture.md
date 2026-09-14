# MI-018 — Actual zero-power packets pay a rootwise rank--height budget for near-perfect harmonic capture

**Evidence level:** exact consequence of [NB-123](../../findings/NB-123-perfect-target-capture-by-a-finite-zero-packet-requires-logarithmic-confluent-rank.md)--[NB-125](../../findings/NB-125-rootwise-annihilator-margins-turn-near-perfect-capture-into-a-vinogradov-korobov-height-budget.md), using the target equality/energy characterization of NB-117 and the explicit Vinogradov--Korobov zero-free region quoted in NB-125. No RH consequence or full coupling to the continuum high-zero compression bound is claimed.

NB-123 identifies the exact separator coming from the actual zero-power representation. For a finite packet `F` with total confluent multiplicity `d`, geometric sampling produces a finite exponential-polynomial sequence with characteristic roots `q^(-conj(rho))`. Perfect target capture requires the missing harmonic root `q^-1`, which no nontrivial zeta zero supplies; exact capture therefore needs logarithmically growing recurrence rank.

NB-124 stabilizes this without parameter inversion. With annihilator

`A_(F,q)(z)=product_(rho in F)(z-q^(-conj(rho)))=sum a_j z^j`,

its normalized missing-root margin

`mathfrak s_(F,q)=(1-q^-1)|A_(F,q)(q^-1)|^2 / sum_j |a_j|^2 q^-j`

controls the target angle directly in the Nyman cell metric. Every fixed finite actual packet has `mathfrak s_(F,q)>0` and hence a cutoff-uniform gap from perfect capture.

NB-125 preserves the product structure that the coarse `beta_F=max Re rho` estimate discarded. If `r=q^-1` and `D_q=(log q)/(2sqrt q)`, then

`mathfrak s_(F,q) >= (1-r) product_(rho in F) ((q^(-beta)-r)/(q^(-beta)+sqrt r))^2`

and therefore

`mathfrak s_(F,q) >= (1-r)D_q^(2d) product_(rho in F)(1-beta)^2`.

This is a structural improvement: each zero is charged only for its own horizontal depth. One exceptionally rightward zero can no longer be charged `d` times and hide the rest of the packet.

If `chi_(F,R)>=1-epsilon`, the stable target-angle bound implies an aggregate horizontal-depth requirement

`sum_(rho in F) log 1/(1-beta) >= (1/2)log(((1-r)(1-epsilon))/(L_R epsilon)) - d log D_q^-1`.

For actual zeta zeros, the explicit Vinogradov--Korobov zero-free region converts each horizontal depth into ordinate height. In the polynomial accuracy regime `epsilon=R^-alpha`, one obtains the additive budget

`(alpha/2)log R <= d log(K_VK/D_q) + (2/3)sum loglog|gamma| + (1/3)sum logloglog|gamma| + O_q(1)`.

Rank and height are therefore fungible only through this explicit price. If every ordinate is at most `R^C`, then near-perfect capture forces

`d(F) >= (3alpha/4+o(1)) log R/loglog R`.

Conversely, if `d` stays fixed, the maximum height must satisfy

`H >= exp(R^(3alpha/(4d)-o(1)))`.

The remaining escape is no longer “rank or horizontal approach” as two independent knobs. Horizontal approach itself must be purchased by height, root by root. The packet can evade the fixed-rank margin only by accumulating enough **rank-weighted height entropy**.

This points directly at the unsolved interface with NB-116. That result says a packet whose source information lives only above height `G` reaches the finite target through a compression channel with retention `O(1/G+1/R)`. NB-125 says near-perfect finite target capture needs enough aggregate height entropy. A closing theorem should show that the required entropy cannot be distributed among actual zeros without simultaneously making the target-bearing compression too weak, or derive a quantitative retention lower bound from the same packet entropy.

**Boundary.** NB-125 does not control minimum height from maximum height, does not by itself lower-bound the NB-116 compression eigenvalues, and does not exclude packets mixing moderate and extremely high zeros. The Vinogradov--Korobov input is one-sided and may not be optimal. The durable resource is the rootwise annihilator margin plus its additive rank--height budget, not generic zero separation or recurrence rank alone.