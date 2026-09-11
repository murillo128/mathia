---
id: CLUE-prime-flute-variable-corridor-reservoir-weyl-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-279-variable-scalar-schur-reservoirs-can-erase-local-corridor-cut-gain.md
  - research/prime_flute/findings/PF-282-energy-normalized-cross-form-is-a-saturated-extension-angle.md
  - research/prime_flute/findings/PF-287-heavy-extension-angle-is-exactly-a-product-of-heavy-range-projections.md
  - research/prime_flute/findings/PF-289-fixed-local-rayleigh-floors-suffice-for-a-heavy-angle-noncompactness-witness.md
  - research/prime_flute/findings/PF-290-optimized-local-low-high-correlation-is-an-exact-high-band-shorting-deficit.md
  - research/prime_flute/findings/PF-291-fixed-window-high-pass-annihilates-compact-response-profiles.md
  - research/prime_flute/findings/PF-292-fixed-physical-high-pass-forces-diverging-local-frequency-floor.md
  - research/prime_flute/findings/PF-293-critical-normalized-source-has-exactly-one-sobolev-derivative.md
  - research/prime_flute/findings/PF-294-fixed-axis-robin-source-is-uniformly-half-sobolev-for-bounded-seam-ratio.md
  - research/prime_flute/findings/PF-295-canonical-seam-ratios-close-the-fixed-axis-parameter-escape.md
  - research/prime_flute/findings/PF-296-weighted-source-row-moment-controls-canonical-fixed-axis-superpositions.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Does the physical heavy-sector extension angle close the weak-trace endpoint?

## Observation

PF-282 factors the mixed extension operator into extension-strength factors and a relative range angle. PF-287 turns the heavy part of that angle into a product of heavy-range projections. PF-289 gives a cheap fixed-threshold noncompactness witness, and PF-290 identifies its optimized local correlation exactly with a high-band shorting deficit `\delta_{n,r}`.

PF-291--PF-292 then impose a strong local falsifier. On a fixed physical window the densifying low-frequency grid annihilates compact response families, while the admissible high space develops a local frequency floor tending to infinity. Hence if the actual normalized mixed Riesz representatives `G_{n,r}` are uniformly bounded in `L^2` and in **any** positive fractional Sobolev norm, their local high projections vanish and `\delta_{n,r}\to0`.

PF-293 shows that the mass-one fixed-axis branch is not intrinsically rough: each fixed-parameter normalized source has one full derivative. PF-294 strengthens this to a uniform physical-axis `H^{1/2}` estimate for every fixed source row whenever `w/s` stays bounded. PF-295 closes that parameter caveat for the canonical flute. The PF-205 seam widths and PF-230 trimmed-corridor geometry force the actual canonical ratios `w_n/s_n` and `w_{n+1}/s_n` to remain uniformly bounded, and the PF-234/PF-235/PF-258 dictionary identifies these with PF-294's parameter. Therefore canonical seam shrinkage cannot itself generate the frequency escape required by PF-292.

PF-296 now makes the remaining **source-row proliferation** loophole quantitative. The proof of PF-294 gives the row-explicit bound `\|y^{(i)}\|_{H^{1/2}}\lesssim q_i`, with `q_i\asymp\kappa_i`. Hence the canonical fixed-axis synthesis map is uniformly bounded from the weighted source space `\ell^1(q)` into physical `H^{1/2}`. A growing collection of source rows therefore cannot sustain the PF-292 frequency escape while its weighted first source moment `\sum_i q_i|a_{n,i}|` remains bounded. Under the fixed-axis-plus-controlled-transport factorization, a persistent PF-290 deficit now requires that weighted moment to diverge, or else roughness must enter through a genuinely residual operator.

The first still-uncontrolled places where roughness can arise are therefore sharper: genuinely mixed/global Schur reassembly of the type warned about by PF-279, neighboring-cell coupling, a **quantitatively diverging** source-row first moment, support migration/end completion, or another normalization not represented by the canonical fixed-axis factor.

## Research question

For the **actual simultaneous one-cusp-pant precision form**, what is the regularity of the complete normalized mixed-response Riesz family `G_{n,r}` on the PF-227 fixed window after the canonical fixed-axis Robin source and the already-controlled PF-255/PF-256 transports have been factored out?

Does there exist one `\sigma>0` such that, after the same scalar energy normalization used in PF-290,

\[
\sup_{n,r}
\left(
\|G_{n,r}\|_{L^2(I)}
+
\|K_D^\sigma G_{n,r}\|_{L^2(I)}
\right)<\infty?
\]

