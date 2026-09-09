# ANF-145 — MRSTT major-arc engine misses bow variance by one full interval length

**Status:** `LITERATURE+DERIVED + EXACT-NORM-BUDGET + NEGATIVE/OBSTRUCTION + SOURCE-SPECIFIC-GATE`. The Matomäki--Radziwiłł--Shao--Tao--Teräväinen almost-all major-arc theorem applies directly to the logarithmic twist `n^{-iU}` in the bow regime `U asymp X^2`, but its quantitative scale is intrinsically too coarse for the variance target isolated in `ANF-102`. This is not merely a loss caused by converting a mean-square estimate to an exceptional-set statement. Inspecting the type-II mean-square estimate used inside the large-`|U|` proof shows the same missing factor before Chebyshev: the available componentwise bound is `K^2` times a logarithmic saving, whereas the bow diagonal is only `K log X` after normalizing by the `x`-length. Thus the current MRSTT architecture misses the required source scale by one full power of the short-interval length `K`. Closing the bow obstruction through this route requires either a diagonal-sensitive type-II estimate with an additional `1/K` gain, or a method that preserves cancellation between arithmetic decomposition pieces instead of bounding them componentwise.

## 1. The bow target is a square-root-scale mean-square problem

Retain the residual and moving logarithmic twist from `ANF-102` and `ANF-144`,

\[
a_X(n)=\Lambda(n)-\Lambda^\sharp(n),
\qquad
S_x(U):=\sum_{x<n\le x+K}a_X(n)n^{-iU},
\tag{1}
\]

with

\[
K=X^{1-2\epsilon+o(1)},
\qquad 0<\epsilon<\frac14,
\qquad U\asymp X^2.
\tag{2}
\]

The moving variance is

\[
V_X(U;K)=\int_X^{2X}|S_x(U)|^2\,dx,
\tag{3}
\]

and `ANF-102` gives the exact diagonal scale

\[
D_X(K)=(1+o(1))XK\log X.
\tag{4}
\]

Therefore the hypothetical bow cancellation requires

\[
V_X(U;K)=o(XK\log X),
\tag{5}
\]

or, after dividing by the `x`-interval length,

\[
\boxed{
\frac1X\int_X^{2X}|S_x(U)|^2\,dx=o(K\log X).
}
\tag{6}
\]

This identifies the natural amplitude scale on a typical interval as

\[
|S_x(U)|\sim\sqrt{K\log X},
\tag{7}
\]

not `K` times a logarithmic saving. Any almost-all theorem used only through pointwise control must therefore reach essentially square-root cancellation in `K`, or replace pointwise control by a genuinely stronger integrated statement.

## 2. The published almost-all theorem cannot close (6), even with no exceptional intervals

Matomäki--Radziwiłł--Shao--Tao--Teräväinen, Theorem 3.1(i), applies for `H>=X^{1/3+epsilon_0}` and every polynomially bounded Archimedean twist `|T|<=X^C`. For `f=Lambda` it gives, for every fixed `A>0`,

\[
\left|
\sum_{x<n\le x+H}
(\Lambda(n)-\Lambda^\sharp(n))n^{-iT}
\right|^*
\le H\log^{-A}X
\tag{8}
\]

outside a set of measure

\[
O_{A,\epsilon_0,C}(X\log^{-A}X).
\tag{9}
\]

The bow parameters satisfy the theorem: choose a fixed `epsilon_0>0` below both `1/6` and the spare exponent in (2), take `H=K`, and take `C>2` so that `U asymp X^2` is allowed.

There are two independent quantitative failures. First, even if the exceptional set in (9) were empty, (8) would yield only

\[
\frac1X\int_X^{2X}|S_x(U)|^2\,dx
\ll K^2\log^{-2A}X.
\tag{10}
\]

Relative to the target scale in (6), the ratio is

\[
\frac{K^2\log^{-2A}X}{K\log X}
=
\frac{K}{\log^{2A+1}X}
\longrightarrow\infty
\tag{11}
\]

for every fixed `A`, because `K` is a fixed positive power of `X`. Thus the good-set amplitude alone is already too large by a polynomial factor.

Second, the exceptional set cannot be discarded trivially either. Since `|a_X(n)|<<log X` on `n asymp X`, one has

\[
|S_x(U)|\ll K\log X.
\tag{12}
\]

If a generic almost-all theorem supplies a good-set bound `|S_x(U)|<=B` outside a measurable set `E`, then the standard good/bad split gives exactly

\[
\boxed{
V_X(U;K)
\ll XB^2+|E|K^2\log^2X.
}
\tag{13}
\]

For this **proof architecture** to make the displayed upper bound `o(XK log X)`, its two nonnegative budgets must satisfy

\[
B=o(\sqrt{K\log X}),
\qquad
|E|=o\!\left(\frac{X}{K\log X}\right),
\tag{14}
\]

unless one replaces the trivial exceptional-set estimate by additional `L^2` information. The published scales `B=K log^{-A}X` and `|E|<<X log^{-A}X` miss both requirements by powers of `K`. This sharpens the qualitative mismatch noted in `ANF-102`: arbitrary logarithmic savings at fixed `A` are in the wrong norm scale.

## 3. The hidden type-II mean square has the same missing power before Chebyshev

A possible escape from Section 2 would be to avoid the published pointwise theorem and use the mean-square estimate from its proof before Chebyshev. The large-`|T|` proof shows that this does not remove the fundamental loss.

MRSTT Lemma 3.5(iii)--(iv) treats a type-II piece

