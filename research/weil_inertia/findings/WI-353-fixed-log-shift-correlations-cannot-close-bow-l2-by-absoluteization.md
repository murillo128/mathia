# WI-353 — fixed-log shift correlations cannot close the bow L2 gate by absoluteization

**Status:** `established`

**Claim type:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED + NON-RH`

**One-line statement:** The exact WI-195 sliding-window identity forces any route that bounds the bow off-diagonal shift-by-shift and then takes absolute values to control the *mean absolute twisted residual correlation* at scale
\[
 o\!\left(\frac{X\log X}{K}\right).
\]
At the surviving bow scale `K=X^(1-2*vartheta+o(1))`, this is a genuine power-saving requirement. Consequently, even a hypothetical all-shift twisted analogue of the Matomäki--Radziwiłł--Tao long-shift correlation theorem with arbitrarily strong **fixed logarithmic** savings `O_A(X log^{-A} X)` would still be polynomially too weak. The actual theorem is untwisted and only almost-all in the shift, so it is farther from the WI-195 interface. The live route must retain the signed weighted aggregate, obtain a `K`-dependent power saving, or use genuinely source-specific arithmetic cancellation.

## 1. Exact scale forced by the sliding identity

Let `a_n` denote the source residual used by WI-195; in the intended application
\[
a_n=\Lambda(n)-\Lambda^\sharp(n)
\]
with the same localization as there. For a fixed distinguished twist `U`, put
\[
b_n:=a_n n^{iU}.
\]
For an integer window length `K>=1`, define
\[
V_K(U):=\int_{\mathbf R}
\left|\sum_{x<n\le x+K} b_n\right|^2dx.
\tag{1}
\]
Expanding the square and measuring the set of starts `x` for which two integers at distance `h` lie in the same window gives the exact identity
\[
\boxed{
V_K(U)
=K C_U(0)
+2\Re\sum_{1\le h<K}(K-h)C_U(h),
}
\tag{2}
\]
where
\[
C_U(h):=
\sum_n a_{n+h}\overline{a_n}
\left(\frac{n+h}{n}\right)^{iU}
\tag{3}
\]
with the inherited support restrictions, and
\[
C_U(0)=\sum_n|a_n|^2.
\tag{4}
\]
This is the additive-coordinate version of the same triangular/Gallagher expansion already isolated in WI-195.

The bow target is
\[
V_K(U)=o(XK\log X),
\tag{5}
\]
while WI-195 identifies the diagonal at
\[
K C_U(0)\asymp XK\log X.
\tag{6}
\]
Hence the actual theorem must produce a macroscopic *negative signed* off-diagonal. But suppose instead that one discards those signs and uses only
\[
\left|
\sum_{1\le h<K}(K-h)C_U(h)
\right|
\le
K\sum_{1\le h<K}|C_U(h)|.
\tag{7}
\]
For such an absoluteized route to establish an error `o(XK log X)`, its input must therefore be strong enough to give
\[
\boxed{
\sum_{1\le h<K}|C_U(h)|=o(X\log X).
}
\tag{8}
\]
Equivalently, the required mean absolute correlation scale is
\[
\boxed{
\frac1K\sum_{1\le h<K}|C_U(h)|
=o\!\left(\frac{X\log X}{K}\right).
}
\tag{9}
\]
This is the decisive quantitative gate. It is much stronger than obtaining a logarithmic saving over the natural `X`-scale separately for each shift.

## 2. Fixed logarithmic savings miss by a polynomial factor

To make the comparison maximally favorable to the shift-correlation route, assume a theorem much stronger than the available prior art: for **every** `1<=h<K`, suppose one had the twisted residual estimate
\[
|C_U(h)|\ll_A X\log^{-A}X
\tag{10}
\]
for each fixed `A>0`.

Then (7) yields only
\[
\left|
\sum_{1\le h<K}(K-h)C_U(h)
\right|
\ll_A XK^2\log^{-A}X.
\tag{11}
\]
Relative to the required `XK log X` scale, the bound supplied by this argument is
\[
\frac{XK^2\log^{-A}X}{XK\log X}
=
K\log^{-A-1}X.
\tag{12}
\]
If
\[
K=X^{\kappa+o(1)}
\qquad(\kappa>0),
\tag{13}
\]
then for every fixed `A`
\[
K\log^{-A-1}X\to\infty.
\tag{14}
\]
Thus even **all-shift**, arbitrarily-high-fixed-logarithmic savings do not close the bow gate after absoluteization. This is not a complaint about constants: the missing factor is polynomial.

The exact scale (9) shows what an absoluteized theorem would have to provide. At `K=X^{\kappa+o(1)}` it needs roughly
\[
|C_U(h)|_{\rm mean}
=o(X^{1-\kappa+o(1)}\log X),
\tag{15}
\]
a power saving of order `X^{-kappa}` relative to the natural `X` correlation scale, up to logarithms.

## 3. The surviving bow range makes the mismatch unconditional

For the live count-saturating fixed-power bows retained after WI-202, the natural WI-195 source length is
\[
K=X^{1-2\vartheta+o(1)},
\qquad
0<\vartheta\le\frac{3943}{12011}.
\tag{16}
\]
Therefore
\[
\kappa=1-2\vartheta
\ge
1-\frac{7886}{12011}
=
\boxed{\frac{4125}{12011}}
=0.34343\ldots .
\tag{17}
\]
At the hardest endpoint, (9) already asks for mean absolute residual correlation
\[
o\!\left(X^{7886/12011+o(1)}\log X\right),
\tag{18}
\]
not `X log^{-A} X`. Deeper inside the surviving range, `K` is longer and the absoluteized requirement is stronger still.

This also explains why an `almost all h` theorem is not automatically useful. If the exceptional shifts are treated crudely after taking absolute values, their count itself must be small enough that their total contribution fits inside (8). A set of size `K log^{-A} X` is still polynomially large for every fixed `A`; no fixed logarithmic exceptional-set saving compensates for the factor `K` in (7).

## 4. Prior art: the strongest nearby long-shift theorem is on the wrong scale

Matomäki, Radziwiłł and Tao prove the expected Hardy--Littlewood asymptotic for
\[
\sum_{X<n\le2X}\Lambda(n)\Lambda(n+h)
\]
for all but `O_{A,epsilon}(H log^{-A} X)` shifts in a range of length `H`, provided
\[
X^{8/33+\varepsilon}\le H\le X^{1-\varepsilon},
\tag{19}
\]
with the individual correlation error also `O_{A,epsilon}(X log^{-A} X)` for those good shifts. See K. Matomäki, M. Radziwiłł and T. Tao, **Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges**, *Proc. London Math. Soc.* 118 (2019), 284--350, DOI `10.1112/plms.12181`, Theorem 1.3; arXiv:1707.01315.

The exponent range itself is not the obstruction here. By (17), the natural surviving bow length is polynomially longer than `X^(8/33+epsilon)` for a fixed sufficiently small `epsilon`. The obstruction is the **error scale and aggregation interface**.

Moreover the published theorem controls the ordinary untwisted `Lambda` correlation. The WI-195 object (3) is harder in three independent ways: it contains the `Lambda-Lambda^sharp` residual, an `n`-dependent logarithmic twist, and a prescribed distinguished `U`. The comparison above deliberately grants all three missing bridges and strengthens `almost all h` to `all h`; even then the fixed-logarithmic shiftwise estimate remains too weak after (7). Therefore the conclusion is an a-fortiori no-go for using the existing theorem as a black box through shiftwise absolute values.

The result does **not** say that Matomäki--Radziwiłł--Tao is irrelevant to a future bilinear or signed argument. Its circle-method decomposition or Dirichlet-polynomial estimates may still be reusable before the shift sum is absoluteized. What is closed is the direct route
\[
\text{almost-all / all-shift Hardy--Littlewood with fixed log savings}
\;\Longrightarrow\;
\text{bound each }C_U(h)
\;\Longrightarrow\;
\text{sum absolute values}
\;\Longrightarrow\;
\text{WI-195 }L^2\text{ gate}.
\tag{20}
\]

## 5. Stress test and boundary of the obstruction

The argument is an information-scale barrier, not a lower bound on the true bow variance. Equation (11) is an upper bound that is too large to prove (5); it does not assert that the off-diagonal itself has that size. Signed correlations can cancel strongly, and the entire accepted clue is precisely about whether they do so at the distinguished twist.

The barrier disappears if one has any genuinely stronger input such as:

- a direct signed estimate for the weighted aggregate in (2), without termwise absolute values;
- average absolute control at the exact scale (9), equivalently a `K`-dependent power saving;
- a theorem coupling the shift `h`, the logarithmic carrier, and `Lambda-Lambda^sharp` before Cauchy--Schwarz/triangle inequality;
- an identity forcing negative covariance rather than merely small individual correlations.

It also does not exclude using a correlation theorem inside a decomposition that subsequently recovers signs. The no-go is specifically about **shiftwise control followed by absoluteization**.

A falsification would require an argument deriving (5) from bounds of the form (10) for polynomial `K` while using no additional signed/coupled information. Equations (7)--(14) show that the ordinary triangle-inequality aggregation cannot do this.

## Prior-art and novelty assessment

The triangular correlation identity and the Matomäki--Radziwiłł--Tao theorem are standard/established inputs. No novelty is claimed for either. The durable Mathia delta is their exact scale comparison at the WI-195 bow interface: the natural bow window turns a fixed-log per-shift saving into an `XK^2 log^{-A} X` absoluteized bound, whereas the required scale is `XK log X`, forcing the power-sensitive threshold (9). A bounded audit of the local `weil_inertia` corpus found many closures of one-point nilsequence/Gowers and phase-feature routes (WI-329--WI-352), but no stored finding isolating this shift-correlation aggregation barrier.

## Research consequence

Do not spend further effort trying to close the accepted distinguished-twist clue by importing an almost-all-shift Hardy--Littlewood theorem, or even an all-shift fixed-logarithmic strengthening, and summing the resulting errors absolutely. The next useful arithmetic theorem must interact with the **signed triangular aggregate itself** or achieve a power saving tied to the bow length `K`. This narrows the prior-art search from generic shift asymptotics to genuinely twisted bilinear/dispersion estimates that preserve the sign and the distinguished source parameter.