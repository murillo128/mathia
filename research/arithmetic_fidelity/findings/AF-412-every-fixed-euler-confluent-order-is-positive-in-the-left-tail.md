# AF-412 — Every fixed Euler confluent order is positive in the left tail

## Status

`EXACT-DERIVED` · `ARITHMETIC-FIDELITY` · `TOTAL-POSITIVITY` · `CONFLUENT-CERTIFICATE` · `LEFT-TAIL-ASYMPTOTIC` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f(t):=-\log(1-e^{-e^t}),
\qquad
H_m(t):=(-1)^{m(m-1)/2}
\det\bigl(f^{(i+j)}(t)\bigr)_{i,j=0}^{m-1}.
\]

Then **every fixed confluent order is eventually positive in the left tail**. More precisely,

\[
H_1(t)\sim -t,
\qquad
H_2(t)\to1
\qquad(t\to-\infty),
\]

and for every fixed `m>=3`,

\[
\boxed{
H_m(t)
= C_m\,e^{(m^2-5m+7)t}\,(1+o(1)),
\qquad C_m>0.
}
\tag{1}
\]

Hence for every fixed `m` there is a finite `T_m^-` such that

\[
\boxed{H_m(t)>0\qquad(t\le T_m^-).}
\tag{2}
\]

Together with AF-411, which proves the analogous statement on the right, every bounded confluent order is positive outside an order-dependent compact interval. Therefore, along any sequence

\[
|t_j|\to\infty,
\qquad
H_{m_j}(t_j)\le0,
\]

one necessarily has

\[
\boxed{m_j\to\infty.}
\tag{3}
\]

This does not prove all-order total positivity. It says that asymptotic sign failure can survive only by **order drift**.

## 1. Split the logarithmic singular coordinate from the analytic germ

Put

\[
x=e^t,
\qquad
u=-\log x=-t,
\qquad
h(x):=-\log\!\left(\frac{1-e^{-x}}{x}\right).
\]

Then

\[
f(t)=u+h(x).
\tag{4}
\]

As in AF-410, `h` is analytic for `|x|<2\pi` and has the Bernoulli expansion

\[
h(x)
=\frac{x}{2}
-\sum_{k\ge1}\frac{B_{2k}}{2k(2k)!}x^{2k}
=\frac{x}{2}-\frac{x^2}{24}+\frac{x^4}{2880}-\frac{x^6}{181440}+\cdots.
\tag{5}
\]

Write

\[
E:=x\frac d{dx},
\qquad
h_j:=E^j h.
\]

Because `d/dt=E-\partial_u`, the derivative sequence is

\[
f=u+h_0,
\qquad
f'=-1+h_1,
\qquad
f^{(j)}=h_j\quad(j\ge2).
\tag{6}
\]

Thus the derivative-Hankel matrix has the exact decomposition

\[
M_m:=\bigl(f^{(i+j)}\bigr)_{i,j=0}^{m-1}
=B_m+U,
\tag{7}
\]

where

\[
B_m=(h_{i+j})_{i,j=0}^{m-1}
\]

and `U` is supported only on its upper-left `2 x 2` block:

\[
U_{\{0,1\},\{0,1\}}
=
\begin{pmatrix}u&-1\\-1&0\end{pmatrix}.
\tag{8}
\]

The determinant of this singular block is `-1`, independent of the unbounded logarithmic variable `u`. That rank-two fact is the left-tail mechanism.

## 2. The analytic germ is a signed exponential moment family

Let

\[
\mathcal A=\{1,2,4,6,8,\ldots\}.
\]

Equation `(5)` can be written

\[
h(x)=\sum_{\lambda\in\mathcal A}c_\lambda x^\lambda,
\tag{9}
\]

with

\[
c_1=\frac12,
\qquad
c_{2k}=-\frac{B_{2k}}{2k(2k)!}\quad(k\ge1).
\tag{10}
\]

The classical Bernoulli sign rule gives

\[
\operatorname{sgn}(c_{2k})=(-1)^k.
\tag{11}
\]

Moreover

\[
h_j(x)=\sum_{\lambda\in\mathcal A}c_\lambda\lambda^j x^\lambda.
\tag{12}
\]

For any fixed finite derivative window, `(12)` is an absolutely convergent rank-one expansion when `x` is sufficiently small. Cauchy--Binet therefore gives the usual generalized-Vandermonde expansion for every finite minor of `B_m`: a nonzero `r x r` minor uses at least `r` distinct exponents from `\mathcal A`.

Define

\[
S_0:=0,
\qquad
S_r:=1+r(r-1)\quad(r\ge1).
\tag{13}
\]

`S_r` is exactly the sum of the `r` smallest exponents in `\mathcal A`, namely

