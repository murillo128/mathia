# MC-255 — The higher 2-class rank tower can vanish while the Legendre cross-block has arbitrarily large nullity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-ARITHMETIC-CONTROL`, `FRONTIER-REFINEMENT`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the genuine-prime Rédei path control of `MC-254`. For arbitrary integers

\[
k\ge 1,\qquad m\ge2,\qquad n=k+m,
\]

that finding constructs distinct primes

\[
q_1,\dots,q_n\equiv1\pmod4
\]

such that the positive fundamental discriminant

\[
D=\prod_{i=1}^n q_i
\]

has binary Rédei matrix `R_4(D)` equal to the mod-2 Laplacian of the path

\[
1-2-\cdots-n.
\]

Cut the path after vertex `k`, and write

\[
R_4=
\begin{pmatrix}
C&A\\
A^{\mathsf T}&E
\end{pmatrix},
\]

where `A` is the `k\times m` lower-prime/shell-prime Legendre cross-block. `MC-254` proves

\[
\operatorname{rank}_{\mathbb F_2}R_4=n-1,
\qquad
\operatorname{rank}_{\mathbb F_2}A=1.
\tag{1}
\]

Hence

\[
\boxed{\dim_{\mathbb F_2}\ker A=m-1,}
\tag{2}
\]

while the narrow class group `\mathcal C=\operatorname{Cl}^+(\mathbb Q(\sqrt D))` has

\[
\boxed{r_4(\mathcal C)=0.}
\tag{3}
\]

The classical higher-rank filtration then collapses completely:

\[
\boxed{r_{2^j}(\mathcal C)=0\qquad(j\ge2).}
\tag{4}
\]

Equivalently, the `2`-primary part of `\mathcal C` has exponent at most `2`; it may have the large genus-theory `2`-rank `r_2=n-1`, but it has no cyclic factor of order `4` or higher.

More sharply, the ordinary Rédei `8`-rank mechanism does not merely fail numerically to control `(2)`: **the nonzero cross-block blind vectors do not enter its domain**. Since every row of `R_4` sums to zero and `(1)` gives maximal possible rank,

\[
\ker R_4=\langle\mathbf 1_n\rangle.
\tag{5}
\]

For any nonzero `v\in\ker A`, the shell-supported vector `(0,v)` is not a multiple of `\mathbf1_n`, so

\[
(0,v)\notin\ker R_4.
\tag{6}
\]

Using the block equation,

\[
R_4\binom0v=inom{Av}{Ev}=inom0{Ev},
\]

we therefore obtain the exact exclusion

\[
\boxed{v\in\ker A\setminus\{0\}\Longrightarrow Ev\ne0.}
\tag{7}
\]

Peter Stevenhagen's standard `8`-rank construction restricts the ambiguous-class map to `\ker R_4` and defines

\[
R_8:\ker R_4\longrightarrow 2\mathcal C/4\mathcal C\cong\mathbb F_2^{r_4},
\qquad
r_8=r_4-\operatorname{rank}_{\mathbb F_2}R_8.
\tag{8}
\]

In the path family, `r_4=0`, so the target in `(8)` is zero-dimensional and `r_8=0`; after removing the single redundant discriminant relation there is no nontrivial `R_8` matrix at all. The same group-theoretic monotonicity then gives `(4)` for every higher `2`-power rank.

Thus for arbitrarily large `m` there are genuine prime-discriminant quadratic fields in which **all full-class-group rank layers above genus theory vanish while the selected Legendre cross-block has nullity `m-1`**.

This closes a specific shortcut left open after `MC-254`: scalar `8`-rank, higher `2^j`-ranks, or any argument that reaches the bipartite generation problem only through the completed quadratic field's higher `2`-class ranks cannot force high rank of `A`. The blind cross-block can already be huge in a family where that entire higher rank tower is identically zero.

This does **not** rule out a new higher Rédei/Kummer invariant built directly on the localized bipartite interaction, a theorem controlling `E` on `\ker A`, or raw higher residue data that does not factor through the full class-group filtration. It also does not realize the path control with the active moving-shell condition `r\in(y,2y]` and gives no estimate for `M(X)`.

## 1. Vanishing `4`-rank kills every higher class-group rank layer

Stevenhagen defines, for the narrow class group `\mathcal C`,

\[
r_{2^j}
=
\dim_{\mathbb F_2}
\mathcal C[2^j]/\mathcal C[2^{j-1}]
=
\dim_{\mathbb F_2}
2^{j-1}\mathcal C/2^j\mathcal C.
\tag{9}
\]

The sequence

\[
r_2,r_4,r_8,\dots
\]

is nonincreasing. This is also immediate from the invariant-factor decomposition of the finite abelian `2`-primary group: `r_{2^j}` counts cyclic factors whose order is at least `2^j`.

For a discriminant with `n` prime-discriminant factors, the ordinary Rédei formula gives

\[
r_4=n-1-\operatorname{rank}R_4.
\tag{10}
\]

The path matrix in `MC-254` has rank `n-1`, so `(10)` gives `(3)`. Nonnegativity and monotonicity then force

\[
0\le r_{2^j}\le r_4=0
\qquad(j\ge2),
\]

which proves `(4)`.

Equivalently, if the `2`-primary part contained any cyclic factor `\mathbb Z/2^e\mathbb Z` with `e\ge2`, then `r_4` would be positive. Therefore the path control has a potentially large elementary-abelian `2`-part but no higher `2`-power structure.

