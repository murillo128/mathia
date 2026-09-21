# MI-082 — Prime-mark entropy controls factor-quotient capacity

**Evidence level:** exact combinatorial synthesis from [MC-431](../../findings/MC-431-fixed-finite-prime-color-quotients-collapse-bell-capacity.md) and [MC-432](../../findings/MC-432-prime-color-entropy-controls-factor-quotient-capacity.md), refining the exact-factor Bell escape in MC-430. Set-partition, multinomial and partition-count ingredients are classical; the line-specific content is the quotient-capacity law on squarefree factor incidence.

Color the `r` distinct prime divisors into classes of sizes `r_1,...,r_k` and quotient unordered exact factorizations by permutations within each color. The quotient state is exactly an unordered multiset of block color-count vectors. Its count `Q` is controlled, uniformly in the number and balance of colors, by the prime-mark distinguishability budget

`D = log(r! / prod_a r_a!)`.

Indeed

`log Q = D + O(r log log r)`.

Along primorials, where `log N_r~r log r`, the retained factor-incidence exponent is therefore `D/(r log r)+o(1)`. A subpolynomial effective alphabet gives only `N_r^(o(1))` states; balanced `k=r^(alpha+o(1))` colors give `N_r^(alpha+o(1))`. The nominal number of labels is not the resource: their actual multinomial entropy is.

The durable conclusion is that **a polynomial fraction of Bell capacity requires a polynomial fraction of prime-identity distinguishability**. Fixed residue classes, a fixed tuple of finite-order characters, or any subpolynomial effective type system cannot explain a polynomial-capacity relational escape, even if complete block incidence among those types is retained.

**Boundary.** Capacity is only a necessary representation resource. A high-entropy quotient may still be analytically useless, and continuous/high-resolution marks must be charged at a justified precision before this count applies. The surviving question is whether a canonical arithmetic relation can retain enough prime-mark entropy to matter before Möbius projection while remaining substantially cheaper than near-lossless prime identity.