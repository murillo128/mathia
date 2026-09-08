# AF-199 — Minimal moment-flat source geometry is a Peano B-spline derivative-norm extremal

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-BRIDGE`, `ARITHMETIC-CONTROL`, `SOURCE-CLASS-OPTIMIZATION`, `QUANTITATIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-195 shows that on `m+1` ordered distinct nodes the unique nonzero signed control annihilating every polynomial of degree below `m` is the divided-difference functional, and that normalizing its alternating positive and negative parts gives the unique mutually singular probability pair in that minimal-support class. AF-196--AF-198 then optimize the resulting fixed-`W_1` observation response by direct rational calculations for `m=3` and `m=4`.

The whole minimal-support free-node problem has a single exact spline representation.

Let

\[
u_0<u_1<\cdots<u_m,
\qquad
\lambda_j=\frac{1}{\prod_{\ell\ne j}(u_j-u_\ell)},
\tag{1}
\]

and put

\[
A=\sum_{\lambda_j>0}\lambda_j
=-\sum_{\lambda_j<0}\lambda_j>0.
\tag{2}
\]

As in AF-195, define the mutually singular probability pair by

\[
\nu:=\mu_+-\mu_-
=\frac1A\sum_{j=0}^m\lambda_j\delta_{u_j}.
\tag{3}
\]

Then `nu` annihilates all polynomials of degree below `m` and

\[
\int x^m\,d\nu(x)=\frac1A.
\tag{4}
\]

Define the classical Peano kernel of the divided difference by

\[
K_u(t)
:=
\frac{1}{(m-1)!}
\sum_{j=0}^m
\lambda_j (u_j-t)_+^{m-1},
\tag{5}
\]

and normalize it to unit integral,

\[
B_u(t):=m!\,K_u(t).
\tag{6}
\]

For ordered knots, `K_u` is the nonnegative B-spline Peano kernel of the `m`-th divided difference. In particular,

\[
K_u\ge0,
\qquad
\operatorname{supp}K_u=[u_0,u_m],
\qquad
\int K_u(t)\,dt=\frac1{m!},
\tag{7}
\]

so `B_u` is a compactly supported nonnegative spline with

\[
\int B_u=1.
\tag{8}
\]

Let

\[
F_\nu(t)=\nu(( -\infty,t])
\tag{9}
\]

be the signed cumulative distribution function. Then, almost everywhere,

\[
\boxed{
F_\nu(t)
=
\frac{(-1)^m}{m!A}\,B_u^{(m-1)}(t).
}
\tag{10}
\]

Moreover, in the sense of distributions,

\[
\boxed{
D^mB_u
=
(-1)^m m!\sum_{j=0}^m\lambda_j\delta_{u_j},
}
\tag{11}
\]

and therefore

\[
\boxed{
\|D^mB_u\|_{\mathrm{TV}}=2m!A.
}
\tag{12}
\]

Using the exact one-dimensional transport identity

\[
W_1(\mu_+,\mu_-)=\|F_\nu\|_{L^1},
\tag{13}
\]

we obtain

\[
\boxed{
W_1(\mu_+,\mu_-)
=
\frac{\|B_u^{(m-1)}\|_{L^1}}{m!A}.
}
\tag{14}
\]

Consequently the scale-free leading moment-flat response studied in AF-196--AF-198,

\[
Q_m(u_0,\ldots,u_m)
:=
\frac{\displaystyle\int x^m\,d\nu(x)}
{W_1(\mu_+,\mu_-)^m},
\tag{15}
\]

has the exact equivalent form

\[
\boxed{
Q_m
=
\frac{m!}{2^{m-1}}
\frac{\|D^mB_u\|_{\mathrm{TV}}^{m-1}}
{\|B_u^{(m-1)}\|_{L^1}^{m}}.
}
\tag{16}
\]

Thus **the free-node minimal-support moment-flat source problem is exactly a knot-optimization problem for a normalized Peano B-spline derivative-norm quotient**. The order-by-order rational objectives in AF-196--AF-198 are coordinate expressions of `(16)`, not separate phenomena.

This gives a sharper general frontier. Define

\[
C_m^{\mathrm{BS}}
:=
\sup_{u_0<\cdots<u_m}
\frac{\|B_u^{(m-1)}\|_{L^1}^{m}}
{\|D^mB_u\|_{\mathrm{TV}}^{m-1}},
\tag{17}
\]

where every `B_u` is normalized by `(6)`--`(8)`. Then

