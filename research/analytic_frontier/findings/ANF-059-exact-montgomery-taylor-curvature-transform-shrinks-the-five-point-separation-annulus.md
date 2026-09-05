# ANF-059 — exact Montgomery--Taylor curvature transform shrinks the five-point separation annulus

**Status:** `EXACT-DERIVED + PROFILE-SPECIFIC-CURVATURE-TRANSFORM + OUTWARD-ROUNDED-CERTIFICATE + SHARPENED-SEPARATION-COMPACTIFICATION + STRUCTURAL-REDUCTION`. `ANF-058` reduces every possible genuine two-pair five-point zero for a spectrum passing the curvature gate to an actual negative lobe of its second-moment cosine transform:

\[
H_J(y_1,y_2;t_1,t_2)=0,\quad y_1,y_2>0
\quad\Longrightarrow\quad
K_J(d)<-\frac13K_J(0),
\qquad d=t_1-t_2.
\tag{1}
\]

For the fixed Montgomery--Taylor spectrum, `ANF-058` bounded those lobes only coarsely and obtained `0.42<|d|<7/4`. The exact Montgomery--Taylor factorization makes the one-dimensional curvature transform elementary. A finite outward-rounded mesh certificate, completed by a twice-integrated Fourier tail, sharpens the necessary separation window to

\[
\boxed{
H_{\rm MT}(y_1,y_2;t_1,t_2)=0,\quad y_1,y_2>0
\quad\Longrightarrow\quad
0.545<|t_1-t_2|<1.01.
}
\tag{2}
\]

The same strict window is necessary for a negative defect. Its width is `0.465`, compared with `1.33` for the previous annulus, so the remaining horizontal domain is reduced by about `65%` before either height or common-translation coherence is analyzed.

## 1. The Montgomery--Taylor curvature transform is an explicit second derivative

Retain the exact spectrum from `ANF-030` and `ANF-038`,

