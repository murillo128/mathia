# PC-440 — Equivariant formal products on complete prime-circle preimage tubes are rigid

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + CONTROL-BLIND. On every finite complete power-map preimage tube, *all* fiber-translation-equivariant, unital, associative **formal deformations of the intrinsic pointwise product** are removed by a fiber-equivariant, unit-preserving formal change of coordinates. An explicit separability contraction supplies the gauge to each order. The algebraic rigidity is classical; the Prime-Circle increment is a precise no-go for an entire class of geometry-motivated sector products beyond the individual gauges of PC-087 and PC-088. This neither excludes nonassociative couplings nor produces an RH implication.

## 1. Exact scope and result

For integers \(d>1\), \(m\ge1\), use the intrinsic PC-053 complete preimage tube
\[
Y=Y_{d,m}=\pi_m^{-1}(P_d^*)
 =\{\zeta_{dm}^{\,a+dt}:a\in(\mathbb Z/d\mathbb Z)^\times,\ t\in\mathbb Z/m\mathbb Z\}.
\tag{1}
\]
It is a *finite set*, with \(|Y|=m\varphi(d)\). Let
\[
A=\mathbb C^Y,\qquad (fg)(y)=f(y)g(y),\qquad
G=\mu_m\cong\mathbb Z/m\mathbb Z .
\tag{2}
\]
The group \(G\) acts by multiplication of the underlying circle point, equivalently by translation of \(t\) inside each complete fiber, and hence by algebra automorphisms of \(A\). The primitive exact-order labels need not be separately preserved by these translations.

Consider any \(\mathbb C[[\varepsilon]]\)-bilinear product
\[
f\star g=fg+\sum_{n\ge1}\varepsilon^n B_n(f,g),
\qquad B_n:A\times A\to A\ \text{complex bilinear},
\tag{3}
\]
which is associative as a formal series, has the *same unit* \(1\), and obeys
\[
\gamma(f\star g)=(\gamma f)\star(\gamma g)
\quad\text{for every }\gamma\in G.
\tag{4}
\]
The coefficients \(B_n\) may depend on the actual chord, cotangent, or old/new data; they are not presumed diagonal, local, symmetric, or independent of the shell geometry.

**Theorem.** There is a formal linear automorphism
\[
T=I+\sum_{n\ge1}\varepsilon^n L_n
 :A[[\varepsilon]]\longrightarrow A[[\varepsilon]],
\quad T(1)=1,\quad T\gamma=\gamma T,
\tag{5}
\]
such that
\[
\boxed{\quad f\star g=T^{-1}\bigl((Tf)(Tg)\bigr).\quad}
\tag{6}
\]
In particular, every such first-order associativity-preserving \(G\)-equivariant bilinear correction represents the zero class in equivariant Hochschild \(HH^2\), and this can be resolved recursively to all formal orders. Since \(T\) commutes with fiber translations, it preserves every fiber-character isotypic sector. No separate projective, prime-ordering, or associative-deformation invariant survives in the **unmarked equivariant product algebra**.

The theorem applies in particular to \(m=pq\) for distinct refinement primes coprime to \(d\), and equally to a matched composite-fiber control with the same finite permutation action. It does **not** assert that arbitrary two products are conjugate by an automorphism required also to preserve a separately marked cotangent operator, birth-shell projector, or anchored-vertex observable.

## 2. An explicit equivariant Hochschild contraction

For \(y\in Y\), let \(e_y\in A\) be the point indicator. These are mutually orthogonal central idempotents:
\[
e_y e_z=\delta_{yz}e_y,\quad
\sum_{y\in Y}e_y=1,\quad e_y f=f(y)e_y.
\tag{7}
\]
The diagonal element
\[
\mathfrak e=\sum_{y\in Y}e_y\otimes e_y\in A\otimes_\mathbb C A
\tag{8}
\]
is a separability idempotent: multiplication sends it to \(1\), it intertwines left and right multiplication by each \(f\in A\), and \((\gamma\otimes\gamma)\mathfrak e=\mathfrak e\) because \(G\) merely permutes the points of \(Y\).

Let \(B:A^2\to A\) be any \(G\)-equivariant Hochschild 2-cocycle. With the standard differential,
\[
(\delta B)(c,f,g)
=cB(f,g)-B(cf,g)+B(c,fg)-B(c,f)g=0.
\tag{9}
\]
Define a **specific** linear cochain
\[
\boxed{\quad L(f)=\sum_{y\in Y}e_y B(e_y,f).\quad}
\tag{10}
\]
Using (9) with \(c=e_y\), multiplying by \(e_y\), then summing over \(y\), gives
\[
\begin{aligned}
(\delta L)(f,g)
 &=fL(g)-L(fg)+L(f)g\\
 &=\sum_y \Bigl[
    f e_yB(e_y,g)+e_y B(f,g)-e_y B(e_y f,g)\Bigr]\\
 &=\sum_y e_y B(f,g)=B(f,g),
\end{aligned}
\tag{11}
\]
where the third equality uses \(e_y f=f(y)e_y\). Thus **every** 2-cocycle is a 2-coboundary, without guessing an operator whose Leibniz defect might happen to equal \(B\). Equivariance is exact:
\[
\gamma L(f)
 =\sum_y e_{\gamma y} B(e_{\gamma y},\gamma f)=L(\gamma f).
\tag{12}
\]
If \(B\) preserves the fixed unit, \(B(f,1)=B(1,f)=0\), and (10) gives \(L(1)=0\).

