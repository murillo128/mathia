# MC-125 — Exact local factor histograms do not control mean-absolute excursions below square-root memory

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

For every integers `r>=2` and `m>=1`, there are two binary increment words of the same length

\[
N=2rm+r-1
\tag{1}
\]

with **exactly the same counts of every contiguous factor of every length at most `r`**, but very different mean-absolute partial-sum excursions.

Write `+` for `+1` and `-` for `-1`, and set

\[
v=+^{r-1},\qquad A=+,\qquad B=-^r+^{r-1}.
\tag{2}
\]

Define

\[
U=vA^mB^m,
\qquad
W=v(AB)^m.
\tag{3}
\]

For a word `X=(x_1,...,x_N)` put

\[
S_X(j)=\sum_{i=1}^j x_i,
\qquad
D_1(X)=\frac1N\sum_{j=1}^N |S_X(j)|.
\tag{4}
\]

Then `U` and `W` are `r`-abelian equivalent, while

\[
\boxed{
D_1(U)
=
\frac{\frac12r(r-1)+mr(m+r-1)}{2rm+r-1}
}
\tag{5}
\]

and

\[
\boxed{
D_1(W)
=
\frac{\frac12r(r-1)+mr^2}{2rm+r-1}.
}
\tag{6}
\]

Consequently, if `m/r -> infinity`,

\[
D_1(U)\sim \frac m2,
\qquad
D_1(W)\sim \frac r2,
\tag{7}
\]

so the same complete local factor histogram can support first-absolute excursions differing by a factor asymptotic to `m/r`.

The failure persists for growing memory. For every fixed

\[
0<\alpha<\frac12,
\tag{8}
\]

choose `m=r^{(1-alpha)/alpha+o(1)}`. Along this family,

\[
r=N^{\alpha+o(1)},
\qquad
D_1(U)=N^{1-\alpha+o(1)},
\qquad
D_1(W)=N^{\alpha+o(1)}.
\tag{9}
\]

Thus one exact local-factor-count equivalence class contains a representative with **super-square-root** mean excursion and another with **sub-square-root** mean excursion whenever the memory exponent is below `1/2`.

This is an information-loss obstruction, not an arithmetic counterexample. The words are not claimed to be multiplicative or to have Möbius square-free support. The result says that translation-invariant local empirical data alone—even the entire factor histogram rather than finitely many selected correlations—does not retain enough ordering information to control an RH-scale first absolute mean below the square-root memory scale.

## 1. Exact equality of all local factor counts

Use the binary de Bruijn graph of order `r-1`: its vertices are words of length `r-1`, and appending one symbol traverses the edge labeled by the corresponding length-`r` word.

Take the common base vertex `v=+^(r-1)`. Appending `A=+` traverses the self-loop `+^r` and returns to `v`. Appending

\[
B=-^r+^{r-1}
\]

also gives a closed walk based at `v`: the first `r-1` minus symbols reach `-^(r-1)`, the next minus traverses the `-^r` self-loop, and the final `r-1` plus symbols return to `v`.

The word `U` therefore traverses `m` copies of the closed walk `A` followed by `m` copies of the closed walk `B`, while `W` traverses the same multiset of closed walks in alternating order. Reordering closed walks based at the same vertex leaves the de Bruijn edge multiset unchanged, so `U` and `W` have exactly the same count of every length-`r` factor.

Both words also have the same prefix and suffix `v`. The standard characterization of `r`-abelian equivalence then gives equality of factor counts at every length at most `r`. Equivalently, for every function

\[
\Phi:\{+1,-1\}^k\to\mathbb C,
\qquad 1\le k\le r,
\]

the translation-invariant cylinder sums agree exactly:

\[
\sum_{j=1}^{N-k+1}\Phi(U_j,\ldots,U_{j+k-1})
=
\sum_{j=1}^{N-k+1}\Phi(W_j,\ldots,W_{j+k-1}).
\tag{10}
\]

So the quotient identifies not merely a chosen list of correlations but the whole empirical distribution of local words through memory `r`.

## 2. Exact excursion areas

All partial sums of both words are nonnegative. The common prefix contributes

\[
1+2+\cdots+(r-1)=\frac{r(r-1)}2.
\tag{11}
\]

For `W`, every pair `AB` begins at height `r-1`. The `A` step reaches `r`; the `r` minus steps in `B` visit `r-1,...,0`; and the final `r-1` plus steps visit `1,...,r-1`. Hence one pair contributes exactly

\[
r+2(1+\cdots+(r-1))=r^2
\tag{12}
\]

to the area. This proves `(6)`.

For `U`, the block `A^m` visits heights `r,...,r+m-1`. Before the `j`-th copy of `B`, with `j=0,...,m-1`, the height is

\[
H_j=r-1+m-j.
\tag{13}
\]

A complete `B` block started at height `H` contributes

\[
(2r-1)H-r^2
\tag{14}
\]

to the area. Summing `(14)` over `(13)` and adding the common prefix and `A^m` contributions gives

\[
\sum_{j=1}^N |S_U(j)|
=
\frac{r(r-1)}2+mr(m+r-1),
\tag{15}
\]

which proves `(5)`.

The difference is therefore purely in **cycle order**. In `W`, each positive loop is immediately followed by the negative-net long cycle and the macroscopic drift is reset. In `U`, all positive loops are accumulated first, creating a height of order `m` before the same negative-net cycles unwind it. The local edge counts cannot see that ordering.

## 3. The square-root boundary of this obstruction family

In the separated regime `m/r -> infinity`, equations `(1)`, `(5)`, and `(6)` give

