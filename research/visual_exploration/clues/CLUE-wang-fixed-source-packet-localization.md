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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

The long Wang chain through `VIS-367` shows that fixed finite compact positive packet geometry, growing raw polynomial depth, and its associated Vandermonde/Chebyshev ill-conditioning contain large source-free components. `VIS-371` further shows that any coordinate-free positive metric built only from the baseline Gram is necessarily spectral and therefore cannot create a genuinely new orientation channel by itself.

The finite-dimensional rational escape is now much narrower. `VIS-378` replaces expression-tree inverse conditioning by the intrinsic derivative of the represented noncommutative rational function. `VIS-379` restricts that sensitivity first to the simultaneous-similarity orbit of the external source tuple and then to the actual tangent supplied by the Wang Gram. A large derivative in an unavailable direction is irrelevant.

`VIS-380` identifies the next necessary geometric degeneration. For a bounded-spread positive rational output, persistent order-one Gram orientation while the external-generator defect tends to zero forces the joint commutator gap of the source tuple to collapse. `VIS-381` shows that gap collapse alone is insufficient: the Gram tangent must carry nonvanishing mass in the collapsing low positive commutator modes.

`VIS-382` fixes the relevant scale. If the output orientation `q=||[G,C]||_F` stays order one and the output spectral spread stays bounded, then a fixed amount of Gram-tangent mass must already lie in positive commutator modes whose eigenvalues are on the defect-squared scale. Its orientation-adapted threshold is homogeneous in the tangent amplitude.

`VIS-383` exposes a representation false positive in the naive generator-coordinate Laplacian. `VIS-384` removes that gauge by replacing the generator list with its centered Hilbert-Schmidt source subspace `S` and the intrinsic commutator Laplacian `Delta_S`. `VIS-385` then supplies a source-free calibration: rank fixes total commutator spectral mass, and under a Haar-uniform rank-`r` source subspace the fixed-`G` defect energy has exact finite-dimensional mean and variance.

`VIS-386` exposes one further representation issue in the exploratory low-mode statistic itself. The raw window `P_(0,alpha epsilon_S(G)^2]G` moves when only the amplitude of `G` is rescaled. After removing the exact commutant component `g=(I-P_0)G`, the scale-invariant quantity is the normalized spectral distribution relative to

`m_S(G)=epsilon_S(G)^2/||g||_F^2`.

But that quotient has an exact universal baseline: for every `alpha>1`, at least `1-1/alpha` of the normalized positive-spectrum Gram mass lies below `alpha m_S(G)` by Markov's inequality. Therefore an order-one self-normalized low-mode mass above the mean is not itself source-specific evidence.

The remaining channel is sharper again: **source-subspace-specific spectral organization after generator gauge, tangent-amplitude gauge, the isotropic rank baseline, and the universal self-normalized spectral floor have all been removed**.

## Research question

Can an admissible Wang/source-packet construction produce a normalized positive-spectrum Gram spectral distribution for the intrinsic source-subspace commutator Laplacian `Delta_S` that is genuinely source-specific and survives matched source-free controls, in a way that can still be propagated to a Wang destination after all scale and conditioning costs are charged?

Equivalently, after quotienting compact/Vandermonde conditioning, Gram-only spectral filtering, bounded positive preconditioning, rational-expression artifacts, unavailable similarity directions, bare commutator-gap collapse, generator-coordinate gauge, tangent-amplitude gauge, the isotropic source-subspace defect-energy budget, and the universal self-normalized Markov floor, is there any remaining low-spectrum organization that carries arithmetic/source information rather than generic approximate reducibility?

A positive answer still needs a destination-level payoff: the source-specific orientation must produce a smaller Wang output after metric scale, Gram-gap/cluster width, coefficient norm, normalization, rank-selection, and source-information costs are all charged.

## Why it may matter

The current question isolates a finite-dimensional positive-Hilbert rational channel that is no longer allowed to claim credit for representation choices or universal first-moment effects. `VIS-386` is especially important because a visually impressive concentration in a self-defect window can otherwise be manufactured by tangent scaling, and after scale normalization a large super-mean mass is partly guaranteed for every source by the same first-moment identity.

This creates a clean diagnostic split. First ask whether the fixed observed `(G,S)` is exceptional at the quadratic defect-energy level relative to the exact `VIS-385` isotropic Grassmann null. If not, compare the **shape** of the normalized positive spectral distribution against stronger matched controls. A source-specific claim must concern excess concentration, sub-mean structure, a stable distributional feature, or identifiable low-mode geometry beyond the universal `1-1/alpha` floor.

