---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-339-wang-prime-source-chebyshev-theta-differential-image.md
  - research/visual_exploration/findings/VIS-340-wang-prime-squarelog-partial-summation-invertible.md
  - research/visual_exploration/findings/VIS-367-growing-depth-chebyshev-capacity-baseline.md
  - research/visual_exploration/findings/VIS-371-unitary-equivariant-gram-metrics-are-spectral.md
  - research/visual_exploration/findings/VIS-378-rational-orientation-is-controlled-by-intrinsic-free-derivative.md
  - research/visual_exploration/findings/VIS-379-gram-orbit-derivative-exact-orientation-condition.md
  - research/visual_exploration/findings/VIS-380-joint-commutator-gap-controls-bounded-orbit-amplification.md
  - research/visual_exploration/findings/VIS-381-bounded-output-orientation-requires-low-commutator-mode-alignment.md
  - research/visual_exploration/findings/VIS-382-defect-squared-low-mode-mass.md
  - research/visual_exploration/findings/VIS-383-source-coordinate-metric-controls-defect-squared-localization.md
  - research/visual_exploration/findings/VIS-384-hilbert-schmidt-source-subspace-laplacian.md
  - research/visual_exploration/findings/VIS-385-isotropic-source-subspace-null-defect-energy-moments.md
  - research/visual_exploration/findings/VIS-386-gram-tangent-scale-normalization.md
  - research/visual_exploration/findings/VIS-387-qubit-source-subspace-spectrum-collapses-to-defect-energy.md
  - research/visual_exploration/findings/VIS-388-qutrit-rank-one-source-spectrum-has-cubic-shape.md
  - research/visual_exploration/findings/VIS-389-qutrit-rank-one-shape-closes-at-second-moment.md
  - research/visual_exploration/findings/VIS-390-isotropic-qutrit-tangent-null-uniform-residual-second-moment.md
  - research/visual_exploration/findings/VIS-391-sector-anisotropic-qutrit-residual-null.md
  - research/visual_exploration/findings/VIS-392-source-stabilizer-gaussian-null-is-sector-scaled.md
  - research/visual_exploration/findings/VIS-393-source-stabilizer-symmetry-does-not-calibrate-qutrit-weights.md
  - research/visual_exploration/findings/VIS-394-replicated-gaussian-packet-normalized-gamma-control.md
  - research/visual_exploration/findings/VIS-395-unequal-replica-count-normalized-gamma-control.md
  - research/visual_exploration/findings/VIS-396-additive-common-gamma-packet-shock-control.md
  - research/visual_exploration/findings/VIS-397-unequal-rate-common-gamma-packet-control.md
  - research/visual_exploration/findings/VIS-398-finite-shared-gamma-network-calibration.md
  - research/visual_exploration/findings/VIS-399-fixed-budget-exclusive-gamma-packet-control.md
  - research/visual_exploration/findings/VIS-400-fixed-budget-exclusive-positive-amplitude-control.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder `G(u)=e^(-u)theta(e^u)-1`. The Wang chain through `VIS-371` and `VIS-378`--`VIS-386` removes Gram-only spectral filtering, expression-tree conditioning, unavailable similarity directions, generator-coordinate gauge, tangent-amplitude gauge, and the universal scalar defect-energy floor before any residual orientation is credited as source information.

`VIS-387`--`VIS-389` identify generic rank-one qutrits as the first nontrivial normalized spectral-shape test bed. After source cubic geometry and first moment `m_1` are fixed, the remaining positive spectral shape is one-dimensional, represented by the residual coordinate `u`. `VIS-390`--`VIS-392` calibrate the complete Gaussian source-stabilizer nuisance ladder; `VIS-393` shows that symmetry alone becomes vacuous beyond Gaussianity because every law on `u` is compatible with source-stabilizer invariance.

`VIS-394`--`VIS-398` then replace symmetry-only nulls with explicit source-free packet mechanisms. Independent replicated Gamma sectors, unequal counts/rates, one shared Gamma block, and arbitrary fixed finite additive Gamma incidence networks all yield exactly specified conditional residual laws when their nuisance parameters are fixed independently of the candidate residual.

`VIS-399` adds a qualitatively different source-free mechanism: a fixed total packet budget with mutually exclusive sector assignment. It produces exact negative cross-sector raw-energy covariance and a finite mixture of normalized-Gamma simplex laws, including exact face components when sectors are empty.

`VIS-400` shows that Gamma closure is not load-bearing for that exclusive-budget mechanism. For any independently specified positive absolutely continuous sector amplitude densities `h_i`, conditioning on the multinomial count vector gives independent sector-sum convolution densities `h_i^{*k_i}`. Normalizing those sums gives the exact component law

`g_k(w)=integral_0^infinity t^2 prod_i h_i^{*k_i}(t w_i) dt`,

with the analogous lower-dimensional formula on faces, while `Cov(Y_i,Y_j)=-N p_i p_j mu_i mu_j` remains unchanged. Thus complicated non-Gamma positive amplitude shapes or tails do not by themselves create an uncontrolled residual law inside the fixed-budget exclusive architecture.

