# WI-331 — all-interval nilsequence control removes distinguished-start exceptionalism below theta 3/16

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT`.

WI-329 shows that on the natural bow source interval

\[
J=X^{1-2\vartheta+o(1)}
\]

the logarithmic carrier at bow height `|U|\ll X^2` is uniformly a fixed-degree polynomial phase up to a power-saving error, but it uses the 2026 *almost-all intervals* theorem and therefore leaves one common exceptional set of source starts. For the lower part of the surviving bow range, that exceptional-start obstruction is already absent in older published prior art.

Let

\[
f_X(n):=\Lambda(n)-\Lambda_X^\sharp(n),
\qquad
\Lambda_X^\sharp(n)
:=\frac{P(R_X)}{\varphi(P(R_X))}\mathbf 1_{(n,P(R_X))=1},
\qquad
R_X:=\exp((\log X)^{1/10}).
\]

Fix

\[
0<\vartheta<\frac{3}{16},
\qquad
\alpha:=1-2\vartheta,
\]

and let `M\asymp X`, `J=X^{\alpha+o(1)}`. Then for every fixed `A,C>0`, for all sufficiently large `X`, **every** such source start `M` satisfies

\[
\boxed{
\sup_{|U|\le C X^2}
\left|
\sum_{1\le j\le J}
 f_X(M+j)
 e\!\left(
 \frac{U}{2\pi}\log\left(1+\frac jM\right)
 \right)
\right|
\ll_{A,C,\vartheta}
J\log^{-A}X.
}
\tag{1}
\]

Equivalently, after multiplication by the harmless unit scalar `M^{iU}`, the same estimate holds for the carrier `(M+j)^{iU}`. Thus a zeta-selected distinguished source start cannot hide in an arithmetic exceptional set for any fixed bow exponent `0<\vartheta<3/16`.

Combining this with WI-202, which already excludes the count-saturating fixed-power bow for every fixed

\[
\vartheta>\vartheta_*:=\frac{3943}{12011},
\]

narrows the range in which **selected-start exceptionalism for this linear-amplitude nilsequence estimate** can remain to

\[
\boxed{
\frac{3}{16}\le \vartheta\le \frac{3943}{12011}.
}
\tag{2}
\]

The qualification in the previous sentence is load-bearing. Equation (1) still does **not** supply the diagonal-scale `L^2` estimate required by WI-195, so it does not by itself exclude a bow, an off-critical zero, or prove RH. The distinguished-twist/off-diagonal clue remains live.

## 1. Published all-interval input

The external theorem is Kaisa Matomäki, Xuancheng Shao, Terence Tao and Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals I. All intervals**, *Forum of Mathematics, Pi* **11** (2023), e29, DOI `10.1017/fmp.2023.28`, arXiv:2204.03754v4.

Their Theorem 1.1(ii) states that if

\[
Y^{5/8+\varepsilon}\le H\le Y^{1-\varepsilon}
\tag{3}
\]

for fixed `\varepsilon>0`, then for every fixed-complexity filtered nilmanifold and Lipschitz test function, and every `A>0`,

\[
\sup_{g\in\operatorname{Poly}(\mathbb Z\to G)}
\left|
\sum_{Y<n\le Y+H}
(\Lambda(n)-\Lambda_Y^\sharp(n))
\overline{F}(g(n)\Gamma)
\right|^*
\ll H\log^{-A}Y.
\tag{4}
\]

The star is a maximal norm over arithmetic progressions inside the interval, so the full interval sum is included. The theorem explicitly notes that polynomial phases `e(P(n))` of any fixed degree are a special case, with the unit circle as nilmanifold. Most importantly here, (4) is an **all-interval** statement: there is no density-one exceptional set of starting points.

The theorem's displayed model uses

\[
R_Y=\exp((\log Y)^{1/10})
\]

in `\Lambda_Y^\sharp`. Remark 1.2 explicitly records flexibility to vary this `R` by a multiplicative factor `\asymp1`. This is enough to match the line's globally fixed `\Lambda_X^\sharp` exactly when the theorem is applied at `Y=M\asymp X`. Indeed, uniformly for `M\in[cX,CX]` with fixed positive `c,C`, the mean-value theorem gives

\[
(\log M)^{1/10}-(\log X)^{1/10}
=O((\log X)^{-9/10}),
\]

and therefore

\[
\frac{R_M}{R_X}
=\exp(O((\log X)^{-9/10}))
=1+o(1).
\tag{5}
\]

So for all large `X`, `R_X` lies inside any fixed multiplicative `\asymp1` window around `R_M`, exactly within the flexibility stated by the authors. No comparison estimate between two different sieve approximants is being assumed.

## 2. The natural bow length enters the `5/8+epsilon` range exactly below 3/16

Set

\[
\alpha=1-2\vartheta.
\]

For fixed `0<\vartheta<3/16`,

\[
\alpha-\frac58
=\frac38-2\vartheta>0,
\qquad
1-\alpha=2\vartheta>0.
\tag{6}
\]

Choose a fixed

\[
0<\varepsilon<rac12
\min\left\{rac38-2\vartheta,\,2\vartheta\right\}.
\tag{7}
\]

Since `M\asymp X` and `J=X^{\alpha+o(1)}`, the `o(1)` exponent can be absorbed into the two fixed gaps in (7), giving for all sufficiently large `X`

\[
M^{5/8+\varepsilon}\le J\le M^{1-\varepsilon}.
\tag{8}
\]

Thus Theorem 1.1(ii) applies at the natural source length for every fixed `0<\vartheta<3/16`. At the endpoint `\vartheta=3/16`, one only has `\alpha=5/8`, and the theorem requires a fixed positive power gap. No endpoint claim is made.

## 3. The bow logarithmic carrier is an admissible polynomial nilsequence

For completeness, the phase reduction from WI-329 can be reused with stronger-than-logarithmic accuracy. Write `n=M+j`, `1\le j\le J`, and choose

\[
d=\left\lceil\frac1\vartheta\right\rceil.
\]

Taylor expansion gives

\[
\log\left(1+\frac jM\right)
=
\sum_{r=1}^{d}
\frac{(-1)^{r+1}}r
\left(\frac jM\right)^r
+O_\vartheta\left((j/M)^{d+1}\right).
\tag{9}
\]

Because `J/M=X^{-2\vartheta+o(1)}` and `|U|\le CX^2`, the phase error after multiplication by `U` is

\[
O_{C,\vartheta}
\left(
X^{2-2\vartheta(d+1)+o(1)}
\right)
=O_{C,\vartheta}(X^{-\delta_\vartheta+o(1)}),
\tag{10}
\]

where

\[
\delta_\vartheta:=2\vartheta(d+1)-2>0.
\]

The Taylor polynomial in (9), multiplied by `U/(2\pi)`, is a real polynomial in `j` of the fixed degree `d`. Theorem 1.1 takes a supremum over all polynomial sequences `g`, so its constant does not depend on the coefficients of this polynomial and hence is uniform throughout `|U|\le CX^2`.

The replacement error is negligible even before using cancellation. Deterministically,

\[
0\le\Lambda(n)\le\log(2X),
\]

and

\[
\frac{P(R_X)}{\varphi(P(R_X))}
=\prod_{p<R_X}\frac p{p-1}
\le
\prod_{2\le m\le \lfloor R_X\rfloor}\frac m{m-1}
\le R_X
=X^{o(1)}.
\tag{11}
\]

Hence

\[
\sum_{j\le J}|f_X(M+j)|
\le JX^{o(1)}.
\tag{12}
\]

Combining (10)--(12), replacing the exact logarithmic carrier by the Taylor polynomial costs

\[
JX^{-\delta_\vartheta+o(1)},
\tag{13}
\]

which is `o(J\log^{-A}X)` for every fixed `A`. Applying (4) with a slightly larger logarithmic saving proves (1).

## 4. Exact consequence for the surviving bow range

WI-202 gives an independent every-center/exponent-pair exclusion for fixed

\[
\vartheta>\frac{3943}{12011}.
\]

For `0<\vartheta<3/16`, (1) now supplies all-start signed nilsequence cancellation at the natural source length. Therefore the specific arithmetic possibility left by WI-327/WI-329 — that the zeta-selected distinguished source lies inside the exceptional set of the available nilsequence theorem — exists only in the intermediate interval (2), with both endpoints genuinely uncovered by the two strict inequalities.

This is a prior-art redirection rather than a new analytic-number-theory theorem. It says that future attempts to de-exceptionalize the **linear-amplitude** signed source do not need a new every-start theorem below `3/16`; one has already been available since 2023. The remaining low-`\vartheta` difficulty is the norm mismatch, not start exceptionalism.

## 5. The WI-195 norm barrier survives unchanged

The target in WI-195 has schematic scale

\[
\int_X^{2X}
\left|
\sum_{x<n\le x+J}
 f_X(n)n^{iU}
\right|^2dx
=o(XJ\log X).
\tag{14}
\]

Even granting the all-start pointwise estimate

\[
\left|\sum f_X(n)n^{iU}\right|
\ll_A J\log^{-A}X,
\]

naive squaring and integration only gives

\[
O_A(XJ^2\log^{-2A}X).
\tag{15}
\]

Relative to the diagonal scale `XJ\log X`, (15) carries the factor

\[
\frac{J}{\log^{2A+1}X}\to\infty
\tag{16}
\]

for every fixed `A`, because `J` is a fixed positive power of `X`. Thus (1) is not the off-diagonal cancellation theorem asked for by the accepted distinguished-twist clue. It also gives no estimate at the exact endpoint `\vartheta=3/16`, no uniform statement as `\vartheta\to0`, and no conclusion about finite or zero-density exceptional zeta zeros.

## 6. Prior-art and novelty audit

Theorem 1.1(ii), the `5/8+\varepsilon` threshold, the polynomial-phase specialization, the sieve approximant, and the multiplicative `R`-flexibility are all established in Matomäki--Shao--Tao--Teräväinen (2023). WI-329 already records this older all-interval threshold in its prior-art section while using the stronger 2026 almost-all theorem at the much shorter `1/3+\varepsilon` scale.

The line-local delta here is narrower: combine WI-329's exact natural-source dictionary `J=X^{1-2\vartheta+o(1)}` and logarithmic-phase reduction with the older all-interval theorem, observe the exact threshold

\[
1-2\vartheta>5/8
\iff
\vartheta<3/16,
\]

match the global `\Lambda_X^\sharp` through the authors' stated `R\asymp R_M` flexibility, and then intersect with WI-202's independent upper cutoff. A bounded fresh search did not locate a published bow/zeta application spelling out this `3/16` transition. **No priority claim is made**: the substantive value is the correction of the live proof-interface map, not novelty of the external theorem.

## Consequence for the line

The source-side frontier splits into two regimes. For fixed `0<\vartheta<3/16`, selected-start exceptionalism is no longer an admissible explanation for failure of linear-amplitude signed cancellation; the unresolved obstruction is the stronger diagonal-scale `L^2` requirement. For `3/16\le\vartheta\le3943/12011`, even the all-start linear-amplitude step is not supplied by this theorem. Any future source theorem should therefore be judged against the correct missing resource in its exponent regime rather than treating the entire surviving bow range as one undifferentiated exceptional-start problem.
