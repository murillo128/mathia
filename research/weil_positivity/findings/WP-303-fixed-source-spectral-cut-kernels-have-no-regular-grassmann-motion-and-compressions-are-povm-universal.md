---
id: WP-303
title: Fixed-source spectral-cut kernels have no regular Grassmann motion, while positive compressions are POVM-universal
branch: weil_positivity
status: supported
kind: fixed-source-spectral-cut-moving-kernel-singularity-and-povm-universality
claim_strength: exact rigidity theorem for any mutually commuting spectral-projector path of one fixed source operator, exact pure-point atomic obstruction for the canonical source log-energy threshold path, exact POVM-compression/Naimark universality boundary, and a narrowed source-forced moving-nullspace escape after WP-302
created: 2026-09-14
related: [WP-275, WP-301, WP-302]
prior_art:
  - John B. Conway, A Course in Operator Theory, Graduate Studies in Mathematics 21, American Mathematical Society, 2000, for the spectral theorem and projection-valued measures
  - M. A. Naimark, On a representation of additive operator set functions, C. R. (Doklady) Acad. Sci. URSS (N.S.) 41 (1943), 359-361, for dilation of positive operator-valued measures
  - Tosio Kato, Perturbation Theory for Linear Operators, 2nd ed., Classics in Mathematics, Springer, 1995, DOI 10.1007/978-3-642-66282-9, for perturbation and regular spectral subspaces of varying operators
---

# WP-303 — Fixed-source spectral-cut kernels have no regular Grassmann motion, while positive compressions are POVM-universal

## Claim

`WP-302` leaves open a source-forced, nonhomogeneous or infinite-dimensional moving nullspace. The most direct way to obtain such motion from one fixed self-adjoint source operator `H` is to let the kernel be a moving spectral subspace of `H`. That entire fixed-source spectral-cut category can be classified before any Gamma matching is attempted.

If

\[
P_t=\mathbf 1_{S_t}(H)
\tag{1}
\]

for Borel sets `S_t`, then all `P_t` commute. Two distinct commuting orthogonal projections are always operator-norm distance one apart. Therefore

\[
\boxed{
P_s\ne P_t\quad\Longrightarrow\quad \|P_s-P_t\|=1,
}
\tag{2}
\]

and every norm-continuous fixed-source spectral-cut path is constant. More strongly, whenever the strong derivative of such a path exists, it is exactly zero. Hence a nonconstant family of kernels obtained only by moving a spectral cut through one fixed source operator cannot supply an ordinary local Fubini--Study/Grassmann tangent: its motion is necessarily singular in the parameter.

The canonical positive threshold realization makes this concrete. Set

\[
Q_t:=\bigl((H-t)_+\bigr)^2\succeq0,
\qquad
P_t:=\mathbf 1_{\{0\}}(Q_t).
\tag{3}
\]

Then

\[
\boxed{P_t=E_H(({-}\infty,t])},
\tag{4}
\]

so the moving zero space is a nested spectral filtration. On the source-native pure-point log-energy carrier recorded in `WP-275`, it is a step filtration at prime-power energies. Any fixed positive compression

\[
M_V(\Delta):=V^*E_H(\Delta)V\succeq0
\tag{5}
\]

remains atomic on the same support and therefore cannot turn that local threshold motion into the smooth nonconstant archimedean Gamma/digamma profile.

There is an opposite exact boundary. Equation (5) is precisely a positive operator-valued measure, and Naimark dilation gives the converse: every normalized POVM is a compression of a projection-valued measure on a larger Hilbert space. Thus if the ambient spectral measure, dilation space, or compression is selected freely in order to match a desired positive response, the construction becomes **POVM-universal**. In the scalar case every prescribed probability measure is realized by a multiplication operator and one cyclic vector, with no primes at all.

The first source-forced spectral escape left by `WP-302` therefore lands in another rigidity/programming dichotomy:

\[
\boxed{
\begin{array}{c}
\text{one fixed source operator + moving spectral cut}
\end{array}
\Rightarrow
\begin{array}{c}
\text{singular/commuting projector motion},
\end{array}
}
\tag{6}
\]

while freeing the spectral realization recovers the universal POVM category. Neither supplies an independent global Weil sign theorem.

