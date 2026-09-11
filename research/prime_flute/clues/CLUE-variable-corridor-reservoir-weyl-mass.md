---
id: CLUE-prime-flute-variable-corridor-reservoir-weyl-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/findings/PF-279-variable-scalar-schur-reservoirs-can-erase-local-corridor-cut-gain.md
  - research/prime_flute/findings/PF-281-energy-normalized-cross-form-removes-bounded-frequency-coupling-gate.md
  - research/prime_flute/findings/PF-282-energy-normalized-cross-form-is-a-saturated-extension-angle.md
  - research/prime_flute/findings/PF-283-heavy-angle-counting-criterion-for-weak-trace-endpoint.md
  - research/prime_flute/findings/PF-284-two-sided-heavy-angle-counting-sandwich.md
  - research/prime_flute/findings/PF-286-physical-extension-strengths-are-not-compact.md
  - research/prime_flute/findings/PF-287-heavy-extension-angle-is-exactly-a-product-of-heavy-range-projections.md
  - research/prime_flute/findings/PF-289-fixed-local-rayleigh-floors-suffice-for-a-heavy-angle-noncompactness-witness.md
  - research/prime_flute/findings/PF-290-optimized-local-low-high-correlation-is-an-exact-high-band-shorting-deficit.md
  - research/prime_flute/findings/PF-291-fixed-window-high-pass-annihilates-compact-response-profiles.md
  - research/prime_flute/findings/PF-292-fixed-physical-high-pass-forces-diverging-local-frequency-floor.md
  - research/prime_flute/findings/PF-293-critical-normalized-source-has-exactly-one-sobolev-derivative.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Does the physical heavy-sector extension angle close the weak-trace endpoint?

## Observation

PF-282 factors the mixed extension operator as

\[
T=F_P\Gamma_{PF}F_H,
\qquad
F_P=f(K_P^{1/2}),\quad F_H=f(K_H^{1/2}),
\qquad
f(t)=\frac{t}{\sqrt{1+t^2}},
\]

so the outer factors record extension strength while `\Gamma_{PF}` records the relative angle of the physical low-fed and high-fed ranges. PF-283 gives a sufficient weak-trace counting law, PF-284 gives the reverse threshold budget, and PF-286 shows that strength decay alone cannot close the canonical endpoint. PF-287 therefore reduces the surviving problem to essential orthogonality and quantitative counting of the heavy extension ranges.

PF-289 makes the cheapest negative test local: a persistent energy-normalized correlation between PF-216's low vector and a PF-227 physical-high direction with a fixed positive Rayleigh floor already forces noncompactness at some fixed heavy thresholds. PF-290 then removes witness choice from the test. The optimized squared correlation is exactly the high-band shorting deficit

\[
\delta_{n,r}
=1-
\inf_{h\in W_n^\sharp}
\frac{k[\ell_r+h]}{k[\ell_r]},
\]

so a positive limsup of `\delta_{n,r}` gives the local noncompactness witness.

PF-291 and PF-292 now sharply constrain how such a positive deficit can survive on a fixed physical window. The increasingly dense physical low-frequency grid annihilates every precompact normalized response family, and the admissible high-pass space has a Dirichlet frequency floor tending to infinity. In particular, if the actual Riesz representatives `G_{n,r}` of the normalized mixed functional are uniformly bounded in `L^2` and in **any** positive fractional Sobolev norm, then their high projections vanish and `\delta_{n,r}\to0`.

PF-293 separates this new regularity gate from the earlier Robin obstruction. PF-278's mass-one branch kills the PF-271 supercritical leakage route, but its normalized fixed-axis source column still has exactly one full `K_0` derivative. The controlled PF-255/PF-256 geometric transports preserve that positive regularity class. Therefore the fixed-axis mass-one branch by itself is not the frequency-escape mechanism demanded by PF-292. Any surviving local obstruction must come from parameter-dependent norm growth, genuinely mixed/global Schur reassembly, support migration, or another normalization effect.

## Research question

For the **actual simultaneous one-cusp-pant precision form**, what is the regularity of the normalized mixed-response Riesz family `G_{n,r}` on the PF-227 fixed window?

Does there exist one `\sigma>0` such that, after the same scalar energy normalization used in PF-290,

\[
\sup_{n,r}
\left(
\|G_{n,r}\|_{L^2(I)}
+
\|K_D^\sigma G_{n,r}\|_{L^2(I)}
\right)<\infty?
\]

