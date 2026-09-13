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
  - research/prime_flute/findings/PF-330-completed-low-normalization-rotates-packet-frame-instead-of-damping-total-energy-mass.md
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
\boxed{g_{n,t}=Q_{L,n}^{-1/2}A_n^{-1/2}\psi_{n,t}},
\qquad
A_n=I+(K_n)_{LL},
\]

and this trace has unit total raw low energy. The block-diagonal seam congruence itself changes the intrinsic angle only by left/right unitaries.

PF-330 sharpens what that last diagonal factor can and cannot do. Writing

\[
U_{L,n}=A_{0,n}^{1/2}Q_{L,n}^{-1/2}A_n^{-1/2},
\]

one has `U_{L,n}` unitary and

\[
A_{0,n}^{1/2}g_{n,t}=U_{L,n}\psi_{n,t}.
\]

Hence the completed packets are still an exact same-density tight frame in the raw **total-energy** Hilbert space. The low diagonal normalization cannot close the PF-318 Hilbert--Schmidt budget merely by damping the total-energy mass of the packet family. What it may destroy is the **physical localization associated with the center `t`**, because the polar unitary `U_{L,n}` need not commute with physical translations.

The remaining direct-channel problem therefore has two distinct forms. An upper-bound proof may estimate the basis-free raw canonical correlation directly. A PF-328 obstruction must additionally prove that the unitary-rotated total-energy frame remains localized enough for the finite-boundary/escaping-boundary geometry to survive.

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

In raw total-energy coordinates PF-330 gives the exact finite-section formula

\[
\boxed{
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
=\operatorname{Tr}
\bigl(A_{0,n}^{-1}B_{0,n}C_{0,n}^{-1}B_{0,n}^*\bigr),
}
\]

and the equivalent PF-325 packet integral over the rotated unit-energy frame. Thus the endpoint can be attacked without first proving pointwise localization of `A_n^{-1/2}\psi_{n,t}`.

For a negative packet obstruction, however, determine whether the polar unitary `U_{L,n}` preserves enough of the PF-328 critical physical localization on a positive-measure family of centers to distinguish the two PF-324 arithmetic boundary regimes.

## Why it may matter

This is the remaining local PDE gate for the direct channel. The earlier seam/corridor calculations have already removed several false shortcuts: raw seam amplification is not the intrinsic angle, fixed critical packets prevent a blanket small-argument corridor estimate, and a single distinguished packet center is insufficient because PF-325 measures the whole translation orbit.

PF-330 removes another false shortcut in the opposite direction. The completed low normalization cannot be credited with an endpoint gain merely because `A_n^{-1/2}\psi_{n,t}` is small in some intermediate coordinate norm: after transport to the raw completed-energy Hilbert space every packet has unit energy and the family remains tight. Endpoint smallness must come from the normalized low/high **correlation**, not loss of low frame mass.

The two PF-324 arithmetic boundary regimes remain genuinely discriminating only if physical localization survives the polar rotation. In the finite-boundary regime the outgoing seam stays a bounded recentered distance from the critical packet; in the escaping-boundary regime it leaves every fixed critical window. Without a locality theorem for `U_{L,n}`, the parameter `t` remains a valid frame label but need not remain the raw spatial center.

## Decisive test

There are now two legitimate decisive routes.

For the **upper-bound route**, estimate directly

\[
T_{0,n}^{(r)}
=A_{0,n}^{-1/2}B_{0,n}C_{0,n}^{-1/2}
\]

or its Hilbert--Schmidt trace

\[
\operatorname{Tr}
\bigl(A_{0,n}^{-1}B_{0,n}C_{0,n}^{-1}B_{0,n}^*\bigr).
\]

A uniform `O(s_n^{1+\varepsilon})` operator bound closes the reference channel by PF-321; the trace bound `O((1+\log P_n)/P_n^2)` closes it at the PF-318 endpoint. This route does not require recovering a translated raw packet profile.

For the **PF-328 obstruction route**, let `\tau_t` be physical translation on the retained low band and write `\psi_{n,t}=\tau_t\psi_{n,0}`. PF-330 identifies the exact localization defect

\[
\boxed{
U_{L,n}\psi_{n,t}-\tau_tU_{L,n}\psi_{n,0}
=[U_{L,n},\tau_t]\psi_{n,0}.
}
\]

Prove a commutator/quasilocality estimate, or an equivalent concentration statement for the raw total-energy packet `g_{n,t}`, on a positive-measure subset of the PF-328 critical interval. Then evaluate the completed raw correlation separately in the `r_n\to0` and `r_n\to\infty` regimes. A verified positive-measure lower response after this total-energy normalization would genuinely falsify the local Hilbert--Schmidt route.

A lower bound for `Q^{-1/2}\psi_{n,t}` before total-energy normalization, a scalar lower bound for `\|A_n^{-1/2}\psi_{n,t}\|`, or PF-328's restored parity scales alone is not decisive. The obstruction needs **spatial survival through the polar unitary**, while the positive endpoint route needs only the normalized correlation estimate.

## Evidence boundary

The direct-angle endpoint is still open. PF-325 gives an exact packet integral, PF-326--PF-328 give exact pre-angle localization/energy information, PF-329 identifies the correct total-energy-unit raw trace, and PF-330 proves that these completed packets form a unitary-rotated tight frame in raw total-energy coordinates.

None of those results proves locality of the polar unitary, a completed-angle lower bound, a superlinear local angle gain, or the PF-318 Hilbert--Schmidt budget. The fact that total-energy packet mass is preserved does **not** imply that the packet remains near its original physical center.

The seam form still matters as the raw positive summand in `A_0,C_0`; the new reduction removes only the interpretation of completed low normalization as an independent packet-mass damping mechanism.

No scattering/determinant theorem, zeta-zero correspondence, critical-line result, or RH implication is established.

## Research disposition

Outcome: `accepted`.

The clue remains live. For a positive endpoint proof, attack the basis-free raw canonical-correlation operator or trace directly. For a PF-328 obstruction, the next missing theorem is locality/concentration of the polar unitary `U_{L,n}` on the critical packet family; only then do the two arithmetic seam-distance regimes become completed-angle tests.