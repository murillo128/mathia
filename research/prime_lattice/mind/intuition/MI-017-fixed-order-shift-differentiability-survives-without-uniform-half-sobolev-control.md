# MI-017 — Uniform BV transports the pure zero-order shift derivative without a half-Sobolev bound

**Evidence level:** supported by [PL-297](../../findings/PL-297-renormalized-hadamard-stress-hhalf-decoupling.md), [PL-298](../../findings/PL-298-fixed-order-fractional-shift-autocorrelation-c1.md) and [PL-299](../../findings/PL-299-uniform-bv-principal-shift-derivative-limit.md). The corresponding compactness for the actual completed-Weil eigenbranch remains open.

PL-297 separates two singular resources in the small-order fractional control. The renormalized boundary stress has a finite nonzero limit while the zero extensions satisfy

`||E u_s||_(H^(1/2)) -> infinity`.

So a finite Hadamard stress does not imply the critical Fourier first moment used by routine absolute differentiation. PL-298 nevertheless shows that every fixed `s>0` has a `C^1` translation autocorrelation through physical-space `W^(1,1) cap L^infty` regularity.

PL-299 closes the remaining `s->0+` passage for the pure principal branch by a different compactness currency. On the centered interval the positive principal eigenfunctions are even and decreasing; uniform `L^infty` control gives

`TV(u_s)=2u_s(0)=O(1)`,

while the small-order theory gives uniform convergence `u_s->u_0`. For continuous compactly supported states, uniform convergence plus a uniform BV bound implies convergence of the autocorrelations in `C^1`. Hence

`C_s -> C_0 in C^1(R)`

uniformly in the lag, including across support-edge activation.

The key distinction is that `H^(1/2)` controls an absolute Fourier first moment, whereas BV controls the derivative as a finite measure and lets the convolution transport that measure against a uniformly convergent continuous state. The former can diverge while the latter remains compact. Therefore failure of the half-Sobolev route is not evidence that the zero-order prime-shift derivative is singular.

The live theorem is now source-specific: establish the same effective compactness for the **regularized completed-Weil eigenbranch**, where a bounded perturbation may destroy positivity and monotonicity. Uniform `C_0` convergence plus uniform BV would suffice; another finite-measure derivative compactness may also suffice if it yields the same autocorrelation transport. Completion/remainder differentiation and the independent ground-state sign gate still have to be handled separately.

**Boundary.** PL-299 proves this only for the pure principal fractional/logarithmic branch. It does not show uniform BV for the arithmetic perturbation, preserve cone membership, determine the sign of the shift derivative, or complete the full Feynman--Hellmann/Weil differentiation.
