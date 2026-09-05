# ANF-043 — positive-spectrum two-pair five-point defect is height-coercive

**Status:** `EXACT-DERIVED + UNIFORM-HEIGHT-COERCIVITY + COMPACT-HEIGHT-OBSTRUCTION-REGION + STRUCTURAL-BOUNDARY`. `ANF-042` gives the exact pointwise normal form for the last unresolved cardinality-five geometry, two conjugate pairs plus one real point, and shows that individual frequencies can be harmful even though the descent is bounded below by one self-energy unit. The remaining issue is cross-frequency coherence. The present finding removes an entire asymptotic regime: for every nonzero continuous compactly supported spectrum `J>=0`, the integrated two-pair defect tends to `+infinity` **uniformly in both horizontal positions whenever either conjugate height tends to infinity**.

Let

\[
F(z)=\widehat J(z)
=\int_{-B}^{B}J(\alpha)e^{-2\pi i\alpha z}\,d\alpha,
\qquad J\ge0,
\tag{1}
\]

where `J` is nonzero, continuous and even. Retain the `ANF-040`/`ANF-042` configuration

\[
W=\{x_1\pm iy_1,x_2\pm iy_2,r\},
\qquad
R(W)=\{x_1,x_1,x_2,x_2,r\},
\qquad y_1,y_2>0,
\]

and put

\[
t_j=x_j-r,
\qquad d=t_1-t_2.
\]

Write

\[
E_F(W)-E_F(R(W))=4H_J(y_1,y_2;t_1,t_2).
\tag{2}
\]

Then

\[
\boxed{
\lim_{Y\to\infty}
\inf_{\substack{y_1,y_2>0\\ \max(y_1,y_2)\ge Y\\ t_1,t_2\in\mathbb R}}
H_J(y_1,y_2;t_1,t_2)
=+\infty.
}
\tag{3}
\]

Thus no finite-height reversal can escape by sending one or both conjugate pairs arbitrarily far from the real axis. Combined with the exact local criterion of `ANF-041`, this has a useful compactness consequence. If

\[
m_5(J)=2K_J(0)+3\inf_tK_J(t)\ge0,
\]

then there exist constants

\[
0<\varepsilon_J<Y_J<\infty
\]

such that every negative two-pair defect must satisfy

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)<0
\quad\Longrightarrow\quad
\varepsilon_J\le y_1,y_2\le Y_J.
}
\tag{4}
\]

The horizontal variables remain a genuine coherence problem and are not compactified here. Equation (4) only says that the projection of any five-point obstruction onto the two height coordinates lies in a compact interior rectangle.

## 1. A square-plus-linear decomposition of the exact pointwise defect

For fixed frequency put

\[
c_j=\cosh(2\pi\alpha y_j),
\qquad
u_j:=c_j-1\ge0,
\qquad
\theta_j:=2\pi\alpha t_j.
\tag{5}
\]

The `ANF-042` integrand is

\[
\begin{aligned}
h_\alpha={}&(c_1^2-1)+(c_2^2-1)
+2(c_1c_2-1)\cos(\theta_1-\theta_2)\\
&+(c_1-1)\cos\theta_1
+(c_2-1)\cos\theta_2.
\end{aligned}
\tag{6}
\]

Substituting `c_j=1+nu_j` and grouping quadratic terms gives the exact identity

\[
\begin{aligned}
h_\alpha
={}&\nu_1\bigl(2+2\cos(\theta_1-\theta_2)+\cos\theta_1\bigr)\\
&+\nu_2\bigl(2+2\cos(\theta_1-\theta_2)+\cos\theta_2\bigr)\\
&+\nu_1^2+\nu_2^2
+2\nu_1\nu_2\cos(\theta_1-\theta_2).
\end{aligned}
\tag{7}
\]

The last line is a squared modulus,

