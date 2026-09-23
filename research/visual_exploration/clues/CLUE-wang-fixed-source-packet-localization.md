---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-339-wang-prime-source-chebyshev-theta-differential-image.md
  - research/visual_exploration/findings/VIS-371-unitary-equivariant-gram-metrics-are-spectral.md
  - research/visual_exploration/findings/VIS-378-rational-orientation-is-controlled-by-intrinsic-free-derivative.md
  - research/visual_exploration/findings/VIS-384-hilbert-schmidt-source-subspace-laplacian.md
  - research/visual_exploration/findings/VIS-386-gram-tangent-scale-normalization.md
  - research/visual_exploration/findings/VIS-388-qutrit-rank-one-source-spectrum-has-cubic-shape.md
  - research/visual_exploration/findings/VIS-389-qutrit-rank-one-shape-closes-at-second-moment.md
  - research/visual_exploration/findings/VIS-390-isotropic-qutrit-tangent-null-uniform-residual-second-moment.md
  - research/visual_exploration/findings/VIS-392-source-stabilizer-gaussian-null-is-sector-scaled.md
  - research/visual_exploration/findings/VIS-393-source-stabilizer-symmetry-does-not-calibrate-qutrit-weights.md
  - research/visual_exploration/findings/VIS-398-finite-shared-gamma-network-calibration.md
  - research/visual_exploration/findings/VIS-399-fixed-budget-exclusive-gamma-packet-control.md
  - research/visual_exploration/findings/VIS-400-fixed-budget-exclusive-positive-amplitude-control.md
  - research/visual_exploration/findings/VIS-401-sector-local-signed-packet-interference-control.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder `G(u)=e^(-u)theta(e^u)-1`. The Wang chain through `VIS-371` and `VIS-378`--`VIS-386` removes Gram-only spectral filtering, expression-tree conditioning, unavailable similarity directions, generator-coordinate gauge, tangent-amplitude gauge, and the universal scalar defect-energy floor before any residual orientation is credited as source information.

`VIS-388`--`VIS-389` reduce the first nontrivial generic rank-one qutrit case to one residual shape scalar `u` after source cubic geometry and first moment `m_1` are fixed. `VIS-390`--`VIS-392` calibrate the Gaussian source-stabilizer nuisance ladder; `VIS-393` shows that symmetry alone is vacuous beyond Gaussianity because every law on `u` is source-stabilizer compatible.

The later packet controls progressively replace symmetry by explicit source-free mechanisms. `VIS-394`--`VIS-398` calibrate independent replicated Gamma sectors, unequal counts/rates, and arbitrary fixed finite additive shared-Gamma incidence networks. `VIS-399` adds fixed-budget exclusive allocation and its negative dependence. `VIS-400` removes Gamma as a load-bearing assumption: arbitrary independently specified positive packet-amplitude laws remain exactly calibratable through convolution and radial normalization.

`VIS-401` now closes the simplest signed/interference escape as well. If exclusively assigned packets carry arbitrary independently specified **signed** sector-local amplitudes, the coherent sector sums have convolution densities, squaring maps them to explicit positive sector-energy densities, and conditional independence across sectors survives. The normalized simplex law and fixed-`m_1` qutrit residual are therefore still exactly calibrated by the same radial construction. For centered signed packets, the raw cross-sector energy covariance remains exactly negative, `-N p_i p_j nu_i nu_j`.

The remaining channel is consequently not "non-Gamma", "signed", or "interfering" in the local sense. It must use a genuinely different dependence architecture or a source-derived admissibility restriction and then survive the full destination-cost test.

## Research question

Can an admissible Wang/source-packet construction produce a normalized positive-spectrum distribution for the intrinsic source-subspace commutator Laplacian `Delta_S` whose qutrit residual is genuinely source-specific relative to an independently specified, mechanistically justified source-free control, and can that surviving direction still yield a Wang destination gain after all scale and conditioning costs are charged?

