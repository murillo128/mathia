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
  - research/prime_flute/findings/PF-146-squared-short-collar-relative-resolvent-is-trace-class.md
---

# Do the prime flute and the all-composite shift clone have complete relative wave operators?

## Observation

PF-125 already places the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1` in the same compact-relative-resolvent and essential-spectrum class. There are now two distinct sufficient programs for upgrading that comparison to complete wave operators.

The first is geometric. Güneysu--Thalmaier's no-injectivity-radius criterion says that, after transporting one metric to the other, finiteness of the inverse-unit-ball weighted metric-deviation integral gives existence and completeness of the two-Hilbert-space wave operators and equality of the absolutely continuous spectra. Most local sectors of that integral are controlled. PF-128 shows that matched collapsing standard collars do not amplify the logarithmic core-length defect in the scattering weight. PF-139 supplies a boundary-coherent lower-pant comparison with summable strong-`L^1` body correction through the standard cusp entry, PF-140 closes the horocycle/cusp handoff at finite total wave weight, and PF-138 identifies the complete tail family of actual Margulis-short closed cores that still require collar insertion.

PF-142 removes the constant angular phase from those short-core interfaces by retaining the canonical zero-twist reflection marking. PF-143/PF-144 then identify the exact local cost of the surviving reflection-odd angular trace. If `psi_eta` is a small normalized angular mismatch, its optimal local near-isometric welding scale is

\[
\operatorname{Cost}_{\rm angular}(\eta)
\asymp
\|\psi_\eta\|_{L^1(\mathbb S^1)},
\]

with constants independent of the collapsing core length. PF-145 closes the analogous local norm-selection problem for transverse/radial interface shape: a small reflection-even radial graph `rho_eta` has sharp radial-only weighted welding cost

\[
\operatorname{Cost}_{\rm radial}(\eta)
\asymp
\|\rho_\eta\|_{L^1(\mathbb S^1)},
\]

and a small reflection-equivariant full trace `(rho_eta,psi_eta)` admits a simultaneous local correction of cost

\[
O\!\left(\|\rho_\eta\|_1+\|\psi_\eta\|_1\right).
\]

Thus the unresolved geometric interface is the actual trace sequence produced by one globally coherent prime/shift body comparison, not the existence of a suitable local extension norm.

PF-146 adds a second, operator-theoretic route. PF-112's local obstruction excludes trace class for the **first** relative resolvent of genuinely different two-dimensional metrics, but PF-146 proves that on every fixed central matched short collar the **squared** resolvent difference is trace class:

\[
\bigl\|(\Delta_{L_+}^D+1)^{-2}-(\Delta_L^D+1)^{-2}\bigr\|_{\mathcal S_1}
\le C_R P^{-3}L^3
\]

for the matched prime/shift separator. The surviving zero transverse mode cancels exactly, and the nonzero modes gain enough extra smoothing to cross the trace endpoint. Classical Kato--Rosenblum plus the Birman--Kato invariance principle then make the global condition

\[
(\Delta_{X_+}+1)^{-2}-(\Delta_X+1)^{-2}\in\mathcal S_1
\]

a sufficient alternative route to complete wave operators after one fixed admissible Hilbert-space identification. PF-146 does not establish that global trace-class statement; it only removes the true central short-collar block as an obstruction to it.

## Research question

Do the exact prime flute and the all-composite shift clone admit a natural globally coherent comparison for which **either** of the following sufficient scattering gates can be proved?

**Geometric gate.** Can the PF-139/PF-140 body-and-cusp comparison be modified around the complete PF-138 family of short closed cores so that one smooth complete globally marked comparison satisfies

\[
\int_X
\mu_g(B_g(x,1))^{-1}
\delta_{g,h}(x)\,d\mu_g(x)<\infty,
\]

and hence the relative wave operators

\[
W_\pm(\Delta_{X_+},\Delta_X,I)
\]

exist and are complete? After PF-143--PF-145 the short-collar gate is to put the actual body image on one fixed interior collar interface into the reflection-equivariant small-graph form

\[
\Gamma_\eta(\theta)
=\bigl(1+\rho_\eta(\theta),
\theta+\psi_\eta(\theta)\bigr),
\]

with `rho_eta` even and `psi_eta` odd, and prove

\[
\sum_\eta
\left(
\|\rho_\eta\|_{L^1}
+
\|\psi_\eta\|_{L^1}
\right)<\infty.
\]

**Operator gate.** Under one fixed natural/unitary identification of the two Laplacians, can the global uncut surface satisfy

\[
\boxed{
(\Delta_{X_+}+1)^{-2}-(\Delta_X+1)^{-2}
\in\mathcal S_1?
}
\]

PF-146 shows that the actual central pinching collars contribute trace-class local blocks with a strong `O(P^{-3}L^3)` suppression. The unresolved terms are the thick body, collar/body transmission and localization commutators, and the infinite sum under one coherent global identification.

A decisive negative answer would show that both sufficient routes fail for an intrinsic reason: either the actual canonical trace mass necessarily diverges for every admissible geometric assembly, or the uncut squared-resolvent difference has a non-trace-class body/interface/global component despite the local collar suppression, or a stronger spectral obstruction rules out complete wave operators directly.

## Why it may matter

A positive answer through either route would show that the exact prime flute and an exact all-composite control have the same absolutely continuous Laplace spectral class under a natural comparison. Together with PF-125, this would rule out both the essential spectrum and the absolutely continuous wave/scattering class as primality selectors for this construction; any RH-relevant mechanism would have to live in finer discrete, resonant, determinant, scattering-matrix, or genuinely arithmetic data not fixed by those equivalences.

The two routes also separate two potential sources of difficulty. Failure of the Güneysu--Thalmaier metric integral need not imply failure of wave equivalence if the resolvent-power trace-class gate survives, while failure of the operator gate would be meaningful only if it comes from an actual uncut body/interface/global mechanism rather than PF-112's already-understood first-resolvent endpoint.

## Decisive test

For the geometric route, a positive resolution must construct one smooth complete comparison rather than sum incompatible local models. It must start from the PF-139/PF-140 global body/cusp map, use PF-138 to isolate every tail short core, retain the PF-142 reflection anchors, choose a fixed interior collar cross-section in the uniformly thick outer slab, and compute the induced normalized traces `(rho_eta,psi_eta)`. It must prove their `C^1` size tends to zero and their total `L^1` mass is summable. PF-144/PF-145 can then supply the local collar welding at exactly an additive `L^1` budget. The proof must control all interpolation and smoothing zones in the same inverse-unit-ball weighted norm, verify global quasi-isometry and completeness, and only then invoke Güneysu--Thalmaier.

For the operator route, use one fixed global identification and a localization/resolvent decomposition adapted to the PF-138 collars and the complementary body. Insert PF-146 for each fixed-central collar block, then estimate every cutoff commutator and transmission term in Schatten ideals strong enough that the full squared-resolvent difference is in `S_1`. The decisive issue is not local pseudodifferential order alone but whether the tail trace norms are summable with constants uniform through the zero-injectivity-radius geometry. If the direct sum/localized estimates cannot be reassembled, exhibit the precise non-trace-class singular-value mechanism in the uncut operator rather than inferring failure from the first-resolvent obstruction.

A decisive negative resolution should prove either unavoidable divergence in the actual geometric trace amplitudes, unavoidable non-`S_1` mass in the global squared-resolvent comparison, or direct failure of wave completeness. Divergence produced only by a non-optimized interpolation, by summing trace derivatives when PF-144/PF-145 show that this derivative ledger is unnecessary, by reintroducing a constant phase that PF-142 removes, or by citing PF-112 for the wrong resolvent power is not decisive.

## Evidence boundary

This clue remains a research question, not evidence for wave-operator existence. PF-143/PF-144 characterize the local angular cost once a standard collar interface and a small reflection-odd trace `psi` are given. PF-145 does the analogous job for a small reflection-even radial graph `rho` and gives a sufficient additive upper bound for a coupled small trace. None of these findings proves that the actual prime/shift body traces are graphs in that regime or satisfy the required global `L^1` summability.

PF-146 likewise proves only a fixed-central Dirichlet-collar trace-class estimate for the **squared** relative resolvent. It does not control the uncut collar/body transmission problem, a growing full collar, the thick-body contribution, or the infinite global sum, and it does not prove the displayed global `S_1` condition. PF-112 still rules out trace class of the first localized relative resolvent whenever the metrics genuinely differ.

PF-128 remains a local optimized model for a matched standard collar; PF-139/PF-140 control the body/cusp comparison outside the unresolved closed-thin interfaces. No finding yet assembles either sufficient route into a proof of complete relative wave operators. Even complete wave operators would not imply equality of scattering matrices, resonances, discrete eigenvalues, Selberg/Ruelle objects, relative determinants, or any RH statement.

The external sufficient theorems are Güneysu--Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, for the weighted geometric route, and the classical Kato/Birman invariance principle anchored in Kato, *Wave operators and unitary equivalence*, Pacific J. Math. 15 (1965), 171--180, DOI `10.2140/pjm.1965.15.171`, for the resolvent-power route. Neither theorem supplies the missing prime-flute global assembly.

## Research disposition

The clue remains `accepted`. PF-145 leaves a precise **geometric** gate: compute the actual PF-142-normalized full trace on a fixed interior collar interface, prove the small-graph regime, and decide the displayed `ell^1(L^1)` summability condition. PF-146 adds a parallel **operator** gate: decide whether a global localization/transmission argument promotes the fixed-central-collar `S_1` squared-resolvent estimate to

\[
(\Delta_{X_+}+1)^{-2}-(\Delta_X+1)^{-2}\in\mathcal S_1.
\]

Either route would suffice for complete wave operators; neither is currently established. Acceptance asserts only that these two concrete global tests are mathematically well-posed and worth active investigation.