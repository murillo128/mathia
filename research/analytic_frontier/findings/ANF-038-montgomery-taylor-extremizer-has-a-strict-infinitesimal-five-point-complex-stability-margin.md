# ANF-038 — the Montgomery--Taylor extremizer has a strict infinitesimal five-point complex stability margin

**Status:** `EXACT-DERIVED + RIGOROUS-INTERVAL-CERTIFICATE + FIVE-POINT-COMPLEX-STABILITY + STRUCTURAL-BOUNDARY`. `ANF-037` reduces the first genuinely complex one-pair-plus-three-real five-point layer to the scalar Fourier--Laplace defect

\[
G_J(y)=A_y+3\inf_{t\in\mathbb R}L_y(t),
\]

and proves the small-height limit

\[
\frac{G_J(y)}{2\pi^2y^2}
\longrightarrow
m_5(J):=2K_J(0)+3\inf_{t\in\mathbb R}K_J(t),
\qquad
K_J(t)=\int_{-1}^{1}\alpha^2J(\alpha)\cos(2\pi\alpha t)\,d\alpha.
\tag{1}
\]

For the exact Montgomery--Taylor spectrum `J_MT` of `ANF-030`, the sign left open in `ANF-037` is strictly positive. In fact

\[
\boxed{
K_{\rm MT}(t)+\frac23K_{\rm MT}(0)>0.0026
\qquad(t\in\mathbb R),
}
\tag{2}
\]

and therefore

\[
\boxed{
m_5(J_{\rm MT})>0.0078.}
\tag{3}
\]

Consequently the sharp Montgomery--Taylor profile is **strictly stable against infinitesimal five-point complex splitting** of the first nontrivial geometry from `ANF-036`--`ANF-037`.

More importantly for the explicit finite-real separator of `ANF-034`, the central-notch ray

\[
J_s=J_{\rm MT}-s\phi_\eta
\]

can be chosen so that it simultaneously keeps its strict finite-real gain and satisfies `m_5(J_s)>0`. Thus a five-point obstruction to that ray, if one exists, cannot be forced merely by taking the conjugate height `y->0`; it must occur at a genuinely finite height or in another complex geometry.

## 1. Exact Montgomery--Taylor spectrum and the curvature measure

Put

\[
a:=\sqrt2,
\qquad
\theta:=\frac1{\sqrt2},
\qquad
c_*:=\frac1{4\sin^2\theta}.
\]

`ANF-030` writes `J_MT=g*g` with

\[
g(u)=\frac{\cos(au)}{\sqrt2\sin\theta}\,
\mathbf 1_{[-1/2,1/2]}(u).
\]

Evaluating the convolution gives, for `0<=alpha<=1`,

\[
\boxed{
J_{\rm MT}(\alpha)
=c_*\left[
\frac{\sin(a(1-\alpha))}{a}
+(1-\alpha)\cos(a\alpha)
\right],
}
\tag{4}
\]

with even extension to `[-1,1]` and zero outside.

Let

\[
w(\alpha):=\alpha^2J_{\rm MT}(\alpha),
\qquad
W_k:=\int_{-1}^{1}|\alpha|^k w(\alpha)\,d\alpha
\quad(0\le k\le4).
\tag{5}
\]

Then `K_MT(t)` is the cosine transform of the nonnegative even density `w`, and `K_MT(0)=W_0`. Elementary integration of (4), using the recurrences for `\int_0^1 alpha^n cos(a alpha)dalpha` and `\int_0^1 alpha^n sin(a alpha)dalpha`, gives the exact moments below. Write

\[
d:=1-\cos a>0.
\]

Then

\[
\begin{aligned}
W_0&=\frac{2a\sin a+3\cos a-3}{2d},\\
W_1&=\frac{16\cos a+2-3a\sin a}{4d},\\
W_2&=\frac{31-19\cos a-20a\sin a}{2d},\\
W_3&=\frac{20a\sin a-9-121\cos a}{2d},\\
W_4&=\frac{213a\sin a+157\cos a-322}{d}.
\end{aligned}
\tag{6}
\]

In particular a direct interval evaluation of these exact expressions gives

\[
0.1549985926411760<W_0<0.1549985926411777.
\tag{7}
\]

The rest of the proof is a global lower bound for the characteristic cosine transform of `w` relative to the threshold `-2W_0/3`.

## 2. Compact-frequency certificate on `|t|<=1`

For every real `x`,

\[
\boxed{
\cos x
\ge
q(x):=-1+\frac{(x-\pi)^2}{2}-\frac{(x-\pi)^4}{24}.
}
\tag{8}
\]

Indeed, with `delta=x-pi`, the desired inequality is equivalent to

\[
\cos\delta
\le
1-\frac{\delta^2}{2}+\frac{\delta^4}{24}.
\]