The same separability idempotent provides the standard contracting homotopy on positive-degree Hochschild cochains, with
\[
(sf)(a_1,\ldots,a_{n-1})
 =\sum_y e_y f(e_y,a_1,\ldots,a_{n-1}),\qquad
\delta s+s\delta=I\quad(n\ge1).
\tag{13}
\]
It commutes with the \(G\)-action. Hence the positive-degree \(G\)-equivariant Hochschild cohomology of \(A\) vanishes; (10)--(12) already give the only degree required for deformation rigidity.

## 3. Removal to every formal order

Suppose an equivariant, unital, associative deformation has already been conjugated so its first possible new term is at order \(r\ge1\):
\[
f\star g=fg+\varepsilon^r C_r(f,g)+O(\varepsilon^{r+1}).
\tag{14}
\]
The coefficient of \(\varepsilon^r\) in associativity is precisely \(\delta C_r=0\); equivariance and the fixed-unit condition also hold for \(C_r\). Take \(L_r\) from (10), so \(\delta L_r=C_r\), and let \(T_r=I+\varepsilon^rL_r\). The transported product
\[
f\star' g
 =T_r\Bigl((T_r^{-1}f)\star(T_r^{-1}g)\Bigr)
\tag{15}
\]
has no order-\(r\) correction, because that coefficient is \(C_r-\delta L_r=0\). The map \(T_r\) commutes with \(G\) and fixes \(1\). Iterating over all \(r\) yields an \(\varepsilon\)-adically convergent formal change of coordinates and proves (5)--(6). This is a *formal*, not an analytic-convergence, assertion.

A two-prime divisor square supplies no exception: the Chinese-remainder description \(G\simeq C_p\times C_q\) is only a relabeling of the same finite action \(C_{pq}\), and every coefficient of the formal product is subject to the same contraction. All finite matched fibers have the same rigidity. The argument neither uses primality nor reads any zero of a zeta or \(L\)-function.

## 4. Mathematical delta, controls and prior art

PC-087 shows that the specific carry factor obtained by transporting **pointwise multiplication** to PC-053 common-base Fourier gauges is an explicit coboundary, while PC-088 proves that the **specific cotangent Leibniz-defect bilinear map** is a Hochschild coboundary, even though its raw associator need not vanish. Those are tests of two canonical constructions. Here the quantifier is stronger: *every* equivariant associative formal correction of the pointwise product, however its coefficients are derived from the chord/cotangent geometry, has an explicitly equivariant primitive and is formally removable. Consequently a candidate cannot use the cohomology class of a finite equivariant deformation as its proposed prime/nonprime discriminator.

**Prior art:** Separability of finite products of fields, vanishing of their positive-degree Hochschild cohomology, and formal rigidity when \(HH^2=0\) are classical. M. Gerstenhaber, *On the deformation of rings and algebras*, Ann. of Math. **79** (1964), 59--103, DOI 10.2307/1970484, is already anchored in this line's SOURCES.md for PC-088. The equivariant deformation framework is also standard: G. Mukherjee and R. B. Yadav, *Equivariant one-parameter deformations of associative algebras*, J. Algebra Appl. **19** (2020), article 2050114, DOI 10.1142/S0219498820501145. No novelty is claimed for the abstract rigidity theorem; the source-local contribution is the complete-preimage-tube specialization, explicit sector-preserving contraction, and sharp exclusion it imposes on the accepted nonlinear-fiber clue.

**What survives:** This result does not rule out a bilinear operation that is not an associative deformation of the pointwise product; a genuinely nonassociative product or independently supplied categorical associator; a singular/infinite-depth limit where compatible gauges fail to exist; an interaction explicitly breaking full fiber-translation symmetry through source-forced exact-order marking; or a **marked** deformation where allowed changes of coordinates must also preserve an independent geometrically specified operator, projection, anchor or cross-level inclusion. In such a marked problem, the cochain (10) need not commute with the additional structure. An unmarked gauge-trivial deformation may retain geometry in the pair (product, mark), so gauge triviality alone is not evidence that every geometry-derived observable is control-blind.

**Decisive audit:** For a proposed finite-sector perturbation compute its order-\(r\) associativity cocycle, construct (10), and check \(B_r-\delta L_r=0\) in vertex coordinates. Check \(\gamma L_r=L_r\gamma\) under every fiber shift, \(L_r(1)=0\), and the cancellation \(C_r-\delta L_r\) in (15). A counterexample under the exact hypotheses (finite full tube, fixed unit, associative formal product, and full fiber equivariance) would falsify the theorem. A nontrivial invariant requiring a separately marked geometric operator instead lies outside the stated gauge category and must pass its own matched-control test.