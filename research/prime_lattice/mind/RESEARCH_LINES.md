# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prevent the first forbidden localized Weil crossing uniformly in aperture

**Linked intuition:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`.

PL-259--PL-276 show that source recovery is not positivity: finite positive interior sources are eventually sign-indefinite and no fixed compact correction removes their two-sided high-frequency Morse defect. PL-278 shows that canonical noncompact completion repairs that high-frequency defect generically, leaving a finite low/mesoscopic residual sector. PL-279 shows individual newly activated prime-power terms enter quadratically softly.

PL-280 makes the cross-aperture direction one-sided: localized domains are nested, ordered min-max levels are nonincreasing with aperture, and the negative Morse index is nondecreasing. PL-281 closes the localization-exhaustion loophole, while PL-282 gives a terminating finite certificate hierarchy for strict positivity at each fixed aperture.

PL-283 transfers a recent non-peer-reviewed computer-assisted lower bound to Suzuki's canonical Friedrichs operator,

\[
A_{0.8}\ge8.9\times10^{-18}I>0,
\]

conditional on the external interval-arithmetic certificate.

PL-284 sharpens the endpoint spectral picture using the same source's parity-resolved min--max bounds. At `a=0.8`, the canonical operator has a simple even ground state with

\[
8.9\times10^{-18}
\le\lambda_1(A_{0.8})
\le2.523\times10^{-16},
\]

while

\[
\lambda_2(A_{0.8})\ge8.206\times10^{-15},
\qquad
\lambda_2-\lambda_1\ge7.9537\times10^{-15}.
\]

These inequalities remain literature-level until the computer-assisted certificate is independently reproduced. They provide a genuinely isolated finite-window ground state and therefore a sharper base point for any controlled aperture perturbation. They do **not** give an all-aperture gap: nested-domain monotonicity controls ordered levels individually but does not prevent the first and second levels from moving toward one another as the aperture grows.

The live theorem remains an **arithmetic first-crossing prevention law** that survives the growing von-Mangoldt comb. Finite-window work is most valuable if the positive margin/gap can be propagated by a source-specific differential, Schur, or variational inequality in aperture; another isolated endpoint certificate without such transport does not change the global gate.

## Separate fixed-window spectral isolation from aperture-uniform coercivity

At `a=0.8` the active prime-power channels are still exactly `2,3,4`, and the next source event occurs at `log(5)/2\approx0.804719`. PL-284 shows that the ground state is not merely positive but spectrally isolated immediately before that next event. This removes degeneracy at the certified endpoint as a local obstruction to perturbative analysis.

What remains unresolved is quantitative control of how the ground level and its gap move under domain enlargement and continuous archimedean evolution, including across later prime-power activations. A fixed-support Stieltjes certificate, a positive endpoint gap, monotone negative index, and global exhaustion are different resources. None by itself prevents a first zero crossing at a larger aperture.
