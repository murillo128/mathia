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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

The long Wang chain through `VIS-367` shows that fixed finite compact positive packet geometry, growing raw polynomial depth, and its associated Vandermonde/Chebyshev ill-conditioning contain large source-free components. `VIS-371` further shows that any coordinate-free positive metric built only from the baseline Gram is necessarily spectral and therefore cannot create a genuinely new orientation channel by itself.

The finite-dimensional rational escape is now much narrower. `VIS-378` replaces expression-tree inverse conditioning by the intrinsic derivative of the represented noncommutative rational function. `VIS-379` restricts that sensitivity first to the simultaneous-similarity orbit of the external source tuple and then to the actual tangent supplied by the Wang Gram. `VIS-380`--`VIS-382` show that bounded output orientation requires collapse of the joint commutator gap together with nonvanishing Gram-tangent mass on the defect-squared low-mode scale.

`VIS-383`--`VIS-386` remove generator-coordinate and tangent-amplitude gauges. The intrinsic centered source subspace `S` carries the Hilbert-Schmidt commutator Laplacian `Delta_S`; after removing `ker Delta_S`, the normalized positive spectral measure is scale-free. Its first moment is the scalar defect rate, and the super-mean cumulative mass has a universal Markov floor, so an order-one self-normalized low-mode mass is not source-specific evidence by itself.

`VIS-387` shows that rank-one qubits are too small: once scalar defect is fixed, the full positive spectral shape is fixed. `VIS-388` and `VIS-389` identify generic rank-one qutrits as the minimal nontrivial test bed. The source cubic invariant fixes the three positive support points, and after the first moment `m_1` is fixed all remaining normalized spectral-shape freedom is one-dimensional, represented by

`u=[m_2-L(m_1)]/[U(m_1)-L(m_1)]`.

`VIS-390` gives the exact isotropic null: at fixed generic source and `m_1`, `u` is uniform. `VIS-391` allows arbitrary independent Gaussian scale in each root sector and gives an exact inverse-cube conditional law with uniformizer `v=F_lambda(u|m_1)`. `VIS-392` proves that this sector-scaled family exhausts all covariance freedom compatible with the full generic source stabilizer **inside the Gaussian class**.

`VIS-393` closes the next tempting interpretation. Source-stabilizer symmetry alone does not determine any law on the three sector weights. By sampling an arbitrary weight vector and Haar-averaging its torus orbit, one can realize every probability law on the weight simplex while preserving the full source stabilizer. At fixed interior `m_1`, every probability law on the residual coordinate `u` is likewise symmetry-compatible. Therefore there is no nontrivial "maximally symmetry-preserving" residual null beyond Gaussianity: enlarging all the way to arbitrary invariant laws makes the test vacuous.

The remaining channel is consequently not just "non-isotropic alignment". It is **a residual law that is exceptional relative to a separately justified, source-free nuisance mechanism or matched control that preserves the relevant Wang resources but is restricted for reasons other than source-stabilizer symmetry**, together with a structural explanation and a destination-level payoff.

## Research question

Can an admissible Wang/source-packet construction produce a normalized positive-spectrum Gram spectral distribution for the intrinsic source-subspace commutator Laplacian `Delta_S` that is genuinely source-specific and survives a falsifiable, independently specified source-free control family, in a way that can still be propagated to a Wang destination after all scale and conditioning costs are charged?

Equivalently, after quotienting compact/Vandermonde conditioning, Gram-only spectral filtering, bounded positive preconditioning, rational-expression artifacts, unavailable similarity directions, bare commutator-gap collapse, generator-coordinate gauge, tangent-amplitude gauge, the isotropic defect-energy budget, the universal Markov floor, the exact qutrit isotropic and sector-scaled Gaussian nulls, and finally the fact that source symmetry alone leaves the non-Gaussian weight law arbitrary, is there a remaining **mechanistically restricted** nonarithmetic control under which the Wang residual is still exceptional?

A positive answer still needs a destination-level payoff: the source-specific orientation must produce a smaller Wang output after metric scale, Gram-gap/cluster width, coefficient norm, normalization, rank-selection, and source-information costs are all charged.

## Why it may matter

The qutrit reduction is now unusually sharp. Source conjugacy is captured by the cubic source invariant, scalar tangent defect by `m_1`, and the remaining positive spectral shape by one scalar `u`. Gaussian nuisance freedom can be calibrated exactly through `VIS-391`, and `VIS-392` proves there is no missing symmetry-compatible Gaussian covariance.

