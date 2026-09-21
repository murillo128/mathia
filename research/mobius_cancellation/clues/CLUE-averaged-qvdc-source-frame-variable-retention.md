---
id: CLUE-mobius-cancellation-averaged-qvdc-source-frame-variable-retention
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-382-iterated-q-vdc-has-an-intrinsic-loglog-source-horizon.md
  - research/mobius_cancellation/findings/MC-383-small-doubling-family-mean-value-retains-global-modulus-horizon.md
  - research/mobius_cancellation/findings/MC-396-paired-block-packing-removes-inverse-gap-depth-tax.md
  - research/mobius_cancellation/findings/MC-397-source-mode-averaging-collapses-to-signature-projector.md
  - research/mobius_cancellation/findings/MC-398-selberg-divisor-pair-lcm-fiber-collapse.md
  - research/mobius_cancellation/findings/MC-399-lcm-retention-separates-from-source-qvdc-phase.md
  - research/mobius_cancellation/findings/MC-400-twisted-lcm-hyperbola-transform-is-mobius-invertible.md
  - research/mobius_cancellation/findings/MC-401-full-lcm-endpoint-is-signed-gcd-energy.md
  - research/mobius_cancellation/findings/MC-402-truncated-lcm-mask-is-mertens-weighted-divisor-energy.md
  - research/mobius_cancellation/findings/MC-405-mangoldt-quotient-self-coupling-needs-cross-scale-cancellation.md
  - research/mobius_cancellation/findings/MC-406-mangoldt-quotient-fibers-collapse-to-harmonic-mobius.md
  - research/mobius_cancellation/findings/MC-407-prime-error-increment-coupling-abel-collapse.md
  - research/mobius_cancellation/findings/MC-408-signed-pnt-error-correlation-is-rh-equivalent.md
  - research/mobius_cancellation/findings/MC-409-well-factorable-upper-sieve-preserves-prime-frame.md
  - research/mobius_cancellation/findings/MC-410-factorable-sieve-character-phase-is-mellin-separable.md
  - research/mobius_cancellation/findings/MC-411-fourier-completion-product-phase-is-dual-permutation.md
  - research/mobius_cancellation/findings/MC-412-zero-residue-well-factorable-degeneracy.md
  - research/mobius_cancellation/findings/MC-413-additive-differencing-complete-block-ramanujan-collapse.md
  - research/mobius_cancellation/findings/MC-446-source-frame-box-mean-square-has-quadratic-occupancy-threshold.md
  - research/mobius_cancellation/findings/MC-447-crt-source-frame-fibers-collapse-to-shift-common-primes.md
  - research/mobius_cancellation/findings/MC-448-fixed-lcm-fourier-weil-averaging-still-pays-polynomial-occupancy.md
  - research/mobius_cancellation/findings/MC-449-centered-complement-duality-closes-near-complete-fixed-lcm-escape.md
  - research/mobius_cancellation/findings/MC-450-lcm-frequency-synchronization-recombines-to-centered-autocorrelation.md
---

# Can actual source coefficients or a genuinely nonseparable pre-quadratic variable beat the source-depth barrier?

## Observation

The current single-character q-vdC route has an intrinsic source-depth tariff: `MC-382` isolates the repeated square-root conductor loss and `MC-383` shows that a generic family mean value does not by itself remove a fixed positive power of the global modulus. The useful comparison remains a q-van der Corput/dispersion mechanism that keeps an arithmetic variable alive long enough to change the diagonal count rather than merely rename the same scalar source mode.

The Selberg/lcm route has already consumed source-mode averaging, divisor-pair/lcm coordinates, moving-hyperbola truncation, incidence/GCD energies, quotient variables and Möbius--PNT-error couplings without an independent source-cost improvement (`MC-397`--`MC-408`). `MC-409` therefore changed the representation: a positive well-factorable upper linear-sieve weight preserves the prime-frame architecture while exposing coefficient factorization before triangle inequality. `MC-410`--`MC-412` show that raw multiplicative phase, ordinary completion and zero-residue progression structure are still separable or degenerate.

