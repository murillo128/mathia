# ANF-045 — two-pair five-point obstruction scalarizes to a strict Hilbert coherence gap

**Status:** `EXACT-DERIVED + HILBERT-COHERENCE-REDUCTION + GLOBAL-SAFETY-BARRIER + COMPACT-COHERENCE-GAP + STRUCTURAL-BOUNDARY`. `ANF-042` shows that the last irreducible cardinality-five geometry can be pointwise negative at individual nonzero frequencies and identifies cross-frequency phase coherence as the remaining issue. `ANF-043`--`ANF-044` then compactify every possible negative defect once the curvature gate `m_5(J)>=0`, but leave a four-variable finite-domain sign problem. The present finding isolates the missing coherence exactly. For fixed heights and relative horizontal separation, optimizing the remaining common translation is equivalent to one normalized Hilbert-space correlation coefficient. Cauchy--Schwarz gives a global safety barrier, equality is impossible for every genuine two-pair shape, and the failure of equality is **uniform on compact shape boxes**. Thus the residual five-point obstruction is no longer an arbitrary four-dimensional oscillatory minimization: it is a compact three-dimensional shape problem plus one scalar coherence statistic with a strict gap from perfect alignment.

Let

\[
F(z)=\widehat J(z)
=\int_{-B}^{B}J(\alpha)e^{-2\pi i\alpha z}\,d\alpha,
\qquad
J\ge0,
\tag{1}
\]

where `J` is nonzero, continuous, even, and compactly supported, and put

\[
F_0:=F(0)=\int J(\alpha)\,d\alpha>0.
\tag{2}
\]

Retain the two-pair configuration of `ANF-040`--`ANF-044`,

\[
W=\{x_1\pm iy_1,x_2\pm iy_2,r\},
\qquad
y_1,y_2>0,
\tag{3}
\]

with

\[
t_j=x_j-r,
\qquad
d=t_1-t_2,
\qquad
c_j(\alpha)=\cosh(2\pi\alpha y_j).
\tag{4}
\]

Writing

\[
a(\alpha):=c_1(\alpha)-1,
\qquad
b(\alpha):=c_2(\alpha)-1,
\tag{5}
\]

`ANF-042` gives

\[
H_J(y_1,y_2;t_1,t_2)=\int J(\alpha)h_\alpha\,d\alpha,
\tag{6}
\]

where

\[
\begin{aligned}
h_\alpha={}&(c_1^2-1)+(c_2^2-1)
+2(c_1c_2-1)\cos(2\pi\alpha d)\\
&+a\cos(2\pi\alpha t_1)
+b\cos(2\pi\alpha t_2).
\end{aligned}
\tag{7}
\]

The energy difference from the real-part collapse is `4H_J`.

## 1. The exact integrand has a Hilbert normal form

Set

\[
\theta_j=2\pi\alpha t_j,
\qquad
V_\alpha:=ae^{i\theta_1}+be^{i\theta_2}.
\tag{8}
\]

Expanding `|V_alpha|^2`, and using `c_1c_2-1=a+b+ab`, gives the exact identity

\[
\boxed{
h_\alpha
=|V_\alpha|^2+\operatorname{Re}V_\alpha
+2(a+b)\bigl(1+\cos(2\pi\alpha d)\bigr).
}
\tag{9}
\]

This rearrangement keeps the physical linkage between phases at different frequencies that is deliberately discarded by the pointwise minimization in `ANF-042`.

For fixed shape `(y_1,y_2,d)`, write `t_2=t` and `t_1=t+d`, and define

\[
u_d(\alpha)
:=a(\alpha)e^{2\pi i\alpha d}+b(\alpha).
\tag{10}
\]

Then introduce the two nonnegative shape functionals

\[
\boxed{
Q(y_1,y_2;d)
:=\int J(\alpha)|u_d(\alpha)|^2\,d\alpha
}
\tag{11}
\]

