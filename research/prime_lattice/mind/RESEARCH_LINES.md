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

PL-282 adds a fixed-support Gauss--Stieltjes lower hierarchy with

\[
L_a>0\quad\Longleftrightarrow\quad\exists m<\infty:\ L_{a,m}>0
\]

for every fixed aperture. Strict positivity on a prescribed finite support is therefore finitely certifiable in principle.

PL-283 strengthens the concrete finite-aperture frontier. A recent non-peer-reviewed computer-assisted source reports

\[
Q_W(f)\ge8.9\times10^{-18}\|f\|_2^2
\]

for every complex test function supported in `[-0.8,0.8]`. The already-audited common-form/test-space dictionary transfers this lower bound in the safe restriction direction to Suzuki's Friedrichs representative:

\[
A_{0.8}\ge8.9\times10^{-18}I>0.
\]

Conditional on the correctness of that external certificate, PL-280 propagates strict positivity to every `0<a<=0.8`, pushing any first negative aperture beyond `0.8`. At `a=0.8` the active prime-power channels are still exactly `2,3,4`; the next source event is only at `log(5)/2\approx0.804719`. The result therefore closes almost all of the source-static interval after the previous `0.72` certificate without relying on a new prime-power activation.

The certificate remains literature-level until its interval-arithmetic proof is independently reproduced, and the tiny margin gives no ordinary floating-point validation route. More importantly, neither the `0.8` boundary nor the terminating fixed-support hierarchy supplies an aperture-uniform margin. The live theorem is still an **arithmetic first-crossing prevention law** that remains effective as the von-Mangoldt comb grows, rather than another isolated finite-window certificate.

## Separate source recovery, tail repair, threshold softness, finite certification, monotone index, and exhaustion

The projective tower is source-lossless; finite positive aggregation is sign-indefinite; canonical noncompact completion repairs the spectral tail; individual atoms activate softly; fixed-support strict positivity has a terminating certificate hierarchy; negative levels persist once created; and support localization exhausts the compact-support negative index exactly.

PL-283 makes the finite-window side quantitatively sharper but does not change that hierarchy of gates. Positivity through `0.8` does not imply positivity to the next prime threshold `log(5)/2`, because the domain and archimedean part evolve continuously between source activations. A fixed-support certificate hierarchy gives no uniform depth or positive gap as `a->infinity`.

What remains unresolved is a source-specific mechanism that prevents the **existence** of the first crossing over the full aperture family. Further finite-window work is most informative when it exposes a reusable inequality or source stratification that can plausibly survive growing aperture, not merely when it advances the certified endpoint by another isolated amount.