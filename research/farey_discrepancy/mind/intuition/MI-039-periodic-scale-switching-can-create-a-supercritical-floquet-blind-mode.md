# MI-039 — Switched-block blindness survives exact full-divisor repair only in the base-anchored non-exhaustive source model

**Evidence level:** exact/literature-backed synthesis from [FD-212](../../findings/FD-212-period-three-diagonal-root-depth-creates-a-source-realizable-supercritical-floquet-blind-ray.md) through [FD-225](../../findings/FD-225-exact-divisor-inversion-removes-triangular-conditioning-from-switched-repair.md), interpreted against the fixed-family dichotomy of FD-210--FD-211.

The periodic schedule `q_j=(0,3,3)` has a physical super-square-root Floquet blind mode even though each instantaneous annihilator has only the harmless root `1`. FD-212--FD-221 show that exact Möbius Euler laws, bounded scheduled observations and a macroscopic earlier-prefix defect can coexist across arbitrarily long fixed blocks until a later Euler window literally covers every prime coordinate affecting the original prefix.

FD-222 proves that the obstruction survives every `J<=C log log N`. FD-223 shows that log-log growth was only the consequence of deliberately weak analytic input. Put `Phi(N)=(log N)^(3/5)/(log log N)^(1/5)`. For every fixed `0<beta<1`, there is `kappa_beta>0` such that every `J<=kappa_beta Phi(N)` admits one deterministic squarefree comparison source satisfying all Euler relations for the **fixed absolute cutoff** `p<=beta N`, with `D asymp 2^J` and a macroscopic earlier defect `X_N(N) asymp_beta N/(D log N)`.

FD-225 removes the remaining apparent switched-matrix cost in that range. The complete divisor-reservoir response operator

`(A c)(m)=sum_(d<=m) c_d M(floor(m/d))`

has the exact integer inverse

`c(n)=sum_(d|n)(y(d)-y(d-1))`.

Using all divisor reservoirs rather than one pivot reservoir per switched row, one can flatten every sampled prefix `X_N(mN)`, `1<=m<=D`, to one common value up to unit rounding error. Every scheduled observation is then `O(1)` while `X_N(N)=N^(1-o(1))`. The previous `17^J` triangular-conditioning factor was therefore a repair artifact, not an intrinsic capacity obstruction.

What remains at the current quantitative frontier is the floor-stable reservoir/source budget. The certified construction still requires roughly

`D^2 D^(o(1)) exp(-c Phi(N)) -> 0`,

coming from shrinking prime reservoirs and the physical Mertens baseline. Reaching the edge of the Vinogradov--Korobov estimate is thus still only a method boundary unless one proves that every admissible non-exhaustive repair must pay a comparable capacity cost.

FD-224 fixes the quantifier boundary that none of these constructions crosses. Exact global Euler windows at several horizons collapse to their union, hence to the maximal cutoff `Y_*`. If each dyadic horizon `H_j=2^jN` carries the same positive fractional coverage `Y_j=theta H_j`, then the original prefix becomes literally Möbius once `theta 2^(J-1)>=1`. A single permanent source satisfying exhaustive exact-Euler windows along any cofinal family is pointwise `mu`. These are source-identification statements, not coercivity supplied by the switched filter.

The reusable distinction is therefore between **base-anchored absolute coverage**, **repair capacity**, and **horizon-relative/cofinal coverage**. FD-225 shows that low-rank or badly conditioned switched response is not the obstruction. FD-224 shows that exhaustive exact source coherence eventually removes the relaxed source altogether. Any stronger blind construction must bypass the remaining reservoir/baseline cost while keeping the source genuinely non-exhaustive; any positive theorem must identify a structural capacity or physical-source mechanism rather than mistaking either analytic exhaustion or source identification for filter coercivity.

**Boundary.** FD-225 proves neither blindness beyond a fixed multiple of `Phi(N)` nor sharpness of the remaining `D^2` budget. FD-224 uses exact global prime relations; its union collapse need not survive averaged, local-in-`n`, probabilistic or approximate fidelity. No counterexample to Möbius cancellation or RH is produced.