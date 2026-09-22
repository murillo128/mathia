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
  - research/mobius_cancellation/findings/MC-459-staged-residual-energy-is-controlled-by-the-normalized-shift.md
---

# Can the staged factor-weighted source kernel beat the Möbius source-frame tariff?

## Observation

The direct source-frame repairs are now tightly classified. `MC-446`--`MC-450` show that ambient box averaging, hidden CRT multiplicity, one-lcm Fourier/Weil control, near-complete intervals, and bare cross-lcm frequency synchronization do not pay the conductor-power occupancy tariff. `MC-451`--`MC-455` then show that fixed-lcm sieve signs, raw truncated Möbius, bounded factorable component counts, internal factor multiplicity, and source-only conductor splitting do not become exponent-saving resources merely by changing representation.

`MC-456` supplies the positive neighboring template: Pascadi/Yang-type dispersion succeeds when factor blocks occupy genuinely different arithmetic roles before positive closure and survive into reciprocal/Kloosterman phases. `MC-457` tests the most direct transfer into the present fixed-conductor frame and finds exact CRT tensorization: an internal factor retained only as an independent coprime residue modulus disappears from complete mixed blocks, leaving factor dependence only in incomplete tails.

`MC-458` identifies a different legal ordering. For one genuine factorable component `lambda=alpha*beta`, write

\[
B_\beta(y)=\sum_{s\mid y}\beta_s,
\qquad
w(m)=\sum_{r\mid m}\alpha_r B_\beta(m/r).
\]

After conditioning the shifted correlation on the `alpha`-block divisors `r,r'`, the incomplete source kernel becomes a translated primitive-character correlation multiplied by two residual divisor-sum weights along affine quotient progressions. Those residual weights vary with the same integer source variable, so they are not the independent coprime residue masks classified by `MC-457`. Expanding them immediately restores the old product variables, but before that expansion there is a genuine staged factor-weighted kernel on which an analytic estimate can act.

`MC-459` settles the first quantitative objection to this carrier. Writing `r=g r_1`, `r'=g r_2`, `h=g h_0`, the two quotient forms satisfy

\[
r_1y_1-r_2y_2=h_0,
\]

so their product has discriminant `h_0^2`. For every divisor quadruple in the coupled residual-weight energy, the exact relative CRT density is `G/(L_1L_2)` with `G=(r_1L_1,r_2L_2)` and compatibility forces `G|h_0`. Consequently the bulk positive energy has only shift-controlled polylogarithmic density, and the all-range true diagonal is `K X^{o(1)}` by the pointwise divisor bound. Progression concentration therefore does **not** force a polynomial loss merely because the quotient slopes are large.

## Research question

Can the exact staged kernel

\[
\sum_{k\in I}
\chi(k+u+\delta)\overline{\chi(k+u)}
B_\beta(A+vk)\overline{B_\beta(A'+v'k)}
\]

be estimated **before** residual divisor expansion and before componentwise positive closure with a strict conductor-power gain that survives the off-diagonal dispersion/completion, outer-factor multiplicity, exceptional source ranges, and later source-depth bookkeeping?

The diagonal side of this question is no longer open: `MC-459` shows that the residual amplitudes themselves do not impose a polynomial progression-energy tariff. The live issue is whether their coupling to the translated-character phase can be exploited before an estimate expands or absolutely majorizes the residual divisors and thereby restores the product quotient.

A second branch remains legitimate but separate: source-only conductor reduction could still win without factor-specific staging if the reduced-conductor estimate beats the full product-level occupancy cost after every later summation.

## Why it may matter

The structural ambiguity in the factor-specific branch is removed. The fixed external character conductor does **not** force every legal well-factorable ordering to become product/lcm-level before analysis: `MC-458` gives an exact pre-positive carrier outside the simple CRT-tensorization hypothesis of `MC-457`. At the same time, the carrier is algebraically equivalent to the old product expansion after its residual divisor weights are opened, so representation change alone is not a gain.

`MC-459` removes the most immediate negative explanation for why the carrier might nevertheless be useless. The quotient progressions can concentrate divisibility only through the normalized shift, and the positive diagonal remains subpower. A successful estimate therefore need not first pay a conductor-sized norm penalty. Conversely, this makes the remaining test more stringent: the branch now needs a genuinely **off-diagonal/interference-sensitive** mechanism, not another norm estimate.

A positive result would identify the first factorable mechanism in this branch that survives long enough to alter the analytic budget. A negative result showing that every usable off-diagonal estimate must expand or separately majorize the residual divisor sums before extracting character cancellation would close the most plausible remaining well-factorable escape without claiming that factorability is useless in other arithmetic geometries.

## Decisive test

Take a balanced well-factorable component `lambda=alpha*beta` in the source form underlying `MC-409`/`MC-413`, and keep the exact `MC-458` ordering through the first nontrivial dispersion/Cauchy/completion step. Do **not** expand `B_\beta` into its complementary divisors before that step and do not replace it by a pointwise divisor-function majorant except when using `MC-459` solely to certify that the positive diagonal is affordable.

The progression-sensitive-energy gate is now discharged by `MC-459`: the two quotient forms have determinant `h/g`, divisor congruence densities are controlled by that normalized shift, and the true positive diagonal is subpower. The next test is the nonzero-frequency/off-diagonal part after the first Cauchy or completion. Determine whether one can retain the `B_\beta` amplitudes jointly with the translated-character phase long enough to obtain a strict conductor-power saving, or whether every admissible completion/large-sieve/dispersion estimate first linearizes the divisor weights back into the complementary factor variables and reproduces the product-level occupancy tariff.

Then propagate the strongest justified bound through the `MC-415` diagonal and `MC-448` occupancy budget. The branch survives only if the final estimate gives a strict conductor-power improvement after outer `(r,r')` summation, shift dependence, exceptional terms, and source depth are all charged.

For the independent source-only branch, propagate the best admissible reduced-conductor estimate through the existing product-level summation and require an actual net conductor-power gain; an improved individual character sum that is consumed by occupancy does not qualify.

## Evidence boundary

`MC-456` is a literature-backed transfer classification, not a theorem about the Möbius kernel. Pascadi and Yang show that factor-specific modulus geometry can power successful dispersion estimates in arithmetic-progression problems; they do not estimate the fixed-conductor staged kernel here.

`MC-457` exactly closes full completion of an independent coprime factor-residue mask. `MC-458` exactly constructs a different staged kernel. `MC-459` proves that its residual quotient pair has normalized-shift discriminant and that the progression-sensitive positive diagonal is not polynomially inflated; Henriot/Nair--Tenenbaum theory is close prior art for organizing polynomial-value divisor sums by discriminant, but it is not a black-box estimate for the character-weighted kernel in all source ranges.

None of these findings proves a conductor-power saving for the nonzero-frequency weighted translated-character sum or an improvement to Möbius cancellation. The substantive analytic question therefore remains open, and the clue stays `accepted`.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-459`**. The residual-weight norm/diagonal is no longer the candidate obstruction. The live well-factorable branch is the first genuinely off-diagonal dispersion/completion of the explicit staged kernel: either exploit the divisor-sum amplitudes while they remain coupled to the translated-character phase, or prove that every useful estimate necessarily destroys that coupling before any conductor-power gain can be extracted.

Generic internal-factor multiplicity, bounded component splitting, source-only q-vdC after product collapse, complete factor-residue completion, and a supposed polynomial progression-energy penalty remain closed or neutralized by `MC-454`--`MC-459`. The independent source-only conductor-reduction branch remains open only as a separate quantitative question.