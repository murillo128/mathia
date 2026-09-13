---
id: CLUE-prime-flute-direct-angle-dtn-principal-symbol-decoupling
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-315-sequential-physical-band-elimination-factorizes-the-full-angle-defect.md
  - research/prime_flute/findings/PF-316-direct-channel-payment-makes-the-conditional-angle-endpoint-visible.md
  - research/prime_flute/findings/PF-317-positive-diagonal-completion-reduces-the-direct-angle-to-local-pant-crossing.md
  - research/prime_flute/findings/PF-318-logarithmic-rank-hilbert-schmidt-averages-already-close-the-direct-angle-at-weak-trace.md
  - research/prime_flute/findings/PF-320-form-smallness-controls-the-direct-angle-even-when-raw-seam-blocks-amplify.md
  - research/prime_flute/findings/PF-321-superlinear-seam-scale-local-angle-decay-is-trace-class.md
  - research/prime_flute/findings/PF-324-critical-packet-seam-distance-remembers-consecutive-prime-gap-ratio.md
  - research/prime_flute/findings/PF-325-physical-translations-convert-the-local-hilbert-schmidt-gate-into-a-packet-position-integral.md
  - research/prime_flute/findings/PF-326-seam-normalization-preserves-fixed-band-packet-localization.md
  - research/prime_flute/findings/PF-327-seam-normalized-critical-packet-shapes-retain-compactified-transverse-energy.md
  - research/prime_flute/findings/PF-328-critical-packet-intervals-restore-explicit-seam-parity-scales.md
  - research/prime_flute/findings/PF-329-final-diagonal-normalization-turns-seam-pulled-packets-into-total-energy-unit-traces.md
---

# Can the shear-deleted local pant angle meet the direct-channel endpoint budget?

## Observation

PF-315--PF-318 isolate the direct retained-low/high angle and show that the global weak-`S_1` endpoint follows from the local squared Hilbert--Schmidt budget

\[
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\lesssim
\frac{1+\log P_n}{P_n^2}
\]

for the shear-deleted local one-cusp-pant angle. PF-320 pays the actual hypercycle shear at the already-affordable reciprocal-prime scale, while PF-321 shows that any fixed superlinear seam gain `O(s_n^{1+\varepsilon})` would close the reference direct channel even in trace class.

PF-324--PF-328 supply a sharp adversarial packet calibration. Critical fixed-band packets occupy a positive-length interval in the exact PF-325 translation variable. Their seam-only raw traces remain localized and retain nonzero compactified transverse energy, while the distance to the outgoing seam has both finite-boundary and escaping-boundary prime-gap-ratio regimes. PF-328 also restores the explicit pre-angle face-parity scales: symmetric energy of order `w_n^{-1}` and antisymmetric energy of order `w_n`.

PF-329 closes an important representation loophole in that calibration. A unit packet `\psi_{n,t}` of the **completed intrinsic angle** does not enter the raw pant as the seam-only trace `Q_{L,n}^{-1/2}\psi_{n,t}`. Its exact raw low trace is

\[
\boxed{
g_{n,t}=Q_{L,n}^{-1/2}A_n^{-1/2}\psi_{n,t},}
\qquad
A_n=I+(K_n)_{LL},
\]

and this trace has unit total raw low energy. Equivalently, the completed packet response is the canonical correlation of `g_{n,t}` against raw high traces normalized by the full high diagonal energy. The block-diagonal seam congruence itself changes the intrinsic angle only by left/right unitaries.

Therefore PF-328's positive-measure family is a valid **pre-angle** obstruction candidate but not yet an angle lower bound. The final low diagonal preconditioner `A_n^{-1/2}` may reshape the packet and need not commute with translations. The remaining direct-channel question is now exactly whether that completed diagonal normalization preserves enough critical structure to obstruct the endpoint, or instead supplies the suppression needed for it.

## Research question

For one canonical shear-deleted one-cusp-pant contribution with the actual seam energy, variable-width corridor, physical low/high split, and common finite-pant/cusp completion retained, determine whether the intrinsic local direct angle `T_{0,n}^{(r)}` satisfies either

\[
\boxed{\|T_{0,n}^{(r)}\|\le Cs_n^{1+\varepsilon}}
\]

for some fixed `\varepsilon>0`, or, failing that,

\[
\boxed{
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\le C\frac{1+\log P_n}{P_n^2}.
}
\]

In the PF-325 packet representation, the second condition is equivalent up to fixed cutoff/component constants to

