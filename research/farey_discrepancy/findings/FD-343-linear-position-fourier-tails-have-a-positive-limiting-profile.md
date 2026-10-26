# FD-343 — Linear position-Fourier tails have a positive limiting profile

**Status:** LITERATURE+DERIVED + UNCONDITIONAL-TAIL-ASYMPTOTIC + SHARP-LINEAR-SCALE.

FD-342 proves that the genuine Farey position-Fourier tail above `cQ` is
`O_c(1/Q)`. That order is sharp for every fixed `c>0`: multiplying the tail
by `Q` gives a finite, strictly positive limit. The limit is an explicit
integral of a least-common-multiple quadratic form in the classical Mertens
function. Its existence requires uniform control of the complementary-divisor
tail before arithmetic averaging; finite-period averaging alone is insufficient.

This identifies the absolute energy discarded by a linear cutoff. It gives no
new upper bound for the total Franel energy, no limit for a power-sublinear
band, and no corresponding absolute asymptotic for the **rank** spectrum.

## 1. Objects and statement

Use FD-341–FD-342's conventions, with integer order `Q>=3`:
\[
N_Q=\sum_{b\le Q}\varphi(b),\qquad
M(y)=\sum_{n\le y}\mu(n),\qquad M(y)=0\quad(0\le y<1),
\]
\[
B_Q(j)=\sum_{\substack{b\mid j\\b\le Q}}bM(Q/b),\qquad
a_{Q,j}=-\frac{B_Q(j)}{\pi j\sqrt{2N_Q}},\qquad
T_{Q,>q}=\sum_{j>q}a_{Q,j}^2.
\tag{1}
\]
All floors in `M` are implicit. For real `t>0` put
\[
f_t(k)=\frac{M(k/t)}k,\qquad
\Gamma(t)=\sum_{k,l\ge1}
 \frac{f_t(k)f_t(l)}{\operatorname{lcm}(k,l)},\qquad
\mathcal P(c)=\frac16\int_c^\infty\Gamma(t)\,dt.
\tag{2}
\]
The double series is absolutely convergent for each `t`, locally uniformly
dominated on `t>0`, and its absolute majorant is integrable on `[c,infinity)`.
The signs inside the double sum are retained.

**Theorem.** For every fixed real `c>0`, along all integer orders `Q` tending
to infinity,
\[
\boxed{Q\,T_{Q,>\lfloor cQ\rfloor}\longrightarrow\mathcal P(c),
       \qquad 0<\mathcal P(c)<\infty.}
\tag{3}
\]
More generally, for fixed `0<c<d<infinity`,
\[
\boxed{\frac1Q\sum_{cQ<j\le dQ}\frac{B_Q(j)^2}{j^2}
       \longrightarrow\int_c^d\Gamma(t)\,dt.}
\tag{4}
\]
The profile is continuous and nonincreasing on `(0,infinity)`, tends to zero
at infinity, and is strictly decreasing on `[1,infinity)`. No limit uniform
as `c` tends to zero with `Q` is asserted.

## 2. Absolute domination before taking the arithmetic mean

The only external arithmetic estimate is the classical unconditional bound
\[
|M(y)|\ll_A \frac{y}{\log^A(2y)}\qquad(y\ge1)
\tag{5}
\]
for every fixed `A>0`. Exponent two suffices for the limiting argument;
exponent four will justify an inverse series in the positivity argument.

