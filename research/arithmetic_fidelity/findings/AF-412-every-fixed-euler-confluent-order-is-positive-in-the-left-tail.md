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

Every fixed confluent order is eventually positive in the left tail. More precisely,

\[
H_1(t)\sim -t,
\qquad
H_2(t)\to1
\qquad(t\to-\infty),
\]

and for every fixed `m>=3`,

\[
\boxed{
H_m(t)=C_m e^{(m^2-5m+7)t}(1+o(1)),
\qquad C_m>0.
}
\tag{1}
\]

Hence for each fixed `m` there is a finite `T_m^-` such that

\[
\boxed{H_m(t)>0\qquad(t\le T_m^-).}
\tag{2}
\]

Combined with AF-411, every bounded confluent order is positive outside an order-dependent compact interval. Therefore any sequence satisfying

\[
|t_j|\to\infty,
\qquad
H_{m_j}(t_j)\le0
\]

must have

\[
\boxed{m_j\to\infty.}
\tag{3}
\]

Thus asymptotic sign failure can survive only through **order drift**. This is not an all-order total-positivity theorem.

## 1. Logarithmic coordinate plus analytic germ

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

As in AF-410, `h` is analytic for `|x|<2\pi` and

\[
h(x)
=\frac{x}{2}-\sum_{k\ge1}\frac{B_{2k}}{2k(2k)!}x^{2k}
=\frac{x}{2}-\frac{x^2}{24}+\frac{x^4}{2880}-\frac{x^6}{181440}+\cdots.
\tag{5}
\]

Let

\[
E:=x\frac d{dx},
\qquad
h_j:=E^j h.
\]

Since `d/dt=E-\partial_u`,

\[
f=u+h_0,
\qquad
f'=-1+h_1,
\qquad
f^{(j)}=h_j\quad(j\ge2).
\tag{6}
\]

Therefore the derivative-Hankel matrix decomposes exactly as

\[
M_m:=\bigl(f^{(i+j)}\bigr)_{i,j=0}^{m-1}=B_m+U,
\qquad
B_m=(h_{i+j})_{i,j=0}^{m-1},
\tag{7}
\]

where `U` is supported only on the upper-left `2 x 2` block,

\[
U_{\{0,1\},\{0,1\}}
=
\begin{pmatrix}u&-1\\-1&0\end{pmatrix}.
\tag{8}
\]

Its determinant is `-1`, independent of the unbounded logarithmic coordinate. This rank-two singular block is the key left-tail mechanism.

## 2. Signed exponential-moment structure

Let

\[
\mathcal A=\{1,2,4,6,8,\ldots\}.
\]

Equation `(5)` has the form

\[
h(x)=\sum_{\lambda\in\mathcal A}c_\lambda x^\lambda,
\tag{9}
\]

with

\[
c_1=\frac12,
\qquad
c_{2k}=-\frac{B_{2k}}{2k(2k)!}.
\tag{10}
\]

The classical Bernoulli sign rule gives

\[
\operatorname{sgn}(c_{2k})=(-1)^k,
\tag{11}
\]

and

\[
h_j(x)=\sum_{\lambda\in\mathcal A}c_\lambda\lambda^j x^\lambda.
\tag{12}
\]

For every fixed finite derivative window, `(12)` is an absolutely convergent rank-one expansion for sufficiently small `x`. Cauchy--Binet then implies that a nonzero `r x r` minor of `B_m` requires at least `r` distinct exponents from `\mathcal A`.

Define

\[
S_0:=0,
\qquad
S_r:=1+r(r-1)\quad(r\ge1).
\tag{13}
\]

This is the sum of the `r` smallest exponents

\[
\Lambda_r:=\{1,2,4,\ldots,2(r-1)\},
\qquad r\ge1,
\tag{14}
\]

with `\Lambda_1=\{1\}`. Hence every fixed `r x r` minor of `B_m` is `O(x^{S_r})` as `x\downarrow0`.

## 3. The rank-two block selects the leading minor

