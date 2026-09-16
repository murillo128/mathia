# MI-037 — High-ordinate zeta bounds cap the boundary-approach tariff

**Evidence level:** literature+derived synthesis from [NB-154](../../findings/NB-154-boundary-approach-amplifies-target-and-euler-response-by-the-same-poisson-width.md), [NB-160](../../findings/NB-160-separated-jordan-supports-force-adverse-zero-reservoir.md) through [NB-165](../../findings/NB-165-high-ordinate-one-line-bounds-cap-the-inverse-boundary-gap-tariff.md). The `zeta'/zeta` estimate used in NB-165 is due to Cully--Hugill--Leong; the line-specific content is its insertion into the zero-mass signed conservation law and the resulting adverse-zero budget.

NB-154 identifies the natural boundary-only currency for a compact zero-mass signed sampler at horizontal distance `a_G` from `Re s=1`. With total variation `V_G` and target charge `c_G`, the absolute Euler-product majorant gives a source remainder of order `V_G/a_G`, so the corresponding conditioning cost is `C_G/a_G` with `C_G=V_G/c_G`.

That estimate deliberately ignores all high-ordinate oscillation. NB-165 uses the actual zeta source to supply an independent bound: uniformly for `sigma>=1` at large ordinate,

`|zeta'(sigma+it)/zeta(sigma+it)| << log t/log log t`.

The completed-Gamma common logarithm still disappears because the sampler has zero total mass. Taking the better of the two source estimates gives the exact available conservation scale

`V_G M_G`,  with  `M_G=min{a_G^(-1), log G/log log G}`.

This changes the interpretation of boundary approach. Above the crossover `a_G ~ log log G/log G`, the elementary inverse-gap estimate remains the stronger one and NB-154 is the right currency. Below the crossover, further motion toward the one-line does **not** keep increasing the source-side tariff. The actual high-ordinate logarithmic derivative caps it at the `log G/log log G` scale.

For a logarithmic target packet, essentially full signed adverse debt is forced whenever

`C_G M_G=o(log G)`.

In the extreme boundary regime this reduces to `C_G=o(log log G)` independently of how fast `a_G->0`. The earlier intuition that arbitrarily small horizontal gap could itself provide arbitrarily large arithmetic amplification is therefore false for compact samplers once the known high-ordinate source theorem is used.

The cap does not create long-range escape. Under the same conservation condition, a fixed fraction of the adverse mass remains within ordinate distance `O(1+C_G)`. Combining this localization with the explicit Vinogradov--Korobov zero-free region gives a divergent lower bound on the number of adverse zero occurrences. Thus the improvement changes the **source remainder scale**, not the basic signed-conservation phenomenon.

This result interacts sharply with NB-164. Growing local moment order cannot cheaply preserve target gain at one Poisson width: it forces nonlocal support or exponential conditioning. Boundary motion cannot cheaply replace that resource either: once the gap crosses `log log G/log G`, the source tariff saturates. The surviving compact regime is therefore not “go closer and cancel more moments,” but **obtain cancellation in the actual high-ordinate arithmetic source beyond its pointwise one-line bound while retaining the target response**.

The reusable lesson is that a geometric amplification parameter should not be extrapolated past the scale where a stronger source theorem takes over. `1/a_G` is the correct absolute-convergence cost, not an intrinsic lower bound on the actual zeta logarithmic derivative. The destination budget must always use the minimum of all independently justified source estimates at the same point.

**Boundary.** The `log G/log log G` scale is an available verified pointwise upper bound, not claimed optimality. NB-165 does not rule out a specially designed sampler cancelling the actual values of `zeta'/zeta` much more strongly. Its support is compact in horizontal and vertical geometry apart from `a_G`; growing vertical diameter requires a new audit. The target-packet hypothesis remains conditional, counts zeros with multiplicity, and does not imply RH.