# NB-205 — Ford's zeta-sum bound pushes positive Euler returns to Vinogradov--Korobov height

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + POSITIVE-EULER + INTEGER-DISCREPANCY + EXPONENTIAL-SUM + NB-204-REFINEMENT`.

`NB-202` converted integer-carrier discrepancy into a positive Euler-return obstruction, `NB-203` removed every fixed polynomial shell height, and `NB-204` used a derivative order growing with the Mellin shell parameter to reach quasi-polynomial height. There is a substantially stronger classical exponential-sum input already adapted to the phase `t log n`: Kevin Ford's explicit Vinogradov--Korobov estimate for partial sums of `(n+u)^(-it)`. Coupling Ford's bound to the same Erdős--Turán occupancy argument pushes the positive-return-free corridor to the scale

\[
\exp\!\left\{
\left(\frac1{\sqrt{133.66}}-o(1)\right)
\frac{X_a^{3/2}}{\sqrt{\log X_a}}
\right\}.
\]

Keep

\[
x_a=e^{r_0/a},\qquad X_a=\log x_a=\frac{r_0}{a},\qquad y_a=e^\Delta x_a,
\]

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x_a,y_a)}(n),
\]

and

\[
\mathcal A_a(t):=\sum_n w_{n,a}|e^{-it\log n}-1|.
\]

For every fixed

\[
0<\kappa<\frac1{\sqrt{133.66}},
\tag{1}
\]

there is `c_kappa>0` such that, for all sufficiently small `a`,

\[
\boxed{
X_a^2\le |t|\le
\exp\!\left\{
\kappa\frac{X_a^{3/2}}{\sqrt{\log X_a}}
\right\}
\quad\Longrightarrow\quad
\mathcal A_a(t)\ge \frac{c_\kappa}{X_a}.
}
\tag{2}
\]

The part below a fixed multiple of `x_a` is inherited from `NB-204`; the new Ford step handles the larger heights. Consequently any high-ordinate positive-return sequence satisfying

\[
X_a\mathcal A_a(t_a)\longrightarrow0
\]

must obey

\[
\boxed{
\liminf_{a\to0}
\frac{\log|t_a|\sqrt{\log X_a}}{X_a^{3/2}}
\ge
\frac1{\sqrt{133.66}}
=0.08649\ldots .
}
\tag{3}
\]

For a physical block `[T_a,2T_a]`, (3) yields the necessary coupled-width condition

\[
\boxed{
X_a\le
\left(\frac{2\cdot133.66}{3}+o(1)\right)^{1/3}
(\log T_a)^{2/3}(\log\log T_a)^{1/3},
}
\tag{4}
\]

or equivalently

\[
\boxed{
a\ge
r_0\left(\frac3{2\cdot133.66}+o(1)\right)^{1/3}
\frac1{(\log T_a)^{2/3}(\log\log T_a)^{1/3}}.
}
\tag{5}
\]

The leading numerical factor in (5), apart from `r_0`, is `0.22389...`. This remains a source-acquisition theorem rather than a lower bound for the optimal Nyman--Beurling distance, and positivity remains load-bearing.

## 1. Ford gives the right logarithmic phase sum directly

Ford defines, for a positive integer `N` and `N<=tau`,

\[
S(N,\tau):=
\max_{0<u\le1}\max_{N<R\le2N}
\left|
\sum_{N<n\le R}(n+u)^{-i\tau}
\right|,
\]

and proves

\[
\boxed{
S(N,\tau)\le
9.463\,N^{1-1/(133.66\lambda^2)},
\qquad
\lambda=\frac{\log\tau}{\log N}.
}
\tag{6}
\]

Thus

\[
N^{-1/(133.66\lambda^2)}
=
\exp\!\left\{
-\frac{(\log N)^3}{133.66(\log\tau)^2}
\right\}.
\tag{7}
\]

The shift in Ford's notation causes no mismatch. A sum of `n^{-i\tau}` over an integer interval is obtained from `(n+u)^{-i\tau}` by taking `u=1` and shifting the integer index, with at most endpoint terms. Negative `tau` is handled by complex conjugation.

Partition the fixed multiplicative shell `[x_a,e^\Delta x_a)` into `O_Delta(1)` intervals of ratio at most two. On every piece the left endpoint `N` satisfies

\[
\log N=X_a+O_\Delta(1).
\tag{8}
\]

For

\[
S_m(t):=
\sum_{x_a\le n<y_a}e^{im t\log n}
\tag{9}
\]

and `|t|>=e^Delta x_a`, Ford applies on every shell piece to `tau=m|t|`. Hence, uniformly for `m>=1`,

\[
\boxed{
\frac{|S_m(t)|}{x_a}
\ll_\Delta
\exp\!\left\{
-\frac{(1-o(1))X_a^3}
{133.66\,[\log(m|t|)]^2}
\right\}.
}
\tag{10}
\]

The `o(1)` in (10) is uniform in the range used below. The constant `9.463`, the finite shell partition and endpoint terms affect only multiplicative constants, not the exponent threshold.

## 2. Erdős--Turán converts Ford's cancellation into sparse favorable cells

Fix a sufficiently small constant `q>0` and define the favorable carrier

\[
E_{a,t}(q):=
\left\{
n\in[x_a,y_a):
\operatorname{dist}(t\log n,2\pi\mathbb Z)
\le\frac q{X_a}
\right\}.
\tag{11}
\]

Apply the one-dimensional Erdős--Turán inequality with

\[
H_a:=\left\lfloor\frac{X_a}{q}\right\rfloor.
\tag{12}
\]

The interval-length term and the truncation term are both `O(q/X_a)`. Writing `Q=log|t|`, the Fourier contribution is bounded using (10): for `1<=m<=H_a`,

\[
\log(m|t|)=Q+O(\log X_a).
\tag{13}
\]

Therefore, throughout the Ford range,

\[
\boxed{
\frac{\#E_{a,t}(q)}{x_a}
\ll_\Delta
\frac q{X_a}
+
\log X_a\,
\exp\!\left\{
-\frac{(1-o(1))X_a^3}
{133.66\,Q^2}
\right\}.
}
\tag{14}
\]

The harmonic factor `log X_a` in (14) comes from `sum_(m<=H_a) 1/m`; using all Fourier modes up to angular resolution `1/X_a` is essential.

The normalized Euler shell has the pointwise atom cap already used in `NB-202`,

\[
w_{n,a}\ll_{r_0,\Delta}\frac{X_a}{x_a}.
\tag{15}
\]

Indeed `D_a asymp_(r_0,Delta) 1` by the prime number theorem, while `Lambda(n)<=log n=X_a+O_Delta(1)` on the shell. Multiplying (14) by (15) gives

\[
\boxed{
\sum_{n\in E_{a,t}(q)}w_{n,a}
\ll
q+
X_a\log X_a\,
\exp\!\left\{
-\frac{(1-o(1))X_a^3}
{133.66\,Q^2}
\right\}.
}
\tag{16}
\]

Now suppose

\[
Q\le
\kappa\frac{X_a^{3/2}}{\sqrt{\log X_a}}
\tag{17}
\]

with fixed `kappa<1/sqrt(133.66)`. Then

\[
\frac{X_a^3}{133.66Q^2}
\ge
\left(\frac1{133.66\kappa^2}+o(1)\right)\log X_a,
\tag{18}
\]

and the exponent coefficient on the right is strictly larger than one. Thus the second term in (16) tends to zero. Choosing `q` once and for all sufficiently small, the favorable cells carry less than (say) half the normalized positive Euler mass for all small `a`.

## 3. Positive mass outside the cells forces a chord gap

For every `n` outside `E_{a,t}(q)`,

\[
|e^{-it\log n}-1|
\ge
2\sin\frac q{2X_a}
\gg_q\frac1{X_a}.
\tag{19}
\]

Since all `w_(n,a)` are nonnegative, (16)--(19) imply

\[
\mathcal A_a(t)\gg_{q,r_0,\Delta}\frac1{X_a}
\tag{20}
\]

uniformly for

\[
e^\Delta x_a\le|t|\le
\exp\!\left\{
\kappa\frac{X_a^{3/2}}{\sqrt{\log X_a}}
\right\}.
\tag{21}
\]

`NB-204` already gives the same `Omega(1/X_a)` lower bound from `X_a^2` far beyond every fixed multiple of `x_a`, so its range overlaps (21) and supplies the lower part of (2). This proves the claimed corridor.

The scale in (3) is therefore not a heuristic first-hit estimate. It is a deterministic exclusion scale inherited from Ford's uniform exponential-sum theorem plus positive Euler occupancy.

## 4. Inverting the return height gives a new coupled-width floor

Let `Q_a=log T_a`. If `[T_a,2T_a]` contains an `o(1/X_a)` positive return, (3) implies

\[
Q_a\ge
\left(\frac1{\sqrt{133.66}}-o(1)\right)
\frac{X_a^{3/2}}{\sqrt{\log X_a}}.
\tag{22}
\]

Squaring and rearranging,

\[
X_a^3\le
(133.66+o(1))Q_a^2\log X_a.
\tag{23}
\]

At the boundary scale `log X_a=(2/3+o(1))log Q_a`, so

\[
X_a\le
\left(\frac{2\cdot133.66}{3}+o(1)\right)^{1/3}
Q_a^{2/3}(\log Q_a)^{1/3},
\tag{24}
\]

which is (4). Since `a=r_0/X_a`, (5) follows.

This is asymptotically stronger than the `NB-204` source-acquisition floor of order `(log log T)/(log T)`: the Ford input changes the height law itself, not merely its constant.

## 5. Adversarial checks and representation audit

**Range of Ford's theorem.** Equation (6) requires `N<=tau`. The new step is therefore asserted only from `|t|>=e^Delta x_a`, which guarantees the hypothesis on every factor-two piece of the fixed shell for every `m>=1`. The already-proved `NB-204` corridor fills the lower range. No extension of Ford below its stated hypothesis is used.

**Shift, sign and shell partition.** Ford's `(n+u)^(-it)` family contains the needed integer sum after an index shift with `u=1`; endpoint changes are `O(1)`. Negative ordinates are conjugates. A shell of fixed logarithmic width requires only `O_Delta(1)` factor-two pieces, so the partition does not alter the exponent in (10).

**Erdős--Turán resolution.** The cutoff `H_a~X_a/q` is retained explicitly. The `1/H_a` truncation contribution is of the same order as the favorable arc length, and the factor `m` changes `log|t|` only by `O(log X_a)` in the target regime. The threshold `1/sqrt(133.66)` comes from demanding that the Ford saving beat the Euler atom-cap factor `X_a` (with the extra harmonic `log X_a` lower-order).

**What is arithmetic-specific.** Once one has a positive probability measure on an integer multiplicative shell with atom size `O(X/x)`, Ford's carrier estimate drives the same occupancy obstruction. The specifically Euler arithmetic is used to normalize the von-Mangoldt shell and obtain the atom cap; the exponential-sum cancellation itself is an all-integers logarithmic-carrier theorem. Thus this is not a new prime-distribution theorem.

**What is not proved.** Positivity is essential in passing from small favorable mass to the chord lower bound. Signed or complex synthesis may cancel between phase sectors and is untouched. More importantly, nothing here proves that a Nyman--Beurling approximant resolving the target must realize an `o(a)` positive Euler-shell return. The destination-coupled bridge remains a separate load-bearing problem, so (5) must not be read as a lower bound for the optimal Nyman--Beurling approximation width or distance.

**Method frontier.** The constant and height scale are inherited from Ford's theorem. A stronger uniform bound for logarithmic exponential sums would immediately improve the positive-source frontier through the same Erdős--Turán plus atom-cap transfer. Conversely, improving only the PNT remainder or short-interval prime resolution does not address this carrier bound.

## Prior-art boundary

Ford's 2002 theorem is classical and is not claimed as new. The new line-local step is the coupling of his explicit bound

\[
S(N,t)\le9.463N^{1-1/(133.66\lambda^2)}
\]

with the `NB-202` angular-resolution Erdős--Turán occupancy argument and the normalized Euler atom cap. A prior-art search located Ford's original paper and later references to its zeta-function consequences, but no source using this theorem as a positive Euler-shell return obstruction in the coupled Nyman--Beurling acquisition problem.

## Consequence for the research frontier

The generic integer-carrier positive branch is no longer limited to polynomial or quasi-polynomial shell heights. Its certified exclusion scale is now Vinogradov--Korobov-shaped,

\[
\log |t|\asymp
\frac{X_a^{3/2}}{\sqrt{\log X_a}},
\]

with the explicit Ford constant on the current transfer. The next positive-source question is therefore whether sharper logarithmic exponential-sum estimates, or a source-specific weighted estimate for the actual von-Mangoldt shell, can push beyond Ford's all-integers carrier law. The two structurally distinct open fronts remain unchanged: control signed/complex synthesis, and prove (or replace) the destination bridge that would make a positive Euler return necessary for successful Nyman approximation.