\[
\boxed{
\inf_{u_0<\cdots<u_m}Q_m
=
\frac{m!}{2^{m-1}C_m^{\mathrm{BS}}}.
}
\tag{18}
\]

Translation and common dilation of the knots leave the quotient in `(17)` invariant, so the supremum is genuinely over knot shape. A global source-class converse at cancellation order `m` is therefore equivalent to determining the sharp constant `C_m^{BS}` and its extremizing knot configurations.

For equally spaced knots with spacing `h`, `B_u` is the scaled cardinal B-spline and

\[
\|D^mB_u\|_{\mathrm{TV}}=\frac{2^m}{h^m},
\qquad
\|B_u^{(m-1)}\|_{L^1}=\frac{2^{m-1}}{h^{m-1}}.
\tag{19}
\]

Hence the quotient in `(17)` equals `1`, and

\[
\boxed{
Q_m^{\mathrm{equispaced}}=\frac{m!}{2^{m-1}}.
}
\tag{20}
\]

AF-196 and AF-197 immediately show that `C_m^{BS}>1` already for `m=3` and `m=4`: the cardinal/equispaced B-spline is not the knot extremizer for this endpoint derivative-norm ratio. In the cubic case,

\[
\frac{Q_3^{\min}}{3!/2^2}
=
\frac{189+33\sqrt{33}}{384}
\approx0.9858608524<1,
\tag{21}
\]

and the mirror-symmetric quartic optimizer from AF-197 gives

\[
\frac{Q_4(t_*)}{4!/2^3}
\approx0.9634127065<1.
\tag{22}
\]

The improvement with free nodes is therefore exactly an improvement in the B-spline derivative-norm quotient, not merely a peculiarity of the Euler logarithm or of the rational formulas chosen in those findings.

## Derivation

### 1. The Peano kernel is the repeated-antiderivative carrier of the signed source

Let

\[
L_u(f)=\sum_{j=0}^m\lambda_j f(u_j)=f[u_0,\ldots,u_m].
\tag{23}
\]

AF-195 proves that `L_u` annihilates every polynomial of degree below `m`. The classical Peano-kernel formula for an `m`-th divided difference is

\[
L_u(f)=\int f^{(m)}(t)K_u(t)\,dt,
\tag{24}
\]

with `K_u` given by `(5)`. For ordered knots this is the standard nonnegative B-spline representation of a divided difference. Applying `(24)` to `f(x)=x^m` gives

\[
1=m!\int K_u(t)\,dt,
\tag{25}
\]

which yields `(7)`--`(8)` without any convention-dependent B-spline normalization.

There is also a direct distributional derivation of the link to the signed source. Differentiating `(5)` `m` times with respect to `t` gives

\[
D^mK_u
=
(-1)^m\sum_{j=0}^m\lambda_j\delta_{u_j},
\tag{26}
\]

hence `(11)` after multiplication by `m!`.

Now let

\[
F_1(t)=F_\nu(t),
\qquad
F_k(t)=\int_{-\infty}^tF_{k-1}(s)\,ds
\quad(2\le k\le m).
\tag{27}
\]

From `(3)`,

\[
F_k(t)
=
\frac{1}{A(k-1)!}
\sum_{j=0}^m\lambda_j(t-u_j)_+^{k-1}.
\tag{28}
\]

For `t>u_m`, the right side is the divided-difference functional applied to the polynomial `(t-x)^{k-1}` of degree `<m`; it therefore vanishes. It also vanishes for `t<u_0`. Thus every `F_k`, `1\le k\le m`, is compactly supported.

Because the divided difference of the polynomial `(x-t)^{m-1}` is zero,

\[
\sum_j\lambda_j(u_j-t)_+^{m-1}
=
(-1)^m
\sum_j\lambda_j(t-u_j)_+^{m-1}.
\tag{29}
\]

Comparing `(5)`, `(28)`, and `(29)` gives

\[
\frac{K_u(t)}A=(-1)^mF_m(t).
\tag{30}
\]

Differentiating `m-1` times almost everywhere yields

\[
\frac{K_u^{(m-1)}(t)}A=(-1)^mF_\nu(t).
\tag{31}
\]

Since `B_u=m!K_u`, `(10)` follows.

Equation `(30)` also supplies a useful positivity statement in source language: the `m`-fold integrated signed source has one sign,

\[
(-1)^mF_m(t)=\frac{K_u(t)}A\ge0.
\tag{32}
\]

