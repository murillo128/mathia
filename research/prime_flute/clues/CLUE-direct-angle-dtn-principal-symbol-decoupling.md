---
id: CLUE-prime-flute-direct-angle-dtn-principal-symbol-decoupling
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-318-logarithmic-rank-hilbert-schmidt-averages-already-close-the-direct-angle-at-weak-trace.md
  - research/prime_flute/findings/PF-320-form-smallness-controls-the-direct-angle-even-when-raw-seam-blocks-amplify.md
  - research/prime_flute/findings/PF-324-critical-packet-seam-distance-remembers-consecutive-prime-gap-ratio.md
  - research/prime_flute/findings/PF-325-physical-translations-convert-the-local-hilbert-schmidt-gate-into-a-packet-position-integral.md
  - research/prime_flute/findings/PF-328-critical-packet-intervals-restore-explicit-seam-parity-scales.md
  - research/prime_flute/findings/PF-329-final-diagonal-normalization-turns-seam-pulled-packets-into-total-energy-unit-traces.md
  - research/prime_flute/findings/PF-330-completed-low-normalization-rotates-packet-frame-instead-of-damping-total-energy-mass.md
  - research/prime_flute/findings/PF-336-relative-polar-transport-removes-the-normalized-insertion-envelope.md
  - research/prime_flute/findings/PF-337-critical-translations-expose-the-frequency-off-diagonal-mass-of-the-normalized-pant-insertion.md
---

# Can the shear-deleted local pant angle meet the direct-channel endpoint budget?

## Observation

The direct retained-low/high channel is now reduced to a genuinely local PDE question. PF-318 shows that the weak-`S_1` endpoint follows if the shear-deleted local angle satisfies

\[
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\lesssim \frac{1+\log P_n}{P_n^2},
\]

while PF-320 pays the actual hypercycle shear at exactly that squared Hilbert--Schmidt scale. PF-325 rewrites the local Hilbert--Schmidt mass as a constant-density integral of translated fixed-band packets, and PF-328 proves that compactification-critical packets occupy a positive-length interval of those same physical translations.

PF-329--PF-330 remove a coordinate-amplitude loophole: after the completed low normalization, the packet family is still an exact same-density tight frame in raw total-energy coordinates, changed by a unitary polar rotation rather than damped away. PF-336 then removes the extra normalized-insertion envelope that had remained in the translation branch. If

\[
K_n=Q_{L,n}^{-1/2}\Lambda_{LL,n}Q_{L,n}^{-1/2},
\]

and `U_n` is the completed polar rotation, then

\[
\|[U_n,\tau_t]\|_{\mathcal S_2}
\le \frac1{\sqrt2}\|[K_n,\tau_t]\|_{\mathcal S_2}.
\]

Thus no separate bound on `\|K_n\|`, no seam condition number, and no retained-rank factor is needed to transfer physical translations through the polar rotation.

PF-337 makes the remaining translation gate directly testable. Averaging `\|[K_n,\tau_t]\|_{\mathcal S_2}^2` over the PF-328 critical interval is an exact positive weighted sum of the Fourier matrix mass `|K_{n;jk}|^2`. Therefore a successful translation gate forces all Hilbert--Schmidt mass at every fixed nonzero physical-frequency separation to vanish. On PF-324's finite-boundary subsequence `r_n\to0`, the critical translations are asymptotically half-cuff translations, so every fixed odd Fourier diagonal has asymptotic commutator weight `4`; in particular

\[
\sum_k|K_{n;k+1,k}|^2=o(1)
\]

is a necessary condition for the translation route.

## Research question

There are still two legitimate routes to the direct-channel endpoint.

For the **upper-bound route**, determine whether the actual shear-deleted local pant angle, with the canonical seam energy, physical low/high split, variable-width corridor, and common finite-pant/cusp completion retained, satisfies either a superlinear operator bound

\[
\|T_{0,n}^{(r)}\|\le Cs_n^{1+\varepsilon}
\]

for some fixed `\varepsilon>0`, or the PF-318 Hilbert--Schmidt endpoint

\[
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\le C\frac{1+\log P_n}{P_n^2}.
\]

For the **PF-328 obstruction route**, work before the nonlinear completion and determine the physical-frequency structure of the normalized pant insertion `K_n`. Does

