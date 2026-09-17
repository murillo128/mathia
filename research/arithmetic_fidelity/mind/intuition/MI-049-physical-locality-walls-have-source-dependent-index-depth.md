# MI-049 — Physical locality walls have source-dependent index depth

**Evidence level:** exact synthesis from [AF-395](../../findings/AF-395-fixed-successor-radius-misses-disconnected-curvature-on-prime-log-meshes.md) through [AF-401](../../findings/AF-401-prime-short-interval-fidelity-pushes-shrinking-locality-to-17-30-successor-depth.md). The fixed-wall conversion, the moving-wall counterexample/repair, and the prime short-interval conversion are exact within their stated asymptotic hypotheses; no detector theorem is transferred between source families.

A locality threshold should first be stated in the source's intrinsic physical coordinate and only then converted into a combinatorial index budget. If an increasing source scale `a_N` is regularly varying with index `rho>0`, then a **fixed** logarithmic reach `h` corresponds to successor depth

`B_N(h)/N -> exp(h/rho)-1`.

When the source admits a locally uniform second-order expansion

`log(a_floor(lambda N)/a_N)=rho log lambda + epsilon_N psi(lambda)+o(epsilon_N)`,

with `N epsilon_N -> infinity`, the same fixed physical wall acquires the source-dependent correction

`B_N(h)=(lambda_*-1)N-[lambda_* psi(lambda_*)/rho]N epsilon_N+o(N epsilon_N)`,

where `lambda_*=exp(h/rho)`. Thus a fixed physical wall is invariant while its index depth records the density law of the source coordinates.

AF-400 adds a scale-matching boundary that ordinary regular variation does not see. Regular variation controls fixed multiplicative ratios; it does **not** control a shrinking reach `h_N -> 0`. There are smooth increasing regularly varying scales for which `B_N(h_N)/(N h_N)` has different subsequential limits. A sufficient repair is the local differential law `x f'(x)/f(x) -> rho`: if also `N h_N -> infinity`, then

`B_N(h_N) ~ N h_N/rho`.

For primes the exact pullback is `B_N(h)=pi(e^h p_N)-N`. AF-400's global PNT control reaches every fixed polylogarithmically shrinking wall covered there. AF-401 pushes the same source-coordinate conversion into a genuinely polynomial shrinking regime by using a uniform primes-in-short-interval theorem: if `h_N -> 0` and `h_N >= p_N^(-13/30+epsilon)` eventually, then

`B_N(h_N) ~ N h_N`.

Hence `h_N=p_N^(-beta)` with `beta<13/30` costs `N p_N^(-beta)` successors, while at the present uniform theorem boundary the depth is `N^(17/30+epsilon+o(1))`. The exponents `13/30` and `17/30` are boundaries of the unconditional source-density theorem being used, not intrinsic locality constants of the prime mesh and not properties of the downstream `PF_3` detector.

The reusable rule is therefore two-stage. **Define the physical relation first, then demand source-coordinate control at the same scale at which that relation is being probed.** Fixed-wall questions may need only regular variation; moving-wall questions need a matching local modulus or short-interval density theorem. Successor count is never an intrinsic locality resource by itself.

**Boundary.** AF-399 treats fixed `h`; AF-400 proves that this cannot simply be extrapolated to arbitrary `h_N -> 0`; AF-401 gives a prime-specific polynomial regime down to the current uniform short-interval threshold. The derivative criterion is sufficient rather than claimed necessary, and the `13/30` boundary is not claimed sharp. None of these results supplies a shrinking `PF_3` detector wall, proves source-density control below the stated prime short-interval range, treats index-zero/rapidly varying scales in general, or proves that higher-order total-positivity problems have the same topology/resource split.