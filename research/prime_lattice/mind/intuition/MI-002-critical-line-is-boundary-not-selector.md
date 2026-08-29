# MI-002 — The critical line is a natural Hilbert/self-dual boundary, not a zero selector

**Evidence level:** proved for the stated examples; supported as a line-wide warning

## Core intuition

Several canonical prime-lattice constructions single out `Re(s)=1/2` for structural reasons that do not use the Riemann zeros. This explains why the critical line is a natural coordinate or unitary boundary, but it also removes a common source of false evidence: **deriving the number `1/2` is much easier than forcing the zero divisor onto it**.

## Strongest justified principle

PL-014 gives the cleanest completed explanation. For an idele-class character `chi=eta|.|^s`, Tate duality sends

\[
\chi\longmapsto\chi^\vee=\chi^{-1}|.|,
\]

and `chi^vee=conj(chi)` exactly when `Re(s)=1/2`. The critical line is therefore the Hermitian/unitary self-dual axis of the completed Fourier--Mellin involution. This is a functional-equation symmetry statement, not RH.

The native Bohr-Hardy geometry reaches the same numerical boundary for a different reason. PL-021 shows that the canonical Möbius Euler product

\[
M_\sigma(z)=\prod_p(1-p^{-\sigma}z_p)
\]

belongs to the standard Hilbert-multidisc `H^2` exactly for `sigma>1/2`; throughout that whole region it is already cyclic unconditionally. At `sigma=1/2` the vector leaves the Hilbert space rather than undergoing an RH-sensitive cyclicity transition. Thus the natural coefficient-Hilbert boundary is not a zero-selection event either.

Earlier Hardy/Schatten constructions in the line exhibit the same separation: `1/2` often marks point-evaluation, Hilbert--Schmidt, or unitary normalization thresholds, while the corresponding canonical determinants or operators remain zero-free or have spectra unrelated to the Riemann zero divisor.

## Evidence against overgeneralization

The repeated appearance of `1/2` is not meaningless. It identifies the correct symmetry/Hilbert scale for several completed objects and is indispensable in Nyman--Beurling and adelic formulations. The restriction is logical: a boundary, fixed axis, or unitarity line requires an **additional selector** before it can become a theorem that zeros lie on that line.

The selector could be positivity, totality, a model-space defect theorem, a cohomological sign rule, or another global rigidity mechanism. This intuition does not decide which one exists.

## Status / novelty

All mechanisms used here are classical or exactly derived from stored findings. The synthesis is a program constraint, not a new theorem about zeta.

## Falsification criterion

Produce a canonical prime-lattice construction for which the same theorem that identifies `Re(s)=1/2` as a structural boundary also, without an additional independent positivity/totality/zero-divisor assumption, forces every nontrivial zeta zero onto that boundary.

## Lean-formalizable core

- Algebraic equivalence `chi^vee=conj(chi) <-> Re(s)=1/2` for `chi=eta|.|^s` with `eta` unitary.
- Norm identity for the Möbius Bohr vector and divergence at `sigma=1/2`.
- Logical separation between a symmetry-fixed set and concentration of an invariant divisor on that set.