\[
J_{\rm MT}=g*g,
\qquad
g(u)=\frac{\cos(\sqrt2\,u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf 1_{[-1/2,1/2]}(u).
\tag{3}
\]

With the Fourier convention used throughout this line, put

\[
G(t):=\widehat g(t).
\tag{4}
\]

Direct integration of (3) gives

\[
\boxed{
G(t)=
\frac{\cos(\pi t)-\lambda t\sin(\pi t)}
{1-2\pi^2t^2},
\qquad
\lambda:=\sqrt2\,\pi\cot(1/\sqrt2).
}
\tag{5}
\]

The apparent singularities at `t=+-1/(sqrt(2)pi)` are removable because (5) is the Fourier transform of a compactly supported integrable function. They lie outside every interval used in the certificate below.

Since `J_MT=g*g`,

\[
F_{\rm MT}(t):=\widehat J_{\rm MT}(t)=G(t)^2.
\tag{6}
\]

The curvature transform of `ANF-038` and `ANF-058` is

\[
K_{\rm MT}(t)
=\int_{-1}^{1}\alpha^2J_{\rm MT}(\alpha)
\cos(2\pi\alpha t)\,d\alpha.
\tag{7}
\]

Differentiating the Fourier transform twice therefore gives the exact closed form

\[
\boxed{
K_{\rm MT}(t)
=-\frac{F_{\rm MT}''(t)}{4\pi^2}
=-\frac{G'(t)^2+G(t)G''(t)}{2\pi^2}.
}
\tag{8}
\]

Thus the one-dimensional gate left by `ANF-058` no longer requires numerical quadrature of the spectrum. It is a rational-trigonometric expression in `t`, `pi`, `sqrt(2)` and `cot(1/sqrt(2))` whose value on rational intervals can be enclosed directly.

For later comparison, `ANF-038` already certifies

\[
\boxed{
L_0:=0.1549985926411760<K_0:=K_{\rm MT}(0)
<0.1549985926411777.
}
\tag{9}
\]

## 2. A Lipschitz mesh clears `0.42<=|d|<=0.545` and `1.01<=|d|<=1.44`

Let

\[
w(\alpha):=\alpha^2J_{\rm MT}(\alpha).
\tag{10}
\]

Differentiating (7) under the integral gives

\[
|K_{\rm MT}'(t)|
\le2\pi\int_{-1}^{1}|\alpha|^3J_{\rm MT}(\alpha)\,d\alpha
=2\pi W_1,
\tag{11}
\]

where `W_1` is the exact moment already computed in `ANF-038`:

\[
W_1=
\frac{16\cos\sqrt2+2-3\sqrt2\sin\sqrt2}
{4(1-\cos\sqrt2)}.
\tag{12}
\]

Directed interval evaluation of (12) gives

\[
0.09014893986892659<W_1<0.09014893986892861,
\tag{13}
\]

and hence

\[
\boxed{|K_{\rm MT}'(t)|<0.566422494442269.}
\tag{14}
\]

Now evaluate the exact expression (8) on the rational mesh `t=k/1000` using outward-rounded interval arithmetic. On the first mesh block,

\[
420\le k\le545,
\]

the smallest certified lower endpoint for

\[
K_{\rm MT}(k/1000)+\frac{L_0}{3}
\]

occurs at `k=545` and satisfies

\[
\boxed{
K_{\rm MT}(k/1000)+\frac{L_0}{3}
>0.000392243185119.
}
\tag{15}
\]

On the second block,

\[
1010\le k\le1440,
\]

the smallest certified lower endpoint occurs at `k=1010` and satisfies

\[
\boxed{
K_{\rm MT}(k/1000)+\frac{L_0}{3}
>0.000389484544030.
}
\tag{16}
\]

Every point of either covered interval lies within `0.0005` of a mesh node. By (14), the maximum interpolation loss is strictly less than

\[
0.0005(0.566422494442269)
=0.0002832112472211345.
\tag{17}
\]

Subtracting (17) from (15)--(16) leaves the continuous margins

\[
\boxed{
K_{\rm MT}(t)+\frac{L_0}{3}
>0.0001090
\qquad(0.42\le|t|\le0.545),
}
\tag{18}
\]

and

\[
\boxed{
K_{\rm MT}(t)+\frac{L_0}{3}
>0.0001062
\qquad(1.01\le|t|\le1.44).
}
\tag{19}
\]

Because `K_0>L_0`, both intervals satisfy the stronger-than-needed implication

\[
K_{\rm MT}(t)>-\frac{L_0}{3}>-\frac{K_0}{3}.
\tag{20}
\]

The certificate is deliberately one-dimensional and auditable. It uses the exact transform (8), rational mesh locations, directed elementary-function intervals and the analytic Lipschitz constant (14); no sampled minimum is promoted without the interpolation bound (17).

## 3. Two integrations by parts clear the entire tail `|d|>=1.44`

It remains to avoid extending the finite mesh indefinitely. Since `J_MT` is even,

\[
K_{\rm MT}(t)
=2\int_0^1w(\alpha)\cos(2\pi t\alpha)\,d\alpha.
\tag{21}
\]

The closed form in `ANF-038` gives

\[
w(0)=w(1)=w'(0)=0.
\tag{22}
\]

Twice integrating (21) by parts therefore yields, with `omega=2pi t`,

\[
|K_{\rm MT}(t)|
\le
\frac{2}{\omega^2}
\left(
|w'(1)|+\int_0^1|w''(\alpha)|\,d\alpha
\right).
\tag{23}
\]

The total variation term can be bounded sharply with a small finite sign audit of the explicit derivatives of `w`. Directed interval arithmetic gives

\[
w'''([-0,0.35])\subset(-12.324,-3.061),
\tag{24}
\]

so `w''` is strictly decreasing on `[0,0.35]`, while

\[
w''(0.3)>0.05959,
\qquad
w''(0.32)<-0.09250.
\tag{25}
\]

Hence `w''` has exactly one zero `r` in `(0.3,0.32)` on that initial range. On the fourteen boxes

\[
[0.32+0.05j,\min(0.37+0.05j,1)],
\qquad 0\le j\le13,
\tag{26}
\]

the largest outward upper endpoint for `w''` is below `-0.0215`; hence there is no later zero. Thus `w'` increases from zero to a unique maximum `M=w'(r)` and then decreases to its negative endpoint value.

The same interval audit gives

\[
M<0.361110,
\qquad
|w'(1)|<0.684756.
\tag{27}
\]

Consequently

\[
\int_0^1|w''(\alpha)|\,d\alpha
=2M+|w'(1)|,
\tag{28}
\]

and therefore

\[
|w'(1)|+\int_0^1|w''(\alpha)|\,d\alpha
=2M+2|w'(1)|
<2.091732.
\tag{29}
\]

Substituting (29) into (23) gives

\[
\boxed{
|K_{\rm MT}(t)|
<\frac{2.091732}{2\pi^2t^2}.
}
\tag{30}
\]

At `|t|=1.44`, the right side is already strictly below

\[
0.051104
<\frac{L_0}{3}
=0.0516661975470586\ldots.
\tag{31}
\]

Since the right side of (30) decreases with `|t|`,

\[
\boxed{
|t|\ge1.44
\quad\Longrightarrow\quad
K_{\rm MT}(t)>-\frac{K_0}{3}.
}
\tag{32}
\]

This replaces the `1/|t|` total-variation tail used in `ANF-058` by a `1/t^2` tail tailored to the smooth explicit Montgomery--Taylor density.

## 4. The residual separation annulus is `0.545<|d|<1.01`

`ANF-058` already proves

\[
|d|\le0.42
\quad\Longrightarrow\quad
K_{\rm MT}(d)>-\frac{K_0}{3}.
\tag{33}
\]

Equation (18) bridges that region through `|d|=0.545`. Equations (19) and (32) prove the same curvature inequality for every `|d|>=1.01`. Therefore

\[
\boxed{
|d|\le0.545
\quad\text{or}\quad
|d|\ge1.01
\quad\Longrightarrow\quad
K_{\rm MT}(d)>-\frac{K_0}{3}.
}
\tag{34}
\]

The Montgomery--Taylor profile satisfies the curvature-gate hypothesis because `ANF-038` proves `m_5(J_MT)>0.0078`. Applying the all-height implication of `ANF-058` to (34) gives

\[
\boxed{
|d|\le0.545
\quad\text{or}\quad
|d|\ge1.01
\quad\Longrightarrow\quad
H_{\rm MT}(y_1,y_2;t_1,t_2)>0
}
\tag{35}
\]

for every pair of genuine positive heights and every common horizontal translation. Taking the contrapositive gives (2).

The threshold (1) remains only a necessary condition. Inside `0.545<|d|<1.01`, the fact that `K_MT(d)` may fall below `-K_0/3` does **not** imply that the full five-point defect is zero or negative. The remaining problem is still the exact Montgomery--Taylor coherence problem accepted in `CLUE-central-notch-base-margin-certificate`; the present result only removes most of its horizontal parameter range before the height variables are touched.

This sharpening is nevertheless useful for the next certificate. Any interval treatment of the exact defect, or of the Hilbert-coherence scalarization from `ANF-045`, now needs to cover less than half a unit of relative separation instead of the former `1.33`-wide annulus. The pre-existing unequal-height exclusions can then be intersected with this narrow strip rather than applied over the old coarse domain.

## 5. Prior art, reproducibility and evidence boundary

The extremal Montgomery--Taylor profile itself is classical within the pair-correlation extremal problem and is already anchored in `SOURCES.md` through Carneiro--Chandee--Littmann--Milinovich. A targeted check of that paper and neighboring pair-correlation literature also finds explicit Fourier-side formulas for the Montgomery--Taylor kernel. Accordingly, no novelty is claimed for the elementary factorization (5)--(8) by itself. The new Mathia content is the use of the exact second-moment transform in the `ANF-058` five-point curvature gate, together with the finite certified exclusion (18)--(19), the profile-specific `1/t^2` tail (30), and the resulting annulus (2).

No new external theorem is load-bearing, so `SOURCES.md` does not need another anchor. All decisive inputs are already canonical locally: the exact `J_MT` profile and moments from `ANF-038`, and the all-height curvature-correlation gate from `ANF-058`. The remaining work is elementary Fourier calculus plus finite directed interval arithmetic on closed expressions.

The finite numerical constants above are evidence only through their outward enclosures. Recomputing ordinary floating-point samples is not a substitute for the certificate. The mesh audit must enclose (8) at every stated rational node, (13) must enclose the exact moment (12), and the derivative-sign audit (24)--(27) must enclose the explicit derivatives of `w`. The positive margins in (18), (19), and (31) are deliberately much larger than the directed-rounding widths used in those evaluations.

This finding does **not** prove Montgomery--Taylor five-point zero-freeness, does not prove that the central-notch perturbation satisfies the full universal affine counting inequality, does not address higher-cardinality conjugation-invariant configurations, and does not by itself imply RH. Its durable contribution is a much smaller, fully explicit horizontal search/certification domain for the one fixed five-point base profile that controls the current central-notch frontier.