# MI-018 — Additive coordinate dimension is not an information-capacity bound

**Evidence level:** exact information-capacity boundary from [FD-141](../../findings/FD-141-one-infinite-precision-additive-coordinate-can-encode-the-full-squarefree-factorization.md), correcting any extrapolation of the fixed-congruence obstruction [FD-140](../../findings/FD-140-every-fixed-congruence-coordinate-alphabet-misses-a-finer-prime-color-wall.md) to arbitrary finite-dimensional strongly additive coordinates

FD-140 proves that every fixed congruence-periodic coordinate alphabet leaves a finer coprime prime-color direction. That conclusion depends on the bounded arithmetic resolution of the visible alphabet, not on finite coordinate dimension by itself.

FD-141 gives an exact one-dimensional counterexample to the over-broad dimensional statement. Enumerate the primes `p_1<p_2<...` and define the strongly additive coordinate

`F(n)=sum_(p_j|n) 3^(-j)`.

On squarefree integers the weights are superincreasing: the first differing prime digit dominates the entire remaining tail. Hence `F` is injective on the squarefree fibre. One exact real number therefore recovers the full prime support, every additive prime-color statistic and every exact ancestry wall built from that support. Conditioning on an exact `F`-cell removes dilution completely because each nonempty squarefree cell is a singleton.

The information has not disappeared; it has moved into precision. On squarefree integers up to `T`, the minimum separation satisfies

`(1/2) 3^(-pi(T)) <= Delta_F(T) <= 3^(-pi(T))`.

Resolving every state through this one scalar thus needs `Theta(pi(T))` bits of worst-case precision. At any fixed absolute quantization scale, distinct high-prime states eventually collide. Algebraic dimension stays one while the effective resolving capacity grows with the whole prime alphabet.

The reusable distinction is therefore **dimension versus resolution capacity**. A finite-dimensional observable can be lossless when exact real digits are unconstrained; conversely, a high-dimensional observable can still be source-poor if its alphabet, precision or regularity is restricted. A meaningful Farey ancestry no-go must price how many source states the admissible coordinates can stably distinguish, not merely how many coordinates are written down.

This changes the live proof obligation after FD-140. A positive source law may still use a nonperiodic coordinate family, but it must be justified by the actual Farey/Möbius construction and remain below circular source reconstruction. A negative theorem against broader coordinate families must impose an information restriction such as finite/growing precision, entropy or covering complexity, regularity of the prime weights, source-native description length, or another quantitative resolution budget. Without such a restriction, diagonalizing against a fixed number of coordinates is false.

**Boundary.** The coordinate `F` is deliberately infinite-precision, nonperiodic and not claimed to be source-native, stable, efficiently decodable or useful for the Franel/Farey endpoint. It ignores prime powers and is used on the squarefree fibre where the ancestry controls live. FD-141 does not prove a coercive Farey theorem; it identifies the missing hypothesis that any general coordinate-incompleteness theorem must state.