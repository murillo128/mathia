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
---

# Can the staged factor-weighted source kernel beat the Möbius source-frame tariff?

## Observation

The empty-vector base component has now been reduced to a sharply defined incomplete pair-sieve discrepancy. `MC-472` shows that its complete joint period has no hidden sieve/character resonance. `MC-473`--`MC-475` close three direct incomplete continuations: exact divisor branching plus independent completion pays exponentially many branches, exact hard-mask Fourier `ell^1` has exponential spectral mass, and plain full-grid `ell^2`/Parseval pays the full primorial frequency dimension. `MC-476` further shows that the modern coefficient-uniform restriction theorem for sifted sets is blind to the translated-ratio character phase at zero frequency.

The representation layer of that restriction theory nevertheless survives. `MC-477` proves that every rational frequency in the Bera--Viswanadham/Ramaré--Ruzsa low-denominator envelope couples to

\[
K_h(n)=\chi(n+h)\overline{\chi(n)}
\]

for only `O(sqrt(p) log p)`, uniformly in the rational denominator. `MC-478` retains the exact pair-sieve local Fourier product and lowers the total absolute envelope coefficient cost to

\[
\ll \frac{z^2(\log(2z))^5}{G(z)}.
\]

`MC-479` closes unsigned transfer back to the exact mask: the Selberg envelope equals the hard indicator on genuine survivors, while its entire error is positive false-positive leakage, with order-one weight on explicit near-cutoff single-prime violations. `MC-480` then shows that complete-period coupling to `K_h` does not cancel this leakage; CRT reproduces its total positive mass with a minus sign.

`MC-481` closes the next apparent escape. If `A` is the hard mask, `beta` the envelope and `L=beta-A`, then after the canonical complete-period mean is removed from every `W`-periodic weight,

\[
\mathcal D_L(I)=\mathcal D_\beta(I)-\mathcal D_A(I).
\]

The quantity called `\mathcal E_{W,h}` in `MC-480` is exactly `\mathcal D_L`. Meanwhile `MC-478` plus the zero Fourier mode of the Bera--Viswanadham envelope already gives a conductor-sensitive bound for `\mathcal D_\beta`. Therefore a conductor-power estimate for centered leakage is, up to that already-cheap comparison term, the original exact rough×rough discrepancy itself. Centering the leakage does not create an independent transfer lemma.

`MC-482` then supplies a genuinely independent order-theoretic replacement: bracket the hard mask between lower and upper beta-sieve divisor sums and use their midpoint. The replacement error is bounded by the upper-minus-lower gap without first estimating the hard-mask discrepancy. Standard fundamental-lemma plus absolute interval-remainder bookkeeping, however, can make that gap conductor-power small only at a polylogarithmic sieve cutoff; a fixed-power cutoff forces incompatible demands on sieve depth and divisor level.

`MC-483` closes the immediate “make the bracket well-factorable and keep the phase” repair. For any pointwise bracket, the exact signed error has the form `(A-B)=theta(B^+-B^-)/2` with `|theta|<=1`. The selector `theta` exactly carries the hard-mask information not fixed by the bracket. Factorability of the upper/lower width therefore does not pass automatically to the signed replacement error: the phase-coupled source coefficient is `K_h theta`, not `K_h`. Without an independent theorem on the selector, taking absolute values returns precisely to the phase-blind gap priced in `MC-482`.

The low-denominator family remains analytically useful as a controlled comparison object, but the base-component bridge must now contain genuinely additional signed/factorable structure rather than merely a better norm estimate for `beta-A`, a deeper upper/lower bracket, or a stronger factorability class for the bracket width. The mixed rough/boundary and first-exit terms remain distinct, as do nonempty rough-block components and cross-component interference before positive closure.

## Research question

Can one construct an **exact signed/factorable error representation** for the hard pair-sieve channel, or prove a nontrivial structural theorem for the exact upper/lower selector, whose retained variables expose a conductor-sensitive estimate before coefficientwise absolute values? If not, can the needed gain instead be recovered from first-exit boundary terms, nonempty rough-block components, or pre-positive cross-component interference?

For the current Selberg envelope, merely proving

\[
\mathcal E_{W,h}(I)
=
\sum_{n\in I}K_h(n)(\beta-A)(n)
+\frac{|I|}{p}\overline{(\beta-A)}
\]

small is no longer an independent subproblem: `MC-481` shows that it directly solves the exact centered hard-mask discrepancy once the known envelope bound is inserted. For a two-sided bracket, merely proving that the gap has well-factorable divisor coefficients is likewise insufficient: `MC-483` shows that the actual signed error contains the additional source selector `theta`.

A useful replacement must therefore expose an exact decomposition, factorization, first-exit rule, selector theorem, or signed cancellation mechanism that supplies new estimable structure before either algebraic target-equivalence or bracket-width scalarization is invoked.

For nonempty components and boundary terms, retain their exact support and first-exit structure rather than importing the empty-vector positive-envelope analysis automatically.

## Why it may matter

