# MI-040 — Wang's upper pointwise ceiling moves from localization coherence to the interior mean-value budget

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-301](../../findings/VIS-301-wang-zero-free-localization-log-squared-window.md), using Wang's displayed localization and mean-value identities as audited there.

VIS-298 removes the lower moving-source crossover by exact gamma recentering. VIS-299 then shows that Wang's fixed exponent gap is not the true pointwise boundary: re-running the localization proof yields the same asymptotic whenever

`x log^3 T/H -> 0`, with `H=T^theta`.

VIS-300 decomposes that apparent boundary. Both pure localization leakage energies are only `O(x log^2 T)` and are already `o(H)` when `x=O(H/log^3 T)`. The extra logarithm sits entirely in the inside--outside cross-coherence

`C_I(x)=int_I A_I(x,t) overline(A(x,t)-A_I(x,t)) dt`.

VIS-301 closes that coherence wall under unconditional classical zero-free information. The standard Vinogradov--Korobov zero-free region bounds the real parts of the relevant zeros away from one by

`eta_T asymp (log T)^(-2/3)(log log T)^(-1/3)`

at the needed scale. In the near-height pieces this inserts the attenuation `q_T(x)=x^(-eta_T)` into both the inside and outside fields. Around the old `H/log^3 T` layer this is already super-polynomially small in `log T`; carrying it through the localization argument gives `C_I(x)=o(H)` throughout

`x=o(H/log^2 T)`.

The first generic `H`-scale term has therefore moved. It is no longer localization at all, but the Montgomery--Vaughan interior mean-value remainder

`O(x log^2(2x))`

for Wang's exact Dirichlet polynomial. This reaches the requested output scale at `x asymp H/log^2 T`.

The reusable lesson is that resolving a bundled proof boundary should **relocate the load-bearing term**, not preserve the old label. Exact recombination removed the lower-source wall; proof-level uniformity moved the first upper wall; energy decomposition isolated one coherence term; classical zero-free information then suppressed that term and exposed the interior Dirichlet-polynomial estimate underneath. A boundary is structural only after all earlier error channels are below resolution and the newly exposed term has itself been tested for coefficient-specific cancellation or sharpness.

For the current Wang statistic, the decisive next question is whether the exact coefficients

`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`

permit an improvement, explicit correction or matching lower/control construction beyond the generic `O(sum n a_n^2)=O(x log^2 x)` mean-value bound near `x~H/log^2 T`.

**Boundary.** `H/log^2 T` is currently a proof boundary, not a proved transition of the pair-correlation statistic. VIS-301 does not establish coefficient-specific cancellation at that scale, improve the fixed-power arithmetic source envelope, control bounded `x`, or justify moving-support versions of the integrated theorem. The `H/log^3 T` localization branch is closed under the current hypotheses and should not be reopened without changing the zero-free input.