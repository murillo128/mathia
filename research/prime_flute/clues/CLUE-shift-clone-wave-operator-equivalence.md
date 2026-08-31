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
---

# Do the prime flute and the all-composite shift clone have complete relative wave operators?

## Observation

PF-125 gives a global marked quasi-isometric comparison between the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1`, with metric coefficients tending to one at infinity and exact isometry sufficiently deep in every cusp. PF-126 shows that the resulting zeroth-order metric defect is weak `L^1` and lies in every `L^r`, `r>1`, but that estimate is not strong enough by itself for scattering.

Güneysu--Thalmaier's no-injectivity-radius criterion gives a precise stronger target: for smooth complete quasi-isometric metrics with Ricci curvature bounded below, finiteness of

\[
\int_X \mu_j(x,1)^{-1}\,\delta_{g,h}(x)\,d\mu_j(x)
\]

for one of the metrics implies existence and completeness of the two-Hilbert-space wave operators and equality of the absolutely continuous spectra. PF-128 proves that an entire matched collapsing canonical collar contributes only `O(|log(L_+/L)|)` to exactly this inverse-unit-ball-volume weight; PF-109 makes that `O(P^-3)` for every PF-004 canonical pinching separator. Thus the unbounded width of a canonical short collar is not by itself an obstruction.

PF-129 now removes the other obvious end obstruction. PF-122's canonical cusp mismatch depends only on the adjacent first difference `d_n=|epsilon_n-epsilon_{n+1}|`, with `sum d_n<infinity`. Interpolating that trace through a fixed Busemann-height slab and then making the map exactly isometric gives total inverse-unit-ball weighted cusp cost `O(sum d_n)<infinity` over **all** cusps. Thus neither the infinitely many cusp ends nor canonical collar collapse forces divergence of the scattering criterion.

## Research question

Can the PF-125 prime/shift comparison be replaced or smoothed within its marking class so that the complete Güneysu--Thalmaier weighted metric-deviation integral is finite, and hence

\[
W_\pm(\Delta_{X_+},\Delta_X,I)
\]

exist and are complete?

Equivalently, does the exact all-composite shift clone lie in the same absolutely-continuous Laplace spectral class as the prime flute under a natural marked identification, beyond the compact-relative-resolvent/essential-spectrum equivalence already proved in PF-125?

## Why it may matter

A positive answer would rule out another natural spectral carrier: not only the essential spectrum but the absolutely continuous dynamical scattering class would survive replacement of every prime label by a composite one. That would make any RH-relevant mechanism depend on finer data than this relative wave-equivalence class.

A negative answer could be more informative than failure of a generic theorem only if it identifies a genuine bounded-height, noncanonical-thin, interface, or infinite-assembly mechanism that survives both PF-128's full canonical-collar cancellation and PF-129's summable all-cusp normalization.

## Decisive test

A positive resolution must construct a smooth complete common-manifold comparison satisfying the hypotheses of Güneysu--Thalmaier and prove the weighted integral globally. In particular it must:

1. reconcile PF-129's summable cusp normalization with the lower pant-body maps without reintroducing a nonsummable transition cost;
2. control the thick/pant-body contribution in strong weighted `L^1`, not merely use PF-126's weak-`L^1` estimate;
3. control every non-cusp Margulis-thin component relevant to the ambient unit-ball volume, not assume without proof that every short simple closed geodesic belongs to the PF-004 canonical separator family;
4. use PF-128 only where its matched-collar hypotheses are actually established, and sum the resulting thin-part costs;
5. smooth and assemble the local comparisons without losing quasi-isometry or weighted integrability.

A decisive negative resolution should prove an unavoidable divergence of this weighted criterion for every admissible marked quasi-isometric comparison, or establish a stronger operator obstruction to complete wave operators. Failure to globalize one particular chart or one sufficient estimate is not enough.

## Evidence boundary

The clue is not evidence for wave-operator existence. PF-129 proves finite total cost only for the cusp-end sector and does not prove compatibility with the lower pant-body comparison. PF-128 is local to matched standard collars, and PF-109 controls only the PF-004 canonical separator family. PF-126 remains unweighted and does not give strong `L^1`, while PF-125's transported metric is only piecewise smooth in the form used for the compact-resolvent theorem. No current finding proves that the remaining bounded-height body/interface pieces and every noncanonical thin component can be assembled with finite inverse-volume weighted cost.

The relevant prior art is classical geometric scattering rather than prime-specific theory. B. Güneysu and A. Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, supply the exact weighted criterion above. Hempel--Post--Weder and Müller--Salomonsen provide neighboring metric-perturbation scattering results with different geometric hypotheses. Directed checks found no theorem that automatically applies to this infinite-type, zero-systole flute from PF-125's present asymptotic coefficient convergence alone.

## Research disposition

The clue remains accepted for active investigation. PF-129 materially narrows it: the remaining question is specifically the **bounded-height pant-body/interface, noncanonical-thin, and global inverse-unit-ball weighted assembly** after both canonical-collar and all-cusp effects have been removed. Acceptance asserts only that this is a well-posed natural spectral test; it does not assert wave completeness, equality of scattering matrices, resonance equality, determinant identities, or any RH consequence.
