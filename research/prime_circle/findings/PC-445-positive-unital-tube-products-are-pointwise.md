# PC-445 — Positive unital tube products are exactly pointwise multiplication

**Status:** EXACT-DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION + CONTROL-BLIND. Imposing the canonical cone of nonnegative real functions on the complete Prime-Circle preimage tubes removes **every** nontrivial unital bilinear product, including the externally cotangent-marked and refinement-compatible associative transports of PC-442–443 whenever those products admit an order-positive real realization. Associativity, translation equivariance, continuity, and any cotangent-mark condition are unnecessary for the rigidity. The abstract result is classical for $C(K)$ Banach lattice algebras; the Prime-Circle increment is the sharp order-theoretic boundary for these particular marked deformation moduli, not a new RH mechanism.

## 1. The exact order-preserving category

Fix $d>1$, $m\ge1$ and the complete PC-053 tube
\[
Y_m=\{y\in S^1:y^m\in P_d^*\},\qquad
A_m^{\mathbb R}=\mathbb R^{Y_m},\qquad
(A_m^{\mathbb R})_+=\{f:f(y)\ge0\text{ for all }y\}.
\tag{1}
\]
Let $\star:A_m^{\mathbb R}\times A_m^{\mathbb R}\to A_m^{\mathbb R}$ be **real-bilinear**, with the same two-sided unit $1$ as ordinary multiplication. Call it *positive* when
\[
f,g\ge0\quad\Longrightarrow\quad f\star g\ge0.
\tag{2}
\]
A complex-bilinear product on $\mathbb C^{Y_m}$ is covered only when it preserves the real-valued subspace and satisfies (2) there.

**Theorem (finite tube).** Under (1)–(2),
\[
\boxed{f\star g=fg\quad\text{pointwise for every }f,g.}
\tag{3}
\]
Neither associativity nor any geometric or arithmetic hypothesis is required. Thus a nontrivial PC-442 marked modulus cannot have an order-positive representative under the fixed function cone. The conclusion is about the *actual multiplication*, not just its equivalence class under a gauge group.

## 2. Direct finite proof without deformation assumptions

For $x\in Y_m$ let $e_x$ be the point indicator, and put $u_{xy}=e_x\star e_y\ge0$. Since $1=\sum_y e_y$ and $1$ is a right unit,
\[
e_x=e_x\star1=\sum_{y\in Y_m}u_{xy}.
\tag{4}
\]
For $z\ne x$ all terms $u_{xy}(z)$ in this sum are nonnegative and sum to zero. Hence $\operatorname{supp}(u_{xy})\subseteq\{x\}$. The **left** unit also gives
\[
e_y=1\star e_y=\sum_{x\in Y_m}u_{xy},
\tag{5}
\]
so $\operatorname{supp}(u_{xy})\subseteq\{y\}$. Consequently $u_{xy}=0$ for $x\ne y$, while (4) forces $u_{xx}=e_x$. The indicators form a real linear basis, proving (3) by bilinearity.

Both unit identities are load-bearing: a merely one-sided unit does not give both support restrictions. Similarly, requiring positivity only of a quadratic form or of a separately marked linear operator is **not** (2).

## 3. All refinement levels, and the stronger $C(X)$ boundary

Let $X=\varprojlim_mY_m$ be the profinite tower of PC-443. The locally constant cylinder algebra
\[
\mathcal A_{\rm cyl}^{\mathbb R}=\bigcup_m\mathbb R^{Y_m}
\tag{6}
\]
contains constants and is closed under pointwise absolute values. Any real-bilinear $\star$ on this algebra that has two-sided unit $1$ and maps pairs of nonnegative functions to nonnegative functions is automatically pointwise. This conclusion does **not** require $\star$ to preserve each separate finite level: it holds on the whole algebra by the following order argument.

