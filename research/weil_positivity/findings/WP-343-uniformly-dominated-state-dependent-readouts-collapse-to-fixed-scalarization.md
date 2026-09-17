---
id: WP-343
title: Uniformly dominated state-dependent readouts collapse to fixed scalarization
branch: weil_positivity
status: supported
kind: state-dependent-positive-readout-domination-obstruction
claim_strength: exact reduction; a stationary operator-order CND transport cannot evade WP-342 by choosing a displacement-dependent positive readout when the readout family is uniformly dominated by one fixed positive functional; finite-dimensional C*-algebras automatically satisfy this domination for arbitrary state selection, and every continuous nonnegative degree-one readout on the positive cone is trace-dominated
created: 2026-09-17
related: [WP-338, WP-339, WP-340, WP-341, WP-342]
prior_art:
  - Huzihiro Araki, Bures Distance Function and a Generalization of Sakai's Non-commutative Radon-Nikodym Theorem, Publications of the Research Institute for Mathematical Sciences 8 (1972), 335-362, DOI 10.2977/prims/1195193113
  - Michael Henle, A Lebesgue Decomposition Theorem for C*-Algebras, Canadian Mathematical Bulletin 15 (1972), 87-91, DOI 10.4153/CMB-1972-016-2
  - Palle E. T. Jorgensen and James Tian, Factorization of positive definite kernels. Correspondences: C*-algebraic and operator valued context vs scalar valued kernels, arXiv:2505.21037 (2025)
---

# WP-343 — Uniformly dominated state-dependent readouts collapse to fixed scalarization

## Claim

`WP-342` leaves nonlinear and state-dependent extraction open because a positive functional chosen separately for each displacement need not itself define one scalar conditionally negative-definite function. There is nevertheless a sharp large subclass in which that extra freedom is illusory.

Let

\[
\Gamma=\bigoplus_{p\ \mathrm{prime}}\mathbb Z e_p,
\qquad
L(\alpha)=\sum_p \alpha_p\log p,
\tag{1}
\]

and let `A` be a unital C*-algebra. Let

\[
\Psi:\Gamma\to A_{\rm sa},
\qquad \Psi(0)=0,
\tag{2}
\]

be a Hermitian translation-invariant operator-order conditionally negative-definite transport in the sense of `WP-342`. Thus `Psi(-alpha)=Psi(alpha)` and

\[
\sum_{i,j}\overline{c_i}c_j\Psi(\alpha_i-\alpha_j)\preceq0
\quad\text{whenever}\quad \sum_i c_i=0.
\tag{3}
\]

Let `omega:A->C` be a fixed positive linear functional. Suppose that for each `alpha` a possibly different positive linear functional `phi_alpha` is chosen, but that the whole family is uniformly order-dominated by `omega`:

\[
0\le \phi_\alpha\le C\omega
\qquad(\alpha\in\Gamma)
\tag{4}
\]

for one finite constant `C>0`. Define the moving readout

\[
s(\alpha):=\phi_\alpha(\Psi(\alpha)).
\tag{5}
\]

If for some `a>0` and `R>=0`

\[
s(\alpha)\ge aL(\alpha)^2
\qquad\text{whenever }|L(\alpha)|\ge R,
\tag{6}
\]

then the **fixed** scalarization

\[
\psi_\omega(\alpha):=\omega(\Psi(\alpha))
\tag{7}
\]

already satisfies

\[
\psi_\omega(\alpha)\ge \frac{a}{C}L(\alpha)^2
\qquad\text{whenever }|L(\alpha)|\ge R.
\tag{8}
\]

Consequently `WP-341` and `WP-342` apply to `psi_omega`: its scalar Levy--Khinchin quadratic component `q_omega` obeys

\[
\boxed{
q_\omega(\alpha)\ge \frac{a}{C}L(\alpha)^2
\qquad(\alpha\in\Gamma).
}
\tag{9}
\]

Thus **state dependence alone does not evade the stationary log-square obstruction when the moving positive probes remain uniformly dominated by one fixed positive functional**. Any Weil-relevant quadratic logarithmic control produced by such a family was already present in a fixed scalar quadratic sector.

There are two useful corollaries.

First, if `A` is finite-dimensional, *every* family of states is automatically uniformly dominated by one fixed finite trace functional. Hence arbitrary displacement-dependent state selection, including choosing the maximizing eigenvector separately at every `alpha`, does not escape `WP-342`.

