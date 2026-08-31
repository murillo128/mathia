---
id: CLUE-prime-flute-shift-clone-wave-operator-equivalence
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-109-shift-clone-preserves-canonical-separator-pinching-multiplicatively.md
  - research/prime_flute/findings/PF-122-canonical-cusp-strip-gluing-cost-is-summable.md
  - research/prime_flute/findings/PF-125-shift-clone-has-compact-relative-resolvent.md
  - research/prime_flute/findings/PF-126-shift-clone-metric-defect-is-Lp-above-one.md
  - research/prime_flute/findings/PF-128-full-collar-wave-weight-is-collapse-benign.md
  - research/prime_flute/findings/PF-129-cusp-synchronization-has-summable-wave-weight.md
  - research/prime_flute/findings/PF-130-lambert-shift-metric-defect-is-strong-L1-summable.md
  - research/prime_flute/findings/PF-131-lambert-split-ray-trace-mismatch-is-summable.md
  - research/prime_flute/findings/PF-132-full-lambert-split-ray-trace-mismatch-is-summable.md
  - research/prime_flute/findings/PF-133-centered-lambert-split-ray-tail-is-strong-W11.md
  - research/prime_flute/findings/PF-134-lambert-scalar-tail-is-log-weight-summable.md
  - research/prime_flute/findings/PF-135-lambert-scalar-mode-has-subcritical-polynomial-moments.md
  - research/prime_flute/findings/PF-136-long-pre-corner-split-mismatch-has-summable-strong-L1-extension.md
  - research/prime_flute/findings/PF-137-pre-corner-wave-loss-localizes-to-true-thin-part.md
  - research/prime_flute/findings/PF-138-zero-twist-reflection-exhausts-margulis-short-closed-geodesics.md
  - research/prime_flute/findings/PF-139-full-pre-cusp-split-mismatch-has-summable-two-sided-extension.md
---

# Do the prime flute and the all-composite shift clone have complete relative wave operators?

## Observation

