---
id: CLUE-mobius-cancellation-averaged-qvdc-source-frame-variable-retention
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-416-weighted-vdc-filters-cannot-remove-diagonal.md
  - research/mobius_cancellation/findings/MC-417-fejer-riesz-closes-positive-finite-band-kernels.md
  - research/mobius_cancellation/findings/MC-456-triply-well-factorable-dispersion-provides-a-factor-specific-quotient-breaking-template.md
  - research/mobius_cancellation/findings/MC-458-staged-factor-conditioning-exposes-residual-divisor-sum-kernel.md
  - research/mobius_cancellation/findings/MC-459-staged-residual-energy-is-controlled-by-the-normalized-shift.md
  - research/mobius_cancellation/findings/MC-460-one-sided-residual-conditioning-promotes-reduced-divisor-to-reciprocal-source-shift.md
  - research/mobius_cancellation/findings/MC-461-residual-source-starts-decompose-into-bounded-anchor-slices.md
  - research/mobius_cancellation/findings/MC-463-gcd-sector-normalization-collapses-to-common-anchor-quotient.md
  - research/mobius_cancellation/findings/MC-464-normalized-gcd-gate-makes-favorable-shifts-totient-sparse.md
  - research/mobius_cancellation/findings/MC-465-fejer-weighted-favorable-gcd-classes-remain-sparse.md
  - research/mobius_cancellation/findings/MC-466-original-shift-fejer-envelope-cancels-outer-gcd-advantage.md
  - research/mobius_cancellation/findings/MC-467-residual-scale-interval-shrinkage-cancels-support-growth.md
  - research/mobius_cancellation/findings/MC-468-root-scale-support-makes-well-factorability-vacuous.md
  - research/mobius_cancellation/findings/MC-469-empty-vector-sieve-component-survives-small-outer-cell-pruning.md
  - research/mobius_cancellation/findings/MC-470-empty-vector-residual-is-a-nonnegative-sieve-boundary-count.md
  - research/mobius_cancellation/findings/MC-471-empty-vector-base-is-two-sided-sifted-translated-ratio-sum.md
  - research/mobius_cancellation/findings/MC-472-pair-sieve-complete-period-factorizes.md
  - research/mobius_cancellation/findings/MC-473-termwise-pair-sieve-completion-pays-exponential-branch-multiplicity.md
  - research/mobius_cancellation/findings/MC-474-pair-sieve-fourier-spectral-norm-is-exponential.md
  - research/mobius_cancellation/findings/MC-475-pair-sieve-parseval-coupling-pays-full-frequency-dimension.md
  - research/mobius_cancellation/findings/MC-476-sifted-restriction-is-coefficient-blind-at-zero-frequency.md
  - research/mobius_cancellation/findings/MC-477-low-denominator-envelope-admits-denominator-free-character-completion.md
  - research/mobius_cancellation/findings/MC-478-pair-sieve-local-fourier-factorization-lowers-envelope-l1-cost.md
  - research/mobius_cancellation/findings/MC-479-selberg-envelope-leakage-is-order-one-on-near-cutoff-single-violations.md
  - research/mobius_cancellation/findings/MC-480-selberg-leakage-complete-period-phase-factorizes.md
  - research/mobius_cancellation/findings/MC-481-centered-selberg-leakage-is-target-equivalent-modulo-envelope.md
  - research/mobius_cancellation/findings/MC-482-two-sided-beta-sieve-transfer-forces-a-polylogarithmic-cutoff.md
  - research/mobius_cancellation/findings/MC-483-well-factorable-bracket-width-does-not-transfer-the-signed-error.md
  - research/mobius_cancellation/findings/MC-484-buchstab-first-exit-removes-selector-but-preserves-dimension-two.md
---

# Can the staged factor-weighted source kernel beat the Möbius source-frame tariff?

## Observation

The empty-vector base component is an incomplete translated-ratio character sum against an exact dimension-two pair-sieve mask. `MC-472`--`MC-476` close the direct full-period, inclusion-exclusion, hard-mask Fourier, plain Parseval and coefficient-blind restriction routes. `MC-477`--`MC-478` show that low-denominator sieve envelopes are compatible with the character phase at polynomial spectral cost, but `MC-479`--`MC-481` show that transferring that gain back through Selberg leakage is either unsigned and too large or, after centering, algebraically target-equivalent to the original hard-mask discrepancy.

`MC-482` supplies an independent positive transfer by a two-sided beta-sieve bracket, but standard fundamental-lemma plus absolute interval-remainder bookkeeping forces the active sieve cutoff to be only polylogarithmic if one demands a fixed conductor-power relative gain on polynomial source intervals. `MC-483` then shows why merely making that bracket well-factorable does not repair the loss: the exact signed error is `theta(B^+-B^-)/2`, and the source-dependent selector `theta` contains precisely the hard-mask information not fixed by the bracket.

`MC-484` changes the frontier. The selector is not intrinsic to the hard mask. Classical Buchstab first exit gives the exact pointwise identity

\[
A_z(n)=A_w(n)-\sum_{w\le q<z}\mathbf 1_{q\mid n(n+h)}A_q(n),
\]

