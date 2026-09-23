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
  - research/visual_exploration/findings/VIS-402-finite-additive-cross-sector-signed-factor-control.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder `G(u)=e^(-u)theta(e^u)-1`. The Wang chain through `VIS-371` and `VIS-378`--`VIS-386` removes Gram-only spectral filtering, expression-tree conditioning, unavailable similarity directions, generator-coordinate gauge, tangent-amplitude gauge, and the universal scalar defect-energy floor before any residual orientation is credited as source information.

`VIS-388`--`VIS-389` reduce the first nontrivial generic rank-one qutrit case to one residual shape scalar `u` after source cubic geometry and first moment `m_1` are fixed. `VIS-390`--`VIS-392` calibrate the Gaussian source-stabilizer nuisance ladder; `VIS-393` shows that symmetry alone is vacuous beyond Gaussianity because every law on `u` is source-stabilizer compatible.

The later packet controls progressively replace symmetry by explicit source-free mechanisms. `VIS-394`--`VIS-398` calibrate independent replicated Gamma sectors, unequal counts/rates, and arbitrary fixed finite additive shared-Gamma incidence networks. `VIS-399` adds fixed-budget exclusive allocation and its negative dependence. `VIS-400` removes Gamma as a load-bearing assumption: arbitrary independently specified positive packet-amplitude laws remain exactly calibratable through convolution and radial normalization. `VIS-401` closes sector-local signed coherent cancellation.

`VIS-402` now closes the broad elementary cross-sector common-factor escape. If several signed sector amplitudes share a fixed finite-dimensional additive latent `L`, but are conditionally independent after `L` is exposed, then squaring each sector and normalizing gives the exact mixture

`g(w)=integral R(dl) integral_0^infinity t^2 prod_i h_i(t w_i|l) dt`.

The fixed-`m_1` qutrit residual is therefore still exactly calibrated once the latent law, loadings and idiosyncratic laws are fixed independently. In the centered scalar-factor specialization, raw sector-energy covariance is necessarily nonnegative: `Cov(Y_i,Y_j)=c_i^2 c_j^2 Var(L^2)`.

The remaining channel is consequently not merely "cross-sector dependence" or "a shared signed latent". It must use a source-derived admissibility restriction or dependence that does not reduce to conditionally independent sector amplitudes given an independently specified finite latent state, and it must still survive the full destination-cost test.

## Research question

Can an admissible Wang/source-packet construction produce a normalized positive-spectrum distribution for the intrinsic source-subspace commutator Laplacian `Delta_S` whose qutrit residual is genuinely source-specific relative to an independently specified, mechanistically justified source-free control, and can that surviving direction still yield a Wang destination gain after all scale and conditioning costs are charged?

After `VIS-402`, a useful escape should involve structure such as a Wang admissibility theorem that restricts the latent law/loadings from arithmetic source data, packet interactions that remain dependent after conditioning on every admitted finite latent state, cross-sector phase dynamics outside the additive real-factor model, or a nontrivial infinite/continuum scaling mechanism. Merely adding finite common factors to otherwise independent sector amplitudes is no longer enough.

## Why it may matter

The qutrit reduction leaves a deliberately small evidential target. Nonuniformity, skew, concentration, boundary mass, positive or negative dependence, unequal counts/rates, non-Gamma amplitudes, sector-local signed cancellation, and finite additive common-factor coherence can all arise from explicit source-free architectures with exact calibration when their nuisance structure is frozen independently.

A surviving anomaly would therefore carry more information than rejection of a convenient parametric or independence null. It would still not be sufficient by itself: the mechanism must propagate through the Wang map after metric scale, Gram-gap/cluster width, coefficient norm, normalization, rank-selection, and source-information costs are charged.

## Decisive test

Choose one explicit admissible source family, center it modulo the identity, form its Hilbert-Schmidt source subspace `S`, freeze the ambient coefficient-space Hilbert metric and numerical rank/tolerance rule, and construct `Delta_S=sum_a ad_(E_a)^*ad_(E_a)`. After removing `ker Delta_S`, compute the scale-invariant positive spectral distribution, source cubic invariant, first moment `m_1`, second moment `m_2`, and qutrit residual coordinate `u`.

Use only a source-free control justified independently by the packet mechanism. Existing exact controls already cover Gaussian orientation/scale nuisance (`VIS-390`--`VIS-392`), finite additive Gamma packet/shock architectures (`VIS-394`--`VIS-398`), fixed-budget exclusive positive amplitudes (`VIS-399`--`VIS-400`), fixed-budget exclusive sector-local signed coherent sums (`VIS-401`), and finite additive common signed factors with conditionally independent idiosyncratic sector amplitudes (`VIS-402`). Do not choose architecture, latent dimension, latent law, loadings, packet budget, assignment probabilities, amplitude laws, phases, rates, moments, or other nuisance freedom by inspecting the candidate residual.

The next useful test must therefore earn a structural restriction rather than another generic nuisance extension. One sharp route is to derive from Wang admissibility an independently fixed constraint on a coupled latent/interaction law and then ask whether the actual source residual violates the resulting normalized-weight family. Another is an interaction whose sector amplitudes remain dependent even after conditioning on the admitted finite latent state. Kill the route if the proposed null becomes flexible enough to represent arbitrary `u` laws, if its nuisance structure is fitted post hoc, or if the surviving residual disappears once the independently justified coupled control is admitted.

For any surviving source-side anomaly, freeze the statistic and decision rule before confirmation data and then propagate the full effect to the Wang destination. Kill the route if the destination argument imports the target arithmetic estimate, if the effect disappears after admitted nuisance calibration, or if tuned ranks/windows are required.

## Evidence boundary

`VIS-378`--`VIS-386` establish the intrinsic source-subspace and normalization gates; `VIS-388`--`VIS-393` classify the minimal qutrit residual and Gaussian/symmetry boundary; `VIS-394`--`VIS-398` calibrate independent and positively dependent finite Gamma packet mechanisms; `VIS-399`--`VIS-400` calibrate fixed-budget exclusive allocation with arbitrary independently specified positive amplitudes; `VIS-401` calibrates sector-local signed coherent cancellation; `VIS-402` calibrates finite additive common-factor cross-sector coherence whenever conditioning on the independently specified latent restores sector independence.

None of these findings proves that an admissible Wang family has an anomalous residual relative to a properly restricted matched control, identifies an arithmetic cause for such an anomaly, or propagates one to a Wang gain. They do not exhaust genuinely interacting sector dynamics, source-derived latent restrictions, infinite/continuum latent limits, or Wang-admissibility constraints tied to arithmetic source data.

## Research disposition

Outcome: **narrowed**.

The clue remains `accepted`. The nuisance frontier has moved past finite additive common-factor coherence. The next coherent test must derive a non-vacuous source-coupled restriction or a genuinely non-conditionally-independent interaction before any residual exception is credited as source information.