\[
\int_0^{\ell_n}
\|(T_{0,n}^{(r)})^*\psi_{n,t}\|^2dt
\lesssim
\frac{1+\log P_n}{P_n^2}.
\]

The raw-PDE version of each integrand must use the PF-329 total-energy-unit trace `g_{n,t}`, or the equivalent raw variational correlation, rather than the seam-only packet from PF-326--PF-328.

## Why it may matter

This is the remaining local PDE gate for the direct channel. The earlier seam/corridor calculations have already removed several false shortcuts: raw seam amplification is not the intrinsic angle, fixed critical packets prevent a blanket small-argument corridor estimate, and a single distinguished packet center is insufficient because PF-325 measures the whole translation orbit.

The two PF-324 arithmetic boundary regimes remain genuinely discriminating. In the finite-boundary regime the outgoing seam stays a bounded recentered distance from the critical packet; in the escaping-boundary regime it leaves every fixed critical window. If the completed total-energy correlation behaves differently in those regimes, adjacent-prime ordering has survived into the local angle response. If both regimes meet the same endpoint estimate, this packet route is suppressed despite the pre-angle critical energy.

PF-329 makes the next step more precise and prevents a false obstruction. The `w_n^{-1}` versus `w_n` parity factors from PF-328 cannot be carried as standalone response amplitudes through the intrinsic angle: the same pant energy enters the completed diagonal denominator, and the correction is generally operator-valued rather than scalar.

## Decisive test

Start from the PF-325 unit packet orbit `\psi_{n,t}` in the normalized physical-low angle coordinate. For the shear-deleted local pant form, compute or bound

\[
A_n^{-1/2}\psi_{n,t},
\qquad
A_n=I+(K_n)_{LL},
\]

on the PF-328 critical interval. Equivalently, work directly in raw coordinates with

\[
g_{n,t}=Q_{L,n}^{-1/2}A_n^{-1/2}\psi_{n,t}
\]

and the exact PF-329 variational response

\[
\|(T_{0,n}^{(r)})^*\psi_{n,t}\|
=
\sup_{0\ne h\in H}
\frac{|\Lambda_{HL,n}[g_{n,t},h]|}
{\langle h,(Q_{H,n}+\Lambda_{HH,n})h\rangle^{1/2}}.
\]

Run this completed calculation on both PF-324 regimes: `r_n\to0`, where the outgoing seam remains at finite recentered distance, and `r_n\to\infty`, where it escapes. The strongest useful outcomes are:

- a uniform `O(s_n^{1+\varepsilon})` bound, which closes the reference channel by PF-321;
- the integrated PF-325 budget `O((1+\log P_n)/P_n^2)`, which closes it at the PF-318 endpoint;
- or a verified positive-measure lower response after **total diagonal normalization**, which would genuinely falsify that local Hilbert--Schmidt route.

A lower bound for `Q^{-1/2}\psi_{n,t}` before `A_n^{-1/2}`, including PF-328's restored parity scales, is not a decisive test. To use the PF-328 critical family positively, prove that the completed diagonal preconditioner preserves enough localization/critical content on a positive-measure set. To use it negatively, show that this preconditioner or the raw high-energy correlation suppresses the family strongly enough to meet the integrated endpoint budget.

## Evidence boundary

The direct-angle endpoint is still open. PF-325 gives an exact packet integral, and PF-326--PF-328 give exact pre-angle localization/energy information, but none controls the completed low diagonal inverse square root. PF-329 proves only the exact representation identity and identifies the correct total-energy-normalized raw trace; it does not show that `A_n^{-1/2}` preserves or destroys the critical packet.

The seam form still matters as the raw positive summand `Q`; PF-329 does not remove the geometry. It removes only coordinate-amplitude reasoning that treats `Q^{-1/2}` or PF-328's common parity factors as if they were already intrinsic-angle amplitudes.

No current finding proves a superlinear local angle gain, the PF-318 Hilbert--Schmidt budget, a positive completed-angle lower bound, scattering/determinant control, a zeta-zero correspondence, the critical line, or RH.

## Research disposition

Outcome: `accepted`.

The clue remains live, but its decisive packet input is now sharper. The next calculation is not to propagate the seam-only PF-328 packet with its raw parity scale. It is to understand the **completed total-energy packet** `Q^{-1/2}A_n^{-1/2}\psi_{n,t}` — or the equivalent raw canonical correlation — across the actual one-cusp pant in both arithmetic boundary regimes.