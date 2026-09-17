# WI-329 — phase-uniform nilsequence control covers the natural bow dephasing scale

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

WI-328 leaves a tempting escape from the endpoint cubic obstruction: move from the twist-frozen `X^{1/3}` block to the longer natural source interval `J\asymp X/H_{\rm bow}`, where the bow's vertical span can produce order-one phase motion, and then try to use the many bow heights as genuinely different twists against the signed source

\[
f_X(n):=\Lambda(n)-\Lambda_X^\sharp(n).
\]

At every fixed surviving bow exponent, the existing 2026 almost-all nilsequence theorem already reaches exactly that longer scale — and it does so **uniformly over all fixed-degree polynomial phases on one common good set of starts**. The logarithmic Archimedean carrier `n^{iU}` on a natural bow source interval is, uniformly for the whole bow `U\asymp X^2`, a fixed-degree polynomial phase up to a power-saving error. Consequently, for every fixed

\[
0<\vartheta\le \vartheta_*:=\frac{3943}{12011},
\qquad
\alpha:=1-2\vartheta,
\tag{1}
\]

and every natural source length

\[
J=X^{\alpha+o(1)},
\tag{2}
\]

there is, for each fixed `A>0`, an exceptional set of only

\[
O_{A,\vartheta}(X\log^{-A}X)
\tag{3}
\]

integer starts `M\in[X,3X/2]` outside which

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
J\log^{-A}X
}
\tag{4}
\]

for every fixed `C>0` (after restricting (2) to any fixed asymptotic representative of the natural length, or a fixed polylogarithmic modification of it). Crucially, the exceptional set in (3) is **independent of `U`**: the source theorem takes a supremum over all polynomial nilsequences before declaring the starting point good.

Thus bow-height dephasing does not turn the published almost-all theorem into many independent chances to escape the WI-327 exceptional locus. At the first dephasing scale from WI-328,

\[
\alpha_*=1-2\vartheta_*
=\frac{4125}{12011}
=0.343435\ldots,
\tag{5}
\]

the theorem already supplies phase-uniform density-one cancellation because

\[
\alpha_* - \frac13
=\frac{364}{36033}>0.
\tag{6}
\]

But a distinguished bow start may still lie in the one common exceptional set. This therefore closes the naive route

\[
\text{long enough source window}
+\text{bow-height dephasing}
+\text{existing almost-all phase theorem}
\Longrightarrow
\text{de-exceptionalization of the distinguished start}.
\]

The conclusion is deliberately narrower than the full WI-195 `L^2` gate. Equation (4) controls macroscopic signed resonance of an individual short sum on density-one starts; even an all-start bound of size `J\log^{-A}X` would still be too weak, after squaring and integrating, to supply the diagonal-scale variance `o(XJ\log X)` required by WI-195. No bow, off-critical zero, or RH consequence is proved here.

## 1. The natural dephasing interval lies inside the published `1/3+epsilon` range

For a fixed surviving count-saturating bow exponent `\vartheta`, WI-195 and WI-328 give

\[
H_{\rm bow}=X^{2\vartheta+o(1)},
\qquad
J_{\rm nat}:=\frac{X}{H_{\rm bow}}
=X^{1-2\vartheta+o(1)}.
\tag{7}
\]

(The suppressed logarithmic factor in the exact `T`-normalization is `X^{o(1)}` and is harmless for every fixed exponent comparison below.) Since `\vartheta\le\vartheta_*`,

\[
1-2\vartheta
\ge
1-2\vartheta_*
=\frac{4125}{12011}
>rac13.
\tag{8}
\]

For each fixed `\vartheta>0`, one also has `1-2\vartheta<1`. Hence one can choose a fixed `\varepsilon_\vartheta>0` such that

\[
\frac13+\varepsilon_\vartheta
<1-2\vartheta
<1-\varepsilon_\vartheta.
\tag{9}
\]

Matomäki--Radziwiłł--Shao--Tao--Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Invent. Math. 244 (2026), Theorem 1.1(ii), applies throughout exactly this regime. For any fixed-degree filtered nilmanifold and fixed Lipschitz test function, it gives outside a set of real starts of measure `O_A(X\log^{-A}X)`

\[
\sup_{g\in\operatorname{Poly}(\mathbb Z\to G)}
\left|
\sum_{x<n\le x+J}
(\Lambda(n)-\Lambda_X^\sharp(n))
\overline{F}(g(n)\Gamma)
\right|^*
\le
J\log^{-A}X.
\tag{10}
\]

The order of quantifiers in (10) is the load-bearing point: one exceptional set controls the supremum over **all** polynomial sequences `g`. Polynomial phases `e(P(n))` of any prescribed fixed degree are explicitly included as a special case of the theorem.

At the largest surviving exponent there is still a fixed margin. Equation (6) gives about `0.01010` above the `1/3` threshold, so for example any theorem parameter `\varepsilon<364/36033` is admissible at power scale. The proposed longer-window escape from WI-328 therefore does not fall into an uncovered sliver between the cubic block and the published nilsequence range.

