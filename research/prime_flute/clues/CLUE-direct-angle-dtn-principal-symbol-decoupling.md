---
id: CLUE-prime-flute-direct-angle-dtn-principal-symbol-decoupling
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-001-exact-cuff-coordinate.md
  - research/prime_flute/findings/PF-205-natural-width-cuff-smoothing-is-C1-uniform-and-critical-orlicz-summable.md
  - research/prime_flute/findings/PF-212-thin-fermi-boundary-frequency-split-closes-local-high-mode-gate.md
  - research/prime_flute/findings/PF-233-variable-width-diagonal-corridor-has-exact-operator-valued-transfer-law.md
  - research/prime_flute/findings/PF-235-hypercycle-boundary-compactification-has-only-quadratic-prime-dependent-defect.md
  - research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes.md
  - research/prime_flute/findings/PF-299-prime-seam-scale-has-critical-ell-one-accumulation.md
  - research/prime_flute/findings/PF-315-sequential-physical-band-elimination-factorizes-the-full-angle-defect.md
  - research/prime_flute/findings/PF-316-direct-channel-payment-makes-the-conditional-angle-endpoint-visible.md
  - research/prime_flute/findings/PF-317-positive-diagonal-completion-reduces-the-direct-angle-to-local-pant-crossing.md
  - research/prime_flute/findings/PF-318-logarithmic-rank-hilbert-schmidt-averages-already-close-the-direct-angle-at-weak-trace.md
  - research/prime_flute/findings/PF-319-corridor-form-smallness-alone-does-not-control-the-seam-normalized-direct-angle.md
  - research/prime_flute/findings/PF-320-form-smallness-controls-the-direct-angle-even-when-raw-seam-blocks-amplify.md
  - research/prime_flute/findings/PF-321-superlinear-seam-scale-local-angle-decay-is-trace-class.md
  - research/prime_flute/findings/PF-322-physical-low-packets-retain-critical-compactified-transverse-energy.md
  - research/prime_flute/findings/PF-323-interior-critical-low-packets-avoid-the-cuff-seam.md
  - research/prime_flute/findings/PF-324-critical-packet-seam-distance-remembers-consecutive-prime-gap-ratio.md
  - research/prime_flute/findings/PF-325-physical-translations-convert-the-local-hilbert-schmidt-gate-into-a-packet-position-integral.md
  - research/prime_flute/findings/PF-326-seam-normalization-preserves-fixed-band-packet-localization.md
---

# Can the shear-deleted local pant angle gain any fixed superlinear power of the seam scale?

## Observation

PF-315--PF-316 reduce the physical `P/H` endpoint to the conditional post-low angle `T_H` and the direct angle. PF-317 localizes the direct channel to finitely many positive local pant crossings; PF-318 shows that the local squared Hilbert--Schmidt budget

\[
O\!\left(\frac{1+\log P_n}{P_n^2}\right)
\]

already closes the global weak-`S_1` endpoint. PF-320 moves the geometric problem to the **shear-deleted intrinsic local pant angle**, because the actual PF-232 shear changes that angle only at the already-affordable reciprocal-prime scale. PF-321 further shows that any fixed superlinear seam gain

\[
\|T_{0,n}^{(r)}\|=O(s_n^{1+\varepsilon}),
\qquad \varepsilon>0,
\]

would make the shear-deleted reference direct channel trace class.

PF-322 blocks the naive proof of such a gain: zero-mean packets entirely inside the fixed physical-low band have order-one `s_n^2`-scaled compactified transverse energy. PF-323 removes the seam-artifact escape by recentering the same critical family at the interior point `tau_{n,lambda}` defined by

\[
s_n\cosh\tau_{n,\lambda}=\lambda,
\qquad 0<\lambda<1,
\]

while keeping every prescribed fixed window strictly inside the cuff cell.

PF-324 shows that the remaining distance from this critical packet to the outgoing seam is itself arithmetic. With `r_n=h_{n+1}/h_n`,

\[
D_{n,\lambda}:=\frac{\ell_n}{2}-\tau_{n,\lambda}
=\log\frac{1+r_n}{\lambda}+o(1),
\]

and `r_n=(g_{n+1}/g_n)(1+o(1))`. The audited Pintz ratio theorem therefore supplies subsequences with

\[
D_{n,\lambda}\to\log(1/\lambda)
\]

and subsequences with

\[
D_{n,\lambda}\to\infty.
\]