\[
\Lambda_r:=\{1,2,4,\ldots,2(r-1)\}
\qquad(r\ge1),
\tag{14}
\]

with the obvious interpretation `\Lambda_1=\{1\}`. Consequently every `r x r` minor of `B_m` is

\[
O(x^{S_r})
\tag{15}
\]

for fixed `m,r` as `x\downarrow0`.

## 3. The two off-diagonal singular entries dominate the determinant

Take `m>=2` and put

\[
r=m-2.
\]

In the determinant expansion of `M_m=B_m+U`, using both rows and both columns of the `2 x 2` block `(8)` contributes

\[
\det(U_{\{0,1\},\{0,1\}})
\det(h_{a+b+4})_{a,b=0}^{r-1}
=-L_r(x),
\tag{16}
\]

where

\[
L_r(x):=\det(h_{a+b+4})_{a,b=0}^{r-1},
\qquad L_0:=1.
\tag{17}
\]

Every term using only one row/column from `U` contains an `(m-1) x (m-1)` minor of `B_m`, and the term using no `U` contains the full `m x m` determinant of `B_m`. By `(15)`,

\[
\det M_m
=-L_r(x)
+O\!\big((u+1)x^{S_{r+1}}\big)
+O(x^{S_{r+2}}).
\tag{18}
\]

Since `u=-\log x` and `S_{r+1}>S_r`, both remainder terms are `o(x^{S_r})`.

It remains only to determine the leading sign of `L_r`.

## 4. Cauchy--Binet gives the exact leading coefficient

From `(12)`,

\[
h_{a+b+4}
=\sum_{\lambda\in\mathcal A}
\bigl(c_\lambda\lambda^4x^\lambda\bigr)
\lambda^a\lambda^b.
\]

Hence

\[
L_r(x)
=
\sum_{\lambda_1<\cdots<\lambda_r\atop \lambda_j\in\mathcal A}
\left(\prod_{j=1}^r c_{\lambda_j}\lambda_j^4x^{\lambda_j}\right)
\Delta(\lambda_1,\ldots,\lambda_r)^2,
\tag{19}
\]

where `Delta` is the Vandermonde determinant. The unique lowest-power term comes from `\Lambda_r`. Therefore

\[
L_r(x)
=
(-1)^{r(r-1)/2}
K_r x^{S_r}(1+o(1)),
\tag{20}
\]

with the explicit positive constant

\[
K_r
:=
\left(\prod_{\lambda\in\Lambda_r}|c_\lambda|\lambda^4\right)
\Delta(\Lambda_r)^2>0,
\qquad K_0:=1.
\tag{21}
\]

The sign in `(20)` follows from `(11)`:

\[
\operatorname{sgn}\!\left(\prod_{\lambda\in\Lambda_r}c_\lambda\right)
=(-1)^{1+2+\cdots+(r-1)}
=(-1)^{r(r-1)/2}.
\tag{22}
\]

Combining `(18)` and `(20)`,

\[
\det M_m
=
(-1)^{1+r(r-1)/2}K_r x^{S_r}(1+o(1)).
\tag{23}
\]

The oriented confluent determinant is

\[
H_m=(-1)^{m(m-1)/2}\det M_m.
\]

Because `r=m-2`,

\[
\frac{m(m-1)}2+1+\frac{(m-2)(m-3)}2
=m(m-3)+4
\]

is always even. Thus the signs cancel exactly:

\[
\boxed{
H_m(t)=K_{m-2}x^{S_{m-2}}(1+o(1))>0
}
\tag{24}
\]

for every fixed `m>=2` and sufficiently small positive `x`.

For `m>=3`,

\[
S_{m-2}=1+(m-2)(m-3)=m^2-5m+7,
\]

which proves `(1)`. The case `m=2` gives `H_2\to K_0=1`; `m=1` follows directly from `f=u+h(x)\sim u`.

## 5. Low-order audit and consistency with the order-five calculation

The first asymptotics are

\[
\begin{aligned}
H_1(t)&\sim -t,\\
H_2(t)&\to1,\\
H_3(t)&\sim \frac12 e^t,\\
H_4(t)&\sim \frac13 e^{3t},\\
H_5(t)&\sim \frac{16}{15}e^{7t}.
\end{aligned}
\tag{25}
\]

The `m=5` coefficient independently matches the AF-408/AF-410 Toda calculation. AF-410 has

\[
H_4\sim\frac13x^3,
\qquad
A_4=-(\log H_4)''\sim\frac{24}{5}x^2,
\]

and AF-404 gives

\[
H_5H_3=H_4^2A_4.
\]

Using `H_3\sim x/2` recovers

\[
H_5\sim\frac{16}{15}x^7,
\]

exactly as `(21)`--`(24)` predict. This checks the orientation and the first nontrivial Bernoulli/Vandermonde coefficient against the independently derived order-five gate.