\[
\nu_1^2+\nu_2^2+2\nu_1\nu_2\cos(\theta_1-\theta_2)
=
\left|\nu_1e^{i\theta_1}+\nu_2e^{i\theta_2}\right|^2,
\tag{8}
\]

and also

\[
=(\nu_1-\nu_2)^2
+4\nu_1\nu_2\cos^2(\pi\alpha d).
\tag{9}
\]

Since

\[
2+2\cos(\theta_1-\theta_2)+\cos\theta_j\ge-1,
\]

equations (7)--(9) give the global lower bound

\[
\boxed{
h_\alpha
\ge
4\nu_1\nu_2\cos^2(\pi\alpha d)
-\nu_1-\nu_2.
}
\tag{10}
\]

This inequality is deliberately different from the universal `h_alpha>=-1/4` floor of `ANF-042`. It can be poor at moderate heights and anti-phase frequencies, but when the two hyperbolic amplitudes are both large its positive quadratic term grows exponentially faster than the linear losses unless the same physical separation `d` keeps `cos(pi alpha d)` tiny across an entire interval of frequencies. The next step shows that this cannot happen.

A second bound handles strongly unequal heights. Define

\[
q_\alpha:=|\nu_1-\nu_2|=|c_1-c_2|.
\tag{11}
\]

The exact `ANF-042` phase reduction writes the minimum over the mean horizontal phase as

\[
R^2-R+4pC^2,
\qquad R\ge q_\alpha,
\]

with nonnegative final term. Therefore, whenever `q_alpha>=1`, the monotonicity of `R^2-R` on `[1,\infty)` gives

\[
\boxed{
h_\alpha\ge q_\alpha^2-q_\alpha.}
\tag{12}
\]

Unlike (10), this bound does not depend on horizontal phases at all.

## 2. A frequency interval has a uniform anti-phase leakage

Let

\[
B_+:=\sup\{\alpha>0:J(\alpha)>0\}.
\]

Continuity, evenness and nontriviality imply `B_+>0`. By the definition of the support edge one may choose

\[
\frac{B_+}{2}<\beta<\gamma<B_+
\]

and a closed interval

\[
I=[\beta,\gamma]
\]

on which

\[
J(\alpha)\ge j_0>0.
\tag{13}
\]

The key coherence constant is

\[
c_I:=\inf_{d\in\mathbb R}
\int_\beta^\gamma\cos^2(\pi\alpha d)\,d\alpha.
\tag{14}
\]

It is strictly positive. For `d!=0`,

\[
\int_\beta^\gamma\cos^2(\pi\alpha d)\,d\alpha
=
\frac{\gamma-\beta}{2}
+
\frac{\sin(2\pi\gamma d)-\sin(2\pi\beta d)}{4\pi d},
\tag{15}
\]

so the integral tends to `(gamma-beta)/2` as `|d|->infinity`. Hence any minimizing sequence may be restricted to a compact set of `d`. A zero minimum at finite `d` would force the continuous nonnegative function `cos^2(pi alpha d)` to vanish identically on the interval `I`, which is impossible. Therefore

\[
\boxed{c_I>0.}
\tag{16}
\]

This elementary leakage statement is the cross-frequency ingredient absent from a pointwise analysis: one linear phase can hit anti-phase at isolated frequencies, but it cannot remain anti-phase throughout a positive-length interval.

## 3. Strongly unequal heights are uniformly safe at large height

Fix any `D>0` and suppose, without loss of generality,

\[
y_1\ge y_2,
\qquad y_1-y_2\ge D.
\]

For positive `alpha`, `ANF-042` gives exactly

\[
q_\alpha
=2\sinh\!\bigl(\pi\alpha(y_1+y_2)\bigr)
\sinh\!\bigl(\pi\alpha(y_1-y_2)\bigr).
\tag{17}
\]

If `y_1>=Y` and `alpha in I`, then

\[
q_\alpha
\ge
Q_Y
:=2\sinh(\pi\beta Y)\sinh(\pi\beta D).
\tag{18}
\]

