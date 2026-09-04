# MC-052 — Complex square-free Möbius closeness forces a simple boundary zero but only a quadratic phase budget

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
f:\mathbb N\to\mathbb C
\]

be multiplicative and supported on the square-free integers, with

\[
f(p^k)=0\quad(k\ge2),
\qquad |f(p)|\le1
\]

for every prime `p`. Assume that for some fixed

\[
0<\alpha<1
\]

its partial sums satisfy

\[
S_f(x):=\sum_{n\le x}f(n)\ll x^\alpha.
\tag{1}
\]

Write

\[
F(s)=\sum_{n\ge1}\frac{f(n)}{n^s},
\qquad
c_p:=1+f(p).
\]

Suppose also that `f` is at finite global ordinary pretentious distance from Möbius:

\[
\boxed{
\mathbb D(f,\mu;\infty)^2
=\sum_p\frac{1+\operatorname{Re}f(p)}p
<\infty.
}
\tag{2}
\]

Then the real-valued positivity conclusion of `MC-051` does not survive unchanged, but two exact facts do.

First, the Dirichlet series `F` is forced to have a **simple zero at `s=1`**. More precisely, if

\[
H(s):=\zeta(s)F(s),
\]

then `H` has a removable singularity at `1` and

\[
\boxed{H(1)=F'(1)\ne0.}
\tag{3}
\]

Thus complex phases do not evade the pole-cancellation interface at `1` that appeared in `MC-049`--`MC-051`.

Second, ordinary Möbius closeness supplies only a **quadratic** convolution budget. Equation `(2)` implies

\[
\boxed{
\sum_p\frac{|1+f(p)|^2}{p}<\infty,
}
\tag{4}
\]

and consequently both the quotient kernel `h=1*f` and its Dirichlet inverse `k=h^{-1}` satisfy

\[
\boxed{
\sum_{n\ge1}\frac{|h(n)|^2}{n}<\infty,
\qquad
\sum_{n\ge1}\frac{|k(n)|^2}{n}<\infty.
}
\tag{5}
\]

But `(2)` does **not** imply the absolute prime budget

\[
\sum_p\frac{|1+f(p)|}{p}<\infty,
\tag{6}
\]

which was automatic in the real class of `MC-051` because `1+f(p)>=0`. An explicit exact-support multiplicative phase construction below has finite ordinary distance and even a convergent nonzero Euler quotient at `s=1`, while `(6)` diverges.

This identifies the load-bearing boundary in `MC-051`. Positivity was not needed to force the simple zero at `1`; it was needed to turn holomorphic continuation into **absolute power-aware convolution control**. Once complex phases are admitted, the ordinary `1/p` metric naturally controls an `L^2` prime defect, while the direct inverse transfer requires much stronger weighted information.

For a target exponent `alpha`, a Cauchy transfer from a weighted quadratic inverse-kernel bound

\[
\sum_n\frac{|k(n)|^2}{n^\beta}<\infty
\]

preserves `x^alpha` only in the range

\[
\beta<2\alpha-1
\tag{7}
\]

(up to the logarithmic endpoint). The automatic information `(5)` is only at `beta=1`, which yields no power saving at all. At the RH scale `alpha=1/2+epsilon`, the missing quadratic information would have to reach approximately `beta<=2epsilon`, exactly the Cauchy information gap already exposed from another direction in `MC-048`.

The finding therefore narrows the complex-comparator escape rather than closing it: a viable complex route must explain how the comparator's own arithmetic upgrades the boundary/simple-zero and `L^2(p^{-1})` phase information to a genuinely power-sensitive carrier. Merely replacing real signs by phases does not by itself supply that upgrade.

## 1. Finite ordinary distance fixes the modulus of the zeta quotient at `s=1`

For `Re(s)>1`, square-free support gives

\[
F(s)=\prod_p\left(1+f(p)p^{-s}\right),
\]

so

\[
H(s)=\zeta(s)F(s)
=\prod_p
\frac{1+f(p)p^{-s}}{1-p^{-s}}.
\tag{8}
\]

For real `sigma>1`, put `u=p^{-sigma}`. Uniformly for `|f(p)|<=1`,

\[
\log\left|
\frac{1+f(p)u}{1-u}
\right|
=(1+\operatorname{Re}f(p))u+O(u^2).
\tag{9}
\]

Every coefficient `1+Re f(p)` is nonnegative, and `(2)` makes

\[
\sum_p\frac{1+\operatorname{Re}f(p)}p
\]

convergent. Dominated convergence in the first-order term of `(9)`, together with absolute convergence of `sum_p p^{-2 sigma}`, therefore gives a finite real limit

\[
\log|H(\sigma)|\longrightarrow L_f
\qquad(\sigma\downarrow1)
\]

for some finite `L_f`. Hence

\[
\boxed{|H(\sigma)|\longrightarrow C_f:=e^{L_f}\in(0,\infty).}
\tag{10}
\]

This conclusion needs no coefficientwise positivity of `H`; it uses only the nonnegative **real-part defect** already encoded by ordinary pretentious distance.

## 2. The comparator power bound upgrades the boundary modulus to a simple analytic zero

From `(1)` and partial summation,

\[
F(s)=s\int_1^\infty S_f(x)x^{-s-1}\,dx
\tag{11}
\]

throughout `Re(s)>alpha`. Thus `F` is holomorphic in a neighborhood of `s=1`.

For real `sigma>1`, equation `(8)` gives

\[
F(\sigma)=\frac{H(\sigma)}{\zeta(\sigma)}.
\]

Since

\[
\zeta(\sigma)\sim\frac1{\sigma-1},
\]

equation `(10)` yields

\[
\boxed{
\frac{|F(\sigma)|}{\sigma-1}\longrightarrow C_f\in(0,\infty).
}
\tag{12}
\]

Holomorphy now determines the zero order. If `F(1)` were nonzero, the left side of `(12)` would diverge. If `F` vanished to order at least two, it would tend to zero. Therefore `F` has a zero of order exactly one:

\[
F(1)=0,
\qquad
|F'(1)|=C_f>0.
\tag{13}
\]

Because zeta has residue `1` at its simple pole, `zeta(s)F(s)` has a removable singularity at `1` with value `F'(1)`, proving `(3)`.

This is the part of the real bootstrap that survives complexification. In `MC-051`, positivity then allowed Landau's theorem to push the Dirichlet-series abscissa of `H` all the way left to `alpha`. Here `H` has complex coefficients, so analyticity and nonvanishing at the single boundary point `1` do not provide that absolute-convergence upgrade.

## 3. Ordinary distance gives exactly an `L^2` prime-phase budget

The local defect satisfies the elementary identity

\[
|1+f(p)|^2
=1+|f(p)|^2+2\operatorname{Re}f(p)
\le
2(1+\operatorname{Re}f(p)).
\tag{14}
\]

Combining `(14)` with `(2)` proves `(4)`.

The quotient coefficients are especially simple. From `(8)`,

\[
\frac{1+f(p)z}{1-z}
=1+c_p z+c_p z^2+c_p z^3+\cdots,
\]

so

\[
h(p^j)=c_p
\qquad(j\ge1).
\tag{15}
\]

Therefore

\[
\sum_n\frac{|h(n)|^2}{n}
=
\prod_p
\left(
1+|c_p|^2\sum_{j\ge1}p^{-j}
\right).
\tag{16}
\]

The logarithm of the product is bounded by a constant multiple of

\[
\sum_p\frac{|c_p|^2}{p},
\]

which is finite by `(4)`. This proves the first half of `(5)`.

For the inverse kernel,

\[
\sum_{j\ge0}k(p^j)z^j
=
\frac{1-z}{1+f(p)z}.
\]

For `j>=1`,

\[
k(p^j)=-c_p(-f(p))^{j-1},
\tag{17}
\]

and hence

\[
|k(p^j)|\le|c_p|.
\tag{18}
\]

The same Euler-product comparison as in `(16)` proves the second half of `(5)`.

Thus complex ordinary pretentiousness is not information-free. It supplies a natural quadratic convolution norm. What it does not supply is the absolute norm used in the real `MC-051` transfer.

## 4. Why the automatic quadratic norm is at the wrong exponent

Since `mu=f*k`, equation `(1)` gives

\[
|M(x)|
\ll
x^\alpha
\sum_{d\le x}\frac{|k(d)|}{d^\alpha}.
\tag{19}
\]

Suppose more generally that for some `beta>0`,

\[
\sum_n\frac{|k(n)|^2}{n^\beta}<\infty.
\tag{20}
\]

Cauchy--Schwarz yields

\[
\sum_{d\le x}\frac{|k(d)|}{d^\alpha}
\le
\left(\sum_n\frac{|k(n)|^2}{n^\beta}\right)^{1/2}
\left(\sum_{d\le x}d^{\beta-2\alpha}\right)^{1/2}.
\tag{21}
\]

If `beta<2 alpha-1`, the second factor is bounded; at equality it is logarithmic. If `beta>2 alpha-1`, equations `(19)`--`(21)` give only

\[
M(x)\ll x^{(1+\beta)/2}
\]

at the power level. This proves `(7)`.

The automatic norm `(5)` corresponds to `beta=1`. For every `alpha<1`, `(21)` then has second factor of order `x^(1-alpha)` and gives only `M(x)<<x`. It does not transfer any fixed power saving from the comparator.

This is the same Cauchy geometry underlying Jung--Lemke Oliver's power-cancellation framework (`MC-S7`) and the explicit terminal-slab calibration in `MC-048`. The present derivation locates it directly inside the complex square-free Möbius quotient: ordinary global distance controls the square of `1+f(p)` with weight `1/p`, whereas RH-scale transfer would need quadratic control at a weight approaching `p^0`.

## 5. A phase-block matched control separates boundary convergence from absolute inversion

The loss of positivity is not merely formal. There are explicit fixed square-free-supported multiplicative functions for which the ordinary distance and the boundary Euler quotient are both well behaved, but the absolute quotient kernel already fails at the prime level.

Because

\[
\sum_p\frac1p=\infty
\]

and `1/p->0`, choose successive disjoint finite blocks of primes `B_j`, `j>=2`, in increasing prime order so that

\[
1\le L_j:=\sum_{p\in B_j}\frac1p
\le1+\frac1{j^2}.
\tag{22}
\]

Put

\[
\theta_j=\frac{(-1)^j}{j}
\]

and define the prime values

\[
f(p)=
\begin{cases}
-e^{i\theta_j},&p\in B_j,\\
-1,&p\notin\bigcup_j B_j,
\end{cases}
\tag{23}
\]

with `f(p^m)=0` for `m>=2`, extended multiplicatively on square-free integers.

Then

\[
1+\operatorname{Re}f(p)=1-\cos\theta_j
\asymp \frac1{j^2}
\]

on `B_j`, so

\[
\sum_p\frac{1+\operatorname{Re}f(p)}p
\asymp
\sum_j\frac{L_j}{j^2}<\infty.
\tag{24}
\]

By contrast,

\[
|1+f(p)|=|1-e^{i\theta_j}|
\asymp\frac1j,
\]

and therefore

\[
\boxed{
\sum_p\frac{|1+f(p)|}{p}
\asymp
\sum_j\frac{L_j}{j}
=\infty.
}
\tag{25}
\]

The quotient nevertheless has a finite nonzero Euler boundary value. Indeed,

\[
1-e^{i\theta_j}
=-i\theta_j+\frac{\theta_j^2}{2}+O(|\theta_j|^3),
\]

so, in natural prime order,

\[
\sum_p\frac{1+f(p)}p
=
\sum_j L_j(1-e^{i\theta_j})
\tag{26}
\]

converges: the first-order imaginary term is an alternating harmonic series, while the real and higher-order terms converge absolutely. Since

\[
\log\frac{1+f(p)/p}{1-1/p}
=
\frac{1+f(p)}p+O\!\left(\frac1{p^2}\right),
\tag{27}
\]

the Euler product for `H` converges at `s=1` to a finite nonzero complex value even though the absolute prime convolution mass `(25)` diverges.

This control deliberately does **not** assert the independent power bound `(1)`. Its role is narrower and decisive: finite ordinary distance, square-free multiplicativity, and even a nonzero boundary value of the zeta quotient do not recover the absolute kernel needed by `MC-051`. Any complex analogue of that bootstrap must use genuinely additional information from the comparator's cancellation or analytic continuation, not merely the same boundary data with phases allowed.

## 6. Unimodular specialization is a pretentious Helson-zeta problem

A particularly natural complex subclass writes

\[
f(n)=\mu(n)\chi(n),
\tag{28}
\]

where `chi` is completely multiplicative and unimodular. Then

\[
f(p)=-\chi(p),
\qquad
\mathbb D(f,\mu;\infty)^2
=
\sum_p\frac{1-\operatorname{Re}\chi(p)}p
=
\mathbb D(\chi,1;\infty)^2.
\tag{29}
\]

Moreover

\[
F(s)
=\prod_p(1-\chi(p)p^{-s})
=\frac1{\zeta_\chi(s)},
\tag{30}
\]

where

\[
\zeta_\chi(s)
=\prod_p(1-\chi(p)p^{-s})^{-1}
\]

is a Helson zeta function.

Thus `(1)` plus finite global distance in `(29)` force `1/zeta_chi(s)` to extend holomorphically to `Re(s)>alpha` and, by Sections 1--2, to have a simple zero at `1`. Equivalently, the induced meromorphic continuation of `zeta_chi` has a simple pole at `1`.

This places the surviving complex-comparator question next to established Helson-zeta prior art. Bochkov--Romanov and Bochkov construct Helson zeta functions with highly flexible prescribed zero/pole divisors in substantial substrips, and Andersson extends divisor/domain flexibility much further; these results are already summarized in `research/prior_art/incremental/PA-helson-zeta-divisor-and-continuation-flexibility.md`. They show that prime-phase Euler products as a broad ambient class do not have the rigidity enjoyed by zeta.

But that literature does **not** supply a matched counterexample to the present hypotheses. The retained Helson-flexibility results do not establish that their prescribed-divisor characters satisfy finite `D(chi,1;infinity)`, nor that the reciprocal coefficients `mu(n)chi(n)` obey an independently proved fixed power bound. Those two restrictions are exactly the information under audit here.

## 7. Prior-art and novelty boundary

The ordinary pretentious metric and its limitation for power cancellation are established theory; `MC-S4`--`MC-S7` and Jung--Lemke Oliver in particular already show that ordinary prime-level closeness does not generally preserve power exponents. The Cauchy threshold `(7)` is the same classical transfer geometry isolated quantitatively in `MC-048`.

The real square-free-supported positivity bootstrap is the immediately preceding Mathia result `MC-051`; its use of nonnegative coefficients is a classical Landau mechanism rather than a new analytic-number-theory theorem. The calculations `(9)`--`(18)` identify what remains when that positivity is removed.

Helson-zeta divisor flexibility is established prior art: I. Bochkov and R. Romanov, *On zeroes and poles of Helson zeta functions*, Journal of Functional Analysis 282 (2022), 109398, arXiv `2106.15949`; I. Bochkov, *Helson zeta functions for characters with finitely many values*, Bulletin of the London Mathematical Society 55 (2023), 2233--2241, DOI `10.1112/blms.12847`; and Johan Andersson, *Mittag-Leffler type theorems for Helson zeta-functions*, arXiv `2408.15713` (2024). The canonical repository summary is `research/prior_art/incremental/PA-helson-zeta-divisor-and-continuation-flexibility.md`.

No novelty is claimed for those general results or for the principle that complex phases destroy coefficientwise positivity. The durable line-specific contribution is the exact boundary synthesis: under the full comparator hypotheses, finite ordinary Möbius distance still forces a **simple analytic zero at `1`**, but the same metric controls only the quadratic prime defect `(4)`; the phase-block construction shows that even a nonzero boundary Euler quotient does not upgrade that defect to absolute inversion. This identifies a precise additional proof obligation rather than treating "complex phases" as an undifferentiated escape hatch.

## 8. Consequence for the comparator frontier

`MC-050` ruled out fixed globally Möbius-close exact-support sign comparators as an independently easier route. `MC-051` showed that the sign discreteness was inessential throughout the real interval `[-1,1]`: positivity of the zeta quotient was the true carrier.

The present finding draws the next boundary. Complexification removes that positivity, but it does **not** remove all rigidity. The comparator must still cancel the zeta pole exactly once at `1`, and ordinary global closeness still imposes an `L^2(p^{-1})` phase budget. What remains missing is a theorem that propagates this boundary/quadratic information to the much stronger power-weighted regime needed for inverse transfer.

A next complex-comparator proposal is substantive only if it supplies such a propagation mechanism from independently weaker arithmetic data. Three routes remain logically distinct: a theorem upgrading the quadratic prime defect to `beta<2 alpha-1`; a signed or bilinear inversion that avoids absolute Cauchy transfer; or a rigidity theorem for globally pretentious Helson characters with power-cancellative reciprocal coefficients. Without one of those, allowing complex phases merely removes the real positivity proof while leaving the Mertens-scale obligation unresolved.