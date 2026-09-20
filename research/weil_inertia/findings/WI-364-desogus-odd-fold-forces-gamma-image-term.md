# WI-364 — Desogus's odd fold forces a gamma image term

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + LOAD-BEARING-PROOF-GAP + NON-ESTABLISHED-RH`.

## Claim

The complete odd archimedean block displayed in Marco Desogus's 17 September 2026 preprint **The Three Gates: A Rooted-Operator Approach to Weil Positivity** (`arXiv:2609.20367v1`) has an exact canonical realization on `(0,1)` that contains an additional **gamma image kernel**. This term is forced by odd parity and is not present in the cancellation written in Lemma 5.2 / Proposition 5.3.

Let

\[
(Ff)(x)=\sqrt2\,f(x),\qquad 0<x<1,
\]

be the unitary identification from `L^2_odd(-1,1)` to `L^2(0,1)`. For the paper's singular Legendre form

\[
\mathfrak h[f]
=\frac14\iint_{(-1,1)^2}
\frac{|f(x)-f(y)|^2}{|x-y|}\,dx\,dy
\]

and endpoint potential

\[
V(x)=-\frac12\log(1-x^2),
\]

the odd fold is exactly

\[
\boxed{
F(H_{\rm Leg}+V)F^*
=B+\frac12K_{\rm Carl},
}
\tag{1}
\]

in quadratic-form sense, where `B` is precisely the logarithmic collar form used later in the paper,

\[
\mathfrak b[g]
=\frac14\iint_{(0,1)^2}
\frac{|g(x)-g(y)|^2}{|x-y|}\,dx\,dy
-\frac12\int_0^1\log(x(1-x))|g(x)|^2\,dx,
\tag{2}
\]

and `K_Carl` is the Carleman operator with kernel `1/(x+y)`.

However the same odd fold applied to the paper's regular gamma operator

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

Thus the full odd archimedean block from the paper's explicit localized operator is

\[
\boxed{
F(H_{\rm Leg}+c_0(a)I+V-K_{\gamma,a})F^*
=
B+\frac12K_{\rm Carl}+c_0(a)I
-aR_{\rm diff}+aR_{\rm sum},
}
\tag{4}
\]

where `R_diff` has kernel `rho(a|x-y|)` and `R_sum` has kernel `rho(a(x+y))`.

The image term `+aR_sum` is not optional bookkeeping: it is the parity image of the gamma kernel, just as the Carleman kernel is the parity image of the singular Cauchy kernel. Lemma 5.2 cancels the regular part of a Cauchy--Carleman half-sum against only the **difference** gamma term `A rho(A|u-v|)`. Proposition 5.3 does not write an explicit full pre-transport form showing where the corresponding image gamma term in (3)--(4) is absorbed or cancelled.

This is a second exact upstream bookkeeping gap, distinct from WI-363's Jacobian multiplication potential. It does **not** prove that the desired normalized collar identity is false: a repaired realization could in principle reassign or cancel the image term together with the other scalar, endpoint, or Carleman pieces. But version 1 does not supply that identity. Any repair of Proposition 5.3 must now account simultaneously for the gamma image term in (3) and the nonconstant half-density correction `W_A` isolated in WI-363.

## 1. Primary-source dependency under audit

The relevant source formulas in `arXiv:2609.20367v1` are the localized archimedean terms and odd operator preceding the transport section, together with Lemmas 5.1--5.2 and Proposition 5.3. In the paper's notation the localized odd operator contains

\[
\widetilde A_a
=H_{\rm Leg}+c_0(a)I+V-K_{\gamma,a}
-2|s_a\rangle\langle s_a|
-\sum_{2\le n<e^{2a}}
\frac{\Lambda(n)}{\sqrt n}(S_{r_n}+S_{r_n}^*),
\tag{5}
\]

with

\[
c_0(a)=-\log a-\log(2\pi)-\gamma,
\qquad
K_{\gamma,a}(x,y)=a\rho(a|x-y|).
\tag{6}
\]

Section 5 explicitly says that the Cauchy singular and regular gamma pieces must be transported together. Lemma 5.1 computes transformed bare Cauchy and Carleman kernels; Lemma 5.2 then uses

\[
\frac1{2r}+A\rho(Ar)
=
A\frac{e^{-Ar/2}}{1-e^{-2Ar}}
\tag{7}
\]

to obtain its off-diagonal cancellation. Proposition 5.3 packages the full result into a `Cauchy--Carleman realization` `\mathfrak c_A`, but does not provide a pre-transport formula for that realization from which every parity image and diagonal term can be checked.

Primary source: Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1 (17 Sep 2026), especially the localized odd operator, equations defining `V`, `rho`, and `c_0(a)`, Lemmas 5.1--5.2, and Proposition 5.3.

## 2. Exact odd fold of the singular form

Write `g=Ff`, so for `x>0`,

\[
f(x)=\frac{g(x)}{\sqrt2},
\qquad
f(-x)=-\frac{g(x)}{\sqrt2}.
\tag{8}
\]

Split the double integral defining `\mathfrak h` into the four sign quadrants. The two same-sign quadrants give the ordinary Cauchy difference form and the two opposite-sign quadrants give a plus-square term. Exactly,

\[
\boxed{
\mathfrak h[F^{-1}g]
=
\frac14\iint_{(0,1)^2}
\frac{|g(x)-g(y)|^2}{|x-y|}\,dx\,dy
+
\frac14\iint_{(0,1)^2}
\frac{|g(x)+g(y)|^2}{x+y}\,dx\,dy.
}
\tag{9}
\]

Expanding the second term gives

\[
\frac14\iint
\frac{|g(x)+g(y)|^2}{x+y}\,dx\,dy
=
\frac12\langle g,K_{\rm Carl}g\rangle
+
\frac12\int_0^1
\log\frac{1+x}{x}|g(x)|^2\,dx.
\tag{10}
\]

Oddness preserves the multiplication form of `V`, hence

\[
\langle F^{-1}g,VF^{-1}g\rangle
=-\frac12\int_0^1\log(1-x^2)|g(x)|^2\,dx.
\tag{11}
\]

The two diagonal potentials combine without approximation:

\[
\frac12\log\frac{1+x}{x}
-\frac12\log(1-x^2)
=-\frac12\log(x(1-x)).
\tag{12}
\]

Equations (9)--(12) prove (1). In particular, the endpoint potential in the paper's collar form is not an unexplained extra term: it is exactly the diagonal contribution generated by the cross-sign singular form together with `V`.

This calculation is valid first on a smooth odd core away from the endpoints. No closure, extension, or boundary-domain assumption is needed for the identity.

## 3. Exact odd fold of the gamma operator

Let

\[
k_a(t)=a\rho(at).
\]

For `x>0`, split the action of the even-difference kernel on `(-1,1)` into positive and negative `y`:

\[
(K_{\gamma,a}f)(x)
=
\int_0^1 k_a(|x-y|)f(y)\,dy
+
\int_0^1 k_a(x+y)f(-y)\,dy.
\tag{13}
\]

Using oddness from (8), then applying the factor `\sqrt2` from `F`, yields

\[
(FK_{\gamma,a}F^*g)(x)
=
\int_0^1
\left[k_a(|x-y|)-k_a(x+y)\right]g(y)\,dy.
\tag{14}
\]

This is (3). The second term is the unavoidable parity image. It is generated by the same cross-sign quadrant that generates the Carleman term in (9), but now for the regular gamma kernel.

Combining (1), (3), and the scalar `c_0(a)I` proves the full archimedean identity (4).

At the level of off-diagonal integral kernels, (4) reads

\[
-\left[
\frac1{2|x-y|}+a\rho(a|x-y|)
\right]
+
\left[
\frac1{2(x+y)}+a\rho(a(x+y))
\right].
\tag{15}
\]

Using the definition of `rho`, each bracket has the exact closed form

\[
\frac1{2t}+a\rho(at)
=
a\frac{e^{-at/2}}{1-e^{-2at}}.
\tag{16}
\]

Therefore the complete folded off-diagonal kernel is

\[
\boxed{
a\frac{e^{-a(x+y)/2}}{1-e^{-2a(x+y)}}
-
a\frac{e^{-a|x-y|/2}}{1-e^{-2a|x-y|}}.
}
\tag{17}
\]

The difference and image channels are thus paired exactly at the level of the full odd archimedean block.

## 4. Why the displayed Lemma 5.2 cancellation is incomplete for the canonical odd block

The paper's Lemma 5.1 correctly identifies the bare Cauchy and Carleman kernels after its exponential substitution, and Lemma 5.2 correctly performs the scalar identity (7) for the kernels it displays. The issue is one of provenance of the **full odd operator**.

Starting from (5), the Carleman channel does not appear in isolation: it is generated by folding the cross-sign part of `H_Leg`. Once that same unitary restriction is applied to `K_{\gamma,a}`, the cross-sign part of the gamma operator generates `-a\rho(a(x+y))` inside `FK_{\gamma,a}F^*`, hence `+aR_sum` after the minus sign in (5). One cannot retain the singular parity image `1/(x+y)` while discarding the regular parity image `rho(a(x+y))` without an additional identity or a different explicitly specified realization.

Lemma 5.2's written cancellation contains a regular gamma correction only as a function of `|u-v|`. Proposition 5.3 invokes a `Cauchy--Carleman realization` but does not derive it from (5) in a formula that exhibits the image term (3). Consequently, the cancellation shown there is not yet a derivation of the full canonical odd-folded block (4).

This is independent of the issue in WI-363. WI-363 shows that a nonconstant half-density transport of a **difference form** creates a multiplication correction even when its off-diagonal transformed kernel is correct. WI-364 shows an earlier parity bookkeeping fact: before that exponential transport is even considered, restriction of the regular gamma operator to the odd sector creates a second, sum-variable kernel.

## 5. Repair criterion

A valid bridge from the explicit localized operator (5) to the normalized collar form must now establish an identity on a common core that tracks all of the following at once:

1. the difference-channel Cauchy and gamma pieces;
2. the parity-image Carleman and gamma pieces, including `a\rho(a(x+y))`;
3. the scalar and endpoint multiplication terms;
4. the nonconstant Jacobian potential `W_A` generated by the exponential half-density transform in WI-363.

A repair need not preserve decomposition (4) term by term. It may use a different but unitarily equivalent realization, provided the equivalence is written explicitly and the image and multiplication terms can be seen to cancel or be reassigned exactly. What is insufficient is an off-diagonal kernel identity involving only the difference gamma term followed by an assertion that the full closed form has no further correction.

Accordingly the current source-level conclusion is

\[
\boxed{
\text{the normalized one-cell form used downstream is still not derived from the full odd archimedean block in v1.}
}
\tag{18}
\]

This leaves WI-362's conditional downstream common-cut / rooted-Schur audit intact: its algebra may remain valid once the normalized one-cell form is granted. The gap is upstream, in proving that the actual localized Weil operator is unitarily the advertised normalized form.

## 6. Stress tests and claim boundary

This finding does **not** assert that:

- the exact localized operator (5) is itself incorrect;
- the desired collar representation cannot be repaired;
- the gamma image term has a sign that by itself destroys positivity;
- the common-cut or rooted-Schur algebra audited in WI-362 is wrong;
- or the Riemann hypothesis is false.

It establishes the narrower exact statement that the canonical odd restriction of the paper's own even-difference gamma kernel has the two-channel form (3), while the load-bearing cancellation written in Section 5 does not account explicitly for the image channel. Any claimed exact unitary equivalence must explain it.

The most direct falsification/repair test is to write the paper's `\mathfrak c_A` explicitly as the quadratic form obtained from (4), apply the exponential half-density unitary to **every** term, and compare the resulting difference, image, and multiplication channels with the claimed collar form. If all extra terms cancel, that supplies the missing durable bridge. If either the image gamma term or WI-363's `W_A` survives, Proposition 5.3 and its downstream uses require correction.

## 7. Prior-art and novelty audit

A fresh targeted search on 20 September 2026 found the primary Desogus submission and generic listings/mirrors but no independent technical critique resolving this specific parity-image bookkeeping issue. Absence from that limited search is not evidence of priority or of absence from the literature.

The identity (3) is elementary parity reduction of an even-difference kernel and is not claimed as a new theorem. The durable contribution of this finding is the source-specific audit: applying that exact reduction to the particular gamma term in `arXiv:2609.20367v1` exposes a load-bearing term that the displayed Section 5 transport does not track.

WI-361 had already marked the normalized-form bridge as unresolved, WI-362 audited later steps conditional on that bridge, and WI-363 isolated the half-density Jacobian potential. WI-364 is not a duplicate of those findings: it reconstructs the complete canonical odd fold before the exponential transport and identifies the independent regular gamma image that any repair must also handle.

## Consequence for the research line

The Desogus audit remains the highest-value live route because it claims the line's strongest possible objective, full RH. The next pass should not continue downstream from the normalized collar form. It should instead perform the now sharply specified repair test: derive the explicit `\mathfrak c_A` from (4), transport both difference and image channels plus all multiplication terms through the paper's exponential coordinate change, and check whether the gamma image and `W_A` cancel exactly.

A successful cancellation would close the principal upstream provenance gap and let the audit resume at the remaining global/certificate gates. A surviving term would convert the present proof gap into an explicit corrected operator that must be propagated through the later positivity argument.