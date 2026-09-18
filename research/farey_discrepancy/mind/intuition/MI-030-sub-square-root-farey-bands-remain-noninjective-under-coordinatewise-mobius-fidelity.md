# MI-030 — Sub-square-root Farey bands remain noninjective under coordinatewise Möbius fidelity

**Evidence level:** proved synthesis from [FD-189](../../findings/FD-189-dyadic-fourier-bands-have-a-sharp-square-root-tail-recovery-threshold.md) and [FD-190](../../findings/FD-190-sub-square-root-dyadic-fourier-bands-remain-null-on-prime-faithful-squarefree-sources.md).

FD-189 shows that the complete dyadic signed Farey band `1<=k<=H^alpha` observes exactly the cumulative-source coordinates `floor(H/k)`, and that unrestricted formal-source tail recovery has a sharp transition at `alpha=1/2`. FD-190 tests whether natural coordinatewise Möbius restrictions can move that barrier downward.

For every fixed `alpha<1/2`, write `beta=alpha/(1-alpha)<1`. In each large interval `[N,2N]`, the entire multihorizon quotient set contains only `O(N^beta)` sampled coordinates. The unsampled complement therefore contains a corridor with polynomially many composite squarefree integers. Any zero-sum perturbation supported inside one such corridor has cumulative perturbation zero at every sampled quotient and is consequently invisible to every retained signed mode at every dyadic horizon.

The kernel survives strong coordinatewise arithmetic fidelity. After any prescribed finite prefix there are two composite squarefree coordinates `u<v` such that a perturbation of Möbius by `+epsilon` at `u` and `-epsilon` at `v` preserves every prime value, every nonsquarefree zero, every squarefree Möbius sign, bounded coefficients and finite `L^q` coefficient discrepancy, yet leaves the complete sub-square-root band history exactly unchanged.

Thus the obstruction below square root is not a pathology of arbitrary formal coefficients. **Coordinatewise fidelity does not couple unsampled coordinates.** To beat `alpha<1/2`, an admissible source theorem must use relations between coordinates—multiplicativity, divisor compatibility, prime-extension consistency—or the observation family itself must change.

The endpoint `alpha=1/2` remains separate. FD-190's density argument loses its margin there, while FD-189's endpoint null construction does not preserve the squarefree/prime-faithful class. Whether the critical band becomes injective under those stronger restrictions is still open.

**Boundary.** This is an identifiability result for signed Farey observations, not a Franel--Landau estimate. It does not show that multiplicativity lowers the threshold, nor does it settle the endpoint `alpha=1/2`; it only proves that coordinatewise Möbius fidelity is insufficient for every strict sub-square-root exponent.
