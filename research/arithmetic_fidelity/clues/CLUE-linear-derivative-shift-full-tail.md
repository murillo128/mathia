---
id: CLUE-linear-derivative-shift-full-tail
type: research-clue
status: resolved
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md
  - research/arithmetic_fidelity/findings/AF-421-finite-critical-windows-reduce-to-full-column-saddle-hierarchy.md
  - research/arithmetic_fidelity/findings/AF-425-second-order-square-packet-detuning-exposes-source-lattice.md
  - research/arithmetic_fidelity/findings/AF-426-exact-square-amplitude-has-irreducible-integer-source-packet-gap.md
  - research/arithmetic_fidelity/findings/AF-427-displaced-square-packet-cancellation-is-metrically-exceptional.md
  - research/arithmetic_fidelity/findings/AF-428-second-order-exceptional-amplitudes-are-residual-but-null.md
  - research/arithmetic_fidelity/findings/AF-429-supercritical-full-column-saddle-has-shrinking-integer-window.md
  - research/arithmetic_fidelity/findings/AF-430-supercritical-residual-packets-preserve-shrinking-saddle-window.md
  - research/arithmetic_fidelity/findings/AF-431-constant-rational-supercritical-sources-hit-first-saddle-window.md
  - research/arithmetic_fidelity/findings/AF-432-supercritical-packet-center-amplitudes-are-residual-but-metrically-thin.md
  - research/arithmetic_fidelity/findings/AF-433-free-left-tail-amplitude-is-not-a-source-discriminator.md
  - research/arithmetic_fidelity/findings/AF-434-full-column-saddle-does-not-transport-source-shell-index.md
  - research/arithmetic_fidelity/findings/AF-435-coefficient-root-neutrality-selects-source-radius.md
---

# Linear derivative-shift full-tail resummation

## Observation

AF-417--AF-432 reduce the left-tail derivative-shift hierarchy to increasingly fine integer-source and packet-balance conditions. In the critical regime the decisive coordinate is

\[
a=\frac{c^2}{4\pi^2},
\qquad
b_n=a n^{s_n/n-2},
\]

with square transitions `b=m^2`. AF-426 excludes complete adjacent-packet cancellation on every exact-square amplitude fiber. AF-427--AF-432 show that displaced or supercritical near-cancellation can occur only through shrinking exceptional target conditions; category-generic exceptional amplitudes are still metrically thin.

AF-433 identifies the source singularity shells for

\[
h(x)=-\log\!\left(\frac{1-e^{-x}}x\right)
\]

as

\[
r_m=2\pi m,
\qquad m\ge1,
\]

while also proving that the reciprocal-order family `x_n(c)=c/n` leaves `c>0` free unless a source-side admissibility rule is supplied. AF-434 then closes the apparent shell/packet-index explanation: source shell labels are aggregated inside the Taylor coefficients before target packet labels are created, so `c=r_m \iff a=m^2` is a coordinate correspondence rather than transported provenance.

AF-435 supplies the missing source-only admissibility mechanism for one natural selector class. For an analytic germ `f(z)=\sum a_jz^j` with finite nonzero radius `R(f)`, the coefficient-root response

\[
\Gamma_f(c)=\limsup_{j\to\infty}|a_jc^j|^{1/j}
\]

satisfies `\Gamma_f(c)=c/R(f)` by Cauchy--Hadamard. Hence the unique coefficient-root-neutral scale is `c=R(f)`. For the present source, `R(h)=2\pi`, so the source selects `c=2\pi` and therefore `a=1` before any target cancellation is inspected.

## Research question

Can the source analytic structure force a principled reciprocal-order probe, in particular the nearest-shell value `c=r_1=2\pi`, before target cancellation or exceptional-set membership is inspected, and does that selected probe survive the current packet-cancellation gate?

## Why it may matter

The question separates provenance from downstream optimization. A useful source selector must be defined without looking at packet cancellation, while the selected value must then face the same pointwise target test as any other fixed amplitude.

AF-435 now provides such a selector inside the coefficient-root-critical class: the source radius is the unique boundary between exponential contraction and amplification of the scaled Taylor coefficients. This removes the arbitrary `\kappa R` freedom that similarity covariance alone could not resolve. The resulting amplitude is not favorable, however: it is the exact-square point `a=1`, where AF-426 already gives an irreducible integer-source packet mismatch.

## Decisive test

**Gate 0 — source admissibility: closed positively in the coefficient-root-critical class.** AF-435 defines the source-only response `\Gamma_f(c)` and proves that its unique neutral scale is `c=R(f)`. For `h`, this is `c=2\pi=r_1`. The criterion uses only the source Taylor germ and does not inspect determinant packets, exceptional sets, primes, or zeros.

**Gate 1 — current shell/packet transfer: closed negatively.** AF-434 shows that, in the present determinant/Cauchy--Binet mechanism, shell labels are aggregated inside the coefficient `\zeta(2k)` before packet labels are formed. The fixed-packet zeta factor is subexponential at the saddle scale, so the matching integer labels do not represent transported provenance.

**Gate 2 — pointwise target membership: closed negatively for the selected probe.** AF-435 gives `c=2\pi`, hence `a=1`. AF-426 applies with `m=1` and proves that complete adjacent-packet cancellation cannot occur on that exact-square fiber. The selected probe therefore does not survive the current cancellation mechanism.

**Gate 3 — next packet scale: not entered.** Since Gate 2 fails for the source-selected probe, there is no basis in this clue for spending further effort on the next complete-packet correction.

## Evidence boundary

AF-435 does not prove that every conceivable canonical notion of reciprocal-order probe must select `2\pi`. It proves that the natural coefficient-root-neutral admissible class has a unique selector and that the selector is the source radius. The construction is canonical relative to the fixed source coordinate and is covariant under positive dilations, not arbitrary nonlinear reparameterizations.

AF-434 still rules out shell-index transport through the existing determinant representation. AF-426 rules out complete adjacent-packet cancellation at the selected amplitude but does not classify every possible full-determinant mechanism or an enriched representation retaining shell-resolved provenance.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/arithmetic_fidelity/findings/AF-435-coefficient-root-neutrality-selects-source-radius.md]]

AF-435 supports the source-selection part of the clue: coefficient-root neutrality selects `c=2\pi` without downstream tuning. Combined with AF-426, that selected value maps to `a=1` and fails the current complete adjacent-packet cancellation test. The present route is therefore closed at the provenance-first pointwise gate; alternative selector classes or enriched shell-resolved constructions are separate future questions rather than unfinished parts of this clue.