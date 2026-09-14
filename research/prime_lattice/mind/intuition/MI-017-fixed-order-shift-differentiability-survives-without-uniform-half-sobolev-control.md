# MI-017 — Zero-order shift transport needs coupled source-specific BV coercivity, not spectral stability

**Evidence level:** supported by [PL-297](../../findings/PL-297-renormalized-hadamard-stress-hhalf-decoupling.md)--[PL-302](../../findings/PL-302-suzuki-prime-comb-sharp-bv-contraction-threshold.md). The needed uniform BV/derivative-measure estimate for the actual completed-Weil ground branch remains open.

PL-297 separates the renormalized Hadamard boundary stress from the critical Fourier first moment: the stress can converge while the zero extensions diverge in `H^(1/2)`. PL-298 nevertheless gives `C^1` translation autocorrelations at every fixed positive fractional order, and PL-299 transports them to zero order on the pure principal branch using uniform convergence plus uniform bounded variation rather than half-Sobolev control.

PL-300 shows why ordinary Hilbert-space stability cannot supply that currency. Norm-small self-adjoint perturbations can preserve a unique simple isolated ground branch and uniform state convergence while injecting tiny-amplitude, huge-variation oscillations that make a prescribed shift derivative diverge.

PL-301 checks the exact Suzuki remainder against that adversary and removes one false obstruction. Compressed prime-power shifts are total-variation nonexpansive channel by channel, and the archimedean completion maps `L^1` uniformly into `BV`. The rough high-frequency packet mechanism of PL-300 therefore cannot be hidden in the actual lower-order remainder.

But BV stability is not BV coercivity. PL-302 proves that the finite arithmetic shift comb itself ceases to be a contraction exactly when the `n=3` channel becomes active: endpoint-localized test functions give an operator-norm lower bound above one for every `a>log(3)/2`, including the working `a=0.8` aperture. No sharper shift-only norm estimate can close the branch there.

The missing resource is now precise: a **coupled eigen-equation mechanism** in which the principal logarithmic/fractional operator, finite prime shifts, completion smoothing and the tracked ground state jointly control derivative measure. A useful theorem may be a principal resolvent estimate that absorbs the comb, cancellation between source channels, graph-norm coercivity, or a direct variation inequality on the eigenbranch. Generic Kato tracking and standalone remainder boundedness are both too weak.

The reusable distinction is between spectral identification, BV transport and BV coercivity. The first says which state is followed; the second says the exact remainder does not manufacture arbitrary variation from nowhere; only the third can prevent the tracked state from accumulating large variation through the coupled equation.

**Boundary.** PL-301--PL-302 do not prove uniform BV of the completed-Weil branch and do not resolve the independent source-specific sign gate. The endpoint test used in PL-302 acts on unrestricted BV data and does not rule out contraction or cancellation on the actual ground-state manifold produced by the full operator.