More generally, on a real unital vector sublattice $V$ of bounded functions on a set $X$ (including $\mathcal A_{\rm cyl}^{\mathbb R}$ or $C(X,\mathbb R)$), let $\star:V\times V\to V$ be positive and bilinear with unit $1$. If $f,g\ge0$, then $0\le g\le\|g\|_\infty1$ gives
\[
0\le f\star g\le\|g\|_\infty f.
\tag{7}
\]
For any real $h$ with $h(x)=0$, the inequalities $-|h|\le h\le|h|$ and (7) imply
\[
-|h|\star g\le h\star g\le|h|\star g,\qquad
(|h|\star g)(x)=0
\tag{8}
\]
whenever $g\ge0$; thus $(h\star g)(x)=0$. Apply this with $h=f-f(x)1$ to obtain
\[
(f\star g)(x)=f(x)(1\star g)(x)=f(x)g(x)
\tag{9}
\]
for $g\ge0$, then write arbitrary real $g=g_+-g_-$ to conclude (3) pointwise on $V$. In particular no new order-positive bilinear product appears by passing to the all-level cylinder union or to $C(X)$, regardless of analytic continuity assumptions.

## 4. Explicit incompatibility with the nontrivial marked moduli

The nontrivial all-refinement transport in PC-443, equation (19), takes the form
\[
T_t=E+(I+tM_c)(I-E)=I+tM_c(I-E),
\qquad
f\star_tg=T_t^{-1}((T_tf)(T_tg)),
\tag{10}
\]
where $E$ averages each $m$-point fiber and $c$ is constant per base fiber but nonconstant across base vertices. Choose real $c_a=1$ on one base fiber and $0$ on another (possible when $\varphi(d)>1$). For distinct points $x,y$ of the first $m$-point fiber, $m>1$, the first-order term of (10) is
\[
(e_x\star_t e_y)(x)=-\frac{t}{m}+O(t^2)<0
\quad\text{for sufficiently small }t>0.
\tag{11}
\]
Indeed its infinitesimal transport is $L=M_c(I-E)$ and the product correction is the Hochschild coboundary
$fL(g)+L(f)g-L(fg)$. Equation (11) exhibits a negative output on two nonnegative point indicators. It is **not** an associativity failure: the transported product remains associative.

For a strictly formal $\mathbb C[[\varepsilon]]$ deformation, there is no default order on complex formal series; the theorem applies only to genuine order-positive **real specializations**, or to an order-compatible real algebra structure with the stated cone. It does not erase the formal algebraic moduli of PC-443; it proves that none of their nontrivial realizations can preserve the standard probabilistic/function-lattice cone together with the common two-sided unit.

## 5. Prior art, geometric controls, and RH boundary

**Prior art:** The uniqueness of a compatible positive multiplication on the Banach lattice $C(K)$ with its specified unit belongs to classical Banach lattice-algebra theory: Laura Martignon, *Banach f-algebras and Banach lattice algebras with unit*, *Boletim da Sociedade Brasileira de Matemática* **11** (1980), 11–18, DOI 10.1007/BF02584875. David Muñoz-Lahoz and Pedro Tradacete, *Banach lattice AM-algebras*, arXiv:2409.18500 (2024), DOI 10.1090/proc/17173, explicitly identify Martignon's uniqueness as the classical $C(K)$ case. The elementary proofs (4)–(9) establish precisely the hypotheses needed here and do not claim abstract novelty.

Apply the same cone, unit, and complete power-preimage construction to an arbitrary set of distinct non-root-of-unity base points. Equations (4)–(9) are unchanged, whether or not a cotangent operator, base-coordinate mark, or prime-birth labels are attached. Therefore the positivity obstruction is **entirely source-blind**.

**Consequence:** PC-442–443's surviving externally marked formal parameters cannot be interpreted as nontrivial positive unital products on the canonical real function cone, even when every refinement level is retained. Positivity of an unrelated operator or quadratic form is outside the theorem. Signed/complex, nonunital, nonbilinear, nonassociative-without-bilinearity, or altered-order interactions also lie outside this exact no-go. No zeta-zero condition, critical-line selector, or RH implication follows.

**Decisive audit:** On any $Y_m$ (for example $d=3,m=2$), verify (4) and (5) without assuming associativity, and check all four combinations $e_x\star e_y$ in an $m=2$ fiber. On the all-level algebra verify closure under absolute values and (7)–(9). For the marked example verify the negative coefficient in (11) directly, while checking that (10) remains associative. A positive, bilinear, two-sided-unital non-pointwise product on the stated function cone would falsify the theorem; a signed or differently ordered product would not.
