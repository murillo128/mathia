# ANF-165 — a fixed Cramer-Granville gauge restores arbitrary-log endpoint discorrelation and forces super-polylogarithmic completion migration

**Status:** `LITERATURE+DERIVED + FIXED-APPROXIMANT-GAUGE + ARBITRARY-LOG-ENDPOINT-DISCORRELATION + SUPER-POLYLOG-REPULSION`. `ANF-164` obtains source-specific cancellation for the actual bow residual at every distinguished height `U asymp X^2`, but its symmetric two-endpoint estimate loses one power of `log X` when it compares the globally fixed rough model `Q_X` with the locally normalized approximant `Q_Y`. That comparison is not necessary. Remark 1.2 of Matomäki--Shao--Tao--Teräväinen explicitly allows the Cramer--Granville cutoff `R` in `Lambda^sharp` to vary by a multiplicative factor `asymp 1`. Across all bow endpoint locations `Y in [X,3X]`, the canonical cutoffs satisfy

\[
\frac{R_X}{R_Y}=1+O((\log X)^{-9/10}),
\qquad
R_Z:=\exp((\log Z)^{1/10}).
\]

Thus the all-interval theorem may be applied at the local base point `Y` while choosing the **same** cutoff `R=R_X` used by the bow source normal form. The resulting approximant is exactly `Q_X`, so the `Q_Y-Q_X` mismatch disappears and arbitrary fixed logarithmic saving survives at both endpoints.

In the bow regime

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac1{16},
\qquad
A X^2\le U\le B X^2,
\]

write

\[
T_{\rm bow}:=XK\log X,
\qquad
R_{\rm TV}:=T_{\rm bow}^{1/3}.
\]

Then for **every fixed `C>=0`**,

\[
\boxed{
E_{\partial,\,r\le R_{\rm TV}(\log X)^C}
=o(XK\log X)
}
\]

uniformly in the distinguished height window. Hence, if the total endpoint completion has macroscopic bow scale along a sequence of `X`, its cumulative-square energy must escape beyond `R_TV (log X)^C` for every fixed `C`: the surviving endpoint obstruction is forced to migrate by more than any fixed polylogarithmic factor beyond the sharp coefficient-mass onset. This strengthens `ANF-164`, which reached only `C<2/3`, while leaving the `epsilon=1/16` activation boundary unchanged.

## 1. One global Cramer cutoff is admissible at every bow endpoint

Retain the source normal form of `ANF-149`, `ANF-163`, and `ANF-164`,

\[
r_X(n)=\vartheta(n)-Q_X(n),
\qquad
Q_X(n)=c_X1_{(n,P(R_X))=1},
\qquad
c_X:=\frac{P(R_X)}{\varphi(P(R_X))},
\tag{1}
\]

with

\[
R_X=\exp((\log X)^{1/10}).
\tag{2}
\]

Let `Y in [X,3X]` be the left endpoint of any physical interval used in a left or right bow endpoint prefix/suffix. If Theorem 1.1(ii) of Matomäki--Shao--Tao--Teräväinen is applied with local large parameter `Y`, its displayed default approximant uses

\[
R_Y=\exp((\log Y)^{1/10}).
\tag{3}
\]

The mean-value theorem gives, uniformly for `Y in [X,3X]`,

\[
(\log Y)^{1/10}-(\log X)^{1/10}
=O((\log X)^{-9/10}),
\tag{4}
\]

because `log(Y/X)=O(1)`. Therefore

\[
\boxed{
\frac{R_X}{R_Y}
=\exp(O((\log X)^{-9/10}))
=1+O((\log X)^{-9/10}).
}
\tag{5}
\]

Remark 1.2 of the same paper states that, in the `Lambda-Lambda^sharp` case of equation (1.6), one can certainly vary the parameter `R` in the Cramer--Granville approximant by a multiplicative factor `asymp 1`. Equation (5) lies strictly inside that admitted flexibility. Consequently, when applying Theorem 1.1(ii) at base point `Y`, choose `R=R_X` rather than the displayed default `R_Y`. The theorem's approximant is then exactly

