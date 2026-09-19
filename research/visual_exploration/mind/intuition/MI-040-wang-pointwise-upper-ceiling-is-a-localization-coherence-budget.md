# MI-040 — Wang's upper pointwise ceiling moves from localization coherence to the interior mean-value budget

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-302](../../findings/VIS-302-wang-weighted-mean-value-log-boundary.md), using Wang's displayed localization and mean-value identities as audited there.

VIS-298 removes the lower moving-source crossover by exact gamma recentering. VIS-299 then shows that Wang's fixed exponent gap is not the true pointwise boundary: re-running the localization proof yields the same asymptotic whenever

`x log^3 T/H -> 0`, with `H=T^theta`.

VIS-300 decomposes that apparent boundary. Both pure localization leakage energies are only `O(x log^2 T)` and are already `o(H)` when `x=O(H/log^3 T)`. The extra logarithm sits entirely in the inside--outside cross-coherence

`C_I(x)=int_I A_I(x,t) overline(A(x,t)-A_I(x,t)) dt`.

VIS-301 closes that coherence wall under unconditional classical zero-free information. The standard Vinogradov--Korobov zero-free region inserts the attenuation `q_T(x)=x^(-eta_T)` into the near-height pieces and makes the localization contribution `o(H)` throughout `x=o(H/log^2 T)`. At that point the first generic `H`-scale term becomes Wang's displayed Montgomery--Vaughan coefficient bound `O(x log^2(2x))`.

VIS-302 shows that this second wall is also a proof-packaging artifact. For the exact Wang coefficients

`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`,

the coefficient weight is not merely `O(x log^2 x)` but

`sum_n n a_n^2=(4/3)x log x+(8/9)x+O(x exp(-cV(log x)))`.

The saved logarithm comes from inserting the classical asymptotic for `sum_(n<=u)Lambda(n)^2` instead of the pointwise majorant `Lambda(n)<=log n`. Feeding this exact weight into Montgomery--Vaughan, while retaining the VIS-301 zero-free localization control, gives the complete pointwise asymptotic whenever

`x log(2x)=o(H)`.

The load-bearing term has therefore moved again. The first unresolved generic upper scale is now

`x log x asymp H`,

or `x asymp H/log T` in the polynomial source regime, and the unresolved object is the **actual off-diagonal time integral** rather than its generic absolute coefficient majorant. A further gain must use the frequencies `log(n/m)` and Wang's exact weights, produce an explicit correction, or exhibit a matched lower/control construction. Re-estimating localization or repeating the `x log^2 x` coefficient bound cannot decide this layer.

The reusable lesson is that resolving a bundled proof boundary should **relocate the load-bearing term and then re-audit the new term after source specialization**. Exact recombination removed the lower-source wall; proof-level uniformity moved the first upper wall; energy decomposition isolated one coherence term; classical zero-free information suppressed that term; and coefficient-specific moment evaluation then removed one logarithm from the newly exposed generic mean-value bound. A boundary is structural only after every earlier channel is below resolution and the first remaining term has survived specialization to the actual source coefficients.

**Boundary.** `x log x asymp H` is currently a proof boundary, not a proved transition of the pair-correlation statistic. VIS-302 evaluates the coefficient weight entering the generic mean-value theorem but does not evaluate the actual off-diagonal remainder at that scale, improve the fixed-power arithmetic source envelope, control genuinely bounded `x`, or justify moving-support versions of Wang's integrated theorem.