The alternating atom pattern of the minimal moment-flat control is therefore the `m`-th distributional derivative of a single nonnegative spline carrier.

### 2. Wasserstein separation is an endpoint derivative norm of the same spline

For probability measures on the real line, the exact Kantorovich--Rubinstein identity gives

\[
W_1(\mu_+,\mu_-)
=
\int_{\mathbb R}|F_\nu(t)|\,dt.
\tag{33}
\]

Substitution of `(10)` gives `(14)`.

The total variation of `(11)` is equally explicit. The signs of the ordered divided-difference weights alternate, and `(2)` says their positive and negative masses both equal `A`. Hence

\[
\left\|\sum_j\lambda_j\delta_{u_j}\right\|_{\mathrm{TV}}
=
\sum_j|\lambda_j|=2A,
\tag{34}
\]

which proves `(12)`.

Finally, AF-195 gives the surviving `m`-th moment `(4)`. Combining `(4)`, `(12)`, and `(14)` gives

\[
\begin{aligned}
Q_m
&=
\frac{1/A}{\left(\|B_u^{(m-1)}\|_1/(m!A)\right)^m}\\
&=(m!)^mA^{m-1}\|B_u^{(m-1)}\|_1^{-m}\\
&=
\frac{m!}{2^{m-1}}
\frac{\|D^mB_u\|_{\mathrm{TV}}^{m-1}}
{\|B_u^{(m-1)}\|_1^m},
\end{aligned}
\tag{35}
\]

which is `(16)`.

### 3. Equispaced knots recover the parity baseline at every order

For

\[
u_j=x+jh,
\qquad h>0,
\tag{36}
\]

AF-195 gives

\[
\lambda_j
=
\frac{(-1)^{m-j}}{m!h^m}\binom mj.
\tag{37}
\]

Therefore `(11)` has atom magnitudes `h^{-m}\binom mj`, whose sum is `2^mh^{-m}`, proving the first identity in `(19)`.

For the cumulative source, the partial-binomial identity

\[
\sum_{k=0}^{j}(-1)^k\binom mk
=(-1)^j\binom{m-1}{j}
\tag{38}
\]

shows that `F_nu` is constant on each interval `[u_j,u_{j+1})` with magnitude

\[
2^{1-m}\binom{m-1}{j}.
\tag{39}
\]

Hence

\[
W_1
=h\,2^{1-m}\sum_{j=0}^{m-1}\binom{m-1}{j}=h.
\tag{40}
\]

Using `(10)` and the equispaced value

\[
A=\frac{2^{m-1}}{m!h^m},
\tag{41}
\]

we obtain the second identity in `(19)`. Equations `(4)` and `(40)` then give `(20)` directly as well.

Thus the familiar parity-split binomial family has a precise spline meaning: it is the distributional `m`-th derivative of the cardinal Peano B-spline, normalized so that the positive and negative atomic parts are probabilities.

## Consequence for the source-class frontier

AF-195 removed coefficient freedom at fixed minimal support; AF-196--AF-198 then began optimizing node geometry order by order. Equation `(18)` replaces that sequence of unrelated rational minimizations by one general extremal object:

\[
C_m^{\mathrm{BS}}
=
\sup
\frac{\|B^{(m-1)}\|_1^m}
{\|D^mB\|_{\mathrm{TV}}^{m-1}}
\tag{42}
\]

over normalized Peano B-splines with exactly `m+1` distinct knots.

This gives three concrete changes to the research frontier.

First, a proposed universal lower recovery bound for minimal-support order-`m` moment-flat controls should be stated as a sharp spline interpolation/variation inequality, not inferred from one chosen stencil. If one proves

\[
\|B^{(m-1)}\|_1^m
\le C\,\|D^mB\|_{\mathrm{TV}}^{m-1}
\tag{43}
\]

for every admissible normalized Peano B-spline, then automatically

\[
Q_m\ge\frac{m!}{2^{m-1}C}.
\tag{44}
\]

Sharpness in the source problem is exactly sharpness of `(43)` on this restricted B-spline class.

Second, classical derivative inequalities can now be used honestly but must be matched to the source category. A sharp constant for a much larger Sobolev/BV function class need not be sharp for Peano B-splines with exactly `m+1` simple knots, and its extremizer may not correspond to an admissible positive source pair. Conversely, variable-knot spline or optimal-recovery theory can potentially settle the whole family without repeating the `m=3`, `m=4`, ... algebra.

