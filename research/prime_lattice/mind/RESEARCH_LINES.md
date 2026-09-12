# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prevent the first forbidden localized Weil crossing uniformly in aperture

**Linked intuition:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`.

PL-259--PL-276 show that source recovery is not positivity: finite positive interior sources are eventually sign-indefinite and no fixed compact correction removes their two-sided high-frequency Morse defect. PL-278 shows that canonical noncompact completion repairs that high-frequency defect generically, leaving a finite low/mesoscopic residual sector. PL-279 shows individual newly activated prime-power terms enter quadratically softly.

PL-280 makes the cross-aperture direction one-sided: localized domains are nested, ordered min-max levels are nonincreasing with aperture, and the negative Morse index `nu(a)` is nondecreasing. PL-281 closes the localization-exhaustion loophole:

\[
\kappa_c=\sup_{a>0}\nu(a)=\lim_{a\to\infty}\nu(a).
\]

A finite global compact-support defect cannot hide beyond every finite window.

PL-282 adds two finite-support facts. First, a recent non-peer-reviewed computer-assisted source reports `A_(0.72)>=5.890e-17 I`; conditional on successful independent reproduction, PL-280 propagates strict positivity to every `0<a<=0.72`, after the source channels `2,3,4` are already active. Second, and more structurally, a Gauss--Stieltjes lower hierarchy gives

\[
L_a>0\quad\Longleftrightarrow\quad\exists m<\infty:\ L_{a,m}>0
\]

for every fixed aperture. Strict positivity on a prescribed finite support is therefore finitely certifiable in principle.

The live theorem is not better finite-window diagonalization or generic completion. It is an **aperture-uniform arithmetic control** preventing the first crossing while infinitely many prime-power atoms enter. A useful source stratification or Schur-complement estimate must retain a positive margin as `a` grows, or otherwise prove that the monotone ledger never acquires its first negative level.

## Separate source recovery, tail repair, threshold softness, finite certification, monotone index, and exhaustion

The projective tower is source-lossless; finite positive aggregation is sign-indefinite; canonical noncompact completion repairs the spectral tail; individual atoms activate softly; fixed-support strict positivity has a terminating certificate hierarchy; negative levels persist once created; and support localization exhausts the compact-support negative index exactly.

These gates do not combine into a global positivity theorem. In particular, a certificate at `a=0.72` does not imply positivity until the next prime threshold, and a fixed-support certificate hierarchy gives no uniform depth or positive gap as `a->infinity`. What remains unresolved is a source-specific mechanism that prevents the **existence** of the first crossing over the full aperture family.