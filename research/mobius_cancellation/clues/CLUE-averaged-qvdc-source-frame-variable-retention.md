---
id: CLUE-mobius-cancellation-averaged-qvdc-source-frame-variable-retention
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-413-additive-differencing-complete-block-ramanujan-collapse.md
  - research/mobius_cancellation/findings/MC-446-source-frame-box-mean-square-has-quadratic-occupancy-threshold.md
  - research/mobius_cancellation/findings/MC-447-crt-source-frame-fibers-collapse-to-shift-common-primes.md
  - research/mobius_cancellation/findings/MC-448-fixed-lcm-fourier-weil-averaging-still-pays-polynomial-occupancy.md
  - research/mobius_cancellation/findings/MC-449-centered-complement-duality-closes-near-complete-fixed-lcm-escape.md
  - research/mobius_cancellation/findings/MC-450-lcm-frequency-synchronization-recombines-to-centered-autocorrelation.md
  - research/mobius_cancellation/findings/MC-451-beta-sieve-fixed-lcm-signs-are-maximally-coherent.md
  - research/mobius_cancellation/findings/MC-452-truncated-mobius-is-not-well-factorable.md
  - research/mobius_cancellation/findings/MC-453-bounded-factorable-splitting-cannot-dilute-quadratic-diagonal.md
  - research/mobius_cancellation/findings/MC-454-internal-factorization-does-not-increase-source-frame-occupancy.md
  - research/mobius_cancellation/findings/MC-455-standard-qvdc-conductor-reduction-preserves-product-quotient.md
  - research/mobius_cancellation/findings/MC-456-triply-well-factorable-dispersion-provides-a-factor-specific-quotient-breaking-template.md
  - research/mobius_cancellation/findings/MC-457-coprime-factor-residue-completion-tensorizes-from-fixed-source-conductor.md
  - research/mobius_cancellation/findings/MC-458-staged-factor-conditioning-exposes-residual-divisor-sum-kernel.md
---

# Can the staged factor-weighted source kernel beat the Möbius source-frame tariff?

## Observation

The direct source-frame repairs are now tightly classified. `MC-446`--`MC-450` show that ambient box averaging, hidden CRT multiplicity, one-lcm Fourier/Weil control, near-complete intervals, and bare cross-lcm frequency synchronization do not pay the conductor-power occupancy tariff. `MC-451`--`MC-455` then show that fixed-lcm sieve signs, raw truncated Möbius, bounded factorable component counts, internal factor multiplicity, and source-only conductor splitting do not become exponent-saving resources merely by changing representation.

`MC-456` supplies the positive neighboring template: Pascadi/Yang-type dispersion succeeds when factor blocks occupy genuinely different arithmetic roles before positive closure and survive into reciprocal/Kloosterman phases. `MC-457` tests the most direct transfer into the present fixed-conductor frame and finds exact CRT tensorization: an internal factor retained only as an independent coprime residue modulus disappears from complete mixed blocks, leaving factor dependence only in incomplete tails.

`MC-458` now identifies a different legal ordering. For one genuine factorable component `lambda=alpha*beta`, write

\[
B_\beta(y)=\sum_{s\mid y}\beta_s,
\qquad
w(m)=\sum_{r\mid m}\alpha_r B_\beta(m/r).
\]

After conditioning the shifted correlation on the `alpha`-block divisors `r,r'`, the incomplete source kernel becomes a translated primitive-character correlation multiplied by two residual divisor-sum weights along affine quotient progressions. Those residual weights vary with the same integer source variable, so they are not the independent coprime residue masks classified by `MC-457`. Expanding them immediately restores the old product variables, but before that expansion there is a genuine staged factor-weighted kernel on which an analytic estimate can act.

## Research question

Can the exact `MC-458` staged kernel

\[
\sum_{k\in I}
\chi(k+u+\delta)\overline{\chi(k+u)}
B_\beta(A+vk)\overline{B_\beta(A'+v'k)}
\]

be estimated **before** residual divisor expansion and before componentwise positive closure with a strict conductor-power gain that survives the true diagonal, progression concentration, exceptional sets, and later source-depth bookkeeping?

