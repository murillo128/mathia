---
id: CLUE-prime-flute-variable-corridor-reservoir-weyl-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-228-flat-corridor-dressing-makes-inverse-seam-multiplicity-weak-trace-compatible.md
  - research/prime_flute/findings/PF-229-frozen-serial-schur-completion-preserves-flat-corridor-cut-scale.md
  - research/prime_flute/findings/PF-279-variable-scalar-schur-reservoirs-can-erase-local-corridor-cut-gain.md
  - research/prime_flute/findings/PF-280-one-sided-frequency-decoupled-schur-transfer-is-reservoir-stable.md
  - research/prime_flute/findings/PF-281-energy-normalized-cross-form-removes-bounded-frequency-coupling-gate.md
  - research/prime_flute/findings/PF-282-energy-normalized-cross-form-is-a-saturated-extension-angle.md
  - research/prime_flute/findings/PF-283-heavy-angle-counting-criterion-for-weak-trace-endpoint.md
  - research/prime_flute/findings/PF-284-two-sided-heavy-angle-counting-sandwich.md
  - research/prime_flute/findings/PF-285-complementary-weak-schatten-extension-strengths-close-the-weak-trace-endpoint-without-angle-decay.md
  - research/prime_flute/findings/PF-286-physical-extension-strengths-are-not-compact.md
  - research/prime_flute/findings/PF-287-heavy-extension-angle-is-exactly-a-product-of-heavy-range-projections.md
  - research/prime_flute/findings/PF-288-diverging-local-form-witnesses-force-heavy-angle-noncompactness.md
  - research/prime_flute/findings/PF-289-fixed-local-rayleigh-floors-suffice-for-a-heavy-angle-noncompactness-witness.md
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Does the physical heavy-sector extension angle close the weak-trace endpoint?

## Observation

PF-279 shows that a variable scalar reservoir can erase a favorable isolated cut scale, while PF-280/PF-281 separate that raw obstruction from the physically mixed low/high block. PF-282 gives the exact factorization

\[
T=F_P\Gamma_{PF}F_H,
\qquad
F_P=f(K_P^{1/2}),\quad F_H=f(K_H^{1/2}),
\qquad
f(t)=\frac{t}{\sqrt{1+t^2}},
\]

where the outer factors record extension strength and `\Gamma_{PF}` records the relative angle of the physical low-fed and high-fed extension ranges.

PF-283 gives the sufficient endpoint criterion

\[
\sup_{0<\tau<\tau_0}
\tau\,N_{Q_P^\tau\Gamma_{PF}Q_H^\tau}(2\tau)<\infty,
\]

while PF-284 shows that weak trace class itself only forces the weaker symmetric envelope `N(2\tau)=O(\tau^{-3})`. PF-285 identifies a strength-only sufficient mechanism, but PF-286 closes it for the canonical physical split: both outer strength factors have infinite heavy populations, so any endpoint closure must come from the relative extension geometry rather than global decay of `F_P,F_H`.

PF-287 identifies the thresholded angle exactly with the product of the corresponding heavy unit-energy extension-range projections. Thus fixed-threshold compactness is an essential-orthogonality problem, and the weak-trace endpoint is its quantitative thresholded refinement. The same angle is computed directly from the physical precision form by diagonal-energy normalization.

PF-288 localizes a strong negative test: separated local physical-low/high vectors with diverging diagonal Rayleigh quotients and persistent normalized mixed correlation force noncompactness at every fixed heavy threshold. PF-216 already supplies the low diverging family.

PF-289 removes the remaining **high-divergence construction** from the cheapest compactness falsifier. To disprove compactness of `T`, one only needs one positive pair of heavy thresholds, not every prescribed threshold. Uniform positive local Rayleigh floors are enough when those thresholds are chosen sufficiently small. PF-227 already supplies such a physical-high local floor: its fixed high/high crossing gives unit high vectors with a nonzero cross-form coefficient, and positivity forces at least one endpoint of each pair to have diagonal high energy bounded below by a fixed constant.

Therefore the current cheapest negative test has only one genuinely new geometric quantity: the energy-normalized mixed correlation between the PF-216 low-symmetric module vector and a suitable PF-227 local physical-high witness. A persistent correlation kills compactness; vanishing of all such optimized local correlations would remove this local obstruction and send the line back to PF-287's positive essential-orthogonality/counting problem.

## Research question

For the actual simultaneous one-cusp-pant extension, what is the singular-value distribution of

\[
\Pi_P^\alpha\Pi_H^\beta,
\]

or equivalently

\[
Q_P^\alpha\Gamma_{PF}Q_H^\beta,
\]

on the physical heavy-strength sectors?

The strongest simple positive target remains PF-283's symmetric law

\[
N_{\Pi_P^\tau\Pi_H^\tau}(2\tau)=O(\tau^{-1}),
\]

which is sufficient for `T\in\mathcal S_{1,\infty}`. Failure of that law is not endpoint failure; PF-284 permits weaker asymmetric threshold budgets.

Before attempting such quantitative counting, test fixed-threshold compactness with PF-289. Let `\ell_m` be PF-216's unit physical-low symmetric vector. From a PF-227 high/high singular pair on a nearby module choose the unit endpoint `h_m` having the larger diagonal high energy, so that