## 2. The logarithmic bow carrier is a fixed-degree polynomial phase on its natural interval

Fix `\vartheta>0` and put `\alpha=1-2\vartheta`. Let `M\asymp X`, `1\le j\le J=X^{\alpha+o(1)}`, and `|U|\le C X^2`. Choose

\[
d:=\left\lceil\frac1\vartheta\right\rceil.
\tag{11}
\]

Since `j/M=X^{-2\vartheta+o(1)}=o(1)`, Taylor's formula for the logarithm gives

\[
\log\left(1+\frac jM\right)
=
\sum_{r=1}^{d}
\frac{(-1)^{r+1}}{r}
\left(\frac jM\right)^r
+R_{d+1}(j/M),
\tag{12}
\]

with, uniformly on the present interval,

\[
|R_{d+1}(j/M)|
\ll_d
\left(\frac jM\right)^{d+1}.
\tag{13}
\]

Multiplying by `U`,

\[
|U R_{d+1}|
\ll_{C,d}
X^{2-2\vartheta(d+1)+o(1)}.
\tag{14}
\]

By (11),

\[
\delta_\vartheta
:=2\vartheta(d+1)-2
>0,
\tag{15}
\]

so (14) is `O(X^{-\delta_\vartheta+o(1)})`. Define the polynomial in `n`

\[
P_{M,U}(n)
:=
\frac{U}{2\pi}
\sum_{r=1}^{d}
\frac{(-1)^{r+1}}{r}
\left(\frac{n-M}{M}\right)^r.
\tag{16}
\]

Then, uniformly for every `M,j,U` above,

\[
 e\!\left(
 \frac{U}{2\pi}\log\left(1+\frac jM\right)
 \right)
=
e(P_{M,U}(M+j))
+O_{C,\vartheta}(X^{-\delta_\vartheta+o(1)}).
\tag{17}
\]

The degree `d` may be large when `\vartheta` is small, but it is fixed once the bow exponent is fixed, exactly the quantifier allowed in Theorem 1.1.

## 3. The approximation error is negligible even on exceptional arithmetic coefficients

No density-one coefficient norm is used to pass from (10) to the exact logarithmic phase. Deterministically, for `n<2X` one has

\[
0\le\Lambda(n)\le\log(2X),
\tag{18}
\]

while, with `R=\exp((\log X)^{1/10})`, the elementary product estimate used in WI-328 gives

\[
0\le\Lambda_X^\sharp(n)
\le \frac{P(R)}{\varphi(P(R))}
\le R
=X^{o(1)}.
\tag{19}
\]

Hence

\[
\sum_{j\le J}|f_X(M+j)|
\le
J\bigl(\log(2X)+R\bigr)
=JX^{o(1)}.
\tag{20}
\]

Combining (17) and (20), replacing the exact logarithmic carrier by the degree-`d` polynomial phase costs only

\[
JX^{-\delta_\vartheta+o(1)},
\tag{21}
\]

which is smaller than `J\log^{-A}X` for every fixed `A` once `X` is sufficiently large. Apply Theorem 1.1(ii) with a larger logarithmic saving, say `2A`, and absorb (21). This proves the real-start version of (4), uniformly in all `|U|\le C X^2`.

The uniformity in `U` does **not** come from Theorem 3.1's Archimedean estimate, whose statement fixes `T`. It comes from the stronger nilsequence theorem: after the fixed-degree polynomial reduction, Theorem 1.1(ii) already takes the supremum over every possible polynomial phase coefficient tuple. This distinction is what prevents one from treating neighboring bow ordinates as independent applications with unrelated good sets.

## 4. The exceptional-set statement transfers to integer starts

Take `J` integer. If an integer start `M` violates (4), choose a witnessing height `U` and its polynomial `P_{M,U}` from (16). For every real

\[
M<x<M+1,
\]

the integers in `(x,x+J]` are exactly `M+1,\ldots,M+J`. Because the supremum in (10) contains `P_{M,U}`, the same violation (up to the power-saving approximation error already absorbed above) occurs for every such `x`. Thus the whole unit interval `(M,M+1)` must lie in the real exceptional set.

These unit intervals are disjoint. Therefore an exceptional set of real measure `O_A(X\log^{-A}X)` contains at most

\[
O_A(X\log^{-A}X)
\tag{22}
\]

bad integer starts. This is the same exact real-to-integer transfer used in WI-327, but now the good integer set is simultaneously good for **all bow heights** at the natural dephasing length.

## 5. What the phase-uniform exceptional set closes

WI-328 proves that an `X^{1/3}` endpoint block is twist-frozen across every surviving bow and identifies the first scale at which order-one bow-height motion can appear:

\[
J\gtrsim X^{1-2\vartheta}.
\tag{23}
\]

