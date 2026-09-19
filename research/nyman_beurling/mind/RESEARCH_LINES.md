# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Control the nested depth-phase carrier only on the shallow exact-Ford layer that survives smooth localization

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-061-ford-damping-is-the-laplace-dual-of-nested-depth-phase`.

NB-218--NB-224 isolate the exact source-side carrier. Keeping source and Mellin kernel coupled removes artificial primitive tariffs; generic strip analyticity is sharp for the ambient class; the actual zeta singularity spectrum plus Bellotti density reaches almost to Ford height; and a proportional logarithmic source shell narrows the vertical carrier enough to reach the exact Ford denominator.

NB-225 proves that the linear shell width is the sharp transition for the current population-only mechanism. Every genuinely sublinear `H=o(R)` permits an abstract near-one packet compatible with the zero-free, density and local-count inputs while retaining an order-one moving-shell contribution. NB-226 shows that unweighted fixed-power phase cancellation does not repair this, and NB-227 closes every separable strengthening of the form `M^vartheta/Q(D)`: the packet can move to a slowly growing depth where horizontal Ford damping exactly compensates the permitted phase bias.

NB-228 identifies the nonseparable object that the residue actually consumes. With normalized zero depth `d_rho=R(1-beta)`, Ford ratio `Y=X/R`, and the full shell coefficient retained in `b_rho`, define the nested cumulative depth-phase carrier

`C(D)=sum_(d_rho<=D) b_rho`.

Stieltjes/Abel summation gives the exact source-faithful relation

`Z_(X,H)(t)=e^(-r) Y int_0^R e^(-YD) C(D) dD + o(1)`.

NB-229 then removes most of the apparent depth interval before any zero-density or phase-cancellation theorem is used. Smooth vertical carrier decay plus the classical local zero count gives the absolute budget

`sum_rho m(rho)|F(Hv_rho)| << Q`,

and therefore the tail bound

`|Z_(d>=D_0)| << Q e^(-Y D_0)`.

With `L=log Q`, depths beyond `(L+omega(1))/Y` are already `o(1)`, and `(1+delta)L/Y` gives `O(Q^(-delta))`. The full Ford interval `0<=D<=R` is therefore vastly larger than the actual dangerous layer. The surviving source problem lives at **shallow moving depth `D=O(L)`**, with the hardest unresolved range `1<<D<<L`.

The prior-art audit sharpens the missing theorem rather than solving it. Classical `eta^(3/2)` zero-density shapes have the right Ford exponent but their published logarithmic/fixed-parameter losses dominate when `D=o(L)`; log-free linear-`eta` forms remove that loss but have the wrong Ford exponent. The useful next input is therefore a local, carrier-weighted or phase-sensitive estimate uniform for `eta=D/R` in `1<<D<<L`, or a direct bound for `C(D)` there. A theorem over the full Ford depth is unnecessarily broad.

## Keep source width, cumulative depth phase, carrier localization and Ford damping in one ledger

The relevant currencies include logarithmic source width `H`, carrier width `1/H`, normalized horizontal depth `D`, the full profiled coefficient `b_rho`, the cumulative process `C(D)`, the damping `e^(-YD)`, the vertical Schwartz budget `O(Q)` and the residue norm consumed by the destination. NB-228 explains how the cumulative process and damping combine; NB-229 shows that the smooth carrier has already paid away all but logarithmic depth.

This is stronger bookkeeping than optimizing population, depth and phase separately. The matched packet no longer has an independent population power to retune once a subcritical cumulative exponent is known, and deep packets cannot matter merely because the formal Ford scale extends to `R`. At the same time, both the Abel identity and the `O(Q)e^(-YD_0)` tail localization use largely generic spectral geometry. The missing theorem remains source-specific inside the shallow active layer and must be independent enough not to recover the same Euler shell by a circular explicit-formula substitution.

The classical Landau--Gonek family is neighboring prior art for sums of `x^rho`, but the live object is vertically localized by the shell profile and truncated cumulatively by horizontal depth. A future result should state exactly which source theorem controls that joint object in the moving range `1<<D<<L` and how much exponent below `Y` it gains.

This remains source-side information. The matched packets are logical controls compatible with the audited zero information, not constructions of actual zeta zeros, and NB-228--NB-229 do not themselves give a quantitative Nyman--Beurling distance theorem. Any destination claim must preserve that bridge explicitly.
