# PC-441 — Coordinate-marked preimage-tube products: rigidity versus artificial moduli

**Status:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-STRUCTURE + CONTROL-BLIND. On a finite complete Prime-Circle preimage tube, requiring an associative product to retain the *intrinsic left multiplication* by the embedded circle coordinate forces the original pointwise product exactly. Merely retaining the coordinate multiplication operator as an *external mark* has the opposite defect: the unital mark-preserving gauge group is trivial, so generic, completely nonarithmetic transport deformations become distinguishable by definition. The two meanings of “preserving the geometry” cannot be interchanged. This settles one finite marked-product ambiguity left by PC-440; it supplies no new zeta or RH implication.

## 1. The exact marked dichotomy

Let \(d>1\), \(m\ge1\), and take the complete PC-053 tube
\[
Y=Y_{d,m}=\{y\in S^1:y^m\in P_d^*\},
\qquad A=\mathbb C^Y,\qquad G=\mu_m.
\tag{1}
\]
Here \(G\) acts by fiber translation, \((fg)(y)=f(y)g(y)\) is the intrinsic algebra product, \(1\in A\) is its unit, and the *embedded circle coordinate*
\[
z\in A,\qquad z(y)=y,\qquad M_z f=zf
\tag{2}
\]
separates **every** vertex of \(Y\), not just the different base fibers.

Consider a unital associative \(\mathbb C[[\varepsilon]]\)-bilinear product \(\star\) on \(A[[\varepsilon]]\) whose zeroth-order term is pointwise multiplication. Neither commutativity nor \(G\)-equivariance is needed in part (a).

**(a) Intrinsic marking is rigid.** If the deformed left regular action of the same element \(z\) equals the original coordinate operator,
\[
\boxed{\quad z\star f=M_zf=zf\quad\text{for every }f\in A[[\varepsilon]],\quad}
\tag{3}
\]
then
\[
\boxed{\quad f\star g=fg\quad\text{for all }f,g\in A[[\varepsilon]].\quad}
\tag{4}
\]
In fact, this conclusion holds for *any* unital associative bilinear product satisfying (3), without a formal-deformation or equivariance hypothesis.

**(b) An external mark freezes gauges but not products.** Suppose \(M_z\) is retained as a separately specified linear operator, with no requirement (3). An equivalence between two such unital marked products must preserve the common unit and intertwine the fixed mark. But any \(\mathbb C[[\varepsilon]]\)-linear map \(S\) satisfying
\[
S1=1,\qquad SM_z=M_zS
\tag{5}
\]
is necessarily \(S=I\). Thus a marked-gauge class has no nontrivial gauge freedom at all. For \(m>1\), there nevertheless exist non-pointwise, unital, associative, \(G\)-equivariant formal products, all unmarked-gauge equivalent to the ordinary one, which remain distinct as externally \(M_z\)-marked products.

The distinction is **not prime-specific**: it holds on any finite set with an injective complex coordinate and, in (b), any matched free finite fiber-permutation action.

## 2. Exact proof of intrinsic-coordinate rigidity

Let \(z^k\) denote the ordinary pointwise power of \(z\), an element of \(A\). The unit gives \(1\star f=f\). Equation (3) gives \(z\star f=zf\), so in particular \(z\star z^k=z^{k+1}\). Associativity now yields inductively
\[
\begin{aligned}
z^{k+1}\star f
 &= (z\star z^k)\star f
  = z\star(z^k\star f)
  = z(z^kf)=z^{k+1}f
\end{aligned}
\tag{6}
\]
for all \(k\ge0\). By linearity, \(P(z)\star f=P(z)f\) for every polynomial \(P\in\mathbb C[X]\).

The values \(z(y)=y\) are pairwise distinct. Consequently the **finite Lagrange idempotents**
\[
e_y=\prod_{\substack{v\in Y\\v\ne y}}\frac{z-v}{y-v},
\qquad e_y(x)=\mathbf1_{\{x=y\}},
\tag{7}
\]
lie in \(\mathbb C[z]\) and span \(A\). Hence every \(f\in A\) is a polynomial in \(z\), and (6) forces \(f\star g=fg\). The same interpolation basis works coefficientwise for \(A[[\varepsilon]]\). No convergence, deformation cohomology or arithmetic input is required.

This also shows the precise general principle: on an algebra of complex functions over a finite set, fixing the left regular action of **one separating coordinate** fixes every associative unital product.

## 3. Why the external marked gauge group collapses

