---
id: WP-286
title: Scale-Haar Følner averaging erases every summable oscillatory screen and is arithmetic-blind
branch: weil_positivity
status: supported
kind: source-symmetry-matched-control
claim_strength: exact Følner/Bohr theorem showing that even averaging justified intrinsically by multiplicative scale symmetry suppresses the favorable-RH zero field for generic spectral reasons
created: 2026-09-13
related: [WP-279, WP-281, WP-283, WP-284, WP-285]
prior_art:
  - classical Bohr almost-periodic mean theory
  - Følner averaging on locally compact abelian groups
  - Aihua Fan, A Weyl-type theorem for Diophantine approximations driven by LCA groups and applications, arXiv:2605.15580v2 (2026)
---

# WP-286 — Scale-Haar Følner averaging erases every summable oscillatory screen and is arithmetic-blind

## Claim

`WP-285` showed that ordinary trailing Cesàro windows, with no zero data and with arbitrarily slowly growing memory, erase the absolutely summable favorable-RH zero field left by the one-state regularizer of `WP-281`. One possible objection remained: the box window used there was not forced by Mathia, whereas logarithmic scale itself carries a canonical group structure. Perhaps averaging could become genuinely source-native if it were derived from multiplicative Haar measure and the amenability of the scale action rather than selected as an external smoother.

That refinement does not rescue the route. Let `F_j subset R` be any measurable Følner sequence of finite positive measure for translations, and define the normalized Haar averages

\[
(\mathcal A_j f)(E)
:=\frac1{|F_j|}\int_{F_j} f(E-t)\,dt.
\tag{1}
\]

For every absolutely summable discrete oscillatory field

\[
A(E)=\sum_{\lambda\in\Lambda}c_\lambda e^{i\lambda E},
\qquad 0\notin\Lambda,
\qquad \sum_{\lambda\in\Lambda}|c_\lambda|<\infty,
\tag{2}
\]

one has

\[
\boxed{
\|\mathcal A_jA\|_\infty\longrightarrow0.
}
\tag{3}
\]

The proof uses only the Følner property and character orthogonality; it does not use the arithmetic locations of `Lambda`.

Under the same favorable-RH control used in `WP-281`--`WP-285`, the regularized zeta zero field

\[
A_a(E)
=-\sum_{\rho=1/2+i\gamma}
\frac{a}{(i\gamma)(a+i\gamma)}e^{i\gamma E}
\tag{4}
\]

satisfies `sum_gamma |c_gamma|<infinity`. Hence **every** logarithmic-scale Haar Følner averaging scheme removes it asymptotically. If the averaging sets are bounded and the observation points `E_j` satisfy

\[
E_j-\sup F_j\to+\infty,
\tag{5}
\]

then for the regularized source decomposition

\[
Y_a(E)=C_\Gamma+A_a(E)+r_a(E),
\qquad r_a(E)\to0,
\tag{6}
\]

one obtains

\[
\boxed{
(\mathcal A_jY_a)(E_j)\longrightarrow C_\Gamma.
}
\tag{7}
\]

This closes a specific provenance loophole left by `WP-285`: **deriving the averaging from the multiplicative scale group's Haar/Følner structure is still not arithmetic selection and still not evidence for Weil positivity.** The same mechanism projects every summable almost-periodic spectrum onto its invariant mode.

