# FD-306 — Vinogradov minor arcs force deep-capacity Möbius spectrum onto rational major arcs

- **Date:** 2026-09-24
- **Status:** proved current-literature localization of the FD-305 spectral obstruction to a vanishing major-arc set at sufficiently deep polynomial scale
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens field / additive Möbius spectrum / Vinogradov minor arcs / rational major arcs / fourth-moment concentration / capacity obstruction
- **Depends on:** FD-300, FD-304, FD-305
- **Classification:** `RH-CONDITIONAL-INPUT + UNCONDITIONAL-MINOR-ARC-BOUND + MAJOR-ARC-LOCALIZATION + FOURTH-MOMENT-CONCENTRATION + CAPACITY-BOUNDARY + ROUTE-RESTRICTION`

## Claim

Continue with the FD-305 near-capacity premise

\[
L_N(x)\ge N^{1/2}x^{1+c-o(1)},
\qquad
c:=1-\log_2(3/2)=0.4150374992\ldots,
\tag{1}
\]

under RH and the fixed polynomial-depth regime

\[
x=N^{\lambda+o(1)}.
\tag{2}
\]

For `\lambda>3/(10c)`, FD-304 and FD-305 produce a dyadic shell `Q<q\le2Q`, with

\[
1\le Q\le2x,
\qquad
X:=NQ,
\tag{3}
\]

and the compact Möbius block

\[
F_X(\alpha)
:=
\sum_{X\le n<2X}\mu(n)e(n\alpha),
\qquad e(t):=e^{2\pi i t},
\tag{4}
\]

satisfying

\[
\boxed{
\int_0^1|F_X(\alpha)|^4\,d\alpha
\ge
Q^2N^{-3/2}x^{9c-o(1)}
}
\tag{5}
\]

and

\[
\boxed{
\|F_X\|_\infty
\ge
Q^{1/2}N^{-5/4}x^{9c/2-o(1)}.
}
\tag{6}
\]

Define the rational major arcs

\[
\mathfrak M_X
:=
\bigcup_{1\le q<X^{2/5}}
\ \bigcup_{\substack{a\pmod q\\(a,q)=1}}
\left\{
\alpha\in\mathbb R/\mathbb Z:
\left\|\alpha-\frac aq\right\|_{\mathbb T}
\le
\frac{X^{-3/5}}q
\right\}.
\tag{7}
\]

The endpoint Möbius form of the Vinogradov-quality estimate proved by Robles implies

\[
\boxed{
\sup_{\alpha\notin\mathfrak M_X}|F_X(\alpha)|
\ll
X^{4/5}(\log 2X)^{C_0}
}
\tag{8}
\]

for an absolute constant `C_0`.

Consequently, if

\[
\boxed{
\lambda>
\lambda_{\rm maj}
:=
\frac{41}{90c-6}
=
1.3076742164\ldots,
}
\tag{9}
\]

then every FD-305 coefficient that realizes the forced scale (6) must lie in `\mathfrak M_X`. More strongly, the full FD-305 fourth-moment lower-bound scale is forced onto those major arcs:

\[
\boxed{
\int_{\mathfrak M_X}|F_X(\alpha)|^4\,d\alpha
\ge
(1-o(1))
Q^2N^{-3/2}x^{9c-o(1)}.
}
\tag{10}
\]

The major arcs themselves have vanishing total measure,

\[
\boxed{
\operatorname{meas}(\mathfrak M_X)
\ll X^{-1/5}.
}
\tag{11}
\]

Thus, above the depth threshold (9), the surviving near-capacity obstruction is no longer an arbitrary additive Fourier spike. It must be concentrated near rationals of denominator `<X^{2/5}`, inside a set of measure `O(X^{-1/5})`.

The conclusion is one-way. It does not rule out the major-arc concentration, does not identify a specific denominator, and does not claim that the threshold (9) is optimal.

## 1. Current Möbius Vinogradov bound gives a clean minor-arc ceiling

Nicolas Robles, *Heath-Brown identities for fractional powers of zeta*, arXiv `2608.07198v1` (7 August 2026), proves a Vinogradov-quality exponential-sum estimate for fractional zeta coefficients and states the endpoint Möbius specialization. In the notation needed here, if `(a,q)=1` and

\[
\left|\alpha-\frac aq\right|\le\frac1{q^2},
\tag{12}
\]

then

\[
\sum_{n\le Y}\mu(n)e(n\alpha)
\ll
\left(
Yq^{-1/2}
+
Y^{4/5}
+
Y^{1/2}q^{1/2}
\right)
(\log 2Y)^{C_0},
\tag{13}
\]

with an absolute log-power loss. This input is unconditional. The RH label of the present finding is inherited from the FD-304 common-window reduction, not from (13).

To pass from the prefix sum in (13) to the fixed block (4), write `F_X` as the difference of the prefixes at `2X` and `X`. The same rational approximation is admissible for both prefixes, so

