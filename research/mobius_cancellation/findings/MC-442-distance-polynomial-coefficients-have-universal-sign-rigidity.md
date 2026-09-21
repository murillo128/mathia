# MC-442 — Positive weighted paths have universal distance-polynomial coefficient signs

**Evidence:** `LITERATURE+DERIVED · EXACT-DERIVED · DECISIVE-NEGATIVE · FRONTIER-ADVANCE · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

Continue with the positive-gap path-distance matrix from `MC-440` and `MC-441`:

\[
x_0<x_1<\cdots <x_n,
\qquad
r=n+1\ge 4,
\qquad
g_i=x_i-x_{i-1}>0,
\qquad
D_{ij}=|x_i-x_j|.
\]

Write

\[
F_D(X)=\det(XD-I_r)=\sum_{k=0}^r c_k X^k.
\]

Then

\[
c_1=0,
\qquad
(-1)^{r-1}c_k>0
\quad\text{for every }2\le k\le r.
\tag{1}
\]

Thus every nonconstant nonzero coefficient of `det(XD-I_r)` has the **same sign**, determined only by the matrix size. This sign pattern is independent of the positive gap values, their order, and whether the points came from rational primes or from a matched non-arithmetic positive-gap control.

There is a second sign rigidity inside the first order-sensitive layer isolated in `MC-441`. With

\[
h_i=1/g_i,
\qquad
S=\sum_{i=1}^n g_i=\sum_{i=1}^n\frac1{h_i},
\qquad
R=\sum_{i=1}^{n-1}h_i h_{i+1},
\]

and

\[
J(g)=h_1+h_n-SR,
\]

one has the exact positive-defect decomposition

\[
J(g)
=
-2\sum_{i=2}^{n-1}h_i
-
\sum_{i=1}^{n-1}
\sum_{\substack{1\le j\le n\\ j\notin\{i,i+1\}}}
\frac{h_i h_{i+1}}{h_j}
<0.
\tag{2}
\]

So the normalized scalar carrying all order dependence at degree `X^{r-2}` is itself strictly negative throughout the entire positive-gap domain. Permutations can change its magnitude, and `MC-441` gives the exact adjacent-swap difference, but they cannot make `J` change sign.

## Derivation

For every `k`, the coefficient of `X^k` is the signed sum of `k\times k` principal minors:

\[
c_k=(-1)^{r-k}e_k(D),
\qquad
e_k(D)=\sum_{\substack{T\subseteq\{0,\dots,n\}\\|T|=k}}\det D[T].
\tag{3}
\]

Take any subset `T` with `|T|=k\ge2` and sort its selected points as

\[
y_1<\cdots<y_k.
\]

Its principal distance matrix `D[T]` is exactly the distance matrix of a weighted path whose induced gaps

\[
\delta_j=y_{j+1}-y_j
\]

are strictly positive. The weighted-tree determinant formula therefore gives

\[
\det D[T]
=
(-1)^{k-1}2^{k-2}
\left(\sum_{j=1}^{k-1}\delta_j\right)
\prod_{j=1}^{k-1}\delta_j.
\tag{4}
\]

Every summand in `e_k(D)` is nonzero and has sign `(-1)^{k-1}`. Hence

\[
(-1)^{k-1}e_k(D)>0.
\]

Combining this with (3) yields

\[
\operatorname{sgn}(c_k)
=(-1)^{r-k}(-1)^{k-1}
=(-1)^{r-1},
\]

which proves (1). Also `c_1=(-1)^{r-1}\operatorname{tr}D=0` because the distance matrix has zero diagonal.

For (2), expand each adjacency term using `S=\sum_j1/h_j`:

\[
S h_i h_{i+1}
=
h_i+h_{i+1}
+
\sum_{\substack{1\le j\le n\\j\notin\{i,i+1\}}}
\frac{h_i h_{i+1}}{h_j}.
\]

Summing over `i=1,\dots,n-1` gives

\[
SR
=
h_1+h_n
+2\sum_{i=2}^{n-1}h_i
+
\sum_{i=1}^{n-1}
\sum_{\substack{1\le j\le n\\j\notin\{i,i+1\}}}
\frac{h_i h_{i+1}}{h_j}.
\]

Subtracting from `h_1+h_n` gives (2). Since `n\ge3` in the `MC-441` regime and every `h_i` is positive, the inequality is strict.

## Consequence for the current route

`MC-440` left open the possibility that descending below the first order-sensitive coefficient might expose a useful signed observable. Equation (1) closes that possibility for **coefficient signs throughout the entire determinant polynomial**: descending from `X^{r-2}` to `X^{r-3}` or any lower nonconstant degree cannot create sign oscillation, because every coefficient has the same universal sign for every positive weighted path.

Equation (2) closes the still narrower possibility that the sign of the `MC-441` order-sensitive scalar could distinguish the actual prime-divisor gap order from a matched positive-gap permutation. It cannot: `J(g)<0` is source-generic.

This does **not** show that coefficient magnitudes are order-blind. In particular, `MC-441` already proves that `J(g)` changes under suitable adjacent swaps. Any surviving path-distance route must therefore use a quantitative magnitude, centered contrast, normalized fluctuation, or a different observable; raw coefficient sign and raw `J` sign contain no arithmetic discriminator.

## Prior art and novelty audit

The sign phenomenon is classical at the tree-distance-polynomial level. Graham and Lovász, *Distance Matrix Polynomials of Trees*, Advances in Mathematics 29 (1978), 60–88, record the fixed sign pattern of distance-polynomial coefficients for unweighted trees. Bapat, Kirkland and Neumann, *On distance matrices and Laplacians*, Linear Algebra and its Applications 401 (2005), 193–209, give the weighted-tree determinant and inertia formulas; their Corollary 2.5 specializes directly to (4). Richman, Shokrieh and Wu, *Principal minors of tree distance matrices*, arXiv:2411.11488, give modern principal-minor formulas including trees with edge lengths.

No novelty is claimed for the tree distance-matrix determinant, inertia, coefficient-sign phenomenon, or principal-minor machinery. The Mathia contribution here is the exact specialization to the current positive-gap path wrapper, the explicit defect identity (2) for the `MC-441` scalar, and the resulting obstruction: the candidate determinant-coefficient branch has no sign-cancellation layer at any degree.

## Boundaries and audit conditions

The positivity of the path gaps is essential. Signed, complex, or otherwise non-metric edge weights are outside this construction and need not satisfy the sign conclusion.

The result is a sign obstruction, not a magnitude obstruction. It does not prove that prime-derived coefficient magnitudes are reproduced by matched controls, and it does not exclude a useful centered or normalized statistic built from those magnitudes.

It also supplies no estimate for `M(x)` and no new statement about zeros of `zeta`. Its role is to prevent a source-generic sign pattern in a determinant wrapper from being mistaken for Möbius cancellation or an arithmetic parity mechanism.