Let
\[
u(k)=\log^{-2}(2k),\qquad
L(t)=1+\frac{\max(0,\log t)}{\log2}.
\]
FD-342, equations (9)–(10), proves
\[
C_u:=\sum_{k,l\ge1}\frac{u(k)u(l)}{\operatorname{lcm}(k,l)}<\infty.
\tag{6}
\]
For completeness, writing `k=ga,l=gb`, dropping coprimality, and applying
the integral test bounds this by
\[
\sum_{g\ge1}\frac1g
 \left(\sum_{a\ge1}\frac1{a\log^2(2ga)}\right)^2
\ll\sum_{g\ge1}\frac1{g\log^2(2g)}<\infty.
\]
When `k>=t`, the comparison
`log(2k)<=L(t) log(2k/t)` and (5) imply
\[
|f_t(k)|\ll\frac{L(t)^2}{t}u(k).
\tag{7}
\]
For `k<t` the left side is zero. Thus
\[
\sum_{k,l\ge1}\frac{|f_t(k)f_t(l)|}{\operatorname{lcm}(k,l)}
\ll C_u\frac{L(t)^4}{t^2}.
\tag{8}
\]
This proves all stated convergence and integrability properties in (2),
without treating a conditionally convergent signed sum as a positive one.

Complementary divisors give the exact identity, for every positive integer
`j`,
\[
F_Q(j):=\frac{B_Q(j)}j
 =\sum_{k\mid j}\frac{M(Qk/j)}k
 =\sum_{k\mid j}f_{j/Q}(k).
\tag{9}
\]
Terms for which `j/k>Q` vanish automatically. This keeps the moving scale
`t=j/Q` inside the coefficients; they are not constant across the band.

## 3. Fixed truncation, then uniform removal of the truncation

Fix `0<c<d` and an integer `R>=1`. Define
\[
F_{Q,R}(j)=\sum_{\substack{k\mid j\\k\le R}}f_{j/Q}(k),\qquad
\Gamma_R(t)=\sum_{k,l\le R}
 \frac{f_t(k)f_t(l)}{\operatorname{lcm}(k,l)}.
\]
For fixed `k,l`, `f_t(k)f_t(l)` is a bounded step function with finitely
many discontinuities on `[c,d]`. Sampling at the multiples of
`operatorname{lcm}(k,l)` is an ordinary Riemann sum. Hence
\[
\frac1Q\sum_{cQ<j\le dQ}F_{Q,R}(j)^2
 \longrightarrow\int_c^d\Gamma_R(t)\,dt.
\tag{10}
\]
Endpoint values at jumps do not alter the limit. In fact the functions
`M(k/t)` are left continuous, so a partition into intervals `(a,b]`
on which all the finitely many coefficients are constant handles the
finite counting directly by differences of floors.

The essential uniform estimate is not a bound on the number of divisors.
Put
\[
h_R(j)=\sum_{\substack{k\mid j\\k>R}}u(k),\qquad
C_R=\sum_{k,l>R}\frac{u(k)u(l)}{\operatorname{lcm}(k,l)}\longrightarrow0.
\]
The finite divisor-count identity gives, for every real `X>=1`,
\[
\sum_{j\le X}h_R(j)^2
 =\sum_{R<k,l\le X}u(k)u(l)
       \left\lfloor\frac X{\operatorname{lcm}(k,l)}\right\rfloor
 \le XC_R.
\tag{11}
\]
On the fixed band (7) consequently gives
\[
\frac1Q\sum_{cQ<j\le dQ}|F_Q(j)-F_{Q,R}(j)|^2
 \ll_{c,d} C_R.
\tag{12}
\]
The corresponding normalized second moments of both `F_Q` and `F_(Q,R)`
are bounded uniformly in `Q,R`, using (11) with the full weight sum.
Cauchy–Schwarz therefore bounds the difference of their normalized square
sums by `O_(c,d)(sqrt(C_R))`. Dominated convergence in (8) also gives
`int_c^d Gamma_R -> int_c^d Gamma`. Take `Q -> infinity` first in (10),
then `R -> infinity`. This proves (4).

