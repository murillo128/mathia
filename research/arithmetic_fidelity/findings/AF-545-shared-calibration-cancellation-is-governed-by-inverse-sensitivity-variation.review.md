---
type: adversarial-review
target: research/arithmetic_fidelity/findings/AF-545-shared-calibration-cancellation-is-governed-by-inverse-sensitivity-variation.md
---

# Adversarial review

## Adversary

Equation (9), the **signed** integral of the pairwise inverse-calibration sensitivity, is correct. But the "Target-relative calibration criterion" calls equation (22), the **integral of its absolute value**, the *exact criterion* for accuracy of the final decoded contrast at scale `sigma_A`. This upgrades a sufficient bound to a necessary condition and discards a possible cancellation along the calibration path.

A smooth, globally invertible counterexample uses
\[
G(z,u)=e^{u^2}z,\qquad q(z)=z.
\]
For each small `t>0`, take the true calibration `u_0=-t`, the applied calibration `u=t` (so `epsilon=2t`), and fixed sources `z_1=0,z_2=1`. Here `G_z=e^{u^2}>0` everywhere, with no branch ambiguity. The exact decoder and sensitivity are
\[
\Phi_v(z)=e^{t^2-v^2}z,\qquad K_q(z,v)=-2vz.
\]
Thus the decoded contrast is `C_v=e^{t^2-v^2}`, and **its final error is identically zero**:
\[
C_t-C_{-t}=1-1=0.
\]
Nevertheless the left side of (22) equals
\[
\int_{-t}^t 2|v|e^{t^2-v^2}\,dv
=2(e^{t^2}-1)\sim 2t^2.
\]
With the required fidelity scale `sigma_t=t^3`, the final contrast error is `0=o(sigma_t)`, but the asserted "exact criterion" (22) fails: its left side is not `o(sigma_t)`. The signed sensitivity changes sign and cancels perfectly.

This matters whenever (22) is used to infer a *necessary* calibration precision or to rule out a representation/contrast based on accumulated absolute sensitivity. The source-dependent sensitivity field `K_q=-2uz` is not identically invariant, yet a finite calibration path can return every pairwise contrast exactly to its initial value. No challenge is made here to the differential identities (2)--(9), to the exact invariance criterion for *all* calibration values, or to the local expansion (23) under its explicit small-remainder qualification.

To resolve the objection, distinguish the exact **signed** endpoint condition `|integral Delta K|=o(sigma_A)` from the **sufficient** total-variation condition (22); the latter can be necessary only with additional hypotheses excluding sign cancellation, or for an appropriately strengthened uniform-in-intermediate-calibration demand. Preserve that distinction in the stated target-relative inference and downstream consequences.
