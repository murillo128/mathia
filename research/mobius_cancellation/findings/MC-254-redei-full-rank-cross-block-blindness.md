# MC-254 — Maximal Rédei rank can coexist with a rank-one Legendre cross-block

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-ARITHMETIC-CONTROL`, `FRONTIER-REFINEMENT`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the quadratic shell matrix from `MC-238`, `MC-252`, and `MC-253`. For odd primes in two disjoint sets

\[
P=\{p_1,\dots,p_k\},
\qquad
S=\{r_1,\dots,r_m\},
\]

write

\[
A_{p,r}=\frac{1-(\frac pr)}2\in\mathbb F_2.
\tag{1}
\]

A natural possible continuation after `MC-253` is to replace bounded-order parity statistics by algebraic-number-theoretic structure. The closest classical object is the Rédei matrix attached to a quadratic discriminant whose prime-discriminant factors are the primes in `P\cup S`.

That connection is exact at the cross-block level. For an odd prime `q`, put

\[
q^*=(-1)^{(q-1)/2}q.
\tag{2}
\]

If the off-diagonal Rédei entry in row `p`, column `r` is the additive bit of the Kronecker symbol `(r^*/p)`, quadratic reciprocity gives

\[
\boxed{
\left(\frac{r^*}{p}\right)=\left(\frac pr\right).
}
\tag{3}
\]

Thus the odd-prime shell matrix `(1)` is literally a rectangular off-diagonal block of a classical Rédei matrix.

However, **the rank of the full Rédei matrix does not control the rank of this cross-block**. In fact there are genuine prime-discriminant Rédei matrices with the maximal possible rank `n-1` while a prescribed bipartite cross-block has rank only `1`.

More precisely, for every `k,m>=1` there exist distinct primes

\[
q_1,\dots,q_{k+m}\equiv1\pmod4
\]

such that, for the positive fundamental discriminant

\[
D=\prod_{i=1}^{k+m}q_i,
\tag{4}
\]

the standard binary Rédei matrix `R_D` is the mod-2 Laplacian of the path

\[
1-2-\cdots-(k+m).
\tag{5}
\]

Consequently

\[
\boxed{\operatorname{rank}_{\mathbb F_2}R_D=k+m-1,}
\tag{6}
\]

which is the maximal possible rank because every Rédei row sums to zero, while after the cut

\[
\{1,\dots,k\}\sqcup\{k+1,\dots,k+m\}
\tag{7}
\]

the off-diagonal Legendre block has exactly one nonzero entry and hence

\[
\boxed{\operatorname{rank}_{\mathbb F_2}A=1.}
\tag{8}
\]

By the classical Rédei rank formula, the example `(4)` has narrow class-group `4`-rank zero. Therefore even the strongest possible scalar conclusion at the ordinary Rédei/`4`-rank level does **not** force the lower-prime / shell-prime Legendre block to have large rank.

The obstruction is structural rather than quantitative. If a full Rédei matrix is partitioned as

\[
R=\begin{pmatrix}
C&A\\
A^{\mathsf T}&E
\end{pmatrix},
\tag{9}
\]

then for `v\in\ker A`,

\[
R\binom0v=\binom0{Ev}.
\tag{10}
\]

Hence full Rédei nullity sees only the stricter subspace

\[
\boxed{
\ker A\cap\ker E,
}
\tag{11}
\]

among vectors supported on the shell block. The shell-shell block `E` can annihilate the visibility of a very large `\ker A` in the full class-group invariant.

This closes one tempting post-`MC-253` shortcut: a theorem showing that a quadratic field built from the same prime-discriminant factors has small or zero `4`-rank would not, by itself, prove the shell generation condition `H=G` or high rank of `A`.

The result does **not** say that the actual Mathia shell matrix has rank one, does not construct the path pattern with the actual lower primes or with all column primes in `(y,2y]`, and gives no estimate for `M(X)`. As in `MC-252`, tight localization and the fixed source prime set remain load-bearing.

## 1. The shell Legendre matrix is an exact Rédei cross-block

Let `p` and `r` be distinct odd primes. From `(2)`,

\[
\left(\frac{r^*}{p}\right)
=
\left(\frac{-1}{p}\right)^{(r-1)/2}
\left(\frac rp\right).
\tag{12}
\]

The supplementary law and quadratic reciprocity give

\[
\left(\frac{-1}{p}\right)^{(r-1)/2}
=(-1)^{(p-1)(r-1)/4}
\tag{13}
\]

and

\[
\left(\frac rp\right)
=(-1)^{(p-1)(r-1)/4}
\left(\frac pr\right).
\tag{14}
\]

The signs cancel, proving `(3)`.

Now form the signed fundamental discriminant

\[
\Delta=\prod_{q\in P\cup S}q^*.
\tag{15}
\]

The classical Rédei matrix for `\Delta` has off-diagonal entries given by the additive bits of the symbols `(q_j^*/q_i)` and a diagonal chosen so that the row/column-sum relation holds. By `(3)`, the rows indexed by `P` and columns indexed by `S` reproduce `(1)` exactly.

Thus class-group/genus-theory language is not merely analogous to the current quadratic blind code: the current odd-prime incidence matrix is a literal rectangular submatrix of the corresponding Rédei matrix.

The single row `p=2` used in some earlier shell formulations is outside this odd-prime dictionary and is governed by the supplementary law. Adding one row can increase the shell-block rank by at most one, so it cannot repair the asymptotic separation exhibited below.

## 2. Full Rédei rank controls the wrong kernel

Partition the full matrix according to `P\sqcup S`, obtaining `(9)`. A shell-supported vector is `(0,v)`. Equation `(10)` is immediate, so

\[
(0,v)\in\ker R
\quad\Longleftrightarrow\quad
v\in\ker A\cap\ker E.
\tag{16}
\]

This is the exact information mismatch.

The quadratic blind code in `MC-238` is `\ker A`: it asks whether the lower-prime rows generate all shell sign directions. The full Rédei kernel additionally imposes all shell-shell equations encoded by `E`. Those extra equations are perfectly capable of removing every shell-supported full-kernel vector while leaving `\ker A` large.

Accordingly, the classical formula relating `4`-rank to full Rédei corank cannot be inverted into a cross-block-rank statement without a new theorem controlling `E|_{\ker A}` or otherwise coupling the two blocks. Full class-group `4`-rank and shell generation are different invariants.

## 3. A path Laplacian gives maximal full rank and rank-one cross rank

Let

\[
n=k+m
\]

and let `L_n\in\mathbb F_2^{n\times n}` be the graph Laplacian of the path `(5)`: for `i\ne j`,

\[
(L_n)_{ij}=1
\quad\Longleftrightarrow\quad
|i-j|=1,
\tag{17}
\]

and the diagonal entry is the degree of the vertex modulo `2`. Every row sums to zero.

The reduced Laplacian obtained by deleting any one row and the corresponding column has determinant equal to the number of spanning trees of the path, namely `1`, by the matrix-tree theorem. Hence it is invertible over `\mathbb F_2`, proving `(6)`.

Cut the path between vertices `k` and `k+1`. The rectangular block between the first `k` and last `m` vertices contains only the edge `(k,k+1)`. Therefore it has one nonzero entry and rank exactly one, proving `(8)`.

This is already a pure linear-algebra counterexample to any implication

\[
\text{maximal full Rédei-type rank}
\Longrightarrow
\text{large cross-block rank}.
\tag{18}
\]

The next section shows that it is not merely an abstract matrix outside arithmetic: it can be realized by genuine prime Legendre symbols.

## 4. The path Rédei matrix is realized by genuine primes

We construct primes inductively. Suppose distinct primes

\[
q_1,\dots,q_{j-1}\equiv1\pmod4
\]

have already been chosen with the desired pairwise Legendre signs. For each `i<j`, prescribe

\[
\left(\frac{q_j}{q_i}\right)
=
\begin{cases}
-1,&j=i+1,\\
+1,&j>i+1.
\end{cases}
\tag{19}
\]

For every `q_i`, choose a nonzero residue class `a_i mod q_i` having the required quadratic character. By the Chinese remainder theorem, these conditions together with

\[
q_j\equiv1\pmod4
\tag{20}
\]

define a reduced residue class modulo

\[
4\prod_{i<j}q_i.
\tag{21}
\]

Dirichlet's theorem supplies infinitely many primes in that class, so choose one distinct from the previous primes and as large as desired. Since every selected prime is `1 mod 4`, quadratic reciprocity has no sign and therefore

\[
\left(\frac{q_i}{q_j}\right)
=
\left(\frac{q_j}{q_i}\right).
\tag{22}
\]

Induction realizes exactly the symmetric path adjacency pattern in the off-diagonal Legendre symbols. The standard Rédei diagonal is the row sum of the off-diagonal bits, so the resulting Rédei matrix is precisely `L_n`.

Because every `q_i\equiv1 mod4`, the product `D` in `(4)` is a positive fundamental discriminant. The classical Rédei formula then gives

\[
\operatorname{rk}_4\mathrm{Cl}^+(D)
=n-1-\operatorname{rank}_{\mathbb F_2}R_D
=0.
\tag{23}
\]

Thus the matrix separation `(6)`--`(8)` occurs inside genuine quadratic-field arithmetic, not only inside the category of arbitrary binary matrices.

The construction is deliberately nonlocal. CRT and Dirichlet may force later primes to be enormous relative to earlier ones. It gives no control placing a prescribed group of columns in one short interval `(y,2y]` while simultaneously fixing the complete lower-prime source set. That missing localization is exactly the frontier retained from `MC-252`.

## 5. Prior art and novelty audit

Rédei matrices and their relation to the `4`-rank of quadratic class groups are classical. Rédei's 1934 work introduced the matrix method; a modern reference is Peter Stevenhagen, *Rédei-matrices and applications*, in *Number Theory, Paris 1992--3*, London Mathematical Society Lecture Note Series 215 (1995), 245--260, DOI `10.1017/CBO9780511661990.015`.

Étienne Fouvry and Jürgen Klüners, *On the 4-rank of class groups of quadratic number fields*, Inventiones Mathematicae 167 (2007), 455--513, DOI `10.1007/s00222-006-0021-2`, use the Rédei matrix as the finite-field rank object governing `4`-rank distributions. Modern narrow-class-group work likewise treats the reduced Rédei matrix as the matrix whose corank gives `rk_4 Cl^+`; see Stephanie Chan, Peter Koymans, Djordjo Milovic and Carlo Pagano, *The 8-rank of the narrow class group and the negative Pell equation*, Forum of Mathematics, Sigma 10 (2022), e46, DOI `10.1017/fms.2022.40`.

There is also direct prior art on graph interpretations of Rédei matrices; for example Robert J. Kingan, *Tournaments and Ideal Class Groups*, Canadian Mathematical Bulletin 38 (1995), 330--333, DOI `10.4153/CMB-1995-048-1`, studies graph/matrix structures arising from Rédei's method.

Accordingly, no novelty is claimed for Rédei matrices, their class-group formula, graph interpretations, the matrix-tree theorem, CRT prescription of finitely many Legendre symbols, Dirichlet's theorem, or quadratic reciprocity. `MC-252` already proves a more general separated-prime universality statement for rectangular Legendre matrices.

The durable Mathia delta is the **frontier identification** obtained by applying this classical language to the exact post-`MC-253` question. The shell matrix is an exact Rédei cross-block, but full Rédei rank is an information-losing aggregation for that question. The path control proves this sharply even with genuine primes and zero narrow `4`-rank. Therefore a class-group route must use more than the scalar full-matrix rank/corank invariant.

## 6. Boundaries and updated frontier

- **No shell realization.** The prime construction does not place the second block in `(y,2y]` relative to a fixed lower-prime set. It is a separated-prime matched control, not an example of the actual Mathia shell.
- **No claim about the actual quadratic field.** The field with discriminant `(15)` attached to the actual lower/shell prime union may have interesting `4`-rank, but this finding neither computes nor estimates it.
- **Cross-block versus full kernel.** Equation `(16)` is the decisive distinction. A small full Rédei kernel does not bound `ker A` unless the shell-shell block is controlled on that kernel.
- **The row `p=2`.** Rédei's odd prime-discriminant block omits the supplementary-law row. One additional row changes rank by at most one and does not defeat the control family.
- **Higher Rédei symbols remain open.** The result concerns ordinary quadratic Rédei matrices and `4`-rank. Rédei triple symbols, `8`-rank/governing-field information, higher residue/Kummer structure, or another shell-localized invariant may contain information not present in full `4`-rank.
- **Bounded-order parity remains separately insufficient.** `MC-253` already rules out fixed-order shell parity balance as a route to high rank. This finding rules out a different shortcut: replacing cross-block rank by the full ordinary Rédei rank.
- **Localization remains load-bearing.** Both `MC-252` and the prime realization here become universal/flexible only because the prescribed primes may escape the tight shell. Any surviving algebraic route must exploit localization or a source coupling that the CRT construction cannot reproduce.

The live algebraic frontier is therefore narrower: if Rédei/Kummer ideas are pursued, the candidate invariant must see the **bipartite lower/shell interaction itself**, or higher-order data that provably constrains that interaction, rather than only the rank/corank of the completed quadratic Rédei matrix.