\[
S_x^{II}
:=
\sum_{\substack{x<mn\le x+K\\m\sim M}}a(m)b(n)
\tag{15}
\]

under the Dirichlet-polynomial hypothesis parameterized by `W`. The estimate actually proved before Chebyshev is their equation (3.8):

\[
\boxed{
\frac1X\int_X^{2X}|S_x^{II}|^2\,dx
\ll
K^2\frac{\log^{O_C(1)}X}{W^{3/10}}.
}
\tag{16}
\]

In the large-`|T|` proof of Theorem 3.1 for `f in {mu,Lambda}`, the type-II pieces are fed into this lemma with

\[
W=\log^{100A}X
\tag{17}
\]

for a fixed `A`; the admissible Dirichlet-polynomial smallness comes from the Vinogradov--Korobov input. Consequently (16) yields at best

\[
\frac1X\int_X^{2X}|S_x^{II}|^2\,dx
\ll K^2\log^{-B}X
\tag{18}
\]

for an arbitrarily large but fixed logarithmic exponent `B`, after choosing `A` large enough relative to the fixed divisor bounds. Again

\[
\frac{K^2\log^{-B}X}{K\log X}
=
\frac{K}{\log^{B+1}X}
\longrightarrow\infty.
\tag{19}
\]

So the obstruction survives **before** the exceptional-set extraction. It is not a Chebyshev artifact.

The size of the missing gain can be read directly from (16). To make that componentwise estimate reach the bow source scale `K log X`, one would need

\[
K^2\frac{\log^{O(1)}X}{W^{3/10}}
=o(K\log X),
\tag{20}
\]

hence, up to logarithms,

\[
\boxed{W\gg K^{10/3+o(1)}.}
\tag{21}
\]

This is far outside Lemma 3.5's admissible `W<=X^{epsilon_0/1000}` range in the bow regime, and much farther outside the logarithmic `W` actually available for `Lambda` from the Vinogradov--Korobov input. Equation (21) is not proposed as a new theorem parameter; it is the exact algebraic price that the **existing bound (16)** would have to pay to hit (6).

## 4. The missing object is a diagonal-sensitive type-II variance estimate

The proof of MRSTT Lemma 3.5 makes the same loss visible one level earlier. Their equation (3.10) asks for

\[
\int_{-T}^{T}|A(1+it)B(1+it)|^2\,dt
\ll
\frac{TK}{X}
\frac{\log^{O(1)}X}{W^{3/10}},
\tag{22}
\]

uniformly for `T>=X/K`; the Parseval-type Lemma 3.3 then converts (22) into (16). To reach the bow diagonal through the same conversion, the right-hand side would need, schematically,

\[
\boxed{
\int_{-T}^{T}|A(1+it)B(1+it)|^2\,dt
\ll
\frac{T}{X}\log X
}
\tag{23}
\]

at the relevant decomposition scales, i.e. one full `1/K` improvement over the short-interval factor in (22), modulo the precise coefficient normalizations.

This identifies a sharper source-side gate than “improve the almost-all theorem.” A useful theorem must be **diagonal-sensitive**: it has to see that the full residual `Lambda-Lambda^sharp` has diagonal mass `K log X`, rather than controlling each Heath--Brown/type-II component at the generic `K^2` short-sum scale and then summing absolute errors. Equivalently, it must retain arithmetic cancellation between decomposition pieces, or produce a type-II mean square already normalized to the residual's diagonal.

This boundary is architectural, not a claim that every conceivable use of MRSTT must fail. The full residual could exhibit cancellation between type-I/type-II pieces that componentwise triangle inequalities erase; an exceptional set could have much smaller actual `L^2` mass than its measure and the trivial bound suggest; or a new Dirichlet-polynomial estimate could exploit the distinguished `U asymp X^2` twist more strongly than the uniform theorem does. Any of those would leave the obstruction above.

## 5. Prior-art boundary, stress test, and research consequence

The literature input is exactly the source already anchored in `research/analytic_frontier/SOURCES.md`: Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones Mathematicae* 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`; arXiv:2411.05770. The load-bearing statements are Theorem 3.1(i), Lemma 3.3, Lemma 3.5 and equations (3.8), (3.10), together with the explicit large-`|T|` specialization `W=log^{100A}X` for `mu` and `Lambda`. The same paper explicitly treats `n^{-iT}` for polynomially large `T`, so no Taylor replacement of the bow logarithmic phase is needed for this audit. No new source anchor is required.

The falsification checks are quantitative. Equation (11) only uses that `K=X^{kappa+o(1)}` for some fixed `kappa>0`; equation (14) follows from the exact nonnegative good/bad decomposition; equations (19)--(21) are direct substitutions into MRSTT's pre-Chebyshev mean square. If a stronger estimate hidden elsewhere in the same architecture removed the `K^2` scale for the **Lambda residual itself**, rather than for a different arithmetic function such as `d_2`, it would supersede this finding. The current paper in fact illustrates the distinction: it records power-saving discorrelation for `d_2`, while the `Lambda` major-arc input remains logarithmic.

For the analytic-frontier program, `ANF-144` localized any robust bow resonance to an absolute `O(X)` twist window. The present finding now removes a tempting source-side shortcut inside that window: simply importing the strongest available almost-all `Lambda-Lambda^sharp` major-arc theorem, or its type-II mean-square estimate before Chebyshev, still leaves one complete power of `K` unaccounted for. The next useful target is therefore an `L^2` theorem at the diagonal scale `K log X` for the distinguished logarithmic twist, preferably formulated directly for the full residual so that the cancellation discarded by Heath--Brown componentwise bounds remains visible.