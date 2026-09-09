# MI-013 — Affine KMS off-diagonal freedom is boundary data, not prime coupling

**Evidence level:** supported by the exact affine KMS residue and matrix-coefficient classification through PL-231

## Core intuition

A nontrivial equilibrium simplex can contain genuine phase freedom without creating arithmetic interaction among the source channels. In the canonical affine-semigroup system the low-temperature freedom lives in a boundary circle measure. Ordinary KMS evaluation replicates that one boundary Fourier profile across every multiplicative channel instead of coupling the channels to each other.

This sharpens the source-selection requirement. Leaving a positive diagonal is not enough if the first off-diagonal layer is merely an invertible encoding of a freely chosen state parameter. A useful affine mechanism must impose a relation before equilibrium scalarization, or supply an independent arithmetic principle that selects and constrains the boundary data non-generically.

## Strongest justified principle

PL-230 shows that affine residue projections are KMS-rigid: their masses are forced by `a^{-beta}`, and Nica covariance produces independent geometric prime-valuation tails. The diagonal is source-defined but positive and local in the wrong way for the desired signed selector.

PL-231 uses the complete published KMS coefficient formula. In the unique phase `1<=beta<=2`, every off-diagonal spanning monomial vanishes, so the shifted critical value `beta=3/2` has no hidden off-diagonal equilibrium signal. For `beta>2`, coefficients with distinct multiplicative channels still vanish. The surviving same-channel additive coefficients are

`a^{-beta} C_(beta,nu)(r)`,

where `C_(beta,nu)` is a fixed divisor smoothing of the Fourier moments of the circle measure `nu`. Ordinary Möbius inversion recovers those moments exactly, so the normalized profile and the arbitrary boundary measure are information-equivalent.

Thus low-temperature symmetry breaking has not produced a rational-prime coupling. It has exposed isotropy/boundary state data that the multiplicative channels merely copy after their Boltzmann normalization.

## Counterevidence / boundary

The classification concerns the canonical affine dynamics and ordinary bounded KMS expectations on its spanning algebra. It does not rule out an independently justified arithmetic selection principle for one boundary measure, a different source-forced dynamics whose energy balance permits cross-channel coefficients, an unbounded affiliated observable, or a target-relative completed trace/positivity construction containing information outside ordinary state moments.

Positive-definiteness constrains the boundary moment sequence, so its coefficients are not independently programmable. The point is not arbitrary coefficient freedom; it is that the constraint is generic circle harmonic analysis rather than a source-selected relation among rational-prime channels.

## Epistemic status

**Exact classification of canonical affine KMS diagonal and off-diagonal scalarization; the remaining affine route must introduce a source relation before or beyond ordinary KMS evaluation.**

## Falsification criterion

Exhibit a nonzero canonical KMS coefficient coupling distinct multiplicative channels in the classified regime, show that the normalized PL-231 profile contains information not recoverable from the boundary measure, or derive an arithmetic selection theorem inside the same system that fixes `nu` and yields a non-generic zero-sensitive sign/coercivity relation. Otherwise a positive continuation should identify the extra pre-scalarization source structure explicitly.
