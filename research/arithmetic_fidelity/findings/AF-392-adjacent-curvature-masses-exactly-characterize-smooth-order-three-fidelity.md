# AF-392 — Adjacent curvature masses exactly characterize smooth order-three fidelity

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `TOEPLITZ` · `CURVATURE-MASS` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f:\mathbb R\to(0,\infty)
\]

be `C^3`, put

\[
g=\log f,
\qquad
q=-g'',
\]

and assume

\[
q(t)>0
\qquad\text{for all }t\in\mathbb R.
\]

For every pair of positive column gaps `a,b`, define the adjacent logarithmic-curvature masses

\[
A_{a}(t)=\int_{t-a}^{t}q(s)\,ds,
\qquad
B_{a,b}(t)=\int_{t-a-b}^{t-a}q(s)\,ds.
\tag{1}
\]

Then the translation kernel

\[
K_f(x,y)=f(x-y)
\]

is totally nonnegative through order three if and only if, for every `t\in\mathbb R` and every `a,b>0`,

\[
\boxed{
A+B+\frac{B'}{B}-\frac{A'}{A}\ge0
}
\tag{2}
\]

where `A=A_a(t)` and `B=B_{a,b}(t)`. Equivalently,

\[
\boxed{
A+B
+\frac{q(t-a)-q(t-a-b)}{B}
-\frac{q(t)-q(t-a)}{A}
\ge0.
}
\tag{3}
\]

Strict inequality in `(2)` for every `t,a,b`, together with `q>0`, gives strict positivity of every non-colliding minor of orders one through three.

Thus, in the smooth positive-curvature regime, order-three translation fidelity is not controlled by a pointwise curvature condition alone. It is exactly controlled by a **two-adjacent-window comparison of curvature mass and logarithmic mass drift**.

This criterion is strictly broader than the log-concavity certificate in AF-391. In particular, sufficiently small smooth oscillations of constant curvature remain `TP_3` even though their curvature is not log-concave.

## Exact reduction to a convexity test

Fix strictly increasing columns

\[
y_1<y_2<y_3,
\qquad
a=y_2-y_1>0,
\qquad b=y_3-y_2>0,
\]

and write `t=x-y_1`. Divide each row of the corresponding order-three minor by the positive factor `f(t)`. The row becomes

\[
(1,U(t),V(t)),
\]

with

\[
U(t)=\frac{f(t-a)}{f(t)},
\qquad
V(t)=\frac{f(t-a-b)}{f(t)}.
\tag{4}
\]

Because `g''=-q`,

\[
(\log U)'=A,
\qquad
(\log V)'=A+B.
\tag{5}
\]

The hypothesis `q>0` gives `A,B>0`, so `U` and `V` are strictly increasing and `U` is a valid global local coordinate along the curve `(U,V)`.

A direct calculation gives

\[
\frac{V'}{U'}
=
\frac{f(t-a-b)}{f(t-a)}\frac{A+B}{A}.
\tag{6}
\]

Taking its logarithmic derivative,

\[
\frac{d}{dt}\log\frac{V'}{U'}
=
B+
\frac{B}{A+B}
\left(\frac{B'}{B}-\frac{A'}{A}\right)
=
\frac{B}{A+B}
\left(A+B+\frac{B'}{B}-\frac{A'}{A}\right).
\tag{7}
\]

Since the prefactor in the final expression is positive, `(2)` is equivalent to

\[
\frac{d}{dt}\frac{V'}{U'}\ge0.
\tag{8}
\]

But `V'/U'` is exactly the derivative of `V` with respect to `U`. Therefore `(2)` is equivalent to convexity of `V` as a function of `U`.

For three row coordinates `t_1<t_2<t_3`,

\[
\det
\begin{pmatrix}
1&U(t_1)&V(t_1)\\
1&U(t_2)&V(t_2)\\
1&U(t_3)&V(t_3)
\end{pmatrix}\ge0
\tag{9}
\]

for every triple if and only if that graph is convex. Restoring the positive row factors proves that `(2)` is necessary and sufficient for all order-three minors for the fixed gaps `a,b`. Requiring it for every `a,b>0` is therefore necessary and sufficient for all order-three translation minors.

Finally, `q>0` means `g` is strictly concave, which is exactly the strict `PF_2` condition for the positive translation kernel. Orders one and two are therefore already controlled, completing the equivalence with `TN_3`.

## Weighted logarithmic-drift form

Write

\[
r=(\log q)'=\frac{q'}{q}.
\]

Since

\[
A'=\int_{t-a}^{t}q(s)r(s)\,ds,
\qquad
B'=\int_{t-a-b}^{t-a}q(s)r(s)\,ds,
\]

the ratios `A'/A` and `B'/B` are the `q`-weighted means of `r` on the right and left adjacent windows respectively. Criterion `(2)` can therefore be read as

\[
\text{rightward increase of mean log-curvature slope}
\le
\text{available adjacent curvature mass}.
\tag{10}
\]

AF-391 imposed the stronger condition that `r` is nonincreasing. Then

\[
\frac{B'}{B}\ge\frac{A'}{A},
\]

so `(2)` is automatic. AF-392 identifies the exact slack: the weighted mean log-slope is allowed to increase, but not by more than `A+B`.

## A non-log-concave `TP_3` family

