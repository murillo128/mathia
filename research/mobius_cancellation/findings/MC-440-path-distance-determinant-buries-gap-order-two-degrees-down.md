# MC-440 — Path-distance determinants escape fixed rank but bury gap order two degrees below the leading scale

**Evidence:** `LITERATURE+DERIVED · EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-MECHANISM · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-439` leaves growing-rank pair kernels as one genuine escape from its fixed-feature-rank collapse. The canonical one-dimensional distance kernel does escape fixed rank, but it has a second exact degeneracy: its two highest homogeneous scale layers forget the order of the adjacent gaps.

Let

\[
x_1<x_2<\cdots <x_r,
\qquad
g_i=x_{i+1}-x_i>0\quad(1\le i\le r-1),
\]

and let `D=D(g)` be the `r\times r` distance matrix

\[
D_{ij}=|x_i-x_j|.
\tag{1}
\]

For the principal-minor divisor statistic of `MC-439`, the full Boolean/Möbius interaction is

\[
I_D=\det(D-I_r).
\tag{2}
\]

More generally scale every adjacent gap by a common factor `X>0`. Writing

\[
S=\sum_{i=1}^{r-1}g_i,
\qquad
P=\prod_{i=1}^{r-1}g_i,
\qquad
Q=\sum_{i=1}^{r-1}\frac1{g_i},
\]

one has

\[
\boxed{
\det(XD-I_r)
=
(-1)^{r-1}2^{r-2}SP\,X^r
+
(-1)^{r-1}2^{r-2}P(SQ-1)\,X^{r-1}
+O_g(X^{r-2}).
}
\tag{3}
\]

Both displayed coefficients are symmetric functions of the **multiset** of adjacent gaps. Therefore, for every permutation `\pi` of the same gaps,

\[
\boxed{
\det(XD(g)-I_r)-\det(XD(g_\pi)-I_r)
=O_g(X^{r-2}).
}
\tag{4}
\]

Since the common leading coefficient in `(3)` is nonzero for positive gaps, the relative separation of two gap orders is at most `O_g(X^{-2})` on this fixed-shape large-scale family.

Thus the path-distance kernel clears the growing-rank gate from `MC-439` and can retain gap order at finite scale, but **the first two determinant scale layers are permutation-blind**. The first possible ordinal signal occurs two degrees below the natural determinant scale.

This is not a proof that distance kernels cannot be useful for Möbius cancellation. It is a quantitative conditioning obstruction: any analytic route that hopes to exploit gap order through this determinant must recover a subleading component rather than the dominant two homogeneous layers.

No estimate for `M(x)` follows.

## 1. Principal-minor expansion

Let

\[
e_k(D)=\sum_{|T|=k}\det D[T],
\qquad e_0(D)=1.
\]

The standard principal-minor expansion gives

\[
\det(XD-I_r)
=
\sum_{k=0}^r(-1)^{r-k}X^k e_k(D).
\tag{5}
\]

Equation `(5)` is the same finite-dimensional mechanism used in `MC-439`; the new question is what the top coefficients become for the growing-rank kernel `(1)`.

For a weighted tree on `r` vertices with edge lengths `g_i`, the classical weighted Graham-Pollak/Bapat-Kirkland-Neumann determinant formula gives

\[
\det D
=
(-1)^{r-1}2^{r-2}
\left(\sum_i g_i\right)
\left(\prod_i g_i\right)
=
(-1)^{r-1}2^{r-2}SP.
\tag{6}
\]

Hence the coefficient of `X^r` in `(5)` is already completely insensitive to gap order.

## 2. The next coefficient is also permutation-blind

The coefficient of `X^{r-1}` is `-e_{r-1}(D)`, so compute the sum of all principal minors obtained by deleting one point.

Deleting an endpoint leaves a path whose gaps are respectively

\[
(g_2,\ldots,g_{r-1})
\quad\text{or}\quad
(g_1,\ldots,g_{r-2}).
\]

Deleting an interior point between `g_i` and `g_{i+1}` merges those two edges into one edge of length `g_i+g_{i+1}`. Applying `(6)` to each resulting `(r-1)`-point path and summing gives

\[
\begin{aligned}
e_{r-1}(D)
&=(-1)^{r-2}2^{r-3}P\Bigg[
\frac{S-g_1}{g_1}
+\frac{S-g_{r-1}}{g_{r-1}}\\
&\qquad\qquad\qquad\quad
+S\sum_{i=1}^{r-2}
\left(\frac1{g_i}+\frac1{g_{i+1}}\right)
\Bigg]\\
&=
\boxed{
(-1)^{r-2}2^{r-2}P(SQ-1)
}.
\tag{7}
\end{aligned}
\]

The bracket simplification is exact: the endpoint terms and the merged-interior terms together count every reciprocal gap twice and contribute the constant `-2`.

