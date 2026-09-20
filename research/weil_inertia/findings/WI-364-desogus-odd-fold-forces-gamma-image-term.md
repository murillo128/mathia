# WI-364 — Desogus's odd fold forces a gamma image term

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + LOAD-BEARING-PROOF-GAP + STRONGER-REPAIR-CONSTRAINT + NON-ESTABLISHED-RH`.

## Claim

The complete odd archimedean block displayed in Marco Desogus's 17 September 2026 preprint **The Three Gates: A Rooted-Operator Approach to Weil Positivity** (`arXiv:2609.20367v1`) has an exact canonical realization on `(0,1)` containing a regular **gamma image kernel**. This term is forced by odd parity and is not present in the difference-only cancellation written in Lemma 5.2 / Proposition 5.3.

Let

\[
(Ff)(x)=\sqrt2\,f(x),\qquad 0<x<1,
\]

be the unitary identification from `L^2_odd(-1,1)` to `L^2(0,1)`. For the paper's singular Legendre form and endpoint potential,

\[
\mathfrak h[f]
=\frac14\iint_{(-1,1)^2}\frac{|f(x)-f(y)|^2}{|x-y|}\,dx\,dy,
\qquad
V(x)=-\frac12\log(1-x^2),
\]

the odd fold is exactly

\[
\boxed{F(H_{\rm Leg}+V)F^*=B+\frac12K_{\rm Carl},}
\tag{1}
\]

where

\[
\mathfrak b[g]
=\frac14\iint_{(0,1)^2}\frac{|g(x)-g(y)|^2}{|x-y|}\,dx\,dy
-\frac12\int_0^1\log(x(1-x))|g(x)|^2\,dx
\tag{2}
\]

and `K_Carl` has kernel `1/(x+y)`. The same odd fold applied to

\[
K_{\gamma,a}(x,y)=a\rho(a|x-y|),
\qquad
\rho(z)=\frac{e^{-z/2}}{1-e^{-2z}}-\frac1{2z},
\]

gives

\[
\boxed{
(FK_{\gamma,a}F^*)(x,y)
=a\rho(a|x-y|)-a\rho(a(x+y)).
}
\tag{3}
\]

Hence the full odd archimedean block is

\[
\boxed{
F(H_{\rm Leg}+c_0(a)I+V-K_{\gamma,a})F^*
=B+\frac12K_{\rm Carl}+c_0(a)I-aR_{\rm diff}+aR_{\rm sum},
}
\tag{4}
\]

with the evident difference and sum kernels.

There is a stronger exact consequence. Pairing each singular image/difference term with its gamma correction and then applying **the inverse of the paper's own exponential half-density transform** shows that the image channel becomes the nonlocal product kernel

\[
\boxed{
P(X,Y)=\frac{XY}{X^2Y^2-1}
=\frac12\left(\frac1{XY-1}+\frac1{XY+1}\right),
\qquad 1<X,Y<e^A.
}
\tag{5}
\]

Moreover

\[
P(X,Y)=\sum_{m\ge0}X^{-(2m+1)}Y^{-(2m+1)},
\tag{6}
\]

so `P` is positive semidefinite and genuinely nonlocal. Therefore **no scalar term, endpoint potential, or Jacobian multiplication correction such as the `W_A` of WI-363 can cancel this image channel**. Any repair of Proposition 5.3 must retain `P` (or an exactly equivalent nonlocal term) and separately account for the diagonal correction isolated in WI-363.

This strengthens the previous repair boundary. It does not prove that the desired positivity estimate is false: `P\succeq0`, so the omitted channel may be favorable. It does prove that the missing image term cannot disappear through the diagonal bookkeeping that remained logically possible in the earlier formulation of this finding.

## 1. Primary-source dependency under audit

The localized odd operator in `arXiv:2609.20367v1` contains

\[
\widetilde A_a
=H_{\rm Leg}+c_0(a)I+V-K_{\gamma,a}
-2|s_a\rangle\langle s_a|
-\sum_{2\le n<e^{2a}}
\frac{\Lambda(n)}{\sqrt n}(S_{r_n}+S_{r_n}^*),
\tag{7}
\]

with

\[
c_0(a)=-\log a-\log(2\pi)-\gamma,
\qquad
K_{\gamma,a}(x,y)=a\rho(a|x-y|).
\tag{8}
\]

Section 5 says that the Cauchy singular and regular gamma pieces must be transported together. Lemma 5.1 computes the transformed bare Cauchy and Carleman operator kernels, while Lemma 5.2 uses

\[
\frac1{2r}+A\rho(Ar)
=A\frac{e^{-Ar/2}}{1-e^{-2Ar}}
\tag{9}
\]

to obtain its displayed off-diagonal cancellation. Proposition 5.3 packages the result into a `Cauchy--Carleman realization` `\mathfrak c_A`, but version 1 does not give a pre-transport full-form identity from (7) in which all parity-image and multiplication channels can be checked.

The current arXiv record remains version 1 as of 20 September 2026. Primary source: Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1 (17 Sep 2026), especially the localized odd operator, the definitions of `V`, `rho`, and `c_0(a)`, Lemmas 5.1--5.2, Proposition 5.3, and the normalized collar form used in Section 4.

## 2. Exact odd fold of the singular form

Write `g=Ff`, so for `x>0`,

\[
f(x)=\frac{g(x)}{\sqrt2},
\qquad
f(-x)=-\frac{g(x)}{\sqrt2}.
\tag{10}
\]

Splitting the double integral defining `\mathfrak h` into the four sign quadrants gives

\[
\boxed{
\mathfrak h[F^{-1}g]
=
\frac14\iint_{(0,1)^2}\frac{|g(x)-g(y)|^2}{|x-y|}\,dx\,dy
+
\frac14\iint_{(0,1)^2}\frac{|g(x)+g(y)|^2}{x+y}\,dx\,dy.
}
\tag{11}
\]

The second term expands as

\[
\frac14\iint\frac{|g(x)+g(y)|^2}{x+y}\,dx\,dy
=
\frac12\langle g,K_{\rm Carl}g\rangle
+
\frac12\int_0^1\log\frac{1+x}{x}|g(x)|^2\,dx.
\tag{12}
\]

Oddness preserves the multiplication form of `V`, and

\[
\frac12\log\frac{1+x}{x}
-\frac12\log(1-x^2)
=-\frac12\log(x(1-x)).
\tag{13}
\]

Equations (11)--(13) prove (1). This calculation is valid first on a smooth odd core away from the endpoints and uses no closure or boundary-domain assumption.

## 3. Exact odd fold of the gamma operator

Put `k_a(t)=a\rho(at)`. For `x>0`, splitting positive and negative `y` gives

\[
(K_{\gamma,a}f)(x)
=
\int_0^1 k_a(|x-y|)f(y)\,dy
+
\int_0^1 k_a(x+y)f(-y)\,dy.
\tag{14}
\]

Using (10) yields (3), hence (4). At the level of off-diagonal kernels, the complete folded archimedean block is

\[
-\left[\frac1{2|x-y|}+a\rho(a|x-y|)\right]
+
\left[\frac1{2(x+y)}+a\rho(a(x+y))\right].
\tag{15}
\]

Define

\[
L_a(t):=\frac1{2t}+a\rho(at)
=a\frac{e^{-at/2}}{1-e^{-2at}}.
\tag{16}
\]

Then the folded off-diagonal kernel is simply

\[
\boxed{L_a(x+y)-L_a(|x-y|).}
\tag{17}
\]

The difference and image channels are therefore paired exactly before the exponential transport; retaining the singular Carleman image while dropping its regular gamma partner is not the canonical odd restriction of (7).

## 4. Exact exponential pullback exposes the product-Hankel image

Now set `a=A` and use precisely the half-density unitary of Section 5,

\[
(U_Af)(u)=\sqrt{Ae^{Au}}\,f(e^{Au}),
\qquad 0<u<1.
\tag{18}
\]

Write

\[
X=e^{Au},\qquad Y=e^{Av}.
\]

If `K(u,v)` is an integral kernel after conjugation by `U_A`, its pullback kernel on `(1,e^A)` is

\[
\frac{K(u,v)}{A\sqrt{XY}}.
\tag{19}
\]

For the difference channel, assume first `X>Y`. Then

\[
\frac{L_A(u-v)}{A\sqrt{XY}}
=
\frac{X}{X^2-Y^2}
=
\frac12\left(\frac1{X-Y}+\frac1{X+Y}\right).
\tag{20}
\]

By symmetry,

\[
\boxed{
\frac{L_A(|u-v|)}{A\sqrt{XY}}
=
\frac12\left(\frac1{|X-Y|}+\frac1{X+Y}\right).
}
\tag{21}
\]

This is exactly the Cauchy--Carleman half-sum of Lemma 5.1, read in reverse.

The image channel is different. Since `e^{A(u+v)}=XY`,

\[
\boxed{
\frac{L_A(u+v)}{A\sqrt{XY}}
=
\frac{XY}{X^2Y^2-1}
=P(X,Y).
}
\tag{22}
\]

Consequently the complete canonical odd archimedean **off-diagonal** kernel in the pre-transport `(X,Y)` coordinates is

\[
\boxed{
P(X,Y)
-
\frac12\left(\frac1{|X-Y|}+\frac1{X+Y}\right).
}
\tag{23}
\]

The image term has not become a scalar or endpoint correction; it has become a product-variable Hankel kernel. Its series (6) converges for `X,Y>1`, and for any compactly supported smooth `f` inside `(1,e^A)`,

\[
\langle f,Pf\rangle
=
\sum_{m\ge0}
\left|\int_1^{e^A}X^{-(2m+1)}f(X)\,dX\right|^2
\ge0.
\tag{24}
\]

Thus `P` is an explicit positive nonlocal channel. Apart from restricting its domain to `(1,e^A)`, its kernel is independent of `A`.

## 5. Diagonal corrections cannot cancel the image channel

The scalar `c_0(a)I`, the endpoint potential, and the correction `W_A` from WI-363 are multiplication operators after the relevant coordinate changes. They therefore cannot cancel `P` as a quadratic form.

Indeed, choose nonzero nonnegative smooth `f,h` with disjoint compact supports in `(1,e^A)`. For every multiplication operator `M`,

\[
\langle f,Mh\rangle=0,
\tag{25}
\]

whereas `P(X,Y)>0` throughout the open square, so

\[
\langle f,Ph\rangle>0.
\tag{26}
\]

Hence no diagonal correction can satisfy `P+M=0` on a common core. In particular, the repair possibility left open by the earlier formulation of WI-364 — cancellation of the gamma image by scalar/endpoint/Jacobian terms — is now ruled out exactly.

Equation (7) already lists the complete archimedean nonlocal pieces being folded: `H_Leg` and `K_{\gamma,a}`. Therefore an exact `\mathfrak c_A` representing that block must either contain `P` explicitly or exhibit another **nonlocal** term exactly equivalent to it. If `P` is intended to be hidden inside the undefined `Cauchy--Carleman realization`, that identity has to be stated and then carried through the subsequent lower-bound argument; Lemma 5.2's displayed difference-only cancellation does not supply it.

The sign matters for the claim boundary. Since `P\succeq0`, this calculation does not show that adding the missing term destroys positivity. It may instead provide extra reserve. What fails is the claimed provenance of the exact normalized one-cell form: Section 4's one-defect and Carleman estimates are stated for a particular collar operator, and version 1 does not derive how the actual `P` channel is retained, discarded by a justified lower bound, or absorbed into an exactly equivalent nonlocal realization in that normalization.

## 6. Repair criterion and boundary

A valid repair of the source-to-cell bridge must now do four separate things: derive `\mathfrak c_A` explicitly from the full odd fold (4); retain `P` or an exactly equivalent nonlocal image term; account independently for the multiplication correction `W_A` and the transformed scalar/endpoint terms; and then prove the required equality or lower-form comparison with the normalized collar operator used by the downstream common-cut and rooted-Schur estimates.

Thus the current source-level conclusion sharpens to

\[
\boxed{
\begin{gathered}
\text{the normalized one-cell form used downstream is still not derived from the full odd}\
\text{archimedean block in v1, and its missing image channel cannot be removed by diagonal corrections.}
\end{gathered}
}
\tag{27}
\]

This finding does **not** assert that the exact localized operator (7) is wrong, that the desired positivity theorem cannot be repaired, that the positive `P` channel itself causes a negative direction, that WI-362's conditional common-cut/rooted-Schur algebra is wrong, or that RH is false. WI-362 remains a valid conditional audit once the correct one-cell lower model is supplied.

The decisive repair test is no longer merely whether `W_A` and the gamma image might cancel each other: they cannot, because they have different operator type. The remaining source-level questions are whether the positive nonlocal `P` can be retained as reserve or rigorously dropped in the needed lower-form direction, and whether the genuinely diagonal `W_A` is then cancelled or controlled by the transformed scalar/endpoint terms.

## 7. Prior-art and novelty audit

A fresh targeted search on 20 September 2026 found the primary Desogus submission and generic listings/mirrors but no independent technical discussion resolving this parity-image / half-density bookkeeping issue. Absence from that limited search is not evidence of priority or of absence from the literature.

The parity reduction (3), kernel conjugation (19), product expansion (6), and positivity argument (24) are elementary operator algebra and are not claimed as new general theorems. The durable contribution is the source-specific audit: applying those exact identities to the load-bearing bridge in `arXiv:2609.20367v1` converts an unspecified possible cancellation into a strict repair constraint. This is a strengthening of the same WI-364 claim identity, not a new finding.

WI-361 marked the normalized-form bridge as unresolved, WI-362 audited later steps conditional on that bridge, and WI-363 isolated the independent half-density multiplication potential. WI-364 now separates the two obligations completely: the image defect is nonlocal and survives every purely diagonal repair, while the Jacobian defect is diagonal and must be settled on its own.

## Consequence for the research line

The highest-value Desogus audit remains upstream of the numerical certificates. The next pass should not ask whether `W_A` can cancel the gamma image: equation (26) closes that possibility. It should determine the exact disposition of the positive product-Hankel channel `P` in the source's intended `\mathfrak c_A`, and separately test the scalar/endpoint cancellation of `W_A`. Only after both channels are connected rigorously to the Section 4 one-cell lower model should the audit resume at the common-cut/certificate/globalization gates.