For large enough `Y`, `Q_Y>=1`, so (12) applies throughout `I`. On the complementary frequencies use only the sharp universal floor `h_alpha>=-1/4` from `ANF-042`. Writing

\[
F(0)=\int J(\alpha)\,d\alpha,
\]

we obtain uniformly in `t_1,t_2`

\[
\boxed{
H_J
\ge
j_0|I|(Q_Y^2-Q_Y)-\frac{F(0)}4.
}
\tag{19}
\]

The right side tends to `+infinity` exponentially with `Y`. Thus a large-height configuration with a fixed positive height disparity is not merely eventually nonnegative: it acquires an arbitrarily large positive collapse margin independent of horizontal placement.

## 4. Nearly equal large heights are forced positive by interval coherence

It remains to treat

\[
|y_1-y_2|<D
\]

with `max(y_1,y_2)` large. Put

\[
y:=\max(y_1,y_2).
\]

Then

\[
y_1+y_2\ge2y-D.
\tag{20}
\]

For `x>=log 4`,

\[
\cosh x-1\ge\frac14e^x,
\qquad
\cosh x-1\le e^x.
\tag{21}
\]

Thus, once `y` is large enough that (21) applies to both heights throughout `I`, equation (10), (13), and the definition of `c_I` give

\[
\begin{aligned}
\int_I J(\alpha)h_\alpha\,d\alpha
&\ge
\frac{j_0c_I}{4}
 e^{2\pi\beta(y_1+y_2)}
-
2M_I e^{2\pi\gamma y},
\end{aligned}
\tag{22}
\]

where

\[
M_I:=\int_IJ(\alpha)\,d\alpha.
\]

Again use `h_alpha>=-1/4` outside `I`. From (20),

\[
\boxed{
H_J
\ge
\frac{j_0c_I}{4}
 e^{2\pi\beta(2y-D)}
-
2M_I e^{2\pi\gamma y}
-
\frac{F(0)}4.
}
\tag{23}
\]

The choice `beta>B_+/2` and `gamma<B_+` implies

\[
2\beta>\gamma.
\tag{24}
\]

Therefore the positive term in (23) grows like `e^(4 pi beta y)`, strictly faster than the linear-loss term `e^(2 pi gamma y)`. The lower bound tends to `+infinity` uniformly in `t_1,t_2`.

Sections 3 and 4 exhaust the height quadrant for the fixed split parameter `D`: either the heights differ by at least `D`, or they differ by less than `D`. This proves the uniform coercivity statement (3).

## 5. Nonnegative curvature confines every remaining reversal to interior heights

Assume now

\[
m_5(J)\ge0.
\tag{25}
\]

`ANF-041` proves that there is a punctured neighborhood of `(0,0)` in which every genuine two-pair split has strictly positive defect. Thus a negative sequence cannot approach the height origin.

The coordinate axes are also uniformly safe away from the origin. `ANF-040` gives

\[
H_J(y,0;t_1,t_2)\ge G_J(y),
\tag{26}
\]

where `G_J` is the one-pair-plus-three-real gate of `ANF-039`. The power-series proof in `ANF-039` actually yields, with

\[
M_4:=\int\alpha^4J(\alpha)\,d\alpha>0,
\]

the explicit strict bound

\[
\boxed{
G_J(y)
\ge
2\pi^2m_5(J)y^2
+
\frac5{24}(2\pi y)^4M_4
>0
\qquad(y>0).
}
\tag{27}
\]

Indeed the quartic coefficient in its exact series is `8+3 cos v>=5`, while every higher coefficient is nonnegative. Hence on any compact interval `y in [a,b] subset (0,infinity)`, the axis margin has a positive uniform lower bound.

