# PC-442 — Joint cotangent/base-coordinate marks leave universal fiber-sector moduli

**Status:** EXACT-DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION + CONTROL-BLIND. For finite complete Prime-Circle power-map tubes, formal associative products with the exact intrinsic base-coordinate left action are classified by fiber-Fourier transports. Requiring equivalences to preserve the original cotangent operator leaves precisely \((\varphi(d)-1)(m-1)\) independent formal relative sector parameters. The same moduli arise for a nonarithmetic matched operator. This is a classification of an explicitly marked finite category, not a new zeta or RH mechanism.

## 1. Exact category and classification

Fix \(d>1\), \(m\ge1\), \(r=\varphi(d)\), and the PC-053 complete preimage tube
\[
Y=Y_{d,m}=\{y\in S^1:y^m\in P_d^*\},\qquad A=\mathbb C^Y,\qquad G=\mu_m.
\tag{1}
\]
The cyclic group \(G\) acts freely by multiplication on each \(m\)-point fiber. Let \(b\in A\) be the intrinsic base coordinate \(b(y)=y^m\), and let \(M_b(f)=bf\). Let \(C=C_{d,m}\) be the original oriented cotangent operator restricted to \(Y\), as in PC-053.

Consider all \(\mathbb C[[\varepsilon]]\)-bilinear products \(\star\) on \(A[[\varepsilon]]\) that are associative, unital with **the same** \(1\), \(G\)-equivariant, reduce modulo \(\varepsilon\) to pointwise multiplication, and preserve the **intrinsic left** base action exactly:
\[
b\star f=bf=M_bf\qquad(f\in A[[\varepsilon]]).
\tag{2}
\]
Two such products are *jointly marked-equivalent* if there is a formal isomorphism \(S=I+O(\varepsilon)\) between them satisfying
\[
S1=1,\qquad SM_b=M_bS,\qquad S\gamma=\gamma S\ (\gamma\in G),\qquad SC=CS.
\tag{3}
\]
The cotangent \(C\) in (3) is a **fixed external linear mark**; no compatibility identity identifying \(C\) with a deformed multiplication is imposed.

**Theorem.** Choose any base vertex \(a_0\in U(d)=(\mathbb Z/d\mathbb Z)^\times\). The jointly marked-equivalence classes of products (2) correspond bijectively to
\[
\boxed{\quad
\prod_{\substack{a\in U(d)\setminus\{a_0\}\\1\le j<m}}
(1+\varepsilon\mathbb C[[\varepsilon]])
\ \cong\
(1+\varepsilon\mathbb C[[\varepsilon]])^{(r-1)(m-1)}.
\quad}
\tag{4}
\]
Each factor is a *free formal unit series*, not a convergence-controlled complex scalar. In particular, the tangent-space dimension is \((r-1)(m-1)\); the whole formal classification is exact, not merely first-order. It vanishes when \(m=1\) or \(d=2\).

## 2. Relative rigidity gives unique fiber-Fourier transports

Write \(b_a=\exp(2\pi ia/d)\) for \(a\in U(d)\), and let \(e_a\in A\) be the indicator of the fiber \(F_a=\{y:y^m=b_a\}\). Since all \(b_a\) are distinct, finite Lagrange interpolation gives \(e_a=p_a(b)\) for an ordinary polynomial \(p_a\). Equation (2), the common unit, and associativity imply inductively that the \(\star\)-powers of \(b\) agree with its ordinary powers, and hence
\[
e_a\star f=e_af,\qquad e_a\star e_a=e_a.
\tag{5}
\]

PC-440 supplies a \(G\)-equivariant, unit-preserving formal isomorphism \(T=I+O(\varepsilon)\) from \((A[[\varepsilon]],\star)\) to ordinary pointwise \((A[[\varepsilon]],\cdot)\):
\[
f\star g=T^{-1}\bigl((Tf)(Tg)\bigr),\qquad T1=1,\qquad T\gamma=\gamma T.
\tag{6}
\]
Because \(e_a\) is a \(\star\)-idempotent, \(T(e_a)\) is an ordinary idempotent congruent to \(e_a\) modulo \(\varepsilon\). Every idempotent of \(\mathbb C[[\varepsilon]]^Y\) has coordinate entries exactly \(0\) or \(1\), so \(T(e_a)=e_a\). Applying (6) to (5) yields
\[
T(e_af)=e_aT(f),\quad\text{hence }TM_b=M_bT.
\tag{7}
\]
In particular, the PC-440 gauge can always be chosen to preserve the *exact* base coordinate; no additional relative Hochschild obstruction is present.

Each \(G\)-regular fiber has one one-dimensional character subspace for every \(j\in\{0,\ldots,m-1\}\). Denote it \(V_{a,j}\). The joint \((M_b,G)\) eigenspaces are exactly these \(V_{a,j}\). Thus (7) and equivariance force
\[
T|_{V_{a,j}}=t_{a,j}(\varepsilon)\,I,\qquad
t_{a,j}\in1+\varepsilon\mathbb C[[\varepsilon]],\qquad
t_{a,0}=1.
\tag{8}
\]
The final identity follows from \(T1=1\): the constant fiber vectors \(e_a\) span the \(j=0\) sector. Conversely, **every** family (8) defines by (6) a product satisfying all of (2), since \(T\) fixes \(b\), commutes with \(M_b\), \(G\), and fixes \(1\).

There is no hidden redundancy in this parametrization of actual products. If two tangent-to-identity transports yield the same product, their ratio is a pointwise algebra automorphism of \(\mathbb C[[\varepsilon]]^Y\) congruent to \(I\). Such an automorphism fixes every primitive point idempotent and is therefore \(I\). Hence the \(r(m-1)\) series \(t_{a,j}\), \(j>0\), uniquely specify the product.

