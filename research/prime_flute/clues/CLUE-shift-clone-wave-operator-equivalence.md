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
  - research/prime_flute/findings/PF-140-full-horocycle-handoff-has-summable-wave-weight.md
  - research/prime_flute/findings/PF-141-bounded-collar-phase-welding-is-wave-weight-collapse-suppressed.md
  - research/prime_flute/findings/PF-142-zero-twist-reflection-removes-short-collar-phase-gauge.md
---

# Do the prime flute and the all-composite shift clone have complete relative wave operators?

## Observation

PF-125 already puts the exact prime flute and exact all-composite shift clone `p_n -> p_n+1` in the same compact-relative-resolvent/essential-spectrum class. The stronger scattering target is Güneysu--Thalmaier's no-injectivity-radius criterion: after transporting one metric to the other, finiteness of the inverse-unit-ball weighted metric-deviation integral implies existence and completeness of the two-Hilbert-space wave operators and equality of the absolutely continuous spectra.

The candidate obstruction has been narrowed substantially. PF-128 proves that an entire matched collapsing standard collar costs only `O(|log(L_+/L)|)` in the weighted criterion, and PF-109 makes that `O(P^-3)` for every canonical pinching separator. PF-129 gives a summable budget for the complete cusp family once an appropriate bottom trace is supplied. PF-130--PF-139 then construct and reconcile the lower Lambert/pant-body maps: their strong-`L^1` body defect is summable, internal split narrowing is not an ambient thinness obstruction, all short closed source geodesics are classified by PF-138, and the left/right Lambert split mismatch admits a summable two-sided extension all the way to the standard cusp entry `y=1`.

PF-140 closes the cusp/horocycle handoff. On the whole normalized standard-cusp sector the exact PF-121 map is exponentially closer to a hyperbolic dilation than its coarse `1+O(delta)` estimate. After restoring the physical pant charts, the leading horocycle mismatch is exactly PF-122's adjacent first-difference mode, while PF-139's top split correction contributes only its summable centered scalar mode. The actual PF-139 trace on `y=1` is therefore `ell^1`-close to the identity in a piecewise first-derivative trace norm and can be cut off directly to exact identity through one fixed Busemann slab with finite total Güneysu--Thalmaier weight.

PF-141 removes collapse amplification of a bounded angular phase: on one short standard collar an explicit central twist costs only `O(L|tau|)`. PF-142 now sharpens that local estimate at the global marked level. PF-124's body comparison can be kept exactly zero-twist-reflection equivariant, and PF-138 gives two canonically marked reflection-fixed points on every tail short separator. Those markings pin the angular origin in source and clone, so the **constant rotation phase is exactly zero** for the canonical equivariant comparison. Reflection without marking would leave a half-turn ambiguity, but the ordered cusp-block/seam marking removes it. Consequently no unproved global sum of `L_gamma|tau_gamma|` is needed for the constant phase mode.

The cusp/horocycle interface and constant angular phase are therefore no longer independent gates. The unresolved issue is concentrated on the **nonconstant reflection-odd angular trace and transverse/radial shape compatibility** between the closed standard collars and the already-controlled body map. PF-138 identifies the relevant tail cores, PF-128 proves that the sum of their optimized length-model costs is finite, and PF-142 removes the constant phase gauge, but no canonical finding yet realizes all local collar comparisons inside the same boundary-coherent global marking with summable shape-straightening cost.

## Research question

Can the PF-139/PF-140 body-and-cusp comparison be modified around the complete PF-138 family of short closed cores so that, simultaneously,

\[
\int_X
\mu_g(B_g(x,1))^{-1}
\delta_{g,h}(x)\,d\mu_g(x)<\infty,
\]

with one smooth complete globally marked comparison, and hence

\[
W_\pm(\Delta_{X_+},\Delta_X,I)
\]

exist and are complete?

Equivalently, can PF-128's boundary-to-boundary optimized collar maps be inserted for every PF-138 canonical short separator while matching the already-established pant-body traces on both collar boundaries at a summable total **nonconstant/transverse shape-interface** cost? PF-142 shows that the canonical marked reflection-equivariant comparison has no constant angular phase to sum. The cusp side no longer needs a separate compatibility construction because PF-140 makes the comparison exactly isometric after a fixed cusp slab.

