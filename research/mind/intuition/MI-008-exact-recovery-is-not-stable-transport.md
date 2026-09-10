# MI-008 — Stable target transport depends on the actual composed map, not local recoverability or smoothing alone

**Evidence level:** supported cross-line synthesis from cancellation-coherent sampling, Nyman closure, finite-seam transport, and Xi observability/source boundaries

## Core intuition

Exact representation, exact state recovery, local smoothing, or a favorable limiting operator does not determine whether the final target is transported stably. The missing quantity often lives in the composition between stages: cancellation may be broken, a quotient may erase the target, a positive component may impose a floor, or an observation map may be exponentially ill-conditioned.

A local theorem should therefore be trusted only after its gain survives the **actual finite/global map** that produces the target currency.

## Strongest justified principle

Arithmetic Fidelity makes cancellation coherence explicit. AF-237--AF-243 show that local source truncations can manufacture a false Li root rate by cutting a global cancellation orbit. AF-245--AF-247 then show that sparse output observability has its own phase-recurrence criterion; fewer faithful outputs do not make source construction cheaper.

Nyman--Beurling gives the quotient analogue. NB-027 finds source-selected coefficient mass transverse to restricted adjacent matchings, but NB-028--NB-029 show that the unrestricted adjacent quotient collapses the signal and that all adjacent differences together span the full Nyman closure. A useful local nuisance direction cannot be extrapolated to an unrestricted quotient without checking the target-bearing closure.

Prime Flute is now the cleanest smoothing counterexample. PF-258--PF-260 prove a genuine fixed-axis fractional window with `R>1`, and PF-261--PF-267 give strong finite-seam Green control. Yet PF-268 proves that the positive lowest mass pole alone makes the **bare finite-seam** separated operator unbounded for every `R>1`. The local smoothing margin survives only if the normalized Robin or spatial propagation map changes the obstruction before endpoint weighting.

Xi Flow supplies the conditioning version. XF-159 shows that even continuum blind-region data remain exponentially transition-insensitive under subexponentially conditioned decoders. XF-162 finds a true Xi-specific source-tail discriminator, but no theorem yet propagates that tail information through the heat/source map into transition visibility.

## Program consequence

Estimate the composed target map in its final normalization. For a limiting/local gain, prove the uniform finite-scale transport theorem; for a quotient, prove that target-bearing closure survives; for sparse output, separate observability from source cost; for source regularity, prove that the regularity enters the transition rather than only the far tail.

## Counterevidence / boundary

The failures are category-specific. Prime Flute may recover a margin after the combined normalized Robin/spatial map; Nyman may isolate a genuinely target-poor low-energy subspace; Xi may have a source identity transporting tail rigidity inward. Those possibilities reinforce rather than weaken the need to analyze the exact composition.

## Epistemic status

**Supported distinction between local correctness and stable transport, strengthened by an exact case where a real fixed-axis smoothing gain fails after the bare finite-seam map.**

## Falsification criterion

Produce a final theorem in one cited setting while bypassing the identified cancellation, closure, finite-seam, or conditioning modulus without adding new source structure, or invalidate an exact map/boundary on which the synthesis relies.