\[
\Lambda^\sharp_{Y;R_X}(n)
=\frac{P(R_X)}{\varphi(P(R_X))}1_{(n,P(R_X))=1}
=Q_X(n).
\tag{6}
\]

No comparison between `Q_X` and `Q_Y` is needed.

Fix `eta>0`. For intervals `I=(Y,Y+H] subset [X,3X]` with

\[
X^{5/8+\eta}\le H\le X^{2/3+o(1)},
\tag{7}
\]

the constant-factor relation `Y asymp X` lets one decrease `eta` slightly and place `H` in the hypotheses of Theorem 1.1(ii) with large parameter `Y`. Its maximal form therefore gives, for every fixed `A_0>0` and every fixed-degree polynomial phase `e(P(n))`,

\[
\boxed{
\left|
\sum_{n\in I}(\Lambda(n)-Q_X(n))e(P(n))
\right|
\ll_{A_0,\eta,P}
H(\log X)^{-A_0}.
}
\tag{8}
\]

Here the dependence indicated by `P` is only through a fixed degree/complexity class; the polynomial coefficients themselves may vary with the interval and with `X`, exactly as in Theorem 1.1(ii).

This is the point missed by the normalization route of `ANF-164`: its estimate

\[
\sum_{n\in I}|Q_X(n)-Q_Y(n)|\ll H/\log X
\]

is a valid `L^1` comparison, but it need not be inserted into the discorrelation argument at all. The external theorem already permits the globally fixed gauge required by the bow residual.

## 2. The exact logarithmic twist inherits arbitrary log saving at both endpoints

Let

\[
A X^2\le U\le B X^2
\tag{9}
\]

for fixed `0<A<B<infinity`. On an interval `I=(Y,Y+H]` in (7), `ANF-164` Taylor-expands `log(Y+j)` through degree six and obtains a real polynomial `P_{Y,U}` of degree at most six such that

\[
n^{-iU}
=e(P_{Y,U}(n))+O(X^{-1/3+o(1)})
\tag{10}
\]

uniformly for `n in I`. The same derivation applies here unchanged because every scale used below remains `H<=X^{2/3+o(1)}`.

Apply (8) to `P_{Y,U}`. The replacement error in (10) is harmless: the local total-variation estimate from `ANF-163`, together with the identical prime/rough upper-bound-sieve calibration used there, gives

\[
\sum_{n\in I}\bigl(\Lambda(n)+Q_X(n)\bigr)\ll_\eta H,
\tag{11}
\]

so the phase replacement costs at most

\[
H X^{-1/3+o(1)}
=o_{A_0}(H\log^{-A_0}X)
\tag{12}
\]

for every fixed `A_0`. Finally,

\[
r_X=(\Lambda-Q_X)-(\Lambda-\vartheta),
\tag{13}
\]

and the second term is supported on prime powers `p^k`, `k>=2`. As in `ANF-164`, on every interval in (7) its total Mangoldt mass is

\[
O(HX^{-1/2}\log X+\log^2X)
=o_{A_0}(H\log^{-A_0}X).
\tag{14}
\]

Combining (8)--(14) yields the symmetric endpoint estimate

\[
\boxed{
\left|
\sum_{n\in I}r_X(n)n^{-iU}
\right|
\ll_{A_0,\varepsilon,A,B}
H\log^{-A_0}X
}
\tag{15}
\]

for **every fixed `A_0>0`**, uniformly in both endpoint location `Y in [X,3X]` and distinguished height (9), whenever (7) holds. In particular, the right endpoint now has the same arbitrary-log strength that `ANF-164` already observed at the left endpoint.

The maximal form of the literature theorem is stronger than needed here; ordinary contiguous endpoint prefixes and suffixes are among its allowed subprogressions.

## 3. Every fixed polylogarithmic enlargement of the cubic onset is negligible

Retain the exact endpoint completion from `ANF-157`,

