# MI-001 — Anchoring and nonlocality are necessary but not sufficient

**Evidence level:** supported

## Core intuition

The prime-circle branch has now crossed a stronger boundary than the earlier “keep the anchor and go nonlocal” rule. Removing the anchor loses arithmetic position, and a finite anchored jet classicalizes, but several genuinely anchored, nonlocal, singular, and all-mode constructions also collapse to pre-existing harmonic or Dirichlet data. The surviving regime must therefore preserve the anchor **and** escape the large symmetry classes that make a single shell diagonalizable or reducible to universal regular-polygon data.

## Strongest justified principle

For a single primitive shell, neither anchoring nor nonlocality alone is enough to create a new arithmetic spectral mechanism.

- PC-019 shows that an unmarked primitive shell identifies odd `n` with `2n`.
- PC-020 shows that the complete finite anchored local jet of one shell is determined by classical cyclotomic/Jordan-totient data.
- PC-032 tests a singular nonlocal inverse-square chord Laplacian at a prime level; grounding the common vertex merely differentiates the characteristic polynomial of the universal regular-polygon operator, whose spectrum is `k(n-k)/2`.
- PC-035 and PC-036 keep the common anchor pointed and make the chord probe increasingly singular, but multiplicative diagonalization yields only finite bundles of classical Dirichlet values `L(2j,chi)` plus explicit local character factors.
- PC-037 allows arbitrary shell-independent rotation-invariant linear/nonlocal harmonic operators; `U(1)` symmetry diagonalizes them mode by mode and the shell dependence reduces to a finite Möbius/divisor recombination of one universal tail sequence.

The common mechanism is **single-shell symmetry reduction**. Once the construction is diagonalized by the ambient cyclic/rotational symmetry, the prime shell supplies at most a classical finite arithmetic filter on a universal operator response.

## Evidence against overgeneralization

This does not rule out all anchored nonlocal constructions. The no-go results leave open operations that couple several levels before spectralization, noncommuting joint use of the pointed shell and anchor data, nonlinear interactions between distinct shells, global uniformization/monodromy, or deformations in which the operator itself is forced by cross-level geometry rather than chosen independently of the shell.

Nor does “classical” mean useless: Dirichlet `L`-values, Ramanujan sums, and divisor filters may be the right coordinates for a later global mechanism. The restriction is epistemic: their appearance after symmetry diagonalization is not evidence that the prime-circle geometry has generated a new zero mechanism.

## Status / novelty

The component collapses are exact or literature-backed findings. The synthesis is a supported design constraint: a viable prime-circle mechanism must defeat both **information loss from removing the anchor** and **classicalization from single-shell equivariant diagonalization**.

## Falsification criterion

Refute this intuition by exhibiting a canonical one-shell construction that is anchored and lies inside one of the audited symmetry classes, yet produces an invariant not determined by the corresponding regular-polygon/Dirichlet/divisor data, without adding a cross-level label, an external kernel, or a noncanonical gauge.

## Lean-formalizable core

- `Phi_(2n)(z)=Phi_n(-z)` for odd `n` and the induced unmarked-shell equivalence.
- The derivative-of-characteristic-polynomial identity for one-vertex grounding of a circulant matrix.
- Finite character-sum reductions of the pointed inverse-power chord profiles.
- Rotation invariance implies Fourier-mode diagonalization and the resulting divisor/lcm reduction.
