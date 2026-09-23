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

`VIS-390` gives the exact isotropic one-replica null: at fixed generic source and `m_1`, `u` is uniform. `VIS-391` allows arbitrary independent Gaussian scale in each root sector and gives an exact inverse-cube conditional law with uniformizer `v=F_lambda(u|m_1)`. `VIS-392` proves that this sector-scaled family exhausts all covariance freedom compatible with the full generic source stabilizer **inside the Gaussian class**.

`VIS-393` closes the next tempting interpretation. Source-stabilizer symmetry alone does not determine any law on the three sector weights. By sampling an arbitrary weight vector and Haar-averaging its torus orbit, one can realize every probability law on the weight simplex while preserving the full source stabilizer. At fixed interior `m_1`, every probability law on the residual coordinate `u` is likewise symmetry-compatible. Therefore there is no nontrivial "maximally symmetry-preserving" residual null beyond Gaussianity: enlarging all the way to arbitrary invariant laws makes the test vacuous.

`VIS-394` supplies a larger control whose restriction comes from an explicit source-free mechanism rather than symmetry. If every qutrit root sector aggregates the same `k` independent Gaussian packet replicas, its sector energy is `Gamma(k,lambda_i)`. Normalizing the three independent sector energies gives an exact normalized-Gamma/scaled-Dirichlet density, and conditioning on `m_1` gives an exact residual law. For equal rates this is already nonuniform for every `k>1`, so finite packet multiplicity can manufacture structured residual shape without arithmetic coupling.

`VIS-395` removes the common-replica-count restriction. If sector `i` aggregates an independently specified count `k_i`, then the exact simplex law is

`f(w) proportional_to prod_i w_i^(k_i-1) / [sum_i lambda_i w_i]^K`,

with `K=sum_i k_i`, and the fixed-`m_1` residual inherits the corresponding one-dimensional density. Even at equal sector rates, an unequal count vector produces asymmetric or skewed nonuniform residual shape. Thus neither residual nonuniformity nor residual asymmetry is source evidence when unequal source-free packet multiplicities are architecturally available.

`VIS-396` removes the simplest uncovered **cross-sector dependence** mechanism. If independent sector-specific packet energies `X_i~Gamma(k_i,lambda)` share an additive common packet block `C~Gamma(k_0,lambda)` through `Y_i=X_i+C`, then the normalized weights have the exact representation

`w_i=(1-r)p_i+r/3`,

where `p~Dirichlet(k_1,k_2,k_3)` and the random shrinkage `r=3C/(sum_i X_i+3C)` is independent of `p` with an explicit density. Cross-sector correlation and barycentric concentration can therefore also be manufactured by a source-free packet mechanism.

`VIS-397` now removes the common-rate restriction from that shared-block control. For independent `X_i~Gamma(k_i,lambda_i)` and `C~Gamma(k_0,lambda_0)`, the simple independent Dirichlet/shrinkage factorization is lost, but the normalized simplex law remains exact:

`f_W(w) proportional_to integral_0^(3 min_i w_i)`
`  r^(k_0-1) prod_i(w_i-r/3)^(k_i-1)`
`  / [lambda_0 r/3 + sum_i lambda_i(w_i-r/3)]^(K+k_0) dr`.

Conditioning on `m_1` again reduces this to a one-dimensional residual density and exact CDF calibration. Unequal sector scales, unequal shared/idiosyncratic rates, positive cross-sector correlation, barycentric concentration, nonuniformity, and asymmetry can therefore all occur inside an explicitly calibratable source-free single-common-block Gamma mechanism when those nuisance parameters are fixed independently.

The remaining channel is consequently **a residual law that is exceptional relative to separately justified source-free mechanisms or matched controls whose nuisance parameters are fixed independently of the candidate residual**, together with a structural explanation and a destination-level payoff.

## Research question

