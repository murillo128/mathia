# MI-049 — Physical locality walls have source-dependent index depth

**Evidence level:** exact synthesis from [AF-395](../../findings/AF-395-fixed-successor-radius-misses-disconnected-curvature-on-prime-log-meshes.md) through [AF-400](../../findings/AF-400-regular-variation-does-not-control-shrinking-locality-walls.md). The fixed-wall conversion and the moving-wall counterexample/repair are exact within their stated asymptotic hypotheses; no detector theorem is transferred between source families.

A locality threshold should first be stated in the source's intrinsic physical coordinate and only then converted into a combinatorial index budget. If an increasing source scale `a_N` is regularly varying with index `rho>0`, then a **fixed** logarithmic reach `h` corresponds to successor depth

`B_N(h)/N -> exp(h/rho)-1`.

When the source admits a locally uniform second-order expansion

`log(a_floor(lambda N)/a_N)=rho log lambda + epsilon_N psi(lambda)+o(epsilon_N)`,

with `N epsilon_N -> infinity`, the same fixed physical wall acquires the source-dependent correction

`B_N(h)=(lambda_*-1)N-[lambda_* psi(lambda_*)/rho]N epsilon_N+o(N epsilon_N)`,

where `lambda_*=exp(h/rho)`. Thus a fixed physical wall is invariant while its index depth records the density law of the source coordinates.

AF-400 adds a scale-matching boundary that ordinary regular variation does not see. Regular variation controls fixed multiplicative ratios; it does **not** control a shrinking reach `h_N -> 0`. There are smooth increasing regularly varying scales for which `B_N(h_N)/(N h_N)` has different subsequential limits. A sufficient repair is the local differential law `x f'(x)/f(x) -> rho`: if also `N h_N -> infinity`, then

`B_N(h_N) ~ N h_N/rho`.

For primes the exact pullback is `B_N(h)=pi(e^h p_N)-N`. The prime number theorem with an error smaller than the requested shrinking reach recovers the expected `N h_N` law, and the Korobov--Vinogradov error is strong enough for every polylogarithmically shrinking `h_N` covered in AF-400. This is a source-density theorem, not evidence that the `PF_3` topology wall itself shrinks.

The reusable rule is therefore two-stage. **Define the physical relation first, then demand source-coordinate control at the same scale at which that relation is being probed.** Fixed-wall questions may need only regular variation; moving-wall questions need a matching local modulus. Successor count is never an intrinsic locality resource by itself.

**Boundary.** AF-399 treats fixed `h`; AF-400 proves that this cannot simply be extrapolated to arbitrary `h_N -> 0`. The derivative criterion is sufficient rather than claimed necessary. None of these results supplies a shrinking `PF_3` detector wall, treats index-zero/rapidly varying scales in general, or proves that higher-order total-positivity problems have the same topology/resource split.