# MI-044 — The completed fixed-gap saddle--transition kernel is universal and factorization-blind

**Evidence level:** exact/literature-aware synthesis from PL-379--[PL-397](../../findings/PL-397-fixed-gap-transition-universal-kernel.md), including PL-391--PL-396. No RH conclusion is claimed.

PL-392--PL-393 give the first representation warning: Euler--Maclaurin continuation can be fixed-zero faithful while disappearing in both the native `B^2` quotient and the fixed-`N` Jessen mean. PL-394 then finds a continuation-sensitive reflected/Gamma-phase cross channel with nominal pair saddle `t approx 2 pi nm`, while PL-395 restores the sharp moving Riemann--Siegel support and shows that every off-diagonal pair reaches that saddle before the larger term is admitted. In the hard main sum, active interior stationary geometry therefore collapses to the diagonal boundary.

PL-396 shows that the hard-support exclusion is not invariant under exact analytic continuation. In the absolutely convergent incomplete-gamma representation, the fixed-gap pair `q=r+d` has order-one smooth weights at its nominal saddle, because the activation offset, transition width and stationary-phase width all scale like `Theta(r)`. The representation-faithful local problem is a coalescing saddle--transition layer.

PL-397 computes its leading fixed-gap shape. With

`t = 2 pi r(r+d) + r u`

and fixed `d,u`, the two normalized incomplete-gamma factors converge to complementary error-function profiles of affine combinations of `d` and `u`, while the cross phase converges, up to the fixed quarter-turn factor, to the universal chirp `exp(i u^2/(4 pi))`. No prime-factor data enter this leading kernel.

This makes the matched control exact rather than heuristic. The fixed-gap transition layer is **structurally factorization-blind**: its leading local law depends on the additive gap and scaled transition coordinate, not on how `r` or `r+d` factor. That is not an information-theoretic statement—an integer still determines its prime factors—but it means the bare continuation kernel itself does not use the prime-lattice coordinates.

Any prime-lattice mechanism must therefore supply an additional arithmetic coupling before the relevant scalarization. A weight or incidence `A(r,r+d)` built from Möbius/von-Mangoldt data, gcd/lcm, divisor structure, cross-level relations or another source-forced object is a qualitatively different ingredient. Its value would have to come from a theorem showing that it survives the completed saddle--transition assembly and remains zero-sensitive, not from the universal kernel it multiplies.

**Boundary.** PL-397 is a leading fixed-gap asymptotic. It does not prove that the completed off-diagonal sum is nonzero, classify gaps growing with `r`, or construct an arithmetic coupling with useful sign or coercivity. Complex transition weights and archimedean terms can still cancel after summation. The durable conclusion is only that the bare fixed-gap transition profile is universal and cannot itself be credited as prime-factor leverage.
