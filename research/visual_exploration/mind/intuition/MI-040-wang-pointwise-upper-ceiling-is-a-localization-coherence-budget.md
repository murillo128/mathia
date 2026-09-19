# MI-040 — Wang's upper pointwise ceiling has narrowed to aggregate-density finite-height coherence on a dense ratio spectrum

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-312](../../findings/VIS-312-wang-dense-ratio-spectrum-no-nearest-spacing.md), using Wang's displayed localization/mean-value identities, the classical weighted Hilbert inequality and the matched support/phase controls audited there.

The upper pointwise boundary in Wang's short-interval pair statistic has moved repeatedly because generic estimates were applied before the exact structure of their load-bearing terms was exposed.

VIS-298 removes the lower moving-source crossover by exact gamma recentering. VIS-299--VIS-304 then move the upper obstruction from localization leakage to the actual prime-power coefficient/frequency geometry, obtaining the absolute bound `x log log x=o(H)`.

VIS-305--VIS-308 successively preserve density, parity, exact prime-power support, coefficient magnitudes and finally all same-base multiplicative harmonic relations while randomizing cross-prime phase. Each matched control has signed remainder far below `H` at `H~x log log x`. Same-base multiplicative coherence is therefore not enough.

VIS-309 tests the actual deterministic common-time orbit `p -> p^(-it)`. For fixed `x,H`, rational independence of prime logarithms makes its Bohr quadratic mean exactly the completely multiplicative Haar mean. The resulting second moment is `O(x log^3(3x))`, so large signed remainders have vanishing long-time density at the candidate boundary. Generic deterministic cross-prime alignment is not the missing mechanism either.

VIS-310 asks how cheaply that Bohr cancellation can be transported to a finite height window. Hard truncate the infinite series at `Y`, control the tail uniformly and apply Montgomery--Vaughan to the retained ratio spectrum using only its global minimum gap. The optimized route gives `o(H^2)` at `H~x log log x` only when

`V >> x^5 log^3 x/(log log x)^2`.

VIS-311 preserves local geometry of the retained finite spectrum. Its coefficient-weighted spacing estimate removes two powers of `x`, lowering the sufficient window to

`V >> x^3 log^3 x/(log log x)^2`.

That improvement isolates global-gap compression as a proof cost, but it does not identify an infinite-spectrum norm.

VIS-312 closes the direct passage `Y->infinity` in the same nearest-neighbor functional. Cross-base prime quotients already give a dense set of supported log-frequencies, and the Wang kernel removes only a discrete lattice. Therefore the **nonzero grouped coefficient support is dense in `R`**. For every fixed retained frequency `lambda_0`, its finite-cutoff nearest-neighbor spacing `delta_(lambda_0,Y)` tends to zero as `Y->infinity`; for a fixed cross-base coefficient that stabilizes once its primes are included,

`|B_(lambda_0)|^2/delta_(lambda_0,Y) -> infinity`.

Hence the weighted VIS-311 quantity `sum |B_lambda|^2/delta_lambda` has no finite cutoff-free limit. This divergence is a representation failure, not evidence that the true finite-window mean square is large.

The reusable point is now sharper than “use an energy-sensitive tail.” On a dense ratio spectrum, **pointwise frequency isolation is itself the wrong infinite-dimensional currency**. A cutoff-free transfer must aggregate frequencies before inversion: local density in smooth/dyadic blocks, a large-sieve/nonharmonic-Fourier inequality based on interval counts, or direct summation of the finite-window kernel `min(V,1/|lambda-mu|)` against the coefficient energy. Such a representation can still fail if a sparse near-resonant packet carries enough Wang mass; VIS-312 only says the nearest-neighbor denominator cannot decide that question.

The survivor test is therefore layered. Preserve exact coefficient/support data; preserve multiplicative phase relations; compare the true common-time orbit with Haar; price finite-height transport using coefficient energy; and, when the support becomes dense, replace individual gaps by an aggregate-density quantity before interpreting a large required window as arithmetic coherence.

**Boundary.** VIS-312 proves density of the full supported ratio spectrum and divergence of the VIS-311 nearest-neighbor functional. It does not give a quantitative collapse rate for each gap, a lower bound on the true averaging horizon, a prescribed-height cancellation theorem, or a joint `x=x(T)` result. Aggregate density/energy control and exceptional-height resonance remain open.
