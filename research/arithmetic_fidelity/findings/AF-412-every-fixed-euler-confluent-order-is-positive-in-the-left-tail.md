# AF-412 — Every fixed Euler confluent order is positive in the left tail

## Status

`EXACT-DERIVED` · `ARITHMETIC-FIDELITY` · `TOTAL-POSITIVITY` · `CONFLUENT-CERTIFICATE` · `LEFT-TAIL-ASYMPTOTIC` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f(t):=-\log(1-e^{-e^t}),
\qquad
H_m(t):=(-1)^{m(m-1)/2}\det\bigl(f^{(i+j)}(t)\bigr)_{i,j=0}^{m-1}.
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
\boxed{H_m(t)=C_m e^{(m^2-5m+7)t}(1+o(1)),\qquad C_m>0.}
\tag{1}
\]

Hence for each fixed `m` there is a finite `T_m^-` such that `H_m(t)>0` for all `t<=T_m^-`. Combined with AF-411, any sequence with `|t_j|\to\infty` and `H_{m_j}(t_j)\le0` must satisfy

\[
\boxed{m_j\to\infty.}
\tag{2}
\]

Thus asymptotic sign failure can survive only through **order drift**. This is not an all-order total-positivity theorem.

## 1. Logarithmic coordinate plus analytic germ

Put

\[
x=e^t,
\qquad
v=-\log x=-t,
\qquad
h(x):=-\log\!\left(\frac{1-e^{-x}}{x}\right).
\]

Then `f(t)=v+h(x)`. As in AF-410, `h` is analytic for `|x|<2\pi` and

\[
h(x)=\frac{x}{2}-\sum_{k\ge1}\frac{B_{2k}}{2k(2k)!}x^{2k}
=\frac{x}{2}-\frac{x^2}{24}+\frac{x^4}{2880}-\frac{x^6}{181440}+\cdots.
\tag{3}
\]

Let `E:=x\,d/dx` and `h_j:=E^j h`. Since `d/dt=E-\partial_v`,

\[
f=v+h_0,
\qquad
f'=-1+h_1,
\qquad
f^{(j)}=h_j\quad(j\ge2).
\tag{4}
\]

Therefore

\[
M_m:=\bigl(f^{(i+j)}\bigr)_{i,j=0}^{m-1}=B_m+U,
\qquad
B_m=(h_{i+j})_{i,j=0}^{m-1},
\tag{5}
\]

where `U` is supported only on the upper-left `2 x 2` block

\[
U_{\{0,1\},\{0,1\}}=
\begin{pmatrix}v&-1\\-1&0\end{pmatrix}.
\tag{6}
\]

Its determinant is `-1`, independent of the unbounded logarithmic coordinate. This rank-two singular block is the key left-tail mechanism.

## 2. Signed exponential-moment structure

Let `\mathcal A=\{1,2,4,6,8,\ldots\}`. Equation `(3)` has the form

\[
h(x)=\sum_{\lambda\in\mathcal A}c_\lambda x^\lambda,
\qquad
c_1=\frac12,
\qquad
c_{2k}=-\frac{B_{2k}}{2k(2k)!}.
\tag{7}
\]

The classical Bernoulli sign rule gives `\operatorname{sgn}(c_{2k})=(-1)^k`, and

\[
h_j(x)=\sum_{\lambda\in\mathcal A}c_\lambda\lambda^j x^\lambda.
\tag{8}
\]

For every fixed finite derivative window, `(8)` is an absolutely convergent rank-one expansion for sufficiently small `x`. Cauchy--Binet implies that a nonzero `r x r` minor of `B_m` requires at least `r` distinct exponents from `\mathcal A`.

Define

\[
S_0:=0,
\qquad
S_r:=1+r(r-1)\quad(r\ge1),
\tag{9}
\]

which is the sum of the `r` smallest exponents

\[
\Lambda_r:=\{1,2,4,\ldots,2(r-1)\},
\qquad r\ge1,
\tag{10}
\]

