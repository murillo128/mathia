# MI-035 — Chebyshev modes are the sharp approximate terminal coordinates

**Evidence level:** exact source-side synthesis from [RE-161](../../findings/RE-161-approximate-terminal-moments-leak-before-factorial-remainder.md), [RE-162](../../findings/RE-162-chebyshev-capacity-gives-the-sharp-growing-moment-terminal-threshold.md), and [RE-163](../../findings/RE-163-chebyshev-modes-diagonalize-sharp-approximate-terminal-leakage.md). The Chebyshev/Bessel expansion used in RE-163 is classical; no Robin inequality consequence is claimed.

RE-162 shows that exact matching of terminal moments through degree `r-1` leaves a sharp residual capacity of size

`(4+o(1))(L/4)^r/r!`.

RE-163 explains why this `4^{-r}` geometry was not visible in the raw approximate-moment coordinates of RE-161. After rescaling the terminal interval to `[-1,1]`, the exact terminal kernel has a positive Chebyshev expansion with

`A_j=(2+o(1))(L/4)^j/j!`

through the relevant degrees, and its full discrepancy is

`sum_(j>=1) A_j chi_j`,

where `chi_j` is the difference of the `j`-th Chebyshev moments of the two terminal packets.

Exact ordinary moment matching through degree `r-1` is equivalent to `chi_j=0` for every `j<r`, so the unresolved positive Chebyshev tail is exactly the sharp RE-162 capacity. Under approximate matching, the natural robust cost is instead

`C_r = sum_(j<r) (L/4)^j |chi_j|/j!`,

or, when arithmetic supplies signed cancellation, the single kernel-weighted low-mode sum. These coordinates measure leakage in the same basis that diagonalizes the destination kernel.

The distinction is real at growing order. RE-161's matched generalized sources can satisfy

`sup_k |mu_k|/L^k -> 0`

for normalized raw monomial discrepancies while an appropriately growing Chebyshev mode remains bounded away from zero. The small raw errors have migrated into a high polynomial mode near the interval endpoint; the triangular monomial-to-Chebyshev change of basis is not uniformly conditioned as degree grows.

Thus **approximate source control should be credited only after conversion into the kernel-adapted Chebyshev leakage actually consumed by the Robin coordinate**. More qualitative moment closeness is not a substitute for that conversion. A positive CA theorem could control every low Chebyshev mode, control their signed kernel-weighted combination, or rule out the endpoint mode migration mechanism; any of these would be materially new arithmetic structure.

**Boundary.** This is a matched generalized-source capacity statement. It does not show that ordinary primes realize the hidden modes or that CA extremals fail to control them. Its role is to identify the sharp approximate information currency after RE-162.
