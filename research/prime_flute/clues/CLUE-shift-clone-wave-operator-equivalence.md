---
id: CLUE-prime-flute-shift-clone-wave-operator-equivalence
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-125-shift-clone-has-compact-relative-resolvent.md
  - research/prime_flute/findings/PF-128-full-collar-wave-weight-is-collapse-benign.md
  - research/prime_flute/findings/PF-138-zero-twist-reflection-exhausts-margulis-short-closed-geodesics.md
  - research/prime_flute/findings/PF-139-full-pre-cusp-split-mismatch-has-summable-two-sided-extension.md
  - research/prime_flute/findings/PF-140-full-horocycle-handoff-has-summable-wave-weight.md
  - research/prime_flute/findings/PF-142-zero-twist-reflection-removes-short-collar-phase-gauge.md
  - research/prime_flute/findings/PF-143-nonconstant-collar-trace-is-not-collapse-suppressed.md
  - research/prime_flute/findings/PF-144-reflection-odd-collar-trace-has-sharp-L1-angular-welding-cost.md
---

# Do the prime flute and the all-composite shift clone have complete relative wave operators?

## Observation

PF-125 already places the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1` in the same compact-relative-resolvent and essential-spectrum class. The stronger scattering target is Güneysu--Thalmaier's no-injectivity-radius criterion: after transporting one metric to the other, finiteness of the inverse-unit-ball weighted metric-deviation integral gives existence and completeness of the two-Hilbert-space wave operators and equality of the absolutely continuous spectra.

Most local sectors of that integral have now been controlled. PF-128 shows that matched collapsing standard collars do not amplify the logarithmic core-length defect in the scattering weight. PF-139 supplies a boundary-coherent lower-pant comparison with summable strong-`L^1` body correction through the standard cusp entry, PF-140 closes the horocycle/cusp handoff at finite total wave weight, and PF-138 identifies the complete tail family of actual Margulis-short closed cores that still require collar insertion.

PF-142 removes the constant angular phase from those short-core interfaces by retaining the canonical zero-twist reflection marking. PF-143 and PF-144 then identify the exact local cost of the surviving reflection-odd **angular** trace. If `psi_eta` is the normalized nonconstant angular mismatch on one standard collar boundary and the trace is tail-`C^1`-small, then within the near-isometric angular welding class

\[
\boxed{
\operatorname{Cost}_{\rm angular}(\eta)
\asymp
\|\psi_\eta\|_{L^1(\mathbb S^1)}
}
\]

with constants independent of the collapsing core length. PF-143 supplies the lower bound and PF-144 an explicit reflection-equivariant soft-threshold extension giving the matching upper bound. Thus pinching neither suppresses nor amplifies this mode, and no stronger `W^{1,1}` derivative ledger is intrinsically required.

The unresolved interface is consequently narrower: determine the **actual** normalized trace amplitudes produced by one globally coherent prime/shift body comparison, and reconcile the remaining transverse/radial shape mismatch with PF-128's optimized standard-collar maps.

## Research question

Can the PF-139/PF-140 body-and-cusp comparison be modified around the complete PF-138 family of short closed cores so that one smooth complete globally marked comparison satisfies

\[
\int_X
\mu_g(B_g(x,1))^{-1}
\delta_{g,h}(x)\,d\mu_g(x)<\infty,
\]

and hence the relative wave operators

\[
W_\pm(\Delta_{X_+},\Delta_X,I)
\]

exist and are complete?

After PF-143/PF-144, the angular subproblem has a precise form. For the canonically reflection-normalized boundary mismatches `psi_eta`, prove

\[
\boxed{
\sum_\eta\|\psi_\eta\|_{L^1}<\infty
}
\]

while keeping their `C^1` size tending to zero, or prove that this fails intrinsically. Independently, construct a finite-weight transverse/radial straightening that makes the surrounding body trace land on the standard collar boundaries used by PF-128 without destroying the already-controlled body/cusp sectors.

## Why it may matter

A positive answer would show that the exact prime flute and an exact all-composite control have the same absolutely continuous Laplace spectral class under a natural marked comparison. Together with PF-125, this would rule out both the essential spectrum and the absolutely continuous wave/scattering class as primality selectors for this construction; any RH-relevant mechanism would have to live in finer discrete, resonant, determinant, or genuinely arithmetic data not fixed by those equivalences.

A negative answer is valuable only if it identifies a genuine obstruction in the **actual trace-amplitude sequence, transverse/radial interface geometry, or operator theory**. Universal cusp collapse, Lambert chart narrowing, unclassified short geodesics, the standard-horocycle handoff, constant phase, and an artificial derivative penalty for nonconstant angular welding are no longer independent failure modes.

## Decisive test

A positive resolution must construct one smooth complete comparison rather than sum incompatible local models. It must start from the PF-139/PF-140 global body/cusp map, use PF-138 to isolate every tail short core, retain the PF-142 reflection anchors, compute the induced normalized boundary traces, and prove their `L^1` amplitudes summable. PF-144 can then supply the angular welding at exactly that total cost. The proof must separately straighten the transverse/radial boundary shape onto PF-128's optimized collar models, control all interpolation and smoothing zones in the same inverse-unit-ball weighted norm, verify global quasi-isometry and completeness, and only then invoke Güneysu--Thalmaier.

A decisive negative resolution should prove either that the actual canonical trace amplitudes have unavoidable divergent `L^1` mass, that every admissible marked comparison incurs a divergent transverse/radial cost, or that complete wave operators fail by a stronger operator-theoretic obstruction. Divergence produced only by a non-optimized angular interpolation, by summing `||psi_eta'||_1` when PF-144 shows that derivative ledger is unnecessary, or by reintroducing a constant phase that PF-142 removes is not decisive.

## Evidence boundary

This clue remains a research question, not evidence for wave-operator existence. PF-143/PF-144 characterize only the local **angular-preserving** welding cost once a standard collar boundary and a small reflection-odd trace `psi` are given. They do not prove that the actual prime/shift body traces satisfy the required `C^1` smallness or `L^1` summability, and they do not control a body image whose collar boundary arrives with transverse/radial shape error.

PF-128 is likewise a local optimized model for a matched standard collar; PF-139/PF-140 control the body/cusp comparison outside the unresolved closed-thin interfaces. No finding yet assembles all of these maps into one smooth complete global comparison. Even complete wave operators would not imply equality of scattering matrices, resonances, discrete eigenvalues, Selberg/Ruelle objects, relative determinants, or any RH statement.

The external theorem remains B. Güneysu and A. Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`; it supplies the sufficient weighted criterion, not the missing prime-flute assembly theorem.

## Research disposition

The clue remains `accepted`. PF-143 and PF-144 materially narrow its angular gate: for the canonical reflection-odd sector, the necessary-and-sufficient local near-isometric welding scale is `||psi_eta||_1`, with no collapsing-collar factor and no forced `W^{1,1}` derivative penalty. Continued work should therefore compute or bound the **actual** PF-142-normalized `L^1` trace amplitudes and solve the independent transverse/radial collar-body compatibility problem. Acceptance asserts only that this remaining global assembly question is mathematically well-posed and worth testing.