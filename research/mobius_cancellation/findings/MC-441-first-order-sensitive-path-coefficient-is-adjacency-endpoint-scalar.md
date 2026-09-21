# MC-441 — The first order-sensitive path-distance coefficient factors through one endpoint-adjacency scalar

**Evidence:** `LITERATURE+DERIVED · EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-440` showed that for a weighted path distance matrix the coefficients of `X^r` and `X^{r-1}` in `det(XD-I_r)` are blind to the order of the adjacent gaps, so the first possible order-sensitive layer is `X^{r-2}`. That layer can be computed exactly, and its order dependence is much narrower than an arbitrary function of the gap permutation.

Let

\[
x_0<x_1<\cdots <x_n,
\qquad
r=n+1\ge 4,
\qquad
g_i=x_i-x_{i-1}>0\quad(1\le i\le n),
\]

and let `D=D(g)` be the `r\times r` distance matrix `D_{ij}=|x_i-x_j|`. Define

\[
S=\sum_{i=1}^n g_i,
\qquad
P=\prod_{i=1}^n g_i,
\qquad
h_i=\frac1{g_i},
\]

and

\[
Q=\sum_{i=1}^n h_i,
\qquad
H_2=\sum_{i=1}^n h_i^2,
\qquad
R=\sum_{i=1}^{n-1}h_i h_{i+1}.
\]

Then the coefficient of `X^{r-2}` in `det(XD-I_r)` is

\[
\boxed{
[X^{r-2}]\det(XD-I_r)
=
(-1)^{r-3}2^{r-4}P
\left[
S\bigl(2Q^2-2H_2-R\bigr)-4Q+h_1+h_n
\right].
}
\tag{1}
\]

For permutations of a fixed gap multiset, `S`, `P`, `Q`, and `H_2` are symmetric. Hence **all order dependence of the first order-sensitive determinant layer factors through the single path-local scalar**

\[
\boxed{
J(g)=h_1+h_n-S\sum_{i=1}^{n-1}h_i h_{i+1}.
}
\tag{2}
\]

In particular, if `g'` is any permutation of the same gaps, then