Can an admissible Wang/source-packet construction produce a normalized positive-spectrum Gram spectral distribution for the intrinsic source-subspace commutator Laplacian `Delta_S` that is genuinely source-specific and survives a falsifiable, independently specified source-free control family, in a way that can still be propagated to a Wang destination after all scale and conditioning costs are charged?

Equivalently, after quotienting compact/Vandermonde conditioning, Gram-only spectral filtering, bounded positive preconditioning, rational-expression artifacts, unavailable similarity directions, bare commutator-gap collapse, generator-coordinate gauge, tangent-amplitude gauge, the isotropic defect-energy budget, the universal Markov floor, the exact qutrit Gaussian ladder, symmetry-only vacuity, the full independent replicated-Gamma count/rate ladder, and the unequal-rate single-common-block Gamma dependence ladder, is there a remaining **mechanistically restricted** nonarithmetic control under which the Wang residual is still exceptional?

A positive answer still needs a destination-level payoff: the source-specific orientation must produce a smaller Wang output after metric scale, Gram-gap/cluster width, coefficient norm, normalization, rank-selection, and source-information costs are all charged.

## Why it may matter

The qutrit reduction is now unusually sharp. Source conjugacy is captured by the cubic source invariant, scalar tangent defect by `m_1`, and the remaining positive spectral shape by one scalar `u`. Gaussian nuisance freedom can be calibrated exactly through `VIS-391`, and `VIS-392` proves there is no missing symmetry-compatible Gaussian covariance.

`VIS-393` shows why rejecting that Gaussian family is not enough: full source-stabilizer invariance permits arbitrary distributions of `u`, so symmetry itself supplies no stronger discriminating null. `VIS-394` and `VIS-395` show that concrete source-free repeated-packet mechanisms already produce broad nonuniform and asymmetric residual families without appealing to arbitrary invariant laws. `VIS-396` adds a classical shared-component mechanism, and `VIS-397` proves that its exact calibratability does not depend on the artificial simplification that all sector and shared packet rates coincide.

This blocks a broader false escalation in which residual shape is called source-specific merely because it is non-Gaussian, nonuniform, skewed, concentrated, correlated across sectors, or inconsistent with one common rate. All of those features can arise from independently specified source-free packet architecture.

## Decisive test

Choose one explicit admissible source family, center it modulo the identity, and form its Hilbert-Schmidt source subspace `S`. Freeze the ambient coefficient-space Hilbert metric and the numerical rank/tolerance rule before inspecting the candidate signal. Construct

`Delta_S=sum_a ad_(E_a)^*ad_(E_a)`

from a Hilbert-Schmidt orthonormal basis `E_a` of `S`, or use the exactly equivalent pseudoinverse-frame contraction. Let `P_0` project onto `ker Delta_S`, set `g=(I-P_0)G`, and if `g != 0` record the scale-invariant positive spectral distribution and its first moment

`m_S(G)=<g,Delta_S g>/||g||_F^2`.

For the generic qutrit rank-one test bed, compute the source cubic invariant, the support `q_1<q_2<q_3`, the moments `m_1,m_2`, and the residual coordinate `u`. Use `VIS-390` only as the isotropic one-replica baseline. Use `VIS-391` when independent sector rates are justified for one Gaussian block per sector. Use `VIS-394` when the source-free mechanism independently specifies a common replica count `k`. Use `VIS-395` when the architecture independently specifies a sectorwise count vector `(k_1,k_2,k_3)` and sector-rate ratios. Use `VIS-396` when the architecture independently specifies one additive shared packet block under a common rate. Use `VIS-397` when the same one-shared-block mechanism has independently specified sector and shared rates. Transform the residual through the corresponding exact conditional CDF. Do not fit counts, rates, shared-block strength, or another nuisance parameter to the same candidate residual being judged.

Do **not** use source-stabilizer invariance itself to justify a broader non-Gaussian null. `VIS-393` proves that the invariant family can realize an arbitrary law on `u`, so a symmetry-only null has no falsifiable residual prediction. Any stronger control must state the additional mechanism that restricts its law and must fix or estimate that restriction from information independent of the candidate effect.

