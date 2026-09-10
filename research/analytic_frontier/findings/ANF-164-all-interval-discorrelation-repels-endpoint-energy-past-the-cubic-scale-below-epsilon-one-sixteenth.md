# ANF-164 — all-interval discorrelation repels endpoint energy past the cubic scale below epsilon one-sixteenth

**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC-TWIST-CANCELLATION + ENDPOINT-SQUARE-FUNCTION-REPULSION + RANGE-BOUNDARY`. `ANF-163` shows that coefficient mass alone cannot rule out bow-scale endpoint completion: a triangular synthetic control can place `Theta(X K log X)` cumulative-square energy at the cubic total-variation scale

\[
R_{\rm TV}:=(XK\log X)^{1/3}.
\]

The all-interval nilsequence theorem of Matomäki--Shao--Tao--Teräväinen supplies the first source-specific cancellation strong enough to exclude the actual prime-minus-rough residual from saturating that control at its natural onset. In the bow regime

\[
K=X^{1-2\varepsilon+o(1)},\qquad 0<\varepsilon<\frac1{16},
\]

and at every distinguished height `U asymp X^2`, the exact logarithmic twist can be replaced on endpoint intervals of length `R <= X^(2/3+o(1))` by a fixed degree-six polynomial phase with power-small error. The all-interval theorem then gives arbitrary logarithmic saving for `Lambda-Lambda^sharp`. A separate scale-freezing lemma compares the theorem's local `Lambda^sharp` to the globally fixed rough model `Q_R` used by the bow source normal form, losing only one power of `log X` uniformly across both endpoints. Consequently, for every fixed `beta<2/3`,

\[
\boxed{
E_{\partial,\,r\le R_{\rm TV}(\log X)^\beta}
=o(XK\log X).
}
\]

Thus a macroscopic endpoint completion cannot live at the sharp coefficient-mass scale or at any fixed polylogarithmic enlargement smaller than `(log X)^(2/3)`. The threshold `epsilon=1/16` is intrinsic to this particular synthesis: `R_TV` lies above the all-interval `X^(5/8+eta)` theorem exactly when `epsilon<1/16`. This does **not** close the full bow endpoint term; energy can still migrate to longer prefixes, and logarithmic discorrelation alone cannot exclude a fixed power enlargement of `R_TV`.

## 1. The cubic endpoint scale crosses the all-interval theorem exactly at epsilon one-sixteenth

Retain the exact source normal form and endpoint notation of `ANF-149`, `ANF-157`, and `ANF-163`. Thus

\[
r_X(n)=\vartheta(n)-Q_X(n),
\qquad
Q_X(n):=c_X1_{(n,P(R_X))=1},
\tag{1}
\]

where

\[
R_X:=\exp((\log X)^{1/10}),
\qquad
c_X:=\frac{P(R_X)}{\varphi(P(R_X))},
\tag{2}
\]

and the endpoint coefficients are

\[
b_n=r_X(n)n^{-iU},
\qquad
A X^2\le U\le B X^2
\tag{3}
\]

for fixed `0<A<B<infinity`. The exact endpoint completion is a sum of squared left and right cumulative sums,

\[
E_\partial
=
\sum_{r=1}^{K-1}|S_r^-|^2
+
\sum_{r=1}^{K-1}|S_r^+|^2.
\tag{4}
\]

The bow target scale is

\[
T_{\rm bow}:=XK\log X,
\tag{5}
\]

and `ANF-163` identifies the sharp coefficient-mass onset

\[
R_{\rm TV}:=T_{\rm bow}^{1/3}.
\tag{6}
\]

If

\[
K=X^{1-2\varepsilon+o(1)},
\tag{7}
\]

then

\[
R_{\rm TV}
=X^{2/3-2\varepsilon/3+o(1)}(\log X)^{1/3}.
\tag{8}
\]

The all-interval theorem of Matomäki--Shao--Tao--Teräväinen applies to `Lambda-Lambda^sharp` against every fixed-complexity nilsequence, hence in particular every fixed-degree polynomial phase, on intervals

\[
H\ge Y^{5/8+\eta}
\tag{9}
\]

for any fixed `eta>0`, with arbitrary fixed powers of logarithmic saving. Compare the power in (8) with `5/8`:

\[
\frac23-\frac{2\varepsilon}{3}-\frac58
=
\frac{1-16\varepsilon}{24}.
\tag{10}
\]

Hence if `0<epsilon<1/16`, there exists a fixed `eta_epsilon>0` such that, for every fixed `C>0`,

\[
\frac{R_{\rm TV}}{(\log X)^C}
\ge X^{5/8+\eta_\varepsilon}
\tag{11}
\]

for all sufficiently large `X`. One may for instance take any

\[
0<\eta_\varepsilon<\frac{1-16\varepsilon}{48}
\tag{12}
\]

after absorbing the `o(1)` in (7). The same intervals are safely below `X^(1-eta_epsilon)` because their upper scale will remain `X^(2/3+o(1))`.

At `epsilon=1/16`, the power in (8) is exactly `5/8`; the logarithmic factor does not supply the fixed positive exponent margin required by (9). For `epsilon>1/16`, the coefficient-mass onset lies strictly below the theorem's all-interval range. This is the origin of the range boundary in the present finding.

## 2. Degree six polynomializes the exact distinguished logarithmic twist with power-small error

The literature theorem is stated for nilsequences, not directly for the Archimedean character `n^(-iU)`. On the endpoint scales needed here the conversion is elementary and uniform.

Let `Y in [X,3X]` be the left endpoint of any relevant physical interval and write `n=Y+j`, `0<=j<=H`, where

\[
H\le X^{2/3+o(1)}.
\tag{13}
\]

Taylor's formula gives

\[
\log(Y+j)
=
\log Y
+
\sum_{m=1}^{6}\frac{(-1)^{m+1}}{m}\left(\frac jY\right)^m
+O\left(\left(\frac jY\right)^7\right).
\tag{14}
\]

Multiplying by `U=O(X^2)`, the phase remainder is

\[
O\left(\frac{X^2H^7}{X^7}\right)
=O\left(\frac{H^7}{X^5}\right)
=X^{-1/3+o(1)}
\tag{15}
\]

uniformly throughout (13). Thus there is a real polynomial `P_{Y,U}` of degree at most six such that

\[
n^{-iU}
=e(P_{Y,U}(n))
+O(X^{-1/3+o(1)}),
\qquad e(t):=e^{2\pi i t},
\tag{16}
\]

uniformly on the interval. The coefficients of this polynomial may depend arbitrarily on `Y` and `U`; Theorem 1.1(ii) of the all-interval paper is uniform over polynomial sequences, so no Diophantine exclusion on the distinguished height is required.

`ANF-163` proves, for every fixed polynomial interval length `H>=X^eta`,

\[
\sum_{n\in I}|r_X(n)|\ll_\eta H.
\tag{17}
\]

Consequently replacing the exact logarithmic carrier by (16) costs only

\[
\ll H X^{-1/3+o(1)}
=o_A(H\log^{-A}X)
\tag{18}
\]

for every fixed `A`. This is why the denominator-one resonance tubes of `ANF-159`--`ANF-161` do not obstruct the present step: they concern the bare carrier, whereas the all-interval theorem is uniform over the degree-six polynomial that captures all lower jets of the exact logarithmic phase.

## 3. Freezing Lambda-sharp across the two bow endpoints costs only H/log X

There is one non-cosmetic normalization issue. The bow residual (1) uses the single global cutoff `R_X`, while applying the all-interval theorem to an interval beginning at `Y in [X,3X]` naturally introduces

\[
R_Y:=\exp((\log Y)^{1/10}),
\qquad
Q_Y(n):=c_Y1_{(n,P(R_Y))=1}.
\tag{19}
\]

The two approximants are close enough in local `L^1` to retain one full logarithmic saving.

Assume first `R_X<=R_Y` and let `S` be the primes in `[R_X,R_Y)`. Since `Y/X` stays in a fixed compact subset of `(0,infinity)`, the mean value theorem gives

\[
|\log R_Y-\log R_X|
\ll (\log X)^{-9/10},
\tag{20}
\]

hence

\[
R_Y-R_X\ll R_X(\log X)^{-9/10}.
\tag{21}
\]

Brun--Titchmarsh on this short interval at the `R_X` scale, together with `log R_X=(log X)^(1/10)`, yields

\[
\#S\ll \frac{R_X}{\log X},
\qquad
s:=\sum_{p\in S}\frac1p\ll\frac1{\log X}.
\tag{22}
\]

The normalizations obey

\[
\frac{c_Y}{c_X}
=
\prod_{p\in S}\frac{p}{p-1}
=1+O(s).
\tag{23}
\]

For an interval `I` of any fixed polynomial length, the Selberg upper-bound sieve already used in `ANF-163` gives

\[
\#\{n\in I:(n,P(R_X))=1\}
\ll \frac{H}{\log R_X}+R_X^4,
\tag{24}
\]

and `c_X<<log R_X`. The mass change on integers which remain `R_Y`-rough is therefore `O(Hs)+X^{o(1)}`.

For integers which are `R_X`-rough but cease to be `R_Y`-rough, use the union bound over `p in S`. If `p|n` and `(n,P(R_X))=1`, then `n=pm` with `(m,P(R_X))=1`. Applying (24) to the induced interval for `m` gives

\[
\#\{n\in I:(n,P(R_X))=1,\ p\mid n\}
\ll
\frac{H}{p\log R_X}+R_X^4.
\tag{25}
\]

Summing (25) over `p in S` and multiplying by `c_X<<log R_X`, equations (22)--(23) give

\[
\sum_{n\in I}|Q_X(n)-Q_Y(n)|
\ll
Hs
+c_X\#S R_X^4
\ll
\frac{H}{\log X}+X^{o(1)}.
\tag{26}
\]

The case `R_Y<R_X` is symmetric. Since every interval used below has `H>=X^(5/8+eta_epsilon)`, the subpolynomial remainder is smaller than `H log^{-A}X` for every fixed `A`. Hence uniformly for `Y in [X,3X]`,

\[
\boxed{
\sum_{n\in I}|Q_X(n)-Q_Y(n)|
\ll \frac{H}{\log X}.
}
\tag{27}
\]

The loss in (27) is real at the level of this comparison: changing the reference point by a fixed multiplicative factor changes `log R` by `Theta((log X)^(-9/10))`, corresponding to total reciprocal-prime mass of order `1/log X`. Thus the present two-endpoint argument should not silently inherit the arbitrary `log^{-A}` saving of the locally normalized theorem.

## 4. The actual twisted residual has a uniform H/log X endpoint bound in the theorem range

Let `I=(Y,Y+H] subset [X,3X]`, with

\[
X^{5/8+\eta_\varepsilon}\le H\le X^{2/3+o(1)}.
\tag{28}
\]

Write

\[
r_X
=(\Lambda-Q_Y)+(Q_Y-Q_X)-(\Lambda-\vartheta).
\tag{29}
\]

After replacing `n^(-iU)` by the degree-six phase from Section 2, Theorem 1.1(ii) of Matomäki--Shao--Tao--Teräväinen gives, for every fixed `A_0>0`,

\[
\left|
\sum_{n\in I}(\Lambda(n)-Q_Y(n))e(P_{Y,U}(n))
\right|
\ll_{A_0,\varepsilon,A,B}
H\log^{-A_0}X.
\tag{30}
\]

The theorem is maximal over arithmetic progressions inside the interval, so ordinary endpoint subintervals are covered a fortiori. Equation (27) handles the frozen-approximant mismatch.

The remaining `Lambda-vartheta` term is supported on prime powers of exponent at least two. On any interval in `[X,3X]`, their number is

\[
O(HX^{-1/2}+\log X),
\tag{31}
\]

so their total Mangoldt weight is

\[
O(HX^{-1/2}\log X+\log^2X)
=o_A(H\log^{-A}X)
\tag{32}
\]

for every fixed `A` in the range (28). Together with the Taylor error (18), equations (27), (30), and (32) yield the source-specific bound

\[
\boxed{
\left|
\sum_{n\in I}r_X(n)n^{-iU}
\right|
\ll_{\varepsilon,A,B}
\frac{H}{\log X}
}
\tag{33}
\]

uniformly for every endpoint interval in (28) and every distinguished height in the fixed window `AX^2<=U<=BX^2`.

At the left endpoint, where the global and local reference scales coincide, the mismatch (27) disappears and (33) may be strengthened to arbitrary fixed logarithmic saving. The single-log version is retained because it is uniform across both bow endpoints without changing the canonical source normal form.

## 5. Endpoint completion is negligible through R_TV times every log power below two-thirds

Fix any

\[
0\le\beta<\frac23
\tag{34}
\]

and define

\[
R_-:=\frac{R_{\rm TV}}{\log X},
\qquad
R_+:=R_{\rm TV}(\log X)^\beta.
\tag{35}
\]

For `epsilon<1/16`, equation (11) puts every length `R_-<=r<=R_+` in the all-interval range for large `X`. Applying (33) to both left and right endpoint prefixes/suffixes gives

\[
\sum_{R_-\le r\le R_+}
\left(|S_r^-|^2+|S_r^+|^2\right)
\ll
\frac1{\log^2X}\sum_{r\le R_+}r^2
\ll
\frac{R_+^3}{\log^2X}.
\tag{36}
\]

Since `R_TV^3=T_bow`, this is

\[
\ll
T_{\rm bow}(\log X)^{3\beta-2}
=o(T_{\rm bow}).
\tag{37}
\]

For `r<R_-`, the local total-variation estimate of `ANF-163` gives

\[
E_{\partial,\,r<R_-}
\ll
R_-^3+X^{3/4}\log^2X
=o(T_{\rm bow}).
\tag{38}
\]

Combining (36)--(38),

\[
\boxed{
E_{\partial,\,r\le R_{\rm TV}(\log X)^\beta}
=o(XK\log X)
\qquad
(0<\varepsilon<1/16,\ \beta<2/3).
}
\tag{39}
\]

This is a strict arithmetic improvement over the sharp information boundary in `ANF-163`. There, coefficient mass alone allows a triangular synthetic packet with target-scale energy at `r asymp R_TV`. Equation (39) proves that the actual prime-minus-rough source cannot realize that saturation mechanism, nor any fixed polylogarithmic dilation of it below exponent `2/3`.

In particular, if for some fixed `delta>0`

\[
E_\partial\ge\delta XK\log X,
\tag{40}
\]

then for every fixed `beta<2/3`,

\[
\sum_{r>R_{\rm TV}(\log X)^\beta}
\left(|S_r^-|^2+|S_r^+|^2\right)
\ge
(\delta-o(1))XK\log X.
\tag{41}
\]

A macroscopic endpoint correction is therefore forced to migrate to genuinely longer cumulative scales.

## 6. What this does and does not cross

The `epsilon=1/16` threshold is exact for the present combination of inputs. From (10), when `epsilon>=1/16`, the coefficient-mass scale `R_TV` is at or below `X^(5/8+o(1))`, while the all-interval theorem needs a fixed positive exponent margin above `5/8`. The triangular information-boundary control of `ANF-163` can therefore accumulate target-scale energy before the theorem becomes available. No conclusion analogous to (39) is obtained in that regime.

Even when `epsilon<1/16`, (39) does **not** prove `E_partial=o(XK log X)`. The all-interval theorem supplies logarithmic rather than power saving. On a dyadic scale `r asymp R`, the crude consequence of a bound `|S_r|<<R/log^A X` is endpoint energy `O(R^3/log^(2A)X)`. Arbitrary fixed `A` can beat any fixed power of `log X`, but not a fixed power enlargement `R/R_TV=X^delta`. Moreover the globally frozen rough model creates the concrete one-log bottleneck (27) when both endpoints are treated simultaneously, which is why the symmetric statement (39) stops at `beta<2/3`.

The almost-all interval theorem of Matomäki--Radziwiłł--Shao--Tao--Teräväinen reaches the shorter exponent `1/3`, but its exceptional set cannot be discarded at these two distinguished bow endpoints. It is therefore not a substitute for the all-interval input used here.

The closest prior art is precisely Matomäki--Shao--Tao--Teräväinen, *Higher uniformity of arithmetic functions in short intervals I. All intervals*, Forum of Mathematics, Pi 11 (2023), e29, Theorem 1.1(ii). That theorem is load-bearing for (30), and the repository source ledger now records it. The paper itself already explains that polynomial phases are nilsequences and discusses Archimedean twists in its reduction machinery. The new claim here is **not** a new standalone exponential-sum theorem: it is the line-specific synthesis of that all-interval discorrelation with the exact bow endpoint square-function, the cubic energy scale of `ANF-163`, the fixed global rough approximant, and the two-endpoint normalization audit leading to (39) and the exact `epsilon=1/16` activation boundary.

### Falsification boundary

This finding would fail if any of the following were required but unavailable: the maximal all-interval `Lambda-Lambda^sharp` estimate with arbitrary fixed log saving at `H>=X^(5/8+eta)`; uniformity over fixed degree-six polynomial phases; the exact identification of the local approximant with `P(R)/phi(P(R)) 1_(n,P(R))=1`; or the local rough-number sieve bound used in (24)--(27). No RH, Lindelof hypothesis, unproved pair correlation, or almost-all-to-all upgrade is used.

### Next gate

For `epsilon<1/16`, the next source-side target is no longer cancellation at the coefficient-mass onset. One must control the cumulative square function on scales beyond `R_TV (log X)^(2/3-o(1))`, ideally by proving a genuinely power-saving estimate at the **exact distinguished logarithmic twist** or by estimating the aggregate endpoint square function directly rather than bounding every prefix separately. For `epsilon>=1/16`, a different all-interval input below exponent `5/8` is needed before this mechanism even reaches the cubic onset. Either improvement would be qualitatively new relative to the literature theorem used here.