For bounded `y_1`, the exact transforms in `ANF-040` converge uniformly in the horizontal variables as `y_2->0`, because the spectral support is compact and every oscillatory cosine has modulus at most one. Consequently a sufficiently thin strip adjacent to either axis inherits the positive margin from (26)--(27). Combining these axis strips with the punctured neighborhood from `ANF-041` and the large-height coercivity (3) proves (4).

Thus, once the already-known curvature gate is nonnegative, the last cardinality-five problem has no hidden asymptotic height regime. Any failure must occur with **both** conjugate pairs at genuinely finite, nonzero height.

## 6. Consequence for Montgomery--Taylor and the central-notch separator

`ANF-038` proves

\[
m_5(J_{\rm MT})>0.0078
\]

for the exact Montgomery--Taylor spectrum, and it constructs compatible central-notch separators `J_s` from `ANF-034` with

\[
m_5(J_s)>0.0003.
\]

Therefore both profiles satisfy the compact-height consequence (4). For the notch this is especially useful: its strict finite-real separation already survives every one-pair-plus-three-real five-point configuration at all heights by `ANF-039`, while `ANF-041` clears the two-pair geometry near the real axis. The present result additionally clears **all sufficiently large joint heights**, uniformly over horizontal placements.

Accordingly, a cardinality-five complex falsifier of the central-notch ray, if one exists, must live in an interior height box. `ANF-042` shows that individual frequencies inside that box can still be negative, so the branch is not closed. What remains is a bounded-height cross-frequency coherence problem rather than an asymptotic vertical-instability problem.

This distinction matters for the scalar program. A numerical or analytic search for a five-point reversal no longer needs to interpret apparent minima drifting toward height zero or infinity as separate escape mechanisms: the former is excluded by the curvature theorem, the latter by coercivity. The unresolved content lies between those two exact barriers.

## 7. Prior art, falsification, and evidence boundary

The external analytic framework remains the classical Fourier--Laplace representation for positive-definite strip functions already anchored in `SOURCES.md` through Buescu--Paixão--Symeonides. A targeted prior-art search around Fourier--Laplace strip positivity, hyperbolic amplification, and finite translation configurations found the expected representation theory but no theorem needed for the coercivity statement above. No publication-level novelty claim is made, and no new source entry is required: every load-bearing inequality is derived from the exact `ANF-042` integrand, compact spectral support, and elementary trigonometric/hyperbolic bounds.

The decisive audit has four finite targets. Expanding (7) must reproduce (6); its quadratic piece must equal the square (8)--(9); the interval leakage constant (14) must be strictly positive; and the two height regimes must have the claimed exponential separation, namely `Q_Y->infinity` in (18) and `2 beta>gamma` in (24). A counterexample to any of these steps invalidates the theorem immediately.

The assumptions matter. Spectral nonnegativity is essential for integrating lower bounds without cancellations; continuity and nontrivial compact support supply the positive interval `I`; compact support also gives the uniform axis-limit passage. The argument does not apply as stated to signed spectra or general exponentially finite noncompact measures.

Most importantly, (3)--(4) are **not** a global sign theorem. They do not prove `H_J>=0` at intermediate heights, do not compactify the horizontal variables, do not close the central-notch certificate, and say nothing about larger conjugation-invariant multisets. A genuine five-point reversal at bounded interior height would be fully compatible with this finding.

## 8. Next decisive gate

For any positive support-one spectrum with `m_5(J)>=0`, further five-point work can now restrict attention to bounded interior heights. The exact normal form of `ANF-042` should be integrated there using the fact that the same two linear horizontal phases control the entire frequency band. The two plausible outcomes are now sharply separated: either a coherent finite-height configuration accumulates enough negative spectral mass to defeat the real collapse, or a bounded-height Fourier inequality completes the all-height two-pair closure.

For the central-notch separator, the decisive target is therefore no longer an unrestricted four-parameter asymptotic search. The height variables are trapped between the local curvature barrier and the coercive large-height barrier; the remaining mathematical difficulty is horizontal cross-frequency coherence inside that finite-height window.