Thus the downstream projected-angle calculation has two genuinely different canonical boundary regimes. A single gap-independent seam-local picture is no longer an adequate falsification model.

PF-325 identifies the exact bridge from those localized packets back to PF-318. In the normalized physical-low Hilbert coordinates, the translations of one equal-amplitude fixed-band packet form a continuous tight frame, and for every local block `B`

\[
\|B\|_{\mathcal S_2}^2
=\frac{m_n}{\ell_n}
\int_0^{\ell_n}\|B^*\psi_{n,t}\|^2dt,
\qquad
\frac{m_n}{\ell_n}\to\frac\kappa\pi.
\]

PF-326 now removes the remaining **seam-localization** ambiguity in that bridge. Pullback through the exact seam normalizer commutes with physical translations. On every fixed physical band, after raw `L^2` renormalization, its symmetric and antisymmetric parity weights converge uniformly to

\[
(1+\xi^2)^{-1/2}
\qquad\text{and}\qquad
1,
\]

respectively. The pulled-back packet is therefore an explicit weighted translation orbit with a nonzero fixed-width limiting profile; seam normalization alone cannot spread it over the growing cuff.

This does not estimate the completed angle. It narrows the surviving uncertainty to the genuinely pant-side operations: the one-cusp-pant crossing, physical `L/H` projection, and common positive completion, with the exact seam multiplier retained in the packet shape and scale.

## Research question

For one canonical one-cusp pant contribution, delete only the PF-232 hypercycle-straightening shear while retaining the actual PF-205 seam energy, the variable-width diagonal corridor, the full common finite-pant/cusp-side completion, and the fixed physical low/high cutoff from PF-212. After distributing the positive identity share as in PF-320, let `T_{0,n}^{(r)}` be the intrinsic local low/high angle for one neighboring offset `r`.

Does the **completed projected angle** satisfy either

\[
\boxed{\|T_{0,n}^{(r)}\|\le Cs_n^{1+\varepsilon}}
\]

for some fixed `\varepsilon>0`, or, failing that,

\[
\boxed{
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\le C\frac{1+\log P_n}{P_n^2}?
}
\]

The first closes the reference direct channel in trace class by PF-321; the second closes it at the weak-trace endpoint by PF-318. PF-320 then restores the actual shear. The independent conditional channel `T_H` remains outside this clue.

By PF-325 the second condition may equivalently be tested, up to the fixed finite boundary-component bookkeeping, as

\[
\boxed{
\int_0^{\ell_n}
\|(T_{0,n}^{(r)})^*\psi_{n,t}\|^2dt
\lesssim
\frac{1+\log P_n}{P_n^2},
}
\]

where `psi_{n,t}` is the translated equal-amplitude packet in the actual seam-normalized low Hilbert coordinates. PF-326 gives its correct raw-boundary representative: a parity-dependent fixed-band weighted packet, not the unweighted PF-323 Dirichlet packet.

## Why it may matter

The open calculation is now sharply localized. PF-233 still gives exact operator-valued corridor transfer and an even transfer function `F(x)=x/sinh x`, but PF-322--PF-323 prove that the retained physical-low space contains genuine compactification-critical packets for which a blanket small-argument Taylor estimate fails even away from the quotient seam.

PF-324 makes the test more discriminating. If suppression of the critical packet is fundamentally a bounded-distance gluing effect, the `r_n->infinity` subsequence is adversarial because the outgoing seam escapes every fixed critical window. If the completed angle nevertheless gains a superlinear seam power there, the mechanism must come from the physical `L/H` projection or genuinely nonlocal finite-pant/common completion rather than from merely placing the packet near a seam.

PF-325 removes the need to return to mode-by-mode bookkeeping if the strong operator-norm target fails: the weak endpoint is exactly the integrated packet-response profile. PF-326 then removes a coordinate loophole in that physical test. The seam normalizer changes the profile by an explicit bounded fixed-band multiplier after common scaling, but preserves physical translation and fixed-scale localization. A downstream disappearance of the critical response therefore has to be produced by the pant-side geometry/completion rather than by cuff-scale delocalization at the seam-normalization step.

A difference between the PF-324 finite-boundary and escaping-boundary response profiles would be a concrete way for adjacent prime ordering to survive into the completed local response. PF-324--PF-326 do not establish such a difference; they isolate the arithmetic parameter and provide a coordinate-honest packet family on which to test it.

## Decisive test