## Why it may matter

A positive answer would show that the exact prime flute and an exact all-composite control have the same absolutely continuous Laplace spectral class under a natural marked comparison. Together with PF-125, this would rule out both the essential spectrum and the absolutely continuous scattering class as primality selectors for this construction; any RH-relevant mechanism would have to live in finer discrete, resonant, determinant, or genuinely arithmetic data not fixed by that equivalence.

A negative answer is now valuable only if it identifies a genuine **nonconstant/transverse closed-thin interface or operator obstruction**. Universal cusp collapse, internal Lambert chart narrowing, unequal Lambert corner heights, unclassified short geodesics, the full standard-horocycle handoff, and constant angular phase have all been removed as independent failure modes. A surviving amplification mechanism would therefore be structurally sharper than the earlier coarse objections.

## Decisive test

A positive resolution must construct one smooth complete comparison, not merely sum incompatible local maps. A viable proof must:

1. start from the PF-139 lower-pant comparison and PF-140 cusp cutoff, which already give a boundary-coherent body/cusp map with finite weighted contribution away from the closed thin collars;
2. use PF-138 to choose the complete tail family of actual closed Margulis-thin cores, with only a finite exceptional head;
3. retain the PF-124/PF-142 reflection-equivariant marking so that every tail short-core interface is anchored at its two fixed points and no constant phase variable is introduced;
4. replace the comparison on each relevant standard collar by a PF-128-type optimized boundary-to-boundary map and prove that the surrounding body trace can be straightened onto the standard collar boundary with a summable total **nonconstant angular plus transverse/radial shape cost**;
5. control the interpolation annuli and smoothing zones in the same inverse-unit-ball weighted norm, without reintroducing a factor depending adversely on the collapsing core length;
6. verify global quasi-isometry, smooth completeness, reflection-compatible marking, and exact deep-cusp isometry after the modifications;
7. invoke Güneysu--Thalmaier only after the complete global integral is established.

A decisive negative resolution should prove an unavoidable divergence for every admissible marked quasi-isometric comparison, or a stronger obstruction to complete wave operators, concentrated in the remaining nonconstant/transverse closed-thin interface sector. Failure of one convenient collar interpolation, a constant phase introduced by a non-equivariant coordinate choice, or a divergent bound caused solely by a non-optimized coordinate choice is not enough. PF-128, PF-141, and PF-142 already show that those are not intrinsic obstructions.

## Evidence boundary

The clue remains a research question, not evidence for wave-operator existence. PF-140 proves only that the **actual PF-139 standard-horocycle trace** can be killed to exact identity through fixed cusp slabs with summable weighted cost. PF-128 proves only a local optimized model for a matched standard collar. PF-138 classifies the short closed source cores and makes the sum of the matched length-change model budgets finite. PF-141 proves only that a bounded angular phase mismatch on one matched short collar can be interpolated at weighted cost `O(L|tau|)`. PF-142 proves only that, for the canonical marked reflection-equivariant comparison, the **constant** phase is a removable gauge and is exactly pinned to zero on every tail short core. None of those findings controls the remaining nonconstant reflection-odd boundary reparametrization or proves that the PF-128 collar boundary traces can be reconciled summably to the PF-139/PF-140 global body map.

Nor would complete wave operators imply equality of scattering matrices, resonances, discrete eigenvalues, Selberg/Ruelle objects, relative determinants, or any RH statement. The external theorem remains Batu Güneysu and Anton Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`; it supplies the sufficient weighted criterion, not the missing prime-flute assembly theorem.

## Research disposition

The clue remains `accepted` for active investigation, but PF-142 materially narrows its decisive gate again. The full `y=1` horocycle/cusp handoff is resolved at finite total wave weight, matched collar length change is collapse-benign, and the canonical zero-twist reflection marking eliminates the constant angular phase globally rather than merely bounding it collar by collar. The next work should therefore focus only on the **nonconstant reflection-odd angular trace and transverse/radial closed-collar/body interface problem**: straighten and insert PF-128's optimized collars coherently inside the PF-139/PF-140 global marking at finite total weighted cost, or exhibit an intrinsic obstruction showing that this cannot be done. Acceptance asserts only that this final assembly question is mathematically well-posed and worth testing.