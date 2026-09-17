# AF-391 — Log-concave logarithmic curvature forces order-three total nonnegativity

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `TOEPLITZ` · `LOG-CONCAVITY` · `NONQUASIANALYTIC` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f:\mathbb R\to(0,\infty)
\]

be `C^2`, write

\[
g=\log f,
\qquad
q=-g'',
\tag{1}
\]

and assume that `q` is a nonnegative log-concave function in the extended sense: its positive support is an interval and `\log q` is concave there. Then the translation kernel

\[
K_f(x,y)=f(x-y)
\tag{2}
\]

is totally nonnegative through order three:

\[
K_f\in TN_3.
\tag{3}
\]

If `q>0` everywhere and is smooth, then every order-two and order-three minor with strictly increasing row and column coordinates is strictly positive. Thus log-concavity of the logarithmic curvature is a direct continuum certificate for `TP_3` away from collisions.

The theorem gives a genuinely nonquasianalytic closure mechanism for the boundary stratum isolated by AF-389 and AF-390. Flat-zero unique continuation is sufficient there, but it is not necessary for order-three fidelity: a logarithmic curvature may have an infinitely-flat zero and still force all order-three Toeplitz minors to be nonnegative through a different shape constraint.

## Proof in the positive smooth case

Assume first that `q>0` and is smooth and log-concave. Fix strictly increasing columns

\[
y_1<y_2<y_3,
\]

put

\[
a=y_2-y_1>0,
\qquad
b=y_3-y_2>0,
\tag{4}
\]

and for a row coordinate `x` write `t=x-y_1`. Dividing the row

\[
\bigl(f(t),f(t-a),f(t-a-b)\bigr)
\]

by the positive factor `f(t)` reduces every order-three determinant to the orientation determinant of the curve

\[
t\longmapsto (U(t),V(t)),
\qquad
U(t)=\frac{f(t-a)}{f(t)},
\qquad
V(t)=\frac{f(t-a-b)}{f(t)}.
\tag{5}
\]

Define the adjacent curvature masses

\[
A(t)=\int_{t-a}^{t}q(s)\,ds,
\qquad
B(t)=\int_{t-a-b}^{t-a}q(s)\,ds.
\tag{6}
\]

Since `g''=-q`,

\[
(\log U)'=A,
\qquad
(\log V)'=A+B.
\tag{7}
\]

Hence `U` and `V` are strictly increasing. Moreover

\[
\frac{V'}{U'}
=
\frac{f(t-a-b)}{f(t-a)}\,\frac{A+B}{A}.
\tag{8}
\]

Let

\[
\ell=(\log q)'.
\]

Log-concavity of `q` says that `\ell` is nonincreasing. Differentiating the interval masses gives