For `|delta|<=sqrt(12)` this is the alternating Taylor upper bound, since from the sixth-order term onward the term magnitudes decrease. For `|delta|>=sqrt(12)`, the quartic polynomial on the right is at least `1`, hence again dominates `cos delta`.

Because `w` is even, applying (8) to `x=2pi t alpha` on `alpha in [0,1]` yields

\[
K_{\rm MT}(t)+\frac23W_0
\ge H(t),
\qquad 0\le t\le1,
\tag{9}
\]

where the degree-four polynomial `H` is determined exactly by (6):

\[
H(t)
=
\frac23W_0
+\sum_{k=0}^4 q_k(2\pi t)^kW_k,
\tag{10}
\]

with

\[
(q_0,q_1,q_2,q_3,q_4)
=
\left(
-1+\frac{\pi^2}{2}-\frac{\pi^4}{24},
-\pi+\frac{\pi^3}{6},
\frac12-\frac{\pi^2}{4},
\frac\pi6,
-\frac1{24}
\right).
\tag{11}
\]

The sign of this quartic can be certified without sampling. Rewrite it in the degree-four Bernstein basis separately on

\[
[0,3/5],\qquad [3/5,9/10],\qquad [9/10,1].
\]

Using outward-rounded rational interval arithmetic on the exact formulas (6), the Bernstein coefficients have the following strict lower bounds, in increasing Bernstein index:

\[
\begin{array}{c|ccccc}
[0,3/5]&0.0841&0.2562&0.1555&0.0689&0.0298\\
[3/5,9/10]&0.0298&0.0103&0.00265&0.0110&0.0238\\
[9/10,1]&0.0238&0.0281&0.0328&0.0377&0.0419
\end{array}
\tag{12}
\]

Every Bernstein basis function is nonnegative and the basis sums to one, so (12) proves

\[
\boxed{H(t)>0.00265\qquad(0\le t\le1).}
\tag{13}
\]

For reproducibility, one sufficient set of outward enclosures used in (12) is

\[
\begin{aligned}
1.41421356237&<\sqrt2<1.41421356238,\\
3.14159265358&<\pi<3.14159265360,\\
0.98776594599&<\sin\sqrt2<0.98776594600,\\
0.15594369476&<\cos\sqrt2<0.15594369477.
\end{aligned}
\tag{14}
\]

The square-root bounds are checked by squaring; the trigonometric bounds follow from the alternating Taylor series with interval input, and the displayed `pi` enclosure may be certified independently, for example by a standard Machin-formula arctangent enclosure. Substitution into (6), (10), followed by the exact power-to-Bernstein basis conversion gives (12). Thus the certificate is a finite rational inequality check, not a numerical minimum search.

## 3. Large-frequency tail from unimodality

It remains to control `|t|>=1`. Formula (4) makes the total variation of `w` elementary.

Differentiate (4):

\[
J_{\rm MT}'(\alpha)
=-c_*\left[
\cos(a(1-\alpha))
+\cos(a\alpha)
+a(1-\alpha)\sin(a\alpha)
\right],
\tag{15}
\]

so `J_MT` is strictly decreasing on `(0,1)`. Put

\[
h(\alpha):=2J_{\rm MT}(\alpha)+\alpha J_{\rm MT}'(\alpha),
\qquad
w'(\alpha)=\alpha h(\alpha).
\tag{16}
\]

A second differentiation gives

