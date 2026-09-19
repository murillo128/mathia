# NB-220 — Gaussian vertical windows give entire source-side continuation of localized zeta-primitive pairings

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + SOURCE-LOCALIZATION + GAUSSIAN-WINDOW + ENTIRE-CONTINUATION + ZETA-PRIMITIVE + NB-219-REFINEMENT`.

`NB-219` showed that compact smooth vertical windowing localizes the exact zeta-primitive convolution on the safe `Re(s)>1` side with superalgebraic source error. It also isolated a specific cost: a compactly supported vertical multiplier has a Schwartz inverse transform, so the modified logarithmic source has noncompact polynomially decaying tails. Those tails are harmless for `Re(s)>1` but are not absolutely summable after moving to a fixed line left of `1`.

That obstruction is **not intrinsic to vertical localization**. It is a consequence of demanding exact compact support in the vertical variable. Replacing the compact cutoff by a Gaussian-type soft window produces a dual logarithmic source with Gaussian tails. The resulting Euler source series then converges absolutely on every vertical line, so it gives an **entire source-side continuation** of the localized zeta-primitive pairing across `Re(s)=1`. At the same time, by making the Gaussian window flat to any prescribed finite order at the origin, the perturbation of the original shell can be made `O(V^{-B})` for any prescribed power `B` while keeping Gaussian source tails.

This removes the source-tail convergence obstacle left by `NB-219`. It does **not** yet provide a left-of-one representation as a local integral of `log zeta` or `-zeta'/zeta`, and therefore does not by itself improve the Vinogradov--Korobov corridor. The remaining issue is now sharper: connect the entire source continuation to zero-free-region data without reintroducing a global vertical acquisition or an absolute-value tariff.

## 1. A finite-order flat Gaussian window

Keep the notation and Fourier convention of `NB-218`--`NB-219`. Fix an integer `j>=1`, constants `r>0`, `Delta>0`, and

\[
\phi\in C_c^\infty((0,\Delta);\mathbb C).
\]

For large `X`, put

\[
\sigma_X:=1+\frac rX,
\qquad
h_X(u):=\phi(u-X),
\qquad
g_X(u):=u^j h_X(u),
\]

\[
K_X(v):=\int_0^\infty g_X(u)e^{ivu}\,du,
\]

and on `Re(s)>1`

\[
P_j(s):=\sum_{n\ge2}
\frac{\Lambda(n)}{(\log n)^j}n^{-s}.
\]

Thus `P_1=log zeta` on its canonical Euler-product branch and `P_j'=-P_(j-1)` with `P_0=-zeta'/zeta`.

For an integer `M>=0`, define the even entire window

\[
W_M(z)
:=
e^{-z^2}
\sum_{\ell=0}^{M}\frac{z^{2\ell}}{\ell!}.
\tag{1}
\]

For real `z`,

\[
0<W_M(z)\le1,
\]

and the omitted exponential tail gives

\[
1-W_M(z)
=
\frac{z^{2M+2}}{(M+1)!}
+O_M(z^{2M+4})
\qquad(z\to0).
\tag{2}
\]

More globally,

\[
|1-W_M(z)|
\ll_M
\min\{1,|z|^{2M+2}\}
\qquad(z\in\mathbb R).
\tag{3}
\]

For `V>=1`, define

\[
I_{X,V,M}(s)
:=
\frac1{2\pi}
\int_{\mathbb R}
W_M(v/V)K_X(v)P_j(s+iv)\,dv,
\qquad \Re(s)>1.
\tag{4}
\]

Unlike the compact cutoff of `NB-219`, the multiplier in (4) never vanishes identically outside a finite interval. But it is Gaussian on the real axis, and for `|v|>>V` it decays faster than any power. Thus it is a soft rather than hard vertical localizer.

## 2. The dual logarithmic kernel has Gaussian tails

Let

\[
\kappa_M(y)
:=
\frac1{2\pi}
\int_{\mathbb R}W_M(v)e^{-ivy}\,dv,
\qquad
\kappa_{M,V}(y):=V\kappa_M(Vy).
\tag{5}
\]

