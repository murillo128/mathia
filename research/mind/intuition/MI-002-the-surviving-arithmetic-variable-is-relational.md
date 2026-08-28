# MI-002 — The surviving arithmetic variable is relational and multiscale

**Evidence level:** supported

## Core intuition

The strongest Mathia constructions repeatedly remove a large universal or gauge-like absolute scale and retain a **relation**: a cross-ratio, gap ratio, cuff contrast, two-point conformal defect, or interscale spectral response.  The newer flute results sharpen this: the useful relation need not be a static ratio.  It can be a directed multiscale memory in which the response at one scale depends on the immediately stronger scale that preceded it.

## Strongest current claim

For prime-flute occurrences near a large common prime scale `P`,

\[
\ell_i(P)=2\log(4P/d_i)+o(1),
\]

so common divergence disappears from differences and adjacent gap ratios become cuff contrasts.  In a graded pinching chain the resolved surface eigenvalue at the `j`-th weak neck has the form

\[
\lambda^{(j)}
=A_j e^{-C_j/4}
-B_j e^{-(2C_j-C_{j-1})/4}
+o\!\left(e^{-(2C_j-C_{j-1})/4}\right),
\qquad C_j=\ell_j-\ell_{j+1},
\]

with explicit positive constants `A_j,B_j`.  The leading term is one relational scale; the first correction is a **relation between relations**.  This is the first rigorous mechanism in the program where an actual Laplace eigenvalue carries directed upstream memory rather than merely encoding the current gap ratio.

The prime-circle side exhibits the same relational filtration in another language.  For the exact map `V(z)=pi cot(pi/z)`, the divided difference factors into two one-endpoint terms and one genuine two-point term.  Mixed differentiation or a four-point cross-ratio kills the one-endpoint factors and leaves the Grunsky--Schiffer kernel.  Its rectangle integral is exactly a hyperbolic separator-length defect.  Thus the circle-to-flute bridge itself selects relational information before spectralization.

## Synthesis of evidence

PF-029/PF-047/PF-074/PF-076 show gap ratios reappearing as hyperbolic moduli, systoles and isoperimetric data.  PF-080/PF-090/PF-091 upgrade this from static ratios to effective-resistance memory `w_j^2/w_{j-1}` in resolved true-surface eigenvalues.  PF-089 shows why that distinction matters: multiplying the modes telescopes the hierarchy and leaves only endpoint contrast.

On the circle side, PC-013/PC-014/PC-018 show that absolute one-dimensional transports are often gauge/subdivision data, while PF-082/PF-085 show that the first exact nonprojective defect survives as a mixed two-point invariant.  PC-019 gives the opposite warning: quotienting away the anchor entirely destroys arithmetic distinction.

## Boundary cases and failure modes

Not every relative quantity is meaningful.  A marked sojourn difference may simply be a classical shear coordinate; an arbitrary generating function of gap ratios adds no structure; and PF-088 shows that a sharp `1/4` threshold can be entirely due to one-dimensional propagation even though it is expressed through a relative operator.

Likewise, the multiscale eigenvalue law is a theorem for finite hyperbolic chains in a graded Burger window, but recurrent realization of that moderate window by actual consecutive prime blocks is not yet proved.  The program should therefore distinguish **geometric relational mechanisms** from **arithmetic recurrence of the required moduli**.

## Status / novelty

Exact/asymptotic for the displayed circle and flute conversions; supported as a program-wide principle.  Cross-ratios, Grunsky kernels, Burger degeneration and Feshbach theory are classical.  The potentially new content is their composition into a directed multi-gap spectral-memory mechanism tied to the exact prime-derived geometry.

## Falsification criterion

Find a robust prime-specific spectral mechanism in this program whose decisive information is an absolute local scale that cannot be rewritten after natural symmetry reduction as a relational invariant, or prove that the apparent upstream correction is removable by a canonical coordinate change and contains no information beyond the current ratio.

## Most informative next move

Search for observables that retain **ordered relational depth**: not only `d_j/d_{j+1}`, but how successive ratios interact under a canonical operator.  Test whether higher Feshbach coefficients, marked residues or Weyl functions retain longer-range combinations that do not telescope and are not reproduced by regular controls.

## Lean-formalizable core

- Conversion from cuff differences to gap ratios.
- Cross-ratio invariance under Möbius normalization.
- Cotangent divided-difference factorization and cancellation of one-endpoint factors.
- Algebraic conversion of `w_j^2/w_{j-1}` to the corresponding three-gap/two-cuff-contrast expression.
