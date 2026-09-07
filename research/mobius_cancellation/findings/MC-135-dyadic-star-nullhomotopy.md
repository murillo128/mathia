# MC-135 — Dyadic divisor-filtration inclusions factor through the prime-2 star

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Let `Delta_n` be Björner's simplicial complex whose simplices are the prime-factor sets `P(m)` of squarefree integers `m<=n`. For integers

\[
2\le a\le b,
\qquad b\ge 2a,
\]

the canonical inclusion

\[
i_{a,b}:\Delta_a\hookrightarrow\Delta_b
\]

factors through the closed star of the vertex `2` in `Delta_b`:

\[
\boxed{
\Delta_a\subseteq \operatorname{st}_{\Delta_b}(2)\subseteq\Delta_b.
}
\tag{1}
\]

Since a simplicial star is a cone, `st_{Delta_b}(2)` is contractible. Therefore

\[
\boxed{i_{a,b}\text{ is null-homotopic whenever }b\ge2a.}
\tag{2}
\]

This strengthens the factor-two homology-transport vanishing in `MC-134`. The ordinary one-parameter divisor filtration has no long-range carrier not only at the level of persistent homology: **every scale-separated inclusion becomes trivial already in the ordinary homotopy category after one dyadic step**.

The factor `2` is sharp as a uniform threshold. If `p` is an odd prime and

\[
p\le b<2p,
\]

then the vertex `p` is an isolated connected component of both `Delta_p` and `Delta_b`. Hence the inclusion `Delta_p -> Delta_b` induces a nonzero map on reduced `H_0`. In particular, no universal multiplicative constant strictly smaller than `2` can replace the threshold in `(2)`.

Thus the residual topological route left by `MC-133`--`MC-134` narrows further: an inter-scale mechanism built only from the ordinary homotopy type of the spaces and the inclusion maps cannot carry nontrivial information across arbitrarily many multiplicative scales. A surviving divisor-topology mechanism must use structure not killed by the prime-2 star factorization, such as arithmetic labels or chain-level data not invariant under homotopy, additional algebraic operations with genuinely new information, higher coherence not determined by the individual homotopy-category maps, or a genuinely different/multiparameter filtration.

## 1. Every earlier simplex lies in the prime-2 star after doubling the scale

A simplex of `Delta_a` is `P(m)` for a squarefree integer `m<=a`. Recall that a face `F` belongs to the closed star of a vertex `v` precisely when

\[
F\cup\{v\}\in\Delta_b.
\]

Take `F=P(m)`.

If `m` is even, then `2\in P(m)`, so

\[
P(m)\cup\{2\}=P(m)\in\Delta_b.
\]

If `m` is odd, then `2m` is squarefree and

\[
2m\le2a\le b.
\]

Therefore

\[
P(m)\cup\{2\}=P(2m)\in\Delta_b.
\]

Both cases place every simplex of `Delta_a` in `st_{Delta_b}(2)`, proving `(1)`.

The argument uses the exact rational-prime/divisor structure of the filtration. It is not a generic statement about nested simplicial complexes: multiplication by the distinguished smallest prime `2` is what makes the whole earlier complex conical inside the doubled-scale complex.

## 2. The inclusion is null-homotopic, not merely homologically zero

The closed star of any vertex is the simplicial cone

\[
\{2\} * \operatorname{lk}_{\Delta_b}(2)
\]

and is therefore contractible. Equation `(1)` gives the factorization

\[
\Delta_a
\longrightarrow
\operatorname{st}_{\Delta_b}(2)
\longrightarrow
\Delta_b.
\]

Any map factoring through a contractible space is null-homotopic, proving `(2)`.

Consequently every homotopy-invariant functor sees zero long-range transport across a factor-two gap. In particular, all induced maps on reduced homology and reduced cohomology vanish, and every based homotopy-group map carried by such an inclusion is trivial. The reduced-homology statement recovers the rank-zero consequence of `MC-134`, but the star proof does not use boundary-matrix reduction or the explicit barcode.

This matters for the information audit. Replacing persistent homology by another ordinary homotopy invariant of the **same inclusion filtration** cannot by itself restore a long-lived scale-to-scale class: the actual structure map is already null-homotopic.

## 3. The dyadic threshold is uniformly optimal

