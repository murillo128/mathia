# ANF-056 — quadratic mismatch retention gives a support-free relative-height stability tube

**Status:** `EXACT-DERIVED + SUPPORT-FREE-HEIGHT-RATIO-TUBE + GLOBAL-HORIZONTAL-CLOSURE + QUADRATIC-MISMATCH-RETENTION + STRUCTURAL-REDUCTION`. `ANF-055` makes the unequal-height neighborhood of the positive diagonal explicit, but its support-edge `cosh` envelope shrinks exponentially with the mean height because it discards the positive quadratic mismatch block. Retaining that block changes the conclusion qualitatively: a fixed relative-height tube is safe at **every** mean height, independently of the spectral support radius.

Let `J` be nonzero, continuous, even and nonnegative with compact support. Put

\[
K_J(t)=\int \alpha^2J(\alpha)\cos(2\pi\alpha t)\,d\alpha,
\qquad
K_0=K_J(0)>0,
\]

and

\[
m_5(J)=2K_0+3\inf_t K_J(t).
\tag{1}
\]

Assume

\[
\boxed{m_5(J)\ge0.}
\tag{2}
\]

For genuine heights `y_1,y_2>0`, write

\[
y=\frac{y_1+y_2}{2},
\qquad
\delta=\frac{|y_1-y_2|}{2},
\qquad
q=\frac{\delta}{y}\in[0,1).
\tag{3}
\]

Define the explicit universal threshold

\[
\boxed{
q_c:=\operatorname{arsinh}\!\left(\frac{1}{8\sinh 1}\right)
=0.10616522\ldots .
}
\tag{4}
\]

Then every two-pair five-point configuration with

\[
\boxed{q\le q_c}
\tag{5}
\]

is strictly safe for **all** horizontal placements:

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)
\ge
\frac{\pi^2}{3}(5-2\sqrt6)K_0y^2
>0.
}
\tag{6}
\]

Equivalently, if `y_max=max(y_1,y_2)` and `y_min=min(y_1,y_2)`, then the whole height-ratio region

\[
\boxed{
\frac{y_{\max}}{y_{\min}}
\le
\frac{1+q_c}{1-q_c}
=1.23754\ldots
}
\tag{7}
\]

is globally positive. A particularly simple rational corollary is

\[
\boxed{
\frac{|y_1-y_2|}{y_1+y_2}\le\frac1{10}
\quad\Longrightarrow\quad
\frac{y_{\max}}{y_{\min}}\le\frac{11}{9}
\quad\Longrightarrow\quad H_J>0.
}
\tag{8}
\]

Unlike the tube of `ANF-055`, (5)--(8) contain no support radius `B` and do not narrow as `y` grows. For the accepted Montgomery--Taylor base-zero problem, every genuine zero must therefore have relative half-mismatch strictly larger than `q_c`; the exact equal-height core and a fixed open cone around it are now removed globally.

## 1. The positive mismatch block absorbs both correlation channels

Retain the mean-height variables and phases of `ANF-055`. Choose a signed half-mismatch `Delta=(y_1-y_2)/2`, so `|Delta|=delta`, and put

\[
u=2\pi\alpha y,
\qquad
v=2\pi\alpha\Delta,
\]

\[
d=t_1-t_2,
\qquad
m=\pi\alpha(t_1+t_2),
\qquad
C=\cos(\pi\alpha d),
\qquad
S=\sin(\pi\alpha d).
\tag{9}
\]

Because both physical heights are positive, `|Delta|<y`; hence

\[
|v|<|u|
\qquad(\alpha\ne0).
\tag{10}
\]

Let `h_alpha` be the exact unequal-height integrand and `h_alpha^diag` the same integrand after replacing both heights by their mean `y` while keeping the horizontal placement fixed. Equation (12) of `ANF-055` gives

\[
\begin{aligned}
h_\alpha-h_\alpha^{\rm diag}
={}&4\sinh^2v\bigl(\sinh^2u+C^2\bigr)\\
&+2\cosh u(\cosh v-1)C\cos m\\
&-2\sinh u\sinh v\,S\sin m.
\end{aligned}
\tag{11}
\]

The previous finding discarded the first line. Here keep it. Set

\[
U=|u|,
\qquad
V=|v|,
\qquad
x=\sinh U\,\sinh V\ge0.
\tag{12}
\]

Use the exact identity

\[
\cosh V-1=\sinh V\tanh\!\left(\frac V2\right).
\tag{13}
\]

Since `0<=V<=U` and `tanh` is increasing,

\[
\cosh U\tanh\!\left(\frac V2\right)
\le
\cosh U\tanh\!\left(\frac U2\right)
=
\sinh U\frac{\cosh U}{\cosh U+1}
\le\sinh U.
\tag{14}
\]