\[
k[h_m]\ge b>0
\]

uniformly on a sparse tail. Is it true or false that one can choose such witnesses with

\[
\frac{|k[\ell_m,h_m]|}
{\sqrt{k[\ell_m]k[h_m]}}
\not\to0?
\]

A positive limsup is already enough to make `T` noncompact by PF-289. No proof that `k[h_m]\to\infty` is needed.

## Why it may matter

PF-281 proves that `T\in\mathcal S_{1,\infty}` closes the mixed Schur/reciprocal-prime commutator gate. PF-286 removes the misleading population-only route, PF-287 converts the survivor into a direct two-subspace geometry problem, and PF-288/PF-289 make the falsification side local.

PF-289 is operationally important because it eliminates an artificial intermediate theorem. PF-227 has already done enough high-side work for a compactness falsifier: it provides local physical-high directions with a fixed diagonal energy floor. The project can now spend its effort directly on the physical **low/high correlation**, which is the information that the angle actually measures.

If that normalized correlation persists, the endpoint route fails before any small-threshold counting asymptotic is needed. If it vanishes for every PF-227 local witness family, the result is also informative: the raw high/high multiplicity is not leaking into the physical low extension range through this local mechanism, and the next task becomes a genuine positive essential-orthogonality theorem or a more global negative witness.

## Decisive test

Take a sparse sequence of pant/module windows separated beyond the PF-214 block-Jacobi interaction range. On each relevant module use the PF-216 low vector `\ell_m`, for which

\[
\|\ell_m\|=1,
\qquad
k[\ell_m]\gtrsim\frac{P_m}{\log P_m}\to\infty.
\]

For the high side, use PF-227 rather than constructing a new divergent-Rayleigh family. Choose a unit source/target high singular pair `x_n,y_n` with

\[
|k_H[y_n,x_n]|\ge b.
\]

Cauchy--Schwarz for the positive form implies

\[
\max\{k_H[x_n],k_H[y_n]\}\ge b.
\]

Let `h_m` be whichever endpoint attains this floor and pair it with the PF-216 low vector on the same local module. Compute or bound

\[
\eta_m
=
\frac{|k[\ell_m,h_m]|}
{\sqrt{k[\ell_m]k[h_m]}}.
\]

It is useful to optimize `\eta_m` over the finite-dimensional PF-227 high witness band rather than over arbitrary high vectors.

If `\limsup\eta_m>0`, pass to a sparse subsequence with `\eta_m\ge c>0`; PF-289 then gives fixed positive heavy thresholds at which the angle is noncompact, so `T` is noncompact and the weak-trace endpoint fails.

If every such optimized local correlation tends to zero, record that as a substantive negative for the local obstruction. It would not prove compactness: return to PF-287's sequence criterion for the full heavy ranges, and only if fixed-threshold essential orthogonality survives should effort move to the PF-283/PF-284 small-threshold counting law.

PF-231's exactly separable untrimmed corridor remains a useful calibration because its leading Fourier sectors may make the local low/high correlation vanish. The actual test must retain the PF-205 hypercycle trim, the fixed physical `P/H` projectors, neighboring-cell inhomogeneity, and simultaneous precision form; do not infer the answer from the separable corridor alone.

## Evidence boundary

PF-282 establishes the strength-angle factorization. PF-283 establishes one sufficient heavy-angle counting law, PF-284 the reverse comparison/necessary budget, and PF-285 an abstract strength-only sufficient route. PF-286 proves that this strength-only route does not apply to the canonical physical factors. PF-287 identifies each thresholded angle with a heavy-range projection product and gives the direct energy-normalized form formula.

PF-288 establishes the stronger every-threshold local noncompactness criterion under divergent low and high Rayleigh quotients. PF-289 establishes that **uniform positive** local Rayleigh floors already suffice for noncompactness at some fixed positive thresholds, and that PF-227 supplies the high-side floor needed for this weaker but decisive compactness falsifier.

What remains unproved is the mixed correlation itself. PF-227 is a high/high statement and does not force overlap with the PF-216 low direction. Therefore PF-289 does not decide compactness or weak trace class; it only removes the need for a separate divergent physical-high construction before testing the angle.

No physical principal-angle counting law, wave-operator theorem, trace formula, relative determinant, prime/clone separation, zeta-zero correspondence, critical-line statement, or RH consequence is established.

## Research disposition

The clue remains `accepted`. The strength-population route is closed by PF-286, PF-287 identifies the surviving object as the heavy extension-range angle, and PF-288/PF-289 reduce the cheapest negative test to a local form calculation. **Do not spend another cycle trying to prove a divergent physical-high Rayleigh law merely to use PF-288.** PF-227 already supplies a fixed positive high Rayleigh floor, which PF-289 shows is sufficient after choosing a small fixed heavy threshold. The immediate task is to compute or bound the normalized PF-216/PF-227 physical low/high correlation. If it persists, the endpoint is noncompact; if it vanishes for all such local witnesses, move to fixed-threshold essential orthogonality and only then to quantitative small-threshold counts.