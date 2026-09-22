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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

The long Wang chain through `VIS-367` shows that fixed finite compact positive packet geometry, growing raw polynomial depth, and its associated Vandermonde/Chebyshev ill-conditioning contain large source-free components. `VIS-371` further shows that any coordinate-free positive metric built only from the baseline Gram is necessarily spectral and therefore cannot create a genuinely new orientation channel by itself.

The finite-dimensional rational escape is now much narrower. `VIS-378` replaces expression-tree inverse conditioning by the intrinsic derivative of the represented noncommutative rational function. `VIS-379` restricts that sensitivity first to the simultaneous-similarity orbit of the external source tuple and then to the actual tangent supplied by the Wang Gram. A large derivative in an unavailable direction is irrelevant.

`VIS-380` identifies the next necessary geometric degeneration. For a bounded-spread positive rational output, persistent order-one Gram orientation while the external-generator defect tends to zero forces the joint commutator gap of the source tuple to collapse. `VIS-381` shows that gap collapse alone is insufficient: the Gram tangent must carry nonvanishing mass in the collapsing low positive commutator modes.

`VIS-382` fixes the relevant scale. If the output orientation `q=||[G,C]||_F` stays order one and the output spectral spread stays bounded, then a fixed amount of Gram-tangent mass must already lie in positive commutator modes with eigenvalues `lambda=O(epsilon_G^2)`, where `epsilon_G^2=<G,Delta_H G>` is the source-tuple commutator defect energy. The surviving channel is therefore not generic rational sensitivity or generic near-reducibility, but **defect-squared low-mode localization aligned with the actual Gram tangent**.

`VIS-383` then exposes a representation false positive in that statistic. The naive coordinate Laplacian `Delta_H=sum_j ad_(H_j)^*ad_(H_j)` depends on the Euclidean metric assigned to the generator index, so anisotropic reweighting can create order-one normalized low-mode mass without changing the source span or exact joint commutant.

`VIS-384` removes that gauge relative to the fixed coefficient-space Hilbert geometry. Center the generators modulo the scalar identity, let `S` be their Hilbert-Schmidt span, and define `Delta_S` by summing commutator squares over any Hilbert-Schmidt orthonormal basis of `S`. Equivalently, contract an arbitrary redundant generator frame with the pseudoinverse of its source Gram. The resulting `Delta_S`, defect energy, and defect-normalized projector profile are invariant under every change of generator coordinates that preserves `S`, including anisotropic and redundant presentations.

The remaining channel is therefore sharper again: **source-subspace-specific defect-squared localization**, after quotienting generator presentation. Universal subspace geometry, approximate reducibility, block structure, a data-dependent numerical rank choice, or another source-independent mechanism could still produce the same low-mode concentration.

## Research question

Can an admissible Wang/source-packet construction force or detect order-one Gram-tangent mass in the `lambda=O(epsilon_S^2)` spectral band of the intrinsic source-subspace commutator Laplacian `Delta_S` in a way that is genuinely source-specific and survives matched source-free controls?

Equivalently, after quotienting the known compact/Vandermonde conditioning, Gram-only spectral filtering, bounded positive preconditioning, rational-expression artifacts, unstructured derivative blow-up, irrelevant similarity-orbit directions, bare commutator-gap collapse, low modes not seen by the Gram tangent, and arbitrary source-generator reparameterization, is there any remaining mechanism that ties the intrinsic defect-squared low eigenspace to arithmetic information rather than generic approximate reducibility of a source subspace?

A positive answer would still need a destination-level payoff: the localized source-specific orientation must produce a smaller Wang output after metric scale, Gram-gap/cluster width, coefficient norm, normalization, rank-selection, and source-information costs are all charged.

## Why it may matter

This question isolates the first finite-dimensional positive-Hilbert rational channel not already explained by source-free conditioning, generic matrix sensitivity, or generator-coordinate gauge. The earlier frontier asked whether an extra non-Gram operator could create useful orientation. The current frontier is sharper: even an external noncommuting operator family receives no credit unless its **intrinsic source subspace** has defect-squared approximate-commutant modes, the actual Gram tangent occupies them, and matched non-arithmetic subspaces do not reproduce the effect.

