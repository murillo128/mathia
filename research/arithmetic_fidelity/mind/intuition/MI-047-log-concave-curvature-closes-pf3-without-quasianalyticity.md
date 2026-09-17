# MI-047 — Log-concave curvature closes `PF_3` recognition without quasianalyticity

**Evidence level:** exact synthesis from [AF-385](../../findings/AF-385-sampled-solid-minor-hierarchy-certifies-continuum-fixed-order-total-nonnegativity.md), [AF-389](../../findings/AF-389-multiscale-solid-pf3-excludes-all-finite-order-boundary-contact.md), [AF-390](../../findings/AF-390-quasianalytic-curvature-closes-multiscale-pf3-recognition.md), and [AF-391](../../findings/AF-391-log-concave-logarithmic-curvature-forces-order-three-total-nonnegativity.md).

For a positive smooth profile `f`, write `q=-(log f)''`. AF-389 shows that shrinking-mesh solid `PF_2/PF_3` consistency forces `q>=0` and makes every zero of `q` infinitely flat. AF-390 then closes the residual boundary whenever the admissible source class has flat-zero unique continuation for `q`.

AF-391 identifies a different closure mechanism. If `q` is nonnegative and log-concave in the extended sense, the order-three placement ratio needed to move from solid to arbitrary Toeplitz minors is monotone. Consequently the translation kernel `K_f(x,y)=f(x-y)` is continuum `TN_3`; when `q` is smooth and strictly positive, increasing coordinates give strict `TP_3`.

The important point is that **quasianalyticity is sufficient but not necessary**. AF-391 includes an explicit curvature profile

`q(x)=0` for `x<=0`, and `q(x)=exp(-1/x)` for `x>0`,

which is nonquasianalytic and infinitely flat at the boundary but still log-concave. Its translation kernel is therefore `TN_3`. An infinitely-flat zero is not itself the obstruction left by AF-389; the residual defect requires additional shape freedom that breaks the log-concave curvature mechanism.

This changes the source-class audit. The multiscale certificate has already recovered the complete finite jet at any boundary zero. One can close the remaining fibre either by a category theorem that says a flat jet determines the curvature globally, as in AF-390, or by a shape theorem that makes every allowed placement minor positive despite that flat zero, as in AF-391. These are logically different resources and should not be conflated.

The next boundary is therefore narrower: construct or rule out a smooth nonnegative curvature `q` with an infinitely-flat zero that is both nonquasianalytic and non-log-concave, satisfies the full shrinking solid hierarchy, yet leaves a negative gapped continuum `3x3` minor. Any weaker source-derived shape condition that excludes that residual fibre would improve the recognition theorem without requiring full quasianalytic rigidity.

**Boundary.** AF-391 does not derive log-concavity of `q` from any Riemann-associated source and does not show that log-concavity is necessary for `TN_3`. It only proves that a broad nonquasianalytic flat-zero class is already harmless. The arithmetic problem remains to obtain the required solid signs or curvature restriction from genuine source information, and none of these recognition statements supplies an RH zero-selection theorem.