\[
|F_X(\alpha)|
\ll
\left(
Xq^{-1/2}
+
X^{4/5}
+
X^{1/2}q^{1/2}
\right)
(\log 2X)^{C_0}.
\tag{14}
\]

Now set

\[
R:=X^{2/5},
\qquad
Y:=X^{3/5}.
\tag{15}
\]

Dirichlet approximation gives, for every `\alpha\in\mathbb T`, a reduced fraction `a/q` with

\[
1\le q\le Y,
\qquad
\left\|\alpha-\frac aq\right\|_{\mathbb T}
\le
\frac1{qY}
=
\frac{X^{-3/5}}q.
\tag{16}
\]

If `\alpha\notin\mathfrak M_X`, this approximant cannot have `q<R`; hence

\[
X^{2/5}\le q\le X^{3/5}.
\tag{17}
\]

The upper bound in (17) also ensures that the approximation in (16) satisfies (12), because

\[
\frac1{qX^{3/5}}\le\frac1{q^2}.
\tag{18}
\]

Across the entire denominator range (17), all three terms in (14) are at most the `X^{4/5}` scale:

\[
Xq^{-1/2}\le X^{4/5},
\qquad
X^{1/2}q^{1/2}\le X^{4/5}.
\tag{19}
\]

This proves the minor-arc ceiling (8).

The exponents `2/5` and `3/5` are not inserted arbitrarily. `R=X^{2/5}` is the smallest power-denominator major-arc cutoff for which the two rational-approximation terms in (14) are simultaneously no larger than the intrinsic `X^{4/5}` term while the complementary Dirichlet denominator ceiling remains `X^{3/5}`.

## 2. The FD-305 pointwise spike cannot remain on the minor arcs at deep scale

Compare the forced lower bound (6) with (8). Since `X=NQ`, their ratio is at least

\[
\frac{
Q^{1/2}N^{-5/4}x^{9c/2-o(1)}
}{
X^{4/5}(\log 2X)^{C_0}
}
=
N^{-41/20}Q^{-3/10}x^{9c/2-o(1)}.
\tag{20}
\]

The dyadic shell supplied upstream always satisfies `Q\le2x`. Therefore

\[
Q^{-3/10}
\gg
x^{-3/10},
\tag{21}
\]

and (20) is bounded below by

\[
N^{-41/20}
 x^{9c/2-3/10-o(1)}.
\tag{22}
\]

Using (2), this becomes

\[
N^{
\lambda(9c/2-3/10)-41/20-o(1)
}.
\tag{23}
\]

The exponent is positive exactly when

\[
\lambda
>
\frac{41/20}{9c/2-3/10}
=
\frac{41}{90c-6},
\tag{24}
\]

which is (9). The fixed logarithmic loss in (8) is swallowed by the positive power margin. Hence, in that depth range, a coefficient at the forced FD-305 scale cannot occur outside `\mathfrak M_X`.

This threshold is deliberately uniform in the source-selected shell. For a particular shell one can retain `Q` in (20) and obtain a sharper shell-dependent test. Equation (9) is what survives without knowing where in `1\le Q\le2x` the capacity-bearing shell lies.

## 3. The entire forced fourth-moment scale is also major-arc supported

The pointwise conclusion is not the strongest consequence. Parseval gives, exactly as in FD-305,

\[
\int_0^1|F_X(\alpha)|^2\,d\alpha
=
\sum_{X\le n<2X}\mu(n)^2
\le X.
\tag{25}
\]

Combining (8) and (25), the minor arcs contribute at most

\[
\begin{aligned}
\int_{\mathbb T\setminus\mathfrak M_X}
|F_X(\alpha)|^4\,d\alpha
&\le
\left(
\sup_{\alpha\notin\mathfrak M_X}|F_X(\alpha)|^2
\right)
\int_0^1|F_X(\alpha)|^2\,d\alpha\\
&\ll
X^{13/5}(\log 2X)^{2C_0}.
\end{aligned}
\tag{26}
\]

Relative to the FD-305 lower-bound scale in (5), the ratio is controlled by

\[
\frac{
Q^2N^{-3/2}x^{9c-o(1)}
}{
X^{13/5}(\log 2X)^{2C_0}
}
=
N^{-41/10}Q^{-3/5}x^{9c-o(1)}.
\tag{27}
\]

Again using `Q\le2x`, the right-hand side is at least

\[
N^{-41/10}x^{9c-3/5-o(1)}
=
N^{
\lambda(9c-3/5)-41/10-o(1)
}.
\tag{28}
\]

The positivity condition for the exponent in (28) is exactly the same threshold (9), because (28) is twice the exponent in (23). Thus, above `\lambda_{\rm maj}`, the minor-arc fourth moment is `o` of the amount already forced by FD-305. Subtracting (26) from the total fourth moment proves (10).