Therefore the Euclidean norm of the two coefficients multiplying `(cos m,sin m)` in (11) is at most

\[
2\sinh V\sqrt{
\cosh^2U\tanh^2(V/2)C^2
+\sinh^2U S^2
}
\le2x.
\tag{15}
\]

Minimizing those two correlation channels jointly over the mean phase can therefore lose at most `2x`. The positive first line of (11), on the other hand, is

\[
4\sinh^2V(\sinh^2U+C^2)
=4x^2+4\sinh^2V C^2.
\tag{16}
\]

Combining (15)--(16) yields the pointwise, all-horizontal inequality

\[
\boxed{
h_\alpha-h_\alpha^{\rm diag}
\ge
4x^2-2x+4\sinh^2V C^2
\ge4x^2-2x.
}
\tag{17}
\]

This is the structural gain missed by the support-edge estimate in `ANF-055`. Once the mismatch amplitude satisfies `x>=1/2`, changing the two heights away from their common mean cannot decrease the defect at that frequency at all. A mismatch can hurt only inside the central amplitude band

\[
\boxed{
\sinh(2\pi|\alpha|y)
\sinh(2\pi|\alpha|\delta)<\frac12.
}
\tag{18}
\]

Thus large hyperbolic amplification is not itself dangerous: beyond the threshold (18) it becomes a positive stabilizer.

## 2. A universal relative mismatch turns the exact loss into a quadratic moment

Write `V=qU`. From (17), the only negative part is bounded by

\[
2x(1-2x)_+.
\tag{19}
\]

For `q<=q_c`, this loss obeys the elementary global estimate

\[
\boxed{
2x(1-2x)_+
\le\frac{U^2}{4}
\qquad(U\ge0).
}
\tag{20}
\]

There are only two regimes.

If `U>=1`, the scalar function `2z(1-2z)` on `0<=z<=1/2` has maximum `1/4`. Hence

\[
2x(1-2x)_+\le\frac14\le\frac{U^2}{4}.
\tag{21}
\]

If `0<=U<=1`, use that `sinh s/s` is increasing for `s>0`. Since `q<=q_c`,

\[
\begin{aligned}
x
&=\sinh U\,\sinh(qU)\\
&\le
U\sinh1\cdot qU\frac{\sinh q_c}{q_c}\\
&\le
U^2\sinh1\sinh q_c
=\frac{U^2}{8},
\end{aligned}
\tag{22}
\]

where the last equality is exactly the definition (4). Thus

\[
2x(1-2x)_+\le2x\le\frac{U^2}{4},
\tag{23}
\]

proving (20). No support bound, small-height expansion or approximation is used.

Substituting `U=2pi|alpha|y` into (17)--(20) gives the pointwise perturbation inequality

\[
\boxed{
h_\alpha-h_\alpha^{\rm diag}
\ge
-\pi^2\alpha^2y^2
\qquad(q\le q_c).
}
\tag{24}
\]

Integrating against `J>=0` therefore yields

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)
\ge
H_J(y,y;t_1,t_2)
-\pi^2K_0y^2.
}
\tag{25}
\]

This is the key support-free replacement for equation (17) of `ANF-055`.

## 3. The curvature margin is strictly larger than the worst mismatch tax

`ANF-054` supplies, under `m_5(J)>=0`, the universal diagonal margin

\[
H_J(y,y;t_1,t_2)
\ge
c_*K_0y^2,
\qquad
c_*:=\frac{8\pi^2}{3}\left(1-\sqrt{\frac38}\right).
\tag{26}
\]

Combining (25) and (26),

\[
H_J(y_1,y_2;t_1,t_2)
\ge(c_*-\pi^2)K_0y^2.
\tag{27}
\]

The constant simplifies exactly:

\[
\begin{aligned}
c_*-\pi^2
&=\frac{\pi^2}{3}
\left(5-8\sqrt{\frac38}\right)\\
&=\boxed{\frac{\pi^2}{3}(5-2\sqrt6)}
=0.33234417\ldots>0,
\end{aligned}
\tag{28}
\]

because `25>24`. This proves (6).

The profile-specific diagonal constant `c_J` from `ANF-055` can be retained instead of `c_*`, giving the stronger bound

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)
\ge(c_J-\pi^2)K_0y^2
\qquad(q\le q_c).
}
\tag{29}
\]

The universal version is preferable as a structural statement: every positive spectrum passing the same curvature gate automatically receives the same fixed relative-height neighborhood.

## 4. Comparison with the previous unequal-height tube

