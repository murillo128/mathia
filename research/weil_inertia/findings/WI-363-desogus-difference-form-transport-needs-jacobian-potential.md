# WI-363 — Desogus's difference-form transport acquires a nonzero Jacobian potential

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + LOAD-BEARING-PROOF-GAP + NON-ESTABLISHED-RH`.

## Claim

Proposition 5.3 of Marco Desogus's 17 September 2026 preprint **The Three Gates: A Rooted-Operator Approach to Weil Positivity** (`arXiv:2609.20367v1`) does not, as written, establish the claimed exact full-form transport into the normalized logarithmic collar form.

The issue is already visible in the singular difference form used in the proposition's proof. Under the paper's half-density unitary

\[
(U_A f)(u)=\sqrt{A e^{Au}}\,f(e^{Au}),\qquad 0<u<1,
\]

the Cauchy difference form

\[
q_C[f]=\frac14\iint_{(1,e^A)^2}
\frac{|f(x)-f(y)|^2}{|x-y|}\,dx\,dy
\]

does **not** become the same difference form with the transported symmetric kernel from Lemma 5.1. It acquires an additional, explicitly nonzero multiplication term:

\[
\boxed{
q_C[U_A^{-1}g]
=
\frac14\iint_{(0,1)^2}K_A(u,v)|g(u)-g(v)|^2\,du\,dv
+
\int_0^1 W_A(u)|g(u)|^2\,du,
}
\tag{1}
\]

where

\[
K_A(u,v)
=
\frac{A e^{-A|u-v|/2}}{1-e^{-A|u-v|}}
=
\frac{A}{2\sinh(A|u-v|/2)},
\tag{2}
\]

and

\[
\boxed{
W_A(u)
=
\frac{A(1-u)}2-2\log2
+\log\!\left(1+e^{-A(1-u)/2}\right)
+\log\!\left(1+e^{-Au/2}\right).
}
\tag{3}
\]

In particular

\[
\boxed{W_A(0)-W_A(1)=\frac A2>0,}
\tag{4}
\]

so this is not a removable zero term.

Lemma 5.1 correctly computes the transported **off-diagonal operator kernel**. That calculation is not enough to transport the closed difference form, because the half-density factors multiplying the two diagonal pieces of `|f(x)-f(y)|^2` are different. Proposition 5.3's proof treats those two statements as if they were the same.

This finding is a proof-gap result, not a proof that the preprint's final full-form identity is false. A repair remains logically possible if the author shows that the exact transform of the other multiplication/scalar pieces of the complete archimedean block cancels `W_A` with the required normalization. Version 1 does not supply that identity. Until such a cancellation is derived independently, the normalized one-cell form used downstream by the common-cut and rooted-Schur argument is not established from the localized Weil operator.

This sharpens the conditional boundary of WI-362: the common-cut/inherited-pivot chain may be exact **given** the normalized one-cell form, while the upstream bridge from the actual localized archimedean block to that form remains load-bearing and currently unverified.

## 1. Primary-source dependency under audit

The relevant chain in `arXiv:2609.20367v1` is:

- Lemma 5.1 transports the bare Cauchy and Carleman operator kernels under `U_A`;
- Lemma 5.2 cancels the regular off-diagonal gamma kernel against the regular part of their transported half-sum;
- Proposition 5.3 then claims that the **complete quadratic form**, including the singular diagonal/killing contribution, is carried by the same unitary to the logarithmic collar form and that no additional diagonal term is introduced;
- the proof of Proposition 5.3 explicitly writes the singular piece as
  \[
  \frac14\iint |f(x)-f(y)|^2/|x-y|
  \]
  and says that transforming the measure, function factors and kernel simultaneously is handled by Lemma 5.1.

Downstream, the argument repeatedly uses the normalized one-cell boundary/collar form

\[
\mathfrak b[g]
=
\frac14\iint_{(0,1)^2}
\frac{|g(u)-g(v)|^2}{|u-v|}\,du\,dv
-
\frac12\int_0^1\log(u(1-u))|g(u)|^2\,du.
\tag{5}
\]

Thus Proposition 5.3 is not a cosmetic coordinate statement. It is the bridge by which the source-capacity estimates, one-defect bound, fixed-target short and later MASTER same-vector bookkeeping are asserted to apply to the actual localized Weil form.

Primary source: Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1 (17 Sep 2026), especially equations (49), (55)--(61) and Proposition 5.3.

## 2. Exact transform of the singular difference form

Set

\[
x=e^{Au},\qquad y=e^{Av},\qquad J(u)=Ae^{Au},
\]

and write `g=U_A f`, so

\[
f(e^{Au})=\frac{g(u)}{\sqrt{J(u)}}.
\]

After the change of variables, the integrand of `q_C` is

\[
\frac{J(u)J(v)}{|e^{Au}-e^{Av}|}
\left|
\frac{g(u)}{\sqrt{J(u)}}-
\frac{g(v)}{\sqrt{J(v)}}
\right|^2.
\tag{6}
\]

Define

\[
K_A(u,v)
:=
\frac{\sqrt{J(u)J(v)}}{|e^{Au}-e^{Av}|}.
\tag{7}
\]

This is exactly the symmetric kernel computed in Lemma 5.1, giving (2). Expanding (6), however, gives

\[
\frac{J(v)}{|e^{Au}-e^{Av}|}|g(u)|^2
+
\frac{J(u)}{|e^{Au}-e^{Av}|}|g(v)|^2
-
2K_A(u,v)\operatorname{Re}(g(u)\overline{g(v)}).
\tag{8}
\]

The cross term agrees with the difference form built from `K_A`. The diagonal coefficient does not: that difference form would contain `K_A(u,v)|g(u)|^2`, whereas the exact transform contains

\[
\frac{J(v)}{|e^{Au}-e^{Av}|}|g(u)|^2.
\]

Symmetrizing the two diagonal pieces therefore yields the exact identity (1), with

\[
W_A(u)
=
\frac12\int_0^1
\left[
\frac{J(v)}{|e^{Au}-e^{Av}|}-K_A(u,v)
\right]dv.
\tag{9}
\]

This calculation is valid first on a smooth compactly supported core away from the endpoints, so no closure or boundary-domain issue is being used to manufacture the correction.

## 3. Closed form of the missing multiplication term

For `v>u`, put `r=v-u`. Then

\[
\frac{J(v)}{|e^{Au}-e^{Av}|}-K_A(u,v)
=
\frac{A}{1+e^{-Ar/2}}.
\tag{10}
\]

For `v<u`, with `r=u-v`,

\[
\frac{J(v)}{|e^{Au}-e^{Av}|}-K_A(u,v)
=
-\frac{A}{1+e^{Ar/2}}.
\tag{11}
\]

Consequently

\[
W_A(u)
=
\frac A2
\left[
\int_0^{1-u}\frac{dt}{1+e^{-At/2}}
-
\int_0^u\frac{dt}{1+e^{At/2}}
\right],
\tag{12}
\]

which integrates to (3). An equivalent form, useful for separating the asymmetric and symmetric pieces, is

\[
W_A(u)
=
\frac{A(1-2u)}4
+
\log\cosh\!\left(\frac{Au}{4}\right)
+
\log\cosh\!\left(\frac{A(1-u)}4\right).
\tag{13}
\]

Equation (4) follows immediately. Thus the correction is not an endpoint distribution, a closure artifact, or a quantity that vanishes on the smooth core. It is a genuine bounded multiplication term for every `A>0`.

A simple conceptual check is that a constant `g` makes the `K_A`-difference form vanish, while `U_A^{-1}g` is proportional to `x^{-1/2}` and is not constant in the original variable; its original Cauchy difference energy is therefore positive. The missing multiplication term is exactly what reconciles those two facts.

## 4. Why Lemma 5.1 does not remove this term

Lemma 5.1 is correct as a statement about the integral kernel of an operator under half-density conjugation:

\[
K(x,y)\mapsto \sqrt{J(u)J(v)}K(e^{Au},e^{Av}).
\]

A closed difference form is different. Its diagonal part is generated by integrating the kernel against `|f(x)|^2`, and after a nonconstant half-density change the coefficient uses `J(v)`, not `\sqrt{J(u)J(v)}`. Therefore a nonconstant coordinate change generally converts

\[
\iint K(x,y)|f(x)-f(y)|^2
\]

into a transported symmetric difference form **plus a multiplication correction**.

This is precisely the distinction Proposition 5.3 needed to check. The sentence that the diagonal contribution is "already contained in the square" does not make the difference form covariant under `U_A`; expansion of that same square gives (8)--(9).

Lemma 5.2 only identifies the regular **off-diagonal** cancellation

\[
\tfrac12(K_{\rm Cauchy}^{(A)}+K_{\rm Carl}^{(A)})
-A\rho(A|u-v|)
=rac1{2|u-v|}
\qquad(u\ne v).
\]

It therefore cannot, by itself, determine the multiplication term (9). The paper in fact notes that the diagonal/killing part must be handled by Proposition 5.3; the direct calculation above shows that this is exactly the unresolved step.

## 5. What would repair the bridge

The full archimedean block also contains scalar and multiplication terms (`c_0 I+V`) and the Carleman/gamma pieces. It is therefore logically possible that, after expressing **all** of these terms in the same pre-transport realization and conjugating them explicitly, their multiplication contribution cancels `W_A` and leaves exactly the normalized collar potential in (5).

A valid repair must exhibit an identity of the form

\[
U_A\,(H_{\rm Leg}+c_0I+V-K_{\gamma,A})\,U_A^*
=
\text{the claimed logarithmic collar operator},
\tag{14}
\]

on a common core, with the multiplication part shown explicitly. In particular it must account for (3), rather than infer the diagonal from the off-diagonal kernel transform.

Version 1 does not write the Cauchy--Carleman realization `\mathfrak c_A` as an explicit full quadratic form before transport, does not display the transformed `c_0+V` multiplier in the `u` coordinate, and does not state a cancellation formula containing `W_A`. Closure cannot supply the missing algebra: it can preserve an identity already proved on a core, but it cannot turn the false kernel-only difference-form transformation into that identity.

Therefore the current audit result is:

\[
\boxed{
\text{the downstream normalized collar argument remains conditional on an upstream identity that Proposition 5.3 does not prove as written.}
}
\tag{15}
\]

## 6. Stress tests and claim boundary

This finding does **not** assert any of the following:

- that the exact localized Weil operator formula (60) is false;
- that a correct full-form Cauchy--Carleman transport cannot exist;
- that the additional term (3) necessarily has the wrong sign for the final argument;
- that the common-cut, inherited-pivot, or MASTER algebra audited in WI-362 fails once the normalized one-cell form is granted;
- or that the Riemann hypothesis is false.

It establishes the narrower load-bearing point that the proof supplied for Proposition 5.3 omits a nonzero term and therefore does not justify the bridge on which the later normalized-cell estimates depend.

The decisive falsification/repair test is equally narrow: derive the complete pre-transport archimedean form with all scalar/multiplication terms, conjugate it by `U_A`, and either (a) show an exact cancellation of `W_A` yielding the advertised collar form, or (b) retain the surviving multiplier and propagate it through the common-cut/Schur argument. Until one of those is done, the claimed RH theorem cannot be imported into Mathia's established evidence base.

## 7. Prior-art and novelty audit

A fresh search on 20 September 2026 located the primary arXiv submission and mirrors/listings but no independent technical discussion resolving Proposition 5.3. This absence is not evidence that no critique exists.

The kernel-versus-difference-form distinction itself is elementary change-of-variables algebra, not a novelty claim. Mathia's durable contribution here is the explicit audit of the particular load-bearing bridge in `arXiv:2609.20367v1`, including the exact correction (3) and the resulting repair criterion.

WI-361 had already listed the upstream normalized-form identification as an unresolved audit gate, and WI-362 deliberately conditioned its positive common-cut audit on that form. WI-363 is therefore not a duplicate: it converts that generic unresolved gate into an exact, falsifiable obstruction in the proof currently supplied.

## Consequence for the research line

The immediate priority is no longer to treat the normalized collar form as merely awaiting a routine provenance check. The next analytic pass should reconstruct the **complete** archimedean quadratic form before the exponential half-density transform and determine whether the explicit Jacobian potential `W_A` cancels against the transformed scalar/endpoint terms.

If the cancellation exists, it should be recorded as the missing durable bridge and the Desogus audit can proceed to the remaining global/certificate gates. If it does not, Proposition 5.3 and every downstream use of the exact normalized one-cell form require correction; that would block the current claimed RH chain at a point strictly upstream of the already-validated conditional algebra in WI-362.