with `\Lambda_1=\{1\}`. Hence every fixed `r x r` minor of `B_m` is `O(x^{S_r})` as `x\downarrow0`.

## 3. The rank-two block selects the leading minor

For `m>=2`, put `r=m-2`. Choosing both rows and columns of `(6)` in the determinant expansion gives

\[
-L_r(x),
\qquad
L_r(x):=\det(h_{a+b+4})_{a,b=0}^{r-1},
\qquad
L_0:=1.
\tag{11}
\]

Terms using only one row/column from `U` contain an `(m-1) x (m-1)` minor of `B_m`; the term using no `U` contains the full `m x m` minor. Therefore

\[
\det M_m=-L_r(x)+O\!\big((v+1)x^{S_{r+1}}\big)+O(x^{S_{r+2}}).
\tag{12}
\]

Since `v=-\log x` and `S_{r+1}>S_r`, both remainders are `o(x^{S_r})`.

Also

\[
h_{a+b+4}=\sum_{\lambda\in\mathcal A}(c_\lambda\lambda^4x^\lambda)\lambda^a\lambda^b,
\]

so Cauchy--Binet gives

\[
L_r(x)=
\sum_{\lambda_1<\cdots<\lambda_r}
\left(\prod_{j=1}^r c_{\lambda_j}\lambda_j^4x^{\lambda_j}\right)
\Delta(\lambda_1,\ldots,\lambda_r)^2.
\tag{13}
\]

The unique lowest-power subset is `\Lambda_r`. Thus

\[
L_r(x)=(-1)^{r(r-1)/2}K_r x^{S_r}(1+o(1)),
\tag{14}
\]

where

\[
K_r:=\left(\prod_{\lambda\in\Lambda_r}|c_\lambda|\lambda^4\right)
\Delta(\Lambda_r)^2>0,
\qquad K_0:=1.
\tag{15}
\]

Indeed,

\[
\operatorname{sgn}\!\left(\prod_{\lambda\in\Lambda_r}c_\lambda\right)
=(-1)^{1+2+\cdots+(r-1)}=(-1)^{r(r-1)/2}.
\]

Combining `(12)` and `(14)`,

\[
\det M_m=(-1)^{1+r(r-1)/2}K_r x^{S_r}(1+o(1)).
\tag{16}
\]

Since `H_m=(-1)^{m(m-1)/2}\det M_m` and `r=m-2`, the total sign exponent is

\[
\frac{m(m-1)}2+1+\frac{(m-2)(m-3)}2=m(m-3)+4,
\]

which is always even. Therefore

\[
\boxed{H_m(t)=K_{m-2}x^{S_{m-2}}(1+o(1))>0}
\tag{17}
\]

for every fixed `m>=2` and sufficiently small `x>0`. For `m>=3`, `S_{m-2}=m^2-5m+7`, proving `(1)`. The case `m=2` gives `H_2\to1`; `m=1` follows from `f=v+h(x)\sim v`.

## 4. Low-order audit

The first cases are

\[
H_1(t)\sim-t,
\quad H_2(t)\to1,
\quad H_3(t)\sim\frac12e^t,
\quad H_4(t)\sim\frac13e^{3t},
\quad H_5(t)\sim\frac{16}{15}e^{7t}.
\tag{18}
\]

The `m=5` coefficient agrees independently with AF-408/AF-410. Those findings give `H_4\sim x^3/3` and `A_4:=-(\log H_4)''\sim(24/5)x^2`, while AF-404 gives `H_5H_3=H_4^2A_4`. With `H_3\sim x/2`, this yields `H_5\sim(16/15)x^7`, matching `(15)`--`(17)`.

## Arithmetic-fidelity interpretation

AF-410 established effective left-tail positivity for the order-five gate. AF-412 shows that the mechanism persists at every fixed confluent order. The source splits into an unbounded logarithmic coordinate and an analytic Bernoulli germ. Under derivative-Hankel compression, the logarithmic part has rank two: after one derivative it disappears. The determinant spends those two singular directions first, and the remaining `m-2` dimensions are filled by the smallest distinct exponential scales of the analytic germ. Cauchy--Binet makes that statement exact, while the Bernoulli sign pattern cancels the orientation sign of `H_m`.

