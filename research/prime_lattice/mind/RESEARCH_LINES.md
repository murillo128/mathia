# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable Prime-Lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Move beyond the completed endpoint state rather than refining its bookkeeping

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-031-the-centered-prime-endpoint-is-a-classical-riesz-zero-spectrum-before-completion`.

PL-338--PL-344 separate activation, raw bounded-block coercivity, essential-edge recurrence, prevalence and canonical completion. The sharp prime-block edges are `+/-e^a` and belong to essential spectrum, but the raw edge event is exponentially rare in long-time density. Bounded modulation nevertheless produces edge-sized raw values because the endpoint weights have a deterministic PNT profile; the zeta-pole term cancels that leading profile. Raw recurrence therefore does not decide the completed problem.

PL-345 identifies the PNT-centered outer endpoint residual with the classical first logarithmic Riesz mean,

`R_a(tau) = -e^(2ia tau) sum_rho e^((2rho-1)a)/(rho+i tau)^2 + O_T(ae^-a)`.

The critical line `Re rho=1/2` is exactly the neutral square-root scale of this expansion, and boundedness at `tau=0` is already equivalent to RH. This was a prior-art redirect rather than a new mechanism, but PL-345 left one genuine bookkeeping question: whether the **full completed Weil form on the same endpoint state** adds an order-one structure not present in the centered outer shell.

PL-346 closes that question decisively. For the normalized endpoint state `u_a`, retaining the pole, all prime sectors, scalar term and archimedean integral gives

`Q_W^a(u_a) = 2 + gamma_E - log(4 pi) - R_a(0) + o(1)`

and hence

`Q_W^a(u_a) = C_zeta + sum_rho e^((2rho-1)a)/rho^2 + o(1)`.

The completed endpoint Rayleigh value is bounded if and only if RH, but this is exactly the classical logarithmic Riesz criterion plus the fixed constant `C_zeta=2 lambda_1`. The previously apparent `O(a)` mismatch came from comparing the pole only with the outer prime shell: the omitted same-end/inner prime sector supplies the missing linear contribution, while the residual archimedean integral tends to zero.

The completed same-state route is therefore exhausted as a source of new endpoint rigidity. More accurate asymptotics for this state can sharpen the representation but cannot create a new RH mechanism unless they expose a quantity not already determined by the classical Riesz residual. A viable continuation must change the observable or state family: for example a genuinely different moving state, a matrix-valued or target-relative family, a noncommutative coupling, or another completed object whose arithmetic content does not scalarize to the same one-dimensional Riesz spectrum.

## Keep universal bulk response distinct from rational-prime residual structure

PL-339--PL-344 use PNT-scale mass, compressed-shift geometry, rational independence, concentration/ergodicity and canonical pole cancellation. Those mechanisms are PNT-universal matched-control phenomena. PL-345 adds rational-prime zero information after centering, but that information is the classical explicit-formula Riesz spectrum. PL-346 shows that full same-state completion does not add a new selective layer: after the inner prime sector is restored, the completed observable remains the same Riesz zero signal plus a fixed constant.

A genuinely new continuation must therefore survive **both** universal PNT subtraction and full completed-state reduction to prior art. It should be rejected early if its exact completed observable can again be written as a classical one-parameter smoothed prime-error criterion with no independent coupling.

## Keep transport, prevalence, centering, explicit-formula identity and completed-state energy distinct

Norm-resolvent continuity transports eigenbranches; the bounded block determines ordinary and essential spectral edges; Haar concentration measures prevalence; PNT asymptotics determine early raw recurrence; pole completion removes that universal profile; the centered residual has a classical zero expansion; and PL-346 now identifies the full completed value for the endpoint state with that same Riesz residual up to a fixed constant and `o(1)`.

The next Prime-Lattice question should therefore begin **after** this collapse. It must explain what extra state/family structure prevents scalar reduction to the classical Riesz criterion and why that extra structure is source-specific and destination-selective rather than another representation of a known RH-equivalent explicit-formula observable.
