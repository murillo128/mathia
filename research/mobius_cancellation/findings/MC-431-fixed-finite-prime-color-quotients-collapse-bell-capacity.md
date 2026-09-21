# MC-431 — Fixed finite prime-color quotients collapse Bell factor capacity

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · CLASSICAL-INGREDIENTS · FRONTIER-ADVANCE · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-430` shows that full exact factor identity is a genuine escape from the recent factor-summary capacity barriers: for a squarefree integer with `r` distinct prime divisors, unordered active factorizations form `B_r` states, and along primorials this is `n^{1-o(1)}`. That finding leaves open whether a substantially smaller **relational quotient** of exact factor identity can retain polynomial state capacity.

A large class of such quotients can now be ruled out exactly.

Let

\[
n=\prod_{p\in P}p
\]

be squarefree, with `|P|=r`. Give each prime divisor one of `k` colors through a map

\[
c:P\to\{1,\ldots,k\},
\]

where `k` is fixed independently of `n` and `X`. Write

\[
r_a=|c^{-1}(a)|,
\qquad
r_1+\cdots+r_k=r.
\]

Let `\mathcal U(n)` be the unordered active factorizations of `n`, equivalently the set partitions of `P`. Now identify two factorizations whenever one can be obtained from the other by permuting prime divisors **within each color class**. Factor-slot order is already absent in `\mathcal U(n)`.

Then every orbit is classified exactly by an unordered multiset of nonzero vectors

\[
v(B)=\bigl(|B\cap c^{-1}(1)|,\ldots,|B\cap c^{-1}(k)|\bigr)
\in\mathbf Z_{\ge0}^k\setminus\{0\},
\]

one vector for each factor block `B`, with coordinate sum

\[
\sum_B v(B)=(r_1,\ldots,r_k).
\]

Hence the orbit count is exactly the multipartite/vector-partition number

\[
Q_k(r_1,\ldots,r_k)
:=
\#\left\{
\text{unordered multisets of nonzero }v\in\mathbf Z_{\ge0}^k:
\sum v=(r_1,\ldots,r_k)
\right\}.
\tag{1}
\]

For every fixed `k`, the weighted-partition bound already derived in `MC-429` gives

\[
\boxed{
Q_k(r_1,\ldots,r_k)
\le
\exp\!\left(C_k r^{k/(k+1)}\right)
}
\tag{2}
\]

for a constant `C_k` depending only on `k`.

Therefore, uniformly for squarefree `n\le X`,

\[
\boxed{
|\mathcal U(n)/(S_{r_1}\times\cdots\times S_{r_k})|
=
X^{o(1)}
}
\tag{3}
\]

for every fixed number of prime colors.

Along the squarefree primorial sequence `N_r`, this should be compared with `MC-430`:

\[
|\mathcal U(N_r)|=B_r=N_r^{1-o(1)},
\]

whereas every fixed finite-color quotient satisfies

\[
|\mathcal U(N_r)/(S_{r_1}\times\cdots\times S_{r_k})|
=N_r^{o(1)}.
\tag{4}
\]

Thus the Bell-capacity escape of `MC-430` is not carried merely by abstract block incidence. It is carried by **prime-distinguishing incidence information**. If exact prime identities are collapsed to any fixed finite alphabet before the factor relation is read, the near-linear Bell state family falls back to subpolynomial size.

Equivalently:

> **A factor-lift mechanism that retains only finitely many prime types cannot obtain polynomial state capacity from exact set-partition incidence alone. Any surviving polynomial-capacity quotient must use a prime-mark alphabet whose effective complexity grows with scale, or retain some other structure not invariant under within-type relabeling.**

This is a state-capacity obstruction only. It gives no estimate for `M(x)` and no RH consequence.

## Exact orbit classification

Take a set partition

\[
\pi=\{B_1,\ldots,B_d\}
\]

of the prime set `P`. Associate to each block its color-count vector `v(B_j)` and discard block order. The resulting multiset is invariant under every color-preserving permutation of `P`, so it is constant on the action of

\[
G=S_{r_1}\times\cdots\times S_{r_k}.
\]

The invariant is also complete. Suppose two set partitions `\pi` and `\pi'` have the same multiset of color-count vectors. Match their blocks so that corresponding blocks have identical vectors. For each color `a`, the matched blocks cut `c^{-1}(a)` into pieces of equal cardinalities on the two sides. Choose bijections piece by piece. Their union is a permutation in `S_{r_a}` carrying every block of `\pi` to its matched block in `\pi'`. Combining the colors gives an element of `G` sending `\pi` to `\pi'`.