\[
E_\partial(b)
=
\sum_{r=1}^{K-1}|S_r^-|^2
+
\sum_{r=1}^{K-1}|S_r^+|^2,
\qquad
b_n=r_X(n)n^{-iU}.
\tag{16}
\]

The bow target and total-variation onset are

\[
T_{\rm bow}=XK\log X,
\qquad
R_{\rm TV}=T_{\rm bow}^{1/3}
=X^{2/3-2\varepsilon/3+o(1)}(\log X)^{1/3}.
\tag{17}
\]

Fix an arbitrary constant `C>=0` and set

\[
R_-:=\frac{R_{\rm TV}}{\log X},
\qquad
R_C:=R_{\rm TV}(\log X)^C.
\tag{18}
\]

When `0<epsilon<1/16`,

\[
\frac23-\frac{2\varepsilon}{3}-\frac58
=\frac{1-16\varepsilon}{24}>0.
\tag{19}
\]

Hence every `r in [R_-,R_C]` lies above `X^{5/8+eta_epsilon}` for some fixed `eta_epsilon>0` and all sufficiently large `X`. Also

\[
R_C=X^{2/3-2\varepsilon/3+o(1)}<X^{2/3+o(1)},
\tag{20}
\]

so the degree-six logarithmic approximation remains valid throughout that range.

For `r<R_-`, the source-specific total-variation estimate of `ANF-163` gives

\[
E_{\partial,\,r<R_-}
\ll R_-^3+X^{3/4}\log^2X
=o(T_{\rm bow}).
\tag{21}
\]

For `R_-<=r<=R_C`, apply (15) with a fixed `A_0` chosen after `C`. Then

\[
\begin{aligned}
E_{\partial,\,R_-\le r\le R_C}
&\ll
\log^{-2A_0}X
\sum_{r\le R_C}r^2 \\
&\ll
\frac{R_C^3}{\log^{2A_0}X} \\
&=
T_{\rm bow}(\log X)^{3C-2A_0}.
\end{aligned}
\tag{22}
\]

Taking, for example, `A_0>3C/2+1` makes (22) `o(T_bow)`. Together with (21),

\[
\boxed{
E_{\partial,\,r\le R_{\rm TV}(\log X)^C}
=o(XK\log X)
\qquad
\text{for every fixed }C\ge0.
}
\tag{23}
\]

This strictly improves the `C<2/3` boundary in `ANF-164`. The earlier exponent `2/3` came only from squaring the avoidable one-log `Q_X-Q_Y` comparison; it is not a genuine arithmetic threshold of the all-interval theorem.

A useful contrapositive is immediate. If for some fixed `delta>0`

\[
E_\partial\ge\delta XK\log X
\tag{24}
\]

along an unbounded sequence of `X`, then for every fixed `C>=0`,

\[
\sum_{r>R_{\rm TV}(\log X)^C}
\bigl(|S_r^-|^2+|S_r^+|^2\bigr)
\ge (\delta-o(1))XK\log X.
\tag{25}
\]

Thus any macroscopic endpoint completion is forced into scales whose ratio to `R_TV` eventually exceeds every fixed power of `log X`. In this precise sense the surviving obstruction is **super-polylogarithmically displaced** from the sharp coefficient-mass onset.

## 4. What remains after the gauge correction

Equation (23) does **not** close the full bow endpoint term. The remaining geometric range is polynomially larger than `R_TV`:

\[
\frac{K}{R_{\rm TV}}
=
X^{(1-4\varepsilon)/3+o(1)}(\log X)^{-1/3},
\tag{26}
\]

which is a positive power of `X` throughout `0<epsilon<1/4`. Arbitrary fixed powers of logarithmic saving cannot absorb the `R^3` growth of the cumulative-square envelope over a fixed-power enlargement `R=R_TV X^delta`. Therefore the new gauge choice removes a normalization artifact but does not manufacture the genuinely power-saving arithmetic input identified as the next gate in `ANF-164`.

Nor does it improve the activation threshold `epsilon=1/16`. At `epsilon=1/16`, `R_TV=X^{5/8+o(1)}` and the all-interval theorem still requires a fixed positive exponent margin above `5/8`; multiplying by any fixed power of `log X` cannot create that margin. For `epsilon>1/16`, the sharp coefficient-mass onset lies below the theorem's all-interval range.

