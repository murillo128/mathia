# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Control the nested depth-phase carrier at subcritical Ford exponential type

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-061-ford-damping-is-the-laplace-dual-of-nested-depth-phase`.

NB-218--NB-224 isolate the exact source-side carrier. Keeping source and Mellin kernel coupled removes artificial primitive tariffs; generic strip analyticity is sharp for the ambient class; the actual zeta singularity spectrum plus Bellotti density reaches almost to Ford height; and a proportional logarithmic source shell narrows the vertical carrier enough to reach the exact Ford denominator.

NB-225 proves that the linear shell width is the sharp transition for the current population-only mechanism. Every genuinely sublinear `H=o(R)` permits an abstract near-one packet compatible with the zero-free, density and local-count inputs while retaining an order-one moving-shell contribution. NB-226 shows that unweighted fixed-power phase cancellation does not repair this, and NB-227 closes every separable strengthening of the form `M^vartheta/Q(D)`: the packet can move to a slowly growing depth where horizontal Ford damping exactly compensates the permitted phase bias.

NB-228 identifies the nonseparable object that the residue actually consumes. With normalized zero depth `d_rho=R(1-beta)`, Ford ratio `Y=X/R`, and the full shell coefficient retained in `b_rho`, define the nested cumulative depth-phase carrier

`C(D)=sum_(d_rho<=D) b_rho`.

Stieltjes/Abel summation gives the exact source-faithful relation

`Z_(X,H)(t)=e^(-r) Y int_0^R e^(-YD) C(D) dD + o(1)`.

Thus Ford damping is the Laplace dual of **one cumulative process across all horizontal depth slabs**, not a collection of independently priced phase estimates. If the tail cumulative carrier has exponential type at most `(1-delta)Y`, its deep residue contribution decays like `e^(-delta Y D_0)`. Conversely the matched controls of NB-225--NB-227 sit exactly at the critical type `e^(YD)` and retain order-one residue mass.

The live source theorem is therefore precise: prove a zeta-specific bound making the nested cumulative carrier subcritical relative to `e^(YD)` on the exact-Ford scale, or show that actual zeta zeros can attain critical type. A population bound, a per-depth phase estimate, or an arbitrarily strong depth-only multiplier does not address this interface unless it implies the required cumulative Laplace bound.

## Keep source width, cumulative depth phase and Ford damping in one ledger

The relevant currencies include logarithmic source width `H`, carrier width `1/H`, normalized horizontal depth `D`, the full profiled coefficient `b_rho`, the cumulative process `C(D)`, the damping `e^(-YD)` and the residue norm consumed by the destination. NB-228 explains exactly how they combine: the residue is an exponentially weighted integral of `C(D)`.

This is stronger bookkeeping than optimizing population, depth and phase separately. The matched packet no longer has an independent population power to retune once a subcritical cumulative exponent is known. At the same time, the Abel identity is generic and therefore not itself new zeta information. The missing theorem must be source-specific and independent enough not to recover the same Euler shell by a circular explicit-formula substitution.

The classical Landau--Gonek family is neighboring prior art for sums of `x^rho`, but the live object is vertically localized by the shell profile and truncated cumulatively by horizontal depth. A future result should state exactly which source theorem controls that joint object and how much exponent below `Y` it gains.

This remains source-side information. The matched packets are logical controls compatible with the audited zero information, not constructions of actual zeta zeros, and NB-228 does not itself give a quantitative Nyman--Beurling distance theorem. Any destination claim must preserve that bridge explicitly.
