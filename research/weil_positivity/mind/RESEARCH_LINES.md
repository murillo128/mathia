# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Reconcile regulator invariance, critical scaling, closability, and archimedean completion in one source-native object

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation`, `MI-011-prime-ray-marginals-do-not-determine-mixed-prime-coupling`, `MI-012-automorphic-multiplicity-does-not-prevent-global-scalarization`, `MI-013-critical-sector-transport-needs-new-global-arithmetic-structure`.

WP-216--WP-255 show that canonical gauge/Toeplitz/Morita/KMS routes either miss the critical sector, scalarize the needed relation, or cannot pack independent prime channels into a normalized `KMS_1` state. WP-256--WP-260 then produce the exact Mangoldt half-density in symmetric Fock space but show that the most obvious convex/Gibbs pairing has the wrong occupation factor.

WP-261--WP-264 separate closability, programmability, critical normalization, and finite-part sign. Complete incidence exposes a real mixed-prime finite part, but an additive diagonal counterterm changes its inertia. WP-265 makes the ambiguity regulator-real: leading-only sharp and Gibbs source-Hamiltonian regularizations land in different inertia classes.

WP-266 removes that particular finite-part ambiguity **without choosing a scalar counterterm**. Let `H e_p=(\log p)e_p` and let `E_H` be the spectral-diagonal conditional expectation. Since the prime spectrum is simple, `E_H` is source-defined. Applying `I-E_H` to either the sharp or Gibbs complete-incidence Gram gives exactly

\[
a_Xa_X^*-D_X
\quad\text{or}\quad
a_\varepsilon a_\varepsilon^*-D_\varepsilon,
\]

and both converge in trace norm to the same connected operator

\[
K=aa^*-D,
\qquad d_p=\frac{\log p}{p^{3/2}}.
\]

Every finite compression of `K` with at least two primes has inertia `(1,m-1,0)`, and `K` is strictly negative on `ker a^*`. Thus regulator-covariant centering and an index-one primitive sign theorem really can coexist.

The obstruction has moved to the **critical-scale transport**. The source-canonical congruence `S=e^{H/2}` restores the Weil half-density on every finite compression, preserving inertia there, but globally the rank-one coefficient vector becomes

\[
b_p=\sqrt{\frac{\log p}{\sqrt p}},
\qquad \sum_p|b_p|^2=\infty.
\]

The critical rank-one quadratic form is therefore nonclosable on `ell^2`. Moreover the connected construction still does not generate the Gamma/polar term. The missing theorem is no longer merely “choose the right finite constant”: it must produce a global object in which **regulator invariance, critical half-density, closability, and archimedean completion are compatible by the same geometry**.

A viable boundary/cohomological/completion mechanism must do more than re-add `\lambda D_W`. It should explain why the critical transport is globally admissible or replace it by another canonical local-to-global operation, survive both sharp and Gibbs regulators without a scheme parameter, retain the finite-compression index structure for a structural reason, and generate the missing archimedean/polar sector rather than calibrating against the Weil formula afterward.

## Treat coefficient sourcing, interaction, connected centering, closability, critical scaling, and Weil orientation separately

The Fock hierarchy solves coefficient sourcing and symmetric-sector criticality. Complete incidence supplies mixed-prime coupling. Hamiltonian diagonal centering now solves the tested regulator finite-part mismatch and exposes a canonical trace-class index-one remainder.

But being canonical and well defined **below** critical scale is not the same as furnishing the critical Weil form. The Hamiltonian operation that restores the target prime amplitude is precisely where global closability fails. Future progress must therefore identify a new global carrier, not another finite subtraction convention.