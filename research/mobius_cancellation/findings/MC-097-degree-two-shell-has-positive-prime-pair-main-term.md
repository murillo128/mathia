# MC-097 — Degree-two radial shell has a positive prime-pair main term

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Use the product-fiber coefficients `W_N(a)` of `MC-092` and the radial shell sums of `MC-095`,

\[
C_{k,N}:=\sum_{\substack{a\ \mathrm{squarefree}\\\omega(a)=k}}W_N(a).
\]

The first genuinely collisional shell is not merely capable of carrying a large coherent subrectangle as shown in `MC-096`: the **complete degree-two shell itself has a positive almost-full-square-scale main term**. As `N -> infinity` through the positive integers,

\[
\boxed{
C_{2,N}
\sim
c_2\frac{N^2}{(\log N)^2},
\qquad
c_2
=\frac{15}{\pi^2}\left(\gamma+\gamma_1-\frac12\right)
\approx 0.0066869236684459>0,
}
\tag{1}
\]

where `gamma` is Euler's constant and `gamma_1` is the first Stieltjes constant in the convention

\[
\zeta(s)=\frac1{s-1}+\sum_{n\ge0}\frac{(-1)^n}{n!}\gamma_n(s-1)^n.
\]

Thus the live radialized route cannot hope to prove a critical-power bound for each `omega(a)` shell separately. In particular, let

\[
H_r(N):=
\left(\sum_{k=0}^{K_N}r^{2k}|C_{k,N}|^2\right)^{1/2},
\qquad
R_r(N):=
\left(\sum_{\substack{0\le k\le K_N\\C_{k,N}\ \mathrm{occurs}}}r^{-2k}\right)^{1/2},
\tag{2}
\]

for any `0<r<=1`, in the fixed-radius discrete-Fourier/Cauchy reconstruction of `MC-095`. Since the degree-two shell occurs for all sufficiently large `N`,

\[
H_r(N)\ge r^2|C_{2,N}|,
\qquad
R_r(N)\ge r^{-2},
\]

and therefore

\[
\boxed{
H_r(N)R_r(N)
\ge |C_{2,N}|
\sim c_2\frac{N^2}{(\log N)^2}
}
\tag{3}
\]

**for every choice of radius `r`, including `N`-dependent radii**. Shrinking the noise radius can move cost from the shell norm to endpoint reconstruction but cannot remove this degree-two floor.

This is stronger than the generic information-loss warning in `MC-095` for the actual source vector. The source itself certifies that taking an `ell_2` norm across radial shells before endpoint recovery loses the cross-degree cancellation needed for any Mertens-scale gain. A surviving one-parameter deformation argument must therefore estimate a signed coupling that allows cancellation **between different degrees before an absolute value or shell norm is taken**, or leave the radial-shell quotient altogether.

No lower bound for the hard Möbius endpoint `mathcal Q_N(1)=sum_k(-1)^k C_{k,N}` is claimed. Other degrees may cancel the positive degree-two main term.

## 1. Exact degree-two decomposition

For `a=pq` with distinct primes `p<q`, the product-fiber formula of `MC-092` is

\[
W_N(pq)
=
\sum_{\substack{b\ \mathrm{squarefree}\\(b,pq)=1\\pqb^2\le N^2}}
R_N(pq,b)
 z\!\left(\frac{N^2}{pqb^2}\right),
\tag{4}
\]

where

\[
R_N(pq,b)
=
\#\left\{d\mid pq:\frac{pqb}{N}\le d\le\frac Nb\right\}
\tag{5}
\]

and

\[
z(x)=\lfloor x\rfloor+\frac12-x.
\]

Put `x=N/b`. The divisors of `pq` are `1,p,q,pq`. The middle pair `p,q` is admissible exactly when `q<=x`; the outer pair `1,pq` is admissible exactly when `pq<=x`. Hence

\[
\boxed{
R_N(pq,b)
=2\mathbf 1_{q\le x}
+2\mathbf 1_{pq\le x}.
}
\tag{6}
\]

(The condition `pqb^2<=N^2` is then automatic whenever the first indicator is nonzero.) Consequently

\[
\boxed{
W_N(pq)
=2\!\sum_{\substack{b\le N/q\\b\ \mathrm{squarefree}\\(b,pq)=1}}
 z\!\left(\frac{N^2}{pqb^2}\right)
+2\!\sum_{\substack{b\le N/(pq)\\b\ \mathrm{squarefree}\\(b,pq)=1}}
 z\!\left(\frac{N^2}{pqb^2}\right).
}
\tag{7}
\]

Summing over `p<q` and exchanging the finite sums gives the exact decomposition

