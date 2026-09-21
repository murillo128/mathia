# MC-436 — Prime-divisor gap-rank permutations attain factorial source capacity

**Evidence:** `EXACT-DERIVED · FRONTIER-ADVANCE · POSITIVE-BOUNDARY · CLASSICAL-INGREDIENTS · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-435` identified global ordinal relations among ordered prime divisors as the first obvious way to escape the bounded-local-decoration source-capacity obstruction. It observed that the relative order of the `r-1` adjacent prime-divisor gaps has at most `(r-1)!` values, but did not establish that all of those ordinal patterns are arithmetically realizable.

They are.

Let

\[
n=p_1\cdots p_r,\qquad p_1<\cdots<p_r,
\]

be squarefree and define the adjacent prime-divisor gaps

\[
g_i:=p_{i+1}-p_i,\qquad 1\le i\le r-1.
\]

Whenever the `g_i` are distinct, let `ord(g)` be the permutation recording their strict relative order. Then for every `r>=2` and every permutation

\[
\pi\in S_{r-1},
\]

there exists a squarefree integer `n` with `omega(n)=r` whose adjacent prime-divisor gaps have order pattern `pi`.

Consequently, if `T_r^{gap}` denotes the number of realized isomorphism types of the canonically ordered prime-divisor chain decorated only by the global rank order of its adjacent gaps, then

\[
\boxed{T_r^{gap}=(r-1)!.}
\tag{1}
\]

Calibrating against the squarefree primorial

\[
N_r:=\prod_{j\le r}p_j,
\qquad
\log N_r=(1+o(1))r\log r,
\]

Stirling's formula gives

\[
\log (r-1)!=(1+o(1))r\log r,
\]

and therefore

\[
\boxed{T_r^{gap}=N_r^{1-o(1)}.}
\tag{2}
\]

Thus the `MC-435` information threshold is sharp at the level of unconstrained source-type realizability: a purely ordinal, globally coupled relation can retain essentially the full primorial-normalized `Theta(r log r)` source-information budget without recording exact prime identities or numerical gap magnitudes.

This is a **representation-capacity result only**. It gives no estimate for `M(x)`, no cancellation theorem, and no RH consequence.

## 1. Exact realization of every gap-order permutation

Fix `r>=2` and a target permutation `pi` of the edge positions `{1,...,r-1}`. Choose positive real numbers

\[
d_1,\ldots,d_{r-1}
\]

with pairwise distinct values and with relative order prescribed by `pi`. Because the set is finite, choose `epsilon>0` so small that the intervals

\[
[d_i-2\varepsilon,d_i+2\varepsilon]
\]

are pairwise disjoint and remain positive.

Define

\[
c_1:=1,
\qquad
c_{i+1}:=c_i+d_i.
\]

For a scale parameter `X`, consider the disjoint ordered intervals

\[
I_i(X):=[c_iX,(c_i+\varepsilon)X].
\tag{3}
\]

For fixed `r`, `pi`, the `c_i`, and `epsilon`, the prime number theorem implies that every `I_i(X)` contains a prime once `X` is sufficiently large. Choose one such prime `p_i` from each interval. Since the intervals occur in increasing order,

\[
p_1<\cdots<p_r.
\]

Moreover,

\[
(d_i-\varepsilon)X
\le p_{i+1}-p_i
\le (d_i+\varepsilon)X.
\tag{4}
\]

The intervals on the right side of `(4)` are pairwise disjoint in exactly the prescribed order, by the choice of `epsilon`. Therefore the gap vector `(g_1,...,g_{r-1})` has strict order pattern `pi`.

Taking

\[
n:=\prod_{i=1}^r p_i
\]

produces the required squarefree source. Since `pi` was arbitrary, every element of `S_{r-1}` occurs, while no strict rank pattern can contribute more than one permutation. This proves `(1)`.

The argument uses only existence of primes in fixed positive-proportion intervals. No theorem on small gaps, large gaps, consecutive-prime patterns, prime tuples, or correlations between consecutive primes is needed.

## 2. Why this escapes the bounded-local alphabet obstruction

At first sight the construction seems to use very little information: each edge is assigned only a rank among the other edges, and the exact gap magnitudes are discarded. But the ranks are **globally coupled**. The rank labels form a permutation, so their joint state space has size `(r-1)!`, not `K^{O(r)}` for fixed `K`.

Equivalently, the effective alphabet at one edge grows on the order of `r`, and the global no-repetition constraint couples all `r-1` positions. Its logarithmic state budget is therefore

\[
\log (r-1)!=\Theta(r\log r),
\]

which is exactly the threshold isolated by `MC-435`.

This makes the distinction in `MC-435` concrete rather than hypothetical:

- bounded-resolution local decorations remain at `exp(O(r))=N_r^{o(1)}` source diversity;
- global gap-rank order reaches `exp((1+o(1))r\log r)=N_r^{1-o(1)}` source diversity.

So **low numerical precision is not low information cost**. A source may be represented only through comparisons, yet the resulting relational pattern can still carry identity-scale combinatorial information.

## 3. The important limitation: realizability is not size-efficient