Third, the cardinal/equispaced candidate is already falsified as a general knot extremizer. Equations `(21)`--`(22)` show that the quotient in `(42)` exceeds `1` once knots move optimally in the cubic and quartic examples. Any general theorem whose equality case forces equispacing is therefore the wrong inequality for this source metric.

The next exact question is consequently: **determine `C_m^{BS}` and its extremizing knot shapes, or prove a sufficiently strong asymptotic bound on it as `m` grows.** Only after the source class is controlled sharply should one ask whether the Euler harmonic ladder or another arithmetic observation defeats the resulting optimal low-band controls.

## Falsification and boundaries

- **The Peano/B-spline representation is classical.** The new durable content here is the exact identification of the AF-195 `W_1`-normalized source objective with the derivative-norm quotient `(16)` and the resulting reduction `(18)`; no novelty is claimed for divided differences, Peano kernels, B-splines, or generic optimal recovery.
- **This is the minimal-support exact-moment class only.** Extra nodes, repeated/confluent nodes, approximate moment cancellation, signed sources without the mutually singular probability normalization, or a different source complexity budget lead to different spline classes and constants.
- **The source metric is exactly one-dimensional `W_1`.** Formula `(14)` uses the CDF identity peculiar to `W_1` on the line. `W_2`, total variation, support diameter, or coefficient norms do not produce `(16)`.
- **The derivative at order `m` is a measure.** The norm in `(12)`, `(16)`, and `(17)` is total variation of the distributional derivative, not an `L^1` norm of an ordinary function.
- **A generic interpolation inequality is not automatically a source theorem.** Its function class, normalization, endpoint derivative notion, and equality cases must match the normalized Peano B-spline subclass before its sharp constant is transferred to `(18)`.
- **AF-198 remains genuinely open globally at `m=4`.** The present reduction does not prove that its symmetric critical point globally maximizes `(17)`; it only gives the correct invariant problem in which to decide that question.
- **No rational-prime specificity follows.** The source pair is a general positive atomic control. The result sharpens the adversarial geometry that a later arithmetic observable must defeat; it neither identifies the ordinary primes nor implies RH.

## Prior art and novelty assessment

The representation behind `(5)`--`(8)` is classical. Carl de Boor, **“Divided Differences,”** *Surveys in Approximation Theory* 1 (2005), 46--69, arXiv:`math/0502036`, develops univariate divided differences and their B-spline/Peano-kernel representations. Standard Peano-kernel theory says that a linear functional annihilating polynomials below degree `m` is represented against the `m`-th derivative by its truncated-power kernel; for the ordered divided-difference functional that kernel is nonnegative and is precisely a B-spline up to normalization.

The broader idea of turning recovery and differentiation questions into spline extremal problems is also established. C. A. Micchelli, T. J. Rivlin, and S. Winograd, **“The optimal recovery of smooth functions,”** *Numerische Mathematik* 26 (1976), 191--200, DOI `10.1007/BF01395972`, prove lower bounds for recovery of smooth functions from finitely many point values and show that spline interpolation at canonical knots essentially attains the bound. C. A. Micchelli and W. L. Miranker, **“Optimal Difference Schemes for Linear Initial Value Problems,”** *SIAM Journal on Numerical Analysis* 10(6) (1973), 983--1009, DOI `10.1137/0710083`, study difference methods by minimizing declared truncation-error functionals. These works make it inappropriate to present spline extremality or optimal-difference design as a new framework.

A targeted literature search found extensive classical work on Peano kernels, variable-knot splines, derivative inequalities, and optimal recovery, but did not establish that the exact restricted constant `C_m^{BS}` in `(17)` with the AF probability normalization and `W_1` source metric has a standard closed form. No novelty claim is made for that residual. The correct use of `(17)` is instead as a precise prior-art search key and a way to import any matching sharp theorem without disguising it as new Arithmetic Fidelity mathematics.

## Relation to recent findings

- **AF-195:** supplies the unique minimal-support divided-difference signed source and the normalization `A` used here.
- **AF-196:** solves `m=3` globally in knot space; in `(17)` it computes the exact `C_3^{BS}` and its extremizer.
- **AF-197:** proves a strict `m=4` improvement over the cardinal spline inside a mirror-symmetric knot family.
- **AF-198:** proves that the AF-197 shape is a strict local optimum in unrestricted five-node knot space. The remaining global problem is exactly the `m=4` instance of `(17)`.
- **This finding:** supplies the order-independent spline carrier and norm quotient that unify those source-geometry results and expose the classical approximation/optimal-recovery machinery relevant to the next step.