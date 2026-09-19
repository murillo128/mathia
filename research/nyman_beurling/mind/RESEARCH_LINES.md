# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Control the nested depth-phase carrier only inside the carrier-width Ford window

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-061-ford-damping-is-the-laplace-dual-of-nested-depth-phase`.

NB-218--NB-224 isolate the exact source-side carrier. Keeping source and Mellin kernel coupled removes artificial primitive tariffs; generic strip analyticity is sharp for the ambient class; the actual zeta singularity spectrum plus Bellotti density reaches almost to Ford height; and a proportional logarithmic source shell narrows the vertical carrier enough to reach the exact Ford denominator.

NB-225--NB-227 show why population, phase and depth cannot be optimized separately. Every genuinely sublinear shell admits matched packets compatible with the audited zero information, fixed-power phase cancellation does not remove them, and every separable `M^vartheta/Q(D)` repair can be defeated by moving to a slowly growing depth where Ford damping compensates the permitted phase bias.

NB-228 identifies the nonseparable object consumed by the residue. With normalized zero depth `d_rho=R(1-beta)`, Ford ratio `Y=X/R`, full shell coefficient `b_rho`, and cumulative carrier

`C(D)=sum_(d_rho<=D) b_rho`,

Stieltjes/Abel summation makes the residue the Laplace-weighted integral of `C(D)` against `e^(-YD)`.

NB-229 first removes the deep formal Ford range. NB-230 then keeps carrier width visible: with `J=1+R/H`, Bellotti's local count gives `M_(t,H)(D) << D+J`, hence an integrated tail `T(D_0,D_1) << e^(-YD_0)(D_0+J+1)`. Every moving depth with `YD_0-log J -> +infinity` is therefore absolutely harmless in the audited range.

NB-231 shows that the remaining transition is sharp for the same information set when `1 << R/H <= log Q`. A phase-aligned packet using a fixed positive fraction of the `J` carrier slots at `YD=log J+O(1)` can carry order-one Ford residue while respecting all population inputs used so far. The open source theorem must therefore attack the bounded transition layer itself rather than improve already-subcritical depths.

NB-232 now removes **global Montgomery-type pair correlation** as that missing input. The carrier packet spacing is `Theta(1/X)`, while the mean zeta-zero spacing is `Theta(1/Q)`, so one selected packet point is separated from the next by `Q/X -> infinity` mean spacings. The packet is mesoscopic, not a close-spacing anomaly. More strongly, inserting only

`A(T)=O(sqrt(log T) log log T)`

such packet ordinates below height `T` changes the usual weighted pair-correlation numerator by at most `O(A(T)log T+A(T)^2)=o(T log T)`, uniformly in the Fourier parameter, while infinitely many selected packets can still carry order-one residue at their own heights. Thus even a complete global pair-correlation asymptotic can be blind to the exceptional transition packets relevant to a uniform endpoint theorem.

The missing observable is now sharper: it must be **local, depth-conditioned and carrier-frequency sensitive**. Schematically it must control the shallow-zero sum in the actual `1/H` window with phase `e^(iX(gamma-t))` while `YD-log(1+R/H)=O(1)`. Natural `1/Q` gap repulsion is too fine for the carrier spacing, and globally normalized two-point statistics average away a packet family sparse enough to matter pointwise.

## Keep source width, cumulative depth phase, carrier capacity and local exceptional quantifiers in one ledger

The relevant currencies are source width `H`, vertical capacity `J=1+R/H`, normalized horizontal depth `D`, the full profiled coefficient `b_rho`, cumulative signed carrier `C(D)`, Ford damping `e^(-YD)`, carrier frequency `X`, and the **uniform-in-height** quantifier required by the endpoint. NB-230 converts linear capacity `J` into a logarithmic depth budget; NB-231 shows that this conversion is sharp for the audited information; NB-232 shows that an exceptional set invisible to global statistics can still saturate the pointwise transition at infinitely many heights.

A useful next zeta theorem must therefore condition the vertical statistic on horizontal depth and resolve the carrier phase on each relevant short window, or obtain an equivalent arithmetic restriction from the explicit formula without averaging away the exceptional heights. Stronger global density-one or pair-correlation information is not enough unless it yields that local conditioned control.

The destination bridge is unchanged. These source-side residue estimates do not themselves prove a quantitative Nyman--Beurling distance bound; a successful destination argument must still force an approximant to realize the positive Euler return tested by this carrier rather than merely control an abstract zero sum.