`ANF-164` itself remains valid. Its `H/log X` right-endpoint estimate is a correct consequence of directly comparing `Q_X` and `Q_Y`; `ANF-165` shows only that this comparison is an avoidable proof route because the source theorem admits a fixed global Cramer gauge.

### Perturbation resilience

The argument is insensitive to replacing `R_X` by any common cutoff `\widetilde R_X` whose ratio to every local default `R_Y`, `Y in [X,3X]`, stays in a fixed compact subset of `(0,infinity)` and for which the Cramer--Granville approximant remains within the flexibility stated in Remark 1.2. The exact choice `R_X=exp((log X)^(1/10))` is retained because it is the canonical bow source normalization.

The degree-six Taylor step is tied to `U=O(X^2)` and endpoint scales `H<=X^(2/3+o(1))`. Faster-growing twists or polynomially longer endpoint windows would require a fresh approximation-degree audit rather than automatic reuse of (10).

### Prior-art audit and provenance

The load-bearing external source is Kaisa Matomäki, Xuancheng Shao, Terence Tao and Joni Teräväinen, *Higher uniformity of arithmetic functions in short intervals I. All intervals*, Forum of Mathematics, Pi 11 (2023), e29, DOI `10.1017/fmp.2023.28`, arXiv:2204.03754. Theorem 1.1(ii) supplies maximal all-interval discorrelation for `Lambda-Lambda^sharp` with arbitrary fixed logarithmic saving above exponent `5/8`; its displayed equation (1.1) defines the Cramer--Granville approximant, and Remark 1.2 explicitly records the multiplicative-factor flexibility in the cutoff `R`. This paper is already registered in `research/analytic_frontier/SOURCES.md` by `ANF-164`.

The new claim is not a new nilsequence estimate. It is the line-specific observation that the theorem's own approximant flexibility lets both bow endpoints use the **same globally fixed source gauge**, eliminating the normalization loss introduced in `ANF-164`, and the consequent integration of the restored arbitrary-log estimate through the exact endpoint square function (16).

Local dependencies are `ANF-149` for the bow source normal form, `ANF-157` for the exact Fejer-minus-endpoint-completion identity, `ANF-163` for the local total-variation envelope and cubic onset, and `ANF-164` for the degree-six logarithmic-twist reduction and the all-interval activation threshold.

### Scope and non-claim

This finding proves only the endpoint square-function localization (23) for the actual residual in the stated bow regime. It does not prove `E_partial=o(XK log X)` over all `r<K`, does not establish the downstream Weil-Inertia coercive conclusion, and does not claim a new result about primes independently of the bow normalization. It also does not convert the 2026 almost-all interval theorem into an all-interval statement.

### Falsification boundary

The result would fail if the cutoff flexibility in Remark 1.2 did not apply uniformly to comparable Cramer--Granville parameters in Theorem 1.1(ii), if `R_X/R_Y` were not uniformly comparable over the two bow endpoint locations, if polynomial-phase uniformity did not allow the interval-dependent degree-six coefficients, or if the exact source residual used a cutoff not representable by the permitted Cramer--Granville approximant. Equation (5) and the published remark settle the first geometric compatibility in the present regime; no RH, Lindelof hypothesis, pair-correlation conjecture, or almost-all-to-all upgrade is used.

### Next gate

For `epsilon<1/16`, the remaining task is now genuinely **power-scale**, not logarithmic: control the aggregate endpoint square function after it has migrated beyond every fixed polylogarithmic enlargement of `R_TV`. A useful theorem would either give power saving for the exact distinguished logarithmic twist on endpoint intervals `R=R_TV X^delta`, or exploit cancellation directly in the cumulative-square aggregate so that a pointwise `R^3` envelope is no longer the governing loss. For `epsilon>=1/16`, the separate gate remains an all-interval source theorem below exponent `5/8` (or another mechanism reaching the cubic onset without such a theorem).