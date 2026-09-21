# MC-432 — Prime-color entropy controls the factor-quotient capacity exponent

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-INGREDIENTS · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-431` proves that collapsing exact prime identities to any **fixed** finite alphabet destroys the near-linear Bell capacity of exact factor incidence. Its fixed-`k` weighted-partition estimate deliberately leaves open the case in which the number of prime types grows with scale.

That escape admits a uniform resource law which does not require a fixed-dimensional vector-partition asymptotic.

Let `P` be an `r`-element set of distinct prime divisors of a squarefree integer, colored into nonempty classes of sizes

\[
r_1,\ldots,r_k,
\qquad
r_1+\cdots+r_k=r.
\]

Let `Q(r_1,\ldots,r_k)` be the number of unordered set partitions of `P` modulo permutations within each color class. Equivalently, by the exact orbit classification of `MC-431`, `Q` is the number of vector partitions of `(r_1,\ldots,r_k)` into an unordered multiset of nonzero vectors.

Define the exact prime-mark distinguishability budget

\[
D(r_1,\ldots,r_k)
:=
\log\binom{r}{r_1,\ldots,r_k}
=
\log\frac{r!}{\prod_{a=1}^k r_a!}.
\tag{1}
\]

Then, with `B_r` the Bell number and `p(r)` the ordinary partition function,

\[
\boxed{
\frac{B_r}{\prod_a r_a!}
\le
Q(r_1,\ldots,r_k)
\le
p(r)\frac{r!}{\prod_a r_a!}.
}
\tag{2}
\]

Consequently,

\[
\boxed{
\log Q(r_1,\ldots,r_k)
=
D(r_1,\ldots,r_k)+O(r\log\log r)
}
\tag{3}
\]

uniformly over **every** number of colors `1<=k<=r` and every color-class profile.

Now take the squarefree primorial

\[
N_r=\prod_{j\le r}p_j.
\]

Since `log N_r=(1+o(1))r log r`, equation `(3)` gives the exponent law

\[
\boxed{
\frac{\log Q(r_1,\ldots,r_k)}{\log N_r}
=
\frac{D(r_1,\ldots,r_k)}{r\log r}+o(1).
}
\tag{4}
\]

Thus the quotient retains a fixed polynomial fraction of the Bell-capacity exponent **if and only if** the coloring itself carries a fixed fraction of the full `r log r` prime-label distinguishability budget.

In particular, because

\[
\binom{r}{r_1,\ldots,r_k}\le k^r,
\tag{5}
\]

we obtain the uniform obstruction

\[
\boxed{
k=r^{o(1)}\quad\Longrightarrow\quad Q=N_r^{o(1)}.}
\tag{6}
\]

So the fixed-alphabet obstruction of `MC-431` is much stronger than its fixed-`k` proof alone showed: **even a subpolynomially growing number of prime types cannot retain polynomial factor-incidence capacity.**

Conversely, if the colors are asymptotically balanced and

\[
k=r^{\alpha+o(1)},
\qquad 0<\alpha\le1,
\]

then

\[
D=(\alpha+o(1))r\log r
\]

and therefore

\[
\boxed{Q=N_r^{\alpha+o(1)}.}
\tag{7}
\]

Polynomially many effective prime types are not merely a way to escape the finite-color theorem; on the primorial scale they buy the factor-quotient exponent essentially one-for-one.

This remains a state-capacity theorem only. It gives no bound for `M(x)` and no RH consequence.

## 1. The lower bound is pure orbit counting

The group

\[
G=S_{r_1}\times\cdots\times S_{r_k}
\]

acts on the `B_r` set partitions of `P` by permuting primes within each color class. Its orbits are exactly the states counted by `Q`, as proved in `MC-431`.

Every orbit has size at most

\[
|G|=\prod_a r_a!.
\]

Therefore the number of orbits is at least the total number of states divided by the largest possible orbit size:

\[
Q(r_1,\ldots,r_k)
\ge
\frac{B_r}{\prod_a r_a!}.
\tag{8}
\]

No assumption on `k`, balance of the classes, or freeness of the action is needed. Stabilizers can only make orbits smaller and increase `Q`.

## 2. A block-shape encoding gives the matching upper bound

Take one color-quotient state and forget the colors temporarily. Its block sizes form an ordinary integer partition

\[
\lambda=(s_1,\ldots,s_d),
\qquad
s_1+\cdots+s_d=r.
\]

There are exactly `p(r)` possible block-size shapes.

Fix one such shape and impose any deterministic ordering of its parts, for example nonincreasing size with an arbitrary order among equal sizes. Replacing an unordered quotient state by an ordered tuple of block color histograms can only increase the number of states.

For this ordered shape, consider the set of all words of length `r` over the `k` colors containing exactly `r_a` copies of color `a`. There are

\[
\binom{r}{r_1,\ldots,r_k}
\tag{9}
\]

such words. Cut a word into consecutive segments of lengths `s_1,\ldots,s_d` and replace each segment by its color-count vector. Every ordered tuple of block color histograms with the prescribed total color counts is realized by at least one such word: inside each segment, write the required number of copies of every color.

Hence, for each fixed block-size shape, the number of possible histogram tuples is at most the multinomial coefficient `(9)`. Summing over all `p(r)` shapes proves

\[
Q(r_1,\ldots,r_k)
\le
p(r)\binom{r}{r_1,\ldots,r_k},
\tag{10}
\]

which is the upper half of `(2)`.

This bound is deliberately insensitive to arithmetic realizability beyond squarefreeness. It is a pure quotient count, exactly matching the object of `MC-431`.

## 3. The two bounds differ only below the primorial exponent scale

Write

\[
D=\log\frac{r!}{\prod_a r_a!}.
\]

The upper bound `(10)` gives

\[
\log Q\le D+\log p(r).
\tag{11}
\]

An elementary Euler-product estimate gives

\[
\log p(r)=O(\sqrt r).
\tag{12}
\]

Indeed, for `t=r^{-1/2}` and the partition generating function

\[
P(z)=\prod_{m\ge1}(1-z^m)^{-1},
\]

positivity of coefficients yields `p(r)<=e^{tr}P(e^{-t})`, while

\[
\log P(e^{-t})
=
\sum_{\ell\ge1}\frac1\ell\frac1{e^{t\ell}-1}
\le
\frac1t\sum_{\ell\ge1}\frac1{\ell^2}
=O(1/t).
\]

For the lower bound, `(8)` gives

\[
\log Q
\ge
D-\log\frac{r!}{B_r}.
\tag{13}
\]

The Bell estimate already used in `MC-430` can be obtained by counting only partitions into blocks of size about `log r`:

\[
\log B_r
\ge
r\log r-r\log\log r-O(r).
\tag{14}
\]

Together with Stirling,

\[
\log r!=r\log r-r+O(\log r),
\]

this implies

\[
\log\frac{r!}{B_r}
\le
r\log\log r+O(r).
\tag{15}
\]

Combining `(11)`--`(15)` proves the uniform estimate `(3)`.

The error `O(r log log r)` is not intended to be sharp. Its significance is that it is

\[
o(r\log r),
\]

so it disappears on the ambient primorial exponent scale.

## 4. Exact effective-alphabet law

Equation `(1)` suggests defining an effective prime-mark alphabet size by

\[
K_{\rm eff}
:=
\exp(D/r).
\tag{16}
\]

This quantity depends on the complete class-size profile rather than merely on the nominal number `k` of colors. It satisfies

\[
1\le K_{\rm eff}\le k,
\tag{17}
\]

where the upper bound follows from `(5)`.

The primorial law `(4)` can then be written as

\[
\boxed{
Q=N_r^{\frac{\log K_{\rm eff}}{\log r}+o(1)}.
}
\tag{18}
\]

This resolves the growing-alphabet loophole at the state-count level.

- If `K_eff=r^{o(1)}`, the quotient is still `N_r^{o(1)}`.
- To retain `N_r^{\alpha+o(1)}` states for fixed `alpha>0`, one needs `K_eff=r^{\alpha+o(1)}` at exponent scale.
- A large nominal alphabet is insufficient when almost all primes remain in one class: what matters is the multinomial distinguishability budget `D`, not the number of unused or sparsely used labels.
- Exact prime identity corresponds to `r_a=1` for all `a`, so `D=log r!` and `(18)` returns exponent `1-o(1)`, consistent with the Bell result of `MC-430`.

For balanced classes, `K_eff=k^{1+o(1)}` whenever the Stirling error is negligible at `r log r` scale. Thus `k=r^{alpha+o(1)}` gives `(7)`.

The resource law makes precise how close a purported intermediate quotient is to simply restoring prime identity. Retaining a positive fraction `alpha` of the Bell exponent requires a prime-mark system with roughly `r^alpha` effective distinguishable types, not merely a slowly growing menu of coarse labels.

## 5. Relation to the current Möbius frontier

`MC-429` prices fixed-dimensional quantized additive factor summaries. `MC-430` shows that exact prime-block incidence has enough raw capacity to escape those no-go results. `MC-431` then proves that every fixed finite prime-type quotient loses that capacity.

The present result closes the obvious quantitative loophole in `MC-431`: letting the number of colors grow slowly does not help. The correct capacity parameter is the exact multinomial label budget `D`. Subpolynomial alphabet growth remains subpolynomial in the ambient integer scale, while polynomial effective alphabet growth purchases the same fraction of the full Bell exponent.

This materially narrows the surviving relational route. A factor construction cannot claim to sit far below exact prime identity merely because it uses a compressed label rather than the literal prime value. If its quotient needs a fixed polynomial fraction of Bell capacity, then at exponent scale its labels must already distinguish a polynomial number of prime types.

The analytic question is now sharper: **is there a canonical arithmetic relation with enough effective prime-mark entropy to survive this capacity theorem, while still being substantially cheaper than exact identity and supporting a signed operation before Möbius projection erases the incidence?** State counting alone cannot answer that next question.

## Representation-match map

The result is the same under the repository's representation lenses.

- **Affine/system view:** represent a factorization by a Boolean prime-by-block incidence matrix. The coloring partitions the rows into classes of sizes `r_a`.
- **Quotient/symmetry view:** factor-slot permutations remove column order, while `G=prod_a S_(r_a)` removes row identity within each color. The orbit is exactly the multiset of block color-count vectors from `MC-431`.
- **Elimination view:** eliminating literal row identities leaves only those block histograms. The exact cost of the retained row-label information is measured by the multinomial coefficient `r!/prod_a r_a!`.
- **Ideal view:** the one-hot Boolean incidence relations are unchanged; the new theorem concerns the size of the symmetry quotient rather than additional polynomial constraints.
- **Rank view:** ordinary matrix rank again does not control the information budget. Two incidence systems with the same dimensions and rank can lie in very different color-orbit profiles. The load-bearing invariant here is orbit distinguishability under the row-symmetry group.

This representation audit also explains why the multinomial coefficient is natural rather than an arbitrary entropy proxy: it is exactly the number of labeled color words with the prescribed class multiplicities.

## Prior art and novelty boundary

The underlying combinatorial languages are classical. `MC-430` already audits Bell-number and multiplicative-partition counting; `MC-431` audits ordinary and multipartite/vector partitions, including MacMahon's classical multipartite-partition framework and the fixed-dimensional weighted-partition boundary.

A fresh search against multipartite partitions, multiset partitions, colored set partitions, and Young-subgroup orbit language confirms that partitioning sets with repeated/color-identical elements is established combinatorics. No novelty is claimed for vector/multiset partitions, Bell asymptotics, integer-partition bounds, multinomial coefficients, group-orbit counting, or entropy interpretations of multinomial type classes.

The durable Mathia contribution is the **frontier specialization and uniform resource law** `(2)`--`(6)`: the exact-factor quotient from `MC-431` can be sandwiched directly between a Bell/orbit lower bound and a block-shape/multinomial upper bound, eliminating the fixed-`k` restriction and proving that every subpolynomial prime-mark alphabet remains subpolynomial on the primorial scale. Equation `(18)` identifies the effective prime-mark complexity required to retain any prescribed fraction of the Bell exponent.

## Boundaries and falsification tests

- **Squarefreeness remains load-bearing.** The set-partition model uses distinct prime divisors. Prime powers require exponent-multiset data and a different orbit count.
- **Within-color relabeling is load-bearing.** A proposed observable that uses actual prime sizes or pair-specific relations does not factor through this quotient merely because each prime also carries a color.
- **The primorial comparison is an exponent-scale calibration.** Equation `(2)` is finite and exact for every `r`; equations `(4)`, `(7)`, and `(18)` use the primorial asymptotic scale.
- **The `O(r log log r)` error is intentionally coarse.** It is sufficient to decide polynomial versus subpolynomial ambient capacity but does not resolve transitions whose multinomial budget itself is only `O(r log log r)`.
- **Polynomial capacity is not analytic usefulness.** A quotient with `K_eff=r^alpha` still has to support a Möbius-sensitive coefficient or transform; no cancellation follows from state volume.
- **Nominal `k` is not enough.** Highly imbalanced classes can have much smaller `D` than `r log k`; any concrete proposal must compute or bound its actual class profile.
- **Continuous/high-resolution marks require a different audit.** Discretizing such marks into a growing alphabet is legitimate only at a justified resolution, after which `(2)` applies to the resulting type profile. Hidden infinite precision must not be counted as free structure.

The next first-kill test for a proposed exact-factor quotient is therefore quantitative: compute its induced multinomial distinguishability budget `D`. If `D=o(r log r)`, the quotient has only `N_r^{o(1)}` states along primorials regardless of how many nominal labels were introduced. If `D` is a positive fraction of `r log r`, the proposal has escaped the capacity barrier but must then justify why that much prime-distinguishing information is canonical and analytically useful rather than a near-lossless relabeling of the prime identities.