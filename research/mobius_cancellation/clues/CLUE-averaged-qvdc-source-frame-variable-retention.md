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
---

# Can an arithmetic Selberg variable be kept inside q-vdC before modewise collapse?

## Observation

`MC-382` shows that the current single-character Cochrane--Granville--Zheng recursion pays one square-root loss per conductor-scale layer, forcing an exponential-in-source-exponent saving tariff and hence a `log log y` analytic horizon. `MC-396` removes the earlier inverse-gap packing loss but leaves that `2^{O(A)}` tariff intact. `MC-383` shows that replacing individual estimates by a generic thin-family mean value is not enough when the theorem still charges a fixed positive power of one global modulus.

Julia Stadlmann's *On primes in arithmetic progressions and bounded gaps between many primes* (Advances in Mathematics 474 (2025), 110190; arXiv:2309.00425) gives a concrete nearby mechanism: her modified q-van der Corput argument retains an arithmetic summation variable inside differencing. In the proof sketch, the earlier treatment does not exploit the `y`-sum and its diagonal forces `Delta<N/Y^2`; after reorganizing the congruence so that both `n` and `y` remain inside q-vdC, the diagonal contributes `O(Delta N/Y)` and permits `Delta<N/Y`.

`MC-397` performs the corresponding pre-modewise source summation exactly in the present endpoint Selberg/Bombieri frame. The source-mode index is Fourier-dual rather than an arithmetic summation variable: summing it produces a source-signature weight, and the uniform source average becomes a multiplicative subgroup projector. Thus the source index itself cannot supply Stadlmann's retained-variable gain in this representation.

## Research question

Can an **arithmetic variable that survives the exact source-signature collapse**—most naturally the Selberg divisor variables, their lcm, or a finer shell/source arithmetic variable before that compression—remain inside q-vdC/Cauchy long enough to change the diagonal geometry in the way Stadlmann's retained `y` variable does?

The target is an exact representation of the endpoint frame quantity in which differencing acts before the surviving arithmetic variable is frozen or bounded trivially. A useful representation must produce a resource scaling qualitatively different from both known barriers: it must avoid the `2^{-Omega(A)}` terminal saving caused solely by sequential conductor depth and avoid a fixed positive global-radical tariff `P^theta` of the type ruled out in `MC-383`.

A direct structured estimate for the source-signature incidence operator also remains admissible, but only if its gain comes from arithmetic distribution/coupling not equivalent to Fourier-expanding the projector and reapplying the individual character estimates.

## Why it may matter

After `MC-396`, further block-packing inside the same single-character recursion can improve constants without changing the exponential source-depth scale. `MC-397` also removes the easiest collective escape: averaging the source modes first is exactly a basis change to signature/coset incidence, not an additional oscillatory sample.

The remaining Stadlmann analogy is therefore much sharper. If one of the arithmetic variables in the exact Selberg expansion changes the Cauchy diagonal count before the character recursion begins, it would attack the actual analytic bottleneck. If every such variable either freezes without gain, recreates the individual q-vdC recursion, or leaves a global-modulus power cost, this entire retained-variable branch can be closed cleanly.

## Decisive test

Start from equation `(9)` of `MC-397`, or from the finer pre-lcm Selberg expansion from which it is derived. Keep the sieve variables and interval/shell variable explicit rather than applying triangle inequality term by term.

Choose one concrete surviving arithmetic variable and derive one full Cauchy/q-vdC step with it still live. Count the resulting diagonal configurations exactly. The direction survives only if retaining that variable produces a quantitative diagonal thinning analogous in mechanism to Stadlmann's `1/Y` gain and the off-diagonal term can still be controlled without paying either a sequential `2^{-Omega(A)}` source-depth tariff or a fixed positive power of the common radical.

Reject a candidate if the supposed extra average is only the source-mode index killed by `MC-397`, if Fourier expansion merely returns to the individual source characters, if arbitrary mode-dependent weights trigger the matched-filter obstruction of `MC-332`, or if the final family estimate has the fixed-global-modulus shape excluded by `MC-383`.

As the literature control, preserve the exact feature of Stadlmann's argument responsible for the gain: an arithmetic summation variable remains inside the differencing/Cauchy geometry and reduces the diagonal count. Similar terminology without that structural effect is not a valid transfer.

## Evidence boundary

No surviving arithmetic variable has yet been shown to yield a better endpoint character-sum estimate. Stadlmann's theorem concerns averaged prime distribution to smooth moduli in a different Type I setup and does not imply an endpoint source-cost theorem or improved Möbius cancellation.

`MC-397` resolves only the **source-index** interpretation: pure source-mode averaging collapses to a signature projector. The sieve-divisor/lcm and other genuinely arithmetic retained-variable branches remain open, as does a structured direct estimate for the signature-incidence operator.

## Research disposition

The clue is accepted in this narrowed form. The initial source-mode branch failed its decisive test by exact finite Fourier orthogonality in `MC-397`; the live question is whether a surviving arithmetic Selberg/shell variable can alter the q-vdC diagonal geometry before modewise character estimation, while respecting `MC-332` and `MC-383`.