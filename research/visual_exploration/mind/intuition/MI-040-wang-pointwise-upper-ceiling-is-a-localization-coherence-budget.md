# MI-040 — Wang's upper pointwise ceiling has narrowed to infinite-tail finite-height coherence

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-311](../../findings/VIS-311-wang-weighted-gap-cubic-horizon.md), using Wang's displayed localization/mean-value identities, the classical weighted Hilbert inequality and the matched support/phase controls audited there.

The upper pointwise boundary in Wang's short-interval pair statistic has moved repeatedly because generic estimates were applied before the exact structure of their load-bearing terms was exposed.

VIS-298 removes the lower moving-source crossover by exact gamma recentering. VIS-299--VIS-304 then move the upper obstruction from localization leakage to the actual prime-power coefficient/frequency geometry, obtaining the absolute bound `x log log x=o(H)`.

VIS-305--VIS-308 successively preserve density, parity, exact prime-power support, coefficient magnitudes and finally all same-base multiplicative harmonic relations while randomizing cross-prime phase. Each matched control has signed remainder far below `H` at `H~x log log x`. Same-base multiplicative coherence is therefore not enough.

VIS-309 tests the actual deterministic common-time orbit `p -> p^(-it)`. For fixed `x,H`, rational independence of prime logarithms makes its Bohr quadratic mean exactly the completely multiplicative Haar mean. The resulting second moment is `O(x log^3(3x))`, so large signed remainders have vanishing long-time density at the candidate boundary. Generic deterministic cross-prime alignment is not the missing mechanism either.

VIS-310 asks how cheaply that Bohr cancellation can be transported to a finite height window. Hard truncate the infinite series at `Y`, control the tail uniformly and apply Montgomery--Vaughan to the retained ratio spectrum using only its global minimum gap. The optimized route gives `o(H^2)` at `H~x log log x` only when

`V >> x^5 log^3 x/(log log x)^2`.

That quintic horizon is explicitly a proof-method boundary: uniform tail control and worst-gap compression discard where the small coefficient energy actually lives.

VIS-311 preserves the local geometry of the retained spectrum. For a grouped frequency `lambda` with reduced rational height `m_lambda`, its inverse nearest-neighbor spacing costs only `Y m_lambda`, and Wang's exact taper gives

`sum_lambda m_lambda |B_lambda|^2 << x^2 log^3(3x)`.

The weighted finite-window estimate becomes

`V^(-1) integral |R_(x,H)(T)|^2 dT << xL^3 + H x^(5/2)L^(3/2)V^(-1/2)`

after optimizing the same hard cutoff. At `H~x log log x`, the sufficient horizon falls from quintic to cubic:

`V >> x^3 L^3/(log log x)^2`.

This identifies which part of VIS-310 was artificial. **Global-gap compression cost two powers of `x`; the remaining large polynomial loss is now tied to the uniform hard-tail representation.** The finite-window frontier is no longer “use coefficient-sensitive spacing”—that has been done. It is to control the infinite ratio tail in an energy-sensitive norm, or to prove that a sparse exceptional resonance defeats such a transfer.

The reusable lesson is a layered survivor test. Preserve the exact object until the first inequality that discards structure; match support statistics; preserve exact support; restore multiplicative phase relations; compare the true deterministic orbit with Haar; preserve local weighted frequency geometry; and finally avoid paying an infinite spectral tail in a norm much stronger than the destination average. A nominal finite-height critical scale becomes arithmetic only after the corresponding joint moving regime defeats all of those matched controls.

**Boundary.** VIS-309 is a Bohr-mean statement for fixed finite frequency data before the large-`x` limit. VIS-310 and VIS-311 give sufficient finite-window bounds, not lower bounds for true dephasing. VIS-311 still inherits the uniform tail estimate from VIS-310 and does not control a prescribed height, a joint limit `x=x(T)`, or pointwise cancellation at `H~x log log x`. Exceptional-height coherence remains open.