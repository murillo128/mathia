# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Separate actual zero-power packets from inverse-section matched controls

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`, `MI-011-canonical-deflation-cancels-raw-cauchy-crowding-volume`, `MI-012-three-state-transverse-confluence-exposes-collective-shear`, `MI-013-absolute-height-and-global-zero-counts-are-invisible-to-the-collective-shear-obstruction`, `MI-014-quadratic-horizontal-tangency-is-the-three-state-conditioning-threshold`, `MI-015-confluent-volume-is-curvature-blind-and-controlled-by-radial-depth`, `MI-016-growing-confluent-rank-is-limited-by-endpoint-extrapolation-cost`, `MI-017-finite-high-zero-target-access-requires-a-target-bearing-compression-near-kernel`.

NB-115 localizes the canonical finite-section escape to target-bearing cell-compression modes. NB-116 uses horizontal Burnol mass plus Selberg density to put every high-zero packet above height `G` on retention scale `O(1/G+1/R)`. NB-117 then removes the spectral-coordinate ambiguity: in natural-cell coordinates, finite target access is exactly weighted interpolation of the harmonic minimizer `C+D/n` by confluent zero-power sums.

NB-118 adds an independent source equation that does not use zero height. Every finite packet of actual zeta zeros is orthogonal to every fixed finite Nyman generator space `V_M`. Writing `p_M=P_(V_M)e`, `r_M=e-p_M`, `d_M=||r_M||`, this forces any packet whose finite target capture exceeds the residual baseline `d_M^2` to cancel its visible correlation with `p_M` beyond the cell cutoff. Since the tail of each fixed `p_M` has norm squared `O_M(1/R)`, a target-bearing witness must satisfy

`||Q_R f||^2/||f||^2 = O_(M,c)(1/R)`

for every fixed capture fraction `c>d_M^2`. The first finite sections are already quantitative: `d_2^2=1-log 2`, while the two-generator space `{g_2,g_3}` gives `d_3^2≈0.09575`.

NB-119 proves that this inverse-section exponent is **sharp under fixed finite Nyman orthogonality alone**. The tail Gram matrix of the fixed generators satisfies

`Gamma_(M,R)=C_M/R+O_M(1/R^2)`

with `C_M>0`. Consequently the perfect visible target `e_R` can be repaired by a unique minimum-norm invisible tail into a vector `f_(M,R) in V_M^perp` with

`Q_R f_(M,R)=e_R`, `q_R(f_(M,R))=1`,

and

`||Q_R f_(M,R)||^2/||f_(M,R)||^2 = 1/(kappa_M R)+O_M(1/R^2)`

for an explicit `kappa_M>0`. Thus no theorem using only a fixed finite family of source equations `<f,g_b>=0` can improve the `1/R` exponent uniformly over that source-equation class.

The live source theorem is therefore sharper than after NB-118: **exclude actual zero-power packets from the inverse-section matched-control class**. The required input must distinguish the confluent power sums of NB-117 from arbitrary vectors in `V_M^perp`. Plausible routes are a source-aware coercive inequality for confluent power sums at `O(1/R)` retention, a growing family of Nyman equations with constants controlled independently of the desired Nyman conclusion, cross-cutoff coherence that prevents rebuilding the witness for each `R`, or another identity specific to actual zeta zeros.

Sending `M` to infinity is not free. The baseline `d_M->0` is itself the Nyman/RH approximation problem, while the periodic-tail repair constants `kappa_M` and the corresponding source conditioning may deteriorate. Any growing-`M` argument must expose that dependence rather than hide it in fixed-section notation.

## Keep target baseline, zero height, continuum mass, cell retention and source coherence separate

NB-118 is not another Gram-conditioning estimate: it combines actual-zero annihilation of fixed Nyman generators with finite target geometry. NB-119 supplies the matched control showing exactly where that information stops. A fixed source section controls capture above its residual threshold `d_M^2`, but once one allows an arbitrary invisible tail, the same finite equations permit perfect target alignment at retention `Theta_M(1/R)`.

Future claims should therefore distinguish available zero rank, horizontal zero mass, finite-section target baseline, continuum norm, retained cell energy, approximation of the harmonic minimizer, and **coherence of the source representation across cells, generators and cutoffs**. The unresolved object is no longer an abstract inverse-section near-kernel mode; it is whether the actual zero-power interpolation class can occupy the matched-control mode that the finite Nyman equations themselves allow.