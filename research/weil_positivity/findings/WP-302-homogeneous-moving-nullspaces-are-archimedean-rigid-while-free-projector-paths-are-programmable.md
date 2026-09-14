---
id: WP-302
title: Homogeneous moving nullspaces have bounded local responses, while freely chosen projector paths can program arbitrary positive metric profiles
branch: weil_positivity
status: supported
kind: moving-nullspace-local-rigidity-and-programmability-obstruction
claim_strength: exact finite-dimensional rigidity theorem for homogeneous unitary projector motion, exact boundedness/almost-periodicity obstruction for regular local finite--archimedean readouts, exact rank-one programmability construction, and a narrowed source-theorem requirement for the moving-nullspace escape left by WP-301
created: 2026-09-14
related: [WP-005, WP-301]
prior_art:
  - J. P. Provost and G. Vallee, Riemannian structure on manifolds of quantum states, Communications in Mathematical Physics 76 (1980), 289-301, DOI 10.1007/BF02193559
  - J. Anandan and Y. Aharonov, Geometry of quantum evolution, Physical Review Letters 65 (1990), 1697-1700, DOI 10.1103/PhysRevLett.65.1697
  - NIST Digital Library of Mathematical Functions, Chapter 5, Section 5.11, especially equation 5.11.2 for the digamma asymptotic
---

# WP-302 — Homogeneous moving nullspaces have bounded local responses, while freely chosen projector paths can program arbitrary positive metric profiles

## Claim

`WP-301` closes the fixed-kernel frustration-free continuation of non-scalar holonomy and leaves a canonically **moving nullspace** as one of the cleanest escapes: allow the positive archimedean constraint itself to vary with the Mellin/spectral parameter so that its zero-mode projector can carry nonconstant information.

There is an exact rigidity/programming dichotomy for the first two natural implementations of that escape.

Let `P(t)` be the orthogonal projector onto the moving kernel of a positive constraint `Q_infty(t)`. If the motion is source-homogeneous,

\[
P(t)=U(t)P_0U(t)^*,
\qquad
U(t)=e^{itA}
\tag{1}
\]

on a finite-dimensional internal fiber, then every local scalar built continuously from a finite jet of `P(t)` and invariant under simultaneous unitary conjugation is constant. More generally, if finitely many fixed bounded source operators `X_1,...,X_m` are allowed as an external finite/arithmetic frame, every trace-polynomial readout in the finite jet of `P(t)` and the `X_j` is a bounded finite exponential polynomial in `t`; every continuous readout of the same finite-dimensional orbit data is bounded.

That is incompatible with an exact identification with the standard archimedean digamma symbol of the completed-zeta explicit formula, whose real part has logarithmic growth:

\[
\Re\,\psi\!\left(\frac14+\frac{it}{2}\right)
=\log |t|+O(1)
\qquad (|t|\to\infty),
\tag{2}
\]

up to normalization constants irrelevant to boundedness. Thus a finite-dimensional homogeneous moving kernel does not by itself supply the required archimedean profile through a regular local geometric response, even when it is measured relative to fixed finite-prime operators.

At the opposite extreme, dropping the source-homogeneous law and choosing the projector path freely makes the most obvious positive geometric response **arbitrarily programmable**. For a rank-one projector in `C^2`,

\[
v(t)=\begin{pmatrix}\cos\theta(t)\\ \sin\theta(t)\end{pmatrix},
\qquad
P_\theta(t)=v(t)v(t)^*,
\tag{3}
\]

the Fubini--Study/Grassmann metric density is

\[
g_\theta(t)
:=\frac12\operatorname{Tr}\bigl(\dot P_\theta(t)^2\bigr)
=\dot\theta(t)^2.
\tag{4}
\]

Hence every prescribed smooth strictly positive profile `h(t)` on an interval is realized exactly by choosing

\[
\theta(t)=\theta(t_0)+\int_{t_0}^{t}\sqrt{h(s)}\,ds.
\tag{5}
\]

So agreement between an arbitrarily chosen moving kernel and a desired nonnegative archimedean density is not evidence of an intrinsic Weil mechanism; the target can be inserted into the path speed itself.

