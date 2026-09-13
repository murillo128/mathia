---
id: WP-278
title: The critical Mangoldt half-density has the zeta-pole continuum as its high-energy tangent measure
branch: weil_positivity
status: supported
kind: source-side-pole-provenance
claim_strength: exact PNT-derived vague-limit identification of the pole continuum from the canonical critical Mangoldt carrier
created: 2026-09-13
related: [WP-259, WP-269, WP-270, WP-273, WP-275, WP-277]
prior_art:
  - prime number theorem and Stieltjes-measure scaling of d psi
  - Bernard L. Julia, Thermodynamic limit in number theory: Riemann-Beurling gases, Physica A 203 (1994), 425-436, DOI 10.1016/0378-4371(94)90008-6
  - J. Arias de Reyna, Explicit formula and quasicrystal definition, arXiv:2402.10604
---

# WP-278 — The critical Mangoldt half-density has the zeta-pole continuum as its high-energy tangent measure

## Claim

`WP-277` leaves an infinite-volume/direct-limit escape from the compact-resolvent obstruction. For the exact critical finite-place carrier already isolated by Mathia, that escape has a canonical measure-level realization.

For `0 <= sigma < 1`, define

\[
\nu_\sigma
:=\frac12\sum_{n\ge2}\frac{\Lambda(n)}{n^\sigma}
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr).
\tag{1}
\]

Center the two high-energy edges at the origin and divide by their local mass growth:

\[
\eta_{E,\sigma}
:=\frac12 e^{-(1-\sigma)E}
\sum_{n\ge2}\frac{\Lambda(n)}{n^\sigma}
\bigl(\delta_{\log n-E}+\delta_{E-\log n}\bigr).
\tag{2}
\]

Then the prime number theorem implies

\[
\boxed{
\eta_{E,\sigma}
\xrightarrow[E\to\infty]{\mathrm{vague}}
\cosh\bigl((1-\sigma)x\bigr)\,dx.
}
\tag{3}
\]

At the already-source-selected Weil half-density `sigma=1/2`,

\[
\boxed{
\eta_{E,1/2}
\xrightarrow[E\to\infty]{\mathrm{vague}}
\cosh(x/2)\,dx,
}
\tag{4}
\]

exactly the polar continuum in the canonical carrier of `WP-270` and `WP-273`,

\[
T_{\rm pole}=\nu_{1/2}-\cosh(x/2)\,dx.
\tag{5}
\]

Thus the finite Mangoldt half-density and the polar continuum are not unrelated ingredients. Within the source carrier, the polar density is its canonical high-energy tangent density. This is a positive structural bridge, not a Weil-positivity theorem: it supplies provenance for the pole term but no sign theorem, no Gamma/digamma term, and no fixed-Hilbert-space positive compression.

