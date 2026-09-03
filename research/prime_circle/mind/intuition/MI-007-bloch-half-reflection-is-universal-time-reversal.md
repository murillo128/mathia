# MI-007 — The intrinsic Bloch half-reflection is universal time reversal, and its candidate strip is a resolvent region

**Evidence level:** proved for the full-chord Bloch pencil in PC-159--PC-160

## Core intuition

A finite spectral family can possess an exact `t <-> 1-t` functional-equation-shaped symmetry with fixed point `1/2` and still have spectral geometry opposite to the Riemann zero problem. For the Prime-Circle full-chord Bloch pencil, the symmetry is already present for every finite subset of roots of unity, and the analytically continued pencil is **strictly accretive throughout `0<Re(t)<1`**.

Thus the intrinsic Bloch coordinate is not merely non-arithmetic as a critical-line selector. Its whole formal analogue of the critical strip is zero-free; the midpoint is quantitatively inside a resolvent region.

## Strongest justified principle

PC-159 proves that for any finite `X subset Z/dZ`, without primitiveness or coprimality assumptions,

`P_X(1-t)=Z_X^{-1} conjugate(P_X(t)) Z_X`,

so the characteristic polynomial factors through `t(1-t)`. The half-reflection is therefore universal cyclic time reversal before any rational-prime condition is imposed.

PC-160 strengthens the matched control geometrically. Complete cyclic lifts show that for real `0<=sigma<=1`,

`P_X(sigma) >= sigma(1-sigma)/(2d^2) I`.

For `t=sigma+i tau`, the Hermitian part acquires the additional positive term `tau^2/(2d^2) I`. Hence `det P_X(t)` cannot vanish anywhere in the open unit strip and the inverse has an explicit norm bound there. A direct scalar-compression argument also shows that every polynomial eigenvalue in `t` is real and belongs to `(-infinity,0] union [1,infinity)`.

The apparent Riemann-shaped reflection and the strip exclusion arise from the same universal complete-fiber geometry. Interpreting `t` itself as a hidden Riemann spectral parameter is therefore decisively blocked.

## What remains possible

Arithmetic information may still live in a fine-fiber puncture sector, a provenance-sensitive cross-level coupling, a nonlinear function of several pencils, a growing-support limit, or another construction that breaks the universal complete-lift positivity before the spectral variable is read.

A viable continuation must identify what new arithmetic operation destroys the matched-subset accretivity and then prove a source-specific sign or zero theorem for the resulting object. Merely reparameterizing or analytically continuing the same finite Bloch pencil cannot do so.

## Status / novelty

Bloch time reversal, definite/hyperbolic Hermitian matrix polynomials, and positive graph Laplacians are classical. The persisted Prime-Circle contribution is the exact control: **the full-chord `1/2` reflection is universal and the entire associated open strip is intrinsically zero-free**.

## Falsification criterion

Find a finite root subset and `t` with `0<Re(t)<1` for which `det P_X(t)=0`, or a nonreal polynomial eigenvalue of the PC-160 pencil. A new carrier that changes the pencil rather than reinterpreting it would evade the result.

## Lean-formalizable core

- Antiunitary `t <-> 1-t` conjugation.
- Complete-lift positive lower bound on the real interval.
- Strict accretivity in the complex strip.
- Reality and exclusion interval for quadratic-pencil eigenvalues.