To reach the infinite frequency tail, FD-342's uniform bound gives, for
`d>=1` and sufficiently large `Q`,
\[
\frac1Q\sum_{j>dQ}F_Q(j)^2\ll\frac{L(d)^4}{d}.
\tag{13}
\]
The right side tends to zero as `d -> infinity`. Equation (8) supplies
the same integrable control for the limiting density. Letting `d` tend
to infinity after (4) proves
\[
\frac1Q\sum_{j>cQ}F_Q(j)^2\longrightarrow
 \int_c^\infty\Gamma(t)\,dt.
\tag{14}
\]
Finally `N_Q/Q^2 -> 3/pi^2`, so
\[
Q T_{Q,>\lfloor cQ\rfloor}
 =\frac{Q^2}{2\pi^2N_Q}
       \left(\frac1Q\sum_{j>cQ}F_Q(j)^2\right)
 \longrightarrow\frac16\int_c^\infty\Gamma(t)\,dt.
\tag{15}
\]
The factor `1/6` uses the number of Farey gaps `N_Q`, not the order `Q`.

## 4. Strict positivity is an inverse-transform statement

Pointwise nonnegativity follows from the factorization
\[
\boxed{\Gamma(t)=\sum_{r\ge1}\varphi(r)C_r(t)^2,
\qquad C_r(t)=\sum_{m\ge1}\frac{f_t(rm)}{rm}.}
\tag{16}
\]
Indeed `1/lcm(k,l)=gcd(k,l)/(kl)` and
`gcd(k,l)=sum_(r|k,r|l) phi(r)`. Absolute convergence (8) justifies
all rearrangements, including the expansion of the squares.

For fixed `a,t>0` with integer `a`, exponent four in (5) gives
\[
\sum_{m\ge1}\frac{\tau(m)|f_t(am)|}{am}<\infty,
\tag{17}
\]
where `tau` is the divisor count. To check convergence, absorb finitely
many terms and use `|f_t(am)|<<_(a,t) log^(-4)(2m)` together with
`sum_(m<=X) tau(m)<=X(1+log X)`. Dyadic grouping leaves the convergent
series `sum_(h>=1) h^(-3)`. Thus Möbius inversion over multiples is
legitimate as an **absolutely convergent** double series:
\[
\sum_{n\ge1}\mu(n)C_{an}(t)
 =\sum_{m\ge1}\frac{f_t(am)}{am}\sum_{n\mid m}\mu(n)
 =\frac{f_t(a)}a.
\tag{18}
\]
If `Gamma(t)=0`, every `C_r(t)=0` by (16), and (18) forces every
`f_t(a)=0`. But for `t>=1`, taking `a=ceil(t)` gives `1<=a/t<2`,
so `M(a/t)=1`. Hence
\[
\Gamma(t)>0\qquad(t\ge1).
\tag{19}
\]
This is enough for `mathcal P(c)>0` at **every** `c>0`, since its integral
includes an interval above `max(c,1)`. It also proves strict decrease on
`[1,infinity)`. No pointwise strict-positivity claim for `0<t<1` is needed.
Continuity and decay of `mathcal P` follow from (8).

## 5. Consequence and precise boundary

The result replaces the upper estimate for the position tail with
\[
T_{Q,>\lfloor cQ\rfloor}
 =\frac{\mathcal P(c)+o_c(1)}Q,
\qquad \mathcal P(c)>0.
\tag{20}
\]
In particular no fixed linear cutoff improves that tail to `o(1/Q)`.
For the genuine ordered Farey points `0=x_0<...<x_(N_Q)=1`, put
`E_Q=sum_(k=1)^(N_Q-1) (x_k-k/N_Q)^2` and
`T_(Q,<=q)=sum_(1<=j<=q) a_(Q,j)^2`.
Together with FD-341's unconditional `K_Q=Q E_Q -> infinity` and
`T_(Q,infinity)=E_Q+1/(12N_Q)`, it also gives the exact relative-tail
description
\[
1-\frac{T_{Q,\le\lfloor cQ\rfloor}}{T_{Q,\infty}}
 =\frac{\mathcal P(c)+o_c(1)}{K_Q}.
\tag{21}
\]
This is a rate in the still-unquantified critical energy `K_Q`, not an
explicit decay rate in `Q`.

