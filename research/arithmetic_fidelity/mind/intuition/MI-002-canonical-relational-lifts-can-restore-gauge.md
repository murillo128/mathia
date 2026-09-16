# MI-002 — Canonical relational lifts can restore an intended gauge only after the residual fibre is classified

**Evidence level:** supported synthesis from exact finite harmonic/Euclidean/spectral models and the translation-total-positivity sequence [AF-371](../../findings/AF-371-hankel-positivity-vs-total-positivity-target-fidelity.md) through [AF-376](../../findings/AF-376-uniform-separation-defeats-e-polya-frequency-determination.md).

Information lost by scalar or quadratic compression need not require restoring absolute coordinates. A canonically available relation between surviving components can make the quotient faithful modulo an intended symmetry. The operative question is not “scalar versus high-dimensional” but the exact fibre left by the retained relations.

The finite models make this algebraic. A bispectrum can recover a finite abelian signal modulo translation when Fourier coefficients do not vanish; an exponent lattice leaves precisely its annihilator ambiguity; Gram data classify ordered Euclidean configurations modulo the appropriate orthogonal gauge, with orientation requiring only the residual torsor when it actually survives. These examples show why one should identify the ambiguity group before adding more observables.

AF-371--AF-373 give the analytic target-fidelity version. Hankel positivity can retain abundant source data yet fail Laguerre--Pólya membership, while Schoenberg translation total positivity tests the correct ordered relation. Fixed determinant order still leaves false positives (AF-372), so relational arity is a separate resource. On a declared exponentially decaying class, some thin sampling sets are determining (AF-373), so sampling geometry is another independent resource.

AF-374--AF-375 classify one exact sampled-kernel gauge. For a row-sampling set `E`, let `H_E=<E-E>`. A positive continuous multiplicative factor is separable on the sampled Toeplitz kernel exactly when translation by `h in H_E` acts by a positive character. Thus `H_E=aZ` leaves an arbitrary positive periodic factor modulo exponential tilt, while dense `H_E` collapses every continuous separable ambiguity to `C e^(lambda t)`. In particular, an irrational second lattice phase kills the nonconstant periodic separable gauge.

AF-376 shows why that classification is not yet a determination theorem. A second geometric quantity matters independently:

`Delta_E = inf{|u-v| : u,v in E, u != v}`.

If `Delta_E>0`, every bounded nonnegative nonzero function supported in an interval shorter than `Delta_E` is `E`-Pólya-frequency at **all** determinant orders: the row-support intervals are disjoint and ordered, so each sampled matrix has at most the identity Leibniz term. Yet no such nonzero compactly supported integrable function is a full Pólya-frequency function. Hence a uniformly discrete `E` admits an infinite-dimensional non-separable target-changing fibre whenever the source class permits these local controls.

For `E=aZ union (tau+aZ)` with irrational `tau/a`, both facts hold simultaneously: `H_E` is dense, so the AF-374/375 periodic gauge disappears, but `Delta_E>0`, so AF-376 still produces exact all-order sampled false positives on Ganzburg's broad exponentially decaying class `L`. Dense generated differences and dense *actual samples* are different resources.

The resulting audit has at least five independent gates: choose the right relation; retain enough relational arity; classify the actual sampling geometry; classify the generated gauge group; and prove that the residual fibre is target-pure in the declared source class. Killing a visible gauge is progress only at the gauge gate. It must not be promoted to target fidelity without the final determination theorem.

**Falsification criterion.** For a claimed relational repair, exhibit two admissible sources that agree on every retained relation but lie on opposite sides of the target property. For sampled total positivity, `Delta_E>0` plus an admissible compact-support control kills determination immediately, regardless of whether `H_E` is dense. A successful repair must exclude that fibre by justified source rigidity or use a sampling set whose actual local spacing supplies a genuine determining theorem.
