# MI-004 — Compatible all-level completion preserves labels but does not supply a coercive RH scale

**Evidence level:** supported by exact/classical completion and operator obstructions

## Core intuition

Passing from individual Prime-Circle shells to the compatible inverse limit solves a real bookkeeping problem: exact-order labels, divisor filtrations, and rational characters survive canonically. But the natural regular Hilbert/operator structures on that completion are too soft, too classical, or too noncompact to turn those labels into an RH-selecting spectrum. Preserving arithmetic identity and producing a proper spectral scale are separate requirements.

## Strongest justified principle

Several exact completions now point in the same direction.

- PC-055 shows that the infinite Möbius birth transform has Euler-product membership thresholds, with `sigma=1/2` appearing as a square-summability boundary, but bounded invertibility only later and no zero selector at the Hilbert threshold.
- PC-058--PC-061 identify the divisor-Haar basis and its infinite limit with classical profinite valuation/Haar structure; after natural normalization the radial spectral mass returns weakly to profinite Haar rather than to a new critical measure.
- PC-064 identifies the compatible circle inverse limit with the adelic solenoid and Fourier dual `Q`. This is a canonical all-level carrier, but PC-065 gives the leafwise Laplacian dense rational-square spectrum, noncompact resolvent, and no ordinary heat-trace/spectral-zeta package.
- PC-066 shows that translation plus transverse unit symmetry fixes the exact-order projectors but leaves their scale `h(n)` arbitrary. PC-067 derives a nontrivial compatible inverse-square chord energy that does resolve exact order, yet high-conductor modes collapse toward zero and the exact-order decoder is noncoercive/discontinuous.
- PC-068 proves that a regular commuting leaf/fiber functional calculus cannot have compact resolvent. PC-069 rules out compact-resolvent Hamiltonians with exact scalar dilation covariance, and PC-070 closes the affine escape: on the natural full solenoid representation no ordinary compact-resolvent self-adjoint operator can satisfy `V_m^* H V_m = cH+dI`; for nonzero additive shift the mean-zero dilation multiplicity is already wrong.

Thus the all-level completion preserves arithmetic labels without canonically turning conductor or prime birth into a **proper spectral height**.

## What remains possible

A surviving operator may be singular in conductor, genuinely noncommuting between leaf and fiber directions, one-sided rather than based on the invertible solenoid dilation, nontranslation-invariant, or formulated through a relative/noncompact spectral invariant rather than ordinary compact resolvent. Such extra structure must be derived from the Prime-Circle geometry itself; inserting the conductor or a hand-chosen height after the fact would only decode labels already present in the solenoid.

The completion is therefore useful as a carrier, but not yet as a Hamiltonian principle.

## Status / novelty

The profinite/solenoidal identifications and the operator obstructions are persisted exact or classical findings. Their common interpretation as a separation between **label preservation** and **coercive spectral scale** is a supported synthesis, not a theorem about every operator on the solenoid.

## Falsification criterion

Derive from the compatible Prime-Circle geometry a canonical self-adjoint or relative operator whose scale is proper on exact-order directions, is not an arbitrary function of decoded conductor, evades the regular commuting and affine-dilation no-go results, and passes matched composite/regular controls. An ordinary compact-resolvent construction with exact affine solenoid dilation covariance would directly contradict PC-069--PC-070.

## Lean-formalizable core

- Exact-order projector decomposition and conductor recovery.
- Dense rational-square spectrum of the leafwise Laplacian.
- Noncompact-resolvent criterion for regular commuting rational-frequency calculus.
- Compact-resolvent obstruction under exact scalar affine unitary dilation covariance.