Equation `(2)` uses the primorial `N_r` only as the same information-scale normalization used in `MC-430`--`MC-435`. The proof above does **not** place the realizing integer `n` near `N_r`, inside `N_r^{O(1)}`, or inside any other stated uniform size window as `r` grows.

For each fixed `r` and pattern `pi`, the prime number theorem eventually supplies the required primes, but the threshold scale `X` may depend strongly on the chosen configuration. Therefore `(1)` proves unconstrained arithmetic realizability of every type, not efficient realization at the natural smallest-source scale.

This distinction is load-bearing. If a later mechanism needs the gap-rank pattern to be available while the source integer remains within a controlled range, it must prove a uniform prime-distribution statement strong enough to supply that range. The present finding gives no such result.

Accordingly, `MC-436` closes only the first representation question left open by `MC-435`:

> Can a canonical, source-varying, non-numeric global relation actually attain the required `Theta(r log r)` source-type budget?

Yes, without a source-size constraint. Whether it does so **economically enough** for a Möbius-facing analytic argument remains open.

## 4. Why this does not yet help Möbius cancellation

The rank pattern depends on the additive geometry of the selected prime divisors,

\[
p_{i+1}-p_i,
\]

whereas Möbius multiplicativity depends only on the parity and support of the prime-factor set. Nothing in the realization proof shows that the ordinal gap pattern survives any of the operations that have repeatedly erased source information elsewhere in the line: divisor convolution, lcm aggregation, character projection, Cauchy/van der Corput squaring, or scalar summation.

Indeed, the result exposes a new possible failure mode. The representation has enough raw type capacity, but that capacity may be analytically inaccessible because comparing two adjacent gaps is equivalent to the four-prime inequality

\[
p_{i+1}-p_i<p_{j+1}-p_j,
\]

which is not multiplicatively separable. A downstream argument that replaces these comparisons by independent local bins falls immediately back under `MC-435`; an argument that keeps the whole permutation may simply have retained nearly lossless source information without gaining a tractable cancellation theorem.

Thus the next gate is not another capacity count. It is an **analytic survival/cost test**: identify a Möbius- or divisor-sum observable that depends nontrivially on the global gap-order type and determine whether that dependence survives the first exact aggregation or quadratic estimate without requiring essentially complete factor recovery.

## 5. Prior art and novelty boundary

The proof of realizability is an elementary application of the prime number theorem plus finite interval separation. `MC-S15` supplies the repository's classical prime-number-theorem anchor; its fixed-modulus arithmetic-progression statement contains the ordinary PNT as the trivial-modulus case. Stirling's formula and the primorial asymptotic are classical and already used throughout the source-capacity branch. No novelty is claimed for any of these ingredients.

The closest literature found in the novelty audit concerns different questions. Work on small or large gaps between **consecutive primes** studies the geometry of the ambient prime sequence and is not needed here because the selected prime divisors may have arbitrarily many unused primes between them. Efthymios Sofos, *Gaps between prime divisors and analogues in Diophantine geometry*, Glasgow Mathematical Journal **65** (2023), S129--S147, DOI `10.1017/S0017089522000398`, studies moments and probabilistic distribution of gaps between prime divisors of random integers. That is adjacent to the object but does not supply the deterministic finite-pattern realization above.

No claim is made that prescribed ordinal gap patterns are a new theorem of independent number-theoretic interest. The durable Mathia contribution is narrower: it resolves the explicit open boundary recorded in `MC-435` and proves that its factorial upper capacity is not merely formal. The global ordinal relation really can realize all factorial types, so representation-level source capacity alone can no longer kill this family.

## Boundaries and falsification tests

- **The gaps are between adjacent selected prime divisors, not necessarily consecutive primes globally.** Any appeal to consecutive-prime-gap theorems must justify why that stronger condition is relevant.
- **Strict order is load-bearing.** The construction separates the target gap scales, so ties do not occur. Other sources may have tied gaps; they simply lie outside the strict-permutation subfamily.
- **No uniform source-size bound is proved.** The factorial type count ranges over all squarefree sources with `omega(n)=r`. A bounded-height or near-primorial version is a different theorem.
- **Capacity is not cancellation.** `(2)` says only that the retained relational datum has enough combinatorial states. It does not imply orthogonality, pseudorandomness, character cancellation, or a bound on `M(x)`.
- **The representation is information-expensive despite being ordinal.** Its `(r-1)!` states carry `(1+o(1))r log r` natural-information units. It therefore escapes `MC-435` by paying the identity-scale budget, not by beating that budget.
- **Post-projection survival is mandatory.** If the intended analytic map depends only on finitely many gap bins, local comparisons, or another bounded quotient of the permutation, the relevant capacity is that quotient's capacity and `MC-435` applies again.
- **Arithmetic usefulness must be demonstrated before further elaboration.** A richer gap-order decoration should not be credited merely for adding more source types; the next result must connect a surviving part of this relation to an exact Möbius-facing operation.

The frontier therefore moves from **whether a global ordinal prime-divisor relation can attain polynomial source diversity** to **whether any such identity-scale relational information can survive a natural Möbius analytic operation at lower cost than retaining the factors themselves**.