The isotropic null and Markov floor are only baseline layers. They do not preserve every Wang resource, so any surviving effect still requires stronger matched nonarithmetic controls and a mathematical explanation.

## Decisive test

Choose one explicit admissible source family, center it modulo the identity, and form its Hilbert-Schmidt source subspace `S`. Freeze the ambient coefficient-space Hilbert metric and the numerical rank/tolerance rule before inspecting the candidate signal. Construct

`Delta_S=sum_a ad_(E_a)^*ad_(E_a)`

from a Hilbert-Schmidt orthonormal basis `E_a` of `S`, or use the exactly equivalent pseudoinverse-frame contraction.

Let `P_0` project onto `ker Delta_S` and set

`g=(I-P_0)G`.

If `g=0`, the tangent carries no positive commutator component and this localization route is trivial. Otherwise record

`epsilon_S(G)^2=<g,Delta_S g>`

and the scale-invariant mean spectral value

`m_S(G)=epsilon_S(G)^2/||g||_F^2`.

Use the normalized spectral CDF

`F_(G,S)(alpha)=||P_(0,alpha m_S(G)]^(Delta_S)g||_F^2/||g||_F^2`

or an equivalently pre-registered scale-invariant spectral statistic. Verify exact invariance under nonzero rescaling of `G`, deliberately anisotropic invertible reparameterizations of the source generators, and redundant expansions of the same centered source subspace.

For `alpha>1`, treat

`F_(G,S)(alpha) >= 1-1/alpha`

as a universal source-free floor, not as evidence. Any quantitative claim should either compare excess above matched controls, use pre-registered sub-mean windows, or compare a broader normalized spectral profile. Freeze the normalization, spectral windows, rank rule, and decision rule before confirmation data.

Before interpreting higher spectral organization, run the `VIS-385` isotropic alignment calibration with `G` held fixed: compare the observed `epsilon_S(G)^2` to the exact Haar-Grassmann rank-`r` mean and variance. Treat an anomalous defect energy and an ordinary defect energy with anomalous normalized spectral shape as different mechanisms.

Then construct stronger matched controls preserving the matrix resources that remain relevant after the quotients: source-subspace dimension, Hermitian structure, fixed ambient Hilbert metric, appropriate operator/subspace scale, relevant coarse Gram clustering, tangent-normalization rule, and destination metric bounds. Break arithmetic/source coupling while keeping those resources. The control must have a nondegenerate realizable sample space.

A candidate source-specific channel must show stable excess or structurally different normalized low-spectrum organization relative to those controls across scale/truncation changes fixed independently of the observed effect. Then identify the geometry mathematically: which approximate symmetry or block relation produces it, why the Gram tangent overlaps it, and which source information is lost when the matched control destroys the effect.

Kill the route if the normalized spectral profile is reproduced by generic source subspaces with matched resources, if the apparent effect reduces to the universal Markov floor, disappears under harmless ambient unitary changes, depends on a data-tuned rank or window, or requires an output metric/rational rule that already imports the target arithmetic estimate. A positive spectral difference is still insufficient unless its full cost propagates to the Wang destination without assuming a stronger bound for `G`, `theta`, or an equivalent unsmoothed source quantity.

## Evidence boundary

`VIS-378`--`VIS-382` establish exact finite-dimensional necessary conditions and accounting bounds for bounded positive rational orientation. `VIS-383` removes a generator-coordinate false positive by exposing it; `VIS-384` supplies the intrinsic source-subspace quotient; `VIS-385` gives exact fixed-`G` isotropic defect-energy calibration; and `VIS-386` removes the tangent-amplitude gauge while identifying the universal self-normalized spectral mass floor.

None of these results proves that a useful arithmetic family has exceptional normalized spectral shape, that any such shape is source-specific, stable, or propagates to a Wang gain. `VIS-386` also does not say super-mean spectral windows are useless; it says their absolute order-one mass is nondiscriminating unless interpreted relative to the universal floor and matched controls.

The clue therefore remains `accepted`: the finite positive-Hilbert rational route has been narrowed to a coordinate-quotiented, tangent-normalized, isotropically calibrated spectral-shape test, but the decisive source-specificity and destination-payoff questions remain open.

## Research disposition

Outcome: **narrowed**.

Future work on this clue should compare scale-invariant positive spectral shape, not raw self-defect projector mass. Start with the `VIS-385` fixed-`G` defect-energy calibration, quotient tangent amplitude as in `VIS-386`, subtract or otherwise account for the universal Markov floor, then ask whether stronger matched nonarithmetic controls reproduce the remaining spectral organization and whether any surviving excess can be charged through to the Wang destination.