Second, on a fixed matrix algebra every continuous nonnegative positively one-homogeneous scalar readout of the positive cone is bounded above by a constant multiple of the trace. Therefore regular degree-one nonlinear spectral readouts — operator norm, extremal positive eigenvalue, Schatten norms, Ky Fan norms, determinant root, and any other continuous one-homogeneous readout — also collapse to the fixed-trace obstruction.

**Classification:** `EXACT-DERIVED + OPERATOR-ORDER-CND + MOVING-POSITIVE-READOUT + UNIFORM-FUNCTIONAL-DOMINATION + FIXED-SCALARIZATION-REDUCTION + FINITE-DIMENSIONAL-STATE-SELECTION-CLOSURE + REGULAR-ONE-HOMOGENEOUS-NONLINEAR-CLOSURE + FULL-PRIME-EXPONENT-LATTICE + MATCHED-CONTROL + DECISIVE-NEGATIVE-FOR-BOUNDED-RADON-NIKODYM-READOUT-FAMILIES + SINGULAR-INFINITE-DIMENSIONAL-BOUNDARY-LEFT-OPEN + NOT-WEIL-POSITIVITY`.

## 1. Operator-order CND transport has positive increments

The domination argument needs positivity of the individual transport values, and in the standard Hermitian CND setting this is automatic.

Apply (3) to the two points `0,alpha` with coefficients `1,-1`. Since `Psi(0)=0` and Hermitian symmetry gives `Psi(-alpha)=Psi(alpha)`,

\[
-2\Psi(\alpha)\preceq0.
\tag{10}
\]

Hence

\[
\boxed{\Psi(\alpha)\succeq0\qquad(\alpha\in\Gamma).}
\tag{11}
\]

This is the operator-valued analogue of the elementary fact that a normalized real negative-type function is nonnegative. It is not an additional arithmetic assumption.

## 2. Uniform domination removes the moving-state freedom

Because `Psi(alpha)` is positive, (4) can be evaluated directly on it:

\[
0\le \phi_\alpha(\Psi(\alpha))
\le C\,\omega(\Psi(\alpha)).
\tag{12}
\]

Combining (6) and (12) gives (8). The right-hand side of (7) is now a **fixed** positive scalarization of the same operator-valued CND transport, so `WP-342` implies that `psi_omega` is scalar CND. Its quadratic dilation limit is therefore

\[
q_\omega(\alpha)
=
\lim_{m\to\infty}\frac{\psi_\omega(m\alpha)}{m^2}.
\tag{13}
\]

Applying (8) to `m alpha` and letting `m` tend to infinity yields (9).

The point is not that `phi_alpha` itself becomes stationary or that the moving scalar readout (5) becomes CND. Neither is required. Uniform domination produces a different fixed scalar CND observable that is at least as strong, up to the constant `C`, for the only growth property relevant to the `WP-338`--`WP-341` variance obstruction.

This is exactly the kind of reduction that a state-dependent proposal must defeat. If its varying states all have bounded Radon--Nikodym density relative to one fixed reference functional, the state motion cannot be the source of the missing logarithmic quadratic direction.

## 3. Finite-dimensional state selection is automatically dominated

Take first `A=M_d(C)` and let

\[
\phi_\rho(X)=\operatorname{Tr}(\rho X),
\qquad \rho\succeq0,
\quad \operatorname{Tr}\rho=1
\tag{14}
\]

be an arbitrary state. Since every density matrix satisfies `0<=rho<=I`, for `X>=0`

\[
\phi_\rho(X)
=\operatorname{Tr}(\rho X)
\le \operatorname{Tr}(X).
\tag{15}
\]

Thus **all states at once**, including an adversarially or source-dependently chosen family `rho_alpha`, satisfy

\[
\phi_{\rho_\alpha}\le \operatorname{Tr}.
\tag{16}
\]

The constant is `C=1` if the unnormalized trace is used as the fixed positive functional. Equivalently, relative to the normalized trace `tau=Tr/d`, one has `phi_rho<=d tau`.

Therefore

\[
\phi_{\rho_\alpha}(\Psi(\alpha))\gtrsim L(\alpha)^2
\Longrightarrow
\operatorname{Tr}\Psi(\alpha)\gtrsim L(\alpha)^2,
\tag{17}
\]

and the trace quadratic sector already contains the arithmetic log-square.

The same argument applies to every finite-dimensional C*-algebra

\[
A\cong\bigoplus_{j=1}^r M_{d_j}(\mathbb C).
\tag{18}
\]