If yes, PF-292 forces `\delta_{n,r}\to0`, closing this local fixed-window noncompactness witness and returning the line to PF-287's global heavy-range essential-orthogonality/counting problem. If no, identify the **first residual operator or source-population moment** that destroys the positive Sobolev margin and quantify its frequency or amplitude escape.

## Why it may matter

The local route is now sharply separated into controlled and uncontrolled pieces. The canonical source scale itself has a uniform positive Sobolev margin; the known hypercycle/density/corridor transports preserve regularity already present; and PF-296 shows that even arbitrary canonical fixed-axis source superpositions remain uniformly regular when their `q`-weighted absolute source mass is bounded. A failure of every positive Sobolev estimate for `G_{n,r}` would therefore expose genuinely new simultaneous/reassembled structure or a concrete divergence of the source-population moment rather than merely amplify the already-understood fixed-axis branch.

Either outcome is useful. Uniform positive regularity removes the cheapest local noncompactness route. A quantified failure identifies the exact high-frequency, amplitude, source-population, or nonlocal component that must be tested against PF-290 and then against fixed heavy-threshold compactness.

## Decisive test

Derive `G_{n,r}` directly from the simultaneous local precision form used by PF-290, retaining the actual PF-205 trim, physical `P/H` projectors, neighboring-cell terms, and the Schur reservoirs isolated by PF-279. Do not replace the response by the scalar reciprocal-width profile already ruled out by PF-291.

Factor out the pieces whose regularity is now settled: PF-295 for the canonical fixed-axis normalized Robin source, PF-296 for its weighted source-row synthesis, and PF-255/PF-256 for the controlled hypercycle/density/corridor transports. Before blaming row proliferation, extract the source coefficient vector `a_n` in this factorization and estimate

\[
\sum_i q_i|a_{n,i}|.
\]

If that quantity is uniformly bounded, PF-296 removes source-row population as the origin of local frequency escape and the next object to inspect is the residual mixed/reassembly operator. If it diverges, determine whether the divergence actually produces nonvanishing mass above PF-292's moving threshold; the moment divergence alone is only loss of a sufficient regularity estimate.

The decisive dichotomy for the complete response remains:

1. prove `\sup_{n,r}(\|G_{n,r}\|_2+\|K_D^\sigma G_{n,r}\|_2)<\infty` for any fixed `\sigma>0`; PF-292 then gives `\delta_{n,r}\to0`;
2. or prove that such bounds fail and isolate either a diverging weighted source moment, a moving threshold `R_n\to\infty` carrying nonvanishing normalized response mass, or a genuine normalized-amplitude blow-up. Quantify that component in the exact PF-290 shorting formula rather than treating high frequency or source count alone as sufficient.

Do **not** attribute failure to an unbounded canonical `w/s` ratio: PF-295 closes that escape. Do **not** attribute it merely to an increasing number of source rows: PF-296 shows that the relevant sufficient currency is the `q_i\asymp\kappa_i` weighted absolute moment. If a different effective ratio, source norm, or mixing operator appears after Schur reduction, derive it explicitly and show where it enters the complete response.

If the local deficit vanishes, return to PF-287's full heavy-range projection product. Only after fixed-threshold essential orthogonality survives should effort move to PF-283/PF-284 quantitative small-threshold counting.

## Evidence boundary

PF-289--PF-292 establish the local noncompactness criterion, exact shorting formulation, fixed-window annihilation, and diverging local-frequency floor. PF-293--PF-295 establish the **canonical fixed-axis source** regularity: for every fixed source row, canonical seam/corridor scaling stays in PF-294's bounded-ratio regime and therefore supplies a uniform positive Sobolev margin. PF-296 strengthens only the source-synthesis side: a canonical fixed-axis superposition with uniformly bounded `\ell^1(q)` source moment also has a uniform positive Sobolev margin. PF-255/PF-256 preserve such regularity through their already-controlled geometric transports.

None of these findings identifies the complete `G_{n,r}` with a controlled fixed-axis synthesis, proves that the actual source coefficient moment is bounded, controls PF-279-type Schur reservoirs, controls all neighboring-cell coupling, or prevents support migration/end completion. No uniform Sobolev bound or frequency-escape theorem for the complete mixed response is established yet.

Consequently no compactness, weak-trace, wave-operator, trace-formula, determinant, zeta-zero, critical-line, or RH conclusion follows from this clue.

## Research disposition

The clue remains `accepted`. The immediate discriminator is now: **extract the complete normalized response, compute the `q`-weighted source-row moment where a fixed-axis synthesis exists, and then locate the first residual factor, if any, that destroys the resulting Sobolev margin.** Canonical seam-ratio growth and bounded-moment source-row proliferation are no longer live explanations.