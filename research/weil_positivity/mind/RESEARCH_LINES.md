# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Fix the critical prime-layer finite part intrinsically before claiming a Weil geometry

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation`, `MI-011-prime-ray-marginals-do-not-determine-mixed-prime-coupling`, `MI-012-automorphic-multiplicity-does-not-prevent-global-scalarization`, `MI-013-critical-sector-transport-needs-new-global-arithmetic-structure`.

WP-216--WP-255 show that canonical gauge/Toeplitz/Morita/KMS routes either miss the critical sector, scalarize the needed relation, or cannot pack independent prime channels into a normalized `KMS_1` state. WP-256--WP-260 then produce the exact Mangoldt half-density in symmetric Fock space but show that the most obvious convex/Gibbs pairing has the wrong occupation factor.

WP-261--WP-263 separate three further gates. Fixed finite-dimensional coherent mixing is nonclosable at the critical scale; arbitrary locally finite infinite-dimensional incidence is closable but programmable; and source-Hamiltonian conditional-Gibbs complete incidence becomes trivial after unit-diagonal normalization on the prime layer because `sum_p1/p` diverges.

WP-264 shows that the pre-normalization failure hides a real global geometry. For cutoff prime incidence,

\[
M_X=H_XD_W+a_Xa_X^*-2D_X,
\]

and subtracting the divergent `H_XD_W` leaves the trace-class finite part

\[
R=aa^*-2D,
\]

with exactly one positive direction and strict negativity on the canonical primitive hyperplane `ker a^*`. Thus complete mixed-prime incidence can evade the old unbounded-index obstruction and produce a genuine Hodge-like `(1,\infty)` signature.

The new obstruction is **renormalization canonicity**. A finite subtraction constant is not source-fixed:

\[
R_C=aa^*-2D+CD_W.
\]

Every `C<=0` retains the same one-positive-direction sign theorem, while `C>0` gives infinite positive index. The sign condition therefore does not select `C`. At the algebraically minimal `C=0`, the primitive metric has weight `(log p)/p^{3/2}`, one factor `1/p` below the critical Weil carrier; choosing `C<0` inserts an arbitrary positive multiple of the desired `(log p)/sqrt p` scale.

The live theorem must consequently fix the finite part **before comparison with the target**. It needs a source-derived boundary, quotient, cohomological, or other global operation that determines the subtraction intrinsically, preserves the useful index-one mixed-prime geometry, and then couples that choice to the Gamma/polar completion and correct Weil orientation. Choosing the counterterm because it matches the desired coefficient is not evidence.

## Treat coefficient sourcing, interaction, closability, critical normalization, finite-part canonicity, and Weil orientation separately

The Fock hierarchy solves coefficient sourcing and symmetric-sector criticality. Complete incidence now supplies a nontrivial index-one finite part, so the issue is no longer simply whether cross-prime coherence exists before normalization. The decisive distinction is whether its finite renormalization is source-forced rather than programmable.

A robust signature is weaker than a canonical arithmetic metric: WP-264 gives an explicit family of inequivalent finite parts sharing the same sign pattern. Any future Hodge-style argument must therefore identify both **why the sign holds** and **why this exact finite scale is the one selected by the source**.