Substituting `(6)` and `(7)` into `(5)` proves `(3)`. Because every `k\times k` principal minor of `D(g)` is homogeneous of degree `k` in the gaps, scaling `g\mapsto Xg` makes the remainder in `(3)` a polynomial of degree at most `r-2`. This proves `(4)`.

## 3. Finite-scale order really survives

The obstruction is not total order erasure. For four points with gaps `(a,b,c)`, direct expansion gives

\[
\begin{aligned}
\det(XD-I_4)
={}&-4abc(a+b+c)X^4\\
&-4(a+b)(a+c)(b+c)X^3\\
&-\bigl(3a^2+4ab+2ac+4b^2+4bc+3c^2\bigr)X^2
+1.
\end{aligned}
\tag{8}
\]

The `X^4` and `X^3` coefficients are symmetric in `{a,b,c}`, exactly as `(3)` predicts. The `X^2` coefficient is not: for example, exchanging the middle and final gap generally changes it. Reversing all gaps leaves the determinant unchanged, as it must, because reflection of the point chain only conjugates `D` by a permutation matrix.

So a path-distance determinant is a **real** growing-rank escape from the fixed-rank theorem of `MC-439`: it does not factor through a fixed-dimensional feature matrix, and it can distinguish non-reversal gap orders. What fails is dominance. The order-sensitive information begins only after two permutation-blind homogeneous layers have been removed.

## 4. Prior art and novelty boundary

The distance-matrix ingredients are classical or now covered by stronger literature results.

- R. B. Bapat, S. J. Kirkland and M. Neumann, *On distance matrices and Laplacians*, Linear Algebra and its Applications 401 (2005), 193–209, DOI `10.1016/j.laa.2004.05.011`, gives determinant and inverse formulas for weighted-tree distance matrices; its weighted determinant formula is `(6)`.
- R. L. Graham and L. Lovász, *Distance matrix polynomials of trees*, Advances in Mathematics 29 (1978), 60–88, DOI `10.1016/0001-8708(78)90005-1`, develops characteristic-polynomial coefficients of tree distance matrices.
- Harry Richman, Farbod Shokrieh and Chenxi Wu, *Principal minors of tree distance matrices*, arXiv:2411.11488, current version dated 22 March 2026, gives a combinatorial formula for arbitrary principal minors, including trees with edge lengths. Their Theorem B strictly subsumes the kind of weighted principal-minor evaluation used here.

Accordingly, **no novelty is claimed** for weighted-tree distance determinants, characteristic-polynomial/principal-minor identities, or formulas for tree-distance principal minors. Equation `(7)` is an elementary path specialization obtainable from that literature.

The durable Mathia contribution is the frontier consequence obtained after combining those classical formulas with the exact Möbius-interaction identity of `MC-439`: the most canonical growing-rank path metric does retain ordinal information, but its determinant interaction puts the entire gap permutation below two leading permutation-invariant scale layers. That identifies a concrete analytic cost which was not visible from rank alone.

## Boundaries and falsification tests

- **This is a common-scale statement.** The `O(X^{-2})` relative suppression compares fixed gap shapes under `g\mapsto Xg`. It is not an asymptotic theorem for actual consecutive prime gaps and does not assert that prime configurations occur as exact scaled copies.
- **Order is not annihilated.** Equation `(8)` explicitly falsifies the stronger claim that `det(D-I)` depends only on the gap multiset. The obstruction is leading-layer blindness, not complete blindness.
- **Reflection is an unavoidable quotient.** Reversed gap sequences give permutation-similar distance matrices. Any orientation-sensitive discriminator is therefore lost by every spectral/determinantal statistic of this unoriented distance matrix.
- **The two-degree loss is determinant-specific.** Other growing-rank kernels, other matrix functionals, or set-dependent kernels need separate analysis.
- **Subleading does not mean unusable.** An exact subtraction, normalization, resolvent, derivative, or other intrinsically justified operation could expose the `X^{r-2}` layer. Such a construction must show that the subtraction is stable and arithmetically available rather than chosen after seeing the desired order signal.
- **No source-capacity conclusion follows from amplitude alone.** `MC-436` shows factorially many realizable gap-rank permutations. Equation `(4)` concerns their determinant separation under a matched scaling family; it does not count how many distinct subleading values survive at finite resolution.
- **No zero-free input is used.** The derivation is finite linear algebra plus classical weighted-tree distance formulas.

## Consequence for the research line

`MC-439` showed that fixed-rank determinant kernels can fake high-order Möbius interaction while depending only on fixed additive feature moments. The path-distance matrix is the first natural test beyond that obstruction: its rank grows with the number of selected primes, and finite-scale gap order genuinely survives.

The new boundary is therefore more precise than “use growing rank.” For this canonical growing-rank kernel, the determinant's dominant and first subdominant scale terms still discard gap order. A viable distance-determinant route must explain how the arithmetic exposes the order-sensitive `r-2`-degree layer (or lower) with enough uniform control that the `X^{-2}` conditioning loss does not erase the signal downstream.