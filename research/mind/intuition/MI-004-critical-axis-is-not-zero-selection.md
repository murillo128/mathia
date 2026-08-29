# MI-004 — A canonical critical axis is not a zero-selection mechanism

**Evidence level:** supported by exact/classical mechanisms in multiple branches

## Core intuition

Mathia now has several independent reasons why a distinguished real part such as `1/2` can emerge naturally: unitarity, self-duality, Hilbert/Schatten membership, product-measure equivalence, Fisher-information breakdown, cusp winding, or graph-domain summability. These mechanisms explain **where a symmetry or analytic transition lives**, but not why the Riemann zero divisor should concentrate there. Axis generation and zero selection are separate mathematical problems even when the same construction also recovers correct finite Euler coefficients.

## Strongest justified principle

Prime Lattice gives the cleanest separation. Tate's completed Fourier--Mellin involution has `Re(s)=1/2` as its Hermitian/unitary self-dual axis (PL-014), while the Möbius Bohr vector leaves the standard `H^2` space at the same boundary without an RH-sensitive cyclicity transition (PL-021). PL-030 adds an exact measure-class transition: the canonical product-Poisson measure attached to the normalized GCD kernel is equivalent to Haar exactly for `sigma>1/2` and singular at and below `1/2`. PL-031 produces the same summability threshold for a natural weighted Hasse Laplacian. In both new cases vertical prime phases are gauge or the resulting spectrum is featureless.

Weil Positivity makes the distinction sharper. WP-022 differentiates that same Poisson family and obtains the **exact finite-prime Weil cosine coefficients** at `sigma=1/2`; nevertheless the canonical positive Fisher norm diverges there. WP-023 shows that standard positive divergence completions either return infinitesimally to Fisher geometry or approach a universal boundary law determined by the simple pole of zeta at `1`, losing fixed prime-power data under natural normalization. Correct local coefficients plus a canonical critical boundary still do not supply the missing sign theorem.

Prime Flute supplies an adversarial analogue. Selected `1/4` scattering/Ruelle thresholds arise from universal one-dimensional propagation and even a single compact endpoint defect, while a full primitive-orbit completion restores the universal parabolic `1/2` threshold through cusp winding (PF-088, PF-102, PF-103). These exponents describe carrier dynamics rather than primality.

The programmatic requirement is therefore

\[
\boxed{
\text{canonical axis/boundary}
+\text{independent selector}
\longrightarrow
\text{possible RH mechanism}.
}
\]

The selector might be a genuine positivity theorem, target-sensitive totality result, cohomological sign rule, inertia elimination, or another global rigidity statement. It cannot be inferred merely from the existence of the boundary, from measure singularity there, or from the appearance of correct first-order Euler coefficients.

## Evidence against overgeneralization

This intuition does not demote the critical line to an arbitrary coordinate. Tate duality shows that it is canonically distinguished in completed arithmetic harmonic analysis, and the Poisson score result shows that exact finite Weil attenuation can naturally occur at the same parameter. The claim is only that **distinguished and coefficient-correct are still weaker than zero-selecting**.

Nor must every useful threshold equal `1/2`; the flute's `1/4` examples are included precisely because compelling exponents can arise from summability alone.

## Status / novelty

The component mechanisms are classical or exact persisted findings. Their separation into “axis generation” versus “zero selection” is a cross-branch synthesis, not a theorem about all RH approaches.

## Falsification criterion

Produce one of the audited canonical axis mechanisms and prove, from that same structural theorem with no additional positivity/totality/divisor assumption, that all nontrivial Riemann zeros lie on its fixed/boundary set. In the Poisson route, a canonical positive continuation retaining the critical score coefficients and forcing the Weil sign would also invalidate the present boundary claim.

## Lean-formalizable core

- Fixed-axis identity for Tate duality.
- Hilbert/Schatten and product-measure boundary calculations.
- `p`-series/cusp-winding threshold calculations.
- Abstract logical distinction between invariance/criticality of a carrier and support of a divisor on that carrier.