Equation (7) shows that this is also the natural multiplicative Gallagher length of WI-195. It was therefore reasonable to hope that moving to (23) would make the many bow ordinates behave like many separate twisted short-interval tests.

Equations (4) and (10) show why the existing almost-all theorem does not provide that leverage. On every good start it already certifies **all** the relevant polynomialized heights at once. Conversely, if the distinguished start lies in the permitted exceptional set, the theorem gives no information at any of those heights. Phase dephasing changes the values of the sums; it does not split the arithmetic exceptional locus into independent sets that can be beaten by sampling more ordinates.

This is a stronger route closure than the cubic twist-freezing statement alone:

- WI-328 says the short cubic block cannot dephase enough;
- the present result says that after moving to the first scale where it *can* dephase, the strongest directly matching almost-all nilsequence theorem is already phase-uniform and leaves one common exceptional-start obstruction.

Therefore the live issue is not to obtain more Archimedean phase diversity from the same distinguished start. A successful use of the 2026 arithmetic input still needs a separate mechanism proving that the source-compatible start cannot belong to its exceptional set, forcing many sufficiently separated **source starts** rather than merely many heights, or coupling the full WI-195 `L^2` object to information stronger than linear-amplitude almost-all discorrelation.

## 6. Norm barrier and evidence boundary

The result must not be confused with a solution of the accepted distinguished-twist clue. WI-195's exact triangular identity requires a diagonal-scale variance estimate of the schematic size

\[
\int_X^{2X}
\left|
\sum_{x<n\le x+J}
 f_X(n)n^{iU}
\right|^2dx
=o(XJ\log X).
\tag{24}
\]

A pointwise good-set estimate `J\log^{-A}X`, even if granted on **all** starts, yields after naive squaring an upper scale `XJ^2\log^{-2A}X`, whose ratio to the target diagonal scale is

\[
\frac{J}{\log^{2A+1}X}\to\infty
\tag{25}
\]

for every fixed `A`. This is exactly the polynomial norm gap already isolated by WI-195. The present finding therefore closes only the de-exceptionalization strategy based on generating many twists at one start; it does not upgrade the theorem to the square-root-scale variance needed by the Weil/BOW covariance.

Likewise, (4) says nothing about what happens on the exceptional starts. It does not show that the distinguished source start is good, that the signed source is small pointwise there, or that an off-critical zero cannot exist.

## 7. Prior-art and novelty audit

The load-bearing external input is established prior art, not a new theorem of this line:

Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones Mathematicae* 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`, arXiv:2411.05770. Theorem 1.1(ii) gives the `1/3+\varepsilon` almost-all bound with a supremum over all bounded-complexity polynomial nilsequences before the exceptional set is declared. The paper explicitly notes that polynomial phases of any fixed degree are special cases. Section 1.1 also records the older all-interval nilsequence threshold `5/8+\varepsilon` for `\Lambda-\Lambda^\sharp`; no pointwise theorem at the natural exponent (5) is supplied there.

The relevant line-local antecedents are WI-190 (an almost-all theorem may hide an entire deterministic B-process alias locus), WI-195 (the exact multiplicative Gallagher `L^2` gate and its norm mismatch with linear-amplitude estimates), WI-327 (generic cubic signed cancellation but a surviving exceptional source start), and WI-328 (bow heights are frozen on the cubic block and first dephase only at `J\gtrsim X^{1-2\vartheta}`). None of those combines the exact dephasing length with the **phase supremum already built into Theorem 1.1(ii)** or proves the uniform logarithmic-to-polynomial reduction (12)--(21).

A bounded fresh audit of the 2026 paper and its 2023 all-interval predecessor found no theorem that removes the exceptional start at the natural surviving-bow lengths, and the 2026 authors themselves describe `5/8+\varepsilon` as the best known all-interval nilsequence range for `\Lambda` in their literature discussion. This negative search is not a priority claim.

The new line-local content is the exact scale synthesis: every fixed surviving bow's first natural dephasing window already lies in the `1/3+\varepsilon` theorem range; the exact logarithmic twist polynomializes with power-saving error at a fixed degree depending only on the bow exponent; and the theorem's phase supremum makes the resulting density-one good set common to the entire bow. The status is therefore `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

## Research consequence

Do not pursue the post-WI-328 route by merely lengthening the source block to `X/H_{\rm bow}` and applying the existing almost-all nilsequence theorem separately at many bow ordinates. At that scale the theorem can already be applied **simultaneously** to all those polynomialized twists, and its only remaining qualitative freedom is exactly the one we cannot tolerate: the distinguished source start may belong to the common exceptional set.

The next source-side advance must change that quantifier or the norm. Concretely, it must provide pointwise/all-start signed control at the source-compatible start, force the bow to interrogate sufficiently many genuinely distinct source starts whose geometry cannot all fit in the exceptional locus, or prove a square-root/diagonal-scale variance estimate strong enough to enter the exact WI-195 `L^2` bridge. More height samples at one start are not a substitute.