Each summand `v^(2 ell)e^(-v^2)` in (1) Fourier-transforms to a derivative of a Gaussian. Hence

\[
\kappa_M(y)=Q_M(y)e^{-y^2/4}
\tag{6}
\]

for an explicit polynomial `Q_M` of degree at most `2M`, up to the fixed Fourier-normalization constant. In particular there are constants `C_M,c_M>0` such that

\[
\boxed{
|\kappa_{M,V}(y)|
\le
C_M V e^{-c_MV^2y^2}
}
\tag{7}
\]

for all real `y` and `V>=1`, after absorbing the polynomial factor into a slightly weaker Gaussian.

Put

\[
g_{X,V,M}:=g_X*\kappa_{M,V},
\qquad
h_{X,V,M}(u):=u^{-j}g_{X,V,M}(u)
\quad(u>0).
\tag{8}
\]

Because `g_X` is supported in `[X,X+Delta]` and has size `O(X^j)` there, (7) gives

\[
|g_{X,V,M}(u)|
\ll_M
X^j
\exp\!\left[
-c_MV^2\operatorname{dist}(u,[X,X+\Delta])^2
\right].
\tag{9}
\]

The same type of estimate holds for every fixed derivative of `g_(X,V,M)`, with an additional polynomial factor in `V` that can again be absorbed into a weaker Gaussian when only tail convergence is at issue.

The difference with `NB-219` is qualitative. A compact vertical cutoff produced only Schwartz decay in `u`; the soft Gaussian window produces Gaussian decay in `u`.

## 3. The modified Euler source is entire in the Mellin variable

Define

\[
H_{X,V,M}(s)
:=
\sum_{n\ge2}
\Lambda(n)
 h_{X,V,M}(\log n)n^{-s}.
\tag{10}
\]

For every real `A>0`, a Chebyshev bound on unit logarithmic shells gives

\[
\sum_{e^m\le n<e^{m+1}}
\Lambda(n)n^{A}
\ll_A e^{(A+1)m}.
\tag{11}
\]

On the upper logarithmic tail `m>X+Delta+1`, equations (8)--(9) give

\[
|h_{X,V,M}(m)|
\ll_M
\exp[-c_MV^2(m-X-\Delta)^2],
\tag{12}
\]

up to a harmless bounded factor `(X/m)^j`. Therefore, uniformly for `s` in any compact subset of the complex plane,

\[
\sum_{m>X+\Delta+1}
\sum_{e^m\le n<e^{m+1}}
\Lambda(n)
|h_{X,V,M}(\log n)n^{-s}|
\]

is dominated by a convergent series of the form

\[
\sum_m
\exp(Cm-c_MV^2(m-X-\Delta)^2).
\tag{13}
\]

The lower logarithmic side contains only finitely many unit shells for each fixed `X`; the factor `u^{-j}` in (8) is harmless because the Euler source starts at `u=log 2>0`. Hence (10) converges absolutely and locally uniformly for **every** `s in C`. Consequently

\[
\boxed{
H_{X,V,M}(s)
\text{ is entire.}
}
\tag{14}
\]

On `Re(s)>1`, absolute convergence of `P_j` permits coefficientwise Fourier inversion exactly as in `NB-219`:

\[
\begin{aligned}
I_{X,V,M}(s)
&=
\sum_{n\ge2}
\frac{\Lambda(n)n^{-s}}{(\log n)^j}
\frac1{2\pi}
\int_{\mathbb R}
W_M(v/V)K_X(v)e^{-iv\log n}\,dv\\
&=
\sum_{n\ge2}
\Lambda(n)h_{X,V,M}(\log n)n^{-s}\\
&=H_{X,V,M}(s).
\end{aligned}
\tag{15}
\]

Thus (10) is an **entire source-defined analytic continuation of the soft-windowed zeta-primitive pairing (4)**. No branch of `log zeta`, zero-free rectangle, or termwise Dirichlet expansion is needed to define that continuation after crossing `Re(s)=1`.

This statement is about the continued pairing, not about the primitive itself. Equation (15) does not assert that the same real-`v` integral with a chosen branch of `P_j(s+iv)` remains valid on the left of `1`.

## 4. The original compact shell is approximated to any prescribed algebraic order