Write \(A=\bigoplus_{y\in Y}\mathbb Ce_y\). Each \(e_y\) is a one-dimensional eigenspace of \(M_z\) with eigenvalue \(y\); these eigenvalues are distinct. Therefore a linear map commuting with \(M_z\), including a formal series of linear maps, must satisfy \(Se_y=s_y(\varepsilon)e_y\). If it also fixes \(1=\sum_y e_y\), then
\[
\sum_y s_y(\varepsilon)e_y=S1=1=\sum_y e_y,
\quad\text{so}\quad s_y(\varepsilon)=1\text{ for all }y.
\tag{8}
\]
Thus \(S=I\), even before imposing \(G\)-equivariance or any tangent-to-identity restriction. Such an external mark can make two abstractly equivalent products look different merely because the equivalence relation admits no nontrivial maps.

For an explicit source-blind example when \(m>1\), let
\[
E=\frac1m\sum_{\gamma\in G}\gamma:A\to A,\qquad
L=E-I,\qquad T_\varepsilon=I+\varepsilon L
\tag{9}
\]
be the canonical fiber average, its zero-on-constants correction, and a formally invertible transport. Since \(E1=1\) and \(E\gamma=\gamma E\), we have \(T_\varepsilon1=1\) and \(T_\varepsilon\gamma=\gamma T_\varepsilon\). Define
\[
f\star_\varepsilon g
 =T_\varepsilon^{-1}\bigl((T_\varepsilon f)(T_\varepsilon g)\bigr).
\tag{10}
\]
This is unital, associative and fiber-equivariant, with
\[
f\star_\varepsilon g
=fg+\varepsilon\bigl(fL(g)+L(f)g-L(fg)\bigr)+O(\varepsilon^2).
\tag{11}
\]
For \(y\ne x\) lying in the same \(m\)-point fiber, substituting \(f=g=e_y\) gives at \(x\)
\[
\bigl[e_yL(e_y)+L(e_y)e_y-L(e_y^2)\bigr](x)
 =-\frac1m\ne0.
\tag{12}
\]
Therefore (10) is a genuinely different product on the fixed vector space, while PC-440 correctly identifies it as an unmarked coboundary transport. It **cannot** be removed by an externally \(M_z\)-preserving, unit-preserving equivalence because (8) leaves only \(S=I\). The same \(E\) and the same calculation apply to composite-fiber or nonarithmetic matched controls; no birth-prime selector has appeared.

## 4. Sharpness: coarse fiber coordinates leave deformations

The separating requirement in (3) matters. The power-map coordinate
\[
b=z^m,\qquad b(y)=y^m\in P_d^*
\tag{13}
\]
is constant on each full fiber of size \(m\), and is thus nonseparating when \(m>1\). The same nontrivial product (10) **does** keep its left regular action exactly fixed:
\[
E(bf)=bE(f),\quad Eb=b,\quad T_\varepsilon b=b,\quad
b\star_\varepsilon f
 =T_\varepsilon^{-1}(bT_\varepsilon f)=bf.
\tag{14}
\]
Thus fixing the intrinsic left action of the base-level coordinate \(z^m\) does not determine multiplication inside a complete lift fiber. Unlike the external \(M_z\)-marked situation, this coarse-coordinate deformation is also trivial under the allowable unit-preserving transport \(T_\varepsilon\), which commutes with \(M_b\). Nontriviality as a multiplication table and nontriviality **modulo the permitted marked gauges** are different claims.

## 5. Prior art, Prime-Circle consequence, and audit boundary

The proof of (a) is ordinary finite Lagrange interpolation; (b) is the simple-spectrum commutant theorem for a diagonal operator. The existence of trivial formal transports and the corresponding Hochschild coboundary is part of classical associative deformation theory (M. Gerstenhaber, *On the deformation of rings and algebras*, *Annals of Mathematics* **79** (1964), 59–103, DOI 10.2307/1970484; already anchored in this line's SOURCES.md). There is **no claim of novelty** for these general facts. The line-local contribution is the exact test of two differently marked versions of PC-440 against the embedded coordinate of the actual PC-053 tube.

This closes only a specific finite marked escape: exact coordinate left multiplication forces no new product; external coordinate marking manufactures distinctions on matched controls. It does **not** classify arbitrary separate marks, cotangent and chord operators jointly, nonlinear nonassociative tensors, geometrically forced symmetry-breaking projectors, or infinite-depth limits. A viable successor would have to specify the exact source-forced mark, the product/mark compatibility equations, the allowable isomorphisms, and a discriminator absent on the matched control; a claim of “marked deformation” alone is insufficient.

**Decisive audit:** Verify (6) by associativity and (7) for distinct circle vertices. Verify the formal transport (10), equivariance, unit, and nonzero first coefficient (12) for \(m>1\). Test (14) separately to avoid conflating \(z\) with \(z^m\). Any counterexample satisfying the exact intrinsic left-mark hypothesis (3) would falsify part (a); a difference arising only from the artificially frozen gauge group in (8) would not constitute an arithmetic mechanism.
