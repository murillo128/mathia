# MI-039 — Periodic scale switching creates a supercritical blind mode that survives horizon-local Euler coherence

**Evidence level:** exact synthesis from [FD-212](../../findings/FD-212-period-three-diagonal-root-depth-creates-a-source-realizable-supercritical-floquet-blind-ray.md) through [FD-216](../../findings/FD-216-logarithmically-growing-euler-coherence-remains-horizon-locally-blind.md), interpreted against the fixed-family dichotomy of FD-210--FD-211.

Let `Delta_A(n)=A(2n)-A(n)` and observe one dyadic root filter at each scale. FD-212 takes the periodic depth schedule `q_j=(0,3,3)` on powers of two. Each instantaneous annihilator has only the harmless root `1`, and the fixed family has gcd `1`, yet the ordered period-three transfer has multiplier

`lambda=-(7+3sqrt(5))/2=-phi^4`,

whose per-step modulus `rho=phi^(4/3)` satisfies `sqrt(2)<rho<2`. The nonautonomous recurrence therefore supports a physical super-square-root Floquet mode at bounded filter depth and critical random cost.

FD-213 shows that this is not merely a sparse-ray artifact. Dyadic dilation preserves the mantissa `t(n)=n/2^floor(log_2 n)`, so a scale-index Floquet mode can be tensored with a boundary-vanishing Lipschitz profile and stitched into one bounded-increment source whose selected switched filter vanishes at every integer while `|A(N_m)| asymp N_m^alpha`, `alpha≈0.9256558848>1/2`.

FD-214 and FD-215 show that substantial arithmetic source fidelity can still be layered onto the same blind mechanism: exact squarefree support, exact unit amplitudes, and every fixed finite collection of Möbius Euler sign laws can be preserved. FD-216 makes the finite-versus-global boundary quantitative. For every fixed

`0<c<1/(2 log 2)`,

there is a deterministic **horizon-indexed** family whose member at scale `N` satisfies the exact Euler law at the first `k=floor(c log N)` primes, yet the switched observation is sub-square-root on the target window while the summatory value remains `N^(alpha-o(1))`. The complete comparison error is governed by

`N^beta G_(1/2)(P)G_beta(P) + 2^k`,

with `beta=alpha-1/2<1/2`; for the first `c log N` primes the Euler products are `N^o(1)` and `2^k=N^(c log 2+o(1))`. Thus merely making the number of exact Euler constraints unbounded does not destroy the blind mode.

The decisive quantifier is not the count of local constraints but whether they belong to **one persistent source across all scales**. If a fixed squarefree ternary source with `xi_1=1` satisfies nested exact Euler laws whose union exhausts the primes, FD-216 shows immediately that `xi=mu`. Horizon-local countermodels can therefore absorb logarithmically growing coherence, while globally compatible exhaustive coherence collapses the source class to Möbius itself.

The reusable mechanism is a fibre decomposition plus a quantifier boundary. The switched observation remains fibrewise enough that finite Euler packages can be preconditioned before source construction, even when their size grows like `log N`. What has not been absorbed is the compatibility required to reuse the **same** source when the constrained prime set changes with scale.

**Boundary.** FD-216 is not a Möbius counterexample and does not prove that `1/(2 log 2)` is sharp. Its sources depend on the target horizon. The surviving research question is whether physical Farey data can exploit same-source cross-scale multiplicative compatibility quantitatively before the assumptions have already identified the source as Möbius.
