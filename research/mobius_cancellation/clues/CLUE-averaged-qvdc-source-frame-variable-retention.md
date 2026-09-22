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
---

# Can a pre-positive factor-specific dispersion transform break the Möbius source-frame quotient?

## Observation

The direct source-frame repairs are now tightly classified. `MC-446`--`MC-450` show that ambient box averaging, hidden CRT multiplicity, one-lcm Fourier/Weil control, near-complete intervals, and bare cross-lcm frequency synchronization do not pay the conductor-power occupancy tariff. The surviving gain must use arithmetic information before generic recombination or positive quadratic closure.

The coefficient side is equally restrictive. `MC-451` shows that the fixed-lcm beta-sieve signs are coherent rather than self-cancelling; `MC-452` shows that raw truncated Möbius is not a standard well-factorable weight; `MC-453` shows that a bounded decomposition into factorable components buys only a bounded constant if the components are separately closed by positive quadratic norms. `MC-454` then identifies the core quotient obstruction: internal tuples such as `(r1,r2,r1',r2')` create no new source occupancy while the kernel depends only on their products `(d,e)`.

`MC-455` tests the obvious conductor-factorization escape and proves that standard source-only q-van-der-Corput steps still factor through `(d,e)` when their conductor splits and shifts are chosen independently of the internal coefficient representative. Conductor reduction is real, but it is not automatically a factor-level source mechanism.

`MC-456` supplies the first positive structural precedent from modern prior art. In Pascadi's triply-well-factorable prime-distribution method, and in Yang's 2026 convolution-type use of it, the factor variables are themselves factors of the progression modulus. Linnik dispersion and completion keep those blocks in different arithmetic roles and produce reciprocal/Kloosterman phases that are not constant on a fixed total-product fibre. This validates the *shape* of the escape condition while also exposing the mismatch with the present fixed external character conductor.

`MC-457` now tests the most direct transfer ordering: keep one internal sieve factor as a separate congruence modulus and complete the translated source sum before recombining it. Because every surviving sieve factor is coprime to the fixed primitive-character conductor, the mixed modulus is a CRT product. Complete blocks tensorize exactly: every nonzero Fourier mode of the factor congruence vanishes and the zero mode is the same Ramanujan correlation `c_q(h)`. Separate factor residues survive only in the incomplete mixed tails.

## Research question

Does the exact pre-recombination well-factorable source form underlying `MC-409`/`MC-413` admit any legitimate **incomplete** dispersion, reciprocity, Poisson/completion, or conductor-coupling order in which two internal factorizations of the same divisor products acquire analytically different source kernels *before* the CRT tensorization of `MC-457` or the positive closure of `MC-453`?

Concretely, can one derive a transformed kernel `K(z;xi)` for internal label `z=(r1,r2,r1',r2')` such that two labels with the same products `r1 r2=d` and `r1' r2'=e` give different kernels on a non-negligible source/dual set, with the distinction surviving the later diagonal/off-diagonal bookkeeping? A useful analogue of the Pascadi/Yang architecture would put disjoint factor blocks into distinct modulus or reciprocal-phase positions in a way that prevents the fixed-conductor source coordinate and the coefficient-factor coordinate from tensorizing.

A second branch remains legitimate but separate: source-only conductor reduction could still win without quotient breaking if the reduced-conductor estimate is quantitatively strong enough to beat the existing product-level occupancy cost after every later summation.

## Why it may matter

The prior-art comparison removes an important ambiguity. Well-factorability is not useful because a coefficient has many convolution representations; successful neighboring theorems use it because the factors enter the arithmetic constraint before dispersion and remain visible in a structured oscillatory kernel. That is qualitatively different from all routes closed by `MC-446`--`MC-457`.

A positive transfer would therefore expose genuinely new usable information in the current branch rather than another reparameterization. A negative transfer theorem showing that the fixed external character conductor forces every admissible pre-positive transform to remain product/lcm-level or CRT-tensorized would, conversely, close the most plausible modern factorable-dispersion escape and leave only a source-only quantitative improvement or a materially different representation.

## Decisive test

Start from one genuine well-factorable component of the centered incomplete correlation in `MC-413`, *before* the multiplication quotient is restored. Keep its internal factor variables explicit and keep the factor-conditioned source intervals incomplete through the first nontrivial dispersion/Cauchy/reciprocity step.

The structural admission test is fibre separation **before full mixed completion**: exhibit a justified transformed phase, congruence, interval, or source kernel that is not constant on the map `(r1,r2,r1',r2')->(d,e)` and that is not merely a nonzero Fourier mode of an independent coprime residue mask destined to vanish by `MC-457`. The Pascadi/Yang template in `MC-456` remains the comparison control: there, separately factorized modulus blocks survive dispersion/completion into reciprocal phases such as `e(h overline(ell d)/c)`. Merely splitting an external conductor as in `MC-455`, or merely retaining a coprime factor residue through complete source analysis as in `MC-457`, does not pass the test.

If fibre separation is obtained, carry the exact transformed form through Cauchy, completion, exceptional sets, common-radical factors, and the true diagonal. The route survives only if the final bound has a strict quantitative gain over the current source-depth/occupancy budget. If every legal ordering can be shown to factor through `(d,e)`, `[d,e]`, or a CRT tensor product before the first useful estimate, record that as the closure result instead.

For the independent source-only branch, propagate the best admissible reduced-conductor estimate through the existing product-level summation and require an actual net conductor-power gain after all losses; an improved individual character sum that is consumed by occupancy does not qualify.

## Evidence boundary

`MC-456` is a literature-backed transfer classification, not a theorem about the Möbius kernel. Pascadi and Yang show that factor-specific modulus geometry can power successful dispersion estimates in arithmetic-progression problems; they do not show that the current divisor-factor variables can be inserted into the fixed-conductor translated-character source geometry.

`MC-457` is an exact finite CRT/Fourier obstruction for one natural attempted insertion: a separate sieve factor used only as an additional coprime residue modulus contributes no nontrivial factor mode on complete mixed blocks. It does not classify genuinely incomplete dispersion or a transform that entangles the factor modulus with the source before completion.

No theorem yet supplies surviving fibre separation for the exact incomplete `MC-413` kernel, and no source-only conductor estimate has yet been propagated to a winning global budget. The accepted clue therefore remains open, but generic factor counting, bounded coefficient splitting, independent q-vdC conductor factorization, and full completion of an independent factor residue are no longer live escapes.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-457`**. The live well-factorable branch is now an incomplete pre-tensorization transfer problem: either derive a Pascadi/Yang-style dispersion step while factor-conditioned source tails remain coupled, producing a non-tensor factor-specific kernel, or prove that the fixed external conductor forces those tails to recombine before any useful estimate. Generic internal-factor multiplicity, source-only q-vdC after product collapse, and complete factor-residue completion are closed by `MC-454`--`MC-457`.

The independent source-only branch remains open only as a quantitative question: reduced conductor must beat the full product-level occupancy budget without crediting internal factor labels.