`MC-413` identifies the first surviving affine datum. Additive differencing creates incomplete translated correlations indexed by CRT starts and the lcm-dependent shift `a=hL^-1`; complete conductor blocks collapse to the divisor-independent Ramanujan scalar, so only the centered incomplete family can retain source phase.

`MC-446`--`MC-449` then close the most direct averaging repairs. Full `(u,a)` RMS cancellation costs effective occupancy about `q^2/H`; in the clean separated regime the frame map has no helpful hidden multiplicity and fixing `a` fixes the exact lcm; a one-lcm mixed-Weil Fourier envelope lowers the generic tariff to `p/H` but the CRT slice has only `2^omega(L)=p^o(1)` starts; and centered complement duality shows that moving `H` near a complete period does not evade the deficit. Uniform one-lcm Fourier/Parseval is therefore power-closed for every interval length.

`MC-450` closes the simplest remaining **cross-lcm Fourier synchronization**. For prime conductor, the exact covariance `widehat g_(h/L)(mL)=widehat g_h(m)` aligns every lcm slice on a common frequency `m`, but after the slices are summed the resulting coefficient is exactly the Fourier transform of the original centered additive-differenced sieve autocorrelation. Generic dual-space Cauchy is identical to generic physical-space Cauchy. The same finding also shows that a fixed-lcm CRT start set has a deterministic near-zero resonant band unless its actual signed coefficients already cancel, so unweighted support geometry is not automatically Fourier-flat.

The surviving question is therefore no longer whether another coordinate, ambient moment, lcm label, frequency relabeling or interval endpoint can expose hidden averaging. It is whether **actual arithmetic coefficients or conductor factorization change the diagonal/off-diagonal problem before those structures are recombined away**.

## Research question

Two branches remain legitimate.

First, can the actual Selberg/source structure inside the truncated lcm form produce a theorem genuinely stronger than generic cutoff inversion? A surviving result must exploit the real coefficient `g`, the source-signature family, or a collective bilinear relation among the incidence energies and, after full bookkeeping, avoid both the sequential source-depth tariff and a fixed positive common-radical cost. Merely rewriting the cutoff through `MC-402` and inserting unavailable Mertens cancellation does not qualify.

Second, can the well-factorable upper-sieve branch exploit structure that disappears under the full recombination classified by `MC-450`? The live possibilities are now narrower: prove cancellation in the **actual signed factorable coefficients** before they recombine into the nonnegative sieve autocorrelation; prove a restricted spectral/dispersion estimate using correlation between those coefficients and the translated-character multiplier rather than only support size; retain several lcm/factor variables in a bilinear form whose true diagonal is parametrically smaller before generic Cauchy; factor a smooth/composite source conductor during a genuine q-vdC `A`-process; or find a quantitatively useful wraparound/nonunit-shift regime outside the clean `MC-447` hypotheses.

A variable surviving in notation is not enough. The desired mechanism must change usable arithmetic information before scalarization, rather than provide a reversible, Abel-equivalent, Fourier-equivalent, residue-permutation-equivalent, complete-period-equivalent, ambient-L2-equivalent, CRT-fibre-equivalent, uniform-Fourier-envelope-equivalent, complement-equivalent, or lcm-frequency-synchronization-equivalent representation.

## Why it may matter

The chain now separates several issues that were previously conflated. Incomplete translated characters genuinely cancel collectively; conditioning on an lcm genuinely improves a generic analytic tariff; the actual fixed-lcm source image is too sparse to pay that tariff at conductor-power scale; near-complete intervals are just complementary short intervals after centering; and aligning many lcm Fourier multipliers is an exact reparameterization of the original centered correlation if followed by generic recombination.

