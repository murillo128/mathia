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

PF-137 materially changes the remaining wave gate. The apparently sharper pre-corner cost `M_n|c_n|` arose only after pessimistically identifying a narrow internal Lambert/split chart width with the ambient unit-ball volume. On every fixed injectivity-radius-thick part, however, the ambient radius-one hyperbolic ball has a uniform positive area floor. Therefore PF-136's unweighted strong-`L^1` estimate automatically implies the Güneysu--Thalmaier weighted estimate there. Small split-strip width by itself is not an intrinsic wave obstruction.

Consequently any residual divergence from the PF-136 support must lie in the **true ambient Margulis-thin set**. For a complete hyperbolic surface this means cusp regions or collars around sufficiently short simple closed geodesics. The cusp family is already controlled by PF-129. PF-128 plus PF-109 control standard collars only when their core belongs to the matched PF-004 canonical separator family. The unresolved geometric sector is therefore sharply localized to **noncanonical short-geodesic collars intersecting the support of the boundary-coherent comparison**, together with the smooth global assembly/interface problem.

## Research question

Can the PF-125 prime/shift comparison be replaced or smoothed within its marking class so that the complete Güneysu--Thalmaier weighted metric-deviation integral is finite, and hence

\[
W_\pm(\Delta_{X_+},\Delta_X,I)
\]

exist and are complete?

After PF-137 the decisive local question is no longer whether a narrow Lambert chart forces an inverse-volume loss. It is whether every genuinely Margulis-thin non-cusp component relevant to the comparison can be matched with summable weighted cost, or whether some noncanonical short-geodesic family amplifies the prime/shift defect in a way not seen by the canonical separator controls.

Equivalently, does the exact all-composite shift clone lie in the same absolutely-continuous Laplace spectral class as the prime flute under a natural marked identification, beyond the compact-relative-resolvent/essential-spectrum equivalence already proved in PF-125?

## Why it may matter

A positive answer would rule out another natural spectral carrier: not only the essential spectrum but the absolutely continuous dynamical scattering class would survive replacement of every prime label by a composite one. Any RH-relevant mechanism would then have to live beyond this relative wave-equivalence class.

A negative answer would be informative only if it identifies a genuine **ambient thin-geometry** or operator obstruction that survives the existing matched controls. PF-137 specifically rules out treating an internal coordinate narrowing as such an obstruction. A surviving divergence must be tied to actual injectivity-radius collapse, noncanonical short closed geodesics, a failure of globally coherent smoothing, or a stronger obstruction to wave completeness.

## Decisive test

A positive resolution must construct a smooth complete common-manifold comparison satisfying the hypotheses of Güneysu--Thalmaier and prove the weighted integral globally. In particular it must:

1. impose PF-125/PF-129-compatible split-ray, finite-cuff, and cusp traces on a pant-body construction while retaining the summable strong-`L^1` localization established by PF-130--PF-136;
2. use PF-137 on every fixed ambient thick part, where the inverse-unit-ball factor is uniformly bounded, rather than paying a fictitious `1/H` penalty from an internal split-strip width;
3. identify every non-cusp component of the true Margulis-thin set that intersects the support of the comparison and match its short core geodesic to the clone geometry;
4. prove a summable bound for the resulting noncanonical collar costs, using PF-128 only where its matched-collar hypotheses are actually established and without assuming that all short geodesics are PF-004 canonical separators;
5. reconcile those thin-component maps with the already-controlled cusp and Lambert pieces;
6. smooth and assemble the local comparisons without losing quasi-isometry or weighted integrability.

A decisive negative resolution should prove an unavoidable divergence of this weighted criterion for every admissible marked quasi-isometric comparison, or establish a stronger operator obstruction to complete wave operators. A divergent estimate obtained solely by replacing ambient unit-ball area with a chosen Lambert-chart width is no longer admissible after PF-137.

## Evidence boundary

The clue is not evidence for wave-operator existence. PF-129 proves finite total cost only for the cusp-end sector. PF-128 is local to matched standard collars, and PF-109 controls only the PF-004 canonical separator family. PF-130--PF-136 establish increasingly coherent unweighted strong-`L^1` control of the Lambert-body and split-ray comparison, but they do not classify every ambient thin component. PF-137 proves that the inverse-volume factor is harmless on each fixed ambient thick part; it does **not** prove that every short simple closed geodesic in the infinite flute is canonical, nor that the remaining noncanonical thin collars have summable matched length distortion.

No current finding supplies one globally smooth boundary-coherent marking with finite Güneysu--Thalmaier weight over all noncanonical thin collars and interfaces. PF-125's transported metric is only piecewise smooth in the form used for the compact-resolvent theorem.

The relevant prior art remains classical geometric scattering rather than prime-specific theory. B. Güneysu and A. Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, supply the weighted criterion above. The 2024 Güneysu--Marot Kato--Ricci extension retains the same inverse-unit-ball-volume factor, so constant curvature `-1` does not by itself remove a genuinely thin-region gate. Hempel--Post--Weder and Müller--Salomonsen provide neighboring metric-perturbation scattering results under different geometric hypotheses. Directed checks found no theorem that automatically upgrades the present prime/shift comparison to complete wave operators on this infinite-type, zero-systole surface.

## Research disposition

The clue remains accepted for active investigation. PF-137 removes the last *coordinate-width* version of the pre-corner obstruction and localizes the unresolved weighted problem to genuine ambient thin geometry. The next decisive mathematical task is therefore to classify or control the noncanonical short-geodesic collars met by a boundary-coherent prime/shift comparison and determine whether their total matched collar cost is summable. Smooth global assembly remains a separate final gate. Acceptance asserts only that this is a well-posed natural spectral test; it does not assert wave completeness, equality of scattering matrices, resonance equality, determinant identities, or any RH consequence.