The mechanisms in `ANF-055` and the present finding are complementary. `ANF-055` bounds each mismatch correlation separately and therefore retains a larger small-height limiting width, but pays support-edge factors

\[
\cosh(2\pi By)\cosh(2\pi Bqy),
\]

which make its certified relative width shrink at large `By`. Equation (17) instead minimizes the two correlation channels together and pays for them with the positive quadratic mismatch block. The resulting width `q_c` is slightly more conservative near `y=0` but is independent of both `B` and `y`.

Consequently the accepted `CLUE-central-notch-base-margin-certificate` no longer needs to treat arbitrarily tiny unequal-height perturbations of the diagonal at large mean height. For the fixed Montgomery--Taylor profile, every genuine base zero must satisfy

\[
\boxed{
\frac{|y_1-y_2|}{y_1+y_2}>q_c
=0.10616522\ldots,
}
\tag{30}
\]

or equivalently

\[
\boxed{
\frac{y_{\max}}{y_{\min}}>1.23754\ldots .
}
\tag{31}
\]

At the same time `ANF-049` requires any negative configuration to remain inside its scale-free height-balance cone. Thus the residual unequal-height search is genuinely intermediate: it is separated by a fixed gap from the diagonal but cannot become strongly imbalanced relative to the horizontal pair separation.

The central-band formulation (18) also suggests a sharper profile-specific continuation. Instead of replacing the negative part of `4x^2-2x` by the quadratic envelope (20), one can retain the exact one-dimensional mismatch-loss functional

\[
\boxed{
D_J(y,\delta)
:=2\int J(\alpha)x(\alpha)
\bigl(1-2x(\alpha)\bigr)_+\,d\alpha,
}
\tag{32}
\]

where

\[
x(\alpha)=
\sinh(2\pi|\alpha|y)
\sinh(2\pi|\alpha|\delta).
\tag{33}
\]

Then (17) gives the exact all-horizontal sufficient certificate

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)
\ge H_J(y,y;t_1,t_2)-D_J(y,\delta).
}
\tag{34}
\]

Because `x(alpha)` is increasing in `|alpha|`, `D_J` is supported only on the unique central interval where `x<1/2`. For the fixed Montgomery--Taylor spectrum this reduces the next refinement of the unequal-height gate to a **two-variable nonnegative integral bound in `(y,delta)`**, with the horizontal variables already eliminated. That is materially smaller than returning to a four-variable defect search.

## 5. Stress tests, audit path, and evidence boundary

The decisive audit begins from the exact identity (11), already independently derived in `ANF-055`. The only new hyperbolic step is (14): use `cosh V-1=sinh V tanh(V/2)`, monotonicity of `tanh`, and `V<=U`. The two mismatch correlations must then have Euclidean norm at most `2x`, while the retained positive block contributes `4x^2+4sinh^2(V)C^2`; this reproduces (17).

The envelope (20) is also finite and explicit. For `U>=1`, it is only the maximum `max_{0<=z<=1/2}2z(1-2z)=1/4`. For `U<=1`, monotonicity of `sinh s/s` and the defining equality `8sinh1 sinh q_c=1` give (22). These checks show exactly where the numerical threshold comes from; no floating-point optimization is evidence for the theorem.

The result is a sufficient positivity theorem, not an optimal tube. The split at `U=1` is deliberately simple, and optimizing the split or retaining the positive `4sinh^2(V)C^2` term can enlarge `q_c`. Failure of (5) says nothing about the sign of the exact defect. Likewise, (32)--(34) are a sharper certification interface, not a proof that the residual Montgomery--Taylor region is positive.

The load-bearing external framework is unchanged. A targeted prior-art check of the positive-definite-strip Fourier--Laplace literature and the pair-correlation Hilbert/semidefinite literature recovers the Buescu--Paixão--Symeonides representation and the established Montgomery--Taylor/Carneiro--Chandee--Littmann--Milinovich extremal framework already anchored in `SOURCES.md`, but no theorem matching the mean-height two-pair inequality (17), the support-free ratio tube (5)--(8), or the loss functional (32). No publication-level novelty claim is made, and no new source anchor is required because all new load-bearing steps are elementary consequences of the canonical `ANF-054`--`ANF-055` identities.

The finding remains confined to the two-conjugate-pair plus one-real-point layer. It does not decide the residual unequal-height Montgomery--Taylor zero problem outside (5), does not prove a full universal affine counting inequality for the central-notch family, does not control larger conjugation-invariant multisets, and does not resolve RH. Its durable contribution is to remove an **all-height, support-independent neighborhood of the diagonal** and to expose a one-dimensional central-band mismatch functional for the remaining five-point certification problem.
