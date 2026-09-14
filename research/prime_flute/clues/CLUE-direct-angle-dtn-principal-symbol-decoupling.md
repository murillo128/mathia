---
id: CLUE-prime-flute-direct-angle-dtn-principal-symbol-decoupling
type: research-clue
status: resolved
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
  - research/prime_flute/findings/PF-342-sharp-physical-cutoff-forces-order-one-direct-angle-correlation.md
---

# Can the shear-deleted local pant angle meet the direct-channel endpoint budget?

## Observation

PF-341 closed the normalized-insertion translation-locality route but left the independent PF-318/PF-320 direct upper-bound branch open. That branch asked whether the current sharp fixed physical `L/H` split could still produce either

\[
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\lesssim \frac{1+\log P_n}{P_n^2}
\]

or the stronger superlinear local estimate

\[
\|T_{0,n}^{(r)}\|\lesssim s_n^{1+\varepsilon}.
\]

PF-342 answers that question negatively for the current decomposition. On a cuff of period `L_n`, the last retained-low Fourier mode and the first high mode have frequencies separated by only `2pi/L_n`. The PF-341 collapsing-corridor argument applied to their sum and difference shows that the pant low/high matrix element has the same `1/(sL)` scale as the diagonal energies. Zero twist makes the two adjacent pant contributions add with the same sign, and the symmetric seam-parity energy is negligible at fixed physical frequency.

After total-energy normalization, the resulting low/high canonical correlation stays bounded below by a fixed positive constant on every sufficiently far tail module. Selecting separated modules produces arbitrarily many such singular directions, so PF-342 proves that the direct angle `Z_{LH}` is not compact on any finite-section-compatible realization.

## Research question

Resolved negatively for the current sharp physical cutoff:

**Can the actual direct channel satisfy the PF-318/PF-320 endpoint budget while retaining the present sharp fixed physical `L/H` split?**

No. PF-342 gives order-one completed canonical correlations between adjacent Fourier modes straddling that cutoff on infinitely many separated tail modules.

This resolution is specific to the current decomposition. A smoothed/transition-band split or a different endpoint factorization is a different research question and should be proposed separately rather than silently weakening this clue.

## Why it may matter

The failure is stronger and cleaner than the earlier raw translation-locality obstruction. It is not inferred from a large unnormalized DtN coefficient and does not depend on controlling the completed polar factor. The obstruction survives the correct diagonal total-energy normalization itself.

The mechanism also explains why the existing sharp split is structurally fragile in the growing-cuff limit: the Fourier lattice spacing tends to zero, so two traces classified into opposite physical sectors can become arbitrarily close on every fixed geometric window. The collapsing pant corridor then correlates them at order one.

This redirects any future direct-channel attempt away from sharper estimates for the same local angle. The architecture must first change the frequency decomposition or the endpoint mechanism so that the cutoff boundary does not manufacture these asymptotically indistinguishable low/high pairs.

## Decisive test

PF-342 performs the decisive negative test requested by this clue.

For each large module it chooses the adjacent Fourier modes immediately below and above the fixed physical cutoff, proves a fixed lower bound for their raw total-energy canonical correlation, transfers that bound exactly through the seam-normalization congruence, and then uses PF-214's finite-range module support to choose separated modules. The resulting finite compressions contain arbitrarily many singular values bounded below by one constant.

Therefore the direct angle is noncompact. In particular neither the PF-318 local Hilbert--Schmidt budget nor the PF-321 superlinear seam-scale bound can hold for this sharp split.

## Evidence boundary

PF-342 rules out the **current sharp physical `L/H` direct channel**. It does not rule out a smooth frequency partition, a transition band, another reference decomposition, or a different endpoint factorization. It does not decide the conditional post-low channel.

The result also does not establish a scattering/determinant theorem, a zeta-zero correspondence, the critical line, or RH. It is a structural negative result about one operator-ideal route inside Prime Flute.

## Research disposition

Outcome: `refuted`.

Resolved by:
- [[research/prime_flute/findings/PF-342-sharp-physical-cutoff-forces-order-one-direct-angle-correlation]]

PF-342 supplies the nonconstant-low/high obstruction that this clue required for a negative resolution. Do not reopen the same PF-318/PF-320 estimate under the unchanged sharp cutoff; a materially different frequency split or endpoint architecture should receive a new clue and its own falsification controls.