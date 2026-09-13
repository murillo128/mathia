# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Derive completed-Weil BV/derivative-measure compactness from the actual remainder structure

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`.

PL-280--PL-296 separate source-static all-log transport, the universal zero-exterior boundary obstruction, the source-specific sign problem and the failure of an explicit Volterra shortcut. PL-297 shows that the renormalized fractional Hadamard boundary stress can stay finite while the zero extensions diverge in `H^(1/2)`, so the critical Fourier moment is not the correct uniform currency.

PL-298 proves that every fixed positive-order fractional state has enough physical-space regularity for `C^1` translation autocorrelations. PL-299 resolves the singular limit for the **pure principal fractional/logarithmic branch**: uniform convergence plus symmetry/monotonicity gives a uniform BV bound, and a BV convolution lemma yields

`C_s -> C_0 in C^1(R)`

even though `||u_s||_(H^(1/2)) -> infinity`.

PL-300 now closes the generic perturbative transfer from that control branch. There are self-adjoint perturbations of rank at most two with operator norm tending to zero for which the simple isolated ground states still converge uniformly to the pure logarithmic ground state, yet their total variations and a prescribed nonzero-lag autocorrelation derivative diverge. The mechanism is the logarithmic symbol itself: a high-frequency packet costs only `O(log K)` in graph energy but `O(K)` in variation/shift derivative.

Therefore norm-resolvent convergence, a persistent gap, Kato tracking, bounded perturbation size and even uniform `C_0` convergence are insufficient to transport the PL-299 mechanism. The live theorem must use the **specific completed-Weil remainder**: prove a uniform BV mapping/coercive estimate, compactness of derivative measures, a variation-diminishing/order property, or a direct eigen-equation estimate that excludes the high-frequency contamination constructed in PL-300. The pure principal operator is no longer a counterexample, but abstract Hilbert-space perturbation theory is no longer a possible proof.

## Keep the source-specific sign theorem separate

PL-294--PL-295 still show that ordinary Beurling--Deny positivity ends before the first prime translation and that ambient `H^log`/subcritical Sobolev closeness does not protect the sign of the selected ground state. PL-299 is an analytic compactness theorem on a positive monotone control branch; PL-300 shows that even its BV conclusion is not perturbatively stable in generic bounded classes. Neither result transfers order structure to the arithmetic perturbation.

The sign gate therefore continues to require an arithmetic mechanism from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation/maximum principle, absolute-value defect identity or another order structure unavailable to matched generic operators.

## Keep boundary stress, Hilbert-space stability, BV transport and order structure distinct

PL-297 separates stress from the half-Sobolev moment. PL-298 supplies fixed-order physical-space variation. PL-299 shows that uniform BV plus uniform state convergence is enough for the pure singular limit. PL-300 proves that spectral stability and uniform state convergence do not imply that BV currency. None of these resources implies cone membership. Future arguments should state which compactness and which order information are derived from the actual completed-Weil structure instead of substituting generic spectral convergence for the derivative-measure estimate the destination consumes.
