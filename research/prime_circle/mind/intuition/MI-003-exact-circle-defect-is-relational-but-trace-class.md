# MI-003 — The exact-circle defect is a two-point curvature, but it is analytically soft

**Evidence level:** proved

## Core intuition

The first genuinely nonprojective information in the exact prime-circle map is not best viewed as a one-point correction.  It is a **two-point projective-curvature kernel**.  The Schwarzian found at one endpoint is only the diagonal trace of that kernel, while finite hyperbolic block-length defects are its rectangle integrals.  This gives an exact bridge from the original interior/exterior circle geometry to the prime-flute, but it also shows a limitation: the canonical conformal defect is too summable to create a singular spectral mechanism by itself.

## Strongest justified claim

For

\[
V(z)=\pi\cot(\pi/z),
\]

the canonical Grunsky--Schiffer kernel on the real tail is

\[
\mathcal K_V(x,y)
=\partial_x\partial_y\log\frac{V(y)-V(x)}{y-x}
=\frac{\pi^2}{x^2y^2}
\left(\csc^2\!\bigl(\pi(1/x-1/y)\bigr)
-\frac{1}{\pi^2(1/x-1/y)^2}\right).
\]

It is positive, satisfies

\[
\mathcal K_V(x,x)=\frac{1}{6}S(V)(x)=\frac{\pi^2}{3x^4},
\]

and, for ordered endpoints `a<b<c<d`, exactly recovers the difference between the projective-reference and exact orthogonal-circle separator lengths:

\[
\int_a^b\int_c^d \mathcal K_V(x,y)\,dy\,dx
=2\log\frac{\tanh(L_0/4)}{\tanh(L_E/4)}.
\]

Hence `L_E<L_0` for every such tail block.  On the canonical prime cells `[p_n,p_{n+1}]`, the normalized kernel compression is trace class; the unnormalized all-block interaction is absolutely summable.  Therefore the canonical exact-circle/projective-reference Fredholm completion cannot itself generate a nontrivial convergence wall or a new zero divisor from this defect.

## Synthesis of evidence

PF-082 identifies the Schwarzian as the first finite-scale defect of projective linearization.  PF-085 shows that this is the diagonal of the full two-point Schiffer kernel and proves the rectangle-to-geodesic identity, positivity, and trace-class prime-cell compression.  This sharpens the negative lesson of PC-013/PC-018: escaping flat first-order transport by passing to a genuine mixed two-point invariant does preserve interior information, but preservation alone does not guarantee analytically hard spectral behavior.

The factorization

\[
\frac{V(y)-V(x)}{y-x}
=\frac{\pi/x}{\sin(\pi/x)}
 \frac{\pi/y}{\sin(\pi/y)}
 \frac{\sin(\pi(1/x-1/y))}{\pi(1/x-1/y)}
\]

is especially revealing.  Mixed derivatives and cross-ratios kill the two one-endpoint factors; the surviving object is intrinsically relational.

## Evidence against overinterpretation / boundary cases

The kernel is attached to `V`, not to primality: any ordered sample of the same exact-circle map sees it.  PF-088 reinforces this warning by showing that a later `1/4` propagation threshold survives replacement of primes by integers.  Thus neither the existence of `K_V` nor a universal analytic exponent built on top of it is, by itself, arithmetic evidence.

This does not rule out a singular operator obtained by composing the trace-class endpoint defect with genuinely long-range dynamical propagation.  It rules out attributing such singularity to the canonical conformal defect alone.

## Status / novelty

The identities and summability statements are exact.  Grunsky--Schiffer theory and its Fredholm interpretation are classical.  The project-specific content is the explicit specialization to `pi cot(pi/z)`, the exact rectangle/hyperbolic-length bridge, and the resulting impossibility boundary for the prime-circle program.

## Falsification criterion

Refute the precise principle by finding a canonical operator built only from the exact endpoint deformation `V` and its interior/exterior conformal coupling, with no added propagation/branching structure, whose prime-cell kernel fails the proved trace-class decay or whose finite-block observable contradicts the rectangle identity.

## Lean-formalizable core

- Cotangent divided-difference factorization above.
- Explicit mixed-kernel formula and diagonal limit `K_V(x,x)=S(V)(x)/6`.
- Positivity of `csc^2(delta)-delta^{-2}` on the relevant interval.
- Rectangle mixed-derivative identity and the deduction `L_E<L_0`.
- Prime-gap telescoping estimate implying absolute summability of the cell compression.