Writing a state by positive block densities `rho_j` with total trace one gives `rho_j<=I` in every block, hence it is dominated by the fixed positive functional `omega(X)=sum_j Tr(X_j)`. Finite internal channel multiplicity therefore cannot hide the required quadratic direction behind a displacement-dependent choice of state.

A particularly important example is the maximal state readout

\[
\sup_{\phi\in S(M_d)}\phi(X)=\lambda_{\max}(X)=\|X\|,
\qquad X\succeq0.
\tag{19}
\]

Even though the maximizing state may change discontinuously with `X`,

\[
\lambda_{\max}(X)\le\operatorname{Tr}X.
\tag{20}
\]

So selecting a new top eigenvector at every arithmetic displacement does not create an escape.

## 4. Regular finite-dimensional nonlinear readouts are trace dominated

The reduction is broader than state selection. Let

\[
F:M_d(\mathbb C)_+\to[0,\infty)
\tag{21}
\]

be continuous and positively one-homogeneous:

\[
F(tX)=tF(X),\qquad t\ge0.
\tag{22}
\]

The unit-trace positive slice

\[
K_d=\{X\succeq0:\operatorname{Tr}X=1\}
\tag{23}
\]

is compact. Hence

\[
C_F:=\max_{X\in K_d}F(X)<\infty.
\tag{24}
\]

For every nonzero `X>=0`, write `X=(Tr X)Y` with `Y in K_d`. Then

\[
\boxed{F(X)\le C_F\operatorname{Tr}X.}
\tag{25}
\]

Therefore

\[
F(\Psi(\alpha))\ge aL(\alpha)^2
\Longrightarrow
\operatorname{Tr}\Psi(\alpha)
\ge \frac{a}{C_F}L(\alpha)^2,
\tag{26}
\]

and once again the fixed trace scalarization falls under `WP-342`.

This covers the regular degree-one nonlinear spectral examples left explicitly open there. For positive matrices, `lambda_max`, every Schatten `p`-norm with `p>=1`, every Ky Fan norm, and `(det X)^{1/d}` are continuous and one-homogeneous; the last also satisfies the sharper arithmetic--geometric mean bound

\[
(\det X)^{1/d}\le \frac1d\operatorname{Tr}X.
\tag{27}
\]

The theorem is deliberately about **degree-one** readouts of the positive transport value. Such readouts preserve the quadratic dilation order of a quadratic operator energy. A higher-degree functional such as `det X` without the `d`th root changes the dilation order and is not ruled out by (25); matching it to a quadratic Weil target would require an additional normalization or singular scaling law that must itself be source-derived.

## 5. Why infinite-dimensional moving states are a real boundary

Uniform domination is not automatic in infinite-dimensional operator algebras. This is not a technical gap.

For example, on `B(ell^2)` let `phi_n` be the vector state at the `n`th basis vector and let `P_n` be the corresponding rank-one projection. If there were a bounded positive functional `omega` and finite `C` with

\[
\phi_n\le C\omega
\qquad\text{for every }n,
\tag{28}
\]

then

\[
1=\phi_n(P_n)\le C\omega(P_n).
\tag{29}
\]

For every `N`, positivity and orthogonality give

\[
\omega(I)
\ge \omega\!\left(\sum_{n=1}^N P_n\right)
=\sum_{n=1}^N\omega(P_n)
\ge \frac{N}{C},
\tag{30}
\]

which is impossible as `N` tends to infinity.

Thus an infinite-dimensional family can genuinely move into mutually orthogonal sectors faster than any one bounded positive functional can dominate. In von Neumann language this is the boundary at which Radon--Nikodym densities relative to a fixed finite reference cease to be uniformly bounded, or where one has to pass to a semifinite/infinite weight instead of a bounded state.

This observation does **not** produce Weil positivity. It identifies what a surviving state-dependent route must pay for: the readout must escape every fixed finite domination envelope. That is the operator-algebraic analogue of the moving-tail phenomenon behind `WP-333`--`WP-339`, where bounded-observable convergence coexists with a defect carried farther and farther into the tail.

## 6. Matched controls show that domination is not arithmetic selectivity

Nothing in the proof uses the prime logarithms until the target lower bound is imposed. Replace `log p` by arbitrary nonzero generator weights `ell_p` and set

\[
L_\ell(\alpha)=\sum_p\alpha_p\ell_p.
\tag{31}
\]

The same implication holds:

