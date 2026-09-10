# MI-006 — The critical endpoint has usable Bessel-four margin; the live gate is the combined Robin transform

**Evidence level:** exact Jacobi/Bessel-four kernels, two-derivative hypercycle/corridor transport, and polar-free Robin recombination through PF-257

## Core intuition

The critical local geometry is no longer the main uncertainty. The actual Jacobi edge has a sharp Bessel-four smoothing window, and the prime-dependent coordinate transport plus the variable-corridor spectral change preserve two derivatives of high-to-low locality. The remaining local question sits in the actual seam operator.

Crucially, that question should not be over-specified as locality of a naked polar partial isometry. The physical normalized Robin injection keeps singular amplitude and orientation correlated and has an exact regular resolvent-transform form.

## Strongest justified principle

PF-252--PF-253 establish the Bessel-four ground-state model and the square-root separated window up to `R<3`. PF-255 identifies hypercycle reparameterization as a projective unitary flow with two-derivative leakage control. PF-256 upgrades form equivalence of the variable corridor to operator graph equivalence and transfers the same locality to the actual `K_a` spectral scale.

PF-254's polar split is exact but PF-257 recombines it: with `X=K^{-1/2}Q^{1/2}`, the normalized source factor is `(I+XX*)^{-1}X=X(I+X*X)^{-1}`, the off-diagonal block of `t/(1+t^2)` applied to a self-adjoint block operator. Near small singular values the combined map vanishes even if the polar orientation itself is unstable. PF-244 still warns that bad high-to-low conversion of the full `X` can defeat smoothing.

## Program consequence

Prove weighted/off-diagonal locality directly for the combined normalized Robin transform, or for a block-operator calculus that implies it, in the actual corridor basis. Then justify the unbounded complete-lift limit and preserve the established margin through physical and global assembly. Do not require an independent theorem about `U` unless the proof genuinely needs it.

## Counterevidence / boundary

PF-257 is exact on bounded/Galerkin regularizations and does not by itself establish the complete-lift domain passage or separated smoothing. Two-derivative coordinate transport does not constrain an arbitrary intrinsic seam square root. The final weak-`S_1` reassembly also remains separate.

## Epistemic status

**Sharp positive critical smoothing plus controlled geometric transport and an exact polar-free physical factorization; the actual seam transform and final assembly remain open.**

## Falsification criterion

Invalidate the Bessel-four window, the two-derivative corridor transfer, or the polar-free identity; or construct the actual source seam so that its combined normalized transform exhibits the PF-244 high-to-low failure. A positive continuation should estimate that combined transform directly.
