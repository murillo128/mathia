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
---

# Do the prime flute and the all-composite shift clone have complete relative wave operators?

## Observation

PF-125 gives a global marked quasi-isometric comparison between the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1`, with metric coefficients tending to one at infinity and exact isometry sufficiently deep in every cusp. PF-126 shows that the resulting coarse zeroth-order metric defect is weak `L^1` and lies in every `L^r`, `r>1`, but that estimate is not strong enough by itself for scattering.

Güneysu--Thalmaier's no-injectivity-radius criterion gives the relevant stronger target: for smooth complete quasi-isometric metrics with Ricci curvature bounded below, finiteness of

\[
\int_X \mu_j(x,1)^{-1}\,\delta_{g,h}(x)\,d\mu_j(x)
\]

for one of the metrics implies existence and completeness of the two-Hilbert-space wave operators and equality of the absolutely continuous spectra.

Several natural sources of divergence have now been removed by canonical findings. PF-128 proves that a matched collapsing standard collar contributes only `O(|log(L_+/L)|)` to the inverse-unit-ball weight, and PF-109 makes this `O(P^-3)` for every PF-004 canonical pinching separator. PF-129 gives a finite total weighted cost for the entire cusp family by synchronizing each cusp through a fixed Busemann slab and making the comparison exactly isometric above it. PF-130 shows that the independent PF-121 Lambert-body deformations have summable strong-`L^1` metric mass, while PF-131--PF-136 show that the left/right split-ray mismatch can be differentiated, propagated through the growing Lambert geometry, and extended across the long pre-first-corner sector without destroying that unweighted `L^1` scale.

PF-137 materially changed the wave gate by showing that a narrow internal Lambert/split chart is not itself an ambient thin region. On every fixed injectivity-radius-thick part, the ambient radius-one hyperbolic ball has a uniform positive area floor, so PF-136's unweighted strong-`L^1` estimate already gives the Güneysu--Thalmaier weighted estimate there. Any residual divergence must therefore be supported on the true ambient Margulis-thin set.

PF-138 now closes the remaining **geometric classification** of the closed thin part for the source prime metric. Every simple closed geodesic of length at most `2 arsinh 1` is either a distinguished tight-flute cuff or a PF-004/PF-034 consecutive-block separator. The distinguished cuffs tend to infinity, so the tail has no noncanonical closed thin cores. Moreover the shortness condition bounds the number of canonical blocks with left label `P` by `O(P^0.525)`; PF-109 gives `O(P^-3)` matched log-length defect for each one, and PF-128 therefore yields a finite sum of local model collar costs over the entire closed thin family.

The unresolved issue is no longer a hidden noncanonical short-geodesic family. It is whether the local collar comparisons realizing that finite model budget can be made compatible with the PF-129 cusp normalization and the PF-130--PF-136 boundary-coherent body correction inside **one smooth global marking**.

## Research question

Can the PF-125 prime/shift comparison be replaced or smoothed within its marking class so that the complete Güneysu--Thalmaier weighted metric-deviation integral is finite, and hence

\[
W_\pm(\Delta_{X_+},\Delta_X,I)
\]

exist and are complete?

After PF-138 the decisive question is an assembly/interface problem: can the matched PF-128 collar maps for all actual closed thin cores be realized simultaneously within the same boundary-coherent global comparison, with their already-summable weighted cost preserved through the transitions to the Lambert/body and cusp pieces?

Equivalently, does the exact all-composite shift clone lie in the same absolutely-continuous Laplace spectral class as the prime flute under a natural marked identification, beyond the compact-relative-resolvent/essential-spectrum equivalence already proved in PF-125?

## Why it may matter

A positive answer would rule out another natural spectral carrier: not only the essential spectrum but the absolutely continuous dynamical scattering class would survive replacement of every prime label by a composite one. Any RH-relevant mechanism would then have to live beyond this relative wave-equivalence class.

A negative answer would now be informative only if it identifies a genuine **global compatibility or operator obstruction** that survives the established thick-part, cusp, and complete closed-thin model budgets. PF-137 rules out fictitious inverse-volume losses caused by internal chart narrowing, and PF-138 rules out a missing noncanonical short-core family as the source-metric explanation.

## Decisive test

A positive resolution must construct a smooth complete common-manifold comparison satisfying the hypotheses of Güneysu--Thalmaier and prove the weighted integral globally. In particular it must:

1. impose PF-125/PF-129-compatible split-ray, finite-cuff, and cusp traces on a pant-body construction while retaining the summable strong-`L^1` localization established by PF-130--PF-136;
2. use PF-137 on every fixed ambient thick part, where the inverse-unit-ball factor is uniformly bounded, rather than paying a fictitious `1/H` penalty from an internal split-strip width;
3. use PF-138 to exhaust the source-metric closed thin cores by the finitely many short head cuffs and the PF-004 canonical separator family;
4. realize PF-128's summable matched-collar model cost for that entire family **within the same global marking**, rather than summing local maps whose boundary traces may be incompatible;
5. reconcile those collar maps with the already-controlled cusp and Lambert pieces;
6. smooth and assemble the local comparisons without losing quasi-isometry or weighted integrability.

A decisive negative resolution should prove an unavoidable divergence of this weighted criterion for every admissible marked quasi-isometric comparison, or establish a stronger operator obstruction to complete wave operators. A divergent estimate obtained solely from an internal chart width, or solely from postulating an unclassified noncanonical thin family, is no longer admissible after PF-137/PF-138.

## Evidence boundary

The clue is not evidence for wave-operator existence. PF-129 proves finite total cost for the cusp-end sector. PF-137 proves the inverse-volume factor is harmless on each fixed ambient thick part. PF-138 proves that all sufficiently short closed source-metric cores belong to the canonical separator family (up to a finite cuff head) and that the **sum of PF-128 local model collar costs over that family is finite**.

What remains unproved is the common-map bridge. PF-128's collar comparison is a local boundary-to-boundary model; PF-130--PF-136 construct the body/split correction by a different local procedure; PF-129 fixes the cusp normalization; and PF-125's compact-resolvent marking is only piecewise smooth in the form used there. No current finding proves that all these local constructions can be chosen with compatible traces and smoothed into one complete quasi-isometric identification while preserving the full Güneysu--Thalmaier weighted integral.

The relevant prior art remains classical geometric scattering rather than prime-specific theory. B. Güneysu and A. Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, supply the weighted criterion above. The 2024 Güneysu--Marot Kato--Ricci extension retains the same inverse-unit-ball-volume factor. Hempel--Post--Weder and Müller--Salomonsen provide neighboring metric-perturbation scattering results under different geometric hypotheses. Directed checks found no theorem that automatically performs the required global compatible smoothing for this infinite-type, zero-systole prime/shift pair.

## Research disposition

The clue remains accepted for active investigation. PF-138 removes the previously open noncanonical-short-collar sector and supplies a finite model budget for every closed source-metric thin core. The next decisive mathematical task is therefore **global compatibility**: construct one smooth boundary-coherent comparison whose restrictions to the canonical collars, cusp slabs, and Lambert/body pieces realize the already-proved local weighted budgets simultaneously. Acceptance asserts only that this is a well-posed natural spectral test; it does not assert wave completeness, equality of scattering matrices, resonance equality, determinant identities, or any RH consequence.