So the localization is not merely existential. Even if the actual fourth moment is larger than the FD-305 lower bound, the **entire amount that FD-305 needs in order to certify near-capacity** must already be carried by the rational major arcs.

## 4. The surviving major-arc set is small

No disjointness of the arcs in (7) is needed. A union bound gives

\[
\begin{aligned}
\operatorname{meas}(\mathfrak M_X)
&\le
\sum_{q<X^{2/5}}
\varphi(q)
\frac{2X^{-3/5}}q\\
&\le
2X^{-3/5}
\sum_{q<X^{2/5}}1\\
&\ll
X^{-1/5}.
\end{aligned}
\tag{29}
\]

Therefore the forced fourth-moment mass in (10) is concentrated on a set whose measure tends to zero polynomially. This is a stronger structural statement than the unrestricted frequency `\alpha_*` left by FD-305: the spectral certificate is now both rationally approximable and spatially sparse in frequency.

Nothing here identifies whether the relevant denominator is bounded, grows slowly, or approaches `X^{2/5}`. That denominator profile is the next information needed before a major-arc asymptotic can be converted into a contradiction or into a more explicit arithmetic obstruction.

## 5. Prior-art boundary and adversarial review

The load-bearing external theorem is the endpoint Möbius Vinogradov estimate from Robles, arXiv `2608.07198v1`, now anchored in `SOURCES.md`. The estimate itself is not claimed as new. The new statement is the parameter match between that current minor-arc ceiling and the source-selected lower bounds of FD-305, including the uniform shell elimination through `Q\le2x` and the resulting threshold (9).

The older Davenport log-power estimate already anchored in `SOURCES.md` is uniform in frequency but is too weak at the power scale relevant here: it cannot distinguish a forced power-above-square-root spike from a generic frequency. The present step uses a genuine power-scale minor-arc estimate, not merely another logarithmic saving.

The adversarial checks are as follows. First, (13) is applied only after producing an admissible reduced Dirichlet approximant; the range `q\le X^{3/5}` is exactly what guarantees the required `q^{-2}` approximation quality. Second, passing from prefixes to the fixed block costs only an absolute factor, not a boundary term comparable with the forced scale. Third, the worst-case shell substitution is in the correct direction: because the comparison contains `Q^{-3/10}` or `Q^{-3/5}`, the upper shell bound `Q\le2x` gives the uniform lower comparison needed for (22) and (28). Fourth, the fixed log-power loss is absorbed only after a strict inequality in (9); no statement is made at the endpoint. Fifth, the fourth-moment argument uses only the exact second-moment bound (25), so it does not assume that the pointwise maximizer carries all of the fourth moment. Sixth, the major-arc measure estimate is a union bound and therefore remains valid even with heavy overlap. Seventh, RH is not smuggled into the minor-arc theorem: it is inherited solely from FD-304/FD-305. Finally, no contradiction is claimed on `\mathfrak M_X`; major arcs are precisely the region where the Vinogradov estimate permits larger arithmetic structure.

## 6. Consequence for the Farey route

FD-303 and FD-304 reduced near-capacity divisor-convolved block-Mertens mass to a common-window family of positive Möbius correlations. FD-305 compressed that family into one fixed Möbius Fourier block but left its frequency completely unrestricted. FD-306 removes that freedom at sufficiently deep polynomial scale: **above `\lambda_{\rm maj}=1.3076742164\ldots`, the required spectral certificate must live on rational major arcs of total measure `O(X^{-1/5})`.**

This sharpens the ownership boundary. The Farey-specific route has selected the block scale `X=NQ` and forced the amount of spectral mass. Once the only remaining question is whether Möbius can support that mass near rationals `a/q`, a generic analysis of the corresponding rational twists belongs naturally to the `mobius_cancellation` line unless additional Farey geometry constrains the denominator `q` or the chosen phase.

The immediate next test inside this line is therefore not another unrestricted Fourier estimate. It is to ask whether the source-selection mechanism itself yields any extra control of the rational denominator in (7). If it does not, the mathematical carrier is ready for a clean handoff to a Möbius-major-arc problem.

## Bottom line

Robles' current unconditional Vinogradov-quality estimate gives

\[
\sup_{\alpha\notin\mathfrak M_X}|F_X(\alpha)|
\ll X^{4/5}(\log X)^{C_0}
\tag{30}
\]

for the classical balance `q\in[X^{2/5},X^{3/5}]`. Combining this with the FD-305 source-selected lower bounds shows that, under RH and

\[
\lambda>
\frac{41}{90c-6}
=
1.3076742164\ldots,
\tag{31}
\]

the near-capacity Farey route forces its Möbius Fourier spike and its entire required fourth-moment scale into rational major arcs of denominator `<X^{2/5}` and total measure `O(X^{-1/5})`. This does not close the route, but it turns the surviving deep-regime obstruction from an arbitrary additive spike into a sharply localized rational one.