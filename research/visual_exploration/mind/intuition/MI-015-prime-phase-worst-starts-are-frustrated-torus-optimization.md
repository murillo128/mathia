# MI-015 — Prime-phase worst starts are a torus optimization with a fractional cycle-frustration certificate

**Evidence level:** exact finite-dimensional reduction from [VIS-213](../../findings/VIS-213-worst-start-prime-phase-torus-optimization.md), exact holonomy criterion from [VIS-214](../../findings/VIS-214-cycle-holonomy-frustration-envelope.md), and exact weighted fractional-packing lower bound from [VIS-215](../../findings/VIS-215-weighted-cycle-frustration-packing.md). No asymptotic lower bound for the actual prime graph, useful recurrence-time bound, or RH consequence is claimed.

For fixed `y,H`, the start variable traces a dense prime-phase torus and

`sup_(T>=T_0)|M_v(y;H,T)-1| = max_(|z_p|=1)|z^*A_(y,H)z|`.

Thus coherent pointwise starts are a finite torus optimization problem, not an existence problem. The long-start variance gives the Haar `L^2` scale of the same objective but does not determine whether the optimum is close to the absolute coefficient envelope.

VIS-214 identifies the exact gauge-invariant obstruction. Vertex phases can switch edge phases, so raw preferred phases are not invariant; products around support cycles are. Exact positive or negative envelope attainment is equivalent to the corresponding cycle holonomies being trivial.

VIS-215 quantifies distributed frustration. With edge weights `w_e`, cycle harmonic resistance

`R(C)=sum_(e in C)1/w_e`,

and positive/negative holonomy `H_±(C)`, every torus point satisfies

`E_± >= |1-H_±(C)|^2/R(C)`.

More importantly, for any fractional cycle packing `lambda_C>=0` obeying `sum_(C contains e)lambda_C<=1`, the cycle rewards add:

`E_± >= sum_C lambda_C |1-H_±(C)|^2/R(C)`.

Let `P_±` be the optimal values of these linear programs. Then

`max_z |z^*Az| <= B(A)-min(P_+,P_-)`.

This replaces “find one frustrated cycle” with a concrete global certificate. Shared edges cannot be counted twice beyond their capacity, while many overlapping short cycles can contribute fractionally. For an equal-weight `k`-cycle at small holonomy, the one-cycle reward scales like `w h^2/k`, improving the earlier minimum-edge `w h^2/k^2` certificate before any packing gain is used.

The live arithmetic question is now precise: determine the scale of `P_+` and `P_-` for the actual prime coefficient graph and compare it with both the coefficient envelope and Haar RMS. Only after that static geometry is understood does the separate one-parameter access-time problem matter.

**Boundary.** Fractional packing is a lower bound on unavoidable frustration, not an exact formula for the torus optimum. Trees give zero certificate as they should. The cycle/synchronization framework is classical; the current content is its exact normalization for the prime-phase objective and the source-specific asymptotic question it exposes.
