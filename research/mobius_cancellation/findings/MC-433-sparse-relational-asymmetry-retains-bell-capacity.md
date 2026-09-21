# MC-433 — Sparse relational asymmetry can retain full Bell factor capacity

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-INGREDIENTS · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-430` shows that exact prime identity gives the unordered factor partitions of a squarefree `r`-prime integer their full Bell-number state family, while `MC-431`--`MC-432` quantify how much of that family survives when prime identities are collapsed to color classes. Those results leave open a materially different escape: a retained **relation among the prime coordinates** can distinguish primes without assigning each prime an explicit high-cardinality color.

There is an exact general lower bound for this case, and it changes the first-kill test.

Let

\[
P=\{p_1,\ldots,p_r\}
\]

be the distinct prime divisors of a squarefree integer, let `R` be any relational structure on `P`, and let

\[
G=\operatorname{Aut}(R)\le S_r
\]

be the permutations of the prime coordinates that preserve that retained relation. Let `\Pi(P)` be the set of unordered set partitions of `P`, equivalently the unordered active factorizations used in `MC-430`, so `|\Pi(P)|=B_r`. If only the relation `R` rather than literal prime labels is retained, the surviving factor states are the orbits

\[
Q_R:=|\Pi(P)/G|.
\]

Then

\[
\boxed{
\frac{B_r}{|\operatorname{Aut}(R)|}
\le Q_R\le B_r.
}
\tag{1}
\]

The lower bound is immediate because every orbit has size at most `|G|`; equivalently Burnside gives

\[
Q_R=\frac1{|G|}\sum_{g\in G}|\operatorname{Fix}_{\Pi(P)}(g)|.
\tag{2}
\]

Define the symmetry-breaking budget

\[
A(R):=\log\frac{r!}{|\operatorname{Aut}(R)|}.
\tag{3}
\]

Using the Bell estimate already audited in `MC-430`--`MC-432`,

\[
\log\frac{r!}{B_r}=O(r\log\log r),
\]

so `(1)` yields

\[
\boxed{
\log Q_R\ge A(R)-O(r\log\log r).
}
\tag{4}
\]

Along the squarefree primorials

\[
N_r=\prod_{j\le r}p_j,
\qquad
\log N_r=(1+o(1))r\log r,
\]

this has a sharp qualitative consequence:

\[
\boxed{
\log|\operatorname{Aut}(R)|=o(r\log r)
\quad\Longrightarrow\quad
Q_R=N_r^{1-o(1)}.
}
\tag{5}
\]

More generally, if

\[
A(R)\ge (\alpha+o(1))r\log r
\]

for fixed `0<alpha<=1`, then

\[
Q_R\ge N_r^{\alpha-o(1)}.
\tag{6}
\]

This is deliberately a **one-sided capacity law**. A small automorphism group is sufficient to guarantee large factor-state capacity, but it is not claimed to be necessary: stabilizers of individual set partitions and the detailed action of `G` can make the orbit count larger than the crude group-size lower bound.

The key obstruction is therefore different from `MC-432`:

> **For general relational lifts, a small alphabet, bounded local degree, or only `O(r)` relation incidences does not imply low factor-state capacity. A sparse relation can break essentially all prime-coordinate symmetry and thereby retain the full Bell exponent.**

This is a representation-capacity statement only. It gives no estimate for `M(x)` and no RH consequence.

## 1. General relational quotient law

The color quotients of `MC-431`--`MC-432` are a special case. A coloring with class sizes `r_1,...,r_k` has automorphism group

\[
S_{r_1}\times\cdots\times S_{r_k},
\]

so

\[
A(R)=\log\frac{r!}{\prod_a r_a!},
\]

which is exactly the multinomial distinguishability budget `D` in `MC-432`.

For colors, much more is available than `(4)`: the exact vector-partition classification supplies the matching upper bound up to `o(r log r)`. For a general relation `R`, the group-action lower bound survives without such a classification. This is enough to show that the color-alphabet law cannot be extrapolated to arbitrary relational structure by counting relation symbols or incidences alone.

The natural invariant at this level is not the number of relation types but the amount of prime-permutation symmetry that the retained structure destroys. If `R` leaves a group of size nearly `r!`, then the lower bound may be small. If `R` has only subexponentially many automorphisms on the `r log r` scale, it already guarantees near-full Bell capacity.

## 2. A sparse bounded-degree relation can be fully asymmetric

The phenomenon does not require a dense relation. For every `r>=7`, construct a tree `T_r` with one central vertex and three path arms of lengths

\[
1,\qquad 2,\qquad r-4.
\]

This tree has `r` vertices, `r-1` edges, and maximum degree `3`. Its automorphism group is trivial.

Indeed, the center is the unique degree-`3` vertex and must be fixed by every automorphism. The three arms have distinct lengths because `r-4>=3`, so every arm must be preserved setwise. Once the center endpoint of a path arm is fixed, the path has no remaining nontrivial automorphism. Therefore every vertex is fixed and

\[
\operatorname{Aut}(T_r)=\{1\}.
\tag{7}
\]

Consequently

\[
Q_{T_r}=B_r,
\tag{8}
\]

so this binary pair relation with only `r-1` incidences preserves **all** unordered factor-partition states. Along primorials,

\[
Q_{T_r}=N_r^{1-o(1)}.
\tag{9}
\]

This gives an explicit matched non-arithmetic control against a tempting extension of `MC-432`: linear edge count and bounded degree do not constitute a low-information relational quotient.

The construction is intentionally elementary. Classical graph theory contains much stronger realization results: Frucht proved that every finite group can occur as the automorphism group of a finite graph, and later showed such realization can be achieved by cubic graphs. No novelty is claimed for asymmetric graphs, asymmetric trees, or graph-automorphism realization.

## 3. Why sparse incidence is not sparse information

The apparent paradox is resolved by distinguishing **description sparsity** from **identity information**. A graph with `O(r)` edges can still use the identities of its endpoints to individualize all `r` vertices. The edge count measures how many pair relations are present, not how many prime-coordinate permutations they exclude.

A simple family-size calibration makes the scale visible. Cayley's classical formula counts

\[
r^{r-2}
\]

labeled trees on `r` vertices, whose logarithm is

\[
(r-2)\log r=(1-o(1))r\log r.
\]

Thus even the class of sparse trees has identity-scale combinatorial capacity. An arbitrary sparse graph relation attached to the prime coordinates may therefore be little more than a compressed encoding of the original labels, despite having only linearly many edges.

This is exactly why `(3)` is useful as a first audit. The quantity

\[
A(R)=\log(r!/|\operatorname{Aut}(R)|)
\]

prices how strongly the relation individualizes the source coordinates under relabeling. It does **not** price how naturally or cheaply that relation is generated arithmetically. Those are separate obligations.

## 4. Relation to the current Möbius frontier

`MC-423`--`MC-429` show that tangent dimension, factor multiplicity, coarse additive summaries, and fixed-dimensional quantized data cannot manufacture polynomial factor-state capacity without paying dimension or precision. `MC-430` identifies exact labeled factor incidence as a genuine capacity escape. `MC-431`--`MC-432` then show that compressing labels to color classes retains a polynomial fraction of Bell capacity only when the color system itself carries a comparable fraction of the full prime-label distinguishability budget.

The present result closes the naive next shortcut: replacing high-cardinality colors by a sparse pair relation does not automatically reduce that budget. A bounded-degree relation can have trivial automorphism group and therefore preserve the complete Bell state family.

The surviving question is consequently narrower and more arithmetic. A proposed relational lift must now answer three independent questions:

1. **Symmetry:** how much prime-coordinate symmetry does the relation actually break? `A(R)` gives a general lower-bound audit.
2. **Provenance:** is that asymmetry forced by canonical arithmetic relations available before the target cancellation is known, or is it merely a disguised near-lossless encoding of prime identity?
3. **Analysis:** after coefficient formation, Möbius projection, averaging, or the intended bilinear operation, does the relation still contribute a signed cancellation mechanism rather than only decoding capacity?

Passing the first question is necessary for escaping the recent state-count barriers but is not evidence for either of the latter two.

## 5. Representation-match map

The same statement can be read in the existing factor-incidence languages.

- **Set-partition view:** unordered active factorizations are `\Pi(P)`. Retaining `R` but forgetting literal prime names means quotienting only by permutations that preserve `R`, hence `\Pi(P)/\operatorname{Aut}(R)`.
- **Incidence-matrix view:** rows are prime coordinates and columns are factor blocks. Factor-slot permutations remove column order. The relation `R` restricts the allowed row permutations from `S_r` to `\operatorname{Aut}(R)`.
- **Symmetry-quotient view:** `A(R)` measures how much of the original row-permutation symmetry the retained relation destroys. The orbit lower bound `(1)` is independent of coordinates or a chosen encoding of `R`.
- **Information view:** a sparse relation may still have identity-scale distinguishability because its endpoint incidences can individualize the rows. Edge count is therefore not a valid substitute for a quotient-entropy or automorphism audit.

No ordinary matrix-rank statement is implied. The load-bearing object here is the permutation action preserving the relation.

## Prior art and novelty boundary

The group-action ingredients are classical: Burnside's lemma and the elementary orbit-size bound give `(1)`--`(2)`. Bell-number asymptotics and the primorial calibration are inherited from the audited ingredients in `MC-430`--`MC-432`.

For graph automorphisms, Robert Frucht, *Herstellung von Graphen mit vorgegebener abstrakter Gruppe*, Compositio Mathematica **6** (1939), 239--250, proves the classical realization theorem for finite automorphism groups; the primary archive is https://www.numdam.org/item/CM_1939__6__239_0/. Frucht's later *Graphs of Degree Three with a Given Abstract Group*, Canadian Journal of Mathematics **1** (1949), 365--378, DOI `10.4153/CJM-1949-033-6`, gives the bounded-degree realization boundary. Cayley's labeled-tree formula is likewise classical.

No novelty is claimed for orbit counting, automorphism groups, asymmetric graphs or trees, Frucht's theorem, Cayley's formula, or Bell asymptotics. The durable Mathia contribution is the **frontier specialization**: applying the automorphism quotient directly to the exact-factor escape of `MC-430` shows that `MC-432`'s prime-color entropy obstruction is not an obstruction to general sparse relational lifts. Sparse relational asymmetry can preserve the full Bell exponent, so future proposals must audit canonical arithmetic provenance and post-projection analytic usefulness rather than infer low information from sparse incidence alone.

## Boundaries and falsification tests

- **Squarefreeness is load-bearing for the set-partition factor model.** Repeated prime powers require exponent-multiset structure.
- **The theorem is a lower-bound resource law, not a complete orbit classification.** Small `|Aut(R)|` guarantees large `Q_R`; large `|Aut(R)|` does not by itself prove small `Q_R`.
- **The asymmetric tree is a control, not an arithmetic candidate.** An arbitrary assignment of such a tree to the rational primes can hide essentially the same identity information that the previous color audit was trying to price.
- **Sparse edge count is not an information budget.** Any proposed complexity measure based only on number of relation incidences, bounded degree, or finite relation type is falsified by `(7)`--`(9)` unless additional invariance or generation constraints are imposed.
- **Automorphism asymmetry is not analytic usefulness.** A rigid relation may preserve every factor state and still be destroyed by Möbius sign projection or contribute no cancellation at all.
- **Canonical arithmetic provenance is now load-bearing.** A viable relational escape must arise from an exact arithmetic rule on the primes, not from an externally chosen graph whose only purpose is to individualize them.
- **Post-projection survival remains load-bearing.** Even a canonical asymmetric relation must be traced through the actual coefficient/source map; if the downstream observable factors through a coarser quotient, the relevant automorphism group is that of the surviving datum, not that of the upstream relation.

The next first-kill test is therefore two-stage. First compute or bound the prime-permutation group that preserves the **actual surviving relational datum**, rather than counting its edges or relation symbols. If that group is small enough to pass `(4)`, then audit whether the symmetry breaking is independently forced by arithmetic and whether it survives into a signed estimate. A construction that passes only the automorphism test has escaped a capacity obstruction, not advanced Möbius cancellation.