The route has progressively removed apparent resources that were artifacts of representation or positive closure: favorable gcd sectors, generic well-factorability, residual coefficient signs, complete-period resonance, full inclusion-exclusion, hard-mask Fourier expansion, generic Hilbert-space averaging, coefficient-uniform restriction, unsigned Selberg-envelope accuracy, complete-period phase cancellation of leakage, centered leakage as an allegedly cheaper transfer target, and now factorability of an upper/lower bracket width without control of its signed selector.

What survives is sharper. The low-denominator envelope proves that the character phase can coexist with a polynomial spectral representation cost, and the two-sided beta-sieve shows that an independently priceable replacement exists at the order level. The failure lies in transporting either advantage to the exact hard mask at conductor-power accuracy without discarding the sign information that distinguishes the target. If an exact signed/factorable representation or a genuine selector theorem exposes additional internal cancellation before separate absolute values or positive closure, the route may still evade the full-primorial and level-depth obstructions. If no such retained structure exists, attention should redirect to boundary/nonempty components or cross-component interference.

## Decisive test

Work in the `R=T=1` empty-vector source frame unless explicitly testing one of the separate boundary/nonempty channels. For any proposed surrogate `B`, first write the exact identity relating `B`, `A`, and `B-A`. Do not credit smallness of `\mathcal D_{B-A}` as a transfer advantage if the only proof obligation is algebraically equivalent to `\mathcal D_A` modulo an already-controlled `\mathcal D_B`.

For any proposed upper/lower bracket `B^- <= A <= B^+`, also write the exact selector representation

\[
A-B=\frac12\theta(B^+-B^-),
\qquad |\theta|\le1.
\]

Do not credit well-factorability, programmable factorability, or another divisor-coefficient property of `B^+-B^-` as a property of the signed error unless the argument either removes `theta` by an exact identity or proves enough structure of the actual selector to preserve the needed phase-coupled estimate. If the proof eliminates `theta` only by `|theta|<=1`, price the resulting positive gap against the `MC-482` level-versus-accuracy tariff.

Accept a surrogate route only if it supplies additional exact structure that can be estimated independently: for example a finite signed factorization of `A-B` whose components retain source variables, a first-exit decomposition with a quantitatively smaller support/mass theorem, a structural representation of the exact selector, or a bilinear/dispersion identity in which the translated-ratio phase couples before coefficientwise absolute values. Price every surviving term against the conductor-sensitive envelope scale

\[
\frac{z^2(\log(2z))^5}{G(z)}\sqrt p\log(2p)
+\frac{H}{pG(z)},
\]

together with source interval length, shell summation, Fejér weights, coefficient normalization, endpoint separation and source depth.

For mixed/boundary terms, use the exact first-exit structure from `MC-470`; for nonempty pieces, retain the exact bin-product support pruning; for cross-component interference, retain the signed finite decomposition through the proposed transform and exhibit a concrete surviving cross term rather than appealing to cancellation after separate absolute bounds.

Kill any proposed repair whose only new content is a different majorant, centering, norm, deeper classical bracket, or stronger factorability class for the bracket width while the exact signed residual remains either target-equivalent to the hard mask or hidden behind an uncontrolled selector.

## Evidence boundary

`MC-477` proves a denominator-independent character estimate for each low-denominator rational mode. `MC-478` improves the aggregate envelope recombination using exact local pair-sieve Fourier factorization. `MC-479` proves that the current Selberg envelope is exact on survivors but has order-one false positives near the cutoff and only logarithmically suppressed unsigned leakage on the complete local period. `MC-480` proves that completing also in the conductor coordinate does not cancel that leakage. `MC-481` proves that after canonical centering the leakage discrepancy equals the difference between the controlled envelope discrepancy and the original exact hard-mask discrepancy.

`MC-482` proves that a classical two-sided beta-sieve midpoint is an independent replacement mechanism, but standard phase-blind fundamental-lemma bookkeeping forces a polylogarithmic cutoff for conductor-power transfer on polynomial source intervals. `MC-483` proves that factorability of an upper/lower bracket width alone does not repair that loss: the exact signed error contains a source selector that is equivalent to the hard-mask information left unresolved by the bracket.

None of these results supplies a conductor-power estimate for the exact rough×rough discrepancy, an exact signed factorable error decomposition, a useful theorem for the actual selector, boundary/nonempty components, or cross-component interference. `MC-481` and `MC-483` are accounting/information obstructions, not lower bounds or hardness theorems. No Möbius bound, zero-free region, or RH consequence has been obtained.

## Research disposition

The clue remains `accepted`, but three tempting transfer subproblems are now closed in their naive forms: centered Selberg leakage, phase-blind two-sided beta-sieve transfer at fixed-power cutoff, and factorability of the upper/lower gap without selector control. The immediate surviving question is whether the empty-vector channel admits an **exact signed factorable representation or nontrivial selector theorem** that retains the translated-ratio phase before scalarization; otherwise the conductor gain must come from first-exit boundary terms, nonempty components, or pre-positive cross-component interference.