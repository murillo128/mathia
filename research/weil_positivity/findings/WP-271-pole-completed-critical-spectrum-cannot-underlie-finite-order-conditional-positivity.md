---
id: WP-271
title: Pole-completed critical spectrum cannot underlie finite-order conditional positivity
branch: weil_positivity
status: supported
kind: conditional-positivity-obstruction
claim_strength: exact local-sign no-go after canonical pole completion
created: 2026-09-12
refined: 2026-09-12
related: [WP-007, WP-009, WP-132, WP-146, WP-269, WP-270]
prior_art:
  - I. M. Gelfand and N. Ya. Vilenkin, Generalized Functions, Vol. 4: Applications of Harmonic Analysis
  - J. Chung, S.-Y. Chung, and D. Kim, Bochner Schwartz Type Theorem for Conditionally Positive Definite Fourier Hyperfunctions, Positivity 7 (2003), 323-334
  - J. Chung and D. Kim, Conditionally Positive Definite Hyperfunctions, Publ. RIMS 41 (2005), 385-396
---

# WP-271 — Pole-completed critical spectrum cannot underlie finite-order conditional positivity

## Claim

`WP-270` shows that the canonical pole-completed critical spectrum

\[
T_{\rm pole}
=\nu_{1/2}-\cosh(\xi/2)\,d\xi,
\qquad
\nu_{1/2}
=\frac12\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr),
\tag{1}
\]

is tempered if and only if RH. That still leaves an apparently weaker sign route: perhaps the negative pole background can be quotiented out by requiring positivity only on a finite-codimensional moment-zero test space, as in the classical theory of conditionally positive-definite kernels and generalized functions.

That escape fails exactly. For every finite order \(s\ge0\), there is **no conditionally positive-definite distribution of order \(s\)** whose Fourier-side distribution is \(T_{\rm pole}\). The same conclusion holds in the classical Fourier-hyperfunction category.

The reason is local and independent of RH. The Gelfand--Vilenkin representation theorem says that the Fourier-side data of a conditionally positive-definite distribution of finite order consists of a **positive measure away from frequency zero**, plus only a finite jet/polynomial ambiguity supported at zero. Chung--Chung--Kim prove the analogous statement for conditionally positive-definite Fourier hyperfunctions, with an infra-exponential positive measure.

But the Riemann pole completion has an open nonzero-frequency interval on which it is strictly negative. For example, because \(\log 2>1/2\),

\[
I=(1/4,1/2)
\tag{2}
\]

contains no Mangoldt atom, and hence

\[
\boxed{
T_{\rm pole}|_I=-\cosh(\xi/2)\,d\xi<0.
}
\tag{3}
\]

No finite-order conditional quotient can change that sign: its allowed ambiguity lives only at \(\xi=0\). Thus even if RH supplies the tempered category descent of `WP-270`, finite-order Schoenberg/Gelfand--Vilenkin conditional positivity still cannot supply the missing Weil sign.

**Classification:** `EXACT-DERIVED + CLASSICAL-REPRESENTATION-THEOREM + LOCAL-SIGN-OBSTRUCTION + FINITE-CODIMENSIONAL-QUOTIENT-NO-GO + FOURIER-HYPERFUNCTION-CONTROL + RH-INDEPENDENT-SIGN-SEPARATION + NOT-A-NEW-CPD-THEOREM`.

## 1. Conditional positivity is the canonical finite-moment escape

For a distribution \(U\) on \(\mathbb R\), Gelfand--Vilenkin call \(U\) conditionally positive definite of order \(s\) when

\[
\langle U,(P\varphi)*(P\varphi)^*\rangle\ge0
\tag{4}
\]

for every test function \(\varphi\) and every homogeneous constant-coefficient differential operator \(P\) of order \(s\). In one dimension there is only the derivative direction up to a scalar, so this is the distributional version of positivity after annihilating a finite polynomial sector.

The representation theorem is the decisive structural fact. Every such distribution is automatically tempered and can be written as a Fourier transform whose nonzero-frequency part is a positive measure \(\mu\) on \(\mathbb R\setminus\{0\}\), while the remaining terms depend only on finitely many derivatives of the Fourier transform of the test function at zero. Equivalently, the spectral distribution has the form