**Classification:** `EXACT-DERIVED + FAVORABLE-RH-MATCHED-CONTROL + SCALE-HAAR-FØLNER + BOHR-CHARACTER-ORTHOGONALITY + ZERO-INDEPENDENT + ARBITRARY-FØLNER-SEQUENCE + ARITHMETIC-BLIND + SOURCE-SYMMETRY-INSUFFICIENT + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Character orthogonality follows directly from the Følner property

For a fixed nonzero frequency `lambda`, set

\[
H_j(\lambda)
:=\frac1{|F_j|}\int_{F_j}e^{-i\lambda t}\,dt.
\tag{8}
\]

Choose `h` with `e^{-i lambda h} != 1`. Translation gives

\[
e^{-i\lambda h}H_j(\lambda)
=\frac1{|F_j|}\int_{F_j+h}e^{-i\lambda t}\,dt.
\tag{9}
\]

Therefore

\[
|1-e^{-i\lambda h}|\,|H_j(\lambda)|
\le
\frac{|(F_j+h)\triangle F_j|}{|F_j|}.
\tag{10}
\]

The right-hand side tends to zero by the Følner condition, so

\[
H_j(\lambda)\to0
\qquad(\lambda\ne0).
\tag{11}
\]

This is the elementary character-level form of Bohr orthogonality along Følner sequences. Aihua Fan's 2026 LCA-group treatment records the general result, together with the corresponding Bohr mean formula for almost-periodic functions; no new harmonic-analysis theorem is claimed here.

Now apply (1) to (2):

\[
(\mathcal A_jA)(E)
=\sum_{\lambda\in\Lambda}
 c_\lambda H_j(\lambda)e^{i\lambda E}.
\tag{12}
\]

Because `|H_j(lambda)|<=1` and `sum |c_lambda|<infinity`, dominated convergence on the counting measure yields

\[
\sup_E|\mathcal A_jA(E)|
\le
\sum_{\lambda\in\Lambda}|c_\lambda|\,|H_j(\lambda)|
\longrightarrow0,
\tag{13}
\]

which proves (3). Unlike the box-specific estimate in `WP-285`, this argument gives no universal rate, but it needs no `1/|lambda|` weighted summability and no interval shape.

## 2. The favorable-RH zeta screen lies exactly in this generic class

In (4),

\[
|c_\gamma|
=\left|\frac{a}{(i\gamma)(a+i\gamma)}\right|
\le\frac{a}{\gamma^2}.
\tag{14}
\]

The Riemann--von Mangoldt zero-counting law implies

\[
\sum_\rho\frac1{|\gamma|^2}<\infty.
\tag{15}
\]

Hence (3) applies directly to the complete regularized zero field, uniformly in the observation point. Constants are fixed by every normalized average,

\[
\mathcal A_j C_\Gamma=C_\Gamma.
\tag{16}
\]

For the remainder in (6), bounded support of `F_j` and (5) give

\[
|\mathcal A_j r_a(E_j)|
\le
\sup_{t\in F_j}|r_a(E_j-t)|\to0.
\tag{17}
\]

Equations (13), (16), and (17) prove (7).

The result is deliberately conditional in exactly the same way as `WP-285`: RH is used first to turn every nontrivial-zero contribution into a pure logarithmic-scale character. If an off-critical zero produces a mode with positive real exponent, Følner character orthogonality does not turn that exponentially growing mode into a harmless oscillation. Nothing here proves RH.

## 3. Why multiplicative Haar provenance is still too weak

In the original positive scale variable `x=e^E`, translation `E -> E+t` is multiplication `x -> e^t x`, and Lebesgue measure `dE` is exactly multiplicative Haar measure `dx/x`. Thus (1) is not an arbitrary coordinate trick: it is the standard amenable averaging construction attached to the scale group itself.

But that source provenance is **structural rather than arithmetic**. Equation (10) knows only that nontrivial characters of an amenable abelian group have zero invariant mean. It is unchanged if the zeta ordinates are replaced by any other nonzero frequency set with summable coefficients. It is also unchanged for any other problem whose regularized residual is a summable Bohr almost-periodic field on logarithmic scale.

Therefore a proposal of the form

\[
\text{``the source has canonical scale symmetry''}
\Longrightarrow
\text{``use its Haar/Følner mean''}
\Longrightarrow
\text{``the zero screen disappears''}
\tag{18}
\]

still fails the matched-control test. The operation can be intrinsic to the **ambient scale action** while remaining completely insensitive to the finite-prime arithmetic whose global sign is at issue.

This distinction sharpens the current research requirement. “Source-forced” cannot merely mean forced by a symmetry shared with generic logarithmic dynamics. A viable construction must use additional source structure that is specific enough to determine the finite-prime/archimedean coupling before the explicit-formula zero decomposition, and its sign must follow from that geometry independently.

## 4. Aggressive falsification and boundary of the no-go

This finding does not rule out all growing-memory or nonlocal source operations. It rules out the entire class whose justification is only normalized Haar averaging along a Følner family of the multiplicative scale group after the source has been regularized into (6).

It also does not say that every Følner sequence is geometrically equally natural. Different sequences may have very different boundary regularity, memory growth, and quantitative attenuation. The point is stronger in the direction relevant to the mandate: **none of those distinctions restores arithmetic specificity at the level of invariant-mode extraction.** Every Følner sequence kills every nonzero character.

The theorem does not supply a positive Weil quadratic form. Positivity here means only that normalized Haar averaging is a positive unital contraction on scalar functions. It neither creates the finite Mangoldt autocorrelation with the Weil orientation nor produces the archimedean and polar counterterms inside one independently nonnegative geometric form.

Finally, the theorem does not touch a genuinely coupled operation performed before scalarization, a nonlinear source construction whose positivity has its own geometric theorem, a cohomological/intersection pairing, or an operator boundary response that mixes finite and archimedean data before any Bohr decomposition. Those remain the relevant categories.

## 5. Prior-art and novelty audit

The harmonic-analysis content is classical. Bohr almost-periodic functions carry a translation-invariant mean, and Følner averaging is the standard amenable-group realization of invariant means. Aihua Fan, *A Weyl-type theorem for Diophantine approximations driven by LCA groups and applications*, arXiv:`2605.15580v2` (26 June 2026), explicitly proves Bohr orthogonality of characters along arbitrary Følner sequences on locally compact abelian groups and a Bohr mean formula for almost-periodic functions.

Accordingly, equations (10)--(13) are not claimed as a new theorem. The Mathia-specific contribution is the **provenance audit** against the exact frontier left by `WP-285`: replacing an externally chosen Cesàro box by a Haar/Følner average canonically attached to multiplicative scale symmetry does not make the successful zero suppression arithmetic. It is still the universal invariant-mean projection of amenable harmonic analysis.

This is not classical Weil positivity, Hilbert--Pólya, Connes/trace, Sonin localization, Frobenius/cohomology, or an intersection-form mechanism. It is a negative control showing that one more apparently intrinsic route remains below the line's required geometric specificity.

## Consequence for `weil_positivity`

`WP-285` eliminated zero coding as a necessary ingredient for favorable-RH Gamma-center extraction by growing positive memory. `WP-286` removes the next easy repair: **ambient multiplicative scale symmetry cannot by itself promote that extraction into a source-specific mechanism.**

A future candidate must therefore derive more than its averaging measure from the source. It must force a non-generic coupling, quotient, boundary condition, incidence relation, or cohomological structure that distinguishes the arithmetic carrier from matched almost-periodic controls and that yields the relevant sign before RH or zero locations are used. Long-time scale averaging, even when justified canonically by Haar/Følner geometry, is now a matched control rather than evidence for the primary mandate.
