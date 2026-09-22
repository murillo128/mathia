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
  - research/mobius_cancellation/findings/MC-460-one-sided-residual-conditioning-promotes-reduced-divisor-to-reciprocal-source-shift.md
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

`MC-459` settles the first quantitative objection to this carrier. Writing `r=g r_1`, `r'=g r_2`, `h=g h_0`, the two quotient forms satisfy `r_1y_1-r_2y_2=h_0`; their product therefore has discriminant `h_0^2`. The exact coupled divisor densities are controlled by the normalized shift, and the true positive residual-weight diagonal is only subpower. Progression concentration does **not** force a polynomial loss merely because the quotient slopes are large.

`MC-460` then answers the next structural question positively. If only one residual block is expanded and `s|y_1` is conditioned before the second block is opened, write `d=(s,r_2)`, `s=d s_0`, and `r_2=d t`. After the forced congruence is solved and the remaining progression is rescaled to unit step, the source phase has the exact form

\[
\chi(j+U_s)\overline{\chi(j+U_s-D_s)},
\qquad
D_s=\delta s_0^{-1}\pmod q,
\]

while the second residual amplitude remains unexpanded on `C_s+r_1s_0j`. Moreover

\[
C_s\equiv r_1s_0(U_s-D_s)\pmod q.
\]

Thus a surviving factor variable has finally entered the **oscillatory source coordinate itself**, reciprocally, and the remaining amplitude is aligned modulo `q` with the conjugate-character leg. This is the factor-specific dependence that was absent from the product/lcm and independent-residue orderings.

## Research question

Can the one-sided staged family isolated by `MC-460`, schematically

\[
\sum_s \beta_s
\sum_{j\in J_s}
\chi(j+U_s)\overline{\chi(j+U_s-\delta s_0^{-1})}
\overline{B_\beta(C_s+r_1s_0j)},
\]

be estimated before the second residual expansion and before componentwise positive closure with a strict conductor-power gain that survives off-diagonal dispersion/completion, outer-factor multiplicity, exceptional source ranges, and later source-depth bookkeeping?

The diagonal side is closed by `MC-459`, and the factor-specific-oscillation existence question is closed by `MC-460`. The live issue is now sharply quantitative: does the coupled parameter map `s -> (U_s,D_s,C_s,r_1s_0)` have enough one-dimensional or low-complexity structure to beat the quadratic source-frame occupancy threshold of `MC-446`, or does the varying start `U_s` restore the same effective two-parameter tariff despite the reciprocal shift and alignment?

A second branch remains legitimate but separate: source-only conductor reduction could still win without factor-specific staging if the reduced-conductor estimate beats the full product-level occupancy cost after every later summation.

## Why it may matter

The earlier structural ambiguity in the factor-specific branch is gone. `MC-458` gives an exact pre-positive carrier, `MC-459` removes positive-energy inflation as the immediate obstruction, and `MC-460` proves that one-sided conditioning can promote a residual factor from amplitude-only dependence into a reciprocal translated-character shift before product collapse.

This is the first point in the branch where the surviving factor enters the same kind of oscillatory coordinate that powers successful neighboring dispersion arguments. But the gain is not automatic: `U_s` varies with the same residual divisor, and the raw source coordinate before thinning still has a fixed shift. A valid estimate must exploit the exact coupling rather than count reciprocal shifts as independent new source samples.

A positive result would identify the first factorable mechanism in this branch that actually alters the analytic conductor budget. A negative result proving that the map `s -> (U_s,D_s)` has full two-parameter occupancy, or that every usable completion first destroys the `MC-460` alignment, would close the most plausible remaining well-factorable escape without claiming factorability is useless in other arithmetic geometries.

## Decisive test

Take a balanced well-factorable component `lambda=alpha*beta` in the source form underlying `MC-409`/`MC-413`. Keep the `MC-458` staging, condition on exactly one complementary divisor as in `MC-460`, and preserve the second `B_\beta` block through the first nontrivial Cauchy/dispersion/completion step.

Do not expand the second residual block before that step. Do not replace it by a pointwise divisor-function majorant except when using `MC-459` solely to certify that the positive diagonal is affordable. Track the exact source parameters

\[
D_s=\delta s_0^{-1},
\qquad
C_s\equiv r_1s_0(U_s-D_s)\pmod q,
\]

and determine the true multiplicity/energy of the induced family of pairs `(U_s,D_s)` after the congruence defining `m_s` is imposed.

The next quantitative gate is passed only if that structure yields a strict conductor-power gain over the `MC-446` source-frame tariff after all off-diagonal completion terms are charged. A bound that merely averages over all possible `(U,D)` pairs, expands the surviving divisor sum first, or uses the reciprocal shape without controlling `U_s` has not used the new structure.

Then propagate the strongest justified estimate through the `MC-415` diagonal and `MC-448` occupancy budget. The branch survives only if the final estimate remains a strict conductor-power improvement after outer `(r,r')` summation, residual-`s` multiplicity, shift dependence, exceptional terms, and source depth are all charged.

For the independent source-only branch, propagate the best admissible reduced-conductor estimate through the existing product-level summation and require an actual net conductor-power gain; an improved individual character sum consumed by occupancy does not qualify.

## Evidence boundary

`MC-456` is a literature-backed transfer classification, not a theorem about the Möbius kernel. Reciprocal/Kloosterman and bilinear character-sum methods in the neighboring literature show that reciprocal factor variables can be analytically meaningful, but they do not estimate the coupled family derived here.

`MC-457` exactly closes full completion of an independent coprime factor-residue mask. `MC-458` exactly constructs the staged carrier. `MC-459` proves that its positive diagonal is affordable. `MC-460` exactly derives the reciprocal source shift and the modular alignment of the surviving amplitude, but proves no large-sieve, bilinear, trace-function, or conductor-saving estimate for that family.

In particular, `MC-460` does not justify replacing the two-dimensional source-frame threshold by a one-dimensional one: the shift `D_s` is reciprocal, but the start `U_s` also varies. None of these findings proves an improvement to Möbius cancellation, so the substantive analytic question remains open and the clue stays `accepted`.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-460`**. The live well-factorable branch is no longer “find some factor-specific source dependence”: that dependence now exists exactly. The target is to classify and estimate the concrete one-sided family produced by `s -> (U_s,D_s,C_s,r_1s_0)`, with special attention to whether the congruence alignment reduces effective source-frame occupancy or whether variable starts restore the old tariff.

Generic internal-factor multiplicity, bounded component splitting, source-only q-vdC after product collapse, complete factor-residue completion, a supposed polynomial progression-energy penalty, and the absence of factor-specific source oscillation are now closed or neutralized by `MC-454`--`MC-460`. The independent source-only conductor-reduction branch remains open only as a separate quantitative question.