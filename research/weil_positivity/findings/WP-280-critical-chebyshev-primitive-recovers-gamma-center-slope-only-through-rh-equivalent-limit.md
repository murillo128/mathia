---
id: WP-280
title: Critical Chebyshev primitive recovers the Gamma-center slope only through an RH-equivalent limit
branch: weil_positivity
status: supported
kind: primitive-archimedean-prior-art-obstruction
claim_strength: exact central-Gamma identity plus literature-exact RH equivalence for the normalized critical primitive
created: 2026-09-13
related: [WP-007, WP-278, WP-279]
prior_art:
  - Masatoshi Suzuki, Aspects of the screw function corresponding to the Riemann zeta-function, Journal of the London Mathematical Society 108 (2023), DOI 10.1112/jlms.12785
  - Masatoshi Suzuki, On variants of Chebyshev's conjecture, The Ramanujan Journal 68, Article 95 (2025), DOI 10.1007/s11139-025-01238-9
---

# WP-280 — Critical Chebyshev primitive recovers the Gamma-center slope only through an RH-equivalent limit

## Claim

`WP-279` proves that after the pole tangent is removed from the critical Mangoldt half-density, scalar high-energy rescaling cannot expose the Gamma/trivial-zero layer before the nontrivial-zero modes. It explicitly leaves one structurally different escape: **retain the Chebyshev primitive that differentiation had discarded**, instead of working only with the positive atomic measure.

That escape does recover a genuine archimedean scalar, but only at an RH-equivalent boundary. Let

\[
\psi_{1/2}(x)
:=\sum_{n\le x}^{\prime}\frac{\Lambda(n)}{\sqrt n}.
\tag{1}
\]

The classical explicit formula gives

