# MI-046 — Exact dephasing needs matched-filter-scale variation away from every common input

**Evidence level:** exact finite-endpoint synthesis from [MC-331](../../findings/MC-331-common-coefficient-prefilters-cannot-cross-quartic-horizon.md) through [MC-334](../../findings/MC-334-exact-dephasing-requires-matched-filter-scale-mode-variation.md).

MC-331 and MC-332 are opposite endpoints of one coefficient geometry. If every mode uses one common prime vector, the endpoint theorem cannot cross the quartic balance. If every mode may choose its own row, the conjugate-character matched filter erases the endpoint phase exactly. MC-333 shows that exact dephasing with a common rowspace of dimension `d` requires a joint rank--Frobenius-energy budget; low rank by itself is not protective because the dangerous evaluation matrix already has rank `R`.

MC-334 identifies an independent resource: how far the mode rows must actually separate from **any** common input. For the endpoint character matrix `B` with `A` shell-prime columns and target amplitudes `c`, define

`V(W) = min_u sum_a ||w_a-u||_2^2`.

Among all exact dephasers satisfying `T_W(a)=A c_a`,

`inf V(W) = A dist(c,col B)^2`.

This is an exact projection identity. The common center can explain precisely the component of the target lying in `col B`; every orthogonal target component has to be supplied by genuinely mode-varying row corrections.

For the spread target `c=1` on the `m=2^R-1` nonprincipal modes,

`dist(1,col B)^2 = m - R/(2^R-R)`.

Hence

`inf V(W) = A(m - R/(2^R-R)) = (1-o(1))Am`.

The direct matched filter `W=B` has `V(B)=A(m-1/m)`, differing from the optimum by only an exponentially tiny relative amount. Thus exact all-mode phase erasure cannot be implemented as a small mode-dependent perturbation of one common prime filter: almost the full matched-filter quadratic scale must appear specifically in cross-mode variation.

The same conclusion is stable under approximate dephasing. If the normalized output is `c+e`, then

`V(W) >= A (dist(c,col B)-||e||_2)_+^2`.

For `c=1`, an architecture with `V(W)<=theta Am` has an order-one lower bound on normalized family RMS error unless `theta` is itself close to one. In particular `V(W)=o(Am)` cannot hide a good all-mode dephaser inside a large common component plus small row corrections.

This separates three coefficient currencies that should not be conflated: shared rowspace dimension, total Frobenius energy, and centered cross-mode variation. MC-333 prices how efficiently a low-dimensional common rowspace can interpolate many target amplitudes; MC-334 prices how much of the target cannot be explained by **any single common input**. A source-natural class can pass one gate and fail the other.

For the live Möbius route, the right admission test is therefore not nominal rank or descriptive complexity. State the admissible prime--mode class, compute or bound its distance from the common-input subspace and from the conjugate-character geometry in the norm used by the analytic theorem, and only then ask whether the class carries arithmetic leverage beyond the quartic endpoint.

**Boundary.** The exact formulas use the finite reciprocal endpoint, equal one-defect cell populations and family `L^2`/Frobenius geometry. Sparse amplitudes, unequal cells, supremum-norm objectives or nonlinear statistics can have different capacity laws. The result is an endpoint admission theorem, not a bound for `M(x)` and not an RH consequence.