`VIS-384` also makes the next comparison cleaner. Controls no longer need to match arbitrary generator weights or coordinate condition numbers; they can be compared through the same fixed coefficient-space Hilbert metric after quotienting each generator list to its centered subspace. If the intrinsic localization is universal under controls preserving dimension, coarse subspace geometry, operator-norm scale and relevant Gram clustering while removing arithmetic coupling, then this positive-Hilbert packet route still has no identified arithmetic carrier. If arithmetic/source structure changes the intrinsic low-mode projector mass or geometry in a stable way those controls cannot reproduce, there is a precise object to analyze.

## Decisive test

Choose one explicit admissible source family, center it modulo the identity, and form its Hilbert-Schmidt source subspace `S`. Freeze the ambient coefficient-space Hilbert metric and the numerical rank/tolerance rule before inspecting the candidate signal. Construct

`Delta_S=sum_a ad_(E_a)^*ad_(E_a)`

from a Hilbert-Schmidt orthonormal basis `E_a` of `S`, or use the exactly equivalent pseudoinverse-frame contraction. Record

`epsilon_S(G)^2=<G,Delta_S G>`

and study

`A_(G,S)(alpha)=||P_(0,alpha epsilon_S(G)^2]^(Delta_S)G||_F`

for fixed preselected `alpha>0`. Use spectral projectors rather than individual eigenvectors so degeneracies and crossings do not create a coordinate artifact.

As an implementation gate, verify exact invariance under deliberately anisotropic invertible reparameterizations and redundant expansions of the same centered source subspace. Failure of that check means the computation has not actually implemented the `VIS-384` quotient.

Then construct matched controls that preserve the obvious matrix resources still relevant after the quotient: source-subspace dimension, Hermitian structure, the fixed ambient Hilbert metric, appropriate operator-norm or subspace-scale data, relevant coarse Gram clustering, and any destination metric bounds. Break the arithmetic/source coupling while keeping those resources. The control must have a nondegenerate realizable sample space; merely conjugating every object together or otherwise preserving the full joint configuration is not a null.

A candidate source-specific channel must show stable excess or structurally different localization of `G` in the `O(epsilon_S^2)` positive spectrum relative to those controls, across scale/truncation changes fixed independently of the observed effect. If a quantitative statistic is used, freeze its normalization, spectral window, rank rule, and decision rule before confirmation data. Then identify the actual low-mode geometry mathematically: which approximate symmetry or block relation produces it, why the Gram tangent overlaps it, and which source information is lost when the matched control destroys the effect.

Kill the route if the localization is reproduced by generic source subspaces with matched resources, disappears under harmless ambient unitary changes, depends on a data-tuned rank threshold, or requires an output metric/rational rule whose construction already imports the target arithmetic estimate. A positive low-mode difference is not enough unless its full cost propagates to the Wang destination without assuming a stronger bound for `G`, `theta`, or an equivalent unsmoothed source quantity.

## Evidence boundary

`VIS-378`--`VIS-382` establish exact finite-dimensional **necessary conditions and accounting bounds** for bounded positive rational orientation. `VIS-383` shows that the naive generator-index metric can manufacture the target normalized localization. `VIS-384` gives an exact coordinate quotient: relative to a fixed coefficient-space Hilbert geometry, the source-subspace Laplacian and its normalized low-mode profile are independent of the generator presentation.

None of these results proves that intrinsic defect-squared low modes exist in any useful arithmetic family, that such modes are source-specific, that their projector mass is stable, or that they improve a Wang destination. `VIS-384` also does not make the ambient coefficient-space metric or numerical rank rule free resources; those must be fixed independently of the observed effect.

The clue therefore remains `accepted`: the finite positive-Hilbert rational route has been narrowed to a coordinate-quotiented source-subspace localization test, but the decisive source-specificity and destination-payoff questions remain open.

## Research disposition

Outcome: **narrowed**.

Future work on this clue should start from the intrinsic centered source subspace and `Delta_S`, not from a raw generator-coordinate Laplacian. The next substantive test is whether arithmetic/source construction produces excess defect-squared Gram overlap relative to matched non-arithmetic source subspaces after the ambient Hilbert metric and rank rule are fixed, and whether any surviving excess can be charged through to the Wang destination.