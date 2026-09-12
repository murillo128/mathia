# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prevent the first forbidden localized Weil crossing

**Linked intuition:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`.

PL-259--PL-276 show that source recovery is not positivity: finite positive interior sources are eventually sign-indefinite and no fixed compact correction removes their two-sided high-frequency Morse defect.

PL-278 shows that canonical noncompact completion repairs the high-frequency source defect generically. The completed localized Weil operator has compact resolvent and only finitely many negative eigenvalues, so RH-facing information is confined to the finite low/mesoscopic residual sector. PL-279 shows individual newly activated prime-power terms enter quadratically softly in the canonical form topology.

PL-280 makes the cross-aperture direction one-sided: the localized form domains are nested, so every ordered min-max level is nonincreasing with aperture and the negative Morse index `nu(a)` is nondecreasing. Once a level crosses below zero, later source activation cannot heal it.

PL-281 closes the remaining localization-exhaustion loophole inside this canonical support family. If `kappa_c` is the negative index of the global compact-support Weil form, then

\[
\kappa_c=\sup_{a>0}\nu(a)=\lim_{a\to\infty}\nu(a).
\]

A finite global defect cannot drift outward while remaining invisible to every finite window. If `kappa_c=r<\infty`, the localized index stabilizes exactly at `r` after some finite aperture; if `kappa_c=\infty`, the finite-aperture indices become unbounded.

The live theorem is therefore purely crossing prevention for the actual arithmetic form. There is no separate “negative direction at infinity” to exclude after positivity has been proved on every finite aperture. A viable source-specific mechanism must keep the first variational level from crossing, for example by a coercive completed-Weil inequality or another arithmetic restriction on the low/mesoscopic source.

## Treat source recovery, generic tail repair, threshold softness, monotone index, and index exhaustion as separate gates

The projective tower is source-lossless; finite positive aggregation is sign-indefinite; canonical noncompact completion repairs the spectral tail generically; individual atoms enter softly; negative levels persist once created; and nested support localization exhausts the compact-support negative index exactly.

What remains unresolved is not visibility of a finite defect but its **existence**. PL-281 does not identify `kappa_c` with Bombieri's Fourier-side finite-defect count or with off-critical zeros. Any such arithmetic identification still needs its own theorem.