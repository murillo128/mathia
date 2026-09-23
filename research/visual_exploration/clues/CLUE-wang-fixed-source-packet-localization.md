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
  - research/visual_exploration/findings/VIS-403-unrestricted-finite-latent-conditional-independence-vacuous.md
  - research/visual_exploration/findings/VIS-404-fixed-uniform-latent-monotone-decoder-universal.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder `G(u)=e^(-u)theta(e^u)-1`. The Wang chain through `VIS-371` and `VIS-378`--`VIS-386` removes Gram-only spectral filtering, expression-tree conditioning, unavailable similarity directions, generator-coordinate gauge, tangent-amplitude gauge, and the universal scalar defect-energy floor before any residual orientation is credited as source information.

`VIS-388`--`VIS-389` reduce the first nontrivial generic rank-one qutrit case to one residual shape scalar `u` after source cubic geometry and first moment `m_1` are fixed. `VIS-390`--`VIS-392` calibrate the Gaussian source-stabilizer nuisance ladder; `VIS-393` shows that symmetry alone is vacuous beyond Gaussianity because every law on `u` is source-stabilizer compatible.

The later packet controls progressively replace symmetry by explicit source-free mechanisms. `VIS-394`--`VIS-398` calibrate independent replicated Gamma sectors, unequal counts/rates, and arbitrary fixed finite additive shared-Gamma incidence networks. `VIS-399` adds fixed-budget exclusive allocation and its negative dependence. `VIS-400` removes Gamma as a load-bearing assumption: arbitrary independently specified positive packet-amplitude laws remain exactly calibratable through convolution and radial normalization. `VIS-401` closes sector-local signed coherent cancellation.

`VIS-402` closes the broad elementary cross-sector common-factor escape. If several signed sector amplitudes share a fixed finite-dimensional additive latent `L`, but are conditionally independent after `L` is exposed, then squaring each sector and normalizing gives the exact mixture

`g(w)=integral R(dl) integral_0^infinity t^2 prod_i h_i(t w_i|l) dt`.

The fixed-`m_1` qutrit residual is therefore still exactly calibrated once the latent law, loadings and idiosyncratic laws are fixed independently. In the centered scalar-factor specialization, raw sector-energy covariance is necessarily nonnegative: `Cov(Y_i,Y_j)=c_i^2 c_j^2 Var(L^2)`.

`VIS-403` removes a misleading representation-level escape. The statement “dependence survives every finite latent state” has no intrinsic content unless the admissible latent family is independently restricted. On the fixed-`m_1` qutrit slice, one scalar latent `L=u` with deterministic conditional sector amplitudes can reproduce any Borel law of the residual while making the sectors conditionally independent. More generally, conditioning on the full finite sector vector always makes its coordinates conditionally independent in the degenerate sense.

`VIS-404` closes the immediate repair “fix the latent prior”. A single pre-fixed `U~Uniform(0,1)` plus the generalized quantile decoder `Q_nu` reproduces any Borel target residual law `nu`, and `Q_nu` is monotone. For positive continuous target densities the same transport can even be `C^1` and bi-Lipschitz, with target-dependent derivative bounds. Fixing the latent distribution, monotonicity, or qualitative smoothness therefore remains non-diagnostic while decoder capacity is allowed to absorb the target.

The remaining channel is consequently not “choose a canonical latent and a regular decoder”. It must earn a **pre-specified, falsifiable restriction on the joint latent-to-residual mechanism** from a source-free packet construction or Wang admissibility, with quantitative/structural capacity fixed independently of the candidate residual.

## Research question

Can an admissible Wang/source-packet construction produce a normalized positive-spectrum distribution for the intrinsic source-subspace commutator Laplacian `Delta_S` whose qutrit residual is genuinely source-specific relative to an independently specified, mechanistically justified source-free control, and can that surviving direction still yield a Wang destination gain after all scale and conditioning costs are charged?

After `VIS-403`--`VIS-404`, the decisive issue is **joint model restriction, not latent representation**. A useful escape should derive before seeing the candidate a non-vacuous family of allowed latent states and decoders/loadings, interaction kernels, phase relations, support/moment constraints, or continuum limits whose induced residual family has a falsifiable boundary. A standard latent prior and qualitative monotonicity/smoothness are not such a boundary when their decoder or numerical regularity constants can be selected from the target.

## Why it may matter

The qutrit reduction leaves a deliberately small evidential target. Nonuniformity, skew, concentration, boundary mass, positive or negative dependence, unequal counts/rates, non-Gamma amplitudes, sector-local signed cancellation, finite additive common-factor coherence, abstract finite-latent conditional independence, and even a fixed scalar latent prior with arbitrary monotone transport can all be source-free or representation-vacuous when their nuisance structure is not independently restricted.

