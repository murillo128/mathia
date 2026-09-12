# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the graded affine Möbius bounds exposed by the first-shell CRT lift

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`.

MC-188--MC-227 show that residue phases are gauge, fixed square-free Hamming degrees form an alternating cascade, and GRH-strength progression bounds are sufficient but too strong; sparse exceptions, generic large-sieve/BDH estimates, and fiberwise control lose the source-selected coupling.

MC-228--MC-231 localize the first-shell obstruction to low/mesoscopic incidence. High incidence is support-harmless, exact-cell diagonalization is sufficient at fixed-power resolution, and singleton cells already carry near-full unsigned mass. Naive same-cell divisibility pairing reaches only a vanishing part of that singleton support.

MC-232 removes the exact-exclusion combinatorics from this stronger diagonal route. If `C_S` is the exact-incidence sum and `B_S=sum_(U superset S) C_U` its partial-intersection sum, Boolean Möbius inversion gives weighted-energy equivalence with condition factor

\[
\kappa^{m_y-1}=X^{o(1)},\qquad \kappa=\frac{3+\sqrt5}{2}.
\]

Thus exact cells and partial intersections are interchangeable at the fixed-power scale relevant here. Each partial intersection is a single CRT progression,

\[
B_S(X)=\sum_{\substack{P/Q_S<k\le X/Q_S\\(k,P)=1}}\mu(kQ_S-P),
\qquad Q_S=\prod_{d\in S}d^2.
\]

The remaining sufficient target is therefore a sparse family of **source-selected affine Möbius sums**, not cancellation inside exclusion masks. At incidence depth

\[
|S|=(\alpha+o(1))\frac{\log X}{\log\log X},\qquad 0\le\alpha<\frac14,
\]

the lifted interval has length `L_S=X^{1-2\alpha+o(1)}` while the sufficient amplitude target remains `|B_S|\le X^{1/2+o(1)}`. The required fixed-power gain over trivial support is `X^{1/2-2\alpha+o(1)}`: genuinely square-root-scale at the bottom and continuously weakening to triviality as `\alpha\uparrow1/4`.

The live theorem should attack this graded surface directly, either uniformly or in the weighted aggregate. A generic logarithmic saving cannot cross the low-incidence fixed-power gap, while GRH-quality square-root-in-length cancellation at every depth is stronger than needed.

## Treat gauge, support, Boolean conditioning, and source cancellation as separate gates

High incidence is cheap by support. The exact-cell alphabet and the Boolean zeta/Möbius transform both cost only `X^{o(1)}`. Singleton divisibility matching is ineffective, but that does not rule out additive, bilinear, harmonic, dispersion, or many-to-many mechanisms on the clean CRT lifts.

MC-232 is a representation reduction, not a cancellation theorem: its energy equivalence concerns the stronger diagonalized target, not the original shell energy itself. Future progress must therefore be credited to an actual estimate for the affine Möbius family, not to the removal of exact incidence masks.