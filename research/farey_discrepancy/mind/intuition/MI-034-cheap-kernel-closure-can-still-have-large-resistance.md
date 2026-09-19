# MI-034 — Cheap kernel closure can still have large resistance, and graph geometry can change that price

**Evidence level:** exact synthesis from [FD-202](../../findings/FD-202-prime-path-cross-mode-differences-collapse-random-multiplicative-energy-to-the-critical-scale.md) through [FD-204](../../findings/FD-204-lowbit-prime-shell-trees-achieve-logarithmic-resistance-at-critical-exponent-random-cost.md).

FD-202 shows that an exact signed projection can change the scaling of a positive quadratic statistic without changing the underlying Farey observation family. Adjacent differences of normalized reciprocal-prime rows cancel their common long Mertens bulk before squaring, and the resulting prime-path energy has critical squarefree-random scale `Theta(H)` instead of the diagonal `H^(3/2+o(1))` tariff. Algebraically the only missing direction is the constant shell mode.

FD-203 shows that the dimension of that kernel is not the right measure of the remaining inverse problem. Add any scalar anchor `ell` with `ell(1)=1`. The constant direction disappears, but the endpoint-difference functional still has exact squared dual norm `m-1`, independently of the anchor. The endpoint anchor itself is cheap in the source-faithful random benchmark, so kernel closure can cost `Theta(H)` while propagation through the path remains `Theta(m)` in squared resistance. **Kernel dimension, source cost and inverse resistance are independent resources.**

FD-204 then proves that the large resistance is a property of the chosen sparse graph, not an unavoidable price of the source information. On the reversed prime shell, the lowbit tree joins `j` to `j-2^(nu_2(j))`. Point evaluation has the exact squared dual norm

`1+popcount(j)`,

so the worst anchored resistance is only `Theta(log m)`. These longer edges remain source-faithful: each is the difference of two explicit Möbius slabs, and any adjacent shell boundary is crossed by at most one edge at each dyadic scale. That bounded multiscale overlap keeps the squarefree-random cost at `O(H log K)=H^(1+o(1))`.

The reusable point is a **joint source-overlap / inverse-resistance design law**. Adding nonlocal constraints is useful only when their source preimages can be reused sparsely enough that conditioning improves faster than the source benchmark deteriorates. Graph density by itself is not the resource; the relevant pair is how many times physical source slabs are charged and how much effective resistance remains after those edges are added.

This also changes how negative conditioning results should be interpreted. A large condition number for one representation can identify the missing graph geometry without proving that the source problem itself is ill-conditioned. Conversely, a well-conditioned auxiliary graph is not enough unless its edge functionals remain exact source observables and the resulting norm connects to the actual Farey/Mertens destination.

**Boundary.** FD-204 does not prove a physical Möbius bound for the lowbit energy and does not recover absolute `M(n)` from its cross-horizon increments. Its random estimate is an upper bound at the critical power exponent, not a proof that the logarithmic overhead is optimal. The remaining arithmetic questions are analytic control of this multiscale energy, outer cross-scale recovery, and the best achievable tradeoff between source-slab overlap and resistance.
