# Farey-discrepancy research lines

This file records current mathematical questions for the Farey-discrepancy line. It is a mutable synthesis, not a chronology or task list.

## Move beyond Vinogradov–Korobov-scale base-anchored switched blindness to an intrinsic coercive boundary

**Linked intuition:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-212--FD-221 show that the periodic switched schedule admits physical super-square-root blind modes and that every fixed block can be realized by one exact-Euler comparison source until literal prefix coverage. FD-222 extends the divisor-reservoir construction to `J=O(log log N)`. FD-223 removes that first quantitative frontier: with `Phi(N)=(log N)^(3/5)/(log log N)^(1/5)`, the same construction works for every `J<=kappa_beta Phi(N)` while the **absolute** exact-Euler cutoff remains fixed at `p<=beta N`, `beta<1`.

In that range the sampled divisor depth satisfies `D asymp 2^J`, every switched observation is at most `O_beta(D)=N^(o(1))`, yet the earlier prefix remains `X_N(N) asymp_beta N/(D log N)=N^(1-o(1))`. The present Vinogradov--Korobov ceiling is therefore a certified analytic range for the base-anchored model, not evidence that the switched filter becomes coercive beyond it.

FD-224 fixes the quantifier interpretation. Exact global Euler windows at several horizons collapse to their maximal prime cutoff `Y_*`. Hence a fixed positive fractional rule `p<=theta H` at every dyadic horizon reaches the original prefix after the finite depth `J_theta=1+ceil(log_2(1/theta))`; at that point the source is literally Möbius on `n<=N`, independently of the filter. Likewise one permanent source satisfying exhaustive exact-Euler windows on a cofinal sequence is pointwise `mu`. Thus the growing FD-222--FD-223 blocks necessarily use vanishing relative fidelity `beta*2^(-j)` at later horizons. Cofinal **exact** Euler compatibility is source identification, not a remaining filter-coercivity problem.

The live negative frontier is now narrower: within the non-exhaustive base-anchored model `Y_*=beta N<N`, determine whether reservoir capacity eventually fails for a structural reason that survives stronger analytic source estimates, or whether a different repair keeps blindness much farther toward logarithmic observation depth. A genuinely different fidelity experiment must be non-exhaustive or approximate; otherwise exact Euler coverage eventually restores the physical source tautologically.

## Keep observation depth, analytic input, reservoir capacity and literal coverage distinct

The FD-223 threshold mixes shrinking divisor reservoirs with the available unconditional prime and Möbius remainders. Reservoir widths are `asymp N/D`, while the published triangular-repair bound also deteriorates with `J`; Vinogradov--Korobov cancellation absorbs those losses up to a fixed multiple of `Phi(N)`. Failure of this particular proof beyond that scale could therefore reflect the available analytic remainder rather than loss of source freedom.

Literal coverage is a different currency. By FD-224, only the maximal exact-Euler cutoff matters for source identity: once it reaches `N`, the earlier prefix has no relaxed-source freedom at all. Before coverage, and especially for the fixed absolute cutoff `beta N`, exhausting the current VK estimate says nothing by itself about an intrinsic capacity theorem.

Future work should therefore state explicitly which boundary changes. An intrinsic result must prove that every admissible non-exhaustive repair fails for structural reasons, not merely that the present floor-stable reservoirs or current zero-free-region estimates run out. Conversely, any stronger blind construction should report both its observation depth and its maximal absolute Euler cutoff so that growing block length is not mistaken for growing fractional multiplicative fidelity.
