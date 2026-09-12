---
id: WP-270
title: Pole completion of the critical Mangoldt spectrum is tempered if and only if RH
branch: weil_positivity
status: supported
kind: prior-art-redirect
claim_strength: exact normalization match with an RH-equivalent temperedness theorem
created: 2026-09-12
refined: 2026-09-12
related: [WP-007, WP-009, WP-132, WP-256, WP-268, WP-269]
prior_art:
  - J. Arias de Reyna, Explicit formula and quasicrystal definition, arXiv:2402.10604
  - Delsarte explicit formula
  - von Koch and Schoenfeld prime-number-theorem error bounds under RH
  - Schwartz tempered-distribution theory
---

# WP-270 — Pole completion of the critical Mangoldt spectrum is tempered if and only if RH

## Claim

`WP-269` leaves two logically possible escapes from the failure of the critical source spectrum to define a positive-definite distribution or Fourier hyperfunction. One is to remain in a larger exponential-growth category. The other is to introduce a **source-forced global cancellation before ordinary positivity is read**, so that the resulting spectral object has smaller growth.

The first canonical cancellation is already present in the zeta explicit formula: the pole terms contribute exactly the exponential density needed to match the leading growth of the critical Mangoldt carrier. However, this does not provide a new Mathia bridge. It lands exactly on a known RH-equivalent temperedness theorem.

Recall the `WP-269` normalization

\[
\nu_{1/2}
:=\frac12\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr).
\tag{1}
\]

Define the pole-completed signed measure

\[
\boxed{
T_{\rm pole}
:=\nu_{1/2}-\cosh(x/2)\,dx.
}
\tag{2}
\]

Then

\[
\boxed{
T_{\rm pole}\in\mathcal S'(\mathbb R)
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\tag{3}
\]

This is not a new RH criterion. Arias de Reyna proves directly that

\[
\mu_{\rm AR}
:=-\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr)
+2\cosh(x/2)\,dx
\tag{4}
\]

is a tempered distribution if and only if RH. Since

\[
\mu_{\rm AR}=-2T_{\rm pole},
\tag{5}
\]

his theorem is **exactly** the `WP-269` critical carrier with the canonical zeta-pole counterterm, in the same logarithmic variable and with only a harmless overall scalar/sign change.

Therefore the obvious completion of the `WP-269` category obstruction by the classical pole term does cancel the leading exponential growth, but membership of the completed object in the ordinary tempered-distribution category is already target-strength: it is equivalent to RH itself. It cannot be used as an unconditional technical preprocessing step before applying ordinary distributional positivity.

**Classification:** `DIRECT-PRIOR-ART-IDENTIFICATION + EXACT-NORMALIZATION-MATCH + RH-EQUIVALENT-CATEGORY-DESCENT + DECISIVE-REDIRECT + NOT-A-NEW-RH-CRITERION`.

## 1. The pole has exactly the missing exponential type

The obstruction in `WP-269` is not merely that the atomic critical measure has infinite total mass. Its positive half has exponential density in the arithmetic-energy variable `x=log n`:

\[
\nu_{1/2}^{+}
=\frac12\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}.
\tag{6}
\]

Let

\[
A(X):=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}.
\tag{7}
\]

The pole main term corresponding to the positive logarithmic half-line is `e^{x/2}dx`; indeed

\[
\int_0^x e^{u/2}\,du
=2e^{x/2}-2.
\tag{8}
\]

Under RH, the classical weighted prime-number theorem gives

\[
A(X)=2\sqrt X+O(\log^3 X),
\tag{9}
\]

so

\[
\nu_{1/2}^{+}([0,x])
=e^{x/2}+O(x^3).
\tag{10}
\]

On the same half-line,

\[
\int_0^x\cosh(u/2)\,du
=2\sinh(x/2)
=e^{x/2}-e^{-x/2}.
\tag{11}
\]

Thus the canonical polar density has precisely the exponential type needed to cancel the leading growth of the critical Mangoldt mass. This is qualitatively different from the polynomial or finite-rank corrections excluded in `WP-269`.