For `m>=2`, put `r=m-2`. Choosing both rows and columns of the block `(8)` in the determinant expansion gives

\[
- L_r(x),
\qquad
L_r(x):=\det(h_{a+b+4})_{a,b=0}^{r-1},
\qquad
L_0:=1.
\tag{15}
\]

Terms using only one row/column from `U` contain an `(m-1) x (m-1)` minor of `B_m`; the term using no `U` contains the full `m x m` minor. Therefore

\[
\det M_m
=-L_r(x)
+O\!\big((u+1)x^{S_{r+1}}\big)
+O(x^{S_{r+2}}).
\tag{16}
\]

Since `u=-\log x` and `S_{r+1}>S_r`, both remainders are `o(x^{S_r})`.

Now

\[
h_{a+b+4}
=\sum_{\lambda\in\mathcal A}
(c_\lambda\lambda^4x^\lambda)\lambda^a\lambda^b,
\]

so Cauchy--Binet gives

\[
L_r(x)
=
\sum_{\lambda_1<\cdots<\lambda_r}
\left(\prod_{j=1}^r c_{\lambda_j}\lambda_j^4x^{\lambda_j}\right)
\Delta(\lambda_1,\ldots,\lambda_r)^2.
\tag{17}
\]

The unique lowest-power subset is `\Lambda_r`. Thus

\[
L_r(x)
=(-1)^{r(r-1)/2}K_r x^{S_r}(1+o(1)),
\tag{18}
\]

where

\[
K_r:=
\left(\prod_{\lambda\in\Lambda_r}|c_\lambda|\lambda^4\right)
\Delta(\Lambda_r)^2>0,
\qquad K_0:=1.
\tag{19}
\]

The sign in `(18)` is exactly

\[
\operatorname{sgn}\!\left(\prod_{\lambda\in\Lambda_r}c_\lambda\right)
=(-1)^{1+2+\cdots+(r-1)}
=(-1)^{r(r-1)/2}.
\]

Combining `(16)` and `(18)`,

\[
\det M_m
=(-1)^{1+r(r-1)/2}K_r x^{S_r}(1+o(1)).
\tag{20}
\]

Since `H_m=(-1)^{m(m-1)/2}\det M_m` and `r=m-2`, the total sign exponent is

\[
\frac{m(m-1)}2+1+\frac{(m-2)(m-3)}2
=m(m-3)+4,
\]

which is always even. Therefore

\[
\boxed{
H_m(t)=K_{m-2}x^{S_{m-2}}(1+o(1))>0
}
\tag{21}
\]

for every fixed `m>=2` and sufficiently small `x>0`. For `m>=3`, `S_{m-2}=m^2-5m+7`, proving `(1)`. The case `m=2` gives `H_2\to1`; `m=1` follows from `f=u+h(x)\sim u`.

## 4. Low-order audit

The first cases are

\[
\begin{aligned}
H_1(t)&\sim -t,\\
H_2(t)&\to1,\\
H_3(t)&\sim \frac12 e^t,\\
H_4(t)&\sim \frac13 e^{3t},\\
H_5(t)&\sim \frac{16}{15}e^{7t}.
\end{aligned}
\tag{22}
\]

The `m=5` coefficient agrees independently with AF-408/AF-410. Those findings give

\[
H_4\sim\frac13x^3,
\qquad
A_4:=-(\log H_4)''\sim\frac{24}{5}x^2,
\]

while AF-404 gives `H_5H_3=H_4^2A_4`. With `H_3\sim x/2`, this yields `H_5\sim(16/15)x^7`, exactly matching `(19)`--`(21)`.

## Arithmetic-fidelity interpretation

AF-410 established effective left-tail positivity for the order-five gate. AF-412 shows that the mechanism persists at every fixed confluent order.