\[
\boxed{
C_{2,N}
=2\sum_{b\ \mathrm{squarefree}} A_b(N/b)
+2\sum_{b\ \mathrm{squarefree}} B_b(N/b),
}
\tag{8}
\]

with

\[
A_b(x)
:=
\sum_{\substack{p<q\le x\\p,q\nmid b}}
 z\!\left(\frac{x^2}{pq}\right),
\tag{9}
\]

and

\[
B_b(x)
:=
\sum_{\substack{p<q\\pq\le x\\p,q\nmid b}}
 z\!\left(\frac{x^2}{pq}\right).
\tag{10}
\]

The first term is a full prime-pair box at scale `x`; the second is the much thinner semiprime-product region.

## 2. The full prime-pair box has an explicit PNT main term

First ignore the finitely many primes dividing `b` and define

\[
A(x):=\sum_{p<q\le x} z\!\left(\frac{x^2}{pq}\right).
\tag{11}
\]

Let

\[
\nu_x:=\frac{\log x}{x}\sum_{p\le x}\delta_{p/x}.
\tag{12}
\]

The prime number theorem implies weak convergence of `nu_x` to Lebesgue measure on `[0,1]`: for every fixed `0<u<v<=1`,

\[
\nu_x([u,v])
=\frac{\log x}{x}\bigl(\pi(vx)-\pi(ux)\bigr)
\longrightarrow v-u.
\tag{13}
\]

The bounded function

\[
f(u,v):=z\!\left(\frac1{uv}\right)
\tag{14}
\]

is continuous except on the axes and on the countable family of hyperbolas `uv=1/m`, all of which have two-dimensional Lebesgue measure zero. Therefore the product measures satisfy

\[
\left(\frac{\log x}{x}\right)^2
\sum_{p,q\le x}
 z\!\left(\frac{x^2}{pq}\right)
\longrightarrow
J,
\tag{15}
\]

where

\[
J:=\int_0^1\!\int_0^1
 z\!\left(\frac1{uv}\right)\,du\,dv.
\tag{16}
\]

The diagonal `p=q` contributes only `O(pi(x))`, so

\[
\boxed{
A(x)
=\frac J2\frac{x^2}{(\log x)^2}(1+o(1)).
}
\tag{17}
\]

This use of the PNT is deliberately low-tech: no zero-density input, prime-pair conjecture, or cancellation theorem is involved.

## 3. The prime-pair constant is a Stieltjes-constant combination

Set `u=e^{-r}`, `v=e^{-s}`. Since a function of `r+s` integrates against `e^{-r-s}dr ds` with convolution density `t e^{-t}dt`, `(16)` becomes

\[
J
=\int_0^\infty t e^{-t}z(e^t)\,dt
=\int_1^\infty z(y)\frac{\log y}{y^2}\,dy.
\tag{18}
\]

For `Re(s)>0`, define

\[
Z(s):=\int_1^\infty z(y)y^{-s-1}\,dy.
\tag{19}
\]

For `Re(s)>1`, the elementary identity

\[
\zeta(s)
=s\int_1^\infty \lfloor y\rfloor y^{-s-1}\,dy
\]

and `floor(y)=y-1/2+z(y)` away from the measure-zero integers give

\[
\boxed{
Z(s)
=
\frac{\zeta(s)-1/(s-1)-1/2}{s}.
}
\tag{20}
\]

The integral in `(19)` is analytic across `s=1`, so use the standard Laurent expansion

\[
\zeta(1+h)=\frac1h+\gamma-\gamma_1 h+O(h^2).
\tag{21}
\]

Differentiating `(20)` at `s=1` yields

\[
Z'(1)=-\gamma_1-\gamma+\frac12.
\]

On the other hand, differentiation under the absolutely convergent integral gives

\[
-Z'(1)
=\int_1^\infty z(y)\frac{\log y}{y^2}\,dy
=J.
\]

Hence

\[
\boxed{
J=\gamma+\gamma_1-\frac12
\approx0.00439981941785616>0.
}
\tag{22}
\]

The Laurent convention and definition of the Stieltjes constants are standard; the same DLMF section already retained as `MC-S18` records them in equations 25.2.4--25.2.5.

## 4. Square-free base summation preserves the main term

Return to `A_b(x)`. Removing the pairs for which `p|b` or `q|b` changes `(11)` by at most

\[
O\!\bigl(\omega(b)\pi(x)\bigr),
\tag{23}
\]

because `|z|<=1/2`. Choose

\[
L_N:=(\log N)^4.
\tag{24}
\]