Let `p` be any odd prime. At filtration value `p`, the newly appearing vertex `p` has no edge to any other vertex because every product `pq` with a prime `q>=2` exceeds `p`. More generally, while `b<2p`, even the smallest possible coface `P(2p)` has not entered, so `p` remains isolated in `Delta_b`.

Thus for every integer `b` with

\[
p\le b<2p,
\]

the connected component represented by the vertex `p` survives under

\[
\Delta_p\hookrightarrow\Delta_b.
\]

There is also at least the component containing the vertex `2`, so the corresponding reduced `H_0` class is nonzero and maps nontrivially. Choosing arbitrarily large odd primes shows that for every fixed ratio `1<c<2` there are arbitrarily large pairs with `b/a` as close to `c` as desired for which the inclusion is not even homologically trivial.

This agrees with, but does not depend on, the exact bars `[m,2m)` of `MC-134`: the first possible universal death scale really is doubling.

## Prior art and novelty assessment

Anders Björner, *A cell complex in number theory*, Advances in Applied Mathematics 46 (2011), 71--85, DOI `10.1016/j.aam.2010.09.007`, arXiv `1101.5704`, is the primary source for `Delta_n`, its shifted-complex structure, its wedge-of-spheres homotopy type, and its Betti-number formula. Björner's proof explicitly uses the ordered prime vertices with `2` as the smallest prime, and multiplication by `2` is also the elementary bijection underlying his odd/even squarefree decompositions.

The only additional topological fact used here is classical: the closed star of a vertex in a simplicial complex is a cone and hence contractible. Targeted searches of Björner's paper and for number-theoretic divisor-complex persistence/null-homotopy statements did not locate the particular factorization `(1)`--`(2)`. That search result is **not** a novelty claim. The result is stored as a direct line-specific deduction from Björner's established complex, not as a new theorem of algebraic topology.

`MC-134` already proves that the full reduced persistent-homology barcode consists of intervals `[m,2m)` for odd squarefree `m>1`. The present result is not a second proof dressed as a new mechanism: its durable addition is the stronger statement that the **space-level inclusion itself** factors through a contractible arithmetic subcomplex at the same threshold.

## Boundaries and falsification tests

- The claim concerns the original one-parameter filtration `Delta_1 subset Delta_2 subset ...` and its ordinary simplicial inclusions. It does not classify a genuinely different or multiparameter filtration.
- Pairwise null-homotopy does not assert that every possible coherent system of chosen null-homotopies is itself information-free. Higher coherence would need a separate definition and a source-natural statistic before it could be assessed.
- The factorization does not erase arithmetic labels attached to simplices, chains, or gradient paths. A statistic that deliberately retains such labels need not factor through the ordinary homotopy category; it must still show an independently cheaper route to Mertens amplitude.
- Single-scale topology remains arithmetically nontrivial. Björner's wedge multiplicities encode the same terminal odd-squarefree parity burden described in `MC-133`; `(2)` only classifies long-range transport of the standard inclusions.
- Sub-dyadic transport is genuinely present. The prime example above prevents interpreting the factor-two vanishing as an artifact of a loose estimate.
- The proof uses no zeta continuation, zero-free region, Mertens estimate, random model, or numerical evidence.

The exact factorization can be falsified by producing a squarefree `m<=a` with `P(m)` outside `st_{Delta_b}(2)` for some `b>=2a`. The two parity cases above exhaust all squarefree `m`, so such a counterexample would have to violate either squarefreeness of `2m` for odd `m` or the inequality `2m<=b`.

## Consequence for the line

`MC-133` showed that static ordinary topology stores the hard sign information as a parity imbalance, and `MC-134` showed that persistent homology has only dyadic-length bars. `MC-135` closes the next immediate escape: **changing the homology functor while keeping the same ordinary homotopy-level filtration does not create long-range transport**, because every inclusion across a factor-two gap is already null-homotopic through the prime-2 star.

The accepted source-to-amplitude frontier should therefore no longer treat generic homotopy-invariant inter-scale structure of Björner's one-parameter filtration as an unexplored carrier. The remaining divisor-topology possibilities must retain information beyond these homotopy-category maps—most plausibly arithmetic labels/chain structure, higher coherent data with a proved nontrivial source statistic, or a different filtration whose structure maps do not admit the same dyadic coning argument.