The source splits into an unbounded logarithmic coordinate and an analytic Bernoulli germ. Under derivative-Hankel compression, the logarithmic part has rank two: after one derivative it disappears. The determinant spends those two singular directions first, and the remaining `m-2` dimensions are filled by the smallest distinct exponential scales of the analytic germ. Cauchy--Binet makes that statement exact, while the Bernoulli sign pattern cancels the orientation sign of `H_m`.

This is a concrete example where asymptotic fidelity is controlled by **rank plus source-scale diversity**, not by the raw magnitude of the uncompressed coordinate. The limitation is equally exact: `K_r`, all implicit constants, and the positivity threshold depend on `m`. There is no uniform-in-order conclusion.

Together AF-411 and AF-412 convert both analytic tails from bounded-order sign problems into one unbounded-order resource problem: any obstruction escaping to either tail must simultaneously move to higher determinant order.

## Prior-art and novelty audit

The Bernoulli expansion, alternating even-Bernoulli signs, Cauchy--Binet, and Vandermonde formulas are classical. DLMF Chapter 24 records the relevant Bernoulli generating-function and sign/zeta formulas.

Bernoulli/Euler Hankel determinants are a substantial classical and modern topic. Dilcher and Jiu (2022) evaluate many Hankel determinants of Bernoulli/Euler sequences, and Jiu--Yin (2026) study another Bernoulli-related sequence and its J-fraction. These works are adjacent prior art, but they concern sequence Hankel determinants rather than this derivative-Hankel `tau` function with the logarithmic rank-two block `(8)`.

A targeted search for the exact Euler-log profile and for Hankel/total-positivity results around `x/(e^x-1)` did not locate a theorem yielding `(1)` or the two-sided order-drift conclusion `(3)`. No novelty claim is made: the proof is an elementary specialization of classical Bernoulli-series and Cauchy--Binet machinery.

Sources:

- NIST DLMF, Chapter 24, *Bernoulli and Euler Polynomials*: https://dlmf.nist.gov/24
- K. Dilcher and L. Jiu, *Hankel Determinants of Sequences Related to Bernoulli and Euler Polynomials*, International Journal of Number Theory 18 (2022), arXiv:2007.09821: https://arxiv.org/abs/2007.09821
- L. Jiu and Y. Yin, *Partial Results on Hankel Determinants and the Corresponding J-Fractions of a Sequence Related to Bernoulli Numbers* (2026), arXiv:2609.05827: https://arxiv.org/abs/2609.05827

## Boundaries and falsification checks

- The theorem is fixed-order. Equation `(21)` is not uniform in `m`; the constants and threshold may deteriorate rapidly with order.
- The result concerns confluent derivative-Hankel certificates. AF-403 is still needed to pass from a complete positive confluent flag through order `r` to arbitrary translation minors through that order.
- The proof uses the exact support `\mathcal A=\{1,2,4,6,\ldots\}` and Bernoulli signs. A generic analytic perturbation can change the leading subset or its sign.
- The logarithmic coordinate is harmless only because its derivative-Hankel contribution has the exact rank-two form `(8)`. A higher-rank singular germ changes the leading minor size and exponent.
- AF-217 remains untouched: the full Euler-log kernel cannot be totally nonnegative at all orders. A fixed bad order merely cannot persist arbitrarily far into the left tail.
- AF-410 remains stronger at `m=5` in one respect: it gives the explicit cutoff `t<=-14`. AF-412 gives existence for every fixed order but no effective general formula for `T_m^-`.
- No rational-prime discriminator appears. The mechanism is source-analytic and therefore gives no RH consequence by itself.

## Consequence for the research line

The finite-order Euler asymptotic problem is now two-sided. AF-411 proves right-tail positivity for every fixed order; AF-412 proves left-tail positivity for every fixed order. Thus each fixed-order failure set is compact, and a family of failures can escape in `|t|` only by sending its determinant order to infinity.

The next structural question is therefore whether the order-dependent compact windows or tail thresholds can be controlled as `m` grows, and whether their growth is compatible with the all-order obstruction in AF-217. The separate order-five compact gate on `[-14,4]` remains unresolved; AF-412 does not bypass it.