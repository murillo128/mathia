---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: resolved
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
  - research/visual_exploration/findings/VIS-408-wang-final-test-packet-does-not-supply-qutrit-decoder-budget.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already been reduced to the normalized Chebyshev-theta remainder `G(u)=e^(-u)theta(e^u)-1`, while `VIS-371` and `VIS-378`--`VIS-386` remove Gram-only spectral filtering, unavailable similarity directions, coordinate gauge, tangent-amplitude gauge, and the universal scalar defect-energy floor before any residual orientation is credited as source information.

In the minimal generic rank-one qutrit test bed, `VIS-388`--`VIS-390` reduce the remaining normalized tangent spectral shape to one residual scalar `u` after source cubic geometry and first moment are fixed. `VIS-393` then shows that source-stabilizer symmetry alone places no law on that residual: every Borel law on `u` can be realized by a source-stabilizer-invariant tangent law. The packet-control chain through `VIS-394`--`VIS-402` further calibrates broad independent, exclusive-budget, signed, and finite additive common-factor source-free mechanisms.

`VIS-403`--`VIS-404` close the representation-level escape in which unrestricted finite latent variables or a fixed uniform latent with target-dependent monotone transport are presented as meaningful restrictions. `VIS-405` identifies the first exact quantitative boundary: a pre-fixed monotone `L`-Lipschitz decoder forces the residual target law to contain the uniform component `L^(-1)Leb_I`. `VIS-406` converts ordinary frozen representation budgets into such a mass floor: fixed basis/coefficient budgets and fixed polynomial degree give explicit target-independent Lipschitz bounds.

`VIS-407` removes source conjugacy/support geometry itself as the missing justification for that budget in the rank-one qutrit test bed. The normalized source quotient has a regular Hilbert-Schmidt arc-length coordinate `theta`, while the complete algebraic invariant `x=tr(E^3)^2=(1/6)cos^2(3theta)` is boundary-singular. A Lipschitz/derivative budget measured only in `x` is therefore coordinate-dependent and cannot be credited as intrinsic source complexity.

`VIS-408` now audits the **actual final Wang packet/test-function interface**. Wang chooses an arbitrary fixed real-even `eta in C_c^infinity((-lambda/2,lambda/2))` with `int eta^2=1`, sets `f=eta^2`, `K=hat(f)`, and optimizes the resulting scalar zero-pair functional `C(f)`. Before optimization this is an infinite-dimensional smooth class with no packet-uniform derivative, finite-basis, polynomial-degree, or Lipschitz budget; normalized bumps can be localized arbitrarily inside the fixed support. After optimization Wang obtains an explicit target-independent cosine profile in the larger `L^2` class and approximates it by admissible smooth squares, but that profile is a scalar zero-pair kernel, not a source-to-qutrit response map. The source supplies no dictionary turning it into the decoder restriction required by `VIS-405`--`VIS-407`.

## Research question

Can an admissible Wang/source-packet construction derive, before inspecting the candidate residual, a genuinely target-independent family of allowed source-to-response maps whose complexity is fixed by packet resources or another intrinsic operational constraint, and does the resulting qutrit residual then violate the corresponding exact source-free null while surviving full Wang destination-cost propagation?

The direct Wang-packet answer is now negative: Wang's actual test-packet admissibility neither imposes a universal numerical decoder capacity nor defines the qutrit source-response map. Any surviving version of this question would therefore require a **new explicit theorem** mapping Wang's arithmetic source decomposition into the intrinsic qutrit tangent/response object and bounding that map independently of the target. That is no longer a property of the existing packet interface.

## Why it may matter

The current qutrit branch deliberately eliminated increasingly flexible ways to manufacture a residual anomaly. The generic approximation-theory part is understood: once a real complexity budget exists, it can be translated into a falsifiable observable null. `VIS-408` establishes that the needed budget is not hidden in Wang's final packet language.

This prevents a source-attribution error. Wang's fixed test functions and variationally optimal kernel are genuine, mathematically controlled objects, but importing their fixedness into an unrelated qutrit decoder would create exactly the representation-level restriction the preceding findings were designed to rule out. A future source-response theorem may still be worthwhile, but it must be established as new mathematics rather than inferred from packet admissibility.

## Decisive test

The decisive test was to inspect the source-level Wang packet construction rather than invent another decoder family. Wang's Section 3 admits every fixed normalized real-even smooth `eta` in the support interval. Dilation of a fixed normalized bump preserves every stated admissibility condition while making derivative norms arbitrarily large, so the class has no uniform numerical smoothness or finite-complexity budget.

Wang's Section 4 does select a unique cosine minimizer for the scalar functional `C(f)` in the larger `L^2` class and proves that admissible smooth-square packets approach the same infimum. This does not repair the decoder route: the optimized object acts as a scalar kernel on zero differences, and no source-to-qutrit tangent/response identification is present.

A future attempt should be treated as a different research question unless it derives an explicit intrinsic map from the Wang arithmetic source to the qutrit response object and proves a target-independent bound on that map. Merely choosing the Wang optimizer, another latent, another chart, or another finite representation is not such a derivation.

## Evidence boundary

`VIS-378`--`VIS-386` establish the intrinsic source-subspace and normalization gates. `VIS-388`--`VIS-393` classify the minimal qutrit residual and show where Gaussian/isotropic calibration ends and symmetry becomes non-identifying. `VIS-394`--`VIS-402` calibrate broad finite source-free packet mechanisms. `VIS-403`--`VIS-406` show that latent/decoder language is vacuous until a numerical target-independent complexity budget is fixed, and then give exact observable consequences once it is. `VIS-407` shows that the natural scalar invariant chart does not provide an intrinsic replacement.

`VIS-408` is an exact interface audit of Wang's paper, not an impossibility theorem for all conceivable arithmetic source-response maps. It establishes only that the **existing Wang final packet/test-function construction** does not itself contain the qutrit decoder budget or dictionary sought here. A genuinely new source-to-response theorem could open a different route.

No result in this chain proves an anomalous qutrit residual, an arithmetic cause for one, a new pair-correlation theorem, a zeta-zero criterion, or an RH consequence.

## Research disposition

Outcome: **refuted**.

Resolved by:
- [[research/visual_exploration/findings/VIS-408-wang-final-test-packet-does-not-supply-qutrit-decoder-budget]]

The decoder-capacity branch cannot be justified from Wang packet admissibility alone. The actual admissible packet class is too flexible to furnish a universal numerical decoder budget, while the variational optimizer is a scalar zero-pair kernel with no proved qutrit source-response dictionary. Any revival requires a new explicit source-to-qutrit response theorem and should enter as a new research question rather than another repair of this clue.