\[
\begin{aligned}
\frac{h'(\alpha)}{c_*}
={}&-2\alpha(1-\alpha)\cos(a\alpha)
+a(5\alpha-3)\sin(a\alpha)\\
&-a\alpha\sin(a(1-\alpha))
-3\cos(a\alpha)-3\cos(a(1-\alpha)).
\end{aligned}
\tag{17}
\]

This is strictly negative throughout `[0,1]`. For `alpha<=3/5`, every displayed term is nonpositive and the cosine terms are strictly negative. For `alpha>=3/5`, the only potentially positive term satisfies

\[
a(5\alpha-3)\sin(a\alpha)<2\sqrt2<3,
\]

whereas

\[
3\bigl(\cos(a\alpha)+\cos(a(1-\alpha))\bigr)
\ge3(1+\cos a)>3;
\]

the remaining terms are nonpositive. Hence `h` is strictly decreasing. Since

\[
h(0)>0,
\qquad
h(1)=J_{\rm MT}'(1)<0,
\]

`w` has exactly one maximum on `(0,1)`.

The same rational interval arithmetic used above gives

\[
h(78/125)>0.00253,
\qquad
h(5/8)<-0.00049,
\tag{18}
\]

so the maximizing point lies in `(78/125,5/8)`. Because `J_MT` decreases,

\[
\max_{0\le\alpha\le1}w(\alpha)
<\left(\frac58\right)^2J_{\rm MT}(78/125)
<0.14.
\tag{19}
\]

Therefore the total variation of the even density `w` on `[-1,1]` is strictly less than `4(0.14)=0.56`. Integration by parts, using `w(+-1)=0`, gives for `t ne 0`

\[
|K_{\rm MT}(t)|
\le
\frac{\operatorname{TV}(w)}{2\pi|t|}.
\tag{20}
\]

Thus for `|t|>=1`,

\[
K_{\rm MT}(t)>-\frac{0.56}{2\pi}>-0.09.
\tag{21}
\]

On the other hand (7) gives

\[
\frac23K_{\rm MT}(0)=\frac23W_0>0.1026.
\tag{22}
\]

Consequently

\[
\boxed{
K_{\rm MT}(t)+\frac23K_{\rm MT}(0)>0.0126
\qquad(|t|\ge1).
}
\tag{23}
\]

Combining (13) and (23), and using evenness in `t`, proves (2).

## 4. The infinitesimal five-point gate is strictly open

From (2),

\[
\begin{aligned}
m_5(J_{\rm MT})
&=2K_{\rm MT}(0)+3\inf_tK_{\rm MT}(t)\\
&=3\inf_t\left(K_{\rm MT}(t)+\frac23K_{\rm MT}(0)\right)\\
&>3(0.0026)=0.0078,
\end{aligned}
\tag{24}
\]

which proves (3).

Equation (1), with the uniform small-height expansion from `ANF-037`, now implies that there exists `y_0>0` such that

\[
\boxed{
G_{J_{\rm MT}}(y)>0
\qquad(0<y<y_0).
}
\tag{25}
\]

Thus the first five-point complex geometry cannot destabilize the exact Montgomery--Taylor spectrum at infinitesimal height.

The same conclusion survives a sufficiently small central notch. `ANF-037` proves

\[
m_5(J_s)
\ge
m_5(J_{\rm MT})
-\frac56s b_\eta\eta^3,
\tag{26}
\]

and `ANF-034` has `0<b_eta<=1` while allowing `s>0` to be chosen arbitrarily small after the admissible notch width `eta` is fixed. For example, imposing in addition

\[
s\eta^3<0.009
\tag{27}
\]

gives from (24)--(26)

\[
m_5(J_s)>0.0078-0.0075>0.
\tag{28}
\]

Therefore the separator construction of `ANF-034` can be made to satisfy **both**

\[
\frac{C(J_s)}{q_{\rm real}(J_s)}<C_{\rm MT}
\]

and the strict infinitesimal five-point complex gate `m_5(J_s)>0`. By `ANF-037`, such a chosen separator has its own `y_0(s,eta)>0` with

\[
G_{J_s}(y)>0
\qquad(0<y<y_0(s,\eta)).
\tag{29}
\]

This removes a natural failure mode: the real separator does not automatically collapse as soon as a conjugate pair leaves the real axis.

## 5. Prior-art and evidence boundary

The external ingredients remain exactly those already anchored in `SOURCES.md`: Carneiro--Chandee--Littmann--Milinovich supply the sharp Montgomery--Taylor extremizer used in `ANF-030`, while the positive Fourier--Laplace representation used to formulate the complex energy is classical and already anchored through Buescu--Paixão--Symeonides. A targeted search of those extremal-function and complex positive-definite literatures found the expected general representation and pair-correlation extremal theory but no matching statement for the five-point curvature threshold (24). No publication-level novelty claim is made.

The new content is the specialization of the exact `J_MT` profile to the `ANF-037` curvature gate and the rigorous global bound (2). The only computer-assisted component is finite outward-rounded interval arithmetic for elementary constants in (12), (18), and (19); the inequalities reduce to explicit rational interval calculations over closed formulas and do not rely on sampled optimization or floating-point evidence. The structural steps -- the global cosine minorant, Bernstein positivity criterion, unimodality, total-variation estimate, and Fourier tail bound -- are exact.

This finding does **not** prove `G_{J_s}(y)>=0` at all finite heights, does not prove that the central-notch ray satisfies the full universal affine inequality, and does not cover every five-point conjugation-invariant geometry. It clears only the infinitesimal one-conjugate-pair-plus-three-real layer that is the first sharp complex instability identified by `ANF-036`--`ANF-037`.

## 6. Next decisive test

The remaining first-layer question is now separated away from the singular endpoint `y=0`. For a concrete notch satisfying the finite-real construction of `ANF-034` and the small-height condition (27), the next decisive quantity is

\[
\boxed{
\inf_{y\ge y_0}
G_{J_s}(y)
=
\inf_{y\ge y_0}\left[
\frac{F_s(2iy)-F_s(0)}2
+3\inf_{t\in\mathbb R}
\bigl(\Re F_s(t+iy)-F_s(t)\bigr)
\right].
}
\tag{30}
\]

A certified negative value would exhibit a genuine finite-height five-point complex reversal and quantify the extra affine cost. A proof of nonnegativity for all heights would clear the complete one-pair-plus-three-real five-point layer for that separator and force the first obstruction into a different five-point fiber pattern or a larger coupled complex configuration.