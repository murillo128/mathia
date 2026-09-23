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
  - research/visual_exploration/findings/VIS-405-fixed-lipschitz-quantile-budget-has-uniform-mass-floor.md
  - research/visual_exploration/findings/VIS-406-fixed-decoder-complexity-forces-uniform-mass.md
  - research/visual_exploration/findings/VIS-407-qutrit-source-invariant-chart-is-boundary-singular.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already been reduced to the normalized Chebyshev-theta remainder `G(u)=e^(-u)theta(e^u)-1`, while `VIS-371` and `VIS-378`--`VIS-386` remove Gram-only spectral filtering, unavailable similarity directions, coordinate gauge, tangent-amplitude gauge, and the universal scalar defect-energy floor before any residual orientation is credited as source information.

In the minimal generic rank-one qutrit test bed, `VIS-388`--`VIS-390` reduce the remaining normalized tangent spectral shape to one residual scalar `u` after source cubic geometry and first moment are fixed. `VIS-393` then shows that source-stabilizer symmetry alone places no law on that residual: every Borel law on `u` can be realized by a source-stabilizer-invariant tangent law. The packet-control chain through `VIS-394`--`VIS-402` further calibrates broad independent, exclusive-budget, signed, and finite additive common-factor source-free mechanisms.

`VIS-403`--`VIS-404` close the representation-level escape in which unrestricted finite latent variables or a fixed uniform latent with target-dependent monotone transport are presented as meaningful restrictions. `VIS-405` identifies the first exact quantitative boundary: a pre-fixed monotone `L`-Lipschitz decoder forces the residual target law to contain the uniform component `L^(-1)Leb_I`. `VIS-406` converts ordinary frozen representation budgets into such a mass floor: fixed basis/coefficient budgets and fixed polynomial degree give explicit target-independent Lipschitz bounds.

`VIS-407` now removes **source conjugacy/support geometry itself** as the missing justification for that budget in the rank-one qutrit test bed. The normalized source quotient has a regular Hilbert-Schmidt arc-length coordinate `theta`, while the complete algebraic invariant `x=tr(E^3)^2=(1/6)cos^2(3theta)` is boundary-singular: root gaps split like `sqrt(x)` or `sqrt(1/6-x)` at the two repeated-root boundaries. A Lipschitz/derivative budget measured only in `x` is therefore coordinate-dependent and cannot be credited as intrinsic source complexity. Together with the arbitrary-law symmetry result of `VIS-393`, this localizes the remaining restriction to **mechanism-specific source--tangent/source--response coupling**, not source conjugacy data by themselves.

## Research question

Can an admissible Wang/source-packet construction derive, before inspecting the candidate residual, a genuinely target-independent family of allowed source-to-response maps whose complexity is fixed by packet resources or another intrinsic operational constraint, and does the resulting qutrit residual then violate the corresponding exact source-free null while surviving full Wang destination-cost propagation?

After `VIS-405`--`VIS-407`, a useful restriction must be more than a chosen latent prior, qualitative smoothness, an arbitrary scalar invariant chart, or a post-hoc finite representation. It should arise from the actual packet/source mechanism: for example a fixed response basis with independently bounded coefficients, a source--tangent differential estimate in an intrinsic metric, a finite incidence/interaction architecture, a phase/support constraint, or another source-derived admissibility condition that excludes some residual laws before the target is seen.

## Why it may matter

The current qutrit branch has deliberately eliminated increasingly flexible ways to manufacture a residual anomaly. The generic approximation-theory part is now understood: once a real complexity budget exists, it can be translated into a falsifiable observable null. The unresolved scientific content is whether Wang/source-packet mathematics supplies that budget rather than merely giving a language in which one can fit it.

A surviving anomaly would therefore carry substantially more information than rejection of a convenient parametric control. Conversely, failure to derive any mechanism-specific restriction after the source-conjugacy and stabilizer-symmetry routes have been removed would close the decoder-capacity branch without confusing coordinate regularity or representational convenience with arithmetic information.

## Decisive test

Choose one explicit admissible Wang/source family, center it modulo the identity, form its Hilbert-Schmidt source subspace `S`, and construct the intrinsic commutator Laplacian `Delta_S=sum_a ad_(E_a)^*ad_(E_a)` with the ambient coefficient-space metric and numerical rank/tolerance rule frozen independently. In the generic rank-one qutrit reduction, condition on the source invariant/support and scalar defect rate and use the residual coordinate `u` from `VIS-389`--`VIS-390`.

Before examining the candidate residual distribution, derive the admissible source-to-response/decoder family from the packet mechanism itself. State the operational input metric or coordinate and justify it. If the restriction is a basis/coefficient, degree, variation, or Lipschitz budget, convert it through `VIS-405`--`VIS-406` into its observable mass/support/moment consequence. A bound expressed in `x=tr(E^3)^2` must additionally survive the `VIS-407` coordinate check or be justified by an independent mechanism that makes `x` the actual operational metric.

Kill the route if the admitted family can still realize arbitrary laws on `u`; if latent, basis, degree, coefficient, metric, or regularity capacity is chosen after seeing the target; if the only finite bound comes from the singular `t^2` chart rather than intrinsic packet geometry; if an equivalent source reparameterization removes the claimed complexity; or if the apparent anomaly disappears under the independently justified restricted control.

For any surviving source-side anomaly, freeze the statistic and decision rule before confirmation data and propagate the complete effect through the Wang destination, charging metric scale, Gram-gap/cluster width, coefficient norm, normalization, rank-selection, and source-information costs. Kill the route if the destination step imports the target arithmetic estimate or requires tuned ranks/windows.

## Evidence boundary

`VIS-378`--`VIS-386` establish the intrinsic source-subspace and normalization gates. `VIS-388`--`VIS-393` classify the minimal qutrit residual and show where Gaussian/isotropic calibration ends and symmetry becomes non-identifying. `VIS-394`--`VIS-402` calibrate broad finite source-free packet mechanisms. `VIS-403`--`VIS-406` show that latent/decoder language is vacuous until a numerical target-independent complexity budget is fixed, and then give exact observable consequences once it is.

`VIS-407` does not show that the full Wang/source-packet construction lacks such a budget. It shows only that rank-one qutrit source conjugacy/support geometry and source-stabilizer symmetry do not supply one by themselves, and that `t^2`-based Lipschitzness is not an intrinsic substitute because the scalar invariant chart is singular at the Weyl boundaries.

No persisted result yet derives a Wang-specific source--response complexity bound, proves that an admissible Wang family has an anomalous residual relative to the resulting frozen control, identifies an arithmetic cause for such an anomaly, or propagates one to a destination gain.

## Research disposition

Outcome: **narrowed**.

The clue remains `accepted`. The source-conjugacy/stabilizer route to the missing decoder budget is now closed in the minimal qutrit test bed. The next coherent step is to inspect the actual Wang/source-packet response construction for a target-independent source--tangent or source--response restriction in an intrinsic operational metric. If no such restriction exists, the decoder-capacity branch should be closed rather than replaced by another representation-level budget.
