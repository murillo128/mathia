# NB-204 — Uniform growing-order van der Corput pushes positive Euler returns to quasi-polynomial shell height

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + POSITIVE-EULER + INTEGER-DISCREPANCY + GROWING-DERIVATIVE + NB-203-REFINEMENT`.

`NB-203` removed every fixed polynomial height from the positive Euler-return frontier by applying the classical `k`-th derivative test with `k` fixed before `a -> 0`. It explicitly stopped there because the constants were not controlled uniformly in `k`. A 2024 explicit theorem of Juan Arias de Reyna supplies exactly that missing ingredient: the three constants in the full van der Corput `d`-th derivative estimate stay bounded uniformly for all `d`. Choosing the derivative order to grow like `log_2(X_a/log X_a)` and re-running the `NB-202` Erdős--Turán carrier argument gives a quantitative superpolynomial obstruction.

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

Then there are constants `c,C>0`, depending only on the fixed shell parameters `r_0,Delta`, such that for all sufficiently small `a`,

\[
\boxed{
X_a^2\le |t|\le
\exp\!\left\{
\frac{X_a}{\log 2}
\bigl(\log X_a-\log\log X_a\bigr)-CX_a
\right\}
\quad\Longrightarrow\quad
\mathcal A_a(t)\ge \frac{c}{X_a}.
}
\tag{1}
\]

Consequently, any high-ordinate positive-return sequence satisfying

\[
X_a\mathcal A_a(t_a)\longrightarrow0
\]

must obey

\[
\boxed{
\liminf_{a\to0}
\frac{\log |t_a|}{X_a\log X_a}
\ge \frac1{\log 2}.
}
\tag{2}
\]

Equivalently, the return height is forced beyond

\[
|t_a|
\ge
x_a^{(1/\log 2-o(1))\log\log x_a}.
\tag{3}
\]

For a physical block `[T_a,2T_a]`, existence of such a return therefore forces

\[
\boxed{
X_a\le (\log 2+o(1))\frac{\log T_a}{\log\log T_a},
\qquad
 a\ge
\left(\frac{r_0}{\log 2}-o(1)\right)
\frac{\log\log T_a}{\log T_a}.
}
\tag{4}
\]

This is still a source-acquisition theorem, not a lower bound for the optimal Nyman--Beurling distance. Positivity remains load-bearing.

## 1. The missing input after NB-203 is genuinely uniform in derivative order

Arias de Reyna proves the following explicit all-orders form of van der Corput. Let `d>=3`, put

\[
\mathsf D=2^d,
\]

and let `f` be `d` times continuously differentiable on an interval of length `Y`, with

\[
0<\lambda\le |f^{(d)}(u)|\le\Lambda.
\]

After replacing `f` by `-f` when needed, his main theorem gives

\[
\left|
\frac1Y\sum e(f(n))
\right|
\le
\max\left\{
A_d\left(\frac{\Lambda}{\lambda Y}\right)^{2/\mathsf D},
B_d\left(\frac{\Lambda^2}{\lambda}\right)^{1/(\mathsf D-2)},
C_d(\lambda Y^d)^{-2/\mathsf D}
\right\},
\tag{5}
\]

with, uniformly for all relevant `d`,

\[
A_d<7.5,\qquad B_d<5.8,\qquad C_d<10.9.
\tag{6}
\]

The uniformity in (6) is the point that `NB-203` did not have. The derivative order can now depend on `a` without hiding an uncontrolled constant.

Apply (5) to

\[
f_m(u)=\frac{m t}{2\pi}\log u
\]

on the fixed multiplicative shell `[x_a,y_a]`. Since

\[
|f_m^{(d)}(u)|
=
\frac{(d-1)!\,m|t|}{2\pi u^d},
\tag{7}
\]

we may take

\[
\lambda=
\frac{(d-1)!\,m|t|}{2\pi y_a^d},
\qquad
\Lambda=
\frac{(d-1)!\,m|t|}{2\pi x_a^d}.
\tag{8}
\]

Writing

\[
S_m(t):=
\sum_{x_a\le n<y_a}e^{im t\log n},
\tag{9}
\]

and absorbing only constants depending on `Delta`, (5)--(8) yield

\[
\boxed{
\frac{|S_m(t)|}{x_a}
\ll_\Delta
\max\left\{
\left(\frac{e^{d\Delta}}{x_a}\right)^{2/\mathsf D},
\left(
\frac{(d-1)!\,m|t|e^{d\Delta}}{x_a^d}
\right)^{1/(\mathsf D-2)},
\left(
(d-1)!\,m|t|\rho_\Delta^d
\right)^{-2/\mathsf D}
\right\},
}
\tag{10}
\]

where

\[
\rho_\Delta:=1-e^{-\Delta}\in(0,1).
\]

Endpoint conventions change (10) by `O(1/x_a)` and are irrelevant below.

## 2. A growing derivative order gives polynomially tiny Fourier modes

Fix a sufficiently large absolute constant `K` (allowed to depend on the fixed shell width only), and define

\[
d_a:=
\left\lfloor
\log_2\frac{X_a}{K\log X_a}
\right\rfloor,
\qquad
\mathsf D_a:=2^{d_a}.
\tag{11}
\]

For sufficiently small `a`, `d_a>=3`, and

\[
\frac{X_a}{2K\log X_a}
<\mathsf D_a
\le
\frac{X_a}{K\log X_a},
\tag{12}
\]

while

\[
d_a
=
\frac{\log X_a-\log\log X_a}{\log2}+O_K(1).
\tag{13}
\]

Let `q>0` be fixed and small, and take the Erdős--Turán cutoff

\[
H_a:=\left\lfloor\frac{X_a}{q}\right\rfloor.
\tag{14}
\]

Define the explicit upper height

\[
T_*(a):=
\exp\{d_aX_a-8\mathsf D_a\log X_a\}.
\tag{15}
\]

For

\[
x_a\le |t|\le T_*(a),
\qquad 1\le m\le H_a,
\tag{16}
\]

all three terms in (10) are polynomially small in `X_a`, uniformly in `m`.

For the first term,

\[
\log\left(\frac{e^{d_a\Delta}}{x_a}\right)^{2/\mathsf D_a}
=
-\frac{2X_a}{\mathsf D_a}
+O_\Delta\left(\frac{d_a}{\mathsf D_a}\right)
\le
-2K\log X_a+o(\log X_a).
\tag{17}
\]

For the second term, (15) and `m<=H_a` give

\[
\begin{aligned}
&\log\left(
\frac{(d_a-1)!\,m|t|e^{d_a\Delta}}{x_a^{d_a}}
\right)\\
&\qquad\le
\log((d_a-1)!)+\log H_a+d_a\Delta
-8\mathsf D_a\log X_a.
\end{aligned}
\tag{18}
\]

Here

\[
\log((d_a-1)!)+\log H_a+d_a\Delta
=O_\Delta(\log X_a\log\log X_a)
=o(\mathsf D_a\log X_a),
\tag{19}
\]

because `\mathsf D_a\log X_a \gg X_a`. Hence the second term in (10) is `O(X_a^{-6})`, after increasing `K` and taking `a` small enough.

For the third term, `|t|>=x_a` implies

\[
\log\left((d_a-1)!\,m|t|\rho_\Delta^{d_a}\right)
\ge X_a-O_\Delta(\log X_a\log\log X_a)
\ge \frac12X_a,
\tag{20}
\]

so by (12) it is at most `X_a^{-K+o(1)}`. Therefore, after fixing `K` once and for all,

\[
\boxed{
\frac{|S_m(t)|}{x_a}\ll_\Delta X_a^{-5}
\qquad
(x_a\le |t|\le T_*(a),\ 1\le m\le H_a).
}
\tag{21}
\]

The exact power `5` is immaterial. What matters is that it beats the `X_a` loss incurred when integer occupancy is converted into Euler mass.

Finally, (12)--(15) imply

\[
\boxed{
\log T_*(a)
=
\frac{X_a}{\log2}
(\log X_a-\log\log X_a)
-O_{K,\Delta}(X_a).
}
\tag{22}
\]

This is where the coefficient `1/log 2` comes from: the first term of the all-orders derivative estimate forces `2^d` to stay below order `X_a/log X_a`, while the upper-frequency term then permits height roughly `x_a^d`.

## 3. Erdős--Turán converts the uniform Fourier bound into a positive-mass gap

Use the same favorable phase carrier as `NB-202`--`NB-203`,

\[
E_{a,t}(q):=
\left\{
n\in\mathbb Z\cap[x_a,y_a):
\operatorname{dist}(t\log n,2\pi\mathbb Z)
\le\frac q{X_a}
\right\}.
\tag{23}
\]

Erdős--Turán at cutoff `H_a` gives

\[
\frac{\#E_{a,t}(q)}{x_a}
\ll_\Delta
\frac q{X_a}
+\frac1{H_a}
+\sum_{m\le H_a}\frac1m\frac{|S_m(t)|}{x_a}.
\tag{24}
\]

Using (14) and (21),

\[
\boxed{
\frac{\#E_{a,t}(q)}{x_a}
\ll_\Delta
\frac q{X_a}+X_a^{-5}\log X_a.
}
\tag{25}
\]

The prime-number theorem on the fixed multiplicative shell gives `D_a\asymp_{r_0,\Delta}1`, and every normalized von-Mangoldt atom satisfies

\[
w_{n,a}\ll_{r_0,\Delta}\frac{X_a}{x_a}.
\tag{26}
\]

Therefore

\[
\sum_{n\in E_{a,t}(q)}w_{n,a}
\ll_{r_0,\Delta}
q+X_a^{-4}\log X_a.
\tag{27}
\]

Choose `q` once, sufficiently small. For all small `a`, at most one half of the positive Euler mass lies in the favorable phase carrier. Every atom outside it obeys

\[
|e^{-it\log n}-1|
\ge
2\sin\frac{q}{2X_a}
\gg_q\frac1{X_a}.
\tag{28}
\]

Positivity now yields

\[
\boxed{
\mathcal A_a(t)\gg_{r_0,\Delta}\frac1{X_a}
\qquad
(x_a\le |t|\le T_*(a)).
}
\tag{29}
\]

`NB-203` already supplies the same scale of lower bound from `X_a^2` through every fixed polynomial height, in particular through `x_a`. Combining it with (29) and then using (22) proves (1).

## 4. Coupled-width consequence

Suppose `a=a_T->0`, `t_T in [T,2T]`, `T>=X_a^2`, and

\[
X_a\mathcal A_a(t_T)\to0.
\tag{30}
\]

By (1),

\[
\log(2T)
\ge
\frac{X_a}{\log2}
(\log X_a-\log\log X_a)
-O(X_a).
\tag{31}
\]

Standard inversion of `X log X` gives

\[
X_a
\le
(\log2+o(1))\frac{\log T}{\log\log T}.
\tag{32}
\]

Since `X_a=r_0/a`, this is exactly (4). Relative to `NB-203`, which only forced `a\log T->infinity`, the growing-order estimate identifies the first quantitative scale:

\[
\boxed{
\liminf
\frac{a_T\log T}{\log\log T}
\ge
\frac{r_0}{\log2}
}
\tag{33}
\]

for this positive-shell acquisition condition.

The constant `r_0/log 2` belongs to the chosen fixed Euler shell. It is not asserted to be a universal Nyman constant, and no optimization over shell placement is claimed.

## Stress tests and limits

The key stress test is the growing derivative order. Unlike `NB-203`, no hidden `d`-dependent implied constant is used in (17)--(21): the external theorem gives bounded `A_d,B_d,C_d` for all `d`. The remaining `d`-dependence is explicit in `(d-1)!`, the derivative ratio `e^{dDelta}`, and the exponent `2^d`; all of these are retained in (10). At the chosen `d_a`, the factorial and shell-ratio costs contribute only `O(log X_a log log X_a)` to logarithms, whereas `D_a log X_a` is order `X_a`.

The coefficient `1/log 2` is a feature of this particular van der Corput hierarchy, not claimed to be a true return threshold. The proof needs Fourier control through harmonic order `H_a\asymp X_a` because the favorable angular window has width `1/X_a`. In (5), the first term deteriorates once `2^d` becomes comparable to or larger than `X_a/log X_a`; this is what fixes the usable growing order. A stronger all-orders exponential-sum theorem could move the constant or the entire scale.

Positivity is still essential. Equation (27) only says that a positive fraction of the source mass lies outside a narrow arc; (28) then turns that escaped mass into chord defect because all weights are nonnegative. Signed or complex source synthesis can cancel across phase sectors and is not constrained by this argument.

The theorem also remains an acquisition obstruction rather than a destination theorem. It does not show that a Nyman--Beurling approximant of small norm must produce the positive Euler return (30). The independent bridge from successful target approximation to this source condition is still missing.

## Generality audit

**Generality audited.** The discrepancy mechanism remains generic integer-carrier geometry. Any positive measure supported on the integer points of a fixed multiplicative shell, with total mass bounded below and point masses `O(X/x)`, inherits the same argument once the logarithmic Fourier sums satisfy (10). The new quantitative scale does not use prime-specific cancellation.

The arithmetic role of the Euler source is limited but exact: the von-Mangoldt shell supplies the normalized positive measure with `D_a\asymp1` and point-mass cap (26), while the target phase is the actual Mellin phase `t log n`. Thus the theorem is source-faithful, but its new cancellation input is still carrier-generic rather than specifically prime-distribution technology.

## Prior-art and novelty audit

The load-bearing new external source is Juan Arias de Reyna, *Explicit van der Corput's d-th derivative estimate*, arXiv:2407.02094v1 (2024). Its main theorem gives (5) with explicit constants uniformly bounded in `d`; the paper also works out applications to zeta sums. It is currently used here as a preprint source, so the evidence classification is literature-backed derivation rather than a claim of a new exponential-sum theorem. The classical Erdős--Turán inequality and the fixed-shell PNT normalization were already anchored in `SOURCES.md`.

A focused prior-art search for logarithmic-phase discrepancy, `t log n` exponential sums, and growing-order van der Corput estimates found the expected zeta-sum applications of the derivative method but no source that states the positive Euler-shell recurrence consequence (1)--(4). No novelty is claimed for the all-orders derivative estimate itself, for optimizing a zeta exponential sum over `d`, or for Erdős--Turán.

The line-local derived contribution is the simultaneous choice `d=d_a`, harmonic resolution `H_a\asymp X_a`, and true Euler point-mass normalization. That coupling converts uniform-in-order exponential-sum constants into the quasi-polynomial return-free height (1) and the explicit coupled-width floor (4).

## Consequence for the research frontier

`NB-203` left “uniform dependence on derivative order” as one of two immediate positive-source continuations. That continuation is now quantitatively resolved using an existing explicit theorem: generic integer-carrier discrepancy excludes an `o(1/X_a)` positive Euler return not merely through every fixed power of `x_a`, but through

\[
\exp\!\left\{(1/\log2+o(1))X_a\log X_a\right\}.
\]

The next positive-source frontier is therefore beyond this quasi-polynomial shell height. Further progress needs either a stronger exponential-sum input whose all-orders behavior beats the `2^d` derivative hierarchy, or genuinely von-Mangoldt-specific occupancy/cancellation. The more important independent frontiers are unchanged: pricing signed/complex synthesis and proving a destination bridge that forces any successful Nyman approximation to pay a source-acquisition condition of this type.