FD-342's full rank/position coefficient transfer is only `o(E_Q)` in
squared norm. Since `Q E_Q` diverges, that error need not be `o(1/Q)`.
It therefore does **not** transport (20), its positive constant, or (21)
to the rank tail at this absolute scale. Likewise, the limits above do not
allow `c=Q^(-1/2)` or `Q^(-1/3)`; neither predeclared sublinear band is
settled. No finite-control confirmation panel was used.

The profile remains a classical divisor/Mertens representation of Farey
data. Its positivity is a Gram-factorization and injectivity fact, not new
Möbius cancellation. The result sharpens the linear-band boundary without
altering the total-energy problem or providing a new RH mechanism.

## 6. Audit and prior-art boundary

A standard-library scratch audit used exact rational arithmetic. For each
`1<=R<=9` and `t` in `{1/2,1,5/4,2,7/2,5,9}`, it compared the truncated
quadratic form with the mean over one complete divisor period: 63 exact
equalities passed. The same cases passed 63 totient factorizations, and
315 individual finite inversion coordinates satisfied (18)'s truncated
identity. These checks include empty support and sign-changing Mertens
coefficients; they are not assertions that truncated forms increase in `R`.

For `R in {4,8}`, `c in {1/2,1,2}`, `d=4`, and
`Q in {16,64,256,1024}`, 24 exact moving-band sums were compared with
their piecewise integrated quadratic forms. Each error obeyed the explicit
floor-count bound `Q^(-1) sum_intervals (sum_(k<=R)|f_t(k)|)^2`.
Finally, 10,176 complementary-divisor identities (9) passed for
`3<=Q<=50`, `1<=j<=8Q`. The finite checks guard signs, endpoint convention,
LCM normalization, and inversion direction. Infinite convergence,
positivity, and the asymptotic are established by the proofs above, not
by extrapolating these checks. No Lean proof or independent adversarial
approval is claimed.

The arithmetic input (5) is Davenport's classical estimate, explicitly
stated for every fixed log exponent in equation (1.2) of Xiaoguang He and
Bingrong Huang, *Exponential sums involving the Möbius function*, Acta
Arithmetica **175**(3) (2016), 201–210,
[publisher PDF](https://www.impan.pl/shop/intranet.php?h=6534c91a557d4&p=91740&t=1697958170).
Only the unconditional zero-frequency case is used. Davenport's original
paper is *On Some Infinite Series Involving Arithmetical Functions (II)*,
Q. J. Math. **os-8** (1937), 313–320,
[DOI](https://doi.org/10.1093/qmath/os-8.1.313).

Florin P. Boca and Alexandru Zaharescu, *The correlations of Farey
fractions*, J. London Math. Soc. **72**(1) (2005), 25–39,
[primary preprint](https://arxiv.org/abs/math/0404114), use the same
Farey exponential-sum/Mertens transform in their Fourier treatment of
correlations. Their correlation scaling uses the cardinality
`N_Q asymp Q^2`; its fixed-test-function limit does not by itself justify
the moving linear-frequency tail or the interchange proved here.
M. N. Huxley, *Identities involving Farey fractions*, Proc. Steklov Inst.
Math. **276** (2012), 125–139,
[primary record](https://www.mathnet.ru/eng/tm3374), remains neighboring
weighted Franel-identity prior art.

Divisibility-density averaging, LCM/GCD quadratic forms, totient
factorization, and Möbius inversion are classical. Targeted comparisons
covered Farey Fourier tails, mesoscopic correlation formulations, and
mean-square divisor sums. No priority claim follows from not locating an
identical formula. The line-local delta beyond FD-342 is an explicit
convergent tail profile and its strict positivity, resolving whether the
existing `1/Q` remainder scale is actually attained.