The exact slack is genuine. Suppose more generally that

\[
0<m\le q\le M<\infty
\]

and that `r=(\log q)'` is globally Lipschitz with constant `L`. Any point in the left window and any point in the right window are at distance at most `a+b`, hence

\[
\frac{B'}{B}-\frac{A'}{A}\ge -L(a+b).
\tag{11}
\]

Also

\[
B\ge mb,
\qquad
\frac{B}{A+B}\le\frac{Mb}{m(a+b)}.
\]

Using `(7)`,

\[
\frac{d}{dt}\log\frac{V'}{U'}
\ge
b\left(m-\frac{ML}{m}\right).
\tag{12}
\]

Consequently the uniform small-oscillation condition

\[
\boxed{L<\frac{m^2}{M}}
\tag{13}
\]

forces strict `TP_3`.

For an explicit family, take

\[
q_\varepsilon(t)=1+\varepsilon\cos t,
\qquad 0<\varepsilon<1,
\tag{14}
\]

and

\[
f_\varepsilon(t)
=
\exp\left(-\frac{t^2}{2}+\varepsilon\cos t\right).
\tag{15}
\]

Then `-(\log f_\varepsilon)''=q_\varepsilon`, while `q_\varepsilon` is not log-concave: `(\log q_\varepsilon)''` is positive near odd multiples of `\pi`.

Here

\[
m=1-\varepsilon,
\qquad M=1+\varepsilon,
\]

and

\[
\left|\left(\frac{q_\varepsilon'}{q_\varepsilon}\right)'\right|
\le
\frac{\varepsilon(1+\varepsilon)}{(1-\varepsilon)^2}.
\tag{16}
\]

Therefore every sufficiently small `\varepsilon>0` satisfying

\[
\varepsilon(1+\varepsilon)^2<(1-\varepsilon)^4
\tag{17}
\]

gives an integrable, smooth, non-log-concave `TP_3` function. This proves that the AF-391 log-concavity cone is a proper sufficient subclass, not the whole smooth positive-curvature `PF_3` region.

## Infinitesimal limit recovers the AF-388 differential inequality

Let `a,b\downarrow0`. The adjacent-window means of `r` satisfy

\[
\frac{B'}{B}-\frac{A'}{A}
=
-\frac{a+b}{2}r'(t)+o(a+b),
\]

while

\[
A+B=(a+b)q(t)+o(a+b).
\]

Substitution into `(2)` yields, after division by `a+b`,

\[
r'(t)\le2q(t),
\]

that is,

\[
(\log q)''\le2q.
\tag{18}
\]

This is exactly the interior differential condition extracted in AF-388 from shrinking solid order-three minors. The AF-388 inequality is therefore the **infinitesimal shadow** of the full adjacent-window criterion; finite non-solid placement information is precisely what is lost when only the shrinking local limit is retained.

That identifies the remaining recognition gap sharply. Any attempt to lift multiscale solid tests to continuum `TN_3` must recover enough finite-window information to promote the local inequality `(18)` to the complete family `(2)`.

## Falsification and boundaries

- Positivity of `q` is essential to the stated equivalence because it makes `U` strictly increasing and keeps `A,B` away from zero. Curvature zeros require a separate limiting/boundary analysis and are not classified here.
- Criterion `(2)` concerns every pair of positive column gaps. Checking only `a=b`, only a discrete mesh, or only the infinitesimal limit is weaker.
- The Lipschitz estimate `(13)` is only a sufficient corollary of the exact criterion; it is not necessary and is deliberately coarse.
- The oscillatory example does not show that arbitrary non-log-concave curvature works. It only proves that log-concavity is not necessary.
- No arithmetic consequence is asserted. The result is a source/target-fidelity theorem for the order-three Toeplitz recognition testbed.

## Prior art and novelty audit

The ambient mathematics is classical. I. J. Schoenberg's 1951 `PF` theory and Samuel Karlin's 1968 monograph establish the translation-kernel/total-positivity framework and the role of ratio and variation-diminishing structures. H. F. Weinberger's 1983 paper, *A Characterization of the Polya Frequency Functions of Order 3*, is directly on the same classification problem and must be treated as the primary neighboring source.

The accessible publisher and institutional metadata confirm that Weinberger gives a dedicated characterization of `PF_3` functions, but the primary article text was not available in the present literature pass. Accordingly **no novelty claim is made** for criterion `(2)`, its convex-curve reformulation, or the possibility of weaker-than-log-concavity `PF_3` certificates. They may be equivalent to, or a smooth specialization of, Weinberger's classical characterization.

The durable contribution for Arithmetic Fidelity is narrower: `(2)` is derived directly in the notation of AF-388--AF-391, it identifies exactly which finite adjacent-window information is absent from the local solid hierarchy, and it proves by `(14)`--`(17)` that the previous log-concavity closure mechanism is not necessary.

Primary/authoritative neighboring sources:

- I. J. Schoenberg, **“On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms,”** *Journal d'Analyse Mathématique* 1 (1951), 331--374, DOI `10.1007/BF02790092`.
- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968), especially the chapters on continuous Pólya-frequency functions.
- H. F. Weinberger, **“A Characterization of the Polya Frequency Functions of Order 3,”** *Applicable Analysis* 15(1--4) (1983), 53--69, DOI `10.1080/00036818308839439`.
