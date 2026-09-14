# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Convert multi-zero geometry into a genuinely finite-section target effect

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`, `MI-011-canonical-deflation-cancels-raw-cauchy-crowding-volume`, `MI-012-three-state-transverse-confluence-exposes-collective-shear`, `MI-013-absolute-height-and-global-zero-counts-are-invisible-to-the-collective-shear-obstruction`, `MI-014-quadratic-horizontal-tangency-is-the-three-state-conditioning-threshold`, `MI-015-confluent-volume-is-curvature-blind-and-controlled-by-radial-depth`, `MI-016-growing-confluent-rank-is-limited-by-endpoint-extrapolation-cost`.

The one-zero route is closed at the scales currently available. NB-111 converts growing confluent rank into exact Laguerre geometry and proves target-poorness whenever `d <= (1/8-epsilon) log G`. NB-112 then uses same-ordinate zeta symmetry together with the Bellotti--Wong zero-counting error to bound the **true** multiplicity of every sufficiently high off-critical zero by `(0.10076+o(1)) log G`, strictly inside that window. Improving the `1/8` constant is therefore not needed merely to eliminate actual one-zero multiplicity.

Distinct zeros do create genuinely new conditioning geometry, but the continuum target audit now sharply separates that geometry from target access. NB-113 proves that every finite common-ordinate packet is exactly orthogonal after canonical deflation, while its Burnol model-space target mass tends to zero. NB-114 removes the common-ordinate restriction on the **target** side: for any finite high packet `F`,

`tau(F)=1-|B_F(1)|^2 <= sum_(rho in F) 1/gamma_rho^2 <= |F|/G^2`.

Thus order-one classical Hardy target mass above height `G` needs `Omega(G^2)` rank. Actual zeta supplies only `O(G log G)` zeros in a fixed-ratio shell, and even pooling the entire positive high-zero tail gives only

`tau_+(G)=O(log G/G) -> 0`.

At the same time NB-098--NB-099 show that relative-ordinate collective shear can remain arbitrarily bad at arbitrarily high absolute ordinate. Hence **large multi-zero shear does not convert into large classical model-space target occupation**. The live zero-state theorem is now finite-section specific: compare a finite target quantity such as `b_N^* G_N^+ b_N` (or a norm-controlled dual certificate) with the continuum Burnol projection and isolate the arithmetic truncation/source term that can either create or fail to create target access. A new high-zero packet, by itself, is no longer enough.

## Keep conditioning, rank supply, continuum target mass and finite arithmetic target access separate

Curvature and collective shear control conditioning; they do not determine target occupation. `L=2a log(B/G)` is a fixed-multiplicity volume depth, `H=2ad log G` is an ambient target-access scale in the one-zero packet, and `T=2(1-a)log(m/r)` is the intrinsic Laguerre depth governing the deterministic `d/T` window. True multiplicity is a source-supply constraint, not another conditioning parameter.

NB-113--NB-114 add another independent currency: the classical Hardy/model-space mass `tau(F)`. It is controlled by the inverse-square ordinate defects of the selected zeros and can vanish even when the canonical transformed Gram is arbitrarily ill-conditioned. Future claims must therefore distinguish at least four questions: how bad the finite state geometry is, how much actual zeta rank is available, how much continuum Burnol target mass that zero packet carries, and whether the finite arithmetic Nyman section produces an additional target-sensitive transfer. None of these quantities is the Nyman distance by itself.