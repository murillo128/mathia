# MI-027 — Polynomially near-confluent simple clusters can be target-poor despite catastrophic ordinary conditioning

**Evidence level:** exact finite-window matched-control splice from [NB-137](../../findings/NB-137-superill-conditioned-simple-clusters-can-converge-to-a-target-poor-confluent-state-space.md), made quantitatively polynomial by [NB-138](../../findings/NB-138-polynomially-tight-simple-clusters-inherit-the-target-poor-confluent-barrier.md), combining the confluent state-space geometry of NB-108--NB-111 with the simple-cluster conditioning obstruction NB-136

NB-136 shows that distinct simple packets can make the ordinary natural-prefix power basis superpolynomially ill-conditioned. NB-137 identifies why that alone cannot be interpreted as target difficulty: the bad conditioning can be a coordinate singularity that survives even when the **entire represented state space is asymptotically irrelevant to the canonical Nyman target**.

NB-137 originally used an existentially small split spacing to make the simple cluster Grassmann-close to its confluent jet space. NB-138 removes that escape. For logarithmic packet rank `d_G=floor(c log G)`, a uniform holomorphic tube and Laguerre-normalized coercivity give an explicit perturbation bound. If

`epsilon_G G^(c log D_a) (log G)^(25/2) -> 0`,  with `D_a=4/a-3`,

then the normalized projection of the Nyman target onto the split simple-state span still tends to zero. In particular every fixed polynomial spacing

`epsilon_G=G^(-B)`,  `B>c log D_a`,

already inherits the target-poor confluent limit.

At the same time, under the same coarse local zero-count envelope used by the preceding controls, the ordinary natural-prefix zero-power matrix can satisfy

`log kappa_2(V_G) >= (cB+o(1))(log G)^2`.

Thus the coexistence of catastrophic raw conditioning and vanishing target access does not require a fantastically small or nonquantified confluence scale. It persists inside an explicit polynomial phase cell.

The correct object is therefore not `sigma_min(V)` or nearest-neighbour spacing in isolation but the pair **state-space geometry + target occupation**. Passing to divided-difference or jet coordinates can regularize the chart while leaving the represented subspace target-poor. Conversely, ruling out only superexponentially tight clusters cannot rescue the route; the source theorem must exclude the polynomial target-poor confluence regime or establish nonvanishing target occupation directly.

**Boundary.** NB-137--NB-138 are matched finite-window constructions under coarse zero-count/zero-free envelopes, not assertions that actual zeta zeros form such polynomial clusters. They do not say confluent coordinates are useless; they show that coordinate conditioning and target relevance are distinct, even at explicit polynomial separation.