\[
\boxed{
[X^{r-2}]\bigl(\det(XD(g)-I_r)-\det(XD(g')-I_r)\bigr)
=
(-1)^{r-3}2^{r-4}P\,[J(g)-J(g')].
}
\tag{3}
\]

Thus `MC-440`'s first surviving ordinal layer does not expose an unrestricted global ordering statistic. It sees only two endpoint reciprocals and one nearest-neighbor reciprocal-product energy. This is a locality/factorization obstruction, not an information-capacity theorem: a real scalar can still take many distinct values on different permutations.

No estimate for `M(x)` follows.

## 1. The coefficient is a sum of codimension-two principal minors

Write

\[
e_k(D)=\sum_{|T|=k}\det D[T].
\]

The principal-minor expansion from `MC-440` is

\[
\det(XD-I_r)=\sum_{k=0}^r(-1)^{r-k}X^k e_k(D).
\tag{4}
\]

Since `(-1)^{r-(r-2)}=1`, the coefficient under study is exactly

\[
[X^{r-2}]\det(XD-I_r)=e_{r-2}(D).
\tag{5}
\]

Every term in `e_{r-2}` is obtained by deleting two vertices from the original path and taking the determinant of the induced distance matrix on the remaining `r-2` points. Those remaining points again form a weighted path, so the weighted Graham–Pollak/Bapat–Kirkland–Neumann determinant formula applies to each term.

## 2. Product factors after deleting two vertices

Index the original vertices by `0,1,\ldots,n`. Introduce one deletion factor per vertex,

\[
u_0=h_1,
\qquad
u_j=h_j+h_{j+1}\quad(1\le j\le n-1),
\qquad
u_n=h_n.
\tag{6}
\]

Deleting one endpoint removes one gap; deleting one interior vertex merges its two adjacent gaps. Consequently, after deleting two **nonadjacent** vertices `a,b`, the product of the induced gaps is

\[
P\,u_a u_b.
\tag{7}
\]

For two adjacent deleted vertices `(i-1,i)`, the shared gap has been counted twice in `(7)`, and the exact product factor is instead

\[
P\,(u_{i-1}u_i-h_i^2).
\tag{8}
\]

Therefore the sum of all normalized induced-gap products is

\[
\sum_{0\le a<b\le n}\frac{P_{a,b}}P
=e_2(u_0,\ldots,u_n)-\sum_{i=1}^n h_i^2.
\tag{9}
\]

Now

\[
\sum_{j=0}^n u_j=2Q
\tag{10}
\]

and

\[
\sum_{j=0}^n u_j^2=2H_2+2R.
\tag{11}
\]

Hence

\[
\boxed{
\sum_{0\le a<b\le n}\frac{P_{a,b}}P
=2Q^2-2H_2-R.
}
\tag{12}
\]

The first genuinely order-sensitive quantity has already appeared: among the terms in `(12)`, only the adjacent reciprocal energy `R` depends on the permutation.

## 3. Endpoint deletions supply the remaining correction

The weighted path determinant is the product of induced gaps multiplied by the span between the first and last retained vertices, times the universal factor

\[
(-1)^{r-3}2^{r-4}.
\tag{13}
\]

If neither endpoint is deleted, the retained span is `S`. Starting from `S` for every deletion pair therefore overcounts exactly the span lost when the left or right endpoint is among the deleted vertices.

For deletion pairs containing the left endpoint, the total normalized lost-span contribution is

\[
2Q-h_1.
\tag{14}
\]

The right endpoint contributes similarly

\[
2Q-h_n.
\tag{15}
\]

Combining `(12)`–`(15)` gives

\[
\sum_{|T|=r-2}
\bigl(\operatorname{span}(T)\bigr)
\bigl(\operatorname{gap\ product}(T)\bigr)
=
P\left[
S(2Q^2-2H_2-R)-4Q+h_1+h_n
\right].
\tag{16}
\]

Multiplication by `(13)` proves `(1)`.

As a check, for four points with gaps `(a,b,c)`, `(1)` becomes

\[
e_2(D)=
-\bigl(3a^2+4ab+2ac+4b^2+4bc+3c^2\bigr),
\tag{17}
\]

which agrees with the explicit `X^2` coefficient in `MC-440`.

## 4. The ordinal response is strictly local under adjacent swaps

The factorization through `J` gives an exact local sensitivity law. Suppose an interior adjacent transposition exchanges `h_i=b` and `h_{i+1}=c`, with neighboring reciprocals

\[
a=h_{i-1},\qquad d=h_{i+2},
\qquad 2\le i\le n-2.
\]

Only three terms of `R` can change, and direct cancellation gives

\[
R_{\mathrm{after}}-R_{\mathrm{before}}
=(c-b)(a-d).
\tag{18}
\]

The endpoints are unchanged, so

\[
\boxed{
J_{\mathrm{after}}-J_{\mathrm{before}}
=-S(c-b)(a-d).
}
\tag{19}
\]

Thus an interior swap is invisible to this first ordinal layer whenever the two outer reciprocal gaps agree, regardless of the rest of the path. More generally, the response to a swap is controlled entirely by that four-gap neighborhood. Global order can influence the coefficient only through the sum of these nearest-neighbor products and the two endpoints.

This sharpens `MC-440`: order does reappear at degree `r-2`, but it initially reappears through a **one-dimensional nearest-neighbor aggregate**, not through an unrestricted global interaction among all gap positions.

## 5. Prior art and novelty boundary

The matrix-theoretic ingredients are established prior art.

- R. L. Graham and L. Lovász, *Distance matrix polynomials of trees*, Advances in Mathematics 29 (1978), 60–88, DOI `10.1016/0001-8708(78)90005-1`, studies coefficients of tree distance characteristic polynomials.
- R. B. Bapat, S. J. Kirkland and M. Neumann, *On distance matrices and Laplacians*, Linear Algebra and its Applications 401 (2005), 193–209, DOI `10.1016/j.laa.2004.05.011`, gives the weighted-tree determinant/inverse framework used already in `MC-440`.
- Harry Richman, Farbod Shokrieh and Chenxi Wu, *Principal minors of tree distance matrices*, arXiv:2411.11488v2 (10 December 2025), gives combinatorial formulas for arbitrary principal minors of tree distance matrices, including trees with positive edge lengths. Its weighted principal-minor theorem subsumes the individual minor evaluations used in deriving `(1)`.

Accordingly, **no novelty is claimed** for principal-minor expansions, weighted-tree distance determinants, or the existence of combinatorial formulas for these minors. Equation `(1)` is an elementary weighted-path specialization and aggregation of known machinery.

The durable contribution here is the Mathia frontier reduction: once `MC-440` identifies degree `r-2` as the first place a path-distance determinant can see gap order, that entire first ordinal layer factors through `(2)`. This turns an unspecified subleading signal into a precise endpoint-plus-nearest-neighbor observable and gives the swap law `(19)` that can be attacked directly in the arithmetic setting.

## Boundaries and falsification tests

- **This is a factorization statement, not a cardinality bound.** `J(g)` is one real scalar, but exact real values can distinguish many permutations. No claim is made that only polynomially many gap orders survive.
- **The coefficient is not permutation-blind.** Generic adjacent swaps change `(19)`. The result identifies the exact restricted form of order sensitivity rather than eliminating it.
- **Reflection remains invisible.** Reversing the gap order preserves both endpoint sum and `R`, hence preserves `J`, consistently with permutation similarity of the reflected distance matrix.
- **The result is specific to the first surviving determinant layer.** Lower coefficients may contain longer-range or genuinely higher-order ordering information.
- **Reciprocal notation uses positive gaps.** The formulas are applied only to positive path edge lengths; no singular zero-gap limit is being hidden.
- **No asymptotic prime-gap model is assumed.** The identities are exact for every finite positive gap vector and do not assert independence, stationarity, or a limiting law for prime gaps.
- **No zero-free information is imported.** The derivation is finite linear algebra plus weighted-tree distance formulas.

## Consequence for the research line

The distance-determinant branch now has a sharper hierarchy. `MC-439` rules out fixed-feature-rank determinants as carriers of unconstrained high-order Möbius interaction. `MC-440` shows that the natural growing-rank path metric restores gap-order sensitivity only two degrees below the leading scale. The present result identifies what that first recovered layer actually contains: endpoint reciprocals plus nearest-neighbor reciprocal adjacency energy.

The next useful question is therefore no longer merely whether subleading order survives. It is whether the arithmetic prime-divisor gap sequences from `MC-436` force nontrivial control, cancellation, or rigidity in

\[
J(g)=\frac1{g_1}+\frac1{g_n}
-\left(\sum_i g_i\right)
\left(\sum_i\frac1{g_i g_{i+1}}\right),
\]

or whether matched non-prime gap permutations reproduce the same behavior. A negative answer would close the first surviving path-distance layer and force the branch to descend to `X^{r-3}` or abandon this determinant observable.