This is a concrete example where asymptotic fidelity is controlled by **rank plus source-scale diversity**, not by the raw magnitude of the uncompressed coordinate. The limitation is equally exact: `K_r`, all implicit constants, and the positivity threshold depend on `m`. There is no uniform-in-order conclusion.

Together AF-411 and AF-412 convert both analytic tails from bounded-order sign problems into one unbounded-order resource problem: any obstruction escaping to either tail must simultaneously move to higher determinant order.

## Prior-art and novelty audit

The Bernoulli expansion, alternating even-Bernoulli signs, Cauchy--Binet, and Vandermonde formulas are classical. DLMF Chapter 24 records the relevant Bernoulli generating-function and sign/zeta formulas.

Bernoulli/Euler Hankel determinants are a substantial classical and modern topic. Dilcher and Jiu (2022) evaluate many Hankel determinants of Bernoulli/Euler sequences, and Jiu--Yin (2026) study another Bernoulli-related sequence and its J-fraction. These works are adjacent prior art, but they concern sequence Hankel determinants rather than this derivative-Hankel `tau` function with the logarithmic rank-two block `(6)`.

A targeted search for the exact Euler-log profile and for Hankel/total-positivity results around `x/(e^x-1)` did not locate a theorem yielding `(1)` or the two-sided order-drift conclusion `(2)`. No novelty claim is made: the proof is an elementary specialization of classical Bernoulli-series and Cauchy--Binet machinery.

Sources:

- NIST DLMF, Chapter 24, *Bernoulli and Euler Polynomials*: https://dlmf.nist.gov/24
- K. Dilcher and L. Jiu, *Hankel Determinants of Sequences Related to Bernoulli and Euler Polynomials*, International Journal of Number Theory 18 (2022), arXiv:2007.09821: https://arxiv.org/abs/2007.09821
- L. Jiu and Y. Yin, *Partial Results on Hankel Determinants and the Corresponding J-Fractions of a Sequence Related to Bernoulli Numbers* (2026), arXiv:2609.05827: https://arxiv.org/abs/2609.05827

## Boundaries and falsification checks

- The theorem is fixed-order. Equation `(17)` is not uniform in `m`; the constants and threshold may deteriorate rapidly with order.
- The result concerns confluent derivative-Hankel certificates. AF-403 is still needed to pass from a complete positive confluent flag through order `r` to arbitrary translation minors through that order.
- The proof uses the exact support `\mathcal A=\{1,2,4,6,\ldots\}` and Bernoulli signs. A generic analytic perturbation can change the leading subset or its sign.
- The logarithmic coordinate is harmless only because its derivative-Hankel contribution has the exact rank-two form `(6)`. A higher-rank singular germ changes the leading minor size and exponent.
- AF-217 remains untouched: the full Euler-log kernel cannot be totally nonnegative at all orders. A fixed bad order merely cannot persist arbitrarily far into the left tail.
- AF-410 remains stronger at `m=5` in one respect: it gives the explicit cutoff `t<=-14`. AF-412 gives existence for every fixed order but no effective general formula for `T_m^-`.
- No rational-prime discriminator appears. The mechanism is source-analytic and therefore gives no RH consequence by itself.

## Consequence for the research line

The finite-order Euler asymptotic problem is now two-sided. AF-411 proves right-tail positivity for every fixed order; AF-412 proves left-tail positivity for every fixed order. Thus each fixed-order failure set is compact, and a family of failures can escape in `|t|` only by sending its determinant order to infinity.

The next structural question is whether the order-dependent compact windows or tail thresholds can be controlled as `m` grows, and whether their growth is compatible with the all-order obstruction in AF-217. The separate order-five compact gate on `[-14,4]` remains unresolved; AF-412 does not bypass it.