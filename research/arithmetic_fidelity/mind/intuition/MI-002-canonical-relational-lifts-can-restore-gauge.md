# MI-002 — Canonical relational lifts can restore an intended gauge only after the residual fibre is classified

**Evidence level:** supported synthesis from exact finite harmonic/Euclidean/spectral models and the translation-total-positivity sequence [AF-371](../../findings/AF-371-hankel-positivity-vs-total-positivity-target-fidelity.md) through [AF-375](../../findings/AF-375-sampling-difference-subgroup-classifies-separable-determinant-gauges.md).

Information lost by scalar or quadratic compression need not require restoring absolute coordinates. A canonically available relation between surviving components can make the quotient faithful modulo an intended symmetry. The operative question is not “scalar versus high-dimensional” but the exact fibre left by the retained relations.

The finite models make this algebraic. A bispectrum can recover a finite abelian signal modulo translation when Fourier coefficients do not vanish; an exponent lattice leaves precisely its annihilator ambiguity; Gram data classify ordered Euclidean configurations modulo the appropriate orthogonal gauge, with orientation requiring only the residual torsor when it actually survives. These examples show why one should identify the ambiguity group before adding more observables.

AF-371--AF-373 give the analytic target-fidelity version. Hankel positivity can retain abundant source data yet fail Laguerre--Pólya membership, while Schoenberg translation total positivity tests the correct ordered relation. Fixed determinant order still leaves false positives (AF-372), so relational arity is a separate resource. On a declared exponentially decaying class, some thin sampling sets are determining (AF-373), so sampling geometry is another independent resource.

AF-374--AF-375 sharpen the sampling question from a qualitative warning into an exact gauge calculation. For row-sampling set `E`, let

`H_E = <E-E>`.

A positive continuous multiplicative factor is separable on the sampled Toeplitz kernel exactly when translation by `h in H_E` acts by a positive character. Hence:

- `H_E=aZ` leaves `p(t)=e^(lambda t) q(t)` with arbitrary positive continuous `a`-periodic `q`;
- dense `H_E` collapses every continuous separable ambiguity to the universal exponential tilt `C e^(lambda t)`.

For `E=aZ union (tau+aZ)`, rational `tau/a` merely refines the hidden period, while irrational `tau/a` makes `H_E` dense and kills every nonconstant periodic separable gauge. This is an exact **gauge-elimination** theorem, not a determining-set theorem: non-separable false-positive fibres may remain.

The resulting audit has four independent gates: choose the right relation; retain enough relational arity; choose sampling geometry whose generated relation group removes the intended gauge; and prove that the remaining fibre is target-pure in the actual source class. Killing a visible gauge is progress only at the third gate. It must not be promoted to source recovery or target fidelity without the fourth.

**Falsification criterion.** For a claimed relational repair, exhibit two admissible sources that agree on every retained relation but lie on opposite sides of the target property. For sampled total positivity specifically, dense `H_E` falsifies only periodic/separable multiplicative aliases; a non-separable false positive would show directly why gauge elimination is weaker than determination.
