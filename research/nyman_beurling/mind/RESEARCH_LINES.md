# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Prove a uniform hard Ford-window second moment with depth marks and carrier phase intact

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`.

NB-245 separates exact algebraic reconstruction from a uniform observable. NB-246 then shows that after freezing the Ford parameters and demodulating the common carrier, the smooth critical current moves with center bandwidth `O(H)` while its pair expansion still resolves the finer `1/X` zero scale and retains the depth marks.

NB-247 removes the remaining Schwartz-tail artifact. Bellotti's weighted near-one population law gives uniform Lipschitz control of the demodulated current on the scaled center variable, so an order-one selected value persists across a fixed fraction of a Ford window. Consequently it is enough to prove

`sup_t0 H int_{t0-A/H}^{t0+A/H} |R_{t0}(s)|^2 ds = o(1)`

for one fixed `A>0`, uniformly over admissible selected centers. The hard box is now source-faithful; the matched coherent packet still has nonvanishing box energy, so success requires arithmetic zero geometry rather than dilution by averaging.

## Keep observability and the missing zero theorem separate

The hard-window implication is proved, but the required shrinking-interval second moment for the actual depth-marked zeta-zero current is not. Macroscopic height averages, random-height laws and estimates that discard the `e^{iX(gamma_j-gamma_k)}` phase do not supply it. The remaining analytic target is precisely the uniform Ford-scale box energy with frozen parameters, depth marks and carrier phase intact.