## 3. The cotangent mark removes only common Fourier-sector gauges

An allowed \(S\) in (3) is likewise diagonal on \(V_{a,j}\):
\[
S|_{V_{a,j}}=s_{a,j}I,\qquad s_{a,0}=1.
\tag{9}
\]
PC-053 gives the exact \(m\)-fiber Fourier blocks of \(C\), with \(D_j(a,a)=\exp(2\pi ija/(dm))\):
\[
K_0=mH_d,\qquad
K_j=mD_j(H_d+J_d)D_j^{-1}-2jI\quad(1\le j<m).
\tag{10}
\]
For **distinct** \(a,c\in U(d)\), the off-diagonal entry of each nonconstant block is
\[
(K_j)_{a,c}
=m\,\exp\!\left(\frac{2\pi ij(a-c)}{dm}\right)
\left(1+i\cot\frac{\pi(a-c)}d\right)\ne0.
\tag{11}
\]
The cotangent is real for these distinct residue representatives, so \(1+i\cot(\cdot)\) never vanishes. Thus \([S,C]=0\) gives
\[
(s_{a,j}-s_{c,j})(K_j)_{a,c}=0
\quad\Longrightarrow\quad
s_{a,j}=s_j\quad\text{for all }a,\ j>0.
\tag{12}
\]
Possible zero edges in the constant block \(K_0\) do not matter: the fixed unit has already forced \(s_{a,0}=1\).

Consequently the full joint mark-preserving gauge group tangent to identity is precisely \((1+\varepsilon\mathbb C[[\varepsilon]])^{m-1}\), acting on (8) by simultaneous rescaling \(t_{a,j}\mapsto t_{a,j}/s_j\) across every base fiber \(a\). Fixing \(a_0\), the exact invariants are
\[
\boxed{\quad u_{a,j}=\frac{t_{a,j}}{t_{a_0,j}},\qquad
a\ne a_0,\quad1\le j<m.\quad}
\tag{13}
\]
To check necessity and sufficiency, an equivalence \(S\) from \(\star_T\) to \(\star_{T'}\) makes \(T'ST^{-1}\) an ordinary pointwise algebra automorphism congruent to \(I\), hence identity. Therefore \(T'=TS^{-1}\), and (12) shows that two products are equivalent exactly when all ratios (13) match. This proves (4), including every formal order.

At first order, write \(t_{a,j}=1+\varepsilon\alpha_{a,j}+O(\varepsilon^2)\). The corresponding correction is the Hochschild coboundary
\[
B_1(f,g)=fL(g)+L(f)g-L(fg),\qquad L|_{V_{a,j}}=\alpha_{a,j}I,\quad \alpha_{a,0}=0.
\tag{14}
\]
The independent infinitesimal marked parameters are \(\alpha_{a,j}-\alpha_{a_0,j}\). These classes are **not** nonzero Hochschild classes: PC-440 makes every underlying algebra deformation gauge-trivial once the external cotangent mark is forgotten.

## 4. Matched control and sharp boundaries

Replace the primitive-root base by any \(r\) distinctly labeled points, each with a free cyclic \(m\)-point fiber; keep their separating base multiplication operator and cyclic action. In the same fiber-Fourier decomposition, choose a nonarithmetic fixed operator \(C^{\rm ctl}\) with \(K_j^{\rm ctl}=J_r-I_r\) for \(j>0\), and any constant block. Its nonconstant off-diagonal graph is complete, exactly as in (11). Every step (5)--(13) applies unchanged, giving **the same formal moduli and dimension**. The classification therefore detects connectivity of a marked finite Fourier block, not prime orders, cyclotomic coefficients, zeta zeros, or a new number-theoretic invariant.

The elementary small cases give the expected counts: \((d,m)=(3,2)\) and \((4,2)\) each have one relative formal unit, while \((5,3)\) has six. If the cotangent mark is forgotten, every product satisfying (2) is gauge-equivalent by a base-preserving, \(G\)-equivariant \(T\), leaving no marked moduli. If instead the **separating** fine coordinate \(z\) has its intrinsic left action fixed, PC-441 forces the original product itself. These three categories must not be conflated.

## 5. Prior art, consequences and falsification boundary

The load-bearing ingredients are the exact finite preimage-tube Fourier formula (PC-053), unital equivariant formal rigidity of the finite product algebra (PC-440), the separating-coordinate distinction (PC-441), and the classical idempotent/intertwiner and finite-diagonal commutant arguments. The general separable-algebra deformation background is classical (M. Gerstenhaber, *On the deformation of rings and algebras*, *Annals of Mathematics* **79** (1964), 59--103, DOI 10.2307/1970484), already documented in this line's SOURCES.md. There is no general-theorem historical-priority claim: the line-local increment is the exact jointly marked **Prime-Circle** quotient, its all-order parameter count, and the explicit matched-control no-go.

The result is limited to **complete finite tubes**, a fixed \(G\)-action, unital formal products reducing to pointwise multiplication, the **intrinsic** coarse base-coordinate left action, and the **external** fixed cotangent mark with tangent-to-identity equivalences. It neither classifies arbitrary chord/Hessian marks nor source-forced symmetry-breaking, cross-level compatibility, incomplete fibers, infinite-depth convergence or nonassociative operations. No RH-facing spectral or positivity consequence is obtained.

A direct falsification test is to check the idempotent lifting argument (5)--(7), the uniqueness of tangent-to-identity pointwise automorphisms, the off-diagonal nonvanishing (11) for every \(j>0\), the exact marked-equivalence identity \(T'=TS^{-1}\), and the nonprime complete-graph control. In particular, a count based only on first-order coboundaries would not establish the exact formal classification (4): uniqueness of the transports and the full mark centralizer are both essential.
