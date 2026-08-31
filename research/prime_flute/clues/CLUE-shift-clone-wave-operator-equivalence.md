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
---

# Do the prime flute and the all-composite shift clone have complete relative wave operators?

## Observation

PF-125 gives a global marked quasi-isometric comparison between the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1`, with metric coefficients tending to one at infinity and exact isometry sufficiently deep in every cusp. PF-126 shows that the resulting zeroth-order metric defect is weak `L^1` and lies in every `L^r`, `r>1`, but that estimate is not strong enough by itself for scattering.

Güneysu--Thalmaier's no-injectivity-radius criterion gives a precise stronger target: for smooth complete quasi-isometric metrics with Ricci curvature bounded below, finiteness of

\[
\int_X \mu_j(x,1)^{-1}\,\delta_{g,h}(x)\,d\mu_j(x)
\]

for one of the metrics implies existence and completeness of the two-Hilbert-space wave operators and equality of the absolutely continuous spectra. PF-128 proves that an entire matched collapsing canonical collar contributes only `O(|log(L_+/L)|)` to exactly this inverse-unit-ball-volume weight; PF-109 makes that `O(P^-3)` for every PF-004 canonical pinching separator. Thus the unbounded width of a canonical short collar is not by itself an obstruction.

PF-129 removes the other obvious end obstruction. PF-122's canonical cusp mismatch depends only on the adjacent first difference `d_n=|epsilon_n-epsilon_{n+1}|`, with `sum d_n<infinity`. Interpolating that trace through a fixed Busemann-height slab and then making the map exactly isometric gives total inverse-unit-ball weighted cusp cost `O(sum d_n)<infinity` over **all** cusps. Thus neither the infinitely many cusp ends nor canonical collar collapse forces divergence of the scattering criterion.

PF-130 sharpens the bounded-height coefficient side. The isolated PF-121 Lambert comparison has strong-`L^1` metric/density mass

\[
O\!\left(\frac{\delta_n}{\sinh a_n}\right),
\]

and these masses are summable over the exact prime/shift sequence. Therefore the coarse weak-`L^1` endpoint of PF-126 is not caused by an unavoidable order-`1/p_n` deformation spread over order-one area inside each Lambert body.

PF-131--PF-134 then audit the missing artificial-split boundary data rather than silently treating the independent Lambert maps as glueable. They show successively that the bounded-height trace mismatch is summable, the **entire** split-ray mismatch is summable in `L^infinity + dot W^{1,1}`, the centered deep tail is strong `W^{1,1}`, and the sole surviving scalar tail mode remains summable even after multiplication by the canonical `O(log p_n)` pre-cusp Busemann length.

PF-135 strengthens the last point materially. The scalar mode `c_n=beta_n-beta_{n+1}` satisfies

\[
\sum_n p_n^\alpha |c_n|<\infty
\qquad(0\le\alpha<19/40)
\]

using only the already-audited Baker--Harman--Pintz input. The natural square-root adjacent-cuff aspect factor is only `O(p_n^(21/80))`, and PF-135 proves that the reciprocal combined Fermi width in the **middle corridor between the two Lambert corner heights** pays at most that factor. Hence extreme neighboring prime-gap ratios cannot create divergence there. The remaining boundary problem is narrower: before the first corner both Lambert widths can be simultaneously much smaller, and a naive transverse correction can pay an individual large-cuff factor. PF-135 does not show that such a loss is necessary or summable.

## Research question

Can the PF-125 prime/shift comparison be replaced or smoothed within its marking class so that the complete Güneysu--Thalmaier weighted metric-deviation integral is finite, and hence

\[
W_\pm(\Delta_{X_+},\Delta_X,I)
\]

exist and are complete?

Equivalently, does the exact all-composite shift clone lie in the same absolutely-continuous Laplace spectral class as the prime flute under a natural marked identification, beyond the compact-relative-resolvent/essential-spectrum equivalence already proved in PF-125?

## Why it may matter

A positive answer would rule out another natural spectral carrier: not only the essential spectrum but the absolutely continuous dynamical scattering class would survive replacement of every prime label by a composite one. That would make any RH-relevant mechanism depend on finer data than this relative wave-equivalence class.

A negative answer could be more informative than failure of a generic theorem only if it identifies a genuine pre-corner boundary-coherence, noncanonical-thin, interface, or infinite-assembly mechanism that survives PF-128's full canonical-collar cancellation, PF-129's summable all-cusp normalization, PF-130's summable isolated Lambert-body coefficient mass, and PF-131--PF-135's trace-level cancellations.

## Decisive test

A positive resolution must construct a smooth complete common-manifold comparison satisfying the hypotheses of Güneysu--Thalmaier and prove the weighted integral globally. In particular it must:

1. impose PF-125/PF-129-compatible split-ray, finite-cuff, and cusp traces on a pant-body construction while retaining a summable version of PF-130's strong-`L^1` localization;
2. solve the **pre-first-corner** two-dimensional extension problem without paying a nonsummable individual large-cuff factor; PF-135 already removes the weaker square-root aspect loss in the middle corridor;
3. convert the resulting body estimate to strong **weighted** `L^1` wherever the ambient unit-ball volume is uniformly controlled;
4. control every non-cusp Margulis-thin component relevant to the ambient unit-ball volume, not assume without proof that every short simple closed geodesic belongs to the PF-004 canonical separator family;
5. use PF-128 only where its matched-collar hypotheses are actually established, and sum the resulting thin-part costs;
6. smooth and assemble the local comparisons without losing quasi-isometry or weighted integrability.

A decisive negative resolution should prove an unavoidable divergence of this weighted criterion for every admissible marked quasi-isometric comparison, or establish a stronger operator obstruction to complete wave operators. Divergence of one naive transverse correction is not enough unless the loss is shown to be intrinsic.

## Evidence boundary

The clue is not evidence for wave-operator existence. PF-129 proves finite total cost only for the cusp-end sector. PF-128 is local to matched standard collars, and PF-109 controls only the PF-004 canonical separator family. PF-130 proves unweighted strong `L^1` only for independent one-parameter Lambert maps. PF-131--PF-135 show that their complete boundary mismatch is much better behaved than the raw reciprocal-prime scale, including polynomially weighted summability of the residual scalar mode, but they do **not** supply a boundary-coherent two-dimensional marking or the ambient inverse-unit-ball weight. PF-125's transported metric is only piecewise smooth in the form used for the compact-resolvent theorem. No current finding proves that the pre-corner body/interface pieces and every noncanonical thin component can be assembled with finite inverse-volume weighted cost.

The relevant prior art is classical geometric scattering rather than prime-specific theory. B. Güneysu and A. Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, supply the exact weighted criterion above. The 2024 Güneysu--Marot Kato--Ricci extension retains the same inverse-unit-ball-volume factor, so constant curvature `-1` does not remove the remaining thin-region gate. Hempel--Post--Weder and Müller--Salomonsen provide neighboring metric-perturbation scattering results with different geometric hypotheses. Directed checks found no theorem that automatically applies to this infinite-type, zero-systole flute from the present combination of compact-resolvent equivalence, thin-part controls, local strong-`L^1` body estimates, and trace polynomial moments.

## Research disposition

The clue remains accepted for active investigation. PF-128--PF-135 now remove a sequence of cheap divergence mechanisms: full canonical-collar collapse, the infinite cusp family, an order-one-area Lambert-body interpretation of the reciprocal-prime deformation, bounded and deep split-ray trace accumulation, logarithmic cusp-entry propagation, and the natural square-root neighboring-cuff aspect loss in the middle Lambert corridor. The remaining question is specifically the **pre-first-corner boundary-coherent weighted extension, noncanonical-thin, and global assembly** problem. Acceptance asserts only that this is a well-posed natural spectral test; it does not assert wave completeness, equality of scattering matrices, resonance equality, determinant identities, or any RH consequence.