Write, as in `NB-219`,

\[
K_X(v)=e^{iXv}A_X(v),
\]

where the family `X^(-j)A_X` has uniformly bounded Schwartz seminorms. Combining this with (3), and splitting the real line into `|v|<=V` and `|v|>V`, gives for every fixed nonnegative derivative order `q` and spatial-decay order `N`

\[
\boxed{
\left|
\frac{d^q}{du^q}
\bigl(g_{X,V,M}(u)-g_X(u)\bigr)
\right|
\le
C_{q,N,M}
X^jV^{-(2M+2)}
(1+|u-X|)^{-N}.
}
\tag{16}
\]

The proof is the same carrier-removal argument as in `NB-219`, with one extra finite-order zero. On `|v|<=V`, equation (3) supplies `V^(-2M-2)|v|^(2M+2)`; on `|v|>V`, arbitrary Schwartz decay of `A_X` supplies the same power of `V`. Differentiating the multiplier only improves the scale after `V>=1`, and integration by parts in `v` yields the spatial factor in (16).

Measure (16) in the actual Euler norm on the natural safe line:

\[
\mathcal R_{X,V,M}
:=
\sum_{n\ge2}
\Lambda(n)n^{-1-r/X}
\left|
 h_{X,V,M}(\log n)-h_X(\log n)
\right|.
\tag{17}
\]

The unit-logarithmic-shell estimate used in `NB-219`, with `N>j+2`, gives

\[
\boxed{
\mathcal R_{X,V,M}
\ll_{M,j,r,\phi}
V^{-(2M+2)}.
}
\tag{18}
\]

Therefore, uniformly in real `t`,

\[
\boxed{
S_X(t)
=
H_{X,V,M}(\sigma_X+it)
+O_{M,j,r,\phi}\!\left(V^{-(2M+2)}\right),
}
\tag{19}
\]

where

\[
S_X(t)
:=
\sum_{n\ge2}
\Lambda(n)h_X(\log n)n^{-\sigma_X-it}.
\]

For any prescribed `B>0` and fixed `epsilon>0`, choose `M` once so that

\[
2(M+1)\epsilon>B.
\]

Then `V=X^epsilon` gives

\[
\boxed{
S_X(t)
=
H_{X,X^\epsilon,M}(\sigma_X+it)
+O_B(X^{-B})
}
\tag{20}
\]

uniformly in `t`. A single fixed Gaussian `M=0` already gives `o(1)` for every choice `V_X->infinity`; increasing `M` buys any desired finite algebraic order without sacrificing Gaussian source tails.

This is slightly weaker than the one-window superalgebraic `V^(-A)` statement of `NB-219`, but it is qualitatively stronger for crossing the one-line: the dual source now has enough decay to define the pairing on every Mellin line.

## 5. Finite-jet annihilation survives with Gaussian accuracy

Let

\[
K_{X,V,M}(v):=W_M(v/V)K_X(v).
\tag{21}
\]

Its inverse Fourier transform is `g_(X,V,M)`. Hence, up to the fixed convention-dependent phase,

\[
\int_{\mathbb R}v^qK_{X,V,M}(v)\,dv
=
2\pi i^q g_{X,V,M}^{(q)}(0).
\tag{22}
\]

The point `u=0` lies distance `X+O(1)` from the support of `g_X`. Differentiating the Gaussian kernel in (5)--(7) therefore gives, for every fixed `q` and `M`,

\[
|g_{X,V,M}^{(q)}(0)|
\le
C_{q,M,j,\phi}
X^j V^{q+1}
(1+VX)^{C_{q,M}}
 e^{-c_MV^2X^2}.
\tag{23}
\]

In particular, for every fixed `q` and every `A>0`,

\[
\boxed{
\left|
\int_{\mathbb R}v^qK_{X,V,M}(v)\,dv
\right|
\ll_{q,M,A}
X^{-A}
}
\tag{24}
\]

uniformly for `V>=1` and sufficiently large `X` after enlarging constants.

Thus the high-pass feature isolated in `NB-218` is preserved even more strongly than under the compact window of `NB-219`: any fixed Taylor jet of the primitive remains invisible up to a Gaussian-small leakage coming from the distance between the moving shell and `u=0`.