After the current calibration ladder, the live escape should involve structure such as a signed latent amplitude shared coherently across sectors before squaring, cross-sector phase locking, packet interactions that destroy conditional independence given counts, a nontrivial infinite/continuum scaling mechanism, or a Wang admissibility constraint that derives a narrower source-coupled law. Merely changing local amplitude signs, tails, packet counts, rates, or finite additive shock architecture is no longer enough.

## Why it may matter

The qutrit reduction leaves a deliberately small evidential target. Nonuniformity, skew, concentration, boundary mass, positive or negative cross-sector dependence, unequal rates/counts, non-Gamma positive amplitudes, and within-sector signed coherent cancellation can all be manufactured by explicit source-free architectures with exact conditional calibration.

A surviving anomaly would therefore carry more information than rejection of a convenient parametric null. It would still not be sufficient by itself: the mechanism must also propagate through the Wang map after metric scale, Gram-gap/cluster width, coefficient norm, normalization, rank-selection, and source-information costs are charged.

## Decisive test

Choose one explicit admissible source family, center it modulo the identity, form its Hilbert-Schmidt source subspace `S`, freeze the ambient coefficient-space Hilbert metric and numerical rank/tolerance rule, and construct `Delta_S=sum_a ad_(E_a)^*ad_(E_a)`. After removing `ker Delta_S`, compute the scale-invariant positive spectral distribution, source cubic invariant, first moment `m_1`, second moment `m_2`, and qutrit residual coordinate `u`.

Use only a source-free control justified independently by the packet mechanism. Existing exact controls already cover Gaussian orientation/scale nuisance (`VIS-390`--`VIS-392`), finite additive Gamma packet/shock architectures (`VIS-394`--`VIS-398`), fixed-budget exclusive positive amplitudes (`VIS-399`--`VIS-400`), and fixed-budget exclusive **sector-local signed coherent sums** (`VIS-401`). Do not choose architecture, packet budget, assignment probabilities, amplitude laws, phases, rates, moments, or other nuisance freedom by inspecting the candidate residual.

The next useful control must change dependence structure. A particularly sharp next case is a **shared signed latent entering two or more sectors before squaring**, because conditional independence of the positive sector energies then fails even after packet counts are fixed. Derive its realizable normalized-weight law or a nontrivial invariant/inequality before comparing it with the Wang residual. Kill that extension if it again reduces to an exactly calibratable generic nuisance family, becomes flexible enough to realize arbitrary `u` laws, or requires parameters fitted to the candidate.

For any surviving source-side anomaly, freeze the statistic and decision rule before confirmation data and then propagate the full effect to the Wang destination. Kill the route if the destination argument imports the target arithmetic estimate, if the effect disappears after admitted nuisance calibration, or if tuned ranks/windows are required.

## Evidence boundary

`VIS-378`--`VIS-386` establish the intrinsic source-subspace and normalization gates; `VIS-388`--`VIS-393` classify the minimal qutrit residual and Gaussian/symmetry boundary; `VIS-394`--`VIS-398` calibrate independent and positively dependent finite Gamma packet mechanisms; `VIS-399`--`VIS-400` calibrate fixed-budget exclusive allocation with arbitrary independently specified positive amplitudes; `VIS-401` shows that signed coherent cancellation confined to each independently allocated sector is still exactly calibratable after squaring.

None of these findings proves that an admissible Wang family has an anomalous residual relative to a properly restricted matched control, identifies an arithmetic cause for such an anomaly, or propagates one to a Wang gain. The current ladder does not exhaust cross-sector coherent signed latents, phase-coupled packet interactions, infinite/continuum latent limits, arbitrary copulas, or Wang-admissibility constraints tied to arithmetic source data.

## Research disposition

Outcome: **narrowed**.

The clue remains `accepted`. For the minimal qutrit route, sector-local signed interference is now part of the calibrated nuisance family rather than a distinct escape. The next coherent test should earn genuinely cross-sector coherence/interaction or source-derived admissibility before any residual exception is credited as source information.