Hence the `G`-orbits are in bijection with the vector partitions counted by `(1)`.

For `k=1`, this reduces to the familiar fact that a set partition modulo arbitrary relabeling of its ground set is determined only by its multiset of block sizes. Thus

\[
Q_1(r)=p(r),
\]

the ordinary integer partition function. The classical Hardy--Ramanujan scale `\log p(r)=\Theta(\sqrt r)` is the one-color endpoint of `(2)`.

## Capacity bound

Let `P_k(s)` denote the number of unordered multisets of nonzero vectors in `\mathbf Z_{\ge0}^k` whose total `\ell^1` weight is exactly `s`, without fixing the coordinate totals. Every orbit counted by `Q_k(r_1,\ldots,r_k)` has total scalar weight `r`, so

\[
Q_k(r_1,\ldots,r_k)\le P_k(r).
\tag{5}
\]

`MC-429` derives the classical weighted-partition generating function

\[
\sum_{s\ge0}P_k(s)z^s
=
\prod_{t\ge1}(1-z^t)^{-\binom{t+k-1}{k-1}}
\tag{6}
\]

and proves directly that, for fixed `k`,

\[
\sum_{s\le S}P_k(s)
\le
\exp\!\left(C_kS^{k/(k+1)}\right).
\tag{7}
\]

Taking `S=r` proves `(2)`.

For squarefree `n\le X`, trivially `r\le\log X/\log2`. Therefore

\[
\log Q_k
\ll_k
(\log X)^{k/(k+1)}
=o(\log X),
\]

which proves `(3)` without requiring primorial asymptotics.

The primorial comparison `(4)` is stronger conceptually rather than technically: `MC-430` shows that at those same inputs the unquotiented exact-factor state family has near-linear exponent. The finite-color quotient therefore destroys essentially all of the Bell-capacity exponent.

## Arithmetic specializations

The theorem applies immediately whenever the retained prime mark takes values in a fixed finite alphabet and the downstream factor observable uses only the resulting within-block type counts.

For example, fixing a modulus `q` and coloring each prime divisor by its residue class modulo `q` gives at most `q` colors, with the finitely many primes dividing `q` handled as additional fixed colors if desired. Exact knowledge of how many primes of each residue type enter every factor block still yields only `X^{o(1)}` orbit states after primes with the same color are identified.

Likewise, a fixed finite collection of finite-order characters, local parity tags, or any other fixed finite tuple of finite-valued prime labels induces only finitely many joint prime types. Retaining the full blockwise histogram of those types does not recover polynomial Bell capacity.

This does **not** cover prime marks of increasing complexity such as exact prime identity, high-resolution `\log p`, residues modulo a growing modulus, or a number of independent character coordinates tending to infinity. Those are precisely the remaining ways to break the finite-color symmetry, and their complexity must be priced separately.

## Relation to the current frontier

`MC-425` shows that factorwise Möbius signs have subpolynomial capacity even when factor depth grows. `MC-426`--`MC-429` extend that obstruction to bounded or coarsely quantized additive factor summaries. `MC-430` then identifies full exact factor identity as a genuine high-capacity escape, because unordered factorizations of a squarefree `r`-prime integer are all set partitions of the **labeled** prime set.

The present result isolates which part of that label information matters for capacity. If the prime labels are collapsed to one type, only integer-partition shape remains. If they are collapsed to any fixed `k` types, only a `k`-dimensional vector partition remains. Both are subpolynomial in the ambient integer scale.

This sharpens the next frontier question. It is no longer enough to seek an abstract relational quotient between Möbius signs and full factor identity. Such a quotient must retain **scale-growing prime distinguishability**. A proposed mechanism based on a fixed menu of prime categories can now be killed before analytic work begins, even if it preserves the complete factor-block incidence among those categories.

