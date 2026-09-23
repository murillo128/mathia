# PC-408 — shell-2 fixed-degree descendant products have a universal zeta hypercube

**Status:** `EXACT-DERIVED` + `CLASSICAL-REFORMULATION` + `DECISIVE-NEGATIVE` for the fixed-degree ordinary pointwise-product completion left open by PC-407. Once the shell-2 descendant law is conjugated to the universal dilation representation of PC-406/PC-407, every fixed-degree product of descendants with the same conductor index has an exact conductor Dirichlet series whose first-order Euler data factor into a finite inclusion-exclusion product of shifted zeta functions. The remaining Euler product is already absolutely convergent for `Re(s)>1/2`, while dependence on the parent shell is only a finite product over primes dividing the parent. A matched arbitrary-profile control reproduces the same factorization exactly. Therefore the shifted-zeta divisor is a property of the universal descendant semigroup and pointwise multiplication, not a retained prime-circle geometric signal.

This does **not** rule out nonlinearities that couple different descendant indices before summation, source-dependent product laws, angular/chord/old-new information, degree or interaction depth growing with the conductor, or genuinely renormalized infinite-degree constructions. It closes the natural fixed-degree family obtained by multiplying finitely many copies of the same descendant and then taking the conductor Dirichlet transform.

## 1. Descendant Mellin multipliers

Use the unitary shell-2 representation from PC-406/PC-407. For a parent `n`, the conductor descendant operator `C_{n,m}` has Mellin multiplier

\[
c_{n,m}(t)
=
m^{it}
\prod_{\substack{p\mid m\\p\nmid n}}
(1-p^{-it}).
\tag{1}
\]

Equivalently, at a prime power `p^k`, `k>=1`,

\[
c_{n,p^k}(t)=
\begin{cases}
p^{ikt},&p\mid n,\\
p^{ikt}(1-p^{-it}),&p\nmid n.
\end{cases}
\tag{2}
\]

Fix an integer `r>=1` and real Mellin frequencies `t_1,...,t_r`. Put

\[
T=t_1+\cdots+t_r
\tag{3}
\]

and, initially for `Re(s)>1`, define the fixed-degree conductor symbol

\[
D_{n,r}(s;\mathbf t)
:=
\sum_{m\ge1}
\frac{1}{m^s}
\prod_{j=1}^r c_{n,m}(t_j).
\tag{4}
\]

This series is absolutely convergent there: the coefficient magnitude is bounded by `2^{r omega(m)}`. Thus its Euler product and the following rearrangements are native identities in `Re(s)>1`.

## 2. Exact local Euler factors

For a prime `p`, write

\[
A_j=p^{it_j},\qquad
A=\prod_{j=1}^r A_j=p^{iT},\qquad
y=p^{-s}.
\tag{5}
\]

If `p|n`, every positive exponent is repeated rather than fresh, so

\[
L_p^{\rm rep}(s;\mathbf t)
=
\sum_{k\ge0}(Ay)^k
=
\frac1{1-Ay}.
\tag{6}
\]

If `p\nmid n`, every positive exponent carries one fresh-prime factor for each frequency. Therefore

\[
\begin{aligned}
L_p^{\rm fresh}(s;\mathbf t)
&=1+
\prod_{j=1}^r(1-A_j^{-1})
\sum_{k\ge1}(Ay)^k\\
&=\frac{1+b_p(\mathbf t)y}{1-Ay},
\end{aligned}
\tag{7}
\]

where

\[
\boxed{
b_p(\mathbf t)
=\prod_{j=1}^r(A_j-1)-A.}
\tag{8}
\]

In particular, the coefficient of `y` in the fresh local factor is

\[
\prod_{j=1}^r(A_j-1).
\tag{9}
\]

The ratio between a repeated-prime and a fresh-prime local factor is especially simple:

\[
\boxed{
\frac{L_p^{\rm rep}}{L_p^{\rm fresh}}
=
(1+b_p(\mathbf t)p^{-s})^{-1}.}
\tag{10}
\]

Thus all parent-shell dependence is already confined to finitely many primes `p|n`.

## 3. Inclusion-exclusion forces a finite shifted-zeta hypercube

For each subset `S subseteq {1,...,r}`, define

\[
t_S:=\sum_{j\in S}t_j,
\qquad
t_\varnothing=0,
\qquad
\epsilon_S:=(-1)^{r-|S|}.
\tag{11}
\]

Consider the finite inclusion-exclusion product

\[
\boxed{
Z_r(s;\mathbf t)
:=
\prod_{S\subseteq\{1,\ldots,r\}}
\zeta(s-it_S)^{\epsilon_S}.}
\tag{12}
\]

At a prime `p`, its coefficient at first order in `y=p^{-s}` is

\[
\sum_S\epsilon_S p^{it_S}
=
\prod_{j=1}^r(p^{it_j}-1),
\tag{13}
\]

which is exactly (9). Hence, if `Z_{r,p}` denotes the local factor of (12),

\[
H_{r,p}(s;\mathbf t)
:=
\frac{L_p^{\rm fresh}(s;\mathbf t)}{Z_{r,p}(s;\mathbf t)}
=
1+O_r(p^{-2\operatorname{Re}s}).
\tag{14}
\]

Therefore

\[
H_r(s;\mathbf t):=\prod_p H_{r,p}(s;\mathbf t)
\tag{15}
\]