\[
\psi_{1/2}(x)-2\sqrt x
=
-\sum_\rho\frac{x^{\rho-1/2}}{\rho-1/2}
-\frac{\zeta'}{\zeta}\!\left(\frac12\right)
+o(1).
\tag{2}
\]

At the center of the completed zeta functional equation,

\[
\boxed{
-\frac{\zeta'}{\zeta}\!\left(\frac12\right)
=
\frac12\left(\psi\!\left(\frac14\right)-\log\pi\right),
}
\tag{3}
\]

where `psi=Gamma'/Gamma`. Thus the scalar that reappears when one keeps the primitive is exactly the central logarithmic slope of the Riemann Gamma factor; it is not an unrelated arithmetic constant.

However, the zero sum in (2) is still unsuppressed. Introduce the canonical logarithmic primitive

\[
F(x)
:=
\int_0^x
\bigl(\psi_{1/2}(y)-2\sqrt y\bigr)\,\frac{dy}{y}
=
\sum_{n\le x}\frac{\Lambda(n)}{\sqrt n}\log\frac{x}{n}
-4\sqrt x.
\tag{4}
\]

Under RH,

\[
F(x)
=
-\frac{\zeta'}{\zeta}\!\left(\frac12\right)\log x
-
\sum_\rho
\frac{x^{\rho-1/2}}{(\rho-1/2)^2}
+o(1),
\tag{5}
\]

and the zero sum is bounded because `Re rho=1/2` and
`sum_rho |rho|^{-2}<infinity`. Hence

\[
\boxed{
\frac{F(x)}{\log x}
\longrightarrow
-\frac{\zeta'}{\zeta}\!\left(\frac12\right)
=
\frac12\left(\psi\!\left(\frac14\right)-\log\pi\right).
}
\tag{6}
\]

This looks at first like the desired source-to-archimedean bridge: the same critical Mangoldt half-density whose local tangent gives the pole continuum in `WP-278` now yields the Gamma-center slope after one global logarithmic primitive and one normalization.

But Suzuki's 2025 Theorem 1 proves the converse as well: **the limit (6) is equivalent to RH**. The same theorem proves that eventual nonpositivity of `F(x)` is equivalent to RH. Suzuki then identifies the corresponding quantity with the nonarchimedean component of the zeta screw function and proves that eventual sign of that component is again RH-equivalent.

Therefore the primitive-retention route left by `WP-279` does not provide an independent Mathia-native geometric source of the archimedean term. It reaches the correct Gamma scalar exactly at a classical RH-equivalent asymptotic boundary.

**Classification:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE-FOR-PRIMITIVE-GAMMA-ESCAPE + RH-EQUIVALENT-ASYMPTOTIC + PRIOR-ART-REDIRECT + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The central constant is exactly Gamma data

Write the completed Riemann xi-function as

\[
\xi(s)
=
\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{7}
\]

Its functional equation `xi(s)=xi(1-s)` implies

\[
\frac{\xi'}{\xi}\!\left(\frac12\right)=0.
\tag{8}
\]

Taking the logarithmic derivative of (7),

\[
\frac{\xi'}{\xi}(s)
=
\frac1s+
\frac1{s-1}
-rac12\log\pi
+rac12\psi(s/2)
+rac{\zeta'}{\zeta}(s).
\tag{9}
\]

At `s=1/2`, the two polar-polynomial terms cancel:

\[
\frac1{1/2}+
\frac1{-1/2}=0.
\tag{10}
\]

Equations (8)-(10) therefore give (3) exactly. This matters for the `WP-279` escape. Differentiating the ordinary Chebyshev explicit formula to obtain the positive Mangoldt atomic measure removes the additive completed-zeta normalization. Retaining the weighted Chebyshev primitive restores it, and at the critical center the functional equation identifies it purely with the Gamma-factor logarithmic slope.

So there is a real bridge here:

\[
\text{critical Mangoldt primitive}
\quad\leadsto\quad
-\zeta'/\zeta(1/2)
\quad=\quad
\tfrac12(\psi(1/4)-\log\pi).
\tag{11}
\]

The question is not whether the Gamma scalar can appear. It can. The decisive question is whether its extraction follows from an independent positive geometry rather than already encoding RH.

## 2. One logarithmic primitive separates the center only under the RH-scale bound

The denominator in the zero term changes from first to second order when (2) is integrated against `dy/y`. Under RH,

\[
\left|x^{\rho-1/2}\right|=1,
\tag{12}
\]

so the absolutely summable square denominator yields

\[
\left|
\sum_\rho
\frac{x^{\rho-1/2}}{(\rho-1/2)^2}
\right|
\le
\sum_\rho\frac1{|\rho-1/2|^2}
<\infty.
\tag{13}
\]

Dividing by `log x` then kills the entire nontrivial-zero contribution while retaining the linear central term, producing (6).

This does **not** contradict `WP-279`. That finding rules out a scalar renormalization of the *local translated tangent residual*. The map in (4) is nonlocal in the scale variable: it integrates the primitive over all earlier logarithmic scales before the final normalization. It is exactly the kind of primitive/global-information escape that `WP-279` intentionally left open.

The new obstruction is sharper. The operation is mathematically canonical enough to succeed conditionally, but the condition needed for it to separate the Gamma-center slope is not supplied by local source geometry. Suzuki proves that the resulting limit itself characterizes RH.

## 3. Suzuki's theorem makes the apparent bridge circular

Suzuki's corrected 2025 article studies precisely (1). Its Theorem 1 states that the following are equivalent:

1. RH;
2. eventual nonpositivity of the logarithmic primitive `F(x)` in (4);
3. the normalized limit (6).

The production correction published in December 2025 concerns formulas in other parts of the article and does not alter Theorem 1 or the formulas used here.

This closes two tempting variants at once.

First, one cannot claim that the Gamma-center constant has been obtained independently merely because the finite-prime primitive converges to it after normalization. **That convergence is already an RH criterion.**

Second, one cannot replace convergence by a supposedly more geometric sign theorem for the same primitive. Eventual sign is also RH-equivalent. A proof that the nonarchimedean primitive eventually has the required sign would therefore already contain RH-level content.

Suzuki further decomposes the zeta screw function as

\[
g_\zeta(t)=g_0(t)+g_\infty(t),
\tag{14}
\]

with

\[
g_0(t)
=
\sum_{n\le e^{|t|}}
\frac{\Lambda(n)}{\sqrt n}
\bigl(|t|-\log n\bigr)
-4(e^{t/2}+e^{-t/2}-2),
\tag{15}
\]

and `g_infty` the Gamma/Hurwitz--Lerch term. Since

\[
g_0(\log x)
=
F(x)-4x^{-1/2}+8,
\tag{16}
\]

(6) is equivalently the asymptotic slope

\[
\frac{g_0(t)}{t}
\longrightarrow
-\frac{\zeta'}{\zeta}\!\left(\frac12\right).
\tag{17}
\]

Meanwhile the linear part of `g_infty` has the opposite slope,

\[
\frac{g_\infty(t)}{t}
\longrightarrow
+\frac{\zeta'}{\zeta}\!\left(\frac12\right),
\tag{18}
\]

by (3). Thus the finite and archimedean linear slopes cancel in the completed screw function. This is a useful exact structural identification, but it is the classical completed-zeta balance, not an independently positive Mathia mechanism.

## 4. Matched controls

### 4.1 Differentiation control

Differentiate (4) with respect to `E=log x`. The accumulated central slope becomes a constant contribution; differentiating once more back toward the atomic Mangoldt measure removes that constant. This recovers the information-loss mechanism isolated in `WP-279`: the positive source measure retains the pole tangent but has forgotten the central archimedean normalization carried by its primitive.

The primitive is therefore not an arbitrary counterterm inserted after the fact. It is precisely the minimal operation that restores the information differentiation discarded. What fails is not naturalness of the operation, but independence of the resulting RH-level limit.

### 4.2 Off-critical exponent control

For a weighted source `Lambda(n)n^{-sigma}` with `sigma>1/2`, nontrivial-zero modes decay under RH after the corresponding pole normalization. Moving off the center can therefore remove the resonance that makes the critical zero sector persist.

But the identity (3) is special to `s=1/2`: it uses `xi'/xi(1/2)=0` and the exact cancellation of the two derivatives from `s(s-1)`. At a shifted exponent, `-zeta'/zeta(sigma)` is not determined by the Riemann Gamma factor alone. Moving away from criticality can improve decay only by giving up the exact Gamma-center scalar that the Weil problem requires.

### 4.3 Generalized-prime control

The Prime-Lattice exponent geometry and the local Mangoldt half-density construction have generalized-prime analogues. But a generic Beurling prime system does not carry the Riemann functional equation or its fixed real-place factor `pi^{-s/2}Gamma(s/2)`. There is then no source-intrinsic reason for the analogue of the finite primitive's constant term to equal `1/2(psi(1/4)-log pi)`.

This separates the two ingredients cleanly. The arithmetic half-density is available from exponent/prime-power structure; equation (3) is forced only after importing the specific global Riemann completion. The Gamma-center slope is therefore not generated by the local positive source geometry alone.

### 4.4 Screw-function prior-art control

`WP-007` already showed that the canonical twofold Green primitive of the `WP-004` Prime-Lattice axis measure is exactly the finite term of Suzuki's 2023 zeta screw function, and that positivity of the completed increment kernel is RH-equivalent. The present result does not claim a new screw-function representation.

The additional point is narrower and directly answers the escape left by `WP-279`: even if one asks only for the **asymptotic central Gamma slope** of the retained critical primitive, rather than positivity of the whole completed screw kernel, Suzuki's 2025 theorem shows that the required normalized limit and eventual sign are themselves RH-equivalent. The weaker readout does not evade the circularity boundary identified in `WP-007`.

## 5. Aggressive falsification and remaining escape routes

A potential falsification would be an unconditional theorem deriving (6) from a source-native positive geometry without implying RH. Suzuki's equivalence rules this out for the exact primitive and normalization (4)-(6): any proof of that limit is already a proof of RH.

Another possible objection is that only the constant in (2) is needed, not the limiting theorem. But before averaging, the zero sum is of the same critical size and changes sign; there is no source-only scalar asymptotic that separates the constant. The logarithmic primitive is exactly what supplies a bounded zero remainder under RH, and the converse theorem shows that this separation cannot be promoted to an unconditional source property.

What remains genuinely open must change category before asserting positivity. Examples include a coupled finite/archimedean geometry in which the cancellation (17)-(18) is a theorem of one global object, a cohomological/intersection construction whose sign is established independently, or a non-scalar operation forced by geometry rather than by zero data. Merely retaining more Chebyshev primitives, normalizing their growth, or reading an eventual sign from `g_0` does not supply such an escape.

## 6. Prior-art and novelty audit

No novelty is claimed for the weighted Chebyshev explicit formula, the value `-zeta'/zeta(1/2)`, its relation to the completed functional equation, the screw-function decomposition, or the RH equivalences in Suzuki's work.

The primary prior-art result is Masatoshi Suzuki, *On variants of Chebyshev's conjecture*, The Ramanujan Journal 68 (2025), Article 95, DOI `10.1007/s11139-025-01238-9`. The article defines `psi_{1/2}`, records (2) and (5), proves Theorem 1 giving the exact equivalence between RH, eventual sign, and the normalized limit (6), and identifies the same primitive with the nonarchimedean part of the zeta screw function. A publisher correction, DOI `10.1007/s11139-025-01289-y`, does not modify these statements.

Suzuki's 2023 JLMS paper remains the broader screw-function prior-art anchor already recorded in `WP-007`.

The Mathia-specific contribution here is the **frontier identification**: `WP-279` had isolated primitive retention as a legitimate escape from its scalar tangent no-go because differentiation destroys the completed-zeta central constant. Equations (3)-(6) show exactly what that escape recovers, and Suzuki's theorem closes it as an independent-positivity route. This is a prior-art redirect and a narrowing of the search, not a new RH criterion.

## Consequence for the research line

The source-tangent picture is now sharper:

\[
\text{critical Mangoldt atoms}
\xrightarrow[\text{WP-278}]{\text{local high-energy tangent}}
\text{pole continuum},
\tag{19}
\]

while the next scalar local layer is screened by nontrivial-zero modes (`WP-279`). Retaining the primitive does restore the missing central Gamma slope, but only through

\[
\text{critical Chebyshev primitive}
\xrightarrow{\int dy/y}
F(x)
\xrightarrow{/\log x}
\frac12\bigl(\psi(1/4)-\log\pi\bigr),
\tag{20}
\]

and the existence of this exact limit is equivalent to RH.

Accordingly, the useful frontier is no longer “can a source-only primitive recover an archimedean scalar?” It can, classically. The surviving question is whether a **single intrinsic global geometry** can force the finite/archimedean cancellation and a Weil-type nonnegative form by an independent theorem, before any RH-equivalent sign or asymptotic criterion is assumed.