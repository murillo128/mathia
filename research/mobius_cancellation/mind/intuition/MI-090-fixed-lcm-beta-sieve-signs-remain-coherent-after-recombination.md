# MI-090 — Fixed-lcm beta-sieve signs remain maximally coherent after recombination

**Evidence level:** exact combinatorial/harmonic synthesis from [MC-450](../../findings/MC-450-synchronized-lcm-frequencies-recombine-to-the-original-additive-autocorrelation.md) and [MC-451](../../findings/MC-451-beta-sieve-fixed-lcm-signs-are-maximally-coherent.md), extending the source-image occupancy audit of MI-089.

Exact dilation covariance can place different fixed-lcm slices on a common Fourier variable, but MC-450 shows that fully recombining those synchronized slices returns the original centered additive-difference autocorrelation. Generic dual Cauchy is therefore not an independent cancellation mechanism; it is the physical-space estimate in another coordinate system.

MC-451 removes the simplest signed-coefficient escape inside one such slice. For classical beta-sieve/Rosser--Iwaniec coefficients `lambda_d=mu(d) rho_d` with `rho_d>=0`, fix a squarefree lcm `L` and a coprime shift. Every compatible pair has `de=L`, so

`mu(d)mu(e)=mu(L)`.

All fixed-lcm coefficients consequently have the same sign. The zero mode of the recombined slice is maximally coherent: its absolute signed mass equals its total variation. In the resonant-band notation of MC-450, the strongest possible coherence parameter `eta=1` is forced rather than merely allowed.

The useful cancellation resource must therefore act **before total fixed-lcm recombination**. Well-factorability can still matter at the level of signed convolutional components, conductor factorization may interact with those components, and several lcm values may couple nontrivially before scalarization. What is closed is the hope that the ordinary Möbius signs of the final beta-sieve coefficients cancel the low-frequency fixed-lcm resonance by themselves.

The reusable lesson is that visible sign variation in the original divisor variables can disappear after the quotient imposed by the analytic destination. The sign geometry that matters is the one retained on the fixed-lcm fibre after the actual pairing constraints are enforced, not the nominal sign pattern of individual sieve coefficients.

**Boundary.** MC-451 concerns the recombined classical beta-sieve sign pattern on clean squarefree fixed-lcm fibres with the stated coprimality. It does not rule out cancellation among pre-recombination well-factorable pieces, cross-lcm coupling, conductor factorization, higher CRT/cycle structure, variable-length effects, or estimates using the detailed nonuniform character multiplier. No character-sum or Mertens improvement follows from the coherence statement alone.