converges normally and absolutely for `Re(s)>1/2` on compact subsets of that half-plane. Combining (7), (10), and (12)--(15) yields the exact factorization

\[
\boxed{
D_{n,r}(s;\mathbf t)
=
Z_r(s;\mathbf t)
H_r(s;\mathbf t)
\prod_{p\mid n}
(1+b_p(\mathbf t)p^{-s})^{-1},
\qquad \Re(s)>1.}
\tag{16}
\]

Equation (16) is the native Dirichlet-series identity. Extending its right-hand side outside `Re(s)>1` is a meromorphic continuation of this explicit factorization; zeros or poles of shifted zeta factors there are not, by themselves, native spectral data of the absolutely convergent descendant sum.

The first two degrees recover the previous results exactly. For `r=1`,

\[
Z_1(s;t)=\frac{\zeta(s-it)}{\zeta(s)},
\qquad H_1=1,
\tag{17}
\]

which is the linear multiplier of PC-406. For `r=2`,

\[
Z_2(s;t_1,t_2)
=
\frac{\zeta(s)\zeta(s-i(t_1+t_2))}
{\zeta(s-it_1)\zeta(s-it_2)}.
\tag{18}
\]

On the quadratic-energy diagonal `t_2=-t_1=t`, this becomes

\[
Z_2(s;t,-t)
=
\frac{\zeta(s)^2}
{\zeta(s-it)\zeta(s+it)},
\tag{19}
\]

which is precisely the universal shifted-zeta divisor isolated in PC-407; its generalized-Jordan Euler correction is the corresponding `H_2`.

At degree three the same mechanism already gives the full cube boundary:

\[
Z_3(s;\mathbf t)
=
\frac{
\zeta(s-i(t_1+t_2+t_3))
\zeta(s-it_1)\zeta(s-it_2)\zeta(s-it_3)
}{
\zeta(s)
\zeta(s-i(t_1+t_2))
\zeta(s-i(t_1+t_3))
\zeta(s-i(t_2+t_3))
}.
\tag{20}
\]

Higher fixed degrees add no qualitatively new arithmetic operation: the zeta factors are the Boolean-lattice inclusion-exclusion over partial frequency sums.

## 4. Ordinary pointwise descendant products reduce to the same symbol

Let `h_1,...,h_r` be Mellin-tame profiles on `R_+`, and propagate each profile by the same source-independent descendant operators `C_{n,m}`. Form

\[
P_{n,r}(s;x)
:=
\sum_{m\ge1}\frac1{m^s}
\prod_{j=1}^r(C_{n,m}h_j)(x).
\tag{21}
\]

Under the standard absolute-convergence/Fubini hypotheses, Mellin convolution gives the frequency-`T` component as

\[
\widehat P_{n,r}(s;T)
=
\frac1{(2\pi)^{r-1}}
\int_{t_1+\cdots+t_r=T}
D_{n,r}(s;\mathbf t)
\prod_{j=1}^r\widehat h_j(t_j)
\,dt_1\cdots dt_{r-1}.
\tag{22}
\]

For the actual shell-2 prime-circle profile, the required Mellin control was already established in PC-406/PC-407. Equation (22) shows that ordinary pointwise multiplication does not create a hidden shell-specific conductor interaction: its entire conductor dependence passes through the universal scalar symbol (16).

## 5. Matched arbitrary-profile control

The decisive control is to forget cyclotomic geometry entirely. Start with arbitrary Mellin-tame profiles `h_j` and apply exactly the same dilation/fresh-prime descendant operators. Equations (1)--(22) remain unchanged. In particular, the same shifted-zeta hypercube `Z_r`, the same universal Euler correction `H_r`, and the same finite parent-prime factor occur without roots of unity, cyclotomic polynomials, chord geometry, or the common anchor.

Therefore the zeta factors in (16) cannot be credited as a new prime-circle bridge. They arise from three classical operations only: multiplicative Euler factorization of the conductor sum, the finite-difference factor `(1-p^{-it_j})` at each fresh prime, and finite inclusion-exclusion across a fixed number of multiplied copies.

## Novelty / prior-art audit

The ingredients are classical. Euler products for multiplicative Dirichlet series provide the local-to-global factorization; Mellin transforms diagonalize the dilation semigroup; products in physical space become Mellin convolutions; and (13) is finite Boolean-lattice inclusion-exclusion. The `r=2` specialization is already the generalized-Jordan structure isolated in PC-407. A targeted literature/duplicate audit found no reason to treat the all-`r` packaging as a new external theorem, and no such claim is made here.

The project-local contribution is instead the exact closure result: **every fixed-degree ordinary same-descendant product has the same universal semigroup provenance**, with all zeta-sensitive factors already present in a matched nonarithmetic control. Thus increasing polynomial degree does not repair the source-identifiability failure diagnosed by PC-406/PC-407.

## Consequence for the research line

This closes the entire route

`fixed-degree pointwise nonlinearity -> same conductor descendant -> Dirichlet sum -> shifted-zeta divisor -> prime-circle-specific RH mechanism`.

The surviving nonlinear frontier must escape at least one hypothesis used above. Natural possibilities are joint couplings of distinct descendant indices before summation, source-dependent nonlinear laws, interactions with angular/chord/old-new data not carried by the shell-2 dilation profile, or complexity whose degree/depth grows with conductor so that finite inclusion-exclusion no longer exhausts the construction. Those remain open; merely increasing a fixed polynomial degree does not.
