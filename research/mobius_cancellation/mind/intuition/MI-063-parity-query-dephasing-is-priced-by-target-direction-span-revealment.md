# MI-063 — Parity-query dephasing is priced by target-direction span revealment

**Evidence level:** exact synthesis from [MC-338](../../findings/MC-338-information-energy-obstruction-for-reciprocal-source-dephasing.md) and [MC-367](../../findings/MC-367-parity-query-span-revealment-tariff.md). The linear-algebra mechanism is classical; the Mathia content is the exact punctured-cube correction and its endpoint dephasing consequence.

MC-366 showed that direct own-coordinate revealment is the exact acquisition currency for adaptive coordinate queries. MC-367 extends the same provenance principle to adaptive noiseless parity queries: what matters is not whether a query syntactically mentions coordinate `i`, but whether the target direction `e_i` enters the span of the queried parity vectors.

For the refined transcript `T_i` that includes the source-independent internal randomness, query path and answers, let `V_i^0` be the query span before target-direction revealment, `r_i^0=dim V_i^0`, and let `p_i^lin` be the probability that `e_i` enters the path span. Then the squared predictor has the exact decomposition

`rho_tilde_i^2 = p_i^lin + (1/(2^R-1)) E[ 1_{e_i notin V_i^0}/(2^(R-r_i^0)-1) ]`.

Any coarser observable obtained from that transcript has no larger predictor norm. The second term is the one-point puncture leakage; away from it, parity information that does not span `e_i` cannot predict the target phase.

For one common rank-`q` parity transcript this yields

`(1/R) sum_i rho_i^2 <= q/R + 1/((2^R-1)(2^(R-q)-1))`.

Combined with the reciprocal endpoint energy inequality, unit-energy exact all-source dephasing therefore requires full rank `q=R`. The acquisition currency has moved from coordinate incidence to **linear-span incidence** while retaining the same provenance logic.

The live arithmetic question is correspondingly narrower: determine whether a concrete Möbius-derived transcript admits a parity-sketch representation with subcritical target-direction span revealment. If it does, the endpoint obstruction becomes source-specific. If it uses genuinely nonlinear or dependent side information, a different provenance theorem is required.

**Boundary.** The full-rank conclusion is for a common transcript. Source-specific transcripts may target different coordinates separately and are not ruled out by rank alone. The theorem does not cover arbitrary nonlinear measurements, source-dependent latent choices, or hidden side channels, and it gives no estimate for `M(x)` by itself.