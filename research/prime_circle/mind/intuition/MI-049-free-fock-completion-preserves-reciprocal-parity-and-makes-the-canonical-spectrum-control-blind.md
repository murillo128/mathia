# MI-049 — Free-Fock completion preserves reciprocal parity and makes the canonical spectrum control-blind

**Evidence level:** exact synthesis from [PC-350](../../findings/PC-350-solvable-decoder-recovers-centered-radial-profile.md), [PC-351](../../findings/PC-351-triangular-development-is-spectrally-trivial-and-control-conjugate.md) and [PC-355](../../findings/PC-355-free-fock-signature-tower-is-unitarily-control-blind.md), sharpening the finite-dimensional quotient audit of MI-047--MI-048.

Prime Circle already separates **source recovery** from **spectral discrimination**. The full Chen signature can retain the centered radial path, while triangular and semisimple finite-dimensional developments can lose the useful orientation under conjugacy-class spectralization. PC-355 shows that the canonical all-depth/free-Fock lift does not evade that obstruction merely by becoming infinite-dimensional in spirit.

Let the centered source alphabet carry the reciprocal parity involution `J`, and let the matched reciprocal path induce the corresponding algebra automorphism on the tensor signature. On the truncated full Fock space through degree `N`, second quantization gives a unitary `Gamma_N(J)` such that the left-regular signature operator satisfies

`L_N(tilde D)=Gamma_N(J) L_N(D) Gamma_N(J)^*`.

Therefore every unitary-conjugacy invariant of the canonical lift is exactly the same for the source and its matched reciprocal control: spectrum, singular values, pseudospectrum, numerical range, traces or determinants of admissible `*`-polynomials, and the corresponding invariants after adjoining the degree/vacuum/number structure preserved by second quantization.

The ordinary finite-level spectrum is even more degenerate. The signature has scalar term `1`, so

`L_N(D)=I+Q_N`,

where `Q_N` strictly raises tensor degree and is nilpotent on the truncation. Hence `Spec L_N(D)={1}` for every finite `N`, independently of the arithmetic source. Degree weights or enlarging the shell alphabet do not remove the parity covariance when they are functorial and parity-compatible.

This closes a tempting escape from PC-354. Moving from fixed finite-dimensional algebraic representations to the canonical full-signature/Fock representation does not manufacture a source-specific spectral coordinate. **Infinite representation depth is not useful by itself when the entire construction remains equivariant under the source/control involution and the destination again quotients by unitary equivalence.**

The surviving design space is more specific: a viable operator construction must introduce source-forced structure **before** the unitary spectral quotient that is not transported by the fixed reciprocal parity. Candidates include a source-dependent domain, metric, boundary condition, coupling, canonical frame or other non-spectral covariant whose control action is not implemented by the same second-quantized unitary. Any such proposal must then be tested against a matched non-arithmetic reciprocal control before assigning zero-selective meaning to the resulting spectrum.

**Boundary.** PC-355 does not rule out source-dependent Hilbert spaces, non-functorial refinement laws, parity-breaking domains/boundary conditions, non-spectral covariants retained before quotienting, or an infinite-dimensional operator whose spectral theorem is tied independently to zeta zeros. It rules out the canonical free-Fock/left-regular signature tower, its parity-compatible degree completions and unitary spectral invariants as a new discriminator merely because they retain all tensor depths.