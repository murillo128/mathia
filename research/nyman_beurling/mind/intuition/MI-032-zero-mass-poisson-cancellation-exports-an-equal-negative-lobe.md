# MI-032 — Cancelling the universal Hadamard log budget exports an equal negative Poisson lobe

**Evidence level:** exact signed-kernel conservation law from [NB-148](../../findings/NB-148-cancelling-the-hadamard-log-budget-forces-an-equal-mass-negative-poisson-lobe.md), complementing the positive reflection-closure classification NB-147.

Positive exterior Poisson sampling has a rigid advantage: every zero contributes with one sign, but the universal Hadamard/archimedean term consumes a leading `(1/2)log G` budget. A natural escape is to use a signed exterior sampler `nu` with total mass zero so that the leading universal term cancels.

NB-148 shows the exact price of that cancellation. The corresponding zero-side Poisson kernel `K_(nu,beta)` has vertical integral

`integral K_(nu,beta)(t) dt = pi M_nu`,

where `M_nu` is the total signed mass of the sampler. Thus `M_nu=0` forces the kernel itself to have zero total mass. If its positive lobe has integrated mass `A`, its negative lobe has integrated mass exactly `A` as well.

Under the quantitative width/total-variation condition used in NB-148, zero mass really does remove the leading logarithmic Hadamard budget on the relevant local window. But it cannot preserve the positive zero-side comparison at the same time. The universal term has been cancelled by exchanging a scalar budget for a **sign debt**: every useful positive target lobe exports equally much negative kernel mass elsewhere.

This turns “try signed sampling” into a concrete source question. A signed route can only improve the positive reflection-closure barrier if another theorem controls the zeros seen by the negative lobe, or if prime-side cancellation pays for that lobe without reintroducing a target-equivalent assumption. Merely choosing more oscillatory coefficients cannot create net positive zero mass after the universal logarithmic term has been removed.

**Boundary.** The conservation law constrains the integrated signed Poisson kernel, not its detailed pointwise shape. It does not rule out a sampler whose negative lobe lands in a region where actual zeta zeros are independently controlled, nor a prime-side identity that compensates it. Those are now the precise missing resources.