\[
D_1(U)\asymp \frac Nr,
\qquad
D_1(W)\asymp r.
\tag{16}
\]

If `r=N^(alpha+o(1))` with `alpha<1/2`, these lie on opposite sides of the square-root scale. When `alpha=1/2`, this particular construction reaches the balance point: both are of square-root order.

This yields a sharp threshold **for this explicit cycle-reordering obstruction**, not a positive theorem above it. The result does not say that `r~sqrt(N)` windows determine the path. It says only that sub-square-root empirical memory can remain compatible with a super-square-root excursion even when every local factor count through that memory is known exactly.

For fixed `r`, the loss is more extreme: `D_1(W)=O_r(1)` while `D_1(U)=Theta_r(N)`. Thus `MC-124`'s fixed-memory logarithmic invisibility is not merely a limitation of sign-odd correlation theorems. At the generic sequence-information level, the **entire** fixed-window empirical distribution can coexist with almost maximal differences in anchored excursion geometry.

## 4. Consequence for local-to-global Möbius proposals

`MC-124` showed, using Tao--Teräväinen, that every globally sign-odd fixed Möbius cylinder observable lies in the qualitative logarithmic fixed-correlation class. That left growing memory as a genuine escape.

The present obstruction closes the simplest version of that escape at the representation level. Merely increasing the window length does not restore the ordering information required for first-absolute excursion control if the data are still compressed to a translation-invariant empirical histogram.

A proposed transfer whose source side factors only through such local histograms should therefore be tested against this construction before it is treated as an excursion-sensitive carrier. To survive, it must use additional information absent here, such as arithmetic placement or prime labels, multiplicative compatibility across distant indices, an ordered/noncommutative statistic recording how local cycle blocks are sequenced, genuinely multiscale state coupling, or another source constraint that excludes the de Bruijn cycle-reordering class for a proved reason.

This narrows the accepted mean-absolute transfer clue but does not resolve it. Möbius multiplicativity, exact square-free support, prime-factor relations, and zeta-specific structure are precisely the kinds of global information not preserved by these binary controls.

## Prior art and novelty assessment

The local-equivalence language is classical. Juhani Karhumäki, Aleksi Saarela and Luca Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, Journal of Combinatorial Theory, Series A 120 (2013), no. 8, 2189--2206, DOI `10.1016/j.jcta.2013.08.008`, arXiv `1301.5104`, defines `k`-abelian equivalence by equality of factor counts through length `k` and supplies the prefix/suffix plus length-`k` count characterization used above.

The relation between `k`-abelian classes and de Bruijn cycle decompositions/switchings is also established combinatorics-on-words territory; see Karhumäki, Puzynina, Rao and Whiteland, *On cardinalities of k-abelian equivalence classes*, Theoretical Computer Science 638 (2016), 11--23, DOI `10.1016/j.tcs.2016.06.010`, and Cassaigne, Karhumäki, Puzynina and Whiteland, *k-Abelian Equivalence and Rationality*, Fundamenta Informaticae 154 (2017), 65--94, DOI `10.3233/FI-2017-1553`.

Within this line, `MC-S11` already gives an adjacent symbolic-dynamics warning: binary normality can survive sparse perturbations while one-symbol bias decays arbitrarily slowly. The present construction is stronger in a different direction: it keeps the **complete finite factor-count vector exactly identical** and computes the resulting first-absolute excursion separation.

A targeted literature search around `k`-abelian equivalence, de Bruijn cycle reorderings, partial sums, discrepancy, and excursions found the standard equivalence/complexity/switching literature but no reason to claim a new general word-combinatorics theorem. The construction and area calculation are elementary once the cycle-ordering viewpoint is chosen. **No novelty is claimed for `k`-abelian equivalence, de Bruijn cycle reordering, or the underlying combinatorial mechanism.** The durable content is the exact information-loss specialization for the Möbius line and the explicit `r` versus `N/r` excursion budget around square-root memory.

## Boundaries and falsification tests

- The controls are binary bounded-increment words, not multiplicative functions. They do not preserve Möbius square-free support by integer position, exact prime values, divisor relations, or zeta-specific analytic structure.
- Equality is for translation-invariant empirical factor counts. Position-weighted cylinders, anchored boundary statistics, ordered block data, adaptive windows, and nonlocal pairings can distinguish the words and lie outside the proved quotient.
- The result does not show that every particular local-histogram hypothesis admits a bad equivalence class. It shows that local-factor-count representation is not sufficient for excursion recovery; an arithmetic theorem must prove that its extra hypotheses exclude this ambiguity.
- The square-root threshold is specific to this construction. No reconstruction or sufficiency claim is made at or above `r~sqrt(N)`.
- Because the words contain no zeros, the construction also sits inside the `{+1,-1}` sector of any three-symbol cylinder language, but it does not preserve the actual Möbius zero/support process.
- No probabilistic independence, RH assumption, zero-free region, Mellin transform, or `1/zeta` identity enters.

## Consequence for the line

The current information-recovery frontier should distinguish **memory length** from **ordered information**. `MC-124` kills fixed sign-odd cylinders as a new logarithmic information class; `MC-125` shows that even the complete empirical cylinder law can remain excursion-blind when memory grows below square-root scale.

Growing memory is therefore not by itself the missing mechanism. A surviving route must explain what Möbius-specific arithmetic structure prevents large de Bruijn-style cycle reorderings, or retain information that does not factor through local pattern histograms in the first place. The accepted source-to-`D_M` problem remains open, but its next candidate should carry explicit nonlocal/order-sensitive or multiplicative information rather than merely a richer list of local frequencies.