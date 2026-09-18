# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable Prime-Lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Move beyond the completed endpoint state rather than refining its bookkeeping

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-032-complete-endpoint-modulation-gram-is-only-localized-weil-in-coordinates`.

PL-338--PL-344 separate activation, raw bounded-block coercivity, essential-edge recurrence, prevalence and canonical completion. The sharp prime-block edges are `+/-e^a` and belong to essential spectrum, but the raw edge event is exponentially rare in long-time density. Bounded modulation nevertheless produces edge-sized raw values because the endpoint weights have a deterministic PNT profile; the zeta-pole term cancels that leading profile. Raw recurrence therefore does not decide the completed problem.

PL-345 identifies the PNT-centered outer endpoint residual with the classical first logarithmic Riesz mean,

`R_a(tau) = -e^(2ia tau) sum_rho e^((2rho-1)a)/(rho+i tau)^2 + O_T(ae^-a)`.

The critical line `Re rho=1/2` is exactly the neutral square-root scale of this expansion, and boundedness at `tau=0` is already equivalent to RH. PL-346 then closes the full same-state completion:

`Q_W^a(u_a) = 2 + gamma_E - log(4 pi) - R_a(0) + o(1)`.

The completed endpoint Rayleigh value is exactly the classical logarithmic Riesz criterion plus the fixed constant `2 lambda_1`; the previously apparent `O(a)` mismatch came from omitting the same-end/inner prime sector, not from a new archimedean mechanism.

PL-347 now closes the most direct matrix-valued continuation. Fixing an aperture `A`, the modulated states `u_(A,k)(x)=e^(i pi k x/A)u_A(x)` retain genuine prime phases in their off-diagonal entries. However, the endpoint envelope is a bounded invertible multiplier on `(-A,A)`, the Fourier modulations are complete there, and their span is a **form core** for the localized completed Weil form. Consequently the full Gram matrix

`K_A(k,l)=Q_W^A(u_(A,k),u_(A,l))`

is positive on every finite index set if and only if the entire localized Weil form is nonnegative. Requiring this for every `A>0` is exactly Weil positivity/RH.

Thus the two natural extremes of the same endpoint family are now classified. One diagonal channel is the classical Riesz residual; the complete cross-modulation family reconstructs the full classical localized Weil problem. Adding all modulations does recover strictly more information than one scalar channel, but the extra information is exactly what ordinary Fourier completeness already supplies to the pre-existing form.

The live question is therefore an **intermediate sufficiency problem**, not a request for more coordinates. Is there a sparse or source-forced modulation/state family whose span is not automatically a form core, yet whose positivity or coupled relations still force the desired zero restriction? Such a result must explain why the restricted family is arithmetically sufficient. A proposal should be rejected if scalar completion reduces it to the Riesz criterion or if polarization plus density merely reconstructs the whole localized Weil form.

## Keep universal bulk response distinct from rational-prime residual structure

PL-339--PL-344 use PNT-scale mass, compressed-shift geometry, rational independence, concentration/ergodicity and canonical pole cancellation. Those mechanisms are PNT-universal matched-control phenomena. PL-345 adds rational-prime zero information after centering, but that information is the classical explicit-formula Riesz spectrum. PL-346 shows that full same-state completion does not add a new selective layer. PL-347 shows that restoring all cross-modulations adds the whole known localized Weil form rather than a new prime-lattice constraint.

A genuinely new continuation must therefore survive **both** universal PNT subtraction and the two classical closure limits of the endpoint family. It should not scalarize to one Riesz channel, and it should not become equivalent by density to the full Weil form. The missing object, if any, must be a source-defined restricted coupling, noncommutative relation or sufficiency theorem that is not invariant under arbitrary replacement by another complete frame.

## Keep transport, prevalence, centering, explicit-formula identity and completed-family closure distinct

Norm-resolvent continuity transports eigenbranches; the bounded block determines ordinary and essential spectral edges; Haar concentration measures prevalence; PNT asymptotics determine early raw recurrence; pole completion removes that universal profile; the centered residual has a classical zero expansion; PL-346 identifies the full completed value for one endpoint state with that same Riesz residual; and PL-347 identifies the complete modulation Gram family with the full localized Weil form.

The next Prime-Lattice question begins between the last two objects. It must identify a restricted family or coupling whose information content is genuinely intermediate between one classical Riesz observable and a complete coordinate reconstruction of known Weil positivity, and prove why arithmetic forces that intermediate structure to be destination-selective.