\[
\widehat U
=\mu+J_0,
\qquad
\mu\ge0\text{ on }\mathbb R\setminus\{0\},
\tag{5}
\]

where \(J_0\) denotes the finite zero-frequency jet allowed by the order-\(s\) subtraction scheme. The exact integrability conditions near zero depend on \(s\), but positivity of \(\mu\) away from zero does not.

This is precisely the classical mechanism one would want if the pole term in (1) were merely a finite-dimensional gauge defect: moment constraints could remove polynomial directions without demanding ordinary positive definiteness on the full test space.

## 2. The pole background is negative on an ordinary open spectral set

The support of the positive arithmetic measure \(\nu_{1/2}\) is

\[
\{\pm\log n:n\ge2,\ \Lambda(n)>0\}.
\tag{6}
\]

Its smallest positive point is \(\log2\). Therefore every open interval

\[
I\Subset(0,\log2)
\tag{7}
\]

is atom-free. On such an interval the entire arithmetic part of (1) vanishes and the pole-completed spectrum is simply

\[
T_{\rm pole}|_I=-\cosh(\xi/2)\,d\xi.
\tag{8}
\]

Consequently, for every nonzero \(g\in C_c^\infty(I)\),

\[
\langle T_{\rm pole},|g|^2\rangle
=-\int_I\cosh(\xi/2)|g(\xi)|^2\,d\xi<0.
\tag{9}
\]

This is not a failure at the singular origin, a divergent tail, or a choice of regularization. It is strict negativity on a compact interval separated from every location where finite-order conditional positivity permits an exceptional jet.

## 3. Gelfand--Vilenkin gives the contradiction immediately

Assume that a conditionally positive-definite distribution \(U\) of some finite order \(s\) had

\[
\widehat U=T_{\rm pole}.
\tag{10}
\]

By the representation theorem, restricting (5) to the interval \(I\) removes the zero-frequency jet and gives

\[
T_{\rm pole}|_I
=\widehat U|_I
=\mu|_I,
\qquad \mu|_I\ge0.
\tag{11}
\]

Equation (8) says instead that the same restriction is a strictly negative smooth measure. This contradiction proves

\[
\boxed{
\nexists\,s<\infty\text{ and conditionally positive-definite }U
\text{ of order }s\text{ with }\widehat U=T_{\rm pole}.
}
\tag{12}
\]

The case \(s=0\) includes ordinary positive definiteness. Increasing \(s\) does not help: it enlarges only the finite jet permitted at the origin and changes the near-origin moment condition on \(\mu\); it never permits negative spectral mass on an open set away from zero.

There is also a direct derivative interpretation. Conditional positivity of order \(s\) makes the appropriate \(2s\)-th constant-coefficient derivative of \(U\) positive definite. Fourier transformation multiplies the nonzero-frequency spectrum by \(|\xi|^{2s}\), so on \(I\) the corresponding spectral density remains

\[
-|\xi|^{2s}\cosh(\xi/2),
\tag{13}
\]

which has the wrong sign for Bochner--Schwartz positivity. The representation-theorem argument above avoids any dependence on Fourier-sign conventions.

## 4. RH repairs growth but not this sign

`WP-270` and (12) separate two logically different obstructions.

If RH is false, \(T_{\rm pole}\) is not tempered, so it cannot be the Fourier-side distribution of a classical conditionally positive-definite distribution in the first place: Gelfand--Vilenkin conditional positivity automatically implies temperedness.

If RH is true, the category obstruction disappears exactly as `WP-270` states, but (8)--(12) remain unchanged. The pole-completed object is then a perfectly valid tempered signed distribution whose nonzero-frequency restriction still contains the negative absolutely continuous background between the Mangoldt atoms. Thus

\[
\boxed{
\text{RH can supply temperedness of }T_{\rm pole},
\text{ but not finite-order conditional positivity.}
}
\tag{14}
\]

This is useful for the research mandate because it rules out treating a finite collection of moment constraints as the missing geometric sign theorem after category descent has been achieved.

## 5. Fourier hyperfunctions do not enlarge this particular escape

