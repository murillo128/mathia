# MC-434 — Canonical prime order is rigid but has zero conditional source-type diversity

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-INGREDIENTS · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-433` shows that a sparse relation on the prime coordinates of a squarefree integer can have trivial automorphism group and therefore retain the full Bell-number family of unordered factor partitions. It leaves canonical arithmetic provenance as one of the next gates: perhaps arbitrary rigid graphs are expensive because they merely encode prime identity, while a relation forced naturally by the arithmetic could be more restrictive.

The simplest canonical relation already shows that **canonical provenance does not by itself provide such a restriction**.

Let

\[
n=p_1\cdots p_r,
\qquad p_1<\cdots<p_r,
\]

be squarefree, and let `P(n)={p_1,...,p_r}`. Retain only the directed successor relation

\[
S_n(p_i,p_j)
\quad\Longleftrightarrow\quad
j=i+1.
\tag{1}
\]

Equivalently, `S_n(p,q)` says that `q` is the next larger prime divisor of `n` after `p`. This relation is intrinsic once the prime divisors are known, uses one binary relation symbol and exactly `r-1` incidences, and requires no externally chosen coloring, graph, or prime labels.

Nevertheless

\[
\boxed{\operatorname{Aut}(P(n),S_n)=\{1\}.}
\tag{2}
\]

Hence the relational factor-state quotient of `MC-433` is maximal:

\[
\boxed{
|\Pi(P(n))/\operatorname{Aut}(S_n)|=B_r.
}
\tag{3}
\]

At the same time, for fixed `r`, every such successor structure is isomorphic to every other one. If

\[
\mathcal T_r
:=
\left\{
[(P(n),S_n)]_{\cong}: n\text{ squarefree},\ \omega(n)=r
\right\},
\]

then

\[
\boxed{|\mathcal T_r|=1.}
\tag{4}
\]

Thus the symmetry-breaking budget from `MC-433`,

\[
A(S_n)=\log\frac{r!}{|\operatorname{Aut}(S_n)|}=\log r!,
\tag{5}
\]

is asymptotically maximal even though the retained relation has **no isomorphism-type variation at all among squarefree sources with the same number of prime factors**.

This separates two quantities that the previous capacity audit did not need to distinguish:

> **Rigidity measures internal coordinate addressability inside one source instance. It does not measure how much arithmetic information the relational isomorphism type carries across different source instances.**

For the canonical prime-successor chain, internal factor-partition capacity is `B_r`, while conditional source-type diversity is exactly one.

The distinction is load-bearing for the Möbius program. Any relation that is universal up to isomorphism at fixed `r` may provide a perfect coordinate frame and still carry no information about which primes actually occur. Source-specific arithmetic must then enter through additional labels, weights, values, residues, gaps, or through a downstream operation that explicitly reintroduces such data.

This is a representation-capacity obstruction only. It gives no estimate for `M(x)` and no RH consequence.

## 1. The canonical successor chain is rigid

For `r=1` the claim is immediate. Assume `r>=2`.

In the directed graph `(P(n),S_n)`, `p_1` is the unique vertex with indegree zero. Therefore every automorphism fixes `p_1`. Once `p_i` is fixed, `p_{i+1}` is its unique `S_n`-successor and must also be fixed. Induction gives

\[
p_i\mapsto p_i
\qquad(1\le i\le r),
\]

which proves `(2)`.

This is stronger than merely using the undirected path on the ordered prime divisors. The undirected path has a possible reflection, whereas the directed successor relation inherits its orientation canonically from the ordinary order on the integers and has no nontrivial automorphism.

Applying the exact orbit definition from `MC-433`, the action on the set `\Pi(P(n))` of unordered set partitions is therefore trivial. Every factor partition is its own orbit, proving `(3)`.

Along primorials `N_r=\prod_{j\le r}p_j`, the Bell estimate already established in `MC-430`--`MC-433` gives

\[
B_r=N_r^{1-o(1)},
\]

so a fixed binary relation with only `r-1` incidences can be both canonical and fully symmetry-breaking on the factor-state scale.

## 2. Rigidity does not imply source diversity

Now compare two squarefree integers

\[
n=p_1\cdots p_r,
\qquad
m=q_1\cdots q_r,
\]

with their prime divisors written in increasing order. The rank map

\[
\phi:P(n)\to P(m),
\qquad
\phi(p_i)=q_i,
\tag{6}
\]

is an isomorphism of directed successor structures, and it is the unique such isomorphism. Therefore all `r`-vertex prime-successor structures have the same isomorphism type, proving `(4)`.

This is not a contradiction with rigidity. A finite linear order can be rigid while all finite linear orders of the same cardinality are mutually isomorphic. Rigidity asks whether one fixed structure has nontrivial self-symmetries; source diversity asks how many non-isomorphic structures occur as the arithmetic input varies.

The same distinction can be written as the pair

\[
\left(
|\operatorname{Aut}(S_n)|,
|\mathcal T_r|
\right)
=(1,1).
\tag{7}
\]

The first `1` means every coordinate is internally addressable by rank. The second `1` means the bare successor relation contains no information distinguishing one `r`-prime source from another after prime values are forgotten.

Consequently there is no implication of the form

\[
A(R)\text{ large}
\quad\Longrightarrow\quad
\text{large arithmetic source diversity}.
\tag{8}
\]

`MC-433` remains correct: a small automorphism group guarantees many factor-partition orbits. The present result identifies what that guarantee does **not** say.

## 3. Where the Bell capacity actually lives

Let a factorization of `n` correspond to a set partition `\pi\in\Pi(P(n))`. Through the unique rank map

\[
p_i\longleftrightarrow i,
\]

the expanded object `(P(n),S_n,\pi)` is completely described by a set partition of `[r]={1,...,r}`.

Therefore, across **all** squarefree inputs with `r` prime factors, the possible expanded order-plus-partition isomorphism types are exactly the `B_r` partitions of `[r]`. The large state family is real, but it comes from arranging blocks relative to a universal rank coordinate frame. It does not come from variation in the underlying arithmetic relation.

This yields a sharper interpretation of the Bell escape:

- `MC-430` shows that full prime-block incidence gives `B_r` exact factor states;
- `MC-433` shows that a rigid retained relation can keep those `B_r` states distinct without literal prime labels;
- the present result shows that such rigidity can be supplied by a **universal canonical scaffold** whose isomorphism type is independent of the actual primes.

Hence an internal orbit count cannot by itself certify that a lift has retained source-specific arithmetic. It certifies only that the lift can address enough coordinate positions to distinguish partitions once a partition has been placed on that scaffold.

## 4. Möbius projection erases the rank scaffold

For a block `A` of the factor partition, squarefreeness gives

\[
\mu\!\left(\prod_{p\in A}p\right)=(-1)^{|A|}.
\tag{9}
\]

Thus the factorwise Möbius signs depend on block cardinalities, not on which rank positions occur in each block. The directed successor relation may distinguish the first, second, ..., `r`th prime divisor perfectly, but the map `(9)` forgets those distinctions.

After factor-slot permutation is also quotiented, `MC-430` already shows that the sign state is determined by the number of blocks and the number of odd-sized blocks, giving only `O(r^2)` possibilities across all depths. The canonical rank scaffold therefore supplies a concrete example that passes both the raw Bell-capacity gate and the canonical-provenance gate but fails the natural Möbius-sign survival gate.

More generally, suppose an observable `F(P,\pi)` factors only through the isomorphism class of `(P,S,\pi)` and does not separately use the numerical prime values. Then for fixed `r` there is a function `\widetilde F` on partitions of `[r]` such that

\[
F(P,\pi)=\widetilde F(\widehat\pi),
\tag{10}
\]

where `\widehat\pi` is the rank partition induced by `\pi`. Equation `(10)` is just transport through the unique order isomorphism, but it gives the exact boundary: any distinction between two prime sets having the same `r` must enter somewhere outside the bare successor relation.

This does not rule out an analytic construction that uses the successor scaffold together with actual prime values, prime gaps, residues, character values, or source-dependent weights. It says that those additional data, not the rigidity of the scaffold, are where the arithmetic information then resides and must be priced.

## 5. Consequence for the relational-lift frontier

`MC-433` ended with three audits: symmetry, provenance, and post-projection analytic usefulness. The successor-chain control shows that the first two are still insufficient when interpreted only as “small automorphism group” plus “canonically generated relation.”

A more discriminating ledger is:

1. **Internal addressability:** how many factor partitions survive the automorphism quotient? This is what `Q_R` and `A(R)` measure.
2. **Conditional source diversity:** after conditioning on coarse invariants such as `r=omega(n)`, how many non-isomorphic relational instances can actually occur as the arithmetic source varies?
3. **Post-projection survival:** which part of that source-varying information reaches the signed coefficient or cancellation observable?

The canonical order has maximal item 1, minimal item 2, and under factorwise Möbius sign it also fails item 3.

The next first-kill test for a relational escape should therefore not ask only whether the relation is rigid and arithmetic. It should first quotient away universal rank scaffolds and identify the **source-varying residue** of the relation. For an ordered prime-divisor construction this means that gaps, ratios, residue labels, edge weights, or other decorations must carry the genuine source variation; the bare chain does not. Those decorations then require their own precision, symmetry, and analytic-survival audit.

## Prior art and novelty boundary

The order-theoretic ingredients are elementary and classical. Every finite linear order of a fixed cardinality is order-isomorphic to the same finite ordinal, and an order-preserving automorphism of a finite linear order is the identity. No novelty is claimed for either fact.

The broader distinction between rigidity and definable/canonical ordering is standard in finite model theory. Yuri Gurevich and Saharon Shelah, *On finite rigid structures*, Journal of Symbolic Logic **61** (1996), 549--562, DOI `10.2307/2275675`, arXiv `math/9411236`, explicitly notes that a definable linear order makes a finite structure rigid and studies why the converse direction is much subtler. That literature is adjacent prior art, not evidence for a Möbius theorem.

No novelty is claimed for finite-order rigidity, directed paths, Bell numbers, or automorphism-orbit counting. The durable Mathia contribution is the **frontier specialization**: the canonical increasing order of the prime divisors gives an explicit source-native, sparse, rigid relation that saturates the internal Bell factor-capacity test while having a single isomorphism type at fixed `omega(n)`. This proves that automorphism asymmetry and canonical generation are not themselves measures of source-specific arithmetic information.

## Boundaries and falsification tests

- **Conditioning on `r` is explicit.** The successor structure reveals its cardinality, so across all squarefree integers it retains `omega(n)`. The zero-diversity statement is conditional on fixed `r`; it does not claim the relation carries literally no source information.
- **Squarefreeness is load-bearing for the Bell factor model.** Repeated prime powers require exponent data in addition to the ordered support.
- **Direction is load-bearing for exact rigidity.** Forgetting orientation leaves an undirected path with a reflection symmetry, but this changes the orbit count only by at most a factor two and does not restore source-type diversity.
- **Construction cost is not being claimed.** Defining the relation presupposes access to the prime divisors of `n`; the result is a representation audit, not an efficient factorization algorithm.
- **The partition itself may depend on source values.** If an analytic rule selects or weights `pi` using the numerical primes, that rule has reintroduced source-specific data. Equation `(10)` applies only when the observable genuinely factors through the order-plus-partition isomorphism type.
- **A universal scaffold can still be analytically useful as coordinates.** The result does not say ordered coordinates are useless; it says their usefulness cannot be credited as retained arithmetic information unless the source-varying data that interact with them are identified.
- **Weighted or decorated successor chains are not ruled out.** They are precisely the surviving escape. Their edge/vertex decorations must be audited for isomorphism-type diversity, retained precision, and survival into the Möbius-facing operation.
- **No zero information or analytic continuation is used.** The argument is finite order theory plus the previously established factor-partition dictionary.

The immediate frontier is therefore narrower than after `MC-433`: search for a canonical relational decoration whose **isomorphism class varies nontrivially among equal-`omega` sources** and whose variation survives a signed analytic projection. A relation that merely rigidifies a universal coordinate frame has escaped permutation collapse but has not yet carried arithmetic cancellation information.