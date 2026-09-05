# ANF-061 — quadratic height renormalization closes the common-translation escape

**Status:** `EXACT-DERIVED + HEIGHT-RENORMALIZED-FOURIER-TAIL + ZERO-LEVEL-COMPACTIFICATION + STRUCTURAL-REDUCTION`. `ANF-044` compactifies negative two-pair five-point defects on an interior height slab, but its horizontal escape constant degenerates as the lower height cutoff tends to zero. `ANF-060` removes the large-height problem for the fixed Montgomery--Taylor profile and leaves common horizontal translation as the only unbounded variable in the exact base-zero search. The missing boundary uniformity can be recovered by dividing the anchor amplitudes by their natural quadratic height scale before applying uniform Riemann--Lebesgue decay.

For every nonzero continuous even compactly supported `J>=0`, every finite `Y,D`, and

\[
H_J(y_1,y_2;t+d,t)
=Q(y_1,y_2;d)+P(y_1,y_2;d)+\operatorname{Re}Z_{y_1,y_2,d}(t)
\tag{1}
\]

in the exact Hilbert normal form of `ANF-045`, there exist `T<infinity` and `c>0`, depending only on `J,Y,D`, such that

\[
\boxed{
0\le y_1,y_2\le Y,
\quad |d|\le D,
\quad |t|\ge T
\quad\Longrightarrow\quad
H_J(y_1,y_2;t+d,t)
\ge c\,(y_1^2+y_2^2).
}
\tag{2}
\]

The bound includes the zero-height boundary. It is strict whenever at least one height is positive. Thus bounded relative separation plus bounded height already prevents a genuine five-point zero from escaping by common horizontal translation, even along sequences with one or both heights tending to zero.

For Montgomery--Taylor, intersecting (2) with `ANF-060` yields a finite constant `T_MT` for which every genuine zero or negative value must satisfy

\[
\boxed{
0.545<|d|<1.01,
\qquad
\frac{|y_1-y_2|}{y_1+y_2}>0.1409,
\qquad
y_1+y_2<1.500355,
\qquad
|t_2|<T_{\rm MT}.
}
\tag{3}
\]

Since `t_1=t_2+d`, also `|t_1|<T_MT+1.01`. The accepted Montgomery--Taylor base-zero problem is therefore bounded in every geometric variable before any interval certificate is attempted; the remaining boundary faces are finite, not noncompact.

## 1. Factor out the quadratic height scale

Retain the notation of `ANF-045`,

\[
a_y(\alpha)=\cosh(2\pi\alpha y)-1.
\tag{4}
\]

For `y>0` define

\[
r_y(\alpha)
:=\frac{\cosh(2\pi\alpha y)-1}{y^2},
\tag{5}
\]

and extend continuously to `y=0` by

\[
\boxed{r_0(\alpha)=2\pi^2\alpha^2.}
\tag{6}
\]

Because the quotient in (5) has an even power series in `y`, `(alpha,y) -> r_y(alpha)` is continuous on every compact rectangle `[-B,B] x [0,Y]`. Hence

\[
y\longmapsto J(\alpha)r_y(\alpha)
\tag{7}
\]

is continuous from `[0,Y]` into `L^1`, and its image is compact.

Write

\[
R_y(s)
:=\int J(\alpha)r_y(\alpha)e^{2\pi i\alpha s}\,d\alpha.
\tag{8}
\]

The compact-family Riemann--Lebesgue lemma already used in `ANF-044` now gives the boundary-uniform decay

\[
\boxed{
\sup_{0\le y\le Y}|R_y(s)|\longrightarrow0
\qquad(|s|\to\infty).
}
\tag{9}
\]

This is the step that the unrenormalized family in `ANF-044` could not use to retain a positive margin as `y->0`.

## 2. The positive block has a uniform quadratic lower bound

From `ANF-045`,

\[
P(y_1,y_2;d)
=2\int J(\alpha)(a_{y_1}(\alpha)+a_{y_2}(\alpha))
\bigl(1+\cos(2\pi\alpha d)\bigr)\,d\alpha.
\tag{10}
\]

The elementary inequality `cosh x-1>=x^2/2` gives

\[
a_y(\alpha)\ge2\pi^2\alpha^2y^2.
\tag{11}
\]

Define

\[
M_J(d)
:=\int J(\alpha)\alpha^2
\bigl(1+\cos(2\pi\alpha d)\bigr)\,d\alpha.
\tag{12}
\]

For every finite real `d`, one has `M_J(d)>0`. Indeed the integrand is nonnegative; a nonzero continuous `J>=0` is positive on an interval containing nonzero frequencies; and `1+cos(2 pi alpha d)` cannot vanish on an interval. Since `M_J` is continuous,

\[
\boxed{
m_{J,D}:=\min_{|d|\le D}M_J(d)>0.}
\tag{13}
\]

Putting

\[
S:=y_1^2+y_2^2,
\tag{14}
\]

(10)--(13) give the scale-matched lower bound

\[
\boxed{
P(y_1,y_2;d)
\ge4\pi^2m_{J,D}S
\qquad(|d|\le D).
}
\tag{15}
\]