If yes, PF-292 forces `\delta_{n,r}\to0`, closing this local fixed-window noncompactness witness and returning the line to PF-287's full heavy-range essential-orthogonality/counting problem. If no, identify the exact component responsible for the loss: a diverging local frequency, a growing normalized amplitude, escape toward the corridor ends/cusp completion, or a nonlocal Schur-reservoir contribution.

This question precedes the small-threshold counting law. A genuine positive-frequency escape that keeps `\limsup\delta_{n,r}>0` already disproves compactness; a regularity bound only removes this local falsifier and does not prove compactness.

## Why it may matter

PF-281 shows that `T\in\mathcal S_{1,\infty}` closes the mixed Schur/reciprocal-prime commutator gate. The route has now been narrowed from a broad spectral-counting problem to one concrete discriminator on the negative side: whether the **complete normalized mixed response** can keep nontrivial mass in a high-pass space whose local frequency floor diverges.

PF-293 is important because it prevents a false explanation of such an escape. The critical mass-one Robin branch is rough enough to defeat a supercritical leakage exponent, but still regular enough for PF-292's compactness mechanism. Thus a failure of every positive Sobolev bound would reveal genuinely new structure in the variable/reassembled response rather than merely repackage the already-understood fixed-axis branch singularity.

Either outcome changes the next step. Uniform positive regularity removes the cheapest local noncompactness route. A quantified failure identifies the exact high-frequency or nonlocal component that must be tested against the shorting deficit and, if persistent, against fixed heavy-threshold compactness.

## Decisive test

Derive the Riesz representative `G_{n,r}` directly from the simultaneous local precision form used by PF-290, retaining the actual PF-205 trim, fixed physical `P/H` projectors, neighboring-cell terms, and the Schur reservoirs isolated by PF-279. Do not replace the response by the scalar reciprocal-width profile already ruled out by PF-291.

Factor out pieces whose regularity is already known. In particular, use PF-293 for the fixed-axis normalized Robin source and PF-255/PF-256 for the controlled hypercycle/density/corridor transports rather than re-opening their regularity. The live estimate is the residual response after those factors and the scalar energy normalization are made explicit.

Then perform the following dichotomy:

1. prove a uniform bound `\sup_{n,r}(\|G_{n,r}\|_2+\|K_D^\sigma G_{n,r}\|_2)<\infty` for any fixed `\sigma>0`; PF-292 then gives `\delta_{n,r}\to0`;
2. or prove that such bounds fail and isolate a moving threshold `R_n\to\infty` carrying nonvanishing normalized response mass. Quantify that escaping component against the PF-290 shorting formula rather than treating high frequency alone as sufficient.

If the local deficit vanishes, return to PF-287's full heavy-range projection product. Only after fixed-threshold essential orthogonality survives should effort move to PF-283/PF-284 quantitative small-threshold counting.

## Evidence boundary

PF-282--PF-287 establish the strength-angle factorization and the heavy-range projection formulation. PF-289 supplies the fixed-threshold local noncompactness criterion, and PF-290 identifies its optimized local correlation with an exact shorting deficit. PF-291 proves annihilation of compact fixed-window response families; PF-292 upgrades that to a diverging local-frequency floor and shows that any uniform positive Sobolev bound kills the local high projection.

PF-293 proves only a **fixed-parameter** regularity theorem for the PF-278 normalized Robin source and explains that PF-255/PF-256 preserve already-controlled positive regularity. It does not prove canonical-tail uniformity and does not identify the complete `G_{n,r}` with a fixed-axis source column. PF-279 remains the warning that Schur reservoirs can change isolated local expectations.

No uniform Sobolev bound or frequency-escape theorem for `G_{n,r}` is established yet. Consequently no compactness, weak-trace, wave-operator, trace-formula, determinant, zeta-zero, critical-line, or RH conclusion follows from this clue.

## Research disposition

The clue remains `accepted`. The immediate discriminator is no longer another generic low/high correlation estimate: **extract the exact normalized response family `G_{n,r}` and decide whether it has any uniform positive Sobolev regularity on the fixed PF-227 window.** PF-291/PF-292 make that test decisive for the local shorting deficit, while PF-293 shows that the known fixed-axis mass-one branch is not by itself an obstruction to such regularity. A negative regularity result must identify the new rough component explicitly before it can support a noncompactness claim.