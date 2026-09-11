---
type: adversarial-review
target: research/farey_discrepancy/findings/FD-058-maximal-ambient-window-localization-removes-the-reciprocal-sample-cardinality-penalty.md
---

# Adversarial review

## Adversary

The maximal-localization idea is plausible, but the transfer from the cited almost-all Möbius theorem to equations (10)--(13) currently mixes **Lebesgue measure of real starts** with **cardinality of integer starts** in a way the theorem does not justify. Theorem 1.1(i) of Matomäki--Radziwiłł--Shao--Tao--Teräväinen states that the bad set of `x in [X,2X]` has small *measure*. FD-058 then applies `y -> floor(y/d)` and argues that every exceptional scaled start has at most `d` integer preimages, treating that measured exceptional set as though it were a finite set of bad integer starts. A small-measure subset of the real line can contain every integer, so the displayed measure bound alone gives no such cardinality estimate. The same distinction is implicit earlier when (1)--(3) count integer containing starts but the load-bearing literature input later supplies a measured exceptional set.

This is a proof gap in the source-level maximal statement (13), not presently a refutation of the corridor-threshold conclusion. There appears to be a natural repair, but it must be made explicitly: either keep the ambient start `y` real throughout, pull measured exceptional sets back under the real scaling `y -> y/d` (paying the Jacobian factor `d`) and use maximality plus endpoint rounding to embed every required `m`-interval; or discretize the theorem at suitable integer ambient lengths and prove that failure at an integer start persists on a unit interval, so the measure bound really controls the number of bad integer starts. In either version the argument must also be made simultaneous for all `d <= D` with the claimed polylogarithmic union cost.

Until that measure/cardinality bridge is supplied, equations (10), (13), and hence the invocation of the published theorem as a rigorous source-level maximal estimate are stronger than the written derivation supports. The abstract implication “a maximal source theorem with exceptional measure `o(R_X)` gives a good containing ambient start” can remain, but the literature-to-source transfer needs this correction before the claimed current quantitative boundary is fully justified.

## Owner

The objection to the written pullback is correct. The same mathematical claim can be repaired without discretizing the exceptional set: keep the ambient start real throughout. Let

\[
J_X=[X-H_X,x_q],
\qquad H_X=4R_X,
\]

so `|J_X|=H_X-h_q\asymp R_X`. Since `H_X=o(X)`, for every `d<=D=(\log X)^C` and all sufficiently large `X`, every `y\in J_X` has

\[
\frac yd\in\left[\frac{X}{2d},\frac Xd\right].
\]

Apply Theorem 1.1(i) at scale `X_d=X/(2d)` with interval length `H_d=H_X/d`, the trivial nilsequence `F\equiv1`, and a fixed `epsilon>0` chosen below both `Theta-1/3` and `1-Theta`. Uniformly for polylogarithmic `d`, its hypotheses hold because `H_X=X^{\Theta+o(1)}` and `\log(X/d)\sim\log X`. Thus there is a measurable exceptional set

\[
E_d\subset [X_d,2X_d],
\qquad
m(E_d)\ll_{K'}\frac{X/d}{(\log X)^{K'}},
\]

such that for `t\notin E_d` the maximal star norm over `(t,t+H_d]` is `\ll H_d/(\log X)^{K'}`. Define the bad ambient starts by the real pullback

\[
B_d=\{y\in J_X:y/d\in E_d\}.
\]

Lebesgue scaling gives, with no floor map and no cardinality assertion,

\[
m(B_d)
=d\,m(E_d\cap(J_X/d))
\le d\,m(E_d)
\ll_{K'}\frac X{(\log X)^{K'}}.
\]

Hence

\[
m\!\left(\bigcup_{d\le D}B_d\right)
\ll \frac{DX}{(\log X)^{K'}}.
\]

For a real `y` outside this union and any consecutive integer subinterval `I\subset(y,y+H_X]`, the set

\[
P_{d,I}:=\{m\in\mathbb Z:dm\in I\}
\]

is itself a consecutive arithmetic progression contained exactly in

\[
(y/d,(y+H_X)/d]\cap\mathbb Z.
\]

Therefore the star norm in Theorem 1.1(i) controls every inner sum in the convolution simultaneously for that `y`; no endpoint rounding is actually needed. Summing `d<=D` gives

\[
\sum_{d\le D}\frac1d
\left|\sum_{m\in P_{d,I}}\mu(m)\right|
\ll
\frac{H_X}{(\log X)^{K'}}\sum_{d\le D}\frac1{d^2}
\ll
\frac{H_X}{(\log X)^{K'}}.
\]

The `d>D` tail is unchanged:

\[
\sum_{d>D}\frac1d\#P_{d,I}
\ll \frac{H_X}{D}+\log X.
\]

Thus the source-level maximal theorem survives with an exceptional set of **Lebesgue measure** `O_K(X/(\log X)^K)` after choosing `K'` larger than `C+K`; the current finding should say measure, not cardinality, in equations (10) and (13). The ambient localization step should likewise use the real interval `J_X`: if the exceptional measure is `o(R_X)`, then it cannot cover `J_X`, so some real containing start is good. For a schematic bound `m(\mathcal F_X)\ll X R_X^{-c+o(1)}`, the same exponent comparison yields `c>(1-\Theta)/\Theta`.

So the review identifies a real exposition/proof gap but not a change of claim identity or of the corridor-threshold conclusion. I am leaving the canonical finding unchanged pending adversary judgment, as required by the review protocol; if this repair is accepted, the integer-start/cardinality wording should be replaced in place by the real-start/measure argument above.

## Adversary

The objection is mathematically resolved. Keeping the ambient start real makes the pullback legitimate: Lebesgue measure scales by the factor `d`, the polylogarithmic union over `d<=D` remains absorbable in the arbitrary logarithmic exceptional exponent, and the maximal star norm controls each consecutive scaled integer progression `P_{d,I}` without converting measure into integer cardinality. The same comparison therefore preserves the corridor threshold `c>(1-Theta)/Theta`.

Closure is pending durable persistence. Please replace the canonical integer-start/cardinality pullback in the localization and convolution-transfer argument with the accepted real-start/Lebesgue-measure formulation, including the Jacobian bound for `B_d`, the simultaneous union over `d<=D`, and the statement of (10)/(13) as measure bounds. Leave the sidecar for final verification after that same-claim repair is persisted.

## Owner

The accepted real-start/Lebesgue-measure repair is now persisted in the canonical `FD-058` finding. The localization uses the real containing-start interval `J_X`; the convolution transfer uses the real pullbacks `B_d` under `y\mapsto y/d` with the Jacobian factor `d`; the union over `d<=D` is simultaneous in Lebesgue measure; and equations (10) and (13) are measure bounds. The mathematical claim and the corridor threshold `c>(1-Theta)/Theta` are unchanged. This sidecar remains for final adversary verification.