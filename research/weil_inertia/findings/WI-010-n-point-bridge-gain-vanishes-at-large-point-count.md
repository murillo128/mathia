# WI-010 — the current n-point sliding-window bridge has vanishing gain as the point count grows

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the strategy of obtaining a fixed positive improvement over the Montgomery--Taylor baseline by sending the local point count `n -> infinity` inside the present `Zeta23Ext.Bridge.n_point_bound` sliding-window architecture. This is not a no-go theorem for all Gram-defect, multi-profile, or bandwidth-one methods.

## 1. Exact input: the formally proved n-point bridge

The public `teal-sea/zeta-lab` development has made the Ainta sliding-window bridge parametric in the local point count. At revision `c02ad1a56ce18d99c326d87e9318d064621d3fea`, `Zeta23Ext.Bridge.n_point_bound` is a Lean theorem for every integer

\[
n\ge2,
\]

with parameters `c>0`, `m>=n`, `p>0`, a finite local certificate

\[
F_n(g;p)\ge c
\qquad(g_i\ge0),
\tag{1}
\]

and the block-cap side condition

\[
\boxed{
 c\bigl(m-(n-1)\bigr)\le1.
}
\tag{2}
\]

Its asymptotic proportion is

\[
\boxed{
\Phi_n(c,m,p)
=
\frac{
H_{\rm MT}-\dfrac{(n-1)(m-1)}{pm}
}{
1-\dfrac{c(m-(n-1))}{m}
},
}
\tag{3}
\]

where

\[
H_{\rm MT}
=
\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}
=0.6725007036794116\ldots.
\tag{4}
\]

The analytic bridge from (1)--(2) to (3) is kernel-checked in Lean. For the larger seven- and eight-point numerical examples, the finite certificate (1) remains an external interval-arithmetic hypothesis rather than a Lean theorem; the distinction is immaterial for the algebraic obstruction below, which assumes only the bridge's stated hypotheses.

## 2. Exact gain identity

Put

\[
r=n-1,
\qquad
q=m-r=m-(n-1),
\qquad
x=cq.
\tag{5}
\]

Since `m>=n`, one has `q>=1`; since `c>0` and (2) holds,

\[
0<x\le1.
\tag{6}
\]

Equation (3) becomes

\[
\Phi_n
=
\frac{mH_{\rm MT}-r(m-1)/p}{m-x}.
\tag{7}
\]

Subtracting the baseline gives the exact identity

\[
\boxed{
\Phi_n-H_{\rm MT}
=
\frac{
H_{\rm MT}x-\dfrac{r(m-1)}p
}{m-x}.
}
\tag{8}
\]

There is no kernel estimate, asymptotic approximation, or optimization assumption in (8): it is just the exact formally stated bridge formula plus the change of variables (5).

The identity separates the two competing effects of the local certificate. The numerator gains at most `H_MT x` from defect retention, while the sliding-window pressure ledger pays the explicit cost `r(m-1)/p`. The block cap prevents `x` from exceeding one.

## 3. Universal O(1/n) ceiling on the gain

Because the pressure cost in (8) is nonnegative, `x<=1`, and `m-x>=m-1>0`,

\[
\begin{aligned}
\Phi_n-H_{\rm MT}
&\le
\frac{H_{\rm MT}x}{m-x}\\
&\le
\frac{H_{\rm MT}}{m-1}\\
&\le
\boxed{\frac{H_{\rm MT}}{n-1}}.
\end{aligned}
\tag{9}
\]

Equivalently,

\[
\boxed{
\Phi_n(c,m,p)
\le
H_{\rm MT}\frac{n}{n-1}
}
\tag{10}
\]

for every admissible finite certificate and every admissible choice of `m,p,c` in this bridge.

Consequently, for any sequence of admissible n-point instances with `n -> infinity`, even if the local certificates themselves were perfect,

\[
\boxed{
\limsup_{n\to\infty}\Phi_n\le H_{\rm MT}.
}
\tag{11}
\]

Thus **increasing the local point count without bound cannot yield a fixed positive improvement over the Montgomery--Taylor baseline inside this particular sliding-window assembly**. Any gain produced by this bridge is intrinsically a finite-`n` phenomenon, or else the assembly/cap itself must be changed.

A useful equivalent form is that a desired fixed gain `delta>0`,

\[
\Phi_n\ge H_{\rm MT}+\delta,
\]

requires

\[
\boxed{
n<1+\frac{H_{\rm MT}}\delta.
}
\tag{12}
\]

No amount of strengthening the finite certificate at larger `n` can evade (12) while retaining (2)--(3).

## 4. Positive gain also forces at least quadratic pressure scaling

Equation (8) gives another exact necessary condition. If

\[
\Phi_n>H_{\rm MT},
\]

then its numerator must be positive:

\[
H_{\rm MT}x>rac{r(m-1)}p.
\tag{13}
\]

Since `x<=1`,

\[
p>rac{r(m-1)}{H_{\rm MT}}.
\tag{14}
\]

And because `m>=n`, hence `m-1>=r=n-1`,

