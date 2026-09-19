# NB-219 — Smooth vertical windowing localizes the exact zeta-primitive convolution with superalgebraic source error

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + SOURCE-LOCALIZATION + SMOOTH-WINDOW + SUPERALGEBRAIC-ERROR + ZETA-PRIMITIVE + NB-218-REFINEMENT`.

`NB-218` reduced the live source-side escape to a signed Fourier coefficient of a zeta primitive, but left two analytically distinct obstacles entangled: the exact convolution runs over the whole vertical line, whereas Vinogradov--Korobov information is local in height; and the eventual contour must move from the absolutely convergent half-plane through `Re(s)=1`. The first issue can be separated cleanly from the second.

For a smooth logarithmic shell centered at `X` and evaluated on the natural line `sigma_X=1+r/X`, multiply the exact primitive kernel by any smooth vertical cutoff that is `1` on `|v|<=V` and vanishes outside `|v|<=2V`. The truncated convolution is **exactly another Euler shell correlation**, whose logarithmic profile is the original shell convolved with a Schwartz approximate identity. Because the original shell profile is `C_c^infinity`, the induced source error is `O_A(V^(-A))` for every `A`, uniformly in the vertical ordinate.

Thus on the safe `1+` side, the full-line tail is not a genuine source-side obstruction: any `V_X -> infinity`, however slowly, gives `o(1)` error, and `V=X^epsilon` gives decay faster than every prescribed power of `X`. What remains nontrivial is transporting this localization across `Re(s)=1`. The windowed source profile is no longer compactly supported in `log n`; its Schwartz tails are harmless for `sigma>1` but are not absolutely summable on a line to the left of `1`. So the old full-line problem splits into a benign Fourier-localization lemma and a genuinely arithmetic contour/continuation problem.

## 1. Exact smooth vertical truncation is another Euler source correlation

Fix an integer `j>=1`, constants `r>0`, `Delta>0`, and a profile

\[
\phi\in C_c^\infty((0,\Delta);\mathbb C).
\]

For large `X`, set

\[
\sigma_X:=1+\frac rX,
\qquad
h_X(u):=\phi(u-X),
\qquad
g_X(u):=u^j h_X(u).
\tag{1}
\]

Define, as in `NB-218`,

\[
K_X(v)
:=
\int_0^\infty g_X(u)e^{ivu}\,du
\tag{2}
\]

and

\[
P_{j,X}(t)
:=
\sum_{n\ge2}
\frac{\Lambda(n)}{(\log n)^j}
 n^{-\sigma_X-it}.
\tag{3}
\]

The exact source shell is

\[
S_X(t)
:=
\sum_{n\ge2}
\Lambda(n)h_X(\log n)n^{-\sigma_X-it}
=
\frac1{2\pi}
\int_{\mathbb R}K_X(v)P_{j,X}(t+v)\,dv.
\tag{4}
\]

Choose once and for all

\[
\chi\in C_c^\infty(\mathbb R),
\qquad
\chi(v)=1\ \text{for }|v|\le1,
\qquad
\operatorname{supp}\chi\subset[-2,2].
\tag{5}
\]

For `V>=1`, define the vertically localized pairing

\[
I_{X,V}(t)
:=
\frac1{2\pi}
\int_{\mathbb R}
\chi(v/V)K_X(v)P_{j,X}(t+v)\,dv.
\tag{6}
\]

Only ordinates

\[
t-2V\le t+v\le t+2V
\tag{7}
\]

occur in (6).

Let

\[
\kappa(y)
:=
\frac1{2\pi}
\int_{\mathbb R}\chi(v)e^{-ivy}\,dv,
\qquad
\kappa_V(y):=V\kappa(Vy),
\tag{8}
\]

and put

\[
g_{X,V}:=g_X*\kappa_V,
\qquad
h_{X,V}(u):=u^{-j}g_{X,V}(u)
\quad(u>0).
\tag{9}
\]

With the Fourier convention in (2), `g_(X,V)` is exactly the inverse transform of `chi(v/V)K_X(v)`. Absolute convergence of (3) on `sigma_X>1` therefore permits coefficientwise Fourier inversion in (6):

\[
\begin{aligned}
I_{X,V}(t)
&=
\sum_{n\ge2}
\frac{\Lambda(n)n^{-\sigma_X-it}}{(\log n)^j}
\frac1{2\pi}
\int_{\mathbb R}
\chi(v/V)K_X(v)e^{-iv\log n}\,dv\\
&=
\sum_{n\ge2}
\Lambda(n)h_{X,V}(\log n)n^{-\sigma_X-it}.
\end{aligned}
\tag{10}
\]

Hence the vertical cutoff has not produced an arbitrary analytic remainder. It has simply replaced the original source profile `h_X` by the explicitly mollified profile `h_(X,V)`.

## 2. The source profile changes by a superalgebraic high-pass tail

Write `u=X+y`. Expanding the polynomial multiplier gives

\[
g_X(X+y)
=(X+y)^j\phi(y)
=
\sum_{k=0}^j
\binom jk X^{j-k}q_k(y),
\qquad
q_k(y):=y^k\phi(y).
\tag{11}
\]

Every `q_k` is a fixed compactly supported smooth function. Factoring the carrier from (2),

\[
K_X(v)
=
e^{iXv}
\sum_{k=0}^j
\binom jk X^{j-k}\widehat q_k(v),
\tag{12}
\]

where every `widehat q_k` is Schwartz. Since `chi(v/V)=1` for `|v|<=V`, the difference `g_(X,V)-g_X` is the inverse transform of the high-frequency tail

\[
-\bigl(1-\chi(v/V)\bigr)K_X(v).
\tag{13}
\]

Schwartz decay, followed by integration by parts in `v`, gives the following uniform estimate: for every nonnegative integers `m,A,N`,

\[
\boxed{
\left|
\frac{d^m}{du^m}
\bigl(g_{X,V}(u)-g_X(u)\bigr)
\right|
\le
C_{m,A,N}
X^jV^{-A}
(1+|u-X|)^{-N}.
}
\tag{14}
\]

The important point is that the carrier `e^(iXv)` has already been removed before integrating by parts. Derivatives used to obtain spatial decay therefore fall on fixed Schwartz transforms `widehat q_k` and on the cutoff, not on the moving phase. All `X`-dependence is contained in the harmless polynomial prefactor bounded by `O(X^j)`.

Equation (14) is purely Fourier analytic. It says that a smooth vertical window of radius `V` changes a fixed-width moving logarithmic shell only by a Schwartz tail whose amplitude is smaller than every power of `V`.

## 3. The Euler source norm preserves the superalgebraic error

The relevant quantity is not a uniform norm of `h_(X,V)-h_X`, because division by `u^j` in (9) amplifies the very low logarithmic region. What matters is the actual Euler source norm on the natural `1+` line:

\[
\mathcal R_{X,V}
:=
\sum_{n\ge2}
\Lambda(n)n^{-\sigma_X}
\left|
h_{X,V}(\log n)-h_X(\log n)
\right|.
\tag{15}
\]

A Chebyshev bound for `psi(x)=sum_(n<=x)Lambda(n)` gives, uniformly for integer `m>=1`,

\[
\sum_{e^m\le n<e^{m+1}}
\Lambda(n)n^{-1-r/X}
\ll_r e^{-rm/X}.
\tag{16}
\]

On the same unit logarithmic interval, (14) and (9) give, up to an absolute adjustment for the first interval,

\[
|h_{X,V}(\log n)-h_X(\log n)|
\ll_{A,N}
X^jV^{-A}
 m^{-j}(1+|m-X|)^{-N}.
\tag{17}
\]

Consequently

\[
\mathcal R_{X,V}
\ll_{A,N,r}
X^jV^{-A}
\sum_{m\ge1}
e^{-rm/X}m^{-j}(1+|m-X|)^{-N}.
\tag{18}
\]

Split the sum into `m<X/2`, `X/2<=m<=2X`, and `m>2X`. In the central range, `X^jm^(-j)=O(1)` and the spatial Schwartz weight is summable. In the lower range, `(1+|m-X|)^(-N)<<X^(-N)` and `sum_(m<=X/2)m^(-j)` grows at most logarithmically. In the upper range, `m-X` is comparable with `m`, so any `N>2` makes the remaining tail uniformly summable. Taking `N>j+2` therefore yields

\[
\boxed{
\mathcal R_{X,V}
\le C_{A,j,r,\phi,\chi}V^{-A}
\qquad
(A>0),
}
\tag{19}
\]

uniformly for all sufficiently large `X` and all `V>=1`.

Since the phase `n^(-it)` has modulus one, (10), (15), and (19) imply the uniform localization theorem

\[
\boxed{
S_X(t)
=
I_{X,V}(t)
+O_A(V^{-A})
}
\tag{20}
\]

for every real `t`.

Thus **no pointwise bound for the zeta primitive is used to remove the full-line tail**. The tail is killed before estimating the primitive, by transferring the vertical cutoff back to the source coefficients and using smoothness of the logarithmic shell.

## 4. Any slowly growing vertical window is enough on the `1+` side

Equation (20) has two useful consequences. First, if

\[
V_X\longrightarrow\infty,
\tag{21}
\]

at any rate, then

\[
S_X(t)
=
I_{X,V_X}(t)+o(1)
\tag{22}
\]

uniformly in `t`. In particular, the exact full-line convolution from `NB-218` does not require a vertical window whose width is comparable with the shell carrier `X`.

Second, for any fixed `epsilon>0`, taking

\[
V_X=X^\epsilon
\tag{23}
\]

gives, for every prescribed `B>0`,

\[
\boxed{
S_X(t)
=
I_{X,X^\epsilon}(t)+O_B(X^{-B}).
}
\tag{24}
\]

Indeed choose `A>B/epsilon` in (20). If additionally `V_X=o(|t|)`, the primitive is sampled only on a genuinely local relative window around the target ordinate. This is precisely the locality shape needed before one can ask whether a Vinogradov--Korobov estimate can retain the signed carrier correlation rather than reverting to an `L^1 times L^infinity` decoupling.

There is no contradiction with `NB-217`. That finding lower-bounds the `L^1` reconstruction norm after absolute-value decoupling. Equation (20) never bounds the primitive by a supremum and never estimates the discarded vertical tail as `int |K_X P_j|`. Instead it shows that **smoothly deleting high vertical frequencies corresponds to a superalgebraically small perturbation of the Euler source itself**.

## 5. Finite-jet annihilation survives truncation to superalgebraic accuracy

The exact kernel `K_X` in `NB-218` annihilates every polynomial in `v` because `g_X` vanishes near `u=0`. Multiplication by `chi(v/V)` destroys that identity exactly, but only by a negligible amount.

Let

\[
K_{X,V}(v):=\chi(v/V)K_X(v).
\tag{25}
\]

Its inverse Fourier transform is `g_(X,V)`. Therefore, up to the convention-dependent unit factor,

\[
\int_{\mathbb R}v^mK_{X,V}(v)\,dv
=
2\pi\,i^m g_{X,V}^{(m)}(0).
\tag{26}
\]

For large `X`, every derivative of `g_X` vanishes at the origin. Applying (14) at `u=0` and choosing the spatial exponent `N` arbitrarily large gives, for every fixed `m` and every `A,B>0`,

\[
\boxed{
\left|
\int_{\mathbb R}v^mK_{X,V}(v)\,dv
\right|
\ll_{m,A,B}
V^{-A}X^{-B}.
}
\tag{27}
\]

Thus a finite Taylor polynomial of `P_j(t+v)` is still invisible to the localized kernel up to an error smaller than arbitrary powers of both the window parameter and the shell scale. Smooth vertical localization does not materially destroy the high-pass cancellation identified in `NB-218`.

## 6. The remaining obstruction is crossing `Re(s)=1`, not the full vertical tail

The conclusion above is deliberately restricted to

\[
\sigma_X=1+r/X>1.
\]

This restriction is structural, not cosmetic. The coefficientwise proof of (10) uses absolute convergence of `P_(j,X)`, and the source estimate (19) is evaluated with the positive Euler weight `n^(-1-r/X)`.

More importantly, compact vertical support has a dual cost. The mollified function `g_(X,V)=g_X*kappa_V` is Schwartz in the logarithmic variable but is no longer compactly supported. Hence `h_(X,V)` has nonzero tails for arbitrarily large `u=log n`. Polynomial decay in `u` is enough on `sigma>1`, but on a line `sigma=1-delta<1` the counting density contributes an exponential factor `e^(delta u)`, which eventually dominates every Schwartz power. The Dirichlet series in (10) therefore does **not** acquire absolute convergence on the Vinogradov--Korobov line merely because its vertical kernel is compactly supported.

So (20) cannot simply be analytically continued term by term through `Re(s)=1`. A continuation argument must still control the pole of zeta, the branch of `log zeta` when `j=1`, the zero-free rectangle used by the contour, horizontal edges, and the noncompact source tails introduced by the window. Those terms are exactly where an absolute-value estimate could reintroduce the Mellin tariff.

This separates the two issues left by `NB-218`:

1. **Full-line versus local vertical acquisition on the `1+` side:** solved by (20) with superalgebraic source error.
2. **Transport of that localized signed pairing to the shifted zero-free contour:** still open and now isolated as the genuine analytic bottleneck.

No Vinogradov--Korobov improvement, no bound for the Nyman--Beurling distance, and no destination-side theorem is asserted here.

## 7. Representation and prior-art audit

**Generic mechanism.** Multiplying a Fourier transform by a smooth compact cutoff is the standard Fourier-multiplier operation dual to convolution with a Schwartz approximate identity. For a fixed smooth compactly supported profile, deleting frequencies `|v|>V` incurs error smaller than every inverse power of `V`. Equation (14) is this classical fact with a moving carrier and a fixed polynomial multiplier.

**Arithmetic specialization.** The nontrivial project-local step is to measure that generic approximation in the Euler norm actually present in the line. On `sigma_X=1+r/X`, the unit-logarithmic-shell estimate (16) converts the moving factor `X^j/u^j` and the off-shell Schwartz tails into the uniform source estimate (19). This is what turns generic Fourier localization into the source-faithful statement (20).

A targeted prior-art search found the classical smooth-test-function/explicit-formula framework, where prime or von-Mangoldt sums are paired with Fourier transforms of smooth test functions, and the standard smoothed explicit-formula literature uses analogous Fourier/Mellin localization. It also found work on logarithmic Fourier integrals for zeta and smoothed hybrid Euler--Hadamard formulas. These are close methodological neighbors, but no external theorem is needed for (10)--(20): Fourier inversion, Schwartz decay, and a Chebyshev/PNT envelope already present in this line suffice. No claim is made that smooth Fourier localization itself is new. The project-local content is the identification that the particular full-line tail exposed by `NB-218` can be removed **before** decoupling the zeta primitive, without paying the `NB-217` reconstruction tariff. `SOURCES.md` therefore needs no new anchor.

## 8. Adversarial checks, falsification test, and consequence

**The cutoff changes the source.** Equation (20) is not the assertion that the literal tail integral `int_(|v|>V)K_X(v)P_j(t+v)dv` is small because `P_j` is bounded there. It is small because the complete signed identity turns the cutoff into a nearby source profile. Any attempted proof that replaces this coefficientwise step by `sup |P_j|` has abandoned the mechanism and falls back under `NB-217`.

**Schwartz is not exponential.** The localized source profile has infinite logarithmic support. This is the simplest falsification test for an overstrong version of the finding: if one tries to use (10) as an absolutely convergent Dirichlet series on any fixed line `sigma<1`, the far-right logarithmic tail defeats the argument. A valid continuation theorem must handle that tail by analytic structure, not by absolute convergence.

**The estimate depends on smooth shell data.** Discontinuous or `X`-dependent profiles whose derivative norms grow rapidly need not satisfy (14) with uniform constants. They require their own approximation budget. The claim here is for a fixed `C_c^infinity` profile translated to the moving shell.

**No local carrier estimate has been proved.** Even after (20), one must still control

\[
\int_{|v|\le2V}
K_X(v)P_{j,X}(t+v)\,dv
\]

without destroying its phase. Localization only makes that target finite-window; it does not make the Fourier coefficient small.

The research consequence is a sharper next question. The old requirement “localize the full primitive convolution and then estimate its carrier coefficient” can now be split. Source-side localization on `Re(s)>1` is already superalgebraically cheap. The next useful result must instead be a **cross-`1` localization/contour lemma that preserves the signed windowed pairing**, or a direct estimate of that pairing on a zero-free rectangle. If such a lemma necessarily incurs the reciprocal-support tariff, it would close the escape negatively; if it transports (20) without that loss, the remaining problem becomes the genuinely local carrier-frequency behavior of the zeta primitive.