# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the paired-coefficient polynomial window for exact omissions

**Linked intuitions:** `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`, `MI-044-finite-exact-omissions-are-triangular-response-columns-not-arbitrary-sparse-increments`, `MI-045-exact-omission-cost-is-a-harmonic-location-profile`, `MI-046-cross-scale-divisibility-not-low-location-drives-exact-omission-amplification`, `MI-047-alternating-rank-merges-create-factorial-incidence-conditioning-without-reaching-the-macroscopic-scale`, `MI-048-ordered-factorization-entropy-caps-exact-omission-conditioning`, `MI-049-parity-dilation-moves-the-exact-omission-frontier-from-support-to-paired-coefficients`, `MI-050-companion-incidence-not-full-support-incidence-controls-isolated-paired-omissions`.

FD-241--FD-247 separate qualitative density-one sampling, approximate residual cost, triangular exact omission columns, harmonic support reach and the primitive-support regime. FD-248 identifies the exact support-side conditioning statistic: for `D=supp(Delta Y)`, the weighted incidence inverse norm `kappa(D)` controls coefficient mass.

FD-249--FD-250 show that divisor merges can make `kappa(D)` large even with subpolynomially many omissions. FD-251 supplies the universal ceiling `kappa(D)<=N^(rho_*-1+o(1))`, where `zeta(rho_*)=2` and `rho_*=1.7286472389...`; therefore all `K=N^(o(1))` exact-omission families remain response-side coercive at the `N^2` coefficient-capacity scale.

FD-252 closes the idea that the special support shape `D subset E union (E+1)` might by itself improve that exponent. Every arbitrary finite divisor support embeds by parity dilation into a genuine exact-omission increment support while preserving its core incidence-Möbius intervals, so support combinatorics alone can be as bad as unrestricted induced divisor supports.

FD-253 shows that this support obstruction can nevertheless be irrelevant to the actual paired coefficient image. For isolated omissions, `Delta Y(e)=Y(e)` and `Delta Y(e+1)=-Y(e)`. If omitted starts do not divide companion locations `C=E+1`, the companion rows close and the inverse cost is controlled by `kappa(C)`, not by `kappa(E union C)`. Large dilations `E=LD`, `L>M`, make `LD+1` an antichain and give coefficient mass `O(H|D|)` even while `kappa(LD union (LD+1))` inherits arbitrarily bad conditioning from `D`.

The live response question is therefore narrower: can a polynomial-size exact-omission family make the **paired** inverse polynomially large by creating substantial companion-side conditioning or by coupling starts back into companion rows? For pure dilations the second mechanism is absent, so a first exact test is simultaneous growth of `kappa(D)` and `kappa(LD+1)` when `L` is not large enough to trivialize the companion poset; the parity case `L=2` is the simplest nontrivial instance. Any claimed amplification must still be compared with the `N/K` scale needed for macroscopic hidden coefficient mass.

The independent source-side question remains whether positivity, finite reservoir capacity, squarefree realization or arithmetic coherence excludes whatever signed paired directions survive. Approximate residual control remains separate from the exact-zero incidence problem.

## Separate support conditioning, paired reachability and source admissibility

Response-space rounding makes bulk integrality cheap once a real reservoir profile is safely inside its capacity box. The remaining discrete obstruction is source admissibility and exact defect geometry.

The exact hierarchy now has three distinct layers. `kappa(D)` prices free coordinates on an active support and is capped by ordered-factorization entropy; the omission map restricts those coordinates to paired/telescoping amplitudes; and FD-253 shows that on isolated families the resulting inverse may be governed by the companion divisibility geometry instead of the worst core support row. A large free-support norm is therefore not evidence of a large exact-omission inverse unless the bad direction is reachable through the paired map. Any source-side theorem must additionally justify positivity and physical arithmetic admissibility.