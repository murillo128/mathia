# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Find cancellation inside the transported local logarithmic-derivative carrier

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-058-exact-zeta-primitive-reconstruction-loses-its-mellin-advantage-only-when-the-signed-convolution-is-decoupled`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, atomic carrying capacity and integer-carrier discrepancy. NB-202--NB-212 derive the current log-squared corridor. NB-213--NB-217 then show that ordinary Mellin primitivization, signs, zero mean, bounded shell moments and support widening all repay apparent gains when reconstruction is estimated by absolute norms. For an arbitrary logarithmic support `E` and `j` primitive transfers, NB-217 isolates the exact absolute reconstruction currency `2pi/J_j(E)`.

NB-218 identifies where that tariff enters. On `Re(s)>1`, the Euler shell is exactly a signed convolution of the `j`-fold zeta primitive with its matched kernel; the factors `(log n)^j` and `(log n)^(-j)` cancel coefficientwise. Because the shell is supported away from zero, the kernel annihilates every finite polynomial jet of the primitive. The positive-power Mellin tariff is therefore not present in the exact algebra; it appears when kernel and primitive are decoupled by absolute values.

NB-219--NB-220 show that localization and source continuation do not force that decoupling. A flat Gaussian-type vertical window gives a dual source profile with Gaussian decay, can approximate the moving shell to arbitrary algebraic order, and produces an Euler source series that is entire in `s`. The remaining question was whether that entire source object could be tied back to local left-of-one zeta data without crossing remote zeros or recreating a global absolute-value tariff.

NB-221 closes that **representation/transport** question for every fixed primitive depth. Repeated integration by parts moves the primitive derivatives onto the flat window and gives one leading term

`A_0(s)=(1/(2pi)) integral L_X(v) w_V(v) (-zeta'/zeta)(s+iv) dv`

plus window-derivative corrections of size `O(log X V^(-2M-2))`. The coefficient of the leading `-zeta'/zeta` convolution is exactly one for every fixed primitive depth. Splitting at `|v|<=|t|/2` then permits a finite rectangular contour shift inside a Vinogradov--Korobov zero-free strip: the physical height stays comparable to `|t|`, the pole at height zero and remote zeta zeros are never crossed, and the omitted tails remain on `Re(s)>1` where absolute convergence controls them.

The transport therefore works locally, but it also exposes the method boundary. After transport, every fixed primitive depth has reduced back to the same local logarithmic-derivative carrier used in NB-212. Applying the existing pointwise Vinogradov--Korobov bound reproduces the same log-squared diagonal corridor, up to arbitrarily small algebraic window errors. Primitive depth, entire source continuation and local contour transport do not improve that exponent by themselves.

The live target is now narrower: exploit **cancellation inside the transported carrier-frequency `-zeta'/zeta` integral** that is invisible to the pointwise Vinogradov--Korobov envelope, while keeping the source/kernel coupling and the final Nyman destination theorem explicit. Another primitive, softer continuation or pointwise bound that is inserted only after taking absolute values does not address this target.

## Keep moving-complexity uniformity, source representation, conditioning, localization and analytic identification explicit

The relevant currencies now include source total variation, signed conditioning, requested return tolerance, integer-cell occupancy, zero-free contour width, reciprocal support mass `J_j(E)`, the destination-visible source functional, reconstruction cost, the exact carrier-frequency coefficient, soft vertical-window width/order, dual Gaussian source tails, local contour height, the transported logarithmic-derivative convolution and any cancellation norm used on that convolution.

NB-219--NB-221 give a useful separation principle. Full-line acquisition, dual source tails and remote zeta singularities can all be removed without destroying the signed source representation. Once that is done, the proof-interface loss is no longer continuation itself: it is the decision to bound the transported `-zeta'/zeta` carrier pointwise. Any claimed improvement must identify a cancellation mechanism in that integral that survives the finite contour transport and still feeds the destination approximation problem.