The remaining channel is therefore a residual law exceptional relative to separately justified source-free mechanisms whose nuisance structure is frozen independently, together with a structural explanation and a destination-level payoff.

## Research question

Can an admissible Wang/source-packet construction produce a normalized positive-spectrum Gram spectral distribution for the intrinsic source-subspace commutator Laplacian `Delta_S` that is genuinely source-specific and survives a falsifiable, independently specified source-free control family, in a way that can still be propagated to a Wang destination after all scale and conditioning costs are charged?

After the current calibration ladder, is there a mechanistically restricted nonarithmetic control under which the qutrit residual remains exceptional, rather than merely reflecting packet multiplicity, sector scaling, finite shared shocks, fixed-budget exclusivity, or the choice of an arbitrary positive one-packet amplitude law?

## Why it may matter

The qutrit reduction now leaves a very small evidential target. Nonuniformity, skew, concentration, boundary mass, positive or negative cross-sector dependence, unequal rates/counts, and non-Gamma positive amplitude laws can all be produced by explicit source-free architectures with exact conditional calibration. Rejecting one convenient parametric null is therefore not source evidence.

A surviving anomaly would have to come from structure not already absorbed by these nuisance mechanisms and would still need to improve the Wang destination after metric scale, Gram-gap/cluster width, coefficient norm, normalization, rank-selection, and source-information costs are charged.

## Decisive test

Choose one explicit admissible source family, center it modulo the identity, form its Hilbert-Schmidt source subspace `S`, freeze the ambient coefficient-space Hilbert metric and numerical rank/tolerance rule, and construct `Delta_S=sum_a ad_(E_a)^*ad_(E_a)`. After removing `ker Delta_S`, compute the scale-invariant positive spectral distribution, source cubic invariant, first moment `m_1`, second moment `m_2`, and qutrit residual coordinate `u`.

Use only the source-free control justified by the mechanism. `VIS-390`--`VIS-392` cover Gaussian orientation/scale nuisance; `VIS-394`--`VIS-395` cover independent replicated-Gamma packet counts/rates; `VIS-396`--`VIS-398` cover fixed finite additive Gamma shock networks; `VIS-399` is the closed-form Gamma special case of fixed-budget exclusive allocation; `VIS-400` covers the same exclusive architecture with arbitrary independently specified positive absolutely continuous sector amplitude densities through convolution and radial integration. Do not select the architecture, packet budget, assignment probabilities, amplitude densities, rates, moments, or other nuisance freedom using the candidate residual being judged.

A genuinely stronger null must now change mechanism rather than merely replace Gamma by another positive amplitude family. Candidate extensions include signed or interfering latent contributions before energy formation, packet interactions that destroy conditional independence given counts, continuous/infinite latent structures with a nontrivial scaling law, or a Wang admissibility constraint that derives a narrower source-coupled law. Any such control must have a nondegenerate realizable sample space and a statistic/decision rule fixed before inspecting confirmation data.

Kill the route if the residual is reproduced by the matched controls, if significance disappears after admitting the independently justified control family, if the null acquires enough post-hoc freedom to fit an arbitrary `u` law, if the effect depends on tuned ranks/windows, or if the destination rule imports the target arithmetic estimate. A positive source-side residual remains insufficient unless its full cost propagates to the Wang destination without assuming a stronger bound for `G`, `theta`, or an equivalent unsmoothed source quantity.

## Evidence boundary

`VIS-378`--`VIS-386` establish the intrinsic source-subspace and normalization gates; `VIS-387`--`VIS-393` classify the minimal qutrit residual and the Gaussian/symmetry boundary; `VIS-394`--`VIS-398` calibrate independent and positively dependent finite Gamma packet mechanisms; `VIS-399` calibrates fixed-budget exclusive Gamma allocation with negative dependence; `VIS-400` removes Gamma as a load-bearing assumption for that exclusive architecture by giving the exact arbitrary-positive-density convolution/radial law.

None of these findings proves that an admissible Wang family has an anomalous residual relative to a properly restricted matched control, identifies an arithmetic cause for such an anomaly, or propagates one to a Wang gain. The current ladder still does not exhaust signed/interfering latent mechanisms, packet interactions, shared latent variables that survive count conditioning, infinite-budget scaling limits, arbitrary copulas, or Wang-admissibility constraints tied to arithmetic source data.

The clue remains `accepted`, but is narrowed again: changing only the positive packet-amplitude family no longer counts as a distinct escape from the fixed-budget exclusive null.

## Research disposition

Outcome: **narrowed**.

For the minimal qutrit route, use the weakest exact control justified by the source-free mechanism and freeze its nuisance structure independently of the candidate. In particular, `VIS-400` subsumes `VIS-399` for positive absolutely continuous amplitudes under fixed-budget exclusive assignment. The next stronger test must earn genuinely different dependence or source coupling—signed/interfering contributions, interactions, nontrivial infinite latent structure, Wang admissibility, or another independently justified mechanism—before any surviving residual is allowed to proceed to the destination-cost test.
