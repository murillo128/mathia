# MI-040 — Wang's cutoff-free dyadic-shell transfer now loses only a squared logarithm

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-314](../../findings/VIS-314-selberg-prime-pair-sieve-wang-shell-log-square.md), using Wang's localization identities, separated-frequency mean-value bounds and the classical Selberg upper-bound sieve.

The upper pointwise boundary in Wang's short-interval pair statistic has moved repeatedly because generic estimates were applied before the load-bearing coefficient/frequency structure was exposed. VIS-298 removes the lower moving-source crossover; VIS-305--VIS-309 show through matched support/phase controls and the actual prime-log orbit that generic cross-prime alignment is not the missing mechanism.

VIS-310--VIS-312 then show that finite-window transfer cannot be organized by a hard cutoff plus one global or nearest-neighbour frequency gap: the full supported cross-base ratio spectrum is dense, so individual isolation has no cutoff-free limit.

VIS-313 replaces it by a fixed near/far ratio split followed by dyadic arithmetic-height shells. Near-shell reduced ratios have separation `delta_M>>M^(-2)`, while the Wang taper makes shell energies summable. The resulting cutoff-free estimate was

`V^(-1) int |R(T)|^2 dT << x^2 + x log^3 x + x^3 log^3 x/V`.

VIS-314 identifies one logarithm in that bound as a proof artifact. The earlier shell energy estimate paid independent pointwise von-Mangoldt majorants. Retaining the actual two-prime sparsity and applying the classical Selberg upper-bound sieve gives

`E_M << M v_x(M)^4 log^2(4M)`,

including proper prime powers as lower-order terms. Replaying the shell argument yields

`V^(-1) int |R(T)|^2 dT << x^2 + x log^2 x + x^3 log^2 x/V`.

At `H~x log log x`, deterministic finite-window mean square is therefore `o(H^2)` once

`V >> x log^2 x/(log log x)^2`.

The representation lesson is now sharper: dense spectrum is not the obstruction, and one logarithm of the residual finite-height cost was merely the price of forgetting pair sparsity inside each arithmetic shell. The remaining gap to the natural local window `V~H~x log log x` is roughly `log^2 x/(log log x)^3`.

A further advance should test whether that residual factor is another aggregation/large-sieve loss or a real exceptional-height phenomenon. Useful targets are sharper weighted prime-pair shell energy, cancellation between shells, a coupling of near and far bands, or a source-faithful near-resonant packet proving a lower bound. Returning to pointwise global gaps or finite support truncations cannot answer that question.

**Boundary.** VIS-314 is a sufficient mean-square-in-starting-height improvement based on a classical upper-bound sieve. It gives no prime-pair asymptotic, pointwise cancellation at every height, moving-`x(T)` joint-limit theorem or proof that the remaining logarithmic factor is intrinsic.
