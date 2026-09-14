# MI-015 — Pointwise worst starts are a prime-phase torus optimization whose exact envelope is controlled by cycle holonomy

**Evidence level:** exact finite-dimensional reduction from [VIS-213](../../findings/VIS-213-worst-start-prime-phase-torus-optimization.md) and exact gain-graph envelope criterion from [VIS-214](../../findings/VIS-214-cycle-holonomy-frustration-envelope.md). No asymptotic lower bound beyond the RMS scale, useful recurrence-time bound, or RH consequence is claimed.

For fixed `y,H`, the tapered statistic satisfies

`M_v(y;H,T)-1 = z(T)^* A_(y,H) z(T)`, `z_p(T)=exp(iT log p)`.

Unique factorization makes the finite prime logarithms rationally independent, so the one-parameter flow is dense in the full prime torus. Therefore

`sup_(T>=T_0) |M_v(y;H,T)-1| = max_(|z_p|=1) |z^*A_(y,H)z|`

for every fixed starting threshold `T_0`. Pointwise coherent starts are not an existence problem at fixed dimension: every torus neighborhood of a maximizer is revisited arbitrarily late. The real questions are the **size of the torus optimum as `y,H` grow** and the Diophantine access time needed to enter a near-maximizing region.

The long-start variance is the Haar `L^2` norm of the same torus objective, so the optimum is at least `sqrt(R_v(y,H))`; in the strictly subcritical regime this is `\gtrsim H^-1/2`. That lower bound does not say whether coherent optimization produces order-one or otherwise macroscopic amplification.

VIS-214 identifies the exact obstruction to attaining the absolute coefficient envelope. Write each nonzero Hermitian edge coefficient as `w_uv exp(i theta_uv)`. Vertex phases are a gauge action on the edge phases. The positive coefficient envelope is attained iff every cycle has zero holonomy; the negative envelope is attained iff every cycle has the corresponding all-negative holonomy. Otherwise the envelope is strictly unattainable. A cycle `C` with holonomy defect `h_+(C)` gives the explicit positive deficit

`B(A)-G(z) >= 2 m(C) [1-cos(h_+(C)/|C|)]`,

and analogously for the negative envelope.

Thus the invariant geometry is not the raw preferred phase on an edge but **weighted cycle holonomy after vertex-gauge quotient**. A large torus optimum requires substantial edge weight to remain nearly globally switchable; visible phase disorder on small-weight cycles is irrelevant. Conversely, one heavy frustrated cycle supplies a rigorous coherent-amplification deficit.

The next quantitative theorem should therefore compare a weighted holonomy/frustration scale with the Haar RMS scale and with the relevant recurrence horizon. This cleanly separates three resources: coefficient mass, gauge-invariant frustration, and one-parameter access time.

**Boundary.** Unit-modulus quadratic programming, Kronecker--Weyl recurrence, gain-graph balance and switching are classical. The line-specific content is their exact identification with the actual prime-ratio statistic and its coefficient normalization.