\[
\sup_{t\in I_n}\|[K_n,\tau_t]\|_{\mathcal S_2}=o(1)
\]

hold? PF-336 would then transfer the estimate directly to `U_n`. The first falsification target should be PF-337's nearest odd Fourier diagonal on the finite-boundary subsequence. If that band has positive lower-limit Hilbert--Schmidt mass, the translation-transport route fails without any further square-root or polar analysis.

Even a positive translation result is not enough by itself: one completed reference packet must still be shown spatially concentrated, or a stronger fixed-window cutoff/off-diagonal estimate must be proved. Spatial cutoffs do not commute with `Q`, so that stronger route remains distinct.

## Why it may matter

Most abstract operator-theoretic uncertainty has now been removed. The shear is already affordable at the endpoint, completed-energy normalization cannot erase packet mass by scalar damping, and the polar rotation cannot create an independent translation-locality obstruction. What remains is the geometry of the shear-deleted one-cusp pant/core DtN response in the exact seam-energy metric.

PF-337 also makes a negative result cheap enough to be valuable. Instead of attempting the full nonlinear packet transport and only then discovering nonlocality, one can test explicit positive Fourier-matrix mass of `K_n`. A persistent first odd diagonal on the arithmetic finite-boundary subsequence, or persistent mass across any fixed physical-frequency gap in any regime, is already incompatible with the PF-336 translation gate.

## Decisive test

For the obstruction branch, compute or estimate the physical Fourier matrix of

\[
K_n=Q_{L,n}^{-1/2}\Lambda_{LL,n}Q_{L,n}^{-1/2}
\]

on the exact shear-deleted one-cusp-pant low section. Start with the PF-324 subsequence `r_n\to0` and the PF-337 quantity

\[
\boxed{
M_n^{(1)}:=\sum_{k:\,k,k+1\ \mathrm{retained}}
|K_{n;k+1,k}|^2.
}
\]

A positive `\limsup M_n^{(1)}` refutes the translation-transport route. If `M_n^{(1)}\to0`, test the other fixed odd offsets and the fixed-physical-separation tail from PF-337 before attempting the full uniform commutator. A proof of the full `o(1)` commutator may then be passed through PF-336 with constant `1/\sqrt2`, but it must still be paired with concentration of one reference profile before the PF-324 finite-boundary/escaping-boundary comparison is meaningful.

For the upper-bound branch, estimate directly the basis-free raw canonical correlation or its trace form from PF-318/PF-320 rather than proving a stronger locality theorem than the endpoint needs. A uniform `O(s_n^{1+\varepsilon})` operator bound closes the reference channel by the existing superlinear criterion; the squared Hilbert--Schmidt budget above closes it at the weak-trace endpoint.

Do not return to generic square-root sensitivity, polar condition numbers, or a uniform `\|K_n\|` envelope: PF-336 has removed those as requirements for translation transport. Do not infer a completed-angle lower bound from pre-completion packet energy alone.

## Evidence boundary

The direct-angle endpoint remains open. PF-337 gives necessary Fourier conditions for the PF-336 translation gate, not a lower bound for the actual pant matrix and not a proof that the gate succeeds or fails. PF-336 transfers a normalized-insertion commutator to the completed polar rotation but does not provide physical concentration of a reference packet. PF-325/PF-328 supply the positive-measure critical packet family, while PF-329/PF-330 identify its correct completed-energy normalization; none proves a nonzero completed low/high correlation.

The upper-bound route is likewise unresolved: no superlinear local-angle estimate and no PF-318 Hilbert--Schmidt endpoint estimate has been established for the full shear-deleted pant completion.

No scattering/determinant theorem, zeta-zero correspondence, critical-line result, or RH implication is established.

## Research disposition

Outcome: `accepted`.

The clue remains live, but its obstruction branch is now narrower. The first translation-side PDE test is the normalized pant insertion itself, not the completed square-root map: evaluate PF-337's explicit Fourier off-diagonal masses, beginning with the nearest odd diagonal on the PF-324 finite-boundary subsequence. Only if those tests survive should effort move to the full `S_2` translation commutator and then to reference-packet concentration or the stronger cutoff route.