and

\[
\boxed{
P(y_1,y_2;d)
:=2\int J(\alpha)(a(\alpha)+b(\alpha))
\bigl(1+\cos(2\pi\alpha d)\bigr)\,d\alpha\ge0.
}
\tag{12}
\]

Finally let

\[
Z_{y_1,y_2,d}(t)
:=\int J(\alpha)e^{2\pi i\alpha t}u_d(\alpha)\,d\alpha.
\tag{13}
\]

Evenness makes `Z(t)` real, although keeping `Re Z` below makes the Hilbert structure transparent. Integrating (9) gives

\[
\boxed{
H_J(y_1,y_2;t+d,t)
=Q(y_1,y_2;d)+P(y_1,y_2;d)
+\operatorname{Re}Z_{y_1,y_2,d}(t).
}
\tag{14}
\]

In particular `Q+P` is exactly the positive residual two-pair block `B_J(y_1,y_2;d)` isolated in `ANF-044`; the only possible source of descent is its correlation with the common translation character.

## 2. Common translation reduces to one coherence coefficient

For every genuine shape `y_1,y_2>0`, one has

\[
\boxed{Q(y_1,y_2;d)>0.}
\tag{15}
\]

Indeed, if `Q=0`, then `u_d(alpha)=0` on an open interval where `J>0`. The function `u_d` is entire in `alpha`, so the identity theorem would force `u_d` to vanish identically. But near zero,

\[
u_d(\alpha)
=2\pi^2(y_1^2+y_2^2)\alpha^2+O(\alpha^3),
\tag{16}
\]

which is nonzero for small nonzero `alpha` because both heights are positive.

Define the dimensionless shape variables

\[
x:=\sqrt{\frac{Q}{F_0}}>0,
\qquad
p:=\frac{P}{F_0}\ge0,
\tag{17}
\]

and the maximal negative character coherence

\[
\boxed{
\kappa_*(y_1,y_2,d)
:=
\frac{\sup_{t\in\mathbb R}\bigl(-\operatorname{Re}Z_{y_1,y_2,d}(t)\bigr)}
{\sqrt{F_0Q}}.
}
\tag{18}
\]

Since `Z(t)->0` by Riemann--Lebesgue, the numerator is nonnegative. Cauchy--Schwarz in `L^2(J(alpha)dalpha)` gives

\[
|Z(t)|
\le
\left(\int J\right)^{1/2}
\left(\int J|u_d|^2\right)^{1/2}
=\sqrt{F_0Q},
\tag{19}
\]

so

\[
0\le\kappa_*\le1.
\tag{20}
\]

More importantly, (18) is not merely a bound: it exactly performs the common-translation minimization in (14). Therefore

\[
\boxed{
\inf_{t\in\mathbb R}
H_J(y_1,y_2;t+d,t)
=F_0\bigl(x^2-\kappa_*x+p\bigr).
}
\tag{21}
\]

Consequently a fixed shape admits a negative defect for some common translation **if and only if**

\[
\boxed{
\kappa_*>x+\frac{p}{x}.
}
\tag{22}
\]

This is the exact scalar form of the cross-frequency coherence question left by `ANF-042`.

## 3. Cauchy gives a global shape-safety barrier

Dropping only the strictness of the coherence and using `kappa_*<=1` in (21) yields, for every geometry,

\[
\boxed{
H_J
\ge Q-\sqrt{F_0Q}+P
=F_0\left[\left(x-\frac12\right)^2+p-\frac14\right].
}
\tag{23}
\]

Several immediate global filters follow. If

\[
P\ge\frac{F_0}{4},
\tag{24}
\]

then the shape is safe for every common translation. Likewise, if

\[
Q\ge F_0,
\tag{25}
\]

then `Q-sqrt(F_0Q)>=0`, so the shape is again safe.

If a negative defect exists, necessarily `p<1/4`; putting