## Arithmetic-fidelity interpretation

AF-410 showed effective left-tail positivity for the specific order-five gate. AF-412 identifies why that phenomenon persists at **every fixed confluent order**.

The source profile splits into an unbounded logarithmic coordinate plus an analytic Bernoulli germ. Under derivative-Hankel compression, the logarithmic piece has only rank two: after the first derivative it disappears. The determinant therefore spends those two singular directions immediately, and the remaining `m-2` dimensions are filled by the smallest distinct exponential scales carried by the analytic germ. Cauchy--Binet turns that statement into the exact exponent `S_{m-2}` and the Bernoulli sign pattern cancels the orientation sign of `H_m`.

This is a concrete example of **asymptotic fidelity being controlled by rank plus source-scale diversity**, rather than by the raw size of the uncompressed coordinate. It also exposes a sharp limitation: the constants and thresholds depend on `m`. Nothing here gives uniform control as `m\to\infty`.

For the Euler-log kernel, AF-411 and AF-412 together imply that any sign obstruction escaping to either analytic tail must pay with growing determinant order. That converts the two asymptotic tails from independent sign problems into a single unbounded-order resource problem.

## Prior-art and novelty audit

The Bernoulli expansion `(5)`, the alternating sign of the even Bernoulli numbers, Cauchy--Binet, and Vandermonde determinant formulas are classical. DLMF Chapter 24 records the Bernoulli generating function and sign/zeta formulas used here.

There is substantial literature on Hankel determinants built from Bernoulli and Euler **sequences**, including Dilcher and Jiu, *Hankel Determinants of Sequences Related to Bernoulli and Euler Polynomials* (2022), and the more recent Jiu--Yin work on a sequence related to Bernoulli numbers (2026). Those papers confirm that Bernoulli Hankel structure is classical territory, but they study sequence Hankel determinants/continued fractions rather than the present derivative-Hankel `tau` function with the rank-two logarithmic block `(8)`.

A targeted search for the exact Euler-log profile and for Hankel/total-positivity results around `x/(e^x-1)` did not locate a theorem that yields `(1)` or the two-sided bounded-order consequence `(3)`. No novelty claim is made: the proof is an elementary specialization of classical Bernoulli-series and Cauchy--Binet machinery to the Mathia confluent certificate.

Sources:

- NIST DLMF, Chapter 24, *Bernoulli and Euler Polynomials*: https://dlmf.nist.gov/24
- K. Dilcher and L. Jiu, *Hankel Determinants of Sequences Related to Bernoulli and Euler Polynomials*, International Journal of Number Theory 18 (2022), arXiv:2007.09821: https://arxiv.org/abs/2007.09821
- L. Jiu and Y. Yin, *Partial Results on Hankel Determinants and the Corresponding J-Fractions of a Sequence Related to Bernoulli Numbers* (2026), arXiv:2609.05827: https://arxiv.org/abs/2609.05827

## Boundaries and falsification checks

- The theorem is **fixed-order**. Neither `(18)` nor `(24)` is uniform in `m`; the implicit constants, convergence threshold, and Vandermonde factor all depend on the order.
- The result concerns confluent derivative-Hankel certificates. AF-403 is still required to pass from a complete positive confluent flag through a fixed order to arbitrary translation minors through that order.
- The left-tail proof uses the exact support pattern `\mathcal A=\{1,2,4,6,\ldots\}` and the Bernoulli signs. A generic analytic perturbation can change the leading subset or its sign.
- The unbounded coordinate `u` is harmless only because its derivative-Hankel contribution has the exact rank-two form `(8)`. A higher-rank singular germ would change the leading minor size and exponent.
- AF-217 remains untouched: the full Euler-log kernel cannot be totally nonnegative at all orders. AF-412 only says a fixed bad order cannot persist arbitrarily far into the left tail.
- AF-410 is stronger at `m=5` in a different sense: it gives the explicit cutoff `t<=-14`. AF-412 gives existence for every fixed order but no effective general formula for `T_m^-`.
- No rational-prime discriminator appears. The argument is source-analytic and would apply to any profile with the same local Bernoulli germ; it therefore supplies no RH consequence by itself.

## Consequence for the research line

The asymptotic finite-order Euler problem is now two-sided. AF-411 proves right-tail positivity for every fixed order; AF-412 proves left-tail positivity for every fixed order. Hence each fixed-order failure set is compact, and any family of failures whose location escapes to infinity must simultaneously send the determinant order to infinity.

The useful next question is therefore no longer whether a bounded order can fail asymptotically. It is whether the order-dependent compact windows or thresholds can be controlled as `m` grows, and whether the growth rate is compatible with the all-order obstruction in AF-217. The remaining order-five problem is still the exact compact gate on `[-14,4]`; AF-412 does not bypass it.