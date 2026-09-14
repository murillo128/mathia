---
id: CLUE-prime-flute-direct-angle-dtn-principal-symbol-decoupling
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-318-logarithmic-rank-hilbert-schmidt-averages-already-close-the-direct-angle-at-weak-trace.md
  - research/prime_flute/findings/PF-320-form-smallness-controls-the-direct-angle-even-when-raw-seam-blocks-amplify.md
  - research/prime_flute/findings/PF-336-relative-polar-transport-removes-the-normalized-insertion-envelope.md
  - research/prime_flute/findings/PF-338-finite-boundary-critical-translations-force-total-half-cuff-mixing-to-vanish.md
  - research/prime_flute/findings/PF-339-half-cuff-invariance-forces-raw-symmetric-pant-fourier-coupling-below-seam-width.md
  - research/prime_flute/findings/PF-340-symmetric-seam-parity-averages-two-adjacent-pant-self-responses.md
  - research/prime_flute/findings/PF-341-thin-pant-self-dtn-contrast-has-common-positive-sign.md
---

# Can the shear-deleted local pant angle meet the direct-channel endpoint budget?

## Observation

The direct retained-low/high channel has now split cleanly into one dead route and one live route.

PF-318 shows that the weak-`S_1` endpoint follows if the shear-deleted local angle satisfies

\[
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\lesssim \frac{1+\log P_n}{P_n^2},
\]

while PF-320 pays the actual hypercycle shear at exactly that squared Hilbert--Schmidt scale. This remains the live **direct upper-bound route**.

The alternative translation-transport route is no longer viable. PF-336 showed that a small physical-translation commutator of

\[
K_n=Q_{L,n}^{-1/2}\Lambda_{LL,n}Q_{L,n}^{-1/2}
\]

would transfer to the completed polar rotation without a condition-number loss. PF-338 reduced that premise on the finite-boundary arithmetic subsequence to asymptotic half-cuff invariance. PF-339 converted it to the raw requirement that every fixed odd Fourier coupling in the symmetric seam channel be `o(w_n)`. PF-340 exposed the only remaining logical loophole: the symmetric module sees the average of two adjacent pant self-responses, so their fixed two-mode contrasts might cancel.

PF-341 closes that loophole. For the explicit PF-339 pair

\[
f_{n,+}=\frac{c_{n,2}+c_{n,1}}{\sqrt2},
\qquad
f_{n,-}=\frac{c_{n,2}-c_{n,1}}{\sqrt2},
\]

each adjacent pant has the same positive contrast, with

\[
\Delta_n^+\gtrsim\frac1{s_nL_n},
\qquad
\Delta_n^-\gtrsim\frac1{s_{n-1}L_n}.
\]

Hence

\[
\frac{\Delta_n^{\mathrm{sym}}}{w_n}
\gtrsim
\frac{P_n^{1.475}}{\log P_n}\to\infty.
\]

The normalized pant insertion therefore does **not** become half-cuff invariant. The PF-336 strategy of proving completed translation locality by first proving translation locality of `K_n` is closed.

## Research question

Can the actual shear-deleted local pant angle still satisfy the PF-318/PF-320 direct endpoint without using the false normalized-insertion translation gate?

The live targets are now only the direct estimates

\[
\boxed{
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\le C\frac{1+\log P_n}{P_n^2}
}
\]

or, more strongly but less sharply tailored to the endpoint,

\[
\boxed{
\|T_{0,n}^{(r)}\|
\le Cs_n^{1+\varepsilon}
}
\]

for some fixed `\varepsilon>0`.

The estimate must be made for the actual shear-deleted one-cusp-pant low/high geometry with the canonical seam energy, variable-width corridor, and finite-pant/cusp completion retained. It may exploit cancellation or smoothing in the **angle/correlation operator itself**, but it may not assume approximate half-cuff translation symmetry of the raw normalized pant insertion: PF-341 disproves that premise.

## Why it may matter

PF-341 is a useful route separator rather than a negative answer to the direct endpoint. The raw normalized DtN insertion has a large, geometrically forced odd Fourier coupling, but PF-336 supplied only a one-way implication from raw translation locality to completed polar locality. Failure of that premise does not force a large completed low/high angle.

The remaining question is therefore sharper than before. Either the completed/direct angle has additional cancellation that suppresses the large raw self-DtN anisotropy down to the weak-trace budget, or the direct endpoint itself fails for a reason that must be seen after the nonlinear completion rather than inferred from `K_n` alone.

## Decisive test

Work directly with the PF-318/PF-320 basis-free raw canonical correlation or its trace form. Keep the seam form and the actual pant completion explicit, and estimate the low/high correlation at the scale required by

\[
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\lesssim \frac{1+\log P_n}{P_n^2}.
\]

A proof of this bound closes the reference/direct channel at the weak-trace endpoint. A lower bound that exceeds this scale on a source-realized subsequence rules out the direct upper-bound route and forces a different reference decomposition or endpoint mechanism.

Do not return to generic square-root sensitivity, polar condition numbers, a uniform `\|K_n\|` envelope, or physical-translation commutators of `K_n`: PF-336 removed the first three as necessary inputs and PF-341 has now falsified the last one as a viable smallness premise.

## Evidence boundary

PF-341 proves that the PF-336 normalized-insertion translation gate fails; it does **not** prove that the completed polar rotation has a large translation commutator and does not give a lower bound for `T_{0,n}^{(r)}`.

No PF-318 Hilbert--Schmidt endpoint estimate and no superlinear local-angle estimate has yet been proved for the full shear-deleted pant completion. The direct-channel endpoint therefore remains open through this upper-bound branch.

No scattering/determinant theorem, zeta-zero correspondence, critical-line result, or RH implication is established.

## Research disposition

Outcome: `accepted`, narrowed by PF-341.

The obstruction-side half-cuff sub-branch is resolved negatively: the raw normalized pant insertion is not asymptotically half-cuff invariant, so it can no longer serve as the locality premise for PF-336 translation transport. Keep this clue active only for the independent PF-318/PF-320 direct Hilbert--Schmidt/superlinear-angle route.