This distinction matters here. A large `r_2` records many genus characters of the **completed** discriminant. It does not say that the rectangular lower/shell block `A` has large rank. Equations `(1)` and `(2)` show the opposite can happen maximally.

## 2. The blind cross-block kernel is filtered out before `R_8`

The stronger information is not just that `r_8=0`. It is the domain mismatch in `(6)`--`(8)`.

For the path Laplacian, row sums vanish, so `\mathbf1_n\in\ker R_4`. Maximal rank `n-1` makes this the entire kernel, proving `(5)`.

Now let `v\in\ker A` be nonzero. The vector `(0,v)` has zero coordinates on the first `k\ge1` vertices, so it cannot equal the nonzero all-ones vector. Therefore it is not in `\ker R_4`. Since `Av=0`, block multiplication shows that the only possible obstruction is the shell-shell block:

\[
R_4(0,v)=(0,Ev).
\]

It follows that `Ev\ne0` for every such `v`, which is `(7)`.

Stevenhagen's construction makes this exact information boundary explicit. His equation defining `R_8` first **restricts to `\ker R_4`** and only then applies the `8`-rank map. The shell-supported blind space `\ker A` is therefore not an input space for the classical higher-rank construction; only the much smaller intersection already isolated in `MC-254`,

\[
\ker A\cap\ker E,
\]

can enter via shell-supported vectors. In the path family that intersection is zero even though `\dim\ker A=m-1`.

When `r_4=0`, the target `2\mathcal C/4\mathcal C` of `R_8` is itself zero. Thus the standard `8`-rank matrix is not a hidden reservoir of cross-block information that happens to have the wrong scalar summary: in this matched control the class-group filtration has already discarded the blind directions before the trilinear Rédei-symbol stage is reached.

## 3. Prior art and novelty boundary

The group-theoretic facts and the Rédei `4`-/`8`-rank machinery are classical. The primary source used here is:

- Peter Stevenhagen, *Rédei reciprocity, governing fields and negative Pell*, Mathematical Proceedings of the Cambridge Philosophical Society **172** (2022), 627--654, DOI `10.1017/S0305004121000335`. Section 2 defines the nonincreasing ranks `r_2,r_4,r_8,...`; equation (22) restricts the `8`-rank map to `\ker R_4`; Theorem 4.1 states `r_8=r_4-rank(R_8)`.

Stevenhagen also emphasizes that the entries of `R_8` are Rédei symbols attached to decompositions of the second kind and ambiguous classes that survive the preceding `R_4` constraint. This is exactly the filtration boundary used in `(6)`--`(8)`.

`MC-254` supplies the other input: a genuine-prime path Rédei matrix with maximal full rank and rank-one chosen cross-block. No novelty is claimed for the definition of higher `2`-power ranks, their monotonicity, the Rédei rank formulas, the `R_8` construction, or the CRT/Dirichlet prime realization already established there.

The durable Mathia delta is the frontier consequence of combining those facts: **the same arithmetic control that destroys any implication from full `4`-rank to cross-block rank simultaneously destroys every scalar higher `2`-class rank and excludes every nonzero blind cross-block vector from the classical `R_8` input domain**. Therefore simply moving from `4`-rank to `8`-rank or higher class-group ranks cannot repair the information mismatch identified in `MC-254`.

A targeted prior-art check found the standard higher-rank theory organized exactly through this nested class-group filtration; no theorem was found that reverses it into a bound for an arbitrary selected Rédei cross-block. No novelty claim depends on that search result.

## 4. Falsification checks and boundaries

- **Full field versus cross-block.** The conclusion concerns invariants of the completed quadratic field. It does not say that all trilinear or higher residue symbols one could define on selected lower/shell primes are zero or useless.
- **`r_4=0` is decisive.** The implication to `(4)` uses the standard nonincreasing rank filtration, not a heuristic about generic class groups.
- **`R_8` domain.** The classical `R_8` map is defined after restriction to `\ker R_4`; it is not a map on all of `\ker A`. Claiming otherwise would erase the obstruction.
- **Raw Rédei symbols remain distinct.** A Rédei symbol may exist as an arithmetic object outside a proposed scalar-rank argument. A successful route would have to show that a shell-localized collection of such symbols constrains `A` directly rather than merely computing `r_8` of the completed field.
- **No shell realization.** As in `MC-254`, the primes realizing the path pattern are produced nonlocally by CRT and Dirichlet. Nothing here places the second block inside `(y,2y]` relative to the first.
- **No Möbius amplitude.** The result concerns the generation/blind-character side of `MC-246`; it gives no cancellation estimate for the exact rough Möbius coset.
- **No zero-set consequence.** No statement about `M(X)`, `1/\zeta`, a zero-free region, RH, or GRH is derived.

## Updated frontier

The post-`MC-254` phrase “try higher Rédei/class-group rank” is now too coarse. **Higher full-class-group ranks are eliminated as a shortcut.** The surviving algebraic possibilities must preserve information that the path control destroys: a direct localized bipartite higher symbol, a theorem forcing `E` to be small or structured on `\ker A`, a shell-localized Kummer/Chebotarev constraint that does not factor through the completed rank tower, or another invariant that distinguishes the actual `(y,2y]` matrix from the nonlocalized prime controls.

The alternative frontier remains unchanged: bypass generation and prove signed cancellation for the exact rough Möbius coset isolated in `MC-246`.