The surviving moving-nullspace route is therefore narrower than `WP-301` states. It needs a **source theorem** that forces nonhomogeneous or infinite-dimensional/unbounded motion, a nonlocal boundary/cohomological response, or a finite--archimedean coupling with an intrinsically forced singular measure/readout. The required nonconstant behavior cannot come merely from a finite-dimensional homogeneous unitary orbit, while an unconstrained nonhomogeneous path is too programmable to count as an explanation.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + HOMOGENEOUS-UNITARY-ORBIT-RIGIDITY + FINITE-DIMENSIONAL-ARCHIMEDEAN-GROWTH-MISMATCH + PROJECTOR-METRIC-PROGRAMMABILITY + MOVING-NULLSPACE-ESCAPE-NARROWED + CLASSICAL-GEOMETRIC-INGREDIENTS + NOT-WEIL-POSITIVITY`.

## 1. Exact object: a positive constraint with a moving kernel

The `WP-301` escape can be represented without assuming a particular Hamiltonian model. Let

\[
Q_\infty(t)\succeq0,
\qquad
P(t)=\mathbf 1_{\{0\}}\bigl(Q_\infty(t)\bigr).
\tag{6}
\]

Unlike the fixed operator in `WP-301`, the kernel may now vary with `t`. The question is whether that motion itself can canonically carry the missing archimedean information while preserving an independent positive origin.

The strongest elementary notion of source-homogeneous motion is a one-parameter unitary action generated by a fixed self-adjoint matrix `A`:

\[
U(t)=e^{itA},
\qquad
P(t)=U(t)P_0U(t)^*.
\tag{7}
\]

This is not an arbitrary gauge change if `U(t)` is supplied by the source dynamics: the subspace genuinely moves relative to any fixed finite-prime operators. The obstruction below therefore distinguishes two cases rather than quotienting all unitary motion away:

1. intrinsic scalars of the moving subspace alone are exactly constant;
2. relative scalars involving fixed source operators may vary, but in finite dimension their regular local responses remain bounded and, for trace-polynomial observables, almost periodic.

## 2. Homogeneous unitary motion has constant intrinsic local geometry

Differentiate (7). Since `A` commutes with `U(t)`,

\[
\dot P(t)=U(t)[iA,P_0]U(t)^*.
\tag{8}
\]

Iterating gives

\[
P^{(k)}(t)
=U(t)\,\operatorname{ad}_{iA}^{k}(P_0)\,U(t)^*.
\tag{9}
\]

Therefore the whole finite jet

\[
J_m(t)=\bigl(P(t),\dot P(t),\ldots,P^{(m)}(t)\bigr)
\tag{10}
\]

is obtained from the fixed jet `J_m(0)` by simultaneous unitary conjugation.

Let `F` be any scalar functional of that jet satisfying

\[
F(VY_0V^*,\ldots,VY_mV^*)=F(Y_0,\ldots,Y_m)
\tag{11}
\]

for every unitary `V`. Then equations (9)--(11) imply immediately

\[
\boxed{F(J_m(t))=F(J_m(0))\quad\text{for all }t.}
\tag{12}
\]

This covers trace contractions, Schatten norms, spectra of words formed from the jet, determinant-type regular invariants, and the standard Grassmann/Fubini--Study speed. In particular,

\[
g_P(t)=\frac12\operatorname{Tr}\bigl(\dot P(t)^2\bigr)
=\frac12\operatorname{Tr}\bigl([iA,P_0]^2\bigr)
\tag{13}
\]

is constant. For a rank-one state this is the familiar constant energy-variance speed of a time-independent unitary evolution in projective Hilbert space.

Thus the simplest idea — let the Gamma term be the intrinsic local curvature/speed/norm of a source-homogeneous moving zero mode — is already too rigid. The kernel moves, but its local conjugation-invariant geometry does not acquire a nonconstant scalar profile.

## 3. A fixed finite-prime frame permits variation, but only bounded finite-frequency variation

A legitimate objection to section 2 is that the archimedean subspace should be measured relative to the finite arithmetic structure rather than in isolation. Let `X_1,...,X_m` be fixed bounded matrices representing any finite collection of source operators, prime constraints, incidence maps, or boundary observables.

Diagonalize the finite-dimensional generator,

\[
A=\sum_{a=1}^{d}\lambda_a E_a.
\tag{14}
\]

Then

\[
P(t)
=\sum_{a,b=1}^{d}
 e^{it(\lambda_a-\lambda_b)}E_aP_0E_b.
\tag{15}
\]

Every derivative multiplies each term only by a power of `i(\lambda_a-\lambda_b)`. Consequently any finite trace polynomial in

\[
P(t),P'(t),\ldots,P^{(r)}(t),X_1,\ldots,X_m
\tag{16}
\]

has the form

\[
R(t)=\sum_{\nu\in\Omega}c_\nu e^{it\nu},
\tag{17}
\]

for a finite frequency set `Omega` generated by eigenvalue differences of `A`. In particular `R` is bounded and Bohr almost periodic.

The same boundedness conclusion needs much less algebra. The closure of the finite-dimensional unitary orbit of the finite jet together with fixed `X_j` is compact. Hence **every continuous scalar readout of those data is bounded**. This includes ordinary overlaps such as `Tr(P(t)X_j)`, commutator norms, finite Gram determinants away from a deliberately introduced singular functional, and continuous spectral functions of bounded orbit data.

So fixed finite-prime operators do evade the strict constancy of (12), but not the boundedness barrier. They can create oscillatory relative orientation; they cannot create a globally logarithmically growing regular local symbol.

## 4. The completed-zeta archimedean symbol crosses that boundedness barrier

The completed-zeta explicit formula contains an archimedean Gamma contribution whose spectral symbol is expressed through the digamma function. The standard asymptotic expansion is

\[
\psi(z)
=\log z-\frac{1}{2z}+O(|z|^{-2})
\tag{18}
\]

in sectors away from the negative real axis. Taking `z=1/4+it/2` gives

\[
\Re\,\psi\!\left(\frac14+\frac{it}{2}\right)
=\log|t|+O(1).
\tag{19}
\]

Different conventional normalizations add constants, multiply by fixed factors, or combine this with the standard polar counterterm; none removes the logarithmic growth of the Gamma symbol.

Equations (17)--(19) therefore give the conditional no-go

\[
\boxed{
\begin{array}{c}
\text{finite-dimensional homogeneous moving kernel}\\
+\ \text{fixed bounded finite/source frame}\\
+\ \text{regular local continuous readout}
\end{array}
\not\equiv
\text{global zeta archimedean digamma symbol}.
}
\tag{20}
\]

This is stronger than the `WP-301` fixed-kernel statement. `WP-301` says that positive reweighting cannot move the harmonic projector at all. Here the projector genuinely moves and may have nontrivial relative overlaps, yet the most source-symmetric finite-dimensional motion still has the wrong global analytic behavior.

The qualifier **regular local** is essential. A singular operation such as a logarithm or inverse at a vanishing determinant can turn bounded orbit data into an unbounded scalar. That is not ruled out here. But the singular locus, branch, domain, and normalization then become new mathematical data that must be forced by the Mathia source rather than chosen to manufacture the Gamma factor. Likewise a nonlocal transform of the orbit can introduce additional measure/kernel structure. Those are genuine escapes, not counterexamples to (20).

## 5. Arbitrary projector motion has the opposite defect: exact programmability

Suppose instead that no source law fixes the motion. In the real two-plane inside `C^2`, let

\[
v(t)=(\cos\theta(t),\sin\theta(t))^T,
\qquad
P_\theta(t)=v(t)v(t)^*.
\tag{21}
\]

A direct differentiation gives

\[
\frac12\operatorname{Tr}\bigl(\dot P_\theta(t)^2\bigr)
=\dot\theta(t)^2.
\tag{22}
\]

Equivalently, for normalized `v`,

\[
\langle \dot v,(I-P_\theta)\dot v\rangle
=\dot\theta(t)^2,
\tag{23}
\]

which is the rank-one Fubini--Study metric density.

Let `h(t)>0` be any smooth target profile on an interval. Define

\[
\theta(t)
=\theta(t_0)+\int_{t_0}^{t}\sqrt{h(s)}\,ds.
\tag{24}
\]

Then (22) gives exactly

\[
\boxed{g_\theta(t)=h(t).}
\tag{25}
\]

The statement extends to nonnegative `h` whenever a smooth square root is available. No arithmetic input was used. The same construction works for a generalized-prime control, a randomized control, or no prime system at all.

Therefore a numerical or symbolic match between a **freely selected** moving-kernel metric and a desired positive archimedean profile has essentially zero explanatory force. The profile can be encoded into the speed of the path by quadrature. Positivity of the metric then certifies only the geometry of the chosen path, not an independently forced arithmetic sign theorem.

## 6. Matched controls and what is actually ruled out

The result is deliberately narrower than a no-go for all moving kernels.

First, it does not assume that unitary motion is gauge. The fixed operators `X_j` in section 3 allow the archimedean subspace to move relative to an arithmetic frame. The obstruction is that **finite-dimensional homogeneous motion plus regular local readout remains bounded**, not that relative motion is meaningless.

Second, the proof is insensitive to whether the fixed frame is built from rational primes or from a matched generalized-prime system. Rational-prime specificity inside the `X_j` may change the coefficients and frequencies in (17), but not the boundedness conclusion. Thus merely injecting prime-dependent fixed matrices does not repair the Gamma-growth mismatch.

Third, this does not rule out:

- an infinite-dimensional unitary representation with a source-forced continuous spectral measure and an unbounded or distributional observable;
- a nonunitary/modular/semigroup evolution whose geometry is not a compact homogeneous orbit;
- a source-forced nonhomogeneous projector path rather than an arbitrarily fitted one;
- nonlocal two-point responses such as `Tr(P(t)P(s))` followed by an independently forced measure or boundary construction;
- a singular determinant/resolvent/compression readout whose singular structure is forced before comparison with the Gamma factor;
- a genuinely coupled finite--archimedean operator in which neither sector remains a fixed bounded external frame;
- a boundary/cohomological readout retaining nonzero spectrum instead of a local finite-jet scalar.

Those are precisely the places where additional global structure can enter.

## 7. Prior-art and novelty audit

No novelty is claimed for the geometric ingredients. The Fubini--Study metric on projective quantum-state space and its relation to quantum fluctuations are classical; Provost--Vallee (1980) is a standard source. Anandan--Aharonov (1990) identifies projective distance/speed with the energy uncertainty of unitary evolution. The digamma asymptotic (18) is standard and is recorded in NIST DLMF 5.11.2. The existing Weil-positivity literature anchors for this line already identify the Gamma/digamma symbol as the archimedean component of the explicit-formula target.

A targeted search did not identify a prior result phrased as the present Mathia route exclusion. The novelty claim is therefore only the **specialized consequence**: the moving-nullspace escape left open by `WP-301` bifurcates sharply. Finite-dimensional homogeneous unitary motion is too rigid/bounded for a regular local realization of the global Gamma symbol, whereas unrestricted projector motion can fit arbitrary positive metric profiles and so cannot count as intrinsic evidence without an independent source law.

This is not a new positivity criterion, a Hilbert--Polya construction, or a new theorem about Fubini--Study geometry. It is an obstruction that prevents a tempting geometric completion of Mathia's frustration-free selector from being counted as progress merely because its kernel moves.

## 8. Adversarial falsification gates

The finding should be narrowed or withdrawn if any of the following fails:

1. equation (9): every derivative of a fixed-generator unitary orbit is a simultaneous conjugate of a fixed operator;
2. every simultaneously conjugation-invariant scalar of a finite jet is therefore constant;
3. in finite dimension, equation (15) holds and finite trace-polynomial relative readouts are finite exponential polynomials;
4. continuous scalar readouts of the finite-dimensional orbit data and fixed bounded source operators are bounded because their domain closure is compact;
5. the completed-zeta archimedean digamma symbol has logarithmic growth on the real spectral axis;
6. the standard polar/global rational corrections do not cancel that logarithmic growth;
7. equation (22): the rank-one projector metric equals `theta'(t)^2`;
8. every smooth strictly positive profile can therefore be realized by (24);
9. no rational-prime property enters the programmability construction;
10. the conclusion is kept conditional on **finite-dimensional homogeneous motion and regular local readout**, rather than being promoted to a no-go for infinite-dimensional, singular, nonlocal, nonunitary, or source-forced nonhomogeneous mechanisms.