## 6. What has and has not been solved

The main consequence is a correction to the frontier left by `NB-219`. **Noncompact source tails are not by themselves the obstruction to transporting a vertically localized primitive pairing across `Re(s)=1`.** They become problematic only when one insists on exact compact support in the vertical variable. A soft analytic window can simultaneously provide:

- effective vertical localization on the real axis;
- arbitrarily high prescribed algebraic fidelity to the original compact Euler shell;
- Gaussian localization in `u=log n`;
- an entire source-defined continuation of the localized pairing; and
- negligible leakage of every fixed polynomial jet.

What remains unresolved is the analytically important part. The equality with the zeta-primitive integral in (15) was proved only on `Re(s)>1`. The entire function `H_(X,V,M)` gives the unique continuation of that pairing, but this alone does not express its left-of-one values as a local integral of `P_j` on a zero-free rectangle. To exploit Vinogradov--Korobov information one still needs a justified complex-`v` contour deformation, or another identity, that connects the entire continuation back to the primitive while tracking the pole and zeta zeros.

The Gaussian window helps that next step structurally: `W_M` is entire and has no artificial cutoff edges, and for a small imaginary displacement `d` its real-axis decay remains Gaussian. But a global contour deformation can still encounter zeta singularities at remote ordinates. Their suppression has not been proved here and cannot be assumed merely because the central rectangle is zero-free.

Therefore no improved Vinogradov--Korobov error, positive-return corridor, Nyman distance bound, or destination-side approximation theorem is claimed.

## 7. Representation, prior-art, and falsification audit

**Generic mechanism.** Gaussian Fourier duality and the fact that a polynomial times a Gaussian Fourier-transforms to another polynomial times a Gaussian are classical. More broadly, the tradeoff between hard frequency support and the decay/analyticity of the dual variable is standard Paley--Wiener territory. A targeted prior-art search also found the standard use of Gaussian smoothing in analytic number theory, including Helfgott's discussion of Gaussian Mellin smoothing in *The ternary Goldbach problem* (arXiv:1501.05438, Chapter 8). No novelty is claimed for Gaussian smoothing or for equations (5)--(7).

**Project-local specialization.** The substantive line-local point is the coupling of that classical soft window to the exact `NB-218` zeta-primitive convolution and the `NB-219` Euler source norm. Equations (10)--(20) show that the particular source-tail obstruction created by hard vertical localization can be removed without reverting to an `L^1 times L^infinity` estimate of the primitive. The proof uses only Fourier inversion, Gaussian decay, and the Chebyshev/PNT shell envelope already available in this line, so no new load-bearing external source is required and `SOURCES.md` need not change.

**Falsification test 1: do not call the window compact.** `W_M(v/V)` is nonzero for all real `v`. Any argument that subsequently assumes the primitive is sampled only on `|v|<=CV` has changed the theorem. The tails are rapidly suppressed, not absent.

**Falsification test 2: continuation is not a left-line primitive formula.** The entire Euler series (10) is the analytic continuation of (4), but zeros of zeta can obstruct writing that continuation as the same real-axis primitive integral on the left. Treating (14) as a zero-free-region estimate would be circular.

**Falsification test 3: the approximation order is finite for a fixed window.** For fixed `M`, equation (18) gives `V^(-2M-2)`, not `O_A(V^-A)` for every `A`. Arbitrary algebraic accuracy is obtained by choosing `M` according to the requested order before taking the asymptotic limit. Allowing `M` to grow with `X` would require a separate audit of the constants.

**Falsification test 4: entire continuation does not imply smallness.** The continued source correlation can be large on a left line. Entirety removes a representation/admissibility obstruction; it is not itself a cancellation theorem.

The next decisive question is therefore narrower than after `NB-219`: use an analytic soft window such as (1) and determine whether its complex-`v` contour can be displaced by a Vinogradov--Korobov width with all remote zero/pole contributions negligible at source scale. A positive result would finally produce a cancellation-sensitive local primitive representation on the shifted contour; a negative result would identify the zero-residue budget that replaces the former Schwartz-tail obstruction.