Equivalently, does staging one well-factorable block as progression geometry and the complementary block as a divisor-sum amplitude create analytically usable coupling, or does every admissible estimate of this object ultimately pay the same product-level occupancy/diagonal tariff once the arithmetic concentration of `B_\beta` on the relevant affine progressions is accounted for?

A second branch remains legitimate but separate: source-only conductor reduction could still win without factor-specific staging if the reduced-conductor estimate beats the full product-level occupancy cost after every later summation.

## Why it may matter

The structural ambiguity in the factor-specific branch is now removed. The fixed external character conductor does **not** force every legal well-factorable ordering to become product/lcm-level before analysis: `MC-458` gives an exact pre-positive carrier outside the simple CRT-tensorization hypothesis of `MC-457`. At the same time, the carrier is algebraically equivalent to the old product expansion after its residual divisor weights are opened, so representation change alone is not a gain.

This leaves a sharper and more valuable question than generic “can factorability help?” A positive estimate would identify the first factorable mechanism in this branch that survives long enough to alter the analytic budget. A negative estimate showing that the progression-sensitive second moment or true diagonal of the residual weights necessarily consumes every prospective conductor saving would close the most plausible remaining well-factorable escape without claiming that factorability is useless in other arithmetic geometries.

## Decisive test

Take a balanced well-factorable component `lambda=alpha*beta` in the source form underlying `MC-409`/`MC-413`, and keep the exact `MC-458` ordering through the first nontrivial dispersion/Cauchy/completion step. Do **not** expand `B_\beta` into its complementary divisors before that step and do not replace it by a pointwise divisor-function majorant unless the resulting loss is explicitly charged.

First derive a progression-sensitive second-moment or dispersion bound for the residual amplitudes `B_\beta(A+vk)` over the actual family of slopes, offsets, source intervals, and factor ranges. The unrestricted exact baseline from `MC-458`, `sum_{y<=Y}|B_\beta(y)|^2 << Y(log S)^3`, is not enough because the affine progressions may concentrate divisibility. Determine the true diagonal after the character phase and both residual weights are retained.

Then propagate the strongest justified bound through the `MC-415` diagonal and `MC-448` occupancy budget. The branch survives only if the final estimate gives a strict conductor-power improvement after all summations and exceptional terms. If the required progression-sensitive energy is necessarily polynomially larger, or every useful estimate must first expand/majorize the residual divisor sums and thereby restore the product quotient, record that as the closure result.

For the independent source-only branch, propagate the best admissible reduced-conductor estimate through the existing product-level summation and require an actual net conductor-power gain; an improved individual character sum that is consumed by occupancy does not qualify.

## Evidence boundary

`MC-456` is a literature-backed transfer classification, not a theorem about the Möbius kernel. Pascadi and Yang show that factor-specific modulus geometry can power successful dispersion estimates in arithmetic-progression problems; they do not estimate the fixed-conductor staged kernel here.

`MC-457` exactly closes full completion of an independent coprime factor-residue mask. `MC-458` exactly constructs a different staged kernel and proves only a global polylogarithmic `L^2` baseline for its residual divisor-sum weight. It does **not** prove a progression-sensitive bound for those weights, a power saving for the weighted translated-character sum, or an improvement to Möbius cancellation.

The structural admission question is therefore answered positively in a narrow sense, but the substantive analytic question remains open. The clue stays `accepted` because no theorem yet shows that the staged carrier produces, or cannot produce, a net conductor-power gain.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-458`**. The live well-factorable branch is no longer a search over arbitrary orderings: it is the quantitative analysis of the explicit staged residual-divisor-sum kernel. The next result must either demonstrate a progression-sensitive dispersion gain that survives the existing source budget or prove that the residual-weight energy/diagonal forces collapse back to the old tariff.

Generic internal-factor multiplicity, bounded component splitting, source-only q-vdC after product collapse, and complete factor-residue completion remain closed by `MC-454`--`MC-457`. The independent source-only conductor-reduction branch remains open only as a separate quantitative question.