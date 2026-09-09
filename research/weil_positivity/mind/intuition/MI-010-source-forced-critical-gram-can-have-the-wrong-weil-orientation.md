# MI-010 — A source-forced critical Gram can have the wrong Weil orientation in essential spectrum

**Evidence level:** exact Bost--Connes critical Gram, exact Poisson-score identification, and Toeplitz essential-spectrum obstruction through WP-218

## Core intuition

Matching the critical half-density, the prime logarithmic scale, and a canonical positive source geometry is still not enough for Weil positivity. The sign theorem depends on **orientation**, and the current Bost--Connes candidate has the wrong orientation at the level of essential spectrum rather than merely through one isolated negative direction.

This changes the completion requirement. A compact boundary repair cannot fix the source Gram while preserving its prime-axis bulk. A viable construction must change the essential operation itself, couple the prime axes noncompactly to additional source structure, or justify a test-space restriction that removes the negative Weyl sequences before the Weil consequence is identified.

## Strongest justified principle

WP-216 proves that normalized Bost--Connes divisibility projections at `beta=1` generate the positive GCD Gram. On each prime axis its Toeplitz coefficients are exactly `p^{-|a-b|/2}`, and the source dynamics supplies the scale `log p`. The finite Weil target nevertheless has local ray `log p(I-G_p)`, which is indefinite.

WP-217 identifies the canonical Bochner and temperature-score route exactly. The Gram's spectral probability measure is the Prime-Torus Poisson measure with `sigma=beta/2`; differentiating the log density at the source critical point cancels the prime-power repetition factor and reproduces the finite-prime Weil cosine comb. This is an exact redirect to the already-audited signed Poisson score, not a new positive orientation.

WP-218 shows that the sign defect is stable in the Calkin algebra. The prime-axis operator `W_p=log p(I-G_p)` is Toeplitz with a continuous sign-changing symbol, so its essential spectrum contains a nontrivial negative interval. Weyl invariance implies that every compact or relatively compact self-adjoint correction leaves that negative essential spectrum unchanged. Finite-dimensional baths, compact boundary variables, compact centering corrections, and finite-sector Schur complements therefore cannot turn the same bulk operator positive.

## Counterevidence / boundary

The obstruction is prime-axis and compact-perturbative. It does not rule out a genuinely noncompact mixed-prime coupling, a finite--archimedean completion that changes the essential symbol, an unbounded/domain-sensitive operation, or an independently justified restricted test space on which the negative Weyl sequences are absent.

Nor does WP-217 say that information geometry is useless in every completion. It says that the ordinary canonical score of the conditioned Gram is already the known Poisson-score route and therefore adds no new sign source by itself.

## Epistemic status

**Exact source-forced critical magnitude, exact score classicalization, and exact negative essential-orientation obstruction stable under compact completion; a noncompact/global sign-producing operation remains open.**

## Falsification criterion

Refute the conditioned Gram/Poisson identification, the equality of the local Weil ray with `log p(I-G_p)`, or the negative essential-spectrum calculation. A positive continuation should identify a source-forced operation that changes the essential prime-axis orientation or legitimately removes its negative Weyl sequences while simultaneously producing the finite-prime, archimedean, and polar normalization needed by the completed Weil form.