Items 1--4 and 7--9 are elementary exact identities/topology. Item 5 is the classical digamma asymptotic. Item 6 depends only on the standard completed-zeta normalization and should be rechecked under any alternative Weil convention before using the obstruction there.

## 9. Consequence for the research frontier

`WP-301` says that fixed positive local constraints lose all nonzero archimedean spectral information when read through their common zero space. Simply allowing that zero space to move is not yet enough.

If the motion is the most canonical finite-dimensional homogeneous unitary flow, intrinsic local geometry is constant and finite-relative regular responses are bounded/almost periodic, whereas the required Gamma symbol is logarithmically unbounded. If the path is freed from a source law, even the canonical positive projector metric can be made equal to any chosen positive profile by selecting the path speed.

The next admissible question is therefore no longer merely **can the kernel move?** It is:

\[
\boxed{
\text{what Mathia-native source theorem forces the particular nonhomogeneous,}
\quad
\text{infinite-dimensional, singular, or nonlocal motion/readout needed by the archimedean term?}
}
\tag{26}
\]

A viable construction should determine that structure before comparison with the explicit formula and should couple the finite-prime and archimedean sectors before positivity is invoked. Otherwise the route falls on one side of the dichotomy established here: homogeneous rigidity or arbitrary programmability.

## Internal dependencies

- `research/weil_positivity/findings/WP-005-prime-lattice-axis-positivity-does-not-survive-weil-autocorrelation-lift.md`
- `research/weil_positivity/findings/WP-301-frustration-free-holonomy-zero-modes-are-universal-kernel-intersections.md`