Construct matched controls preserving the matrix resources that remain relevant after the quotients: source-subspace dimension, Hermitian structure, fixed ambient Hilbert metric, appropriate operator/subspace scale, coarse Gram clustering or admissibility resources actually used by the construction, tangent-normalization rule, and destination metric bounds. In the qutrit case stratify or match by source cubic geometry and `m_1`. Break the arithmetic/source coupling while keeping those nonarithmetic resources. The control must have a nondegenerate realizable sample space and a pre-registered statistic/decision rule.

The next useful extension should now come from a genuinely different source-free restriction not covered by independent Gamma sector energies or a single additive common Gamma block even with unequal rates: for example non-Gamma packet-amplitude laws, several shared latent blocks coupling different sector subsets, or a Wang admissibility constraint that derives a coupled law. A candidate source-specific channel must remain exceptional relative to the resulting independently constrained family across scale/truncation changes fixed without seeing the effect.

Kill the route if the residual is reproduced by the matched controls, if significance disappears after independently calibrated independent-Gamma or unequal-rate common-shock nuisance structure is admitted, if the null acquires enough post-hoc freedom to fit an arbitrary `u` law, if the effect depends on tuned rank/windows, or if the destination rule imports the target arithmetic estimate. A positive source-side residual remains insufficient unless its full cost propagates to the Wang destination without assuming a stronger bound for `G`, `theta`, or an equivalent unsmoothed source quantity.

## Evidence boundary

`VIS-378`--`VIS-386` establish exact finite-dimensional necessary conditions and remove coordinate/amplitude false positives. `VIS-387`--`VIS-389` classify the minimal qutrit residual-shape degree. `VIS-390` gives the exact isotropic one-replica conditional null. `VIS-391` gives the exact sector-scaled one-replica Gaussian extension. `VIS-392` proves that extension is the full source-stabilizer-invariant Gaussian covariance family. `VIS-393` proves that once Gaussianity is dropped, source-stabilizer symmetry alone leaves the sector-weight and fixed-`m_1` residual laws arbitrary. `VIS-394` proves the exact common-count replicated-Gaussian normalized-Gamma control. `VIS-395` extends that calculation to independently specified sectorwise replica counts and rates. `VIS-396` adds one additive shared Gamma block under a common rate. `VIS-397` removes that common-rate restriction and derives the exact normalized-simplex and fixed-`m_1` residual laws for independently specified sector and shared rates.

None of these results proves that an admissible Wang family has an anomalous residual relative to a properly restricted matched control, identifies an arithmetic cause for such an anomaly, or propagates one to a Wang gain. `VIS-397` does not exhaust non-Gamma packet laws, multiple or subset-specific shared shocks, arbitrary dependence, or admissibility-induced coupling and does not license fitting nuisance parameters to the candidate residual.

The clue therefore remains `accepted`, but is narrowed again: the next source-specificity test must compare the qutrit residual against mechanistically justified controls whose nuisance degrees of freedom are frozen independently. Independent replicated-Gamma packet architectures and the full unequal-rate single-common-block Gamma mechanism are now exactly calibratable; further extensions need genuinely different source-free structure.

## Research disposition

Outcome: **narrowed**.

For the minimal qutrit route, apply the exact source-free ladder only at the level justified by the mechanism: `VIS-390` for one isotropic block, `VIS-391` for one independently scaled Gaussian block per sector, `VIS-394` for a common independently specified replica count, `VIS-395` for independently specified sectorwise counts/rates, `VIS-396` for one additive common packet block under a common rate, and `VIS-397` for the same single-common-block mechanism with independently specified unequal rates. Rejecting those controls is still not source evidence by itself. The next stronger null must earn its restrictions from non-Gamma amplitudes, richer multi-block dependence, Wang admissibility, or another independently justified mechanism, and only a residual surviving that control should proceed to the destination-cost test.
