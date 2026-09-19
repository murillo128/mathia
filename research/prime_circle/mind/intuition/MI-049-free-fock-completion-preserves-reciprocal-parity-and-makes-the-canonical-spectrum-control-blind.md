# MI-049 — Free-Fock completion and covariant source metrics preserve reciprocal control equivalence

**Evidence level:** exact synthesis from [PC-350](../../findings/PC-350-solvable-decoder-recovers-centered-radial-profile.md), [PC-351](../../findings/PC-351-triangular-development-is-spectrally-trivial-and-control-conjugate.md), [PC-355](../../findings/PC-355-free-fock-signature-tower-is-unitarily-control-blind.md) and [PC-356](../../findings/PC-356-source-induced-radial-gram-metrics-remain-matched-control-isometric.md), sharpening the finite-dimensional quotient audit of MI-047--MI-048.

Prime Circle already separates **source recovery** from **spectral discrimination**. The full Chen signature can retain the centered radial path, while triangular and semisimple finite-dimensional developments can lose the useful orientation under conjugacy-class spectralization. PC-355 shows that the canonical all-depth/free-Fock lift does not evade that obstruction merely by becoming infinite-dimensional in spirit.

Let the centered source alphabet carry the reciprocal parity involution `J`, and let the matched reciprocal path induce the corresponding algebra automorphism on the tensor signature. On the truncated full Fock space through degree `N`, second quantization gives a unitary `Gamma_N(J)` such that the left-regular signature operator satisfies

`L_N(tilde D)=Gamma_N(J) L_N(D) Gamma_N(J)^*`.

Therefore every unitary-conjugacy invariant of the canonical lift is exactly the same for the source and its matched reciprocal control: spectrum, singular values, pseudospectrum, numerical range, traces or determinants of admissible `*`-polynomials, and the corresponding invariants after adjoining the degree/vacuum/number structure preserved by second quantization.

The ordinary finite-level spectrum is even more degenerate. The signature has scalar term `1`, so

`L_N(D)=I+Q_N`,

where `Q_N` strictly raises tensor degree and is nilpotent on the truncation. Hence `Spec L_N(D)={1}` for every finite `N`, independently of the arithmetic source. Degree weights or enlarging the shell alphabet do not remove the parity covariance when they are functorial and parity-compatible.

PC-356 tests the most direct objection: perhaps the fixed one-particle metric is itself the source of the blindness. Let `T_S` map the centered shell alphabet to the actual radial derivative profiles and define the source-native energy metric

`G_S=T_S^*T_S`.

This Gram form is positive definite and can genuinely break parity: already for shells `{2,3}` the calibration/transverse cross term is `pi/sqrt(3)-2 != 0`, so `J^*G_SJ != G_S`. But the reciprocal matched control has radial realization `T~_S=T_SJ`, and applying the same native construction to it gives exactly

`G~_S=J^*G_SJ`.

Thus `J` is an isometry **between** the source and control Hilbert spaces even though it is not an isometry of the source metric to itself. Its tensor powers and second quantization again implement unitary equivalence of the corresponding Fock constructions. Spectra, singular values, pseudospectra, numerical ranges, resolvents and functorial `*`-polynomial spectral data remain matched-control blind.

The reusable obstruction is therefore **covariance**, not symmetry of a chosen metric. A source-dependent enrichment does not break a matched control if the enrichment is recomputed fairly on the control and is transported by the same involution as the underlying source data. Making the Hilbert geometry more source-native can still leave the entire destination isometric.

The surviving design space is more specific: a viable operator construction must introduce source-forced structure **before** the unitary spectral quotient that is not transported covariantly by reciprocal control. Candidates include an independently anchored domain, boundary condition, asymmetric coupling, canonical frame or other non-spectral covariant whose control-side reconstruction is not just the `J`-transport of the source object. Such asymmetry must itself have an arithmetic justification and survive a matched non-arithmetic reciprocal control.

**Boundary.** PC-356 rules out the Euclidean radial-energy Gram construction and, more generally, the inference that a parity-noncommuting source-native metric is automatically discriminating. It does not rule out every source-dependent Hilbert space, non-functorial refinement law, parity-breaking domain/boundary condition, non-spectral covariant retained before quotienting, or an infinite-dimensional operator whose spectral theorem is tied independently to zeta zeros. The obstruction applies when the source/control construction is covariant under the same reciprocal involution.
