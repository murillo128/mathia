# RE-071 — matched first-layer packets force opposite Chebyshev-Mertens error drift

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + FIRST-LAYER-ONLY-PACKET + MATCHED-FRINGE + CHEBYSHEV-MERTENS-OPPOSITE-DRIFT + UNBOUNDED-PACKET + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-068` shows that a complete matched `0 -> 0` first-layer fan packet has exactly the same ordinary-prime multiset on the selector side and on the physical event side. `RE-070` nevertheless shows that the tied selector geometry stretches that fixed Chebyshev mass over a longer interval, forcing the standard Chebyshev error

\[
H_\vartheta(x):=x-\vartheta(x)
\]

to increase across the packet. The reciprocal-prime source has a complementary constraint: after the standard Mertens normalization is retained, it is forced to move in the **opposite direction**.

Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on the sufficiently late common positive CA counterexample blocks of `RE-040`. At a rightmost-fan breakpoint `b\in J`, let

\[
C_-<C_+,
\qquad
Y_\pm:=\log C_\pm,
\tag{2}
\]

be consecutive exposed states tied at the common adaptive amplitude

\[
c:=A_b(C_-)=A_b(C_+)>0,
\tag{3}
\]

with adaptive tangent selectors `Z_-<Z_+`. Suppose that the complete physical packet from `C_-` to `C_+` is first-layer-only and has matched fringe pattern

\[
\chi_- = \chi_+ =0.
\tag{4}
\]

No bound on packet cardinality is assumed. Define

\[
M(x):=\sum_{p\le x}-\log(1-p^{-1}),
\qquad
E_\ell(x):=M(x)-\gamma-\log\log x.
\tag{5}
\]

As in `RE-070`, put

\[
a_c(Y):=\frac{cY^{-b}}{1+cY^{-b}},
\qquad
h_c(Y):=\log(1+cY^{-b}),
\tag{6}
\]

and let `Z_c(Y)>Y` solve

\[
g(Z_c(Y))=g(Y)-\frac{b\,a_c(Y)}Y,
\qquad
g(x):=\frac1{x\log x}.
\tag{7}
\]

Then the reciprocal-prime error satisfies

\[
\boxed{
E_\ell(Z_+)-E_\ell(Z_-)
=-b(1-b)\int_{Y_-}^{Y_+}\frac{a_c(t)}{t}\,dt\,(1+o_J(1))<0.
}
\tag{8}
\]

The `o_J(1)` is uniform over such late matched first-layer packets, including packets whose number of first-layer events tends to infinity. Combining (8) with the Chebyshev drift of `RE-070`,

\[
H_\vartheta(Z_+)-H_\vartheta(Z_-)
=b(1-b)\int_{Y_-}^{Y_+}a_c(t)\log t\,dt\,(1+o_J(1))>0,
\tag{9}
\]

gives the joint packet law

\[
\boxed{
\frac{-\bigl(E_\ell(Z_+)-E_\ell(Z_-)\bigr)}
{H_\vartheta(Z_+)-H_\vartheta(Z_-)}
=
\frac{\displaystyle\int_{Y_-}^{Y_+}a_c(t)t^{-1}\,dt}
{\displaystyle\int_{Y_-}^{Y_+}a_c(t)\log t\,dt}
\,(1+o_J(1)).
}
\tag{10}
\]

Thus the matched packet is not merely Chebyshev-underdense: it is a **two-source saddle**. The standard error `Z-vartheta(Z)` rises while the logarithmic Mertens-product error falls. For a sublinear packet, with

\[
Y:=Y_-,\qquad \Delta Y:=Y_+-Y_-=o(Y),\qquad a_-:=a_c(Y),
\]

this becomes

\[
\boxed{
E_\ell(Z_+)-E_\ell(Z_-)
=-b(1-b)a_-\frac{\Delta Y}{Y}(1+o_J(1)),
}
\tag{11}
\]

and, using `RE-070`,

\[
\boxed{
E_\ell(Z_+)-E_\ell(Z_-)
=-\frac{H_\vartheta(Z_+)-H_\vartheta(Z_-)}{Y\log Y}
(1+o_J(1)).
}
\tag{12}
\]

The point is not that the reciprocal prime weights distinguish the prime multiset: `RE-068` proves they do not. The new information comes from the interaction between that exact multiset identity, the change of the Robin height along the tied common-amplitude curve, and the different normalizations `log log Y` and `log log Z`. The only residual discrepancy between the two prime weights is a positive prime-square correction, and it is too small to reverse the forced drift.

## 1. Exact reciprocal-prime increment identity

Let

\[
\mathcal S:=\{p\text{ prime}:Z_-<p\le Z_+\}.
\tag{13}
\]

By the matched first-layer prime-set theorem `RE-068`, `S` is exactly the set of physical first-layer labels crossed by the packet. Hence

\[
\frac{C_+}{C_-}=\prod_{p\in\mathcal S}p,
\tag{14}
\]

and every crossed event changes the exponent of its prime from zero to one. Therefore

\[
\frac{\sigma(C_+)/C_+}{\sigma(C_-)/C_-}
=\prod_{p\in\mathcal S}\left(1+\frac1p\right).
\tag{15}
\]

Since

\[
h(C)=\log G(C)-\gamma
=\log\frac{\sigma(C)}C-\log\log Y-\gamma,
\qquad Y=\log C,
\tag{16}
\]

subtraction gives the exact height increment

\[
\boxed{
h(C_+)-h(C_-)
=\sum_{p\in\mathcal S}\log(1+p^{-1})
-\bigl(\log\log Y_+-\log\log Y_-\bigr).
}
\tag{17}
\]

For each prime define the positive prime-square remainder

\[
\tau_p
:=-\log(1-p^{-2}).
\tag{18}
\]

The Euler-factor identity

\[
-\log(1-p^{-1})
=\log(1+p^{-1})+\tau_p
\tag{19}
\]

is exact. Using (17) in the definition (5) therefore yields

\[
\boxed{
\begin{aligned}
E_\ell(Z_+)-E_\ell(Z_-)
&=h(C_+)-h(C_-)\\
&\quad+\log\log Y_+-\log\log Y_-\\
&\quad-\log\log Z_++\log\log Z_-\\
&\quad+\sum_{p\in\mathcal S}\tau_p.
\end{aligned}
}
\tag{20}
\]

At the breakpoint both endpoint heights lie on the same common-amplitude curve,

\[
h(C_\pm)=h_c(Y_\pm),
\qquad
Z_\pm=Z_c(Y_\pm).
\tag{21}
\]

Define the smooth comparison function

\[
F_c(Y):=h_c(Y)+\log\log Y-\log\log Z_c(Y).
\tag{22}
\]

Then (20) is the exact packet decomposition

\[
\boxed{
E_\ell(Z_+)-E_\ell(Z_-)
=F_c(Y_+)-F_c(Y_-)
+\sum_{p\in\mathcal S}\tau_p.
}
\tag{23}
\]

No prime-number-theorem estimate has entered.

## 2. The tied selector makes the smooth Mertens component strictly decrease

Differentiate (22). From (6),

\[
h_c'(Y)=-\frac{b\,a_c(Y)}Y.
\tag{24}
\]

Also

\[
\frac{d}{dY}\log\log Y=g(Y),
\qquad
\frac{d}{dY}\log\log Z_c(Y)=Z_c'(Y)g(Z_c(Y)).
\tag{25}
\]

Using the tangent identity (7), these terms collapse exactly:

\[
\begin{aligned}
F_c'(Y)
&=-\frac{ba_c(Y)}Y+g(Y)-Z_c'(Y)g(Z_c(Y))\\
&=\bigl(Z_c'(Y)-1\bigr)
\left(\frac{ba_c(Y)}Y-g(Y)\right).
\end{aligned}
\tag{26}
\]

Equivalently,

\[
\boxed{
F_c'(Y)
=-\frac{Z_c'(Y)-1}{Y\log Y}
\bigl(1-ba_c(Y)\log Y\bigr).
}
\tag{27}
\]

This exact factorization exposes the sign. `RE-070` proves uniformly on late tied segments that

\[
Z_c'(Y)-1
=b(1-b)a_c(Y)\log Y
\left(1+O_J\left(\frac1{\log Y}+a_c(Y)\log Y\right)\right),
\tag{28}
\]

while the common small-height regime gives

\[
a_c(Y)\log Y\to0.
\tag{29}
\]

Substitution into (27) gives

\[
\boxed{
F_c'(Y)
=-\frac{b(1-b)a_c(Y)}Y
\left(1+O_J\left(\frac1{\log Y}+a_c(Y)\log Y\right)\right).
}
\tag{30}
\]

In particular, `F_c` is strictly decreasing on every sufficiently late tied segment. Integrating,

\[
F_c(Y_+)-F_c(Y_-)
=-b(1-b)\int_{Y_-}^{Y_+}\frac{a_c(t)}t\,dt\,(1+o_J(1)).
\tag{31}
\]

The same selector expansion that produced the positive Chebyshev deficit in `RE-070` therefore produces a negative smooth reciprocal-prime drift after the exact Robin-height normalization is inserted.

## 3. The positive prime-square correction is uniformly lower order

It remains to show that the last term in (23) cannot cancel (31). For every prime `p>=2`,

\[
0<\tau_p=-\log(1-p^{-2})\le \frac{2}{p^2}.
\tag{32}
\]

Put `X:=Y_-`. The tangent selector always satisfies `Z_c(X)>X`, so every `p\in S` obeys `p>X`. The false-RH common blocks of `RE-040` also supply one uniform lower amplitude `c>=c_0>0`.

First suppose `Y_+<=2X`. From `RE-068`,

\[
Y_+-Y_-=\sum_{p\in\mathcal S}\log p,
\tag{33}
\]

hence

\[
\#\mathcal S\le\frac{Y_+-Y_-}{\log X}.
\tag{34}
\]

Equation (32) then gives

\[
\sum_{p\in\mathcal S}\tau_p
\ll\frac{Y_+-Y_-}{X^2\log X}.
\tag{35}
\]

Because `b<=b_1<1/2`, `c>=c_0`, and `a_c` decreases only by a bounded factor on `[X,2X]`,

\[
\int_X^{Y_+}\frac{a_c(t)}t\,dt
\gg_J (Y_+-X)X^{-1-b_1}.
\tag{36}
\]

Consequently the ratio of (35) to (36) is

\[
O_J\left(\frac{X^{b_1-1}}{\log X}\right)=o(1).
\tag{37}
\]

If instead `Y_+>2X`, then already the initial dyadic portion gives

\[
\int_X^{Y_+}\frac{a_c(t)}t\,dt
\ge\int_X^{2X}\frac{a_c(t)}t\,dt
\gg_J X^{-b_1},
\tag{38}
\]

whereas the entire future prime-square tail satisfies the elementary estimate

\[
\sum_{p\in\mathcal S}\tau_p
\le2\sum_{n>X}\frac1{n^2}
\ll\frac1X.
\tag{39}
\]

Again the ratio is `O_J(X^{b_1-1})=o(1)`. Thus in both regimes

\[
\boxed{
\sum_{p\in\mathcal S}\tau_p
=o_J\left(\int_{Y_-}^{Y_+}\frac{a_c(t)}t\,dt\right).
}
\tag{40}
\]

Combining (23), (31), and (40) proves (8), including its eventual strict negative sign. The argument uses no PNT and no packet-cardinality bound.

## 4. Coupling to the Chebyshev drift

`RE-070` proves on the same packet

\[
H_\vartheta(Z_+)-H_\vartheta(Z_-)
=b(1-b)\int_{Y_-}^{Y_+}a_c(t)\log t\,dt\,(1+o_J(1)).
\tag{41}
\]

Dividing (8) by (41) gives (10). Since

\[
\frac{\int a_c(t)t^{-1}\,dt}{\int a_c(t)\log t\,dt}
\]

is the weighted average of `1/(t log t)` with respect to the positive measure `a_c(t) log t\,dt`, it also obeys

\[
\frac1{Y_+\log Y_+}
\le
\frac{\int_{Y_-}^{Y_+}a_c(t)t^{-1}\,dt}
{\int_{Y_-}^{Y_+}a_c(t)\log t\,dt}
\le
\frac1{Y_-\log Y_-}.
\tag{42}
\]

For `Y_+-Y_-=o(Y_-)`, both bounds are asymptotic to `1/(Y log Y)`, giving (11)--(12).

The two error functions therefore encode the same selector dilation with different kernels. `H_vartheta` sees the dilation at scale `a log Y` times interval length, while `E_l` sees it after the additional reciprocal factor `1/(Y log Y)`. This is not a contradiction with `RE-069`: that result concerns the direct transport from prime locations to delayed first-layer event coordinates inside the exact Robin workload. Here the surviving signal comes from the common-amplitude selector geometry and the Robin-height/Mertens normalization before that direct timing tax is applied.

## 5. Prior-art boundary, falsification, and research consequence

Joint behavior of weighted prime-counting errors is not new. Bhattacharya--Martin--Simpson study correlations between normalized errors including `theta(x)-x` and the logarithmic Mertens prime-product error, and obtain RH-equivalent one-sided comparison results plus conditional joint distributions. That literature is already anchored in `SOURCES.md`. The prime-square correction in (18)--(19) is also standard Euler-factor algebra. Mantovanelli's recent CA workload framework supplies the closest packet/event prior-art boundary and is likewise already anchored.

The line-specific content here is narrower: for **two consecutive exposed CA states tied at one false-RH adaptive amplitude**, with a complete matched first-layer physical packet between them, the exact prime-set reconciliation plus the tied tangent relation force the cross-endpoint asymptotic (8) and hence the opposite-signed pair (8)--(9). No priority claim is made beyond this derived specialization, and no new external theorem is load-bearing.

The matched fringe hypothesis is essential. A `0 -> 1` or `1 -> 0` packet has the unmatched endpoint prime of `RE-068`, and its reciprocal-prime weight enters (20) at first order; the sign conclusion need not survive. The first-layer-only hypothesis is equally essential: a higher-layer event changes the active higher-layer mass and exponent tail and is precisely the separate charge mechanism of `RE-060`--`RE-066`.

The common-amplitude condition is also structural, not cosmetic. Equation (27) uses one smooth curve `h_c(Y),Z_c(Y)` joining the tied endpoints. It must not be applied to arbitrary CA states or to endpoints selected at unrelated threshold parameters.

The result concerns the **unscaled** Mertens error `E_l`. It does not assert that the normalized coordinate `V(Z)=E_l(Z)sqrt(Z)log Z` of `RE-036`--`RE-037` decreases: the changing normalization can dominate such a local statement. Nor does it contradict known prime-error oscillation or false RH. An off-critical zero permits errors much larger than these packet increments, so (8) is a structural obligation rather than an immediate exclusion.

What changes is the remaining matched first-layer problem. `RE-070` left a source-specific positive excursion of `Z-vartheta(Z)` on adaptively selected intervals. Those same intervals must now simultaneously carry a negative excursion of the logarithmic Mertens error with the calibrated magnitude (10). A future cross-packet contradiction may therefore use the **joint** selected trajectory rather than seeking a stronger one-coordinate short-interval estimate. Conversely, any matched synthetic control that aims to reproduce the late fan must now reproduce both signs and their packet-scale ratio, not merely the Chebyshev underdensity.