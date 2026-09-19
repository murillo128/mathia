# MI-050 — Full localized Weil energy turns any RH failure into a finite-radius first crossing

**Evidence level:** `WI-355` synthesis from Suzuki's localized Weil-form theorem plus exact variational monotonicity.

For the localized Weil form on `(-a,a)`, let

`lambda(a)=inf_(v!=0) Q_W(v)/||v||_2^2`.

Suzuki's framework identifies this as the lowest eigenvalue of a localized self-adjoint Weil operator, proves continuity in `a`, positivity for sufficiently small `a`, and that failure of RH is equivalent to `lambda(a)<0` for some finite radius.

The nested variational domains add a simple but decisive exact fact: if `a<b`, every test function supported in `(-a,a)` is also admissible in `(-b,b)`, hence

`lambda(b)<=lambda(a)`.

Therefore under `not RH` there is a canonical first radius

`a_*=inf{a: lambda(a)<=0}`

with `0<a_*<infinity` and `lambda(a_*)=0`. Because the localized operator has discrete lower-bounded spectrum, zero is then an actual ground-state eigenvalue rather than a defect visible only through a cofinal limiting sequence.

This changes the sparse-defect ledger. A normalized pair-correlation statistic can make finitely many or zero-density off-line zeros asymptotically invisible, but the **full localized quadratic form cannot hide every RH failure in that way**: some finite radius must lose coercivity. At radius `a`, the arithmetic kernel uses only prime powers up to `e^(2a)`, so the hypothetical failure has finite arithmetic support data even though the operator problem remains infinite-dimensional.

The reusable distinction is between localization that compresses and normalizes away sparse defects and localization that retains a monotone variational ground energy. The RH-facing source problem becomes: prove strict positivity of the localized ground energy for every finite radius, or find a propagation principle that prevents its first zero crossing as new prime-power thresholds enter.

**Boundary.** Finite prime-power input does not make the localized operator finite-dimensional or automatically decidable. This intuition does not give an effective bound on a hypothetical `a_*`, does not invalidate `WI-354` for pair correlation, and does not prove the required coercivity. It identifies a stronger defect-sensitive interface and the exact first-crossing event that RH would forbid.