Unlike the interior-slab margin of `ANF-044`, this lower bound loses exactly the same quadratic height factor as the anchor oscillation and therefore remains useful all the way to `S=0`.

## 3. The common-translation term has the same scale and decays uniformly

The exact Fourier term of `ANF-045` is

\[
Z_{y_1,y_2,d}(t)
=\int J(\alpha)e^{2\pi i\alpha t}
\left(a_{y_1}(\alpha)e^{2\pi i\alpha d}+a_{y_2}(\alpha)\right)d\alpha.
\tag{16}
\]

Using `a_y=y^2r_y` gives the exact decomposition

\[
\boxed{
Z_{y_1,y_2,d}(t)
=y_1^2R_{y_1}(t+d)+y_2^2R_{y_2}(t).
}
\tag{17}
\]

Fix `Y,D`. By (9), for every `eta>0` there is `T_0` such that

\[
|R_y(s)|<\eta
\qquad
(0\le y\le Y,\ |s|\ge T_0).
\tag{18}
\]

If `|t|>=T_0+D`, then both `|t|>=T_0` and `|t+d|>=T_0` for every `|d|<=D`. Therefore (17) gives

\[
\boxed{
|Z_{y_1,y_2,d}(t)|
\le\eta S.
}
\tag{19}
\]

Choose `eta=2 pi^2 m_{J,D}` and set `T=T_0+D`. Since `Q>=0`, equations (1), (15), and (19) imply

\[
\begin{aligned}
H_J(y_1,y_2;t+d,t)
&\ge P-|Z|\\
&\ge
\bigl(4\pi^2m_{J,D}-2\pi^2m_{J,D}\bigr)S\\
&=2\pi^2m_{J,D}S.
\end{aligned}
\tag{20}
\]

Thus (2) holds with the explicit structural margin

\[
\boxed{c=2\pi^2m_{J,D}>0,}
\tag{21}
\]

while only the location of the cutoff `T` remains qualitative. At `S=0` the bound reads `H_J>=0`; for every genuine configuration `S>0`, so the tail is strictly positive.

## 4. Consequence for the Montgomery--Taylor residual box

`ANF-060` proves that every genuine Montgomery--Taylor zero or negative defect satisfies

\[
0.545<|d|<1.01,
\qquad
q:=\frac{|y_1-y_2|}{y_1+y_2}>0.1409,
\qquad
y_1+y_2<1.500355.
\tag{22}
\]

In particular each height is below `1.500355`. Apply (2) with

\[
J=J_{\rm MT},
\qquad
Y=1.500355,
\qquad
D=1.01.
\tag{23}
\]

There is a finite `T_MT` such that `|t_2|>=T_MT` forces `H_MT>0` for every shape satisfying the larger bounded box in (23). Hence every zero or negative value obeys (3). The common translation can no longer run to infinity while the heights approach the real axis, which is exactly the escape not covered uniformly by the interior-height version of `ANF-044`.

Equivalently, using the mean-height parameterization of `ANF-060`, every genuine residual zero lies in the finite closure

\[
0\le y\le0.7501775,
\qquad
0.1409\le q\le1,
\qquad
0.545\le|d|\le1.01,
\qquad
|t|\le T_{\rm MT},
\tag{24}
\]

with strict interior conditions imposed for a genuine two-pair configuration and with the `y=0`, `q=1`, and separation faces handled by the already-canonical boundary arguments. Equation (24) is an enclosure for certification, not a claim that its artificial boundary points are genuine zeros.

## 5. Prior art, stress tests, and next certificate

The analytic ingredients are classical: `cosh x-1>=x^2/2` and uniform Riemann--Lebesgue decay for a compact `L^1` family. The latter was already proved locally in `ANF-044`; the new content is to renormalize the exact five-point anchor family by `y^2` and match it against the positive `P` block, so the horizontal margin survives the zero-height limit. A targeted check of current pair-correlation finite-compression and bandlimited-kernel literature found the expected Fourier-decay machinery but no external theorem that supplies this height-renormalized two-pair five-point compactification. No publication-level novelty claim is made, and no new external result is load-bearing, so `SOURCES.md` is unchanged.

The main stress tests are the two degenerations that defeated a naive compactness argument. If one height tends to zero, its coefficient in (17) vanishes while the other remains controlled by the same compact family. If both heights tend to zero at any relative rate, division by `S` leaves convex weights multiplying the uniformly decaying `R_y`, while (15) retains a fixed positive coefficient. The proof therefore does not hide a lower height cutoff. Bounded `d` is essential to this particular common-translation statement because it makes `t` and `t+d` escape together; large relative separation is a different regime already treated in `ANF-044` and is irrelevant after the much stronger `ANF-059` separation window.

This finding does **not** decide Montgomery--Taylor five-point zero-freeness, does not provide a numerical value for `T_MT`, does not certify the central-notch perturbation, and does not address larger conjugation-invariant multisets. Its durable contribution is topological and quantitative at the natural boundary scale: after `ANF-060`, the accepted base-zero problem has no remaining noncompact geometric direction. The next decisive step can therefore be a validated certificate on one finite four-parameter enclosure, with a separate quantitative Fourier-tail calculation needed only if an explicit numerical `T_MT` is desired.