For `b<=L_N`, one has `x=N/b >= N/(log N)^4`, so `(17)` and `(23)` give uniformly

\[
A_b(N/b)
=
\frac J2
\frac{(N/b)^2}{\log^2(N/b)}(1+o(1)).
\tag{25}
\]

Since `log(N/b)=log N+O(log log N)` uniformly in this range,

\[
2\sum_{\substack{b\le L_N\\b\ \mathrm{squarefree}}}
A_b(N/b)
=
J\frac{N^2}{\log^2N}
\left(
\sum_{\substack{b\le L_N\\b\ \mathrm{squarefree}}}\frac1{b^2}
+o(1)
\right).
\tag{26}
\]

The classical Euler product gives

\[
\sum_{b\ \mathrm{squarefree}}\frac1{b^2}
=\frac{\zeta(2)}{\zeta(4)}
=\frac{15}{\pi^2}.
\tag{27}
\]

For the remaining bases use only `|z|<=1/2` and `pi(x)<=x`:

\[
\sum_{b>L_N}|A_b(N/b)|
\ll
N^2\sum_{b>L_N}\frac1{b^2}
\ll \frac{N^2}{(\log N)^4}
=o\!\left(\frac{N^2}{\log^2N}\right).
\tag{28}
\]

Thus the first sum in `(8)` contributes

\[
\boxed{
2\sum_{b\ \mathrm{squarefree}}A_b(N/b)
\sim
\frac{15J}{\pi^2}\frac{N^2}{\log^2N}.
}
\tag{29}
\]

## 5. The product-bounded semiprime term is lower order

The second term in `(8)` needs no delicate semiprime asymptotic. Trivially,

\[
|B_b(x)|
\le
\frac12\#\{p<q:pq\le x\}.
\tag{30}
\]

Counting `q` by integers and using the reciprocal-prime estimate retained as `MC-S6`,

\[
\#\{p<q:pq\le x\}
\le
\sum_{p\le x}\frac{x}{p}
\ll x\log\log(3x).
\tag{31}
\]

Therefore

\[
\sum_{b\ \mathrm{squarefree}}|B_b(N/b)|
\ll
N\sum_{b\le N}\frac{\log\log(3N/b)}{b}
\ll N\log N\log\log N
=o\!\left(\frac{N^2}{\log^2N}\right).
\tag{32}
\]

Combining `(8)`, `(22)`, `(27)`, `(29)`, and `(32)` proves `(1)`.

## 6. Consequence for the radial-shell frontier

`MC-096` showed that a concrete degree-two prime rectangle has positive mass `asymp N^2/log^2N`, while leaving open the possibility that the rest of the degree-two shell might cancel it down to the critical `N^{1+o(1)}` power. Equation `(1)` closes that possibility: the **full shell retains a positive main term of the same polynomial scale**.

This kills one of the explicit surviving branches of `MC-095`--`MC-096`: a theorem bounding the individual degree-shell sums strongly enough that their weighted `ell_2` norm is critical. The obstruction is source-specific rather than merely dimensional, and `(3)` shows that changing the noise radius cannot rescue the `ell_2`-then-Cauchy reconstruction.

The result does **not** kill the one-parameter deformation itself. Since

\[
\mathcal Q_N(1)=\sum_k(-1)^kC_{k,N},
\]

an improved Mertens mechanism could still arise from structured cancellation between different `k` values, from a signed recurrence coupling several degrees before absolute values, or from a non-radial source statistic retaining relational/phase information that the shell quotient discards. What is ruled out is treating the radial shells as separately small or combining them only after a positive norm.

## 7. Prior art and novelty boundary

The Huxley--Watt finite sawtooth framework is classical (`MC-S24`), and `MC-092`/`MC-095` supply the source-specific product-fiber and radial-shell identities used here. The prime-number-theorem scaling argument in `(12)`--`(17)`, the Euler product `(27)`, and the zeta Laurent/Stieltjes expansion in `(20)`--`(22)` are classical mechanisms; `MC-S15`, `MC-S6`, and the DLMF material already represented by `MC-S18` are sufficient anchors for those ingredients.

A targeted literature search around reciprocal prime-pair sawtooth sums, semiprime fractional-part sums, and Titchmarsh divisor problems for almost primes found adjacent semiprime-counting and shifted-divisor literature but no basis for claiming an external new theorem under the exact formulation `(1)`. **No novelty claim is made.** The durable line-specific content is the exact composition of the `MC-092` source quotient with the PNT limit, which turns the qualitative degree-two obstruction of `MC-096` into an explicit full-shell asymptotic and decisively removes shellwise `ell_2` cancellation as a route to the Mertens scale.