A positive result that keeps well-factorable components or conductor factors alive through a nontrivial dispersion step would therefore be qualitatively new for this branch: it would use arithmetic information that every closure result above explicitly discards. Conversely, if the factorable components themselves can be shown to obey an unavoidable conductor-power diagonal after the sharpest admissible dispersion, the well-factorable/q-vdC route would be close to a genuine closure rather than merely lacking a stronger individual character-sum estimate.

## Decisive test

For the truncated-lcm branch, exhibit a nontrivial bound for the source form or a collective source-signature/bilinear estimate and identify the ingredient absent for generic coefficients and a generic quadratic character. Propagate it through every source-depth factor, common-radical power, exceptional set, logarithmic loss and truncation error. Reject any argument whose only gain is one of the already classified coordinate changes in `MC-397`--`MC-408`.

For the well-factorable branch, begin from the centered incomplete correlation of `MC-413` and treat `MC-446`--`MC-450` as hard controls. A fixed-lcm theorem must use more than `max_t |widehat f_a(t)|=O(sqrt(p))`, support cardinality or a near-complete interval. A multi-lcm theorem must use more than the exact reindexing `t=mL`: if the slices are first synchronized, fully recombined into the single residue coefficient, and then generic Cauchy is applied, `MC-450` proves that nothing has been gained.

A surviving continuation should instead write the factorable coefficient decomposition explicitly and prove a dispersion/bilinear estimate **before full recombination**, with a diagonal/off-diagonal count that is strictly better than the current source-depth budget. Alternatively it should factor the source conductor during the q-vdC process and show quantitatively that the reduced conductor survives all later summations. For a detailed fixed-lcm Fourier proposal, it must exploit actual signed coefficient cancellation or a nonuniform correlation with the translated-character multiplier; the bare CRT start set is insufficient because of the resonant band in `MC-450`.

Reject continuations that apply individual incomplete character bounds pair-by-pair, use the full ambient box and fail `MC-446`, credit collisions excluded by `MC-447`, use only the uniform fixed-lcm envelope of `MC-448`, invoke near-completion without `MC-449`, or present lcm-frequency synchronization followed by generic `L^2` as a new averaging mechanism after `MC-450`.

## Evidence boundary

No theorem using the actual Selberg lcm coefficient has changed the source-cost scaling, and no factorable-upper-sieve estimate has yet beaten the existing source-character bound. `MC-409` establishes the alternative positive frame; `MC-410`--`MC-413` classify successive separable, degenerate and complete-period reductions.

`MC-446` is an exact ambient two-variable moment calculation, `MC-447` exact CRT fibre algebra, `MC-448` a finite Fourier/Weil consequence for one fixed-lcm prime-conductor slice, `MC-449` an exact centered complement identity, and `MC-450` an exact Fourier-dilation/recombination obstruction. None proves that coefficient-specific dispersion or conductor factorization cannot work. In particular, `MC-450` deliberately distinguishes generic recombination from a theorem that keeps signed well-factorable components separate long enough to change the diagonal.

Smooth/composite modulus factorization, a genuinely coefficient-sensitive pre-recombination dispersion estimate, collective variable-length structure, and wraparound/nonunit-shift regimes remain unexploited. The scalar Möbius--PNT-error branch remains classified by `MC-408` as RH-equivalent at the target exponent.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-450`**. Ambient averaging, hidden frame multiplicity, a free shift coordinate, uniform one-lcm Fourier-Weil control, the near-complete endpoint, and bare cross-lcm frequency synchronization are all classified and cannot supply a conductor-power gain by themselves.

The live well-factorable question now requires a genuinely pre-recombination mechanism: actual signed coefficient cancellation, a restricted dispersion theorem with a smaller true diagonal, or source-conductor factorization. Detailed CRT Fourier geometry remains live only when tied to those actual coefficients or to nonuniform multiplier correlation; the unweighted/start-set geometry alone is not enough. The independent truncated-lcm/source-specific branch remains open.