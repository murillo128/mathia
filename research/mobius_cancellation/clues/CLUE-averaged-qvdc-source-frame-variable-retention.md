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
---

# Can an arithmetic Selberg variable be kept inside q-vdC before modewise collapse?

## Observation

`MC-382` shows that the current single-character Cochrane--Granville--Zheng recursion pays one square-root loss per conductor-scale layer, forcing an exponential-in-source-exponent saving tariff and hence a `log log y` analytic horizon. `MC-396` removes the earlier inverse-gap packing loss but leaves that `2^{O(A)}` tariff intact. `MC-383` shows that replacing individual estimates by a generic thin-family mean value is not enough when the theorem still charges a fixed positive power of one global modulus.

Julia Stadlmann's *On primes in arithmetic progressions and bounded gaps between many primes* (Advances in Mathematics 474 (2025), 110190; arXiv:2309.00425) gives a concrete nearby mechanism: her modified q-van der Corput argument retains an arithmetic summation variable inside differencing. In the proof sketch, the earlier treatment does not exploit the `y`-sum and its diagonal forces `Delta<N/Y^2`; after reorganizing the congruence so that both `n` and `y` remain inside q-vdC, the diagonal contributes `O(Delta N/Y)` and permits `Delta<N/Y`.

`MC-397` performs the corresponding pre-modewise source summation exactly in the present endpoint Selberg/Bombieri frame. The source-mode index is Fourier-dual rather than an arithmetic summation variable: summing it produces a source-signature weight, and the uniform source average becomes a multiplicative subgroup projector. Thus the source index itself cannot supply Stadlmann's retained-variable gain in this representation.

`MC-398` then tests the most literal Selberg-divisor escape inside the already-squared majorant. The two labels `(d_1,d_2)` enter the arithmetic inner sum only through `ell=[d_1,d_2]`; exact regrouping replaces the whole pair fiber by one scalar coefficient `C_g(ell)`. Therefore the pair labels themselves are also not independent arithmetic samples. The surviving standard-Selberg candidate is the single lcm/shell variable, unless a different pre-quadratic representation can exhibit arithmetic dependence that genuinely does not factor through the lcm.

## Research question

Can an **arithmetic variable that survives both exact collapses**—most naturally the lcm/shell variable `ell`, or a genuinely non-lcm-factorable variable exposed before the quadratic Selberg compression—remain inside q-vdC/Cauchy long enough to change the diagonal geometry in the way Stadlmann's retained `y` variable does?

The target is an exact representation of the endpoint frame quantity in which differencing acts before the surviving arithmetic variable is frozen or bounded trivially. A useful representation must produce a resource scaling qualitatively different from both known barriers: it must avoid the `2^{-Omega(A)}` terminal saving caused solely by sequential conductor depth and avoid a fixed positive global-radical tariff `P^theta` of the type ruled out in `MC-383`.

A direct structured estimate for the source-signature incidence operator also remains admissible, but only if its gain comes from arithmetic distribution/coupling not equivalent to Fourier-expanding the projector and reapplying the individual character estimates.

## Why it may matter

After `MC-396`, further block-packing inside the same single-character recursion can improve constants without changing the exponential source-depth scale. `MC-397` removes the easiest collective escape: averaging the source modes first is exactly a basis change to signature/coset incidence, not an additional oscillatory sample. `MC-398` removes a second bookkeeping escape: preserving the two Selberg divisor labels after the square has already been expanded does not preserve two arithmetic variables, because simultaneous divisibility factors exactly through their lcm.

The remaining Stadlmann analogy is therefore sharper. If the lcm/shell variable, or a truly pre-lcm arithmetic coordinate, changes the Cauchy diagonal count before the character recursion begins, it would attack the actual analytic bottleneck. If the lcm variable freezes without gain and every pre-quadratic candidate either re-collapses to lcm, recreates the individual q-vdC recursion, or leaves a global-modulus power cost, this entire retained-variable branch can be closed cleanly.

## Decisive test

Start from equation `(3)` or `(4)` of `MC-398`, where the standard Selberg divisor-pair fibers have already been compressed exactly to the lcm variable. Keep `ell` and the interval/shell variable explicit rather than applying triangle inequality term by term.

Derive one full Cauchy/q-vdC step with `ell` still live and count the resulting diagonal configurations exactly. The direction survives only if retaining `ell` produces a quantitative diagonal thinning analogous in mechanism to Stadlmann's `1/Y` gain and the off-diagonal term can still be controlled without paying either a sequential `2^{-Omega(A)}` source-depth tariff or a fixed positive power of the common radical.

A pre-quadratic alternative is admissible only if it passes the representation test from `MC-398`: the arithmetic phase, congruence, interval, or signature must distinguish the proposed divisor/source variables separately and must not factor through `[d_1,d_2]`. Merely retaining two labels before an exact lcm regrouping is rejected.

Also reject a candidate if the supposed extra average is only the source-mode index killed by `MC-397`, if Fourier expansion merely returns to the individual source characters, if arbitrary mode-dependent weights trigger the matched-filter obstruction of `MC-332`, or if the final family estimate has the fixed-global-modulus shape excluded by `MC-383`.

As the literature control, preserve the exact feature of Stadlmann's argument responsible for the gain: an arithmetic summation variable remains inside the differencing/Cauchy geometry and reduces the diagonal count. Similar terminology without that structural effect is not a valid transfer.

## Evidence boundary

No surviving arithmetic variable has yet been shown to yield a better endpoint character-sum estimate. Stadlmann's theorem concerns averaged prime distribution to smooth moduli in a different Type I setup and does not imply an endpoint source-cost theorem or improved Möbius cancellation.

`MC-397` resolves the source-index interpretation, and `MC-398` resolves the independent divisor-pair interpretation inside the standard squared Selberg majorant. Neither finding rules out a gain from the single lcm/shell variable nor from a genuinely non-lcm-factorable pre-quadratic representation. A structured direct estimate for the signature-incidence operator also remains open.

## Research disposition

The clue remains accepted but is narrowed again. The source-mode branch failed by exact finite Fourier orthogonality in `MC-397`; the standard Selberg divisor-pair branch failed by exact lcm-fiber compression in `MC-398`. The live question is now whether the **single surviving lcm/shell variable** changes q-vdC diagonal geometry, or whether a different pre-quadratic representation exposes an arithmetic variable that provably does not factor through lcm, while respecting `MC-332` and `MC-383`.