\[
\frac{A'}{A}
=
\frac{\int_{t-a}^{t}q(s)\ell(s)\,ds}{\int_{t-a}^{t}q(s)\,ds},
\qquad
\frac{B'}{B}
=
\frac{\int_{t-a-b}^{t-a}q(s)\ell(s)\,ds}{\int_{t-a-b}^{t-a}q(s)\,ds}.
\tag{9}
\]

The `B` interval lies entirely to the left of the `A` interval, so monotonicity of `\ell` gives

\[
\frac{B'}{B}\ge \frac{A'}{A}.
\tag{10}
\]

Taking the logarithmic derivative of (8),

\[
\frac{d}{dt}\log\frac{V'}{U'}
=
B
+
\frac{B}{A+B}
\left(
\frac{B'}{B}-\frac{A'}{A}
\right)
>0.
\tag{11}
\]

Therefore `V'/U'` is strictly increasing. Since `U'>0`, this says exactly that `V` is a strictly convex function of `U`.

For `t_1<t_2<t_3`, strict convexity gives

\[
\det
\begin{pmatrix}
1&U(t_1)&V(t_1)\\
1&U(t_2)&V(t_2)\\
1&U(t_3)&V(t_3)
\end{pmatrix}
>0.
\tag{12}
\]

Restoring the positive row factors `f(t_i)` proves positivity of every order-three minor with strictly increasing row and column coordinates. Also `q\ge0` means `g` is concave, so the usual ratio-monotonicity argument gives nonnegativity of every order-two translation minor. Order one is immediate from `f>0`. This proves `TP_3` in the positive smooth-curvature case.

## Closure across zeros of the curvature

Now let `q\ge0` be merely continuous and log-concave, allowing zeros. If `q\equiv0`, then `g` is affine and

\[
f(x)=Ce^{\alpha x};
\]

`K_f` has rank one and is totally nonnegative of every order.

Otherwise convolve `q` with a centered Gaussian approximate identity `\varphi_\varepsilon`:

\[
q_\varepsilon=q*\varphi_\varepsilon.
\tag{13}
\]

Convolution preserves log-concavity, and the Gaussian makes `q_\varepsilon` smooth and strictly positive. Choose `g_\varepsilon` by

\[
g_\varepsilon''=-q_\varepsilon,
\qquad
g_\varepsilon(0)=g(0),
\qquad
g_\varepsilon'(0)=g'(0),
\tag{14}
\]

and put `f_\varepsilon=e^{g_\varepsilon}`. Local convergence `q_\varepsilon\to q` implies `g_\varepsilon\to g` and `f_\varepsilon\to f` locally. The positive smooth case gives

\[
K_{f_\varepsilon}\in TP_3.
\]

Every fixed minor is a finite continuous expression in sampled values of `f_\varepsilon`; taking `\varepsilon\downarrow0` therefore gives the corresponding minor of `K_f` as a limit of nonnegative minors. Hence `K_f\in TN_3`.

The only external closure fact used here is the classical preservation of log-concavity under convolution; no total-positivity theorem is imported into the determinant argument.

## A genuinely nonquasianalytic flat-zero example

Define

\[
q(x)=
\begin{cases}
0,&x\le0,\\[2mm]
e^{-1/x},&x>0.
\end{cases}
\tag{15}
\]

This `q` is `C^\infty`; every derivative vanishes at `0`, but `q` is not identically zero. Thus it violates the flat-zero unique-continuation hypothesis used in AF-390. Nevertheless its support `[0,\infty)` is convex and

\[
(\log q)''(x)=-\frac{2}{x^3}<0
\qquad(x>0),
\tag{16}
\]

so `q` is log-concave in the extended sense.

Choose `g''=-q`, `g(0)=0`, and `g'(0)=c>0`, and set `f=e^g`. Then `f` is positive and smooth, its logarithmic curvature has a nontrivial infinitely-flat zero, and the theorem still gives

\[
K_f\in TN_3.
\tag{17}
\]

This example can also be chosen integrable: on the negative half-line `g(x)=cx`, while on the positive half-line `q(x)\to1`, so `g` eventually has negative quadratic growth. In the usual integrable terminology it therefore supplies a nonquasianalytic `PF_3` function with an infinitely-flat curvature boundary.

## Relation to AF-388–AF-390

AF-388 derived the local necessary inequality

\[
R=2q^3-q q''+(q')^2\ge0
\tag{18}
\]

from shrinking-mesh solid order-three positivity. Log-concavity of `q` is the stronger differential condition

\[
q q''-(q')^2\le0,
\tag{19}
\]

so it automatically lies inside the locally admissible region of (18). AF-389 then showed that any zero surviving the full smooth multiscale solid hierarchy must be infinitely flat. AF-390 removed that boundary under a quasianalytic/flat-jet uniqueness hypothesis.

AF-391 shows that a second mechanism removes it without unique continuation: **shape rigidity of the curvature itself can make the non-solid order-three determinants positive even when flat zeros genuinely exist.** Consequently any counterexample to the remaining recognition problem must leave this log-concave-curvature cone; infinite flatness alone is no longer a plausible obstruction.

What remains open is genuinely broader: whether a non-log-concave, nonquasianalytic infinitely-flat `q` can satisfy the shrinking-mesh solid `PF_2/PF_3` hierarchy while some non-solid continuum order-three minor is negative, or whether another condition weaker than log-concavity/quasianalyticity still forces `TN_3`.

## Falsification and boundary checks

- The determinant proof uses arbitrary positive column gaps `a,b`, not only equal or lattice-aligned gaps; it therefore certifies non-solid minors directly.
- The sign comes from convexity of `V` as a function of `U`; no appeal is made to the solid-minor criterion whose boundary failure motivated AF-387.
- If `q` is positive but log-concavity is dropped, inequality (10) can fail and the proof no longer controls the sign of (11). The theorem makes no claim in that region.
- If `q` has zeros, strict positivity is not claimed after passage to the limit; only total nonnegativity is stable under closure.
- The theorem is a sufficient structural certificate, not a characterization of `PF_3` and not a proof that the multiscale solid hypotheses imply log-concavity of `q`.
- No arithmetic consequence is asserted. The result belongs to Arithmetic Fidelity because it identifies a concrete information-preserving source class for the exact order-three compression/recognition obstruction shared by the current Toeplitz testbed.

## Prior art and novelty audit

H. F. Weinberger's 1983 paper *A Characterization of the Polya Frequency Functions of Order 3* gives directly adjacent classical prior art: `PF_3` translation kernels already have a dedicated necessary-and-sufficient theory. The available bibliographic/abstract-level material confirms that scope, so this finding makes **no novelty claim** for an order-three characterization or for the possibility of analytic criteria for `PF_3`. The exact curvature-log-concavity sufficient condition and the short convex-curve proof above were derived here, but they should be treated as a specialization that may be contained implicitly or explicitly in the classical characterization until the primary theorem has been compared line by line.

For the approximation step, preservation of log-concavity under convolution is classical; a modern authoritative review is Adrien Saumard and Jon A. Wellner, *Log-concavity and strong log-concavity: a review*, *Statistics Surveys* 8 (2014), 45–114, DOI `10.1214/14-SS107`.

The durable content of AF-391 is therefore the exact source-class bridge and its consequence for the AF-389/AF-390 boundary, not a priority claim over classical total-positivity theory.