# MI-007 — An exact half-reflection can be universal time reversal rather than arithmetic duality

**Evidence level:** proved for the full-chord Bloch pencil in PC-159

## Core intuition

A finite spectral family can possess an exact `t <-> 1-t` functional-equation-shaped symmetry with fixed point `1/2` and still contain no zeta-specific localization mechanism. What matters is not the visual or algebraic resemblance to the Riemann reflection but whether the symmetry survives a control that removes the arithmetic source.

For the Prime-Circle full-chord Bloch pencil, the half-reflection is already present for every finite subset of roots of unity. It is therefore a real cyclic time-reversal symmetry of the carrier, not a selector for rational primes or Riemann zeros.

## Strongest justified principle

PC-159 proves that for any finite `X subset Z/dZ`, without coprimality or primitive-shell assumptions,

`P_X(1-t) = Z_X^{-1} conjugate(P_X(t)) Z_X`.

The corresponding antiunitary `Theta_X=Z_X^{-1}K` satisfies `Theta_X^2=I`, and the characteristic polynomial obeys

`F_X(z,t)=F_X(z,1-t)=G_X(z,t(1-t))`.

Thus the exact half-axis and its polynomial functional equation arise before the primitive arithmetic is imposed. Replacing `U(d)` by an arbitrary subset of roots leaves the symmetry intact.

This corrects the temptation to read the fixed point `t=1/2` as an intrinsic Riemann critical line. The reflection can organize the spectrum and constrain coefficients, but those constraints are matched by non-arithmetic root subsets.

## What remains possible

Arithmetic information may still live in how the primitive subset populates the reflected family, in a provenance-sensitive coupling across levels, or in an additional positive/unitary theorem that fails for generic subsets. The half-reflection can be part of such a mechanism, but it cannot supply the missing arithmetic selector by itself.

A viable continuation must therefore identify a residual not fixed by the antiunitary symmetry and show that it survives the existing bulk, refinement, puncture, and matched-subset controls.

## Status / novelty

Bloch time reversal, antiunitary conjugation, and polynomial reflection invariance are classical mechanisms. The persisted contribution is the exact Prime-Circle control: **the full-chord `1/2` reflection is carrier symmetry before it is arithmetic symmetry**.

## Falsification criterion

Find a finite root subset for which the exact PC-159 matrix identities fail, or derive an arithmetic invariant from the half-reflection alone that changes when `U(d)` is replaced by a matched non-arithmetic subset despite the same reflected pencil symmetry.

## Lean-formalizable core

- Matrix conjugation identity for `P_X(t)`.
- Antiunitary involution and `t <-> 1-t`.
- Characteristic-polynomial factorization through `t(1-t)`.
