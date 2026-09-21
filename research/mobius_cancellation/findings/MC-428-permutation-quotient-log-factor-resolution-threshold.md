# MC-428 — Permutation quotient raises logarithmic factor precision threshold to inverse-log scale

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · CLASSICAL-INGREDIENTS · FRONTIER-ADVANCE · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-427` counts **ordered** words of quantized factor log-sizes and shows that sub-power-of-`log X` precision has only subpolynomial state volume. That leaves a broad intermediate regime: an ordered factorization can acquire polynomially many nominal states once the logarithmic mesh becomes inverse-polylogarithmic, even when the downstream mechanism does not intrinsically distinguish factor-slot labels.

Quotienting those artificial slot permutations changes the capacity scale sharply.

Let `n<=X` be squarefree, put `r=omega(n)`, and consider every ordered active factorization

\[
n=u_1\cdots u_d,
\qquad 1\le d\le r,
\qquad u_j>1.
\tag{1}
\]

For a logarithmic mesh `eta>0`, retain each factor only through

\[
q_j=Q_\eta(u_j)
:=
\left\lfloor\frac{\log u_j}{\eta}\right\rfloor.
\tag{2}
\]

Suppose the retained observable is invariant under permutations of the factor coordinates, so its raw state is the unordered multiset

\[
\{q_1,\ldots,q_d\}.
\tag{3}
\]

Write

\[
L:=\left\lfloor\frac{\log n}{\eta}\right\rfloor
\le
\frac{\log X}{\eta}.
\tag{4}
\]

If `N_sym(n,eta)` denotes the number of distinct permutation-orbit states `(3)` across **all active depths**, then

\[
\boxed{
N_{\rm sym}(n,\eta)
\le
(r+1)\sum_{s=0}^{L}p(s)
\le
(r+1)(L+1)p(L),
}
\tag{5}
\]

where `p(s)` is the ordinary integer-partition function. By the Hardy--Ramanujan asymptotic,

\[
\log p(L)
=
\pi\sqrt{\frac{2L}{3}}+o(\sqrt L),
\tag{6}
\]

so, whenever `L->infinity`,

\[
\boxed{
\log N_{\rm sym}(n,\eta)
\le
\pi\sqrt{\frac{2L}{3}}
+o(\sqrt L)
+O(\log L+\log\log X).
}
\tag{7}
\]

In particular, for any fixed `0<=delta<1`,

\[
\eta^{-1}\le (\log X)^{\delta+o(1)}
\tag{8}
\]

implies

\[
\boxed{N_{\rm sym}(n,\eta)=X^{o(1)}}
\tag{9}
\]

uniformly for squarefree `n<=X`.

Thus **every inverse-polylogarithmic log-size mesh strictly coarser than `1/log X` still has only subpolynomial permutation-invariant state volume**. This is much stronger than the ordered-word threshold in `MC-427`.

There is a quantitative converse. If, for some fixed `alpha>0`, a permutation-invariant scalar log-size channel has

\[
N_{\rm sym}(n,\eta)\ge X^\alpha
\tag{10}
\]

along an unbounded sequence of `X`, then necessarily

\[
\boxed{
\liminf
\frac{\eta^{-1}}{\log X}
\ge
\frac{3\alpha^2}{2\pi^2}
}
\tag{11}
\]

along that sequence, with the statement interpreted trivially when the ratio tends to infinity. In particular, polynomial orbit-state capacity forces

\[
\boxed{\eta^{-1}=\Omega(\log X).}
\tag{12}
\]

So the interval between the ordered threshold of `MC-427` and inverse-logarithmic precision can be entirely **factor-order capacity**. A factor-size mechanism whose final readout is symmetric in the extracted factor slots cannot credit that capacity as independent source information.

This is an information-capacity obstruction only. It gives no new bound for `M(x)`, no character-sum estimate, and no RH consequence.

## Exact orbit count

From `(1)` and `(2)`,

\[
\sum_{j=1}^d q_j
\le
\left\lfloor
\frac{1}{\eta}\sum_{j=1}^d\log u_j
\right\rfloor
=
\left\lfloor\frac{\log n}{\eta}\right\rfloor
=L.
\tag{13}
\]

Fix one permutation orbit of `(q_1,\ldots,q_d)`. Remove the zero entries and sort the positive entries in nonincreasing order. The result is an ordinary integer partition of

\[
s=\sum_j q_j,
\qquad 0\le s\le L.
\tag{14}
\]

Conversely, the positive partition together with the number `z` of zero entries determines the complete multiset `(3)`. Since `d<=r`, one has `0<=z<=r`. We therefore obtain

\[
N_{\rm sym}(n,\eta)
\le
(r+1)\sum_{s=0}^{L}p(s).
\tag{15}
\]

The partition function is nondecreasing, giving the second inequality in `(5)`.

The squarefree hypothesis also gives the elementary depth bound

\[
2^r\le n\le X,
\qquad
r\le\frac{\log X}{\log 2},
\tag{16}
\]

so the factor `(r+1)` contributes only `O(log log X)` to the logarithm. Applying `(6)` proves `(7)`.

Under `(8)`, equation `(4)` gives

\[
L
\le
(\log X)^{1+\delta+o(1)}.
\tag{17}
\]

Because `delta<1`,

\[
\sqrt L
\le
(\log X)^{(1+\delta)/2+o(1)}
=o(\log X),
\tag{18}
\]

and `(7)` yields `(9)`.

## The inverse-log threshold constant

Assume `(10)`. If `eta^{-1}/log X` is unbounded along the relevant sequence, `(12)` is automatic. Otherwise pass to any subsequence on which

\[
\frac{\eta^{-1}}{\log X}\le C+o(1)
\tag{19}
\]

for a finite constant `C`. Then

\[
L\le (C+o(1))(\log X)^2.
\tag{20}
\]

Equations `(5)`--`(7)` therefore imply

\[
\alpha\log X
\le
\pi\sqrt{\frac{2C}{3}}\,\log X
+o(\log X).
\tag{21}
\]

Hence

\[
C\ge\frac{3\alpha^2}{2\pi^2}.
\tag{22}
\]

Since this applies to every finite subsequential upper limit compatible with `(10)`, it gives `(11)`.

The numerical constant is secondary. The structural point is the change in entropy law:

- ordered quantized factor words are bounded by weak-composition counts, whose logarithm is proportional to the available factor depth;
- unordered quantized factor states are bounded by integer partitions, whose logarithm grows only like `sqrt(L)`.

That change moves the first possible polynomial-capacity scale from a generic inverse power of `log X` all the way to the inverse-logarithmic boundary.

## Relation to the current frontier

`MC-423` showed that exact fixed-product fibers at fixed factor depth have only subpolynomial tangent volume. `MC-424` showed that fixed-depth lifts cannot amplify the shell exponent. `MC-425` and `MC-426` then priced growing depth after projecting each factor to sign-only or bounded fixed-dimensional additive data. `MC-427` handled the first natural unbounded additive statistic, logarithmic factor size, but deliberately counted **ordered** factor words.

The present result isolates a missing distinction in that escape. Many analytic decompositions introduce named factor slots, but a named slot is useful information only if the mathematics later treats it asymmetrically or preserves a relation tied to that label. If all downstream processing is invariant under permuting slots, the correct state space is not the weak-composition space from `MC-427`; it is the partition quotient `(5)`.

This mirrors the earlier source-site lesson in `MC-204`, where full permutation invariance of a ternary source vector collapses exponentially many labelled configurations to a small orbit space. The two statements are mathematically different: `MC-204` classifies finite-alphabet source-site orbits exactly through symbol counts, whereas the present finding gives a quantitative partition bound for **quantized factor magnitudes across variable factorization depth**.

The surviving log-size route is consequently sharper. A candidate must do at least one of the following:

1. retain factor slots with an intrinsic asymmetric role and prove that the role survives the analytic architecture;
2. retain scalar log-size at inverse-logarithmic or finer precision;
3. retain higher-dimensional, nonadditive, relational, or exact factor data not covered by the scalar permutation quotient.

Passing any of these tests only escapes this counting obstruction; it does not itself produce cancellation.

## Prior art and novelty boundary

All combinatorial ingredients are classical. Hardy and Ramanujan's 1918 paper *Asymptotic formulæ in combinatory analysis*, Proc. London Math. Soc. (2) **17**, 75--115, gives the partition asymptotic used in `(6)`; the unrestricted partition function is also recorded in NIST DLMF §27.14.

The distinction between ordered/labeled and unordered multiplicative factorizations has its own established literature. E. Rodney Canfield, Paul Erdős and Carl Pomerance, *On a Problem of Oppenheim concerning “Factorisatio Numerorum”*, Journal of Number Theory **17** (1983), 1--28, DOI `10.1016/0022-314X(83)90002-1`, studies unordered multiplicative factorizations. Augustine O. Munagi, *Labeled Factorization of Integers*, Electronic Journal of Combinatorics **16** (2009), R50, DOI `10.37236/139`, treats labeled-factor variants and their relation to multiplicative partitions. `MC-427` already records nearby ordered-factorization literature.

A targeted search of multiplicative partitions, unordered factorizations, logarithmic factor encodings, and integer-partition bounds found the component mechanisms above but no reason to promote `(5)`--`(12)` as a standalone new number-theoretic theorem. **No novelty is claimed** for partition asymptotics, multiplicative-partition theory, or the labelled/unlabelled distinction.

The durable contribution is the mechanism-specific frontier consequence: once factor-slot order is quotiented out, the coarse logarithmic-size escape left by `MC-427` remains subpolynomial throughout every fixed inverse-polylogarithmic precision regime below `1/log X`.

## Limits and decisive test

- **Permutation invariance is load-bearing.** In Heath-Brown/Ramaré-type decompositions, factor variables can have genuinely different coefficient supports, ranges, primality constraints, or analytic roles. Such labels must not be quotiented away merely for convenience.
- **This is a scalar log-size statement.** Several retained coordinates lead to vector-partition rather than ordinary-partition counting and require a separate analysis.
- **Quantization is load-bearing.** Exact `log u` determines the integer `u`; exact factor identities are outside this coarse-state theorem.
- **Capacity is not usefulness.** Reaching the inverse-log threshold only makes polynomial orbit-state count combinatorially possible. It supplies no independence, Fourier bandwidth, correlation estimate, or positive-kernel gain.
- **The bound intentionally ignores arithmetic realizability.** Not every integer partition in `(5)` comes from prime-factor blocks of one `n`; enforcing realizability can only reduce the state family.
- **No zeta zero information is used.** The proof is finite combinatorics plus `sum_j log u_j=log n`.

A proposed high-precision factor-size escape now has a direct first-kill test: state whether factor slots are mathematically intrinsic or merely names introduced by a decomposition. If the final readout is permutation-invariant, quotient them and apply `(5)` before crediting state volume. If the slots are intrinsically asymmetric, identify the exact asymmetric structure and show that it survives subsequent Cauchy/positive closure. Only after that representation audit is it meaningful to ask whether the retained precision produces new Möbius cancellation.