**Classification:** `EXACT-DERIVED + PNT-ONLY + SOURCE-NATIVE-MANGOLDT-HALF-DENSITY + HIGH-ENERGY-TANGENT-MEASURE + INFINITE-VOLUME-CATEGORY-CHANGE + EXACT-POLE-DENSITY + CRITICAL-EXPONENT-ALIGNMENT + PRIOR-ART-CLASSICALIZED-INGREDIENTS + MATCHED-CONTROLS + GAMMA-MISSING + SIGN-MISSING + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Exact tangent theorem

Let

\[
\psi(X)=\sum_{n\le X}\Lambda(n).
\tag{6}
\]

The prime number theorem says `psi(X)~X`. Hence on every compact interval of `(0,infinity)`,

\[
e^{-E}\,d\psi(e^E u)
\xrightarrow[E\to\infty]{\mathrm{vague}}du.
\tag{7}
\]

Indeed, for fixed `0<a<b`,

\[
e^{-E}\bigl(\psi(e^E b)-\psi(e^E a)\bigr)\to b-a,
\tag{8}
\]

and monotonicity gives convergence against compactly supported continuous tests.

For `phi in C_c(R)`, the positive edge of (2) is

\[
I^+_{E,\sigma}(\phi)
=\frac12 e^{-(1-\sigma)E}
\int_0^\infty t^{-\sigma}\phi(\log t-E)\,d\psi(t).
\tag{9}
\]

Substituting `t=e^E u`, applying (7), and then putting `u=e^x` gives

\[
I^+_{E,\sigma}(\phi)
\longrightarrow
\frac12\int_{\mathbb R}\phi(x)e^{(1-\sigma)x}\,dx.
\tag{10}
\]

The reflected edge gives

\[
I^-_{E,\sigma}(\phi)
\longrightarrow
\frac12\int_{\mathbb R}\phi(x)e^{-(1-\sigma)x}\,dx.
\tag{11}
\]

Adding (10) and (11) proves (3). No zero locations, RH assumption, explicit-formula cancellation, analytic continuation to the critical strip, or interpolation kernel enters this derivation. The number-theoretic input is only the ordinary prime number theorem.

## 2. Why the `sigma=1/2` match is structural

The general family (3) prevents the `cosh(x/2)` match from being a free normalization. For the source weight `Lambda(n)n^{-sigma}`, the tangent exponent is forced to be `1-sigma`. Therefore the exact completed-zeta pole density `cosh(x/2)dx` occurs precisely at

\[
1-\sigma=\frac12,
\qquad \sigma=\frac12.
\tag{12}
\]

But `sigma=1/2` was already selected on the finite side. `WP-259`, building on `WP-256`, gives on the permutation-fixed prime-Fock sector

\[
T_{\rm sym}e_n^{\rm sym}
=\frac{\Lambda(n)}{\sqrt n}e_n^{\rm sym}.
\tag{13}
\]

Thus two readings of the same source agree:

\[
\boxed{
\text{critical finite amplitude }n^{-1/2}
\Longrightarrow
\text{high-energy tangent }\cosh(x/2)dx.
}
\tag{14}
\]

The mass normalization in (2) is likewise forced at leading order. On every fixed nonempty logarithmic interval, the weighted mass grows like `e^{(1-sigma)E}`. A stronger exponential normalization makes the tangent vanish; a weaker one makes its local mass diverge.

## 3. Relation to the `WP-277` continuum obstruction

`WP-277` proves that the fixed logarithmic Hamiltonian

\[
H_{\rm ar}e_n=(\log n)e_n
\tag{15}
\]

has compact resolvent and cannot acquire an absolutely continuous channel by bounded or relative-bound-`<1` mixing with another compact-resolvent sector. It explicitly leaves thermodynamic/direct limits open.

Equation (4) realizes that escape only at **measure level**. Every finite-`E` measure is atomic; after moving to the high-energy edge and rescaling its growing mass, the local limit is absolutely continuous. The continuum is not created by perturbing `H_ar` on one fixed Hilbert space, so there is no conflict with `WP-277`.

The distinction also prevents overclaiming. Vague convergence does not supply a canonical strong-resolvent limit on one Hilbert space, an isometry from the prime-power carrier to `L^2(cosh(x/2)dx)`, the graph-positive sampling contraction required by `WP-273`, or exact covariance of the type ruled out by `WP-275`. It establishes the continuum's source provenance, not the required positive operator architecture.

## 4. Aggressive falsification and matched controls

The derivation uses only first-order prime density. Any Beurling/generalized-prime system with `psi_B(X)~X` has the same tangent law. Therefore (3) cannot distinguish the Riemann zeta function from matched generalized-prime controls, encode zero locations, or force RH.

The full integer spectrum gives an even sharper control. Remove `Lambda` and define

\[
\widetilde\eta_E
=\frac12e^{-E/2}\sum_{n\ge1}n^{-1/2}
\bigl(\delta_{\log n-E}+\delta_{E-\log n}\bigr).
\tag{16}
\]

An elementary Riemann-sum argument gives

\[
\widetilde\eta_E\xrightarrow{\rm vague}\cosh(x/2)\,dx.
\tag{17}
\]

So the pole continuum is a weighted Weyl-density feature of the critical logarithmic source. The Mangoldt selector changes the discrete fluctuations and support, while the PNT restores the same leading density.

Most importantly, (4) does **not** justify the global subtraction in (5). `WP-270` remains unchanged: temperedness of that global centered measure is equivalent to RH. A local tangent can be identified unconditionally while the global fluctuations around it remain target-strength.

Nor does (4) produce the archimedean Gamma contribution. The zeta pole and Gamma factor are distinct pieces of the completed explicit formula. The tangent theorem explains only the polar background, and the difference between a positive atomic measure and its positive mean density is still locally indefinite as in `WP-273`.

## 5. Prior art and novelty boundary

The analytic ingredients are classical. The prime number theorem gives (7). Bernard Julia's 1994 Riemann--Beurling gas work already treats the logarithmic arithmetic spectrum thermodynamically and uses a continuous high-energy level-density approximation. Arias de Reyna's 2024 quasicrystal formulation contains exactly the symmetric critical Mangoldt comb together with `2 cosh(x/2)dx`; `WP-270` records its RH-equivalent temperedness theorem.

A targeted literature search located those two ingredients separately but did not locate the specific formulation (4) as the vague high-energy tangent of the critical Mangoldt half-density. No new PNT or explicit-formula theorem is claimed. The Mathia-specific contribution is the compatibility statement that the same source-derived half-density which carries the finite Mangoldt coefficients also fixes the exact polar continuum through its thermodynamic tangent law.

## Consequence for `weil_positivity`

One part of the finite/global matching problem is now intrinsic to a single Mathia carrier:

\[
\boxed{
\text{critical prime-power atoms}
\xrightarrow{\text{high-energy tangent}}
\text{exact polar continuum}.
}
\tag{18}
\]

The next legitimate burden is not to rediscover the pole term, but to determine whether this measure-level tangent correspondence lifts canonically to a global boundary/operator/cohomological construction that retains prime-power fluctuations, supplies the missing Gamma term, and has an independent sign theorem on the full Weil test class. Without such a lift, (4) remains an exact source-provenance result rather than a positivity mechanism.