A surviving moving-nullspace route must change mechanism: for example a source-forced **nonnested spectral subspace of a genuinely varying noncommuting operator family**, an independently forced nonlocal resolvent/scattering/boundary transform of the spectral measure, or a finite--archimedean coupled operator formed before projection. The present result does not rule out those categories.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + FIXED-SOURCE-SPECTRAL-CUT-RIGIDITY + COMMUTING-PROJECTION-NORM-DISCRETENESS + STRONG-DERIVATIVE-ZERO + PURE-POINT-ARCHIMEDEAN-MISMATCH + POVM-COMPRESSION + NAIMARK-PROGRAMMABILITY-CONTROL + MOVING-NULLSPACE-ESCAPE-NARROWED + CLASSICAL-OPERATOR-THEORY + NOT-WEIL-POSITIVITY`.

## 1. The first source-forced spectral law after WP-302

`WP-301` shows that a fixed frustration-free positive Hamiltonian has a fixed common kernel and screens its nonzero archimedean spectrum. `WP-302` therefore asks for a kernel that moves for a reason supplied by the source rather than by fitting a path to the target.

A fixed self-adjoint operator `H` already supplies a canonical spectral calculus. The broadest projector one can make from `H` alone without adding a second operator is

\[
P_t=\mathbf1_{S_t}(H)
=E_H(S_t)
\tag{7}
\]

for a parameter-dependent Borel set `S_t`. Thresholds, moving windows, unions of bands, and source-selected spectral sectors are all special cases.

The key structural fact is not the shape of `S_t`. It is that all these projectors live in the same abelian von Neumann algebra generated by `H`:

\[
P_sP_t=P_tP_s
\qquad(s,t\in\mathbb R).
\tag{8}
\]

That commutativity alone prevents regular Grassmann motion.

## 2. Distinct commuting projections are always unit distance apart

Let `P` and `Q` be commuting orthogonal projections. Then

\[
(P-Q)^2=P(I-Q)+(I-P)Q.
\tag{9}
\]

The two terms on the right are orthogonal projections with orthogonal ranges, so `(P-Q)^2` is itself an orthogonal projection. If `P\ne Q`, then `(P-Q)^2\ne0`, and therefore

\[
\boxed{\|P-Q\|=1.}
\tag{10}
\]

Applying this to (7) proves the following.

### Proposition 1

If `t -> P_t=1_{S_t}(H)` is operator-norm continuous on an interval `I`, then `P_t` is constant on `I`.

### Proof

At each `t_0 in I`, norm continuity gives a neighborhood on which `||P_t-P_{t_0}||<1`. Equation (10) then forces `P_t=P_{t_0}` throughout that neighborhood. The path is locally constant; connectedness of `I` makes it constant. ∎

Thus merely replacing a fixed kernel by a moving **spectral window of the same source operator** does not produce a regular curve in the ordinary projection Grassmannian. The obstruction is stronger than the nested-threshold case: every Borel spectral-cut family of one fixed `H` is norm-discrete whenever it actually changes.

## 3. Strong differentiability also collapses

One might weaken the topology and ask only for a strong derivative. Pairwise commutativity still kills the tangent.

### Proposition 2

Let `P_t` be a family of orthogonal projections that commute pairwise. If the strong derivative

\[
D_t:=\operatorname*{s-lim}_{h\to0}
\frac{P_{t+h}-P_t}{h}
\tag{11}
\]

exists, then

\[
\boxed{D_t=0.}
\tag{12}
\]

### Proof

Every difference quotient in (11) commutes with `P_t`, hence the strong limit `D_t` commutes with `P_t`.

Differentiate `P_t^2=P_t` strongly. The existence of the derivative implies strong continuity at `t`; uniform boundedness of the convergent difference quotients justifies the product rule, giving

\[
D_tP_t+P_tD_t=D_t.
\tag{13}
\]

Because `D_tP_t=P_tD_t`, equation (13) becomes

\[
2P_tD_t=D_t.
\tag{14}
\]

Multiplying by `P_t` gives `2P_tD_t=P_tD_t`, hence `P_tD_t=0`; substituting into (14) yields `D_t=0`. ∎

Consequently a pairwise-commuting projector family that is strongly differentiable at every point of a connected interval is constant there. Smooth nontrivial motion of spectral subspaces therefore requires leaving the abelian projector family of one fixed operator; a genuinely varying operator family can do this because its spectral projectors at different parameter values need not commute.

## 4. The canonical positive threshold is a singular filtration

The cleanest way to make the moving projector the zero space of a positive constraint is

\[
f_t(\lambda)=((\lambda-t)_+)^2,
\qquad
Q_t=f_t(H)\succeq0.
\tag{15}
\]

Its zero set is exactly `(-infinity,t]`, so functional calculus gives

\[
\ker Q_t=E_H(({-}\infty,t])\mathcal H,
\qquad
P_t=E_H(({-}\infty,t]).
\tag{16}
\]

For `s<t`,

\[
P_t-P_s=E_H((s,t])
\tag{17}
\]

is an orthogonal projection. This is the nested specialization of Proposition 1.

Nonconstant threshold families can still be strongly continuous. For the multiplication operator `H=M_x` on `L^2(mu)`,

\[
(P_tf)(x)=\mathbf1_{(-\infty,t]}(x)f(x)
\tag{18}
\]

is strongly continuous at atom-free thresholds. But its local motion is generically too rough to possess a tangent:

\[
\left\|
\frac{(P_{t+h}-P_t)f}{h}
\right\|^2
=
\frac{1}{h^2}
\int_{(t,t+h]}|f(x)|^2\,d\mu(x).
\tag{19}
\]

If the scalar spectral measure `|f|^2 mu` has a positive finite density `rho_f(t)` at `t`, then the right side is

\[
\frac{\rho_f(t)}{|h|}+o(|h|^{-1}),
\tag{20}
\]

and diverges. The nontrivial motion sits in spectral increments rather than in a finite Grassmann tangent.

## 5. Hilbert--Schmidt Grassmann speed does not regularize a genuine crossing

Suppose a faithful semifinite trace `tau` is available and local threshold increments have finite trace. For `h>0`, orthogonality of the increment gives

\[
\|P_{t+h}-P_t\|_{2,\tau}^2
=\tau(E_H((t,t+h])).
\tag{21}
\]

If

\[
\tau(E_H((t,t+h]))
=\rho_\tau(t)h+o(h),
\qquad
0<\rho_\tau(t)<\infty,
\tag{22}
\]

then

\[
\frac{\|P_{t+h}-P_t\|_{2,\tau}^2}{h^2}
=\frac{\rho_\tau(t)}{h}+o(h^{-1})
\longrightarrow\infty.
\tag{23}
\]

So replacing finite-dimensional Fubini--Study geometry by the most direct Hilbert--Schmidt Grassmann geometry does not create a finite local metric speed at an absolutely-continuous spectral crossing. The natural finite first-order object is instead the **spectral measure** `dE_H`, not `\dot P_t` as a bounded tangent.

This is a genuine third case beyond `WP-302`: the path is neither a bounded homogeneous orbit nor an arbitrary smooth curve. It is canonical but singular.

## 6. The current Mathia log-energy specialization stays atomic

`WP-275` records the source-native Fock/log-energy carrier with

\[
H e_{p^k}=k\log p\;e_{p^k}
=\log(p^k)\;e_{p^k}.
\tag{24}
\]

Its relevant spectral type on that carrier is pure point at the prime-power log energies. The threshold construction gives

\[
P_t
=\sum_{\log(p^k)\le t}E_{p^k},
\tag{25}
\]

with only finitely many source jumps on every bounded `t`-interval.

Let `V:K->H` be any fixed bounded finite--archimedean incidence/compression map and define

\[
M_V(\Delta)=V^*E_H(\Delta)V.
\tag{26}
\]

Because the source spectral measure is pure point,

\[
M_V(\Delta)
=\sum_{\log(p^k)\in\Delta}V^*E_{p^k}V.
\tag{27}
\]

The compression can alter positive weights and matrix directions, but **not spectral support**. Its cumulative response `F_V(t)=M_V((-infinity,t])` is still a step function, and its distributional derivative is still an atomic positive operator-valued measure on the same source energies.

Therefore no parameter-independent local pointwise functional of `F_V(t)` can equal the smooth nonconstant archimedean digamma symbol: between consecutive source jumps the operator input is literally constant. Ordinary differentiation likewise cannot create an absolutely-continuous Gamma density.

The qualifier **local pointwise** is essential. A resolvent, Stieltjes transform, Poisson transform, scattering transform, regularized determinant, or another nonlocal transform of an atomic spectral measure can be smooth and can even produce Gamma/digamma-type functions in classical models. Such a transform is not ruled out. It introduces a kernel, boundary prescription, subtraction, or regularization that must itself be forced by the Mathia source and audited independently.

## 7. Positive compression is exactly the POVM category

Equation (26) is precisely a positive operator-valued measure. If `V` is an isometry, then

\[
M_V(\mathbb R)=V^*V=I_K,
\tag{28}
\]

so `M_V` is a normalized POVM. For general bounded `V` it is a bounded positive operator-valued measure with total mass `V^*V`.

The converse is classical Naimark dilation: every normalized POVM `M` on the real line can be represented on a larger Hilbert space as

\[
\boxed{
M(\Delta)=V^*E(\Delta)V
}
\tag{29}
\]

for an isometry `V` and a projection-valued measure `E`. On the real line the spectral theorem realizes `E` as the spectral measure of a self-adjoint operator (bounded when the outcome support is bounded, possibly unbounded otherwise).

Therefore allowing the enlarged spectral source and compression to be selected after seeing the desired positive response makes the construction universal. It no longer distinguishes a source-derived Weil mechanism from an inverse realization.

The scalar matched control makes this explicit. Let `mu` be any probability measure on a bounded interval `I`, take

\[
\mathcal H=L^2(I,\mu),
\qquad
(Hf)(x)=x f(x),
\qquad
v(x)=1.
\tag{30}
\]

Then

\[
\boxed{
\langle v,E_H(\Delta)v\rangle
=\mu(\Delta)
}
\tag{31}
\]

for every Borel set `Delta`. Any prescribed positive scalar measure on that window can therefore be encoded as a fixed-source spectral response with no primes at all once the source operator itself is free to choose.

This is the spectral-measure analogue of `WP-302`'s free-path programmability control. There the target positive density could be programmed into the speed of a smooth projector path; here an arbitrary positive measure can be programmed into the spectral measure/dilation. Positivity is genuine in both cases, but without an independent source theorem it certifies the chosen realization rather than explaining the arithmetic target.

## 8. Matched controls and exact scope

The result survives the line's source-removal and generalized-prime controls in two complementary ways.

First, replace the rational prime-power energies in (24) by any locally finite countable set of generalized-generator energies with arbitrary positive weights. Every fixed-source spectral cut still belongs to a commuting projection algebra, and the threshold specialization is still pure point. The regularity and atomicity obstructions are therefore not rational-prime-specific.

Second, remove arithmetic entirely and choose an arbitrary positive scalar measure `mu` in (30). The same PVM/POVM architecture realizes it exactly. Thus a successful fit obtained only after selecting the ambient spectral measure does not become arithmetic evidence merely because its realization is positive and geometric.

The theorem does **not** say that spectral theory is irrelevant. It separates three operations that must not be conflated:

- selecting a Borel spectral subspace of one fixed operator, which is an abelian/commuting operation and cannot move smoothly;
- choosing a new PVM/POVM to reproduce a desired positive measure, which is universally possible and therefore needs an independent source law;
- deriving a nonlocal transform or a noncommuting operator deformation from source geometry, which is additional structure and remains open.

## 9. Prior art and novelty audit

The operator-theoretic ingredients are classical.

The representation `P_t=E_H(S_t)` is the standard projection-valued spectral calculus. The norm gap for distinct commuting projections is an elementary projection identity, and the zero strong derivative follows immediately from combining pairwise commutativity with the tangent identity obtained from `P^2=P`.

Positive compressions of spectral measures and their converse are exactly the classical POVM/Naimark framework. Naimark's 1943 theorem is therefore a **prior-art boundary**, not evidence of a new operator-theoretic structure. Kato perturbation theory supplies the relevant neighboring category: regular spectral projectors can occur for isolated spectral subspaces of a genuinely varying operator family. That mechanism differs essentially from changing a Borel cut of one fixed `H`, because projectors at different parameter values need not commute.

A targeted literature search found no basis for attributing the projection lemmas or POVM dilation to Mathia, and no prior result was found phrased as the present Weil-positivity route exclusion. The branch-local delta is the classification of a concrete escape left by `WP-302`: **the simplest target-independent spectral source law does not land between rigidity and programmability. Keeping one source operator forces singular commuting motion; freeing the spectral realization recovers a universal inverse category.**

This is not a new spectral theorem, a new dilation theorem, a new positivity criterion, or evidence for RH.

## 10. Adversarial falsification gates

The finding should be narrowed or withdrawn if any of the following fails:

1. spectral projectors `1_{S_t}(H)` of one fixed self-adjoint `H` commute pairwise;
2. two distinct commuting orthogonal projections have operator-norm distance exactly one;
3. pairwise commutativity plus the differentiated identity `P_t^2=P_t` forces any existing strong derivative to vanish;
4. for `Q_t=((H-t)_+)^2`, its zero-space projection is exactly `E_H((-infinity,t])`;
5. equation (19) correctly describes the strong difference quotient in the multiplication-operator model, including the stated positive-density divergence;
6. under the trace hypothesis in section 5, equation (21) and the `h^{-1}` metric-speed divergence are correct;
7. the source carrier invoked from `WP-275` is genuinely pure point at the stated prime-power log energies and locally finite on bounded energy windows;
8. a fixed compression `V^*E_H(.)V` cannot create spectral support outside the support of `E_H`;
9. Naimark dilation gives the converse POVM representation used in section 7;
10. the scalar multiplication-operator control (30)--(31) realizes an arbitrary prescribed probability measure;
11. the conclusion remains restricted to **spectral cuts of one fixed source operator and their local/fixed positive compressions**, not to noncommuting spectral projectors of varying operators or independently forced nonlocal spectral transforms.

Items 1--6 and 8--10 are exact operator identities/theorems. Item 7 is the internal source specialization already recorded in `WP-275`. Item 11 is a scope boundary: a resolvent or scattering construction that smooths the pure-point measure is not a counterexample because it changes the readout category and introduces additional source structure that must be audited on its own terms.

## 11. Consequence for the research frontier

The moving-nullspace route now has a sharper sequence of gates.

A fixed kernel loses the archimedean spectrum (`WP-301`). A finite-dimensional homogeneous moving kernel is too rigid, while a freely chosen smooth projector path is too programmable (`WP-302`). `WP-303` now closes the most immediate source-law compromise: **all moving spectral cuts of one fixed source operator remain in one commuting projection algebra, so nontrivial motion is singular; the current pure-point source stays atomic under fixed positive compression; and freeing the spectral measure merely invokes universal POVM realization.**

The next admissible candidate therefore needs a stronger source law than `P_t=1_{S_t}(H)` for one fixed `H`. Three mechanisms remain genuinely different:

1. a **nonnested, noncommuting projector** arising as an isolated spectral subspace of a source-forced varying operator `H(t)`, with the operator family fixed before comparison with Gamma;
2. a **nonlocal or singular transform** of the current spectral measure whose kernel, boundary condition, subtraction and normalization are forced independently rather than fitted to the completed zeta factor;
3. a **genuinely coupled finite--archimedean operator** whose spectral type and sign theorem are produced only after the two sectors interact, so neither the prime-power atomic carrier nor an externally supplied continuum is the final input.

Any survivor still has to meet the original line mandate: recover the finite-prime, archimedean and global counterterms under one audited Weil normalization and obtain the final nonnegativity from an independent geometric theorem. `WP-303` supplies no such theorem; it removes one natural but insufficient way of making the zero space move.

## Internal dependencies

- `research/weil_positivity/findings/WP-275-source-time-covariant-positive-sampling-compressions-are-trivial-by-spectral-type.md`
- `research/weil_positivity/findings/WP-301-frustration-free-holonomy-zero-modes-are-universal-kernel-intersections.md`
- `research/weil_positivity/findings/WP-302-homogeneous-moving-nullspaces-are-archimedean-rigid-while-free-projector-paths-are-programmable.md`
