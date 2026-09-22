# MI-069 — Dilute carrier floors are collective and sparse-defect blind

**Evidence level:** exact RH-independent response bound from [WI-392](../../findings/WI-392-dilute-source-exact-carriers-are-sparse-packet-blind-at-the-moving-frequency.md), refining the RH-conditional positive-floor mechanism of MI-068.

The WI-391 dilute carrier can produce an order-one sampled contribution under RH only collectively. Its `L^2` mass near frequency `R` is `epsilon_R=c/log R`, so one complex Fourier evaluation near the carrier has only `O(sqrt(epsilon_R))` amplitude. The `Theta(log R)` critical-line zeros in a fixed-width packet can accumulate those small contributions into the positive floor of MI-068, but one selected zero does not receive order-one weight.

For an off-critical zero `rho=1/2+delta+i gamma` with `|gamma-R|<=Delta`, WI-392 gives the absolute bound

`|T_rho(f_(A,R))| << e^(A|delta|) (1/log R + e^(-A)/A^2 + R^(-2M))`.

Uniformly in the critical strip this is bounded by

`q(A,R)=e^(A/2)/log R + e^(-A/2)/A^2 + e^(A/2)R^(-2M)`,

and the WI-391 scale `A=o(log log R)` forces `q(A,R)->0`. Therefore an off-line packet of total multiplicity `M_off` satisfying `M_off q(A,R)->0` is asymptotically invisible at order-one scale to the same moving-frequency channel. For the explicit choice `R=exp(exp(A^2))`, the sufficient sparse regime is `M_off=o(A^2 e^(A/2))`.

This separates two notions that the RH-side construction alone did not distinguish: **collective sampled floor** and **sparse defect sensitivity**. Escaping logarithmic spectral compactness can defeat the recurrent no-gap mechanism, but the dilution that makes the escape affordable also weakens each individual moving-frequency defect. The same scalar carrier cannot be assumed to provide a converse/coercive RH criterion merely because it has a positive floor when all zeros are on the line.

A reverse implication therefore needs an additional mechanism: enough aggregate off-line density in the moving packet, a different channel whose response grows with horizontal displacement, a multiscale family that does not dilute every sparse defect, or use of the fuller Weil form rather than this one anisotropic scalar sequence. Which of those can remain source-exact and quantitatively controlled is a separate question.

**Boundary.** WI-392 does not show that the complete Weil form is blind to finite or sparse RH failures, does not bound off-line zeros outside the moving packet, and does not suppress the fixed base profile's response to a bounded-ordinate off-line zero. The result concerns only the moving dilute-carrier mechanism that creates the WI-391 RH-side floor.