But `VIS-393` shows why rejecting that Gaussian family is not enough. Full source-stabilizer invariance permits arbitrary distributions of `u`; symmetry itself supplies no stronger discriminating null. The next control must therefore come from actual nonarithmetic mechanism: admissibility, block geometry, repeated source-free constructions, externally fixed radial/tail laws, or another resource that can be frozen independently of the candidate arithmetic residual.

This prevents a false escalation in which every Gaussian rejection is called source evidence while the unrestricted invariant family could reproduce the same residual by construction.

## Decisive test

Choose one explicit admissible source family, center it modulo the identity, and form its Hilbert-Schmidt source subspace `S`. Freeze the ambient coefficient-space Hilbert metric and the numerical rank/tolerance rule before inspecting the candidate signal. Construct

`Delta_S=sum_a ad_(E_a)^*ad_(E_a)`

from a Hilbert-Schmidt orthonormal basis `E_a` of `S`, or use the exactly equivalent pseudoinverse-frame contraction. Let `P_0` project onto `ker Delta_S`, set `g=(I-P_0)G`, and if `g != 0` record the scale-invariant positive spectral distribution and its first moment

`m_S(G)=<g,Delta_S g>/||g||_F^2`.

For the generic qutrit rank-one test bed, compute the source cubic invariant, the support `q_1<q_2<q_3`, the moments `m_1,m_2`, and the residual coordinate `u`. Use `VIS-390` only as the isotropic baseline and `VIS-391` only when the Gaussian sector-rate ratios are fixed from independent controls or a pre-specified source-free model. Do not fit nuisance parameters to the same candidate residual being judged.

Do **not** use source-stabilizer invariance itself to justify a broader non-Gaussian null. `VIS-393` proves that the invariant family can realize an arbitrary law on `u`, so a symmetry-only null has no falsifiable residual prediction. Any stronger control must state the additional mechanism that restricts its law and must fix or estimate that restriction from information independent of the candidate effect.

Construct matched controls preserving the matrix resources that remain relevant after the quotients: source-subspace dimension, Hermitian structure, fixed ambient Hilbert metric, appropriate operator/subspace scale, coarse Gram clustering or admissibility resources actually used by the construction, tangent-normalization rule, and destination metric bounds. In the qutrit case stratify or match by source cubic geometry and `m_1`. Break the arithmetic/source coupling while keeping those nonarithmetic resources. The control must have a nondegenerate realizable sample space and a pre-registered statistic/decision rule.

A candidate source-specific channel must remain exceptional relative to this independently constrained family across scale/truncation changes fixed without seeing the effect. Then identify the geometry mathematically: which source relation creates the residual, why the matched control destroys it, and what source information is therefore retained.

Kill the route if the residual is reproduced by the matched controls, if significance disappears after independently calibrated Gaussian or non-Gaussian nuisance structure is admitted, if the null acquires enough post-hoc freedom to fit an arbitrary `u` law, if the effect depends on tuned rank/windows, or if the destination rule imports the target arithmetic estimate. A positive source-side residual remains insufficient unless its full cost propagates to the Wang destination without assuming a stronger bound for `G`, `theta`, or an equivalent unsmoothed source quantity.

## Evidence boundary

`VIS-378`--`VIS-386` establish exact finite-dimensional necessary conditions and remove coordinate/amplitude false positives. `VIS-387`--`VIS-389` classify the minimal qutrit residual-shape degree. `VIS-390` gives the exact isotropic conditional null. `VIS-391` gives the exact sector-scaled Gaussian extension. `VIS-392` proves that extension is the full source-stabilizer-invariant Gaussian covariance family. `VIS-393` proves that once Gaussianity is dropped, source-stabilizer symmetry alone leaves the sector-weight and fixed-`m_1` residual laws arbitrary.

None of these results proves that an admissible Wang family has an anomalous residual relative to a properly restricted matched control, identifies an arithmetic cause for such an anomaly, or propagates one to a Wang gain. `VIS-393` also does not claim that every invariant law is Wang-admissible; it shows only that **symmetry cannot be the restriction that makes the stronger null informative**.

The clue therefore remains `accepted`, but is narrowed again: the next source-specificity test must compare the qutrit residual against a mechanistically restricted nonarithmetic family justified independently of the candidate arithmetic residual. The symmetry hierarchy itself is exhausted as a source of a canonical stronger null.

## Research disposition

Outcome: **narrowed**.

For the minimal qutrit route, use the exact Gaussian ladder only when its nuisance parameters are independently calibrated. If that ladder is rejected, do not infer source specificity from source-stabilizer symmetry: `VIS-393` shows that unrestricted invariant non-Gaussian laws can realize any residual-shape distribution. The next useful control must earn its restriction from source-free Wang/admissibility structure, and only a residual surviving that control should proceed to the destination-cost test.