A surviving anomaly would therefore carry more information than rejection of a convenient parametric or independence null. It would still not be sufficient by itself: the mechanism must also propagate through the Wang map after metric scale, Gram-gap/cluster width, coefficient norm, normalization, rank-selection, and source-information costs are charged.

## Decisive test

Choose one explicit admissible source family, center it modulo the identity, form its Hilbert-Schmidt source subspace `S`, freeze the ambient coefficient-space Hilbert metric and numerical rank/tolerance rule, and construct `Delta_S=sum_a ad_(E_a)^*ad_(E_a)`. After removing `ker Delta_S`, compute the scale-invariant positive spectral distribution, source cubic invariant, first moment `m_1`, second moment `m_2`, and qutrit residual coordinate `u`.

Use only a source-free control justified independently by the packet mechanism. Existing exact controls already cover Gaussian orientation/scale nuisance (`VIS-390`--`VIS-392`), finite additive Gamma packet/shock architectures (`VIS-394`--`VIS-398`), fixed-budget exclusive positive amplitudes (`VIS-399`--`VIS-400`), fixed-budget exclusive sector-local signed coherent sums (`VIS-401`), and finite additive common signed factors with conditionally independent idiosyncratic sector amplitudes (`VIS-402`). `VIS-403` adds a representation gate: do not count conditional independence given some finite latent as a restriction unless the allowed latent law and decoder/interaction family were fixed independently and exclude the trivial `L=u`/`L=S` encoding. `VIS-404` strengthens that gate: fixing the scalar latent law to `Uniform(0,1)` still excludes nothing if an arbitrary monotone quantile decoder remains available.

The next useful test must therefore derive the admissible nuisance family **jointly**. Starting from Wang/source-packet mathematics rather than from the observed residual, predeclare the latent law when relevant, the decoder/interaction family, and any numerical capacity bounds independently of the target. Obtain at least one testable consequence: an inequality, support exclusion, moment/cumulant relation, conditional phase constraint, fixed degree/basis or coefficient budget, fixed Lipschitz/variation bound, restricted copula, scaling law, or another invariant that excludes some residual laws. Then compare the actual source residual only against that frozen family.

Kill the route if the proposed control can realize arbitrary laws on `u`; if latent, decoder, basis, degree, coefficient, regularity or interaction capacity is enlarged after seeing the candidate; if a fixed latent prior merely pushes arbitrary target dependence into a quantile/transport decoder; if the supposed restriction disappears under an equivalent reparameterization; or if the surviving source-side effect vanishes once the independently justified restricted control is admitted.

For any surviving source-side anomaly, freeze the statistic and decision rule before confirmation data and then propagate the full effect to the Wang destination. Kill the route if the destination argument imports the target arithmetic estimate, if the effect disappears after admitted nuisance calibration, or if tuned ranks/windows are required.

## Evidence boundary

`VIS-378`--`VIS-386` establish the intrinsic source-subspace and normalization gates; `VIS-388`--`VIS-393` classify the minimal qutrit residual and Gaussian/symmetry boundary; `VIS-394`--`VIS-398` calibrate independent and positively dependent finite Gamma packet mechanisms; `VIS-399`--`VIS-400` calibrate fixed-budget exclusive allocation with arbitrary independently specified positive amplitudes; `VIS-401` calibrates sector-local signed coherent cancellation; `VIS-402` calibrates finite additive common-factor cross-sector coherence whenever conditioning on the independently specified latent restores sector independence.

`VIS-403` does not say that every restricted smooth/noisy latent model is universal or that latent models are invalid controls. It shows that finite-latent conditional independence by itself is non-identifying. `VIS-404` does not show that one fixed smoothness budget or a Wang-derived decoder family is universal; it shows that a fixed standard latent and merely qualitative monotonicity/regularity still leave arbitrary residual freedom when the decoder is target-dependent.

None of these findings proves that an admissible Wang family has an anomalous residual relative to a properly restricted matched control, identifies an arithmetic cause for such an anomaly, derives the required joint Wang admissibility restriction, or propagates one to a destination gain.

## Research disposition

Outcome: **narrowed**.

The clue remains `accepted`. The nuisance frontier has moved past generic finite-latent language and fixed-prior monotone-transport repairs. The next coherent test must derive a pre-candidate Wang/source-packet family with decoder/interaction capacity quantitatively or structurally bounded independently of the residual, then test a consequence that excludes at least some residual laws.
