# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the hard Ford-window second moment after the positive-frequency Hardy projection

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`.

NB-245--NB-247 reduce the observable to one literal hard `1/H` Ford box while preserving the depth marks and carrier phase. NB-248 shows why the first-order area field cannot be squared directly: every zero produces a Cauchy pole at the planar `L^2` endpoint, and a carrier-compatible `Theta(J)` packet leaves an order-one obstruction after regularization.

NB-249 now identifies the canonical admissible operation before squaring. Resolving the smooth Mellin shell into its positive Fourier frequencies turns the Ford-scaled Cauchy kernel into a one-sided Hardy projection. It selects only the shallower depth edge `d<d_rho`; the projection exponential cancels the Ford depth factors exactly, and the cumulative edge integral recovers `chi(d_rho)`. The pole field is therefore first converted back into the finite marked zero current, with its original carrier and depth coefficient, and only that finite current may enter a Hilbert-space or second-moment step.

The required theorem is a uniform `o(1)` hard-window second moment for the resulting depth-marked carrier (equivalently its two-copy pair energy) over admissible selected centers. The matched coherent packets survive the Hardy projection, so the projection fixes the representation/order-of-operations problem but supplies no decay by itself.

## Keep the exact projection identity and the missing zero theorem separate

The hard-window implication is proved, and NB-249 gives an exact way to perform the signed divisor/Cauchy pairing without a planar `L^2` singularity. Neither result proves the required shrinking-interval second moment for actual zeta zeros. A future argument must estimate the projected finite zero current while retaining `e^{iX(gamma_j-gamma_k)}` and the horizontal depth marks; returning to absolute local bounds for `zeta'/zeta`, subcritical `L^p`, macroscopic averages, or statistics that discard the carrier phase loses the interface that NB-249 makes exact.