The point is also forced by the explicit formula rather than fitted to (1): the two zeta-pole evaluations produce the `e^{x/2}+e^{-x/2}=2 cosh(x/2)` term in the additive logarithmic formulation. After the factor `1/2` used in (1), the matching background is exactly `cosh(x/2)dx`.

## 2. Why the remaining growth is exactly RH-sensitive

The one-sided mechanism can be written directly in terms of Chebyshev's function

\[
\psi(X):=\sum_{n\le X}\Lambda(n).
\tag{12}
\]

On `x>=0`, the unsigned critical atomic measure is

\[
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}
=e^{-x/2}\,d\psi(e^x),
\tag{13}
\]

while the growing polar part is

\[
e^{x/2}dx=e^{-x/2}\,d(e^x).
\tag{14}
\]

Hence their difference is

\[
e^{-x/2}\,d\bigl(\psi(e^x)-e^x\bigr).
\tag{15}
\]

If RH holds, Schoenfeld's explicit form of the von-Koch estimate gives

\[
\psi(X)-X=O(\sqrt X\log^2X).
\tag{16}
\]

After the critical half-density normalization this becomes only polynomial growth in logarithmic energy:

\[
e^{-x/2}\bigl(\psi(e^x)-e^x\bigr)=O(x^2).
\tag{17}
\]

Taking one distributional derivative and adding the harmless multiplication by `1/2` therefore leaves a tempered distribution. This is the elementary growth mechanism behind the forward implication in (3).

The converse is equally sharp. On the positive half-line, before analytic continuation and for `Re s>1/2`, the Laplace transform of the unscaled prime-minus-pole residual is