The result also differs from `MC-204`. There the source itself is a ternary coordinate word and full permutation invariance collapses it to a small histogram. Here a nontrivial relational object -- a set partition of the source coordinates -- survives, and the exact quotient is correspondingly richer: a vector partition rather than a single histogram. The new point is that this relational enrichment is still subpolynomial when the source alphabet remains fixed.

## Representation-match map

The same object survives the repository representation audit without changing the claim.

- **Affine/system view:** use Boolean incidence variables `x_{pj}` indicating whether prime `p` belongs to factor block `j`, with `x_{pj}^2=x_{pj}` and one-hot row constraints. The coloring partitions the rows into `k` symmetry classes.
- **Ideal view:** the Boolean one-hot ideal is preserved by permutations within each row-color class and by factor-slot permutations. No extra polynomial relation is needed for the quotient theorem.
- **Quotient/symmetry view:** quotienting columns removes artificial factor order; quotienting rows within color classes leaves exactly the multiset of block color-count vectors. This is the complete orbit invariant proved above.
- **Elimination view:** eliminating individual row identities while retaining color sums replaces every block support by its vector `v(B)`. Sorting the resulting vectors is exactly the vector-partition quotient `(1)`.
- **Rank view:** ordinary matrix rank is not the controlling invariant. Matrices with the same color-count orbit data can have different labeled supports before the quotient; the information loss is caused by the symmetry action, not by a rank deficiency.

The vector-partition representation is useful because it makes the state-count theorem immediate and exposes the resource that must grow to escape it: the number or resolution of prime marks.

## Prior art and novelty boundary

The combinatorics used here is classical. Ordinary set partitions modulo relabeling reduce to integer partitions of the ground-set size. Hardy and Ramanujan's classical partition asymptotics quantify the one-color case.

For several colors, P. A. MacMahon, *The Enumeration of the Partitions of Multipartite Numbers*, Proceedings of the Cambridge Philosophical Society **22** (1925), 951--963, DOI `10.1017/S0305004100014547`, is an early systematic source for multipartite/vector partition enumeration. The weighted-partition product and the exponent `k/(k+1)` used in `(6)`--`(7)` are already treated as classical in `MC-429`, which also records modern Meinardus-type references.

A fresh prior-art search also found modern literature on various notions of colored set partitions, but those works study different colorings/statistics and are not needed for the exact orbit argument above. No novelty is claimed for set partitions, their symmetric-group orbits, integer partitions, multipartite partitions, or weighted-partition asymptotics.

The durable contribution is the **frontier specialization**: applying the classical vector-partition quotient to the exact-factor escape in `MC-430` proves that any fixed finite prime-type compression destroys its polynomial Bell capacity. This turns the vague requirement to retain "rich relational arithmetic" into a sharper resource condition: prime-distinguishing complexity itself must grow.

## Boundaries and falsification tests

- **Fixed `k` is load-bearing.** The constant in `(2)` depends on `k`; no uniform conclusion is claimed when the number of prime types grows with `r`. Determining the growing-`k` threshold is the natural next capacity question.
- **Within-type relabeling is load-bearing.** If an observable distinguishes two primes of the same nominal type through their actual sizes, residues at a growing modulus, pair relations, or another mark, then it does not factor through this quotient.
- **Squarefreeness is load-bearing for the simple set-partition model.** Repeated prime powers require exponent-multiset data.
- **Factor-slot symmetry is built in.** Ordered factor tuples contain additional artificial slot information and are not the object counted here.
- **State count is not cancellation.** Escaping `(2)` is only a necessary representation-capacity condition, not evidence for orthogonality, a useful signed transform, or a bound for `M(x)`.
- **Finite arithmetic marks are not dismissed as useless.** They may prove important theorems for other reasons; the statement here is only that their exact factor-block incidence cannot by itself account for the near-linear Bell capacity of full prime identity.
- **The theorem does not price continuous or high-resolution marks.** Those return to precision/variation questions such as `MC-427`--`MC-429` or require a new analysis.

The next first-kill test for a relational exact-factor proposal is therefore explicit: identify the effective prime-mark alphabet after all claimed symmetries. If its size is fixed, `(2)` gives subpolynomial capacity immediately. If it grows, quantify that growth and show that the resulting extra distinguishability is canonical arithmetic structure rather than a near-lossless encoding of the original prime labels.