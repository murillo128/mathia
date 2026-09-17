# MI-028 — Uniform state boundedness collapses the first-prime gate

**Evidence level:** exact synthesis from [PL-329](../../findings/PL-329-source-amplitude-gate-for-first-prime-reflection.md) through [PL-337](../../findings/PL-337-prime-shift-jump-boundedness.md). The state bound that was conditional in PL-336 is proved on compact aperture/eigenvalue ranges in PL-337.

PL-329 expresses the moving first-prime sign problem through the endpoint-source amplitude `S_delta`, the selected critical coefficient `C_delta`, and the half-log scale `L_delta`. PL-336 showed that these apparently separate quantities would become controlled together under one concrete state-space hypothesis: a uniform `L^infty` bound on the normalized simple odd eigenbranch as `delta->0`.

PL-337 supplies that hypothesis. Rewriting each active prime translation as a positive atomic jump Dirichlet form plus a bounded scalar shift allows the weakly singular logarithmic-Laplacian boundedness argument to survive the prime-power activation jumps. On every compact aperture interval and bounded eigenvalue window, normalized eigenstates are uniformly bounded in `L^infty`.

The exact completed-Weil eigen-equation then gives `S_delta=O(1)`. The source equation supplies the family-uniform half-log boundary envelope and endpoint remainder required by PL-329/PL-332; norm-resolvent transport gives `C_delta->C_0`; and PL-335's odd reflected Hopf mechanism gives `C_0>0` on the lowest odd threshold branch. Consequently

`(1+S_delta)/(|C_delta| sqrt(L_delta)) -> 0`,

so the PL-329 source-amplitude gate is actually closed and the first-prime reflected correlation has the favorable sign for sufficiently small `delta` on that branch.

The reusable lesson is that a moving-boundary forcing problem can collapse to a norm of the **state that generates the forcing** when the operator admits an appropriate positive jump-form representation. A state-space bound can simultaneously control source amplitude, endpoint remainder and branch transport even when fixed logarithmic seminorms miss the hostile compressed layer.

**Boundary.** This closes the first-prime concentration obstruction, not the full arithmetic activation problem. Later prime-power activations can introduce independent correlation-sign and branch-ordering questions, and no claim is made that the completed operator generates a globally positivity-preserving semigroup. The result is not an RH proof or a global branch-existence theorem.