\[
\phi_\alpha(\Psi(\alpha))\gtrsim L_\ell(\alpha)^2,
\quad
\phi_\alpha\le C\omega
\Longrightarrow
q_\omega(\alpha)\gtrsim L_\ell(\alpha)^2.
\tag{32}
\]

So neither state motion nor regular finite-dimensional nonlinear extraction selects `ell_p=log p`. A Mathia-native proposal must still explain from the source why the arithmetic logarithmic homomorphism is singled out, and then separately supply the finite-prime/archimedean/polar assembly and its independent sign theorem.

This also prevents a misleading interpretation of the result. The existence of a trace channel containing `L^2` is not itself progress toward RH: the same theorem holds on a free abelian matched control with arbitrary generator labels. Its value is negative and structural — it removes a purported source of selectivity.

## 7. Prior-art and novelty audit

Order domination of positive functionals and its Radon--Nikodym interpretation are classical operator-algebraic material. Sakai's noncommutative Radon--Nikodym theory and extensions such as Araki's 1972 treatment describe dominated normal positive functionals in operator terms; C*-algebraic Lebesgue/Radon--Nikodym decompositions likewise predate this work. Modern operator-valued kernel theory also treats domination and scalarization through positive operators and completely positive maps.

No novelty is therefore claimed for positive-functional domination, density matrices, trace bounds, Radon--Nikodym derivatives, compactness of the unit-trace cone, or operator-valued CND kernels.

The Mathia-specific content is the **frontier reduction** relative to `WP-341`--`WP-342`:

- `WP-342` closed fixed positive scalarization but explicitly left state-dependent and nonlinear readouts open;
- uniform domination shows that a moving positive readout cannot help unless it escapes every fixed bounded positive envelope;
- finite-dimensional operator algebras automatically have such an envelope for *all* states;
- continuous degree-one nonlinear positive readouts on a fixed matrix cone are also trace dominated;
- therefore a surviving nonlinear/operator-valued route must become genuinely singular or infinite-dimensional, nonstationary, non-one-homogeneous, or operator-level before scalarization rather than merely choosing a different finite-dimensional positive probe at each displacement.

A bounded literature audit found the expected classical noncommutative Radon--Nikodym and operator-valued kernel frameworks, not a distinct arithmetic theorem with this conclusion. The result is a branch-specific obstruction, not a claimed new theorem of C*-algebras.

## Representation audit

The hypothesis `phi_alpha<=C omega` is order-theoretic and basis independent. Under a *-isomorphism of `A`, both sides transform covariantly and the domination constant is unchanged.

For matrix algebras, the unnormalized trace is invariant under unitary change of basis. The compactness argument for (25) does not require `F` to be spectral or unitary invariant; it applies to any continuous nonnegative one-homogeneous scalar readout. Therefore the conclusion is stronger than a statement about eigenvalue coordinates.

What is not intrinsic is the existence of a preferred finite reference functional in an arbitrary infinite-dimensional source. The theorem does not insert one. It says that **if** all source-selected probes remain uniformly dominated by one, then their apparent state dependence cannot be the missing mechanism. If a candidate deliberately leaves that class, the source must canonically explain the unbounded/singular migration rather than choose it because it reproduces the Weil target.

## Consequence for the Weil-positivity search

The open boundary after `WP-342` can be narrowed from "state-dependent or nonlinear positive readout" to a much smaller class:

\[
\boxed{
\begin{aligned}
&\text{stationary operator-order CND transport}
\\
&+\ \text{moving positive readouts uniformly dominated by one fixed functional}
\\
&+\ \text{quadratic control of the arithmetic logarithm}
\\[2mm]
&\Longrightarrow\ \text{a fixed scalar quadratic sector already contains }L^2.
\end{aligned}
}
\tag{33}
\]

In particular, **fixed finite-dimensional internal geometry plus arbitrary state selection is not a new source of Weil positivity**, and neither is a regular degree-one nonlinear scalar observable on that geometry.

The live operator-valued escape now requires at least one genuinely stronger ingredient: an infinite-dimensional family of probes with no uniform bounded Radon--Nikodym envelope, a canonical semifinite or singular weight, a nonlinear readout singular on the positive-cone boundary, nonstationary/source-supported geometry, a change of dilation order with an independently forced normalization, or an operator-level/noncommutative positivity theorem that is established before any scalar readout. None of these remaining possibilities by itself supplies the Gamma factor, polar counterterms, or the global Weil sign.