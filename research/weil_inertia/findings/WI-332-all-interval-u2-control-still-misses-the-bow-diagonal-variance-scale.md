# WI-332 — all-interval U² control still misses the bow diagonal-variance scale

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE`.

The 2023 all-interval short-interval uniformity theorem contains a stronger input than the nilsequence statement used in WI-331: at the `5/8+epsilon` scale it gives arbitrary logarithmic saving in the normalized local `U^2` norm of the *signed source* `Lambda-Lambda^sharp`. This is genuinely closer to the WI-195 bow `L^2` target than a single pointwise twisted-sum estimate, but it still does not close that target by black-box Fourier/Hölder transference.

There are two independent obstructions. First, the natural bow carrier `n^{iU}` with `|U| asymp X^2` is nonlinear at order two on the source scale, while `U^2` is invariant only under linear phases. Second, even if the twist is removed completely, a direct conversion of a normalized local `U^2` bound

\[
\|a\|_{U^2(I)}\le \delta
\]

into mean square of length-`K` interval sums loses one full factor of `K`: on `K`-sized source blocks it gives only

\[
O(\delta^2 K^3),
\]

and after covering a macroscopic `X`-interval this is

\[
O(\delta^2 X K^2).
\]

The WI-195 gate is instead

\[
o(XK\log X).
\]

Thus the published `delta <<_A log^{-A} X` saving remains polynomially too weak whenever `K=X^{c+o(1)}` with fixed `c>0`. Any direct norm-only route of this form would need, schematically,

\[
\delta^2=o\!\left(\frac{\log X}{K}\right),
\]

a power-scale gain rather than an arbitrary fixed logarithmic gain.

This does **not** say the bow variance estimate is false, and it does not close higher-order or arithmetic routes. It closes only the tempting shortcut “all-interval `U^2` logarithmic uniformity ⇒ the WI-195 diagonal-scale variance bound.” The distinguished-twist clue therefore remains a problem about additional off-diagonal arithmetic cancellation (or a genuinely stronger structural norm input), not about extracting more fixed logarithmic saving from the existing `U^2` theorem.

## 1. Published input: an all-interval `U^2` logarithmic saving

The primary source is:

Kaisa Matomäki, Xuancheng Shao, Terence Tao and Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals I. All intervals**, *Forum of Mathematics, Pi* **11** (2023), e29, DOI `10.1017/fmp.2023.28`, arXiv:2204.03754v4.

The paper proves all-interval higher uniformity at interval exponent `5/8+epsilon` for the von Mangoldt function and its sieve approximant. In the discussion of the `s=2` case the authors record the stronger quantitative form: for every fixed `A,epsilon>0`, on intervals of the admissible `5/8+epsilon` scale,

\[
\|\Lambda-\Lambda^\sharp\|_{U^2(I)}
\ll_{A,\varepsilon}\log^{-A}X,
\tag{1}
\]

with the local Gowers norm normalized relative to the interval. The same discussion gives the corresponding bound for `mu`. This is stronger, for `s=2`, than merely knowing an unspecified `o(1)` normalized Gowers norm.

For the bow line, the important point is that (1) is already stated for the signed source `Lambda-Lambda^sharp`; no comparison with a different model is needed before asking whether `U^2` itself can close WI-195.

## 2. First obstruction: the bow carrier is not a linear phase at natural height

Write

\[
f_X(n):=\Lambda(n)-\Lambda_X^\sharp(n).
\]

The WI-195 variance gate concerns the twisted source

\[
a_n=f_X(n)n^{iU},
\qquad |U|\asymp X^2,
\tag{2}
\]

on `n asymp X`. Multiplication by a linear phase preserves the `U^2` norm, but the phase in (2) is `U log n`. Its discrete second difference is

\[
\begin{aligned}
\Delta^2(U\log n)
&=U\bigl(\log(n+2)-2\log(n+1)+\log n\bigr)\\
&=-\frac{U}{n^2}+O\!\left(\frac{|U|}{n^3}\right).
\end{aligned}
\tag{3}
\]

At `n asymp X` and `|U| asymp X^2`, the curvature in (3) is order one. Hence the natural bow twist is not uniformly reducible to a linear character on growing source intervals, and the invariance that would transfer (1) directly to `f_X(n)n^{iU}` is unavailable.

This is a phase-order mismatch, not a claim that the carrier is arithmetically hostile. WI-329/WI-331 show that the logarithmic carrier can instead be approximated by a fixed-degree polynomial phase on the relevant short intervals and handled by nilsequence theorems. What fails here is specifically the attempt to use the *`U^2`* estimate as though the bow twist were linear.

## 3. Second obstruction: even the untwisted black-box conversion loses a factor `K`

The more decisive normalization barrier is already present at `U=0`, so it cannot be blamed on (3).

Let `I` be an integer interval of length `L` and let `a` be supported on `I`. Use the unnormalized Fourier transform

\[
\widehat a(\alpha)=\sum_n a_n e(-n\alpha),
\qquad \alpha\in\mathbb R/\mathbb Z.
\]

The exact `U^2` Fourier identity is

\[
\|a\|_{U^2(\mathbb Z)}^4
=
\int_0^1|\widehat a(\alpha)|^4\,d\alpha.
\tag{4}
\]

For the indicator of an interval,

\[
\|1_I\|_{U^2(\mathbb Z)}^4
=
\sum_d(L-|d|)_+^2
=
\frac{2L^3+L}{3}.
\tag{5}
\]

Therefore a normalized local estimate

\[
\|a\|_{U^2(I)}\le\delta
\]

implies

\[
\int_0^1|\widehat a(\alpha)|^4\,d\alpha
\le
\delta^4\frac{2L^3+L}{3}.
\tag{6}
\]

Now let

\[
D_K(\alpha):=\sum_{1\le h\le K}e(h\alpha).
\]

For discrete starts, Parseval gives

\[
\sum_x\left|\sum_{x<n\le x+K}a_n\right|^2
=
\int_0^1|\widehat a(\alpha)|^2|D_K(\alpha)|^2\,d\alpha.
\tag{7}
\]

Applying Cauchy--Schwarz to (7), then using (6) and the companion exact identity

\[
\int_0^1|D_K(\alpha)|^4\,d\alpha
=
\frac{2K^3+K}{3},
\tag{8}
\]

gives

\[
\sum_x\left|\sum_{x<n\le x+K}a_n\right|^2
\ll
\delta^2 L^{3/2}K^{3/2}.
\tag{9}
\]

To apply this locally to starts in `[X,2X]`, divide the start range into blocks of length `K` and enlarge each source block to length `L\asymp K` so every corresponding length-`K` window is contained in its source block. Equation (9) then costs `O(delta^2 K^3)` per block. There are `O(X/K)` blocks, hence the direct global consequence is only

\[
\boxed{
O(\delta^2 X K^2).
}
\tag{10}
\]

Endpoint enlargement and the continuous-vs-discrete interpolation used in Gallagher-type formulas change only constants at this scale; the lost power of `K` in (10) is structural.

## 4. Comparison with the WI-195 gate

WI-195 isolates the natural multiplicative-Gallagher target

\[
\int_X^{2X}
\left|
\sum_{x<n\le x+K}f_X(n)n^{iU}
\right|^2dx
=o(XK\log X),
\tag{11}
\]

with

\[
K=X^{1-2\vartheta+o(1)}
\]

in the bow regime under study. Even granting away the phase-order obstruction and inserting the published quantitative `U^2` saving

\[
\delta\ll_A\log^{-A}X
\]

into (10) gives only

\[
O_A(XK^2\log^{-2A}X).
\tag{12}
\]

Relative to (11), the scale ratio is

\[
\frac{K}{\log^{2A+1}X},
\tag{13}
\]

which diverges for every fixed `A` when `K=X^{c+o(1)}` with fixed `c>0`. More generally, a black-box estimate of the form (10) could reach (11) only if

\[
\boxed{
\delta^2=o\!\left(\frac{\log X}{K}\right).
}
\tag{14}
\]

Thus arbitrary fixed logarithmic saving in normalized `U^2` is categorically the wrong scale for this transference.

This reproduces, at the norm level, the same polynomial gap that WI-195 and WI-331 observed when squaring pointwise `K log^{-A}X` cancellation. The stronger `U^2` input is real, but the direct Fourier/Hölder bridge still spends one factor of `K` too much.

## 5. Scope of the no-go

The conclusion is deliberately narrow.

It **does** rule out the following strategy as a standalone closure of WI-195:

1. take the published all-interval logarithmic `U^2` estimate for `Lambda-Lambda^sharp`;
2. use only the norm bound plus generic Fourier/Hölder inequalities;
3. deduce the diagonal-scale bow variance.

It does **not** rule out:

- a direct shifted-correlation or variance theorem that identifies and cancels the off-diagonal terms rather than bounding them by a norm inequality;
- extra arithmetic information about `Lambda-Lambda^sharp` unavailable to a generic `U^2` argument;
- a genuinely nonlinear transference mechanism adapted to the `U log n` carrier;
- a higher-order Gowers argument with quantitative strength and model matching sufficient for the bow scale.

The last qualification matters. Higher `U^s` norms are compatible with polynomial phases of degree below `s`, so (3) is not a no-go for higher-order uniformity in principle. The published general higher-order theorem is not the same quantitative signed-source `log^{-A}` statement being used in (1), and no claim is made here that every higher-Gowers route has the normalization loss (10).

## 6. Research consequence

The current distinguished-twist clue should therefore continue to target the actual off-diagonal object exposed by WI-195. The useful next information is something that distinguishes the diagonal `K` scale from the generic `K^2` scale: a shift-correlation asymptotic, a direct second-moment theorem, a bilinear spectral estimate, or another identity that retains cancellation across shifts.

More all-interval `U^2` logarithmic saving, by itself, cannot supply that missing power.

## 7. Evidence and novelty audit

- **Primary source verified:** Matomäki--Shao--Tao--Teräväinen, *Higher uniformity of arithmetic functions in short intervals I. All intervals*, arXiv:2204.03754v4 / *Forum Math. Pi* 11 (2023), e29. The `s=2` discussion supplies the quantitative all-interval normalized `U^2` logarithmic saving used in (1).
- **Repository comparison:** WI-195 identifies the bow `L^2` variance gate; WI-329 and WI-331 analyze phase-uniform and all-start nilsequence cancellation and already warn that pointwise logarithmic cancellation has the wrong squared scale. None of those findings audits the stronger `U^2` remark or the exact Fourier/Hölder conversion (4)--(14).
- **Novelty posture:** a targeted current-tree audit located no dedicated finding for this `U^2` shortcut. This is not a priority claim; the substantive contribution here is the exact applicability/barrier audit inside the `weil_inertia` proof program.

**Classification:** the external `U^2` input is `LITERATURE+DERIVED`; equations (3)--(14) are `EXACT-DERIVED`; the research disposition is `DECISIVE-NEGATIVE` for the direct norm-only shortcut.