Use PF-326's seam-normalized pullback of the PF-325 translation orbit as the boundary input. Equivalently, in each seam face-parity channel use the exact Fourier weights

\[
q_{n,\pm}(\xi_{n,k})^{-1/2},
\]

whose raw-`L^2` normalized fixed-band shapes converge to `(1+xi^2)^(-1/2)` and `1`. Keep their common seam-scale factors when computing the intrinsic response magnitude; PF-326 removes only the localization ambiguity, not those energetic factors.

Propagate this weighted packet through the **actual shear-deleted one-cusp pant**, retain the finite-pant quotient, apply the physical `L/H` mixed corner and the common positive completion used by PF-320, and record

\[
a_{n,r}(t):=\|(T_{0,n}^{(r)})^*\psi_{n,t}\|.
\]

Run the same completed calculation on both arithmetic subsequences singled out by PF-324: the finite-boundary regime `r_n->0`, where `D_{n,lambda}->log(1/lambda)`, and the escaping-boundary regime `r_n->infinity`, where `D_{n,lambda}->infinity`.

The two endpoint routes have distinct exact tests. If

\[
\sup_t a_{n,r}(t)=O(s_n^{1+\varepsilon}),
\]

PF-321 closes the reference channel strongly. If that fails, compute

\[
\int_0^{\ell_n}a_{n,r}(t)^2dt.
\]

PF-325 and PF-318 close the weak endpoint exactly when this is `O((1+log P_n)/P_n^2)` up to fixed cutoff/component constants. Conversely, if even one unit normalized packet has

\[
a_{n,r}(t)\gg\frac{\sqrt{1+\log P_n}}{P_n},
\]

then the PF-318 Hilbert--Schmidt fallback fails for that local block. A fixed-width set of such centers gives the same obstruction directly through the integrated identity.

The first especially useful discriminator remains the escaping-boundary regime. Determine whether the completed response near the PF-323 critical center is suppressed after the outgoing seam escapes every fixed critical window. PF-326 shows that seam normalization itself has not destroyed that fixed-window probe. Do not stop at one center if its response is small: the positive PF-318 route requires the full integrated packet-position budget.

A negative conclusion must still be expressed at the **intrinsic angle** level. Large compactified `A`-form energy, raw seam-block amplification, or the PF-215 constant mode are not sufficient witnesses.

## Evidence boundary

PF-321 is an implication theorem, not the missing local PDE estimate. PF-233 supplies exact transfer structure but does not make its unbounded transverse operator uniformly small on the growing physical-low space. PF-322 proves that such uniform smallness is false at the cell-energy level; PF-323 moves the witness into the cuff interior; PF-324 proves that its recentered seam distance has non-universal arithmetic subsequences.

PF-325 is an exact Hilbert--Schmidt/packet-position reduction. PF-326 resolves one narrow coordinate issue left open there: on a fixed physical band, seam-energy pullback preserves the translation orbit and a uniform positive fraction of raw-trace mass remains in a fixed physical window. It does **not** preserve the raw Dirichlet packet exactly, does not transport PF-322's exact compactified-energy constant, and does not estimate the common seam-scale amplitude factors in the final intrinsic response.

Most importantly, PF-326 does not control the one-cusp-pant crossing, physical `L/H` projection, or common positive completion. Those operations may still suppress, redistribute, or erase the critical component, including on the escaping-boundary subsequence. Conversely, no current finding proves that they do. The superlinear angle estimate and the PF-318/PF-325 integrated Hilbert--Schmidt fallback remain open.

PF-320 controls only the difference between the actual sheared and shear-deleted local angles at the established reciprocal-prime cost. It does not transfer PF-233's formal quadratic cancellation through the reference problem. PF-324's gap-ratio dependence is geometric input to this test, not yet a spectral invariant or RH-relevant arithmetic recovery theorem.

The clue remains `accepted`, not `resolved`.

## Research disposition

Outcome: `accepted`.

PF-322--PF-324 complete the unprojected adversarial calibration, PF-325 converts the weak endpoint into an exact physical-position packet integral, and PF-326 removes seam-normalization-induced cuff-scale delocalization as an escape route. The surviving target is now strictly pant-side: compute the **completed physical projected intrinsic-angle response profile** for the explicit seam-weighted packet family, separately on the finite-boundary and escaping-boundary prime-gap-ratio subsequences. Any fixed superlinear seam gain closes the reference channel by PF-321; otherwise the integrated squared packet response must meet the PF-318 reciprocal-prime Hilbert--Schmidt budget.