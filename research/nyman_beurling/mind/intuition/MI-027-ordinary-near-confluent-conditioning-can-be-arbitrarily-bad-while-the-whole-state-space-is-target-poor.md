# MI-027 — Ordinary near-confluent conditioning can be arbitrarily bad while the whole state space is target-poor

**Evidence level:** exact finite-window matched-control splice from [NB-137](../../findings/NB-137-superill-conditioned-simple-clusters-can-converge-to-a-target-poor-confluent-state-space.md), combining the confluent state-space geometry of NB-108--NB-111 with the simple-cluster conditioning obstruction NB-136

NB-136 shows that distinct simple packets can make the ordinary natural-prefix power basis superpolynomially ill-conditioned. NB-137 identifies why that alone cannot be interpreted as target difficulty: the bad conditioning can be a coordinate singularity that survives even when the **entire represented state space is asymptotically irrelevant to the canonical Nyman target**.

A growing simple cluster can be chosen arbitrarily close in the Grassmannian to the confluent jet state space obtained by coalescing its ordinates. Under the same coarse zero-count and zero-free-region envelopes used by NB-133--NB-136, one can arrange simultaneously

`kappa_2(V_G) >= exp((c+o(1))(log G)^4)`

and

`||P_(S_G^split)e_G||^2 / ||e_G||^2 -> 0`.

Thus an enormous condition number may say mostly that the ordinary Vandermonde/power coordinates are a bad chart near confluence. Passing to divided-difference or jet coordinates can remove that coordinate singularity, yet it does not create target capture: the limiting confluent subspace itself can remain target-poor.

The correct object is therefore not `sigma_min(V)` in isolation but the pair **state-space geometry + target occupation**. A useful source theorem must either force the actual zero packet away from target-poor confluent Grassmann limits or prove that the Nyman target has a quantitatively nonvanishing projection onto the admitted packet space. Better coordinates can repair numerical conditioning without repairing relevance.

**Boundary.** NB-137 is a matched finite-window construction, not an assertion about actual zeta-zero clusters. It does not say confluent coordinates are useless; it says they must be audited against target projection rather than accepted because they regularize an ill-conditioned simple basis.