\[
r_\pm(p)
:=\frac{1\pm\sqrt{1-4p}}{2},
\tag{26}
\]

one must have

\[
\boxed{
r_-(p)<x<r_+(p).}
\tag{27}
\]

Equivalently,

\[
F_0r_-(p)^2<Q<F_0r_+(p)^2.
\tag{28}
\]

Thus even before exploiting strict coherence, a negative five-point shape must place its quadratic displacement energy in a bounded Cauchy window and must keep the positive residual term `P` below one quarter of a self-energy.

## 4. Perfect cross-frequency coherence is impossible

The weak inequality `kappa_*<=1` has a strict geometric improvement for every fixed genuine shape:

\[
\boxed{
\kappa_*(y_1,y_2,d)<1
\qquad(y_1,y_2>0,\ d\in\mathbb R).
}
\tag{29}
\]

If `kappa_*=1`, then because `sqrt(F_0Q)>0` and `Z(t)->0`, the supremum in (18) is attained at some finite `t_*`. Equality in (19), together with `-Re Z(t_*)=sqrt(F_0Q)`, forces equality in Cauchy--Schwarz with negative real phase. Hence

\[
e^{2\pi i\alpha t_*}u_d(\alpha)
\]

must equal one fixed negative real constant for `J(alpha)dalpha`-almost every `alpha`. Since `J` is continuous and nonzero, it is positive on an open interval. The left side is entire in `alpha`, so equality on that interval forces equality identically. At `alpha=0`, however, `a(0)=b(0)=0`, and hence the left side vanishes. The constant would therefore have to be zero, contradicting `Q>0`.

The obstruction is structural: Cauchy saturation would require the hyperbolic two-pair amplitude to be exactly one Fourier character across a continuum of frequencies. Its forced double zero at the central frequency prevents that alignment.

## 5. The coherence gap is uniform on compact shape boxes

The strict inequality (29) becomes uniform once the shape variables are confined to a compact interior set. Fix

\[
\mathcal S_{\varepsilon,Y,D}
=[\varepsilon,Y]^2\times[-D,D],
\qquad 0<\varepsilon\le Y<\infty,
\quad D<\infty.
\tag{30}
\]

Then there exists

\[
\boxed{
\delta_{J,\varepsilon,Y,D}>0
}
\tag{31}
\]

such that

\[
\boxed{
\sup_{(y_1,y_2,d)\in\mathcal S_{\varepsilon,Y,D}}
\kappa_*(y_1,y_2,d)
\le1-\delta_{J,\varepsilon,Y,D}.
}
\tag{32}
\]

To prove this, first note that `Q` is continuous and strictly positive by (15), so compactness gives a uniform lower bound `Q>=q_*>0` on the shape box. The family

\[
J(\alpha)u_d(\alpha)
\tag{33}
\]

is continuous in the shape parameters as a compact family in `L^1`, because the spectral support and all heights and separations are bounded. The same finite-net argument used in `ANF-044` therefore gives uniform Riemann--Lebesgue decay:

\[
\sup_{(y_1,y_2,d)\in\mathcal S_{\varepsilon,Y,D}}
|Z_{y_1,y_2,d}(t)|\longrightarrow0
\qquad(|t|\to\infty).
\tag{34}
\]

If (32) failed, there would be shapes `s_n` and translations `t_n` with normalized negative correlation tending to one. The lower bound on `Q` and (34) prevent `|t_n|` from tending to infinity. Passing to a subsequence gives `s_n->s_*` and `t_n->t_*`; continuity then yields exact Cauchy saturation for the limiting genuine shape, contradicting (29). This proves (32).

Combining (21) and (32), every shape in the box satisfies the stronger uniform bound

\[
\boxed{
\inf_t H_J
\ge
F_0\left[x^2-(1-\delta)x+p\right],
\qquad
\delta=\delta_{J,\varepsilon,Y,D}>0.
}
\tag{35}
\]

