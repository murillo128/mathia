# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the zeta-specific zero-spectrum gain to the exact Ford scale

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-059-generic-strip-analyticity-does-not-cancel-the-transported-carrier`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, atomic carrying capacity and integer-carrier discrepancy. NB-202--NB-212 derive the previous log-squared constant-gap corridor. NB-213--NB-217 then show that ordinary Mellin primitivization, signs, zero mean, bounded shell moments and support widening all repay apparent gains when reconstruction is estimated by absolute norms. For an arbitrary logarithmic support `E` and `j` primitive transfers, NB-217 isolates the exact absolute reconstruction currency `2pi/J_j(E)`.

NB-218 identifies where that tariff enters. On `Re(s)>1`, the Euler shell is exactly a signed convolution of the `j`-fold zeta primitive with its matched kernel; the factors `(log n)^j` and `(log n)^(-j)` cancel coefficientwise. Because the shell is supported away from zero, the kernel annihilates every finite polynomial jet of the primitive. The positive-power Mellin tariff is therefore not present in the exact algebra; it appears when kernel and primitive are decoupled by absolute values.

NB-219--NB-220 show that localization and source continuation do not force that decoupling. A flat Gaussian-type vertical window gives a dual source profile with Gaussian decay, can approximate the moving shell to arbitrary algebraic order, and produces an Euler source series that is entire in `s`.

NB-221 closes the representation/transport question for every fixed primitive depth. Repeated integration by parts moves primitive derivatives onto the flat window and leaves one leading carrier

`A_0(s)=(1/(2pi)) integral L_X(v) w_V(v) (-zeta'/zeta)(s+iv) dv`,

with coefficient exactly one. A finite-height rectangle transports that carrier left inside a Vinogradov--Korobov zero-free strip without crossing remote zeros or the pole, while source tails remain on the absolutely convergent side. Applying the pointwise logarithmic-derivative bound reproduces the same log-squared corridor.

NB-222 proves that this pointwise step cannot be improved from generic bounded strip analyticity alone. For the same moving-shell kernel and flat windows, the contour factor `e^(-X eta)` is sharp over the admissible analytic class; a carrier-matched exponential saturates the operator norm and the full Cauchy derivative envelope.

NB-223 supplies the first direct arithmetic escape on exactly that carrier. Instead of staying inside the zero-free strip, shift the smooth carrier globally and write it as the weighted zero sum

`sum_rho m(rho) e^(-X(1-beta)) (1+|gamma-t|)^(-A)`

up to negligible pole/top-line errors. Bellotti's near-one zero-density theorem controls the population in layers `1-beta~K/R`, with `R=(log |t|)^(2/3)(log log |t|)^(1/3)`. A finite layer decomposition shows that it is enough to have

`X/R >= (log log |t|)^d`

for any fixed `d>0`; the exponential zero weight then beats the permitted sublogarithmic layer population. Consequently, for every fixed `epsilon>0` and `kappa>0`, the smooth Euler barycenter is `o(1)` uniformly throughout

`log |t| <= kappa X^(3/2)/(log X)^(1/2+epsilon)`,

and the positive-return observable has an order-one gap on the same range. This improves the previous `(log X)^(-2)` corridor to every fixed logarithmic margin below the Ford denominator `(log X)^(-1/2)`.

The exact Ford scale remains open for a precise reason. There `X/R=Theta(1)`, while Bellotti's moving density control reaches every fixed power `(log log T)^alpha` with `alpha<1`, not the final depth comparable with `log log T`. The next source-side target is therefore to control that last near-one layer or exploit **phase cancellation among its zero residues**, rather than returning to generic strip estimates. The signed/complex route sees the same weighted zero sum before absolute values and may admit a phase-sensitive gain.

## Keep moving-complexity uniformity, source representation, conditioning, localization and analytic identification explicit

The relevant currencies now include source total variation, signed conditioning, requested return tolerance, integer-cell occupancy, zero-free contour width, reciprocal support mass `J_j(E)`, reconstruction cost, soft-window width/order, the exact transported logarithmic-derivative carrier, strip operator norm, zero-residue weight `e^(-X(1-beta))`, near-one zero population by layer, and any phase-sensitive cancellation norm placed on that zero sum.

NB-219--NB-223 give a useful separation principle. Full-line acquisition, dual source tails and remote zeta singularities can all be removed without destroying the signed source representation. Generic strip analyticity cannot improve the carrier scale, but **zeta-specific spectral population can**: NB-223 converts near-one zero-density into an order-one Euler gap almost up to Ford height. The endpoint obstruction is now the final `log log T`-deep zero layer or cancellation inside it, not another primitive, softer window, contour shift or generic derivative bound.

This remains source-side information. NB-223 does not itself give a quantitative Nyman--Beurling distance theorem or show that every good Nyman approximant must realize the positive Euler return observable. Any destination claim must still preserve that bridge explicitly.
