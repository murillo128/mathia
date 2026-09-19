# MI-040 — Wang's upper pointwise ceiling moves from localization coherence to the interior mean-value budget

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-303](../../findings/VIS-303-wang-odd-shift-power-two-sparsity.md), using Wang's displayed localization and mean-value identities as audited there.

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

VIS-303 then decomposes the actual off-diagonal object at the exposed boundary instead of applying another generic majorant. Because `Lambda` is supported on prime powers, write `D_x=D_2+D_o`, where `D_2` contains powers of two and `D_o` odd prime powers. The power-of-two sector satisfies

`sum_(k>=1) a_(2^k)^2 << 1/x`,

`sum_(k>=1) 2^k a_(2^k)^2 << 1`.

Consequently, throughout `x log(2x)=O(H)`, the full mean-value remainder and the odd-prime-power remainder differ by only `o(H)`. Opposite parity is exactly the sector of odd additive differences, since the only even prime powers are powers of two. Therefore **every potentially `H`-scale off-diagonal contribution at the current boundary is carried by pairs of odd prime powers, hence by even additive differences**.

The load-bearing term has thus moved twice inside the same proof interface. First it moved from localization to the exact coefficient-weighted mean-value remainder; after source specialization and parity decomposition it moves again to the interval-kernel sum over odd-prime-power/even-shift pairs. A further gain must estimate that surviving sector using its exact frequencies `log(m/n)` and weights, produce a stable `H`-scale correction, or exhibit a matched admissible lower/control construction. Spending effort on powers of two, odd additive shifts, localization leakage, or the old `x log^2 x` coefficient majorant cannot decide the boundary.

The reusable lesson is that resolving a bundled proof boundary should **relocate the load-bearing term and then decompose that term using the exact source support before declaring the next barrier structural**. Exact recombination removed the lower-source wall; proof-level uniformity moved the first upper wall; energy decomposition isolated one coherence term; classical zero-free information suppressed it; coefficient-specific moment evaluation removed one logarithm; and exact prime-power support then deletes the whole odd-shift sector at the newly exposed scale.

**Boundary.** `x log x asymp H` remains a proof boundary, not a proved transition of the pair-correlation statistic. VIS-303 does not estimate the surviving even-shift sector, prove a Hardy--Littlewood-type asymptotic, distinguish prime pairs from general odd-prime-power pairs, improve the fixed-power arithmetic source envelope, control genuinely bounded `x`, or justify moving-support versions of Wang's integrated theorem.