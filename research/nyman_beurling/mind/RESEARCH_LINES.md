# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Prove a uniform hard Ford-window second moment with depth marks and carrier phase intact

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`.

NB-245 separates exact algebraic reconstruction from a uniform observable. NB-246 shows that after freezing the Ford parameters and demodulating the common carrier, the smooth critical current moves with center bandwidth `O(H)` while its pair expansion still resolves the finer `1/X` zero scale and retains the depth marks. NB-247 removes the Schwartz-tail artifact: Bellotti population regularity makes one literal hard `1/H` box sufficient for pointwise control.

NB-248 now fixes the proof interface. The normalized first-order field `R^{-1} zeta'/zeta` has Cauchy poles that are locally `L^p` only for `p<2`; its planar `L^2` norm diverges logarithmically, and a matched `Theta(J)` zero packet leaves no decay after regularization. The hard-window target therefore cannot be obtained by squaring that area integrand and applying black-box Cauchy--Schwarz.

The live theorem remains `sup_t0 H int_{t0-A/H}^{t0+A/H} |R_{t0}(s)|^2 ds = o(1)` for one fixed `A>0`, uniformly over admissible selected centers, but the signed divisor pairing must be performed before squaring, or the argument must work directly with the equivalent two-copy depth-marked carrier energy.

## Keep observability, the missing zero theorem and the singular first-order field separate

The hard-window implication is proved, while the required shrinking-interval second moment for actual zeta zeros is not. NB-248 is a method obstruction, not a counterexample to that second moment: it only excludes local `L^2` control of `zeta'/zeta` before pairing. Macroscopic averages, random-height laws, subcritical absolute `L^p` bounds and estimates that discard the `e^{iX(gamma_j-gamma_k)}` phase still do not supply the missing theorem.