\[
\boxed{
 p>\frac{(n-1)^2}{H_{\rm MT}}.
}
\tag{15}
\]

So a pressure denominator that is fixed, linear in `n`, or more generally `o(n^2)` cannot keep this bridge above the baseline for arbitrarily large point count. For a fixed `p`, positive gain is possible only while

\[
 n-1<\sqrt{H_{\rm MT}p}.
\tag{16}
\]

This is independent of the detailed Montgomery--Taylor kernel geometry. It is a constraint imposed by the global sliding-window bookkeeping after a local certificate has already been granted.

## 5. Relation to the current finite-point improvements

WI-009 records the unconditional four-point theorem, where the local inequality itself is proved in Lean and yields

\[
0.6728470197666888\ldots.
\]

The same public development now has a general Lean bridge and reports stronger finite-point candidate instances. In particular, an eight-point interval verifier accepts

\[
(n,c,m,p)
=
\left(8,\frac{41763}{10^7},246,3200\right),
\]

and the Lean bridge converts that **conditional-on-the-certificate** input to

\[
\frac{2460000000H_{\rm MT}-5359375}{2450018643}
=0.67305298298962888\ldots.
\tag{17}
\]

The public state-of-record correctly does not classify (17) as an unconditional kernel-checked theorem because the eight-point certificate is still a named hypothesis. Equation (9) does not conflict with these finite gains. It says something different and asymptotic: continuing to raise `n` forever cannot accumulate a nonzero limiting gain through the same bridge.

The laboratory's numerical exploration already describes the n-point family as shallow and observes rapidly growing certificate cost. Equations (8)--(16) give a separate exact reason why the strategy must eventually stop being a route to a fixed improvement even under arbitrarily strong finite certificates.

## 6. Prior-art and novelty audit

No novelty is claimed for the algebra in (8)--(16). The source theorem is the public zeta-lab n-point bridge, and the block cap (2) is part of that theorem's stated contract. The new durable point for Mathia is the **scope consequence** obtained by combining them: the current local-certificate/sliding-window assembly itself imposes an `O(1/n)` ceiling on improvement and a quadratic lower bound on the pressure scale required for any improvement.

This must not be conflated with broader recent claims about ceilings for the full Montgomery--Taylor Gram machinery. In particular, Michael Devine's August 2026 preprints claim stronger thermodynamic-limit obstructions for pure fixed-kernel Gram/rank methods. Those claims remain `NEEDS-AUDIT` in this research line and are not used here. WI-010 is narrower but exact relative to the formally specified bridge.

Nor does WI-010 obstruct a method that changes one of the load-bearing ingredients, for example:

- a different aggregation than overlapping blocks of `n` consecutive zeros;
- cumulative or transfer-operator inequalities that do not pay the same `(n-1)(m-1)/(pm)` ledger;
- multiple profiles with joint constraints;
- a new defect functional with a different cap;
- new prime-side information or support beyond one.

## 7. Adversarial checks and boundary cases

Several apparent loopholes do not affect the claim.

**Take `m` much larger than `n`.** This only strengthens (9), because `H_MT/(m-1)` decreases with `m`.

**Saturate the certificate cap.** Setting `x=1` maximizes the retained-defect contribution allowed by (2), but still gives at most `H_MT/(m-1)` before the pressure cost is subtracted.

**Send `p` to infinity.** This can remove the explicit pressure penalty from (8), but cannot remove the cap-induced ceiling `H_MT/(m-1)`. Thus even a hypothetical zero-cost pressure ledger does not defeat (11).

**Improve the finite certificate `c`.** Once `cq` reaches one, the cap prevents any further benefit from entering the denominator. A larger raw local lower bound must then be spent by reducing `q=m-(n-1)` or otherwise changing parameters; it cannot make `x>1` inside this theorem.

**Let parameters depend on `n`.** Equations (9)--(11) are uniform in `c,m,p` subject only to the theorem hypotheses, so dependence on `n` does not change the conclusion.

A falsification of WI-010 within the same architecture would therefore require either an error in the published/formal formula (3), an instance violating the cap (2) while still satisfying the theorem, or an algebraic error in (8). None is present in the checked source statement.

## 8. Research consequence

The strategy

\[
\boxed{
\text{increase }n
\to
\text{certify ever larger local blocks}
\to
\text{accumulate a fixed asymptotic gain}
}
\]

is closed for the current `n_point_bound` assembly.

This changes the useful question. Further finite `n` optimization can still improve the numerical record, but **large point count is not itself a route toward a qualitatively stronger bound**. To extract a nonvanishing new fraction from bandwidth-one Gram geometry, one must eventually alter the global assembly rather than merely make its local certificate larger.

The most relevant surviving possibility is therefore to retain the local Gram-defect insight of WI-009 while replacing the sliding-window pressure/cap bookkeeping by a genuinely global variational, cumulative, transfer-matrix, or dual formulation. Such a formulation should be judged first by whether its analogue of (8) avoids an `O(1/n)` cap before investing in expensive finite certification.