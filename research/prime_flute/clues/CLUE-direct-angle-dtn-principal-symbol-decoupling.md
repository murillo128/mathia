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

PF-324 now shows that the remaining distance from this critical packet to the outgoing seam is itself arithmetic. With `r_n=h_{n+1}/h_n`,

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

## Why it may matter

The open calculation is now sharply localized. PF-233 still gives exact operator-valued corridor transfer and an even transfer function `F(x)=x/\sinh x`, but PF-322--PF-323 prove that the retained physical-low space contains genuine compactification-critical packets for which a blanket small-argument Taylor estimate fails even away from the quotient seam.

PF-324 makes the test more discriminating. If suppression of the critical packet is fundamentally a bounded-distance seam/gluing effect, the `r_n->infinity` subsequence is adversarial because the outgoing seam escapes every fixed critical window. If the completed angle nevertheless gains a superlinear seam power there, the mechanism must come from the physical `L/H` projection, seam-energy normalization, or genuinely nonlocal finite-pant completion rather than from merely placing the packet near a seam. Conversely the `r_n->0` subsequence keeps the seam at the minimal finite critical distance and maximizes the opportunity for a local boundary cancellation.

A difference between these two regimes would be a concrete way for adjacent prime ordering to survive into the completed local response. PF-324 does not establish such a difference; it only supplies the canonical arithmetic parameter and the two subsequences on which to test it.

## Decisive test

Use PF-323's **interior critical packets** at one fixed `lambda`, not only the seam-centered PF-322 packet. Propagate them through the actual shear-deleted one-cusp-pant construction: retain the finite-pant quotient, transport into the PF-205 physical cuff representation, apply the true seam-energy diagonal normalization, keep the common positive completion used by PF-320, then form the physical `L/H` mixed corner and its intrinsic angle.

Run the same calculation on both arithmetic subsequences singled out by PF-324:

1. **finite-boundary regime:** `r_n->0`, hence `D_{n,lambda}->log(1/lambda)`;
2. **escaping-boundary regime:** `r_n->infinity`, hence `D_{n,lambda}->infinity`.

For each regime distinguish three outcomes. If the compactification-critical component cancels and one gets `O(s_n^{1+epsilon})`, PF-321 closes the reference channel strongly. If operator-norm superlinear decay fails but the local squared Hilbert--Schmidt leakage remains `O((1+log P_n)/P_n^2)`, PF-318 still closes the endpoint. If a nonconstant PF-323 packet survives the complete quotient/normalization/completion with angle mass incompatible with both criteria, the direct-angle route is genuinely obstructed.

The first especially useful discriminator is the escaping-boundary regime. Determine whether the completed normalized `L/H` response of the interior critical packet still tends to zero faster than `s_n`, or whether an order-`s_n`, order-one, or PF-318-incompatible singular direction remains when the outgoing seam is arbitrarily far away in the natural critical coordinate.

A negative conclusion must be expressed at the **intrinsic angle** level. Large compactified `A`-form energy, raw seam-block amplification, or the PF-215 constant mode are not sufficient witnesses.

## Evidence boundary

PF-321 is an implication theorem, not the missing local PDE estimate. PF-233 supplies exact transfer structure but does not make its unbounded transverse operator uniformly small on the growing physical-low space. PF-322 proves that such uniform smallness is false at the cell-energy level; PF-323 moves the witness into the cuff interior; PF-324 proves that its recentered seam distance has non-universal arithmetic subsequences.

None of PF-322--PF-324 proves that the completed shear-deleted local angle is large. The finite-pant quotient, seam normalization, `L/H` projection, and common completion may erase the critical component, including on the escaping-boundary subsequence. Conversely, no current finding proves that they do. The superlinear angle estimate and the PF-318 Hilbert--Schmidt fallback remain open.

PF-320 controls only the difference between the actual sheared and shear-deleted local angles at the established reciprocal-prime cost. It does not transfer PF-233's formal quadratic cancellation through the reference problem. PF-324's gap-ratio dependence is geometric input to this test, not yet a spectral invariant or RH-relevant arithmetic recovery theorem.

The clue remains `accepted`, not `resolved`.

## Research disposition

Outcome: `accepted`.

PF-322--PF-324 have completed the unprojected adversarial calibration. The surviving target is strictly downstream: compute the **completed physical projected intrinsic angle** on PF-323's interior critical packet, separately on the finite-boundary and escaping-boundary prime-gap-ratio subsequences. Any fixed superlinear seam gain closes the reference channel by PF-321; otherwise measure singular-value/Hilbert--Schmidt leakage against PF-318.