so the hard mask has a selector-free signed decomposition retaining the first-exit prime `q` before absolute values. After writing `n=a+qm` on one of the one or two roots of `n(n+h)=0 (mod q)`, both structures close exactly: the character phase remains a translated-ratio phase with conductor shift `h q^{-1} (mod p)`, and the residual roughness remains a dimension-two pair-sieve mask with CRT shift `h q^{-1} (mod P(q))` and cutoff `q`.

Thus the algebraic existence question is answered. The cost is that first exit does not lower the sieve dimension: it converts the target into a moving-prime bilinear family on intervals of length about `H/q`. Triangle bounding the prime branches gives only the harmonic/endpoint budget and no conductor power. The surviving resource is the **coupled dependence on the same first-exit prime `q` in the source interval, character shift and pair-sieve shift**.

## Research question

Does the exact Buchstab first-exit family

\[
\sum_{w\le q<z}
\sum_{m\in I_{q,a}}
K_{h q^{-1}\,(\mathrm{mod}\ p)}(m)
\mathbf 1_{(m(m\pm\delta_q),P(q))=1},
\qquad
q\delta_q\equiv h\pmod{P(q)},
\]

admit a conductor-sensitive bilinear, dispersion, reciprocity or staged-factor estimate that uses the common `q` dependence before coefficientwise absolute values and survives restoration of the exact q-vdC source weights?

If not, can one prove a source-specific obstruction showing that every admissible recombination of the first-exit branches collapses to the known harmonic/endpoint, full-frequency, or positive-envelope tariffs? The separately retained nonempty rough-block, first-exit boundary and pre-positive cross-component channels remain alternatives if the empty-vector first-exit family is killed.

## Why it may matter

This is the first live continuation that removes the `MC-483` selector without replacing the hard mask by a positive surrogate. It therefore evades the exact information-loss mechanism that killed the most natural upper/lower-bracket repair. At the same time, `MC-484` prevents false optimism: classical Buchstab iteration preserves the generic two-residue sieve geometry, so the well-known bilinear remainder theory of the **linear** Rosser-Iwaniec sieve cannot simply be imported as a dimension-two theorem.

A genuine estimate for the moving first-exit family would retain a factor variable that every previous positive or Fourier scalarization lost. A negative result would be equally useful because it would close the most canonical selector-free escape and redirect effort away from further bracket/envelope refinements.

## Decisive test

Work first in the `R=T=1` empty-vector source frame. Split the first-exit prime into dyadic blocks and keep the exact root parameterization `n=a+qm`. For each block, retain simultaneously:

- the shortened source interval and its exact endpoint dependence;
- the translated-ratio character separation `h q^{-1} (mod p)`;
- the exact residual pair-sieve cutoff `q` and CRT shift `delta_q`;
- the outer q-vdC/Fejér and staged-sieve coefficients that actually occur in the source frame.

Accept the route only if a proved estimate for the recombined block gains a fixed conductor power after all coefficient normalizations, shell summations, endpoint terms and diagonal costs are restored. The gain must occur **before** replacing the `q` sum by absolute values. A bound obtained independently for each `q` and then summed is not enough unless its aggregate genuinely beats the trivial first-exit budget.

Do not invoke Iwaniec's bilinear linear-sieve remainder or Pomykała's subunit-dimensional Rosser-Iwaniec result as a black box. A transfer must verify the actual `kappa=2` density and the moving character/sieve shifts, or explicitly reduce the problem to dimension-one pieces without reopening exponential branch multiplicity. Higher-dimensional Buchstab/DHR-type identities may reorganize the tree, but iteration counts as progress only if the terminal pieces land in an independently controlled analytic range.

Kill this continuation if every valid decomposition either: (i) scalarizes the first-exit prime and returns to a positive-envelope/selector problem; (ii) expands the residual hard mask with the superpolynomial branch/frequency tariffs already proved in `MC-473`--`MC-475`; or (iii) retains `q` but cannot beat the harmonic/endpoint recombination after exact source weights are restored.

## Evidence boundary

`MC-484` proves only the exact Buchstab specialization and the simultaneous affine/CRT closure of the character phase and pair-sieve mask. It does **not** prove a bilinear estimate, a conductor-power saving, a dimension-two analogue of Iwaniec's remainder theorem, or any improved bound for the Möbius function.

The classical literature establishes Buchstab iteration in arbitrary sieve settings, bilinear/factorable remainder structure for the linear Rosser-Iwaniec sieve, a subunit-dimensional extension, and separate higher-dimensional sieve frameworks. The current evidence does not identify a theorem that directly supplies the required dimension-two, moving-shift, character-coupled estimate. Absence from the targeted search is not a novelty claim.

`MC-482`--`MC-483` remain valid: positive bracketing still has the level/selector tariffs they identify. `MC-484` avoids those tariffs by changing the representation, not by disproving them. No Möbius bound, zero-free region, or RH consequence has been obtained.

## Research disposition

The clue remains `accepted` and is narrowed. The immediate empty-vector question is no longer whether an exact signed representation exists; Buchstab first exit supplies one. The active test is whether its **dimension-two moving-prime bilinear family** admits a conductor-sensitive estimate with the exact source weights retained. If that test fails, continue with the already-separated nonempty, boundary or pre-positive cross-component channels rather than returning to deeper positive brackets.