\[
\begin{aligned}
\mathcal L(s)
&=\sum_{n\ge2}\frac{\Lambda(n)}{n^{s+1/2}}
-\int_0^\infty e^{-sx}e^{x/2}\,dx\\
&=-\frac{\zeta'}{\zeta}(s+1/2)-\frac1{s-1/2}.
\end{aligned}
\tag{18}
\]

The second term cancels the pole of `-zeta'/zeta` coming from the pole of `zeta` at `1`; it does not cancel poles coming from nontrivial zeros. If the residual were tempered and supported in a half-line, its Fourier--Laplace transform would be holomorphic throughout `Re s>0`. Any zero `rho` of `zeta` with `Re rho>1/2` would instead create a pole at

\[
s=\rho-1/2,
\tag{19}
\]

inside that half-plane. Thus temperedness forces zero-freeness to the right of the critical line. The functional equation then forces every nontrivial zero onto `Re rho=1/2`.

This is the analytic reason the category descent in (3) is not a soft regularization statement: a hypothetical off-line zero manifests exactly as residual exponential growth after the critical pole background is removed.

## 3. Direct prior art is exact, not merely analogous

Arias de Reyna's *Explicit formula and quasicrystal definition*, arXiv:2402.10604 (2024; current arXiv version in 2026), states as its main theorem that the measure (4) is tempered if and only if RH. Under RH it further gives the Fourier identity

\[
\mathcal F\!\left(
\sum_\gamma\delta_{\gamma/(2\pi)}
-2\vartheta'(2\pi t)\,dt
\right)
=
\mu_{\rm AR},
\tag{20}
\]

where `gamma` runs over the ordinates of nontrivial zeros and `vartheta` is the Riemann--Siegel phase.

The match to the Mathia object is exact:

- the atoms are at the same source arithmetic frequencies `+-log n`;
- the masses are the same critical Mangoldt half-density `Lambda(n)/sqrt(n)`;
- the counterterm is the same pole density `2 cosh(x/2)`;
- equation (5) identifies the normalization with `WP-269` without any fitted kernel, regularization, or change of variable.

Consequently no historical or mathematical novelty can be claimed for the statement that the pole-completed critical Mangoldt carrier is tempered exactly on RH. The useful new information for this branch is the **redirect**: the most obvious source-forced cancellation left open by `WP-269` has already been classified in precisely the needed category.

## 4. The archimedean term does not make this an unconditional escape

Equation (20) is also important for interpreting the Gamma sector correctly. The archimedean contribution appears through the Riemann--Siegel phase density `vartheta'`. Its large-`|t|` behavior is logarithmic, hence it is tempered. Likewise the zero-counting density under RH is of polynomial growth.

Therefore the hard category change in (3) is not repaired by appending an independently tempered Gamma correction. If `T` is not tempered and `G` is tempered, then `T+G` cannot be tempered, because otherwise `T=(T+G)-G` would be tempered. The nontrivial cancellation of exponential type is supplied by the pole background, not by a hidden high-growth archimedean term.

This does **not** mean the Gamma factor is unimportant for Weil positivity. It means only that, for the specific question of descending the `WP-269` critical carrier into `S'`, the Gamma contribution cannot turn a false RH instance into a tempered one after the pole subtraction has been fixed canonically.

## 5. Aggressive falsification of the apparent escape

Several possible overreadings fail.

First, (2) is always a perfectly valid **local distribution** on compactly supported tests: both the atomic carrier and the smooth pole density are locally finite. The RH equivalence concerns extension to the Schwartz space as a **tempered** distribution. Ordinary local distributional hostability therefore does not supply the global Fourier category needed by Bochner--Schwartz.

Second, the pole term is not hand-picked from the desired asymptotic. It is forced independently by the poles at `0` and `1` in the completed explicit formula. This is why the cancellation is worth testing. The negative conclusion comes only afterwards: the amount of cancellation needed to reach polynomial growth is exactly RH-sensitive.

Third, a proof from genuinely new geometry that (2) is tempered would not be logically circular; it would prove RH. What is ruled out is treating pole subtraction plus temperedness as an innocuous **preliminary regularization** and then claiming the subsequent positivity theorem as the substantive step. The preliminary category descent already has target strength.

Fourth, temperedness still does not give the desired sign. `T_pole` is a signed distribution, not a positive spectral measure. Even assuming RH and obtaining (20), one has not recovered an independent source-side Bochner positivity theorem. The zero-side measure in (20) is itself an RH realization and cannot be imported as independent geometric evidence.

Fifth, the ultra-hyperfunction escape of `WP-269` is not contradicted. The original positive carrier has fixed exponential growth and can live in larger generalized-function categories. What fails is the idea that the **classical pole counterterm alone** gives an unconditional descent back to ordinary tempered distributions.

## 6. What remains genuinely open

The source-forced-cancellation branch from `WP-269` is now substantially narrower.

A successful construction cannot merely take the critical Mangoldt carrier, subtract the standard zeta-pole density, assert that the result is tempered, and then invoke ordinary Fourier/distributional machinery. That exact operation is (3), already known to be equivalent to RH.

There are still logically distinct possibilities. A Mathia-native geometry could prove the RH-equivalent descent by an independent theorem; a stronger global quotient could change the carrier before it becomes the classical pole-renormalized distribution; or the construction could remain in an exponential-growth category and derive a sign theorem there without requiring `S'` hostability. But each of these must supply genuinely new structure. The canonical pole cancellation by itself is not the missing geometric positivity mechanism.

## Consequence

`WP-269` should therefore be sharpened as follows. The statement that its critical positive spectrum is too large for ordinary positive-definite distributions is not repaired unconditionally by adding the most obvious global counterterm. The zeta pole contributes exactly the required exponential background, but the resulting signed object

\[
\nu_{1/2}-\cosh(x/2)dx
\]

is tempered **if and only if RH**. This is direct prior art, not a new criterion.

The next viable step must therefore explain more than growth cancellation. It must derive a global finite--archimedean structure whose sign is independent, or operate in the larger exponential-growth category with an independently forced Weil orientation. Treating ordinary temperedness after classical pole subtraction as already available would simply move RH into the domain/category assumption.