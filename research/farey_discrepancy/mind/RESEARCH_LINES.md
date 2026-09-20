# Farey-discrepancy research lines

This file records current mathematical questions for the Farey-discrepancy line. It is a mutable synthesis, not a chronology or task list.

## Move beyond Vinogradov–Korobov-scale base-anchored switched blindness to an intrinsic coercive boundary

**Linked intuition:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-212--FD-221 show that the periodic switched schedule admits physical super-square-root blind modes and that every fixed block can be realized by one exact-Euler comparison source until literal prefix coverage. FD-222 extends the divisor-reservoir construction to `J=O(log log N)`. FD-223 removes that first quantitative frontier: with `Phi(N)=(log N)^(3/5)/(log log N)^(1/5)`, the same construction works for every `J<=kappa_beta Phi(N)` while the **absolute** exact-Euler cutoff remains fixed at `p<=beta N`, `beta<1`.

FD-225 strengthens the geometry inside that same range. The complete divisor-reservoir response operator has the exact inverse `c(n)=sum_(d|n)(y(d)-y(d-1))`. Using all divisor reservoirs, rather than one pivot reservoir per switched row, one can flatten every sample `X_N(mN)` for `1<=m<=D` to one common value up to error at most `1`. Hence all scheduled switched observations are actually `O(1)` while `X_N(N) asymp_beta N/(D log N)=N^(1-o(1))`. The previous `17^J` triangular-conditioning loss is therefore not structural.

FD-224 fixes the quantifier interpretation. Exact global Euler windows at several horizons collapse to their maximal prime cutoff `Y_*`. Hence a fixed positive fractional rule `p<=theta H` at every dyadic horizon reaches the original prefix after the finite depth `J_theta=1+ceil(log_2(1/theta))`; at that point the source is literally Möbius on `n<=N`, independently of the filter. Likewise one permanent source satisfying exhaustive exact-Euler windows on a cofinal sequence is pointwise `mu`. Thus the growing FD-222--FD-223/FD-225 blocks necessarily use vanishing relative fidelity `beta*2^(-j)` at later horizons. Cofinal **exact** Euler compatibility is source identification, not a remaining filter-coercivity problem.

The live negative frontier is now narrower: within the non-exhaustive base-anchored model `Y_*=beta N<N`, the present `Phi(N)` ceiling can no longer be attributed to loss of rank or exponential conditioning of the switched repair. What remains in the floor-stable construction is the `D^2 D^(o(1)) exp(-c Phi(N))` budget coming from shrinking prime reservoirs and from fitting the physical Mertens baseline. Determine whether a different reservoir geometry or baseline construction keeps blindness farther toward logarithmic observation depth, or prove a capacity obstruction that survives exact full-divisor inversion and stronger analytic source estimates. A genuinely different fidelity experiment must be non-exhaustive or approximate; otherwise exact Euler coverage eventually restores the physical source tautologically.

## Keep observation depth, analytic input, reservoir capacity and literal coverage distinct

FD-223 originally mixed three quantitative effects: floor-cell reservoir width `asymp N/D`, unconditional prime/Möbius remainders, and a pivot-only triangular inverse bounded by `17^J`. FD-225 removes the third effect completely by an exact divisor-response inversion and even makes the whole integer-multiple sample grid constant up to unit rounding error. The certified Vinogradov--Korobov depth is therefore now controlled by the first two effects, not by switched-matrix conditioning.

Literal coverage remains a different currency. By FD-224, only the maximal exact-Euler cutoff matters for source identity: once it reaches `N`, the earlier prefix has no relaxed-source freedom at all. Before coverage, and especially for the fixed absolute cutoff `beta N`, exhausting the current VK estimate says nothing by itself about an intrinsic capacity theorem.

Future work should therefore state explicitly which boundary changes. An intrinsic result must prove that every admissible non-exhaustive repair fails for structural reasons, not merely that the present floor-stable reservoirs or current zero-free-region estimates run out. Conversely, any stronger blind construction should report both its observation depth and its maximal absolute Euler cutoff so that growing block length is not mistaken for growing fractional multiplicative fidelity.
