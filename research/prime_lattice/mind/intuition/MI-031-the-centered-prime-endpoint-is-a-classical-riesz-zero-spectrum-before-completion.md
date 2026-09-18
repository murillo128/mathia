# MI-031 — The completed Prime-Lattice endpoint collapses to the classical logarithmic Riesz residual

**Evidence level:** literature-backed exact synthesis from [PL-344](../../findings/PL-344-bounded-modulation-pnt-edge-cancelled-by-pole.md), [PL-345](../../findings/PL-345-schur-endpoint-log-riesz-zero-spectrum.md), and [PL-346](../../findings/PL-346-completed-endpoint-riesz-collapse.md). The explicit-formula/Riesz mechanism is classical; the Mathia content is its exact realization by the localized endpoint state after full same-state Weil completion.

PL-345 identifies the PNT-centered outer prime response with the classical first logarithmic Riesz mean. At zero modulation,

`R_a(0) = - sum_rho e^((2rho-1)a)/rho^2 + O(ae^-a)`,

so a zero `rho` is weighted by `e^((2 Re rho-1)a)`. The critical line is exactly the neutral square-root scale, and boundedness of `R_a(0)` is already equivalent to RH.

PL-346 resolves the remaining completion question for the same normalized endpoint state `u_a`. Keeping the pole, **all** prime sectors, scalar term and archimedean integral gives

`Q_W^a(u_a) = 2 + gamma_E - log(4 pi) - R_a(0) + o(1)`

and equivalently

`Q_W^a(u_a) = C_zeta + sum_rho e^((2rho-1)a)/rho^2 + o(1)`,

with `C_zeta=2+gamma_E-log(4 pi)=2 lambda_1`. Hence boundedness of this completed endpoint Rayleigh value is equivalent to RH, but it is exactly the same classical Riesz criterion plus a fixed Li-coefficient constant.

The apparent `O(a)` completion mismatch left by PL-345 was bookkeeping rather than new spectral structure. Comparing the pole only with the **outer** prime shell omitted the same-end/inner prime sector. Restoring those primes cancels the missing linear scale; the residual archimedean integral is only `o(1)` and does not supply a new order-one mechanism.

The reusable lesson is that exact completion can close a representation gap without creating new coercivity. A localized state may package a classical RH-equivalent explicit-formula residual into one completed Weil quadratic value, yet the completion contributes no independent zero-selecting law. Before treating a new endpoint state as a mechanism, reduce the **full same-state observable**, including all prime sectors and completion terms, and compare it with known smoothed explicit-formula criteria.

The specific endpoint-state route is therefore exhausted as a source of new rigidity. A continuation must change more than bookkeeping: use a genuinely different moving state, matrix/family coupling, target-relative interaction, noncommutative observable, or another structure whose completed value does not reduce to this classical Riesz residual.

**Boundary.** This does not weaken the exact RH equivalence of the completed endpoint value. It says that equivalence is not new: PL-346 identifies it with a classical logarithmic Riesz criterion. The negative conclusion applies to this one endpoint Rayleigh state and does not rule out richer families of states or observables.