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
  - research/prime_flute/findings/PF-145-reflection-even-collar-graph-has-sharp-L1-radial-welding-cost.md
---

# Do the prime flute and the all-composite shift clone have complete relative wave operators?

## Observation

PF-125 already places the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1` in the same compact-relative-resolvent and essential-spectrum class. The stronger scattering target is Güneysu--Thalmaier's no-injectivity-radius criterion: after transporting one metric to the other, finiteness of the inverse-unit-ball weighted metric-deviation integral gives existence and completeness of the two-Hilbert-space wave operators and equality of the absolutely continuous spectra.

Most local sectors of that integral are controlled. PF-128 shows that matched collapsing standard collars do not amplify the logarithmic core-length defect in the scattering weight. PF-139 supplies a boundary-coherent lower-pant comparison with summable strong-`L^1` body correction through the standard cusp entry, PF-140 closes the horocycle/cusp handoff at finite total wave weight, and PF-138 identifies the complete tail family of actual Margulis-short closed cores that still require collar insertion.

PF-142 removes the constant angular phase from those short-core interfaces by retaining the canonical zero-twist reflection marking. PF-143/PF-144 then identify the exact local cost of the surviving reflection-odd angular trace. If `psi_eta` is a small normalized angular mismatch, its optimal local near-isometric welding scale is

\[
\operatorname{Cost}_{\rm angular}(\eta)
\asymp
\|\psi_\eta\|_{L^1(\mathbb S^1)},
\]

with constants independent of the collapsing core length.

PF-145 now closes the analogous **local norm-selection problem** for transverse/radial interface shape. On a fixed interior cross-section of a sufficiently short standard collar, a small reflection-even radial graph `rho_eta` has sharp radial-only weighted welding cost

\[
\operatorname{Cost}_{\rm radial}(\eta)
\asymp
\|\rho_\eta\|_{L^1(\mathbb S^1)},
\]

again without a core-length factor. Moreover a small reflection-equivariant full trace `(rho_eta,psi_eta)` admits a simultaneous local correction of cost

\[
O\!\left(\|\rho_\eta\|_1+\|\psi_\eta\|_1\right).
\]

Thus neither angular nor radial interface geometry intrinsically requires a global `W^{1,1}` derivative ledger, and pinching does not make either nonconstant trace mode automatically cheap. The unresolved interface is now the **actual trace sequence produced by one globally coherent prime/shift body comparison**, not the existence of a suitable local extension norm.

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

After PF-143--PF-145 the short-collar gate has a concrete target. Choose one fixed interior collar interface in the uniformly thick outer slab, prove that the actual PF-139/PF-140 body image is a reflection-equivariant `C^1`-small graph

\[
\Gamma_\eta(\theta)
=\bigl(1+\rho_\eta(\theta),
\theta+\psi_\eta(\theta)\bigr),
\]

with `rho_eta` even and `psi_eta` odd, and establish

\[
\boxed{
\sum_\eta
\left(
\|\rho_\eta\|_{L^1}
+
\|\psi_\eta\|_{L^1}
\right)<\infty.
}
\]

A decisive negative answer would show that this actual canonical trace mass is intrinsically divergent, that the body image cannot be put into the required small-graph regime without divergent weighted cost, or that a stronger operator-theoretic obstruction prevents complete wave operators despite all local geometric estimates.

## Why it may matter

A positive answer would show that the exact prime flute and an exact all-composite control have the same absolutely continuous Laplace spectral class under a natural marked comparison. Together with PF-125, this would rule out both the essential spectrum and the absolutely continuous wave/scattering class as primality selectors for this construction; any RH-relevant mechanism would have to live in finer discrete, resonant, determinant, or genuinely arithmetic data not fixed by those equivalences.

A negative answer is valuable only if it identifies a genuine obstruction in the **actual trace-amplitude sequence, global assembly, or operator theory**. Universal cusp collapse, Lambert chart narrowing, unclassified short geodesics, the standard-horocycle handoff, constant phase, an artificial derivative penalty for angular welding, and an artificial derivative penalty for small radial graph straightening are no longer independent failure modes.

## Decisive test

A positive resolution must construct one smooth complete comparison rather than sum incompatible local models. It must start from the PF-139/PF-140 global body/cusp map, use PF-138 to isolate every tail short core, retain the PF-142 reflection anchors, choose a fixed interior collar cross-section in the uniformly thick outer slab, and compute the induced normalized traces `(rho_eta,psi_eta)`. It must prove their `C^1` size tends to zero and their total `L^1` mass is summable. PF-144/PF-145 can then supply the local collar welding at exactly an additive `L^1` budget. The proof must control all interpolation and smoothing zones in the same inverse-unit-ball weighted norm, verify global quasi-isometry and completeness, and only then invoke Güneysu--Thalmaier.

A decisive negative resolution should prove either that the actual canonical trace amplitudes have unavoidable divergent total `L^1` mass, that every admissible marked comparison fails the required small-graph/summability regime, or that complete wave operators fail by a stronger operator-theoretic obstruction. Divergence produced only by a non-optimized interpolation, by summing trace derivatives when PF-144/PF-145 show that this derivative ledger is unnecessary, or by reintroducing a constant phase that PF-142 removes is not decisive.

## Evidence boundary

This clue remains a research question, not evidence for wave-operator existence. PF-143/PF-144 characterize the local angular cost once a standard collar interface and a small reflection-odd trace `psi` are given. PF-145 does the analogous job for a small reflection-even radial graph `rho` and gives a sufficient additive upper bound for a coupled small trace. None of these findings proves that the **actual** prime/shift body traces are graphs in that regime or satisfy the required global `L^1` summability.

PF-128 remains a local optimized model for a matched standard collar; PF-139/PF-140 control the body/cusp comparison outside the unresolved closed-thin interfaces. No finding yet assembles all of these maps into one smooth complete global comparison. Even complete wave operators would not imply equality of scattering matrices, resonances, discrete eigenvalues, Selberg/Ruelle objects, relative determinants, or any RH statement.

The external theorem remains B. Güneysu and A. Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`; it supplies the sufficient weighted criterion, not the missing prime-flute assembly theorem.

## Research disposition

The clue remains `accepted`. PF-145 materially narrows it: both nonconstant angular and small radial interface modes now have a local `L^1` welding budget independent of core collapse. Continued work should stop searching for a generic collar-extension discount or derivative-norm shortcut and instead compute the **actual PF-142-normalized full trace** on a fixed interior collar interface, prove the small-graph regime, and decide the displayed `ell^1(L^1)` summability condition. Acceptance asserts only that this remaining global assembly question is mathematically well-posed and worth testing.