PF-125 gives a global marked quasi-isometric comparison between the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1`, with metric coefficients tending to one at infinity and exact isometry sufficiently deep in every cusp. PF-126 shows that the resulting coarse zeroth-order metric defect is weak `L^1` and lies in every `L^r`, `r>1`, but that estimate is not strong enough by itself for scattering.

Güneysu--Thalmaier's no-injectivity-radius criterion gives the relevant stronger target: for smooth complete quasi-isometric metrics with Ricci curvature bounded below, finiteness of

\[
\int_X \mu_j(x,1)^{-1}\,\delta_{g,h}(x)\,d\mu_j(x)
\]

for one of the metrics implies existence and completeness of the two-Hilbert-space wave operators and equality of the absolutely continuous spectra.

Several natural sources of divergence have now been removed by canonical findings. PF-128 proves that a matched collapsing standard collar contributes only `O(|log(L_+/L)|)` to the inverse-unit-ball weight, and PF-109 makes this `O(P^-3)` for every PF-004 canonical pinching separator. PF-129 gives a finite total weighted cost for the entire cusp family by synchronizing each cusp through a fixed Busemann slab and making the comparison exactly isometric above it. PF-130 shows that the independent PF-121 Lambert-body deformations have summable strong-`L^1` metric mass, while PF-131--PF-136 identify the complete split-ray mismatch and propagate it through the long pre-first-corner sector without destroying that unweighted `L^1` scale.

PF-137 materially changed the wave gate by showing that a narrow internal Lambert/split chart is not itself an ambient thin region. On every fixed injectivity-radius-thick part, the ambient radius-one hyperbolic ball has a uniform positive area floor, so an unweighted strong-`L^1` estimate already gives the Güneysu--Thalmaier weighted estimate there. Any residual divergence must therefore be supported on the true ambient Margulis-thin set.

PF-138 closes the remaining **geometric classification** of the closed thin part for the source prime metric. Every simple closed geodesic of length at most `2 arsinh 1` is either a distinguished tight-flute cuff or a PF-004/PF-034 consecutive-block separator. The distinguished cuffs tend to infinity, so the tail has no noncanonical closed thin cores. Moreover the shortness condition bounds the number of canonical blocks with left label `P` by `O(P^0.525)`; PF-109 gives `O(P^-3)` matched log-length defect for each one, and PF-128 therefore yields a finite sum of local model collar costs over the entire closed thin family.

PF-139 removes another genuine assembly ambiguity. It constructs a two-sided Fermi correction of the **full** left/right PF-121 split mismatch from the finite split endpoint all the way to the canonical standard cusp horocycle `y=1`. The correction leaves every finite-cuff and outer-cusp boundary trace unchanged, has pantwise bilipschitz constants tending to one even for extreme neighboring gap ratios, and has summable strong-`L^1` metric defect. Thus unequal Lambert corner heights and the previously open middle/post-corner part of the artificial split no longer constitute a separate two-dimensional extension obstruction.

The unresolved common-map bridge is now more specific. The split-coherent lower-pentagon map produced by PF-139 still has to be handed off at the full `y=1` horocycle to PF-129's preferred cusp normalization, and PF-128's optimized maps on every PF-138 closed thin collar still have to be realized compatibly inside the same global marking. Those two handoffs, plus smoothing, are the remaining geometric gates before the weighted scattering theorem can be invoked.

## Research question

Can the PF-125 prime/shift comparison be replaced or smoothed within its marking class so that the complete Güneysu--Thalmaier weighted metric-deviation integral is finite, and hence

\[
W_\pm(\Delta_{X_+},\Delta_X,I)
\]

exist and are complete?

After PF-139 the decisive question is no longer whether the two Lambert halves themselves can be made split-coherent. It is whether one can complete **both remaining external handoffs** with finite total weighted cost:

1. reconcile the PF-139 lower-pentagon map with the PF-129 standard-cusp map across the full horocycle/interface, not merely at the artificial split point;
2. realize PF-128's summable matched-collar model cost for every PF-138 closed thin core while preserving those pant/cusp traces.

Equivalently, does the exact all-composite shift clone lie in the same absolutely-continuous Laplace spectral class as the prime flute under a natural marked identification, beyond the compact-relative-resolvent/essential-spectrum equivalence already proved in PF-125?

## Why it may matter

A positive answer would rule out another natural spectral carrier: not only the essential spectrum but the absolutely continuous dynamical scattering class would survive replacement of every prime label by a composite one. Any RH-relevant mechanism would then have to live beyond this relative wave-equivalence class.

A negative answer would now be informative only if it identifies a genuine **horocycle, closed-thin-interface, or operator obstruction** that survives the established split extension, thick-part localization, cusp budget, and complete closed-thin model budget. PF-137 rules out fictitious inverse-volume losses caused solely by internal chart narrowing, PF-138 rules out a missing noncanonical short-core family, and PF-139 rules out unequal Lambert corner heights as an unweighted two-dimensional split-extension obstruction.

## Decisive test

A positive resolution must construct a smooth complete common-manifold comparison satisfying the hypotheses of Güneysu--Thalmaier and prove the weighted integral globally. In particular it must:

1. start from a split-coherent pant-body comparison using PF-139, retaining PF-124's exact finite-cuff zero-twist traces and the summable strong-`L^1` body budget;
2. prove a **full-horocycle handoff** from that lower-pentagon comparison to PF-129's cusp normalization with summable weighted cost, rather than checking only the split ray or outer rays separately;
3. use PF-137 on every fixed ambient thick part, where the inverse-unit-ball factor is uniformly bounded;
4. use PF-138 to exhaust the source-metric closed thin cores by the finitely many short head cuffs and the PF-004 canonical separator family;
5. realize PF-128's summable matched-collar model cost for that entire family **within the same global marking**, rather than summing local maps whose boundary traces may be incompatible;
6. smooth and assemble the horocycle, collar, and thick-body transitions without losing quasi-isometry or weighted integrability.

A decisive negative resolution should prove an unavoidable divergence of this weighted criterion for every admissible marked quasi-isometric comparison, or establish a stronger operator obstruction to complete wave operators. A divergent estimate obtained solely from an internal split-strip width, solely from unequal Lambert corner heights, or solely from postulating an unclassified noncanonical thin family is no longer admissible after PF-137--PF-139.

## Evidence boundary

The clue is not evidence for wave-operator existence. PF-129 proves finite total cost for the cusp-end sector **once its boundary trace is imposed**. PF-139 proves that the lower Lambert pair can be made split-coherent up to `y=1` with summable strong-`L^1` cost while preserving the genuine pant boundaries, but it does not prove that its complete `y=1` horocycle trace is the PF-129 trace. PF-137 proves the inverse-volume factor is harmless on each fixed ambient thick part. PF-138 proves that all sufficiently short closed source-metric cores belong to the canonical separator family (up to a finite cuff head) and that the **sum of PF-128 local model collar costs over that family is finite**.

What remains unproved is the final common-map bridge. PF-128's collar comparison is a local boundary-to-boundary model, PF-129 fixes the preferred cusp normalization, and PF-139 fixes the internal Lambert split while deliberately leaving the full horocycle handoff open. No current finding proves that these constructions can all be chosen with compatible external traces and smoothed into one complete quasi-isometric identification while preserving the full Güneysu--Thalmaier weighted integral.

The relevant prior art remains classical geometric scattering rather than prime-specific theory. B. Güneysu and A. Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, supply the weighted criterion above. The 2024 Güneysu--Marot Kato--Ricci extension retains the same inverse-unit-ball-volume factor. Hempel--Post--Weder and Müller--Salomonsen provide neighboring metric-perturbation scattering results under different geometric hypotheses. Directed checks found no theorem that automatically performs the required global compatible smoothing for this infinite-type, zero-systole prime/shift pair.

## Research disposition

The clue remains accepted for active investigation. PF-139 removes the internal Lambert split as an independent global-assembly gate. The next decisive mathematical task is therefore the **external interface problem**: first make the complete `y=1` horocycle handoff to the PF-129 cusp map summable, then fit the PF-128 canonical-collar comparisons into that same boundary-coherent marking. Acceptance asserts only that this is a well-posed natural spectral test; it does not assert wave completeness, equality of scattering matrices, resonance equality, determinant identities, or any RH consequence.