The Fourier-hyperfunction analogue has the same decisive structure. Chung--Chung--Kim prove that a conditionally positive-definite Fourier hyperfunction of finite order has the Gelfand--Vilenkin representation with a **positive** spectral measure away from zero, now satisfying the appropriate infra-exponential growth condition, together with the same finite-order zero-frequency ambiguity.

Therefore any Fourier-hyperfunction realization whose spectral data agree with \(T_{\rm pole}\) would again have to be nonnegative on \(I\), contradicting (8). Passing from tempered distributions to Fourier hyperfunctions does not turn the negative pole density into an admissible finite-order conditional gauge term.

This conclusion should not be overextended to Fourier **ultra-hyperfunctions**. `WP-269` notes that ordinary positive-definite ultra-hyperfunction theory can host positive measures of fixed exponential growth, which is large enough for the uncompleted positive Mangoldt spectrum. The bounded literature audit here found no basis for asserting an analogous finite-order conditional-positive representation theorem in that larger category. What is closed is the classical finite-order distribution/Fourier-hyperfunction quotient route.

## 6. Aggressive falsification and matched controls

A global sign flip does not rescue the construction. The distribution \(-T_{\rm pole}\) is positive on the atom-free interval \(I\), but at every prime-power frequency it contains a **negative atom**

\[
-\frac12\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n},
\tag{15}
\]

which likewise cannot occur in the positive nonzero-frequency measure \(\mu\). Hence neither orientation of the canonical pole completion is finite-order conditionally positive.

Adding any polynomial in the time variable, or equivalently any finite jet supported at spectral frequency zero, is also powerless: it leaves both (8) and the nonzero prime-power atoms unchanged. This is exactly the freedom already built into the conditional-positive representation theorem.

Nor is the obstruction an artifact of the particular gap \((1/4,1/2)\). Every nonempty open subinterval of \((0,\log2)\) supplies the same strict negative witness. More generally, between consecutive positive Mangoldt frequencies the continuous pole density remains negative; the first gap is merely the cleanest certificate.

Finally, this result is different from `WP-146`. That finding exhibits conditional indefiniteness of a finite Prime-Circle resultant matrix on a mixed-prime three-chain. Here the object is the **global pole-completed critical spectral distribution of `WP-270`**, and the obstruction is the classical theorem that finite-order conditional positivity can hide only zero-frequency polynomial data, not a negative continuous density on a nonzero-frequency interval.

## 7. Prior-art and novelty audit

The conditional-positive representation theorem is classical, not a Mathia discovery. Gelfand and Vilenkin proved the distributional Bochner--Schwartz generalization; Chung, Chung, and Kim extended it to conditionally positive-definite Fourier hyperfunctions; Chung and Kim give an audit-friendly formulation in their 2005 hyperfunction paper, including the fact that every conditionally positive-definite distribution is tempered and the positive-measure representation away from the origin.

The Mathia-specific content is the exact application of that theorem to the canonical Riemann spectrum already isolated in `WP-270`. Once the pole-completed carrier is written in the source normalization (1), the empty interval below \(\log2\) gives a one-line local certificate that no finite polynomial/moment quotient can turn the signed completion into a positive generalized covariance.

No novelty is claimed for conditional positive definiteness, the Gelfand--Vilenkin theorem, Fourier-hyperfunction extensions, or the idea of quotienting polynomials. The durable research value is the route closure: the finite-codimensional conditional-positivity escape left implicit after `WP-270` is unavailable even on RH.

## Consequence

The live boundary after `WP-269`--`WP-271` is narrower. The positive uncompleted Mangoldt spectrum can be hosted only in a sufficiently large exponential-growth generalized-function category; the canonical pole subtraction descends to tempered distributions exactly on RH; and **after that descent, no finite-order moment/polynomial quotient supplies positivity**, because the pole background has the wrong sign on ordinary nonzero-frequency open sets.

A surviving Mathia-native route must therefore change something more structural before the final sign is read: modify or quotient the carrier by a genuinely nonlocal/infinite-dimensional source construction, derive a different finite--archimedean coupling whose spectral completion is not (1), or establish an independent positivity theorem directly in an exponential-growth category. Merely replacing ordinary positivity by classical finite-order conditional positivity does not evade the obstruction.