Hence a negative shape in such a box must obey

\[
x+\frac{p}{x}<1-\delta,
\tag{36}
\]

and in particular, by AM--GM,

\[
\boxed{
p<\frac{(1-\delta)^2}{4}.}
\tag{37}
\]

The universal quarter-self-energy danger budget from `ANF-042` is therefore never approached by a compact family of genuine physical two-pair shapes: some coherence is uniformly lost.

## 6. Consequence after `ANF-044` compactification

Assume the curvature gate

\[
m_5(J)\ge0.
\tag{38}
\]

`ANF-044` gives constants `epsilon_J,Y_J,T_J` such that every negative defect satisfies

\[
\varepsilon_J\le y_1,y_2\le Y_J,
\qquad
|t_1|,|t_2|\le T_J.
\tag{39}
\]

Therefore every negative candidate has

\[
|d|=|t_1-t_2|\le2T_J
\tag{40}
\]

and lies in the compact shape box

\[
[\varepsilon_J,Y_J]^2\times[-2T_J,2T_J].
\tag{41}
\]

Applying Section 5 gives a single constant `delta_J>0` valid for **every remaining negative candidate**. Thus the complete unresolved cardinality-five problem can be written as the compact scalar inequality

\[
\boxed{
\kappa_*(y_1,y_2,d)
\le x(y_1,y_2,d)+\frac{p(y_1,y_2,d)}{x(y_1,y_2,d)}
}
\tag{42}
\]

on the compact shape box, with `kappa_*<=1-delta_J` already known independently of the detailed spectrum.

This is a genuine reduction in the remaining certification burden. The common horizontal translation need not be treated as a fourth nonlinear geometry variable: its entire effect is the Fourier-character coherence (18). A rigorous interval or analytic closure can separately bound the smooth shape functionals `Q,P` and the one-dimensional Fourier supremum defining `kappa_*`. Conversely, any counterexample must exhibit a compact shape whose character coherence exceeds the explicit threshold in (42); pointwise negative frequencies alone are insufficient.

For the central-notch separators `J_s` of `ANF-034` chosen with the positive curvature margin of `ANF-038`, all hypotheses above hold. The finding does **not** prove that their two-pair five-point defect is nonnegative, but it identifies exactly what a remaining finite-height falsifier must accomplish and rules out arbitrarily close Cauchy saturation across the compact obstruction family.

## 7. Prior art, audit boundary, and next test

The Hilbert inequality used in (19) is ordinary Cauchy--Schwarz, and the compact-family Fourier decay in Section 5 is the same elementary uniform Riemann--Lebesgue argument already proved in `ANF-044`. The positive Fourier--Laplace framework is already anchored in `SOURCES.md` through Buescu--Paixão--Symeonides. A targeted check of the positive-definite strip and pair-correlation Hilbert-space literature found the expected general frameworks but no external theorem is needed for the finite-configuration identities (9), (14), or (21). No publication-level novelty claim is made, and no new source entry is required.

The proof is exact and has no numerical component. Its quickest audit is algebraic: expand the right side of (9) and recover (7); integrate after writing `t_1=t+d`, `t_2=t` to obtain (14); then apply Cauchy--Schwarz once to get (23). The strictness argument can fail only if `u_d` is a character up to a constant on an interval, which its nonzero quadratic coefficient (16) excludes. Uniform strictness is then a compactness consequence of uniform Fourier decay.

The result does **not** prove the full five-point collapse inequality, does not close the universal affine certificate, and does not address larger conjugation-invariant multisets. It also does not claim an explicit numerical value for `delta_J`; (31) is qualitative. The next decisive test is therefore spectrum-specific: on the obstruction box supplied by `ANF-044`, certify (42) for the Montgomery--Taylor-compatible central notch, or find a genuine interior shape violating it. Either outcome now has a scalar cross-frequency witness rather than an unconstrained four-dimensional phase search.
