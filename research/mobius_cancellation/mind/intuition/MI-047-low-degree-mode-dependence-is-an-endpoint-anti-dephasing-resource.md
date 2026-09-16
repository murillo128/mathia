# MI-047 — Low-degree endpoint mode dependence is anti-dephasing only in coordinates that cannot read their own source phase

**Evidence level:** exact finite-endpoint synthesis from [MC-332](../../findings/MC-332-arbitrary-mode-dependent-prime-rows-exactly-dephase-the-reciprocal-endpoint.md) through [MC-336](../../findings/MC-336-source-coordinate-degree-needs-self-phase-exclusion.md).

MC-332 shows that arbitrary dependence of prime coefficients on the endpoint mode is too expressive: the conjugate-character matched filter erases the phase exactly, even though its evaluation matrix has rank only `R`. MC-333--MC-334 then show that rank, total Frobenius energy and centered variation are separate currencies.

MC-335 adds Fourier degree in the **standard endpoint mode bits**. If every prime-coordinate function extends to a Walsh polynomial of degree at most `d`, multiplication by the one-defect character geometry restricts the reachable output frequencies. For `1<=d<=R-2` the best approximation error to uniform all-mode dephasing is explicit; when `d=o(R)` the normalized family RMS error tends to the full target scale. In those coordinates, genuinely low degree is a real anti-programmability resource.

MC-336 identifies the hidden coordinate dependence. Reparameterize the mode by the source phases `x_i(a)=(-1)^(a·s_i)`. The matched filter is then degree one: a coefficient at source cell `i` can simply read `x_i` and cancel that same phase locally. Low polynomial degree by itself is therefore not an invariant complexity bound. A nonlinear coordinate change that exposes the target phase can turn an apparently hard matched filter into a linear observable.

The exact repair at the reciprocal endpoint is **self-phase exclusion**. If the coefficient assigned to source cell `i` may depend on the other source phases but not on `x_i` itself, and that dependence has source-coordinate degree at most `d`, the reachable output space is exactly the span of nonconstant source monomials of degrees `1,...,d+1`. The missing high-degree tail has dimension

`q_d=sum_(k=d+2)^R binom(R,k)`,

and the optimal punctured-cube all-mode dephasing error is

`N q_d/(q_d+1)`

in the finding's normalization. Thus `d=o(R)` again leaves asymptotically full RMS error, while exact dephasing first appears only at `d=R-1`.

The durable resource is consequently not “low degree” in isolation but **low degree plus an information-flow restriction that prevents each output coefficient from observing/reconstructing the phase it is meant to cancel**. This survives the natural source-coordinate reparameterization and distinguishes a structured class from a coordinate artifact.

Rank, energy, variation, degree and self-phase access remain independent. A class can be low rank but contain the matched filter; low degree in a target-exposing coordinate can be fully programmable; and self-phase exclusion can rule out exact cancellation even when the remaining cross-phase dependence is rich. Any analytic theorem must charge restrictions in the same source-relative representation in which programmability is tested.

**Boundary.** MC-336 is exact for the finite reciprocal endpoint and its source-phase character geometry. It does not show that a useful arithmetic coefficient family satisfies self-phase exclusion, and allowing reconstruction of `x_i` indirectly through additional side information could reopen the loophole. Different mode sets, nonlinear output statistics or analytic norms require a separate capacity calculation. Nothing here bounds `M(x)` or proves RH.