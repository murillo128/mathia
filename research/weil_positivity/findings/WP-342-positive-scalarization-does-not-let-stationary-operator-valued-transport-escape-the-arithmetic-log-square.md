---
id: WP-342
title: Positive scalarization does not let stationary operator-valued transport escape the arithmetic log-square
branch: weil_positivity
status: supported
kind: operator-valued-stationary-scalarization-obstruction
claim_strength: exact reduction under a fixed positive linear readout; any C*-algebra-valued stationary conditionally-negative transport whose positive scalarization supplies the quadratic logarithmic control required by WP-338--WP-341 already has that arithmetic log-square in the scalarized quadratic Levy-Khinchin sector; operator-valued internal channels alone do not evade the stationary scalar obstruction
created: 2026-09-17
related: [WP-338, WP-339, WP-340, WP-341]
prior_art:
  - I. J. Schoenberg, Metric Spaces and Positive Definite Functions, Transactions of the American Mathematical Society 44 (1938), 522-536, DOI 10.2307/1989894
  - Fritz Gesztesy and Michael Pang, On (conditional) positive semidefiniteness in a matrix-valued context, Studia Mathematica 236 (2017), 93-131, arXiv:1602.00384
  - Palle E. T. Jorgensen and James Tian, Factorization of positive definite kernels. Correspondences: C*-algebraic and operator valued context vs scalar valued kernels, arXiv:2505.21037 (2025)
---

# WP-342 — Positive scalarization does not let stationary operator-valued transport escape the arithmetic log-square

## Claim

`WP-341` deliberately left operator-valued/noncommutative transport open because an operator-valued positive correspondence need not reduce to a single scalar negative-type cost **before** positivity is taken. There is nevertheless one large operator-valued subclass for which the apparent escape is illusory.

Let

\[
\Gamma=\bigoplus_{p\ \mathrm{prime}}\mathbb Z e_p,
\qquad
L(\alpha)=\sum_p\alpha_p\log p,
\tag{1}
\]

and let `A` be a unital C*-algebra. Suppose

\[
\Psi:\Gamma\to A_{\rm sa},
\qquad \Psi(0)=0,
\tag{2}
\]

is translation-invariant and conditionally negative in the C*-order, meaning that for every finite family `alpha_1,...,alpha_m in Gamma` and every `c_1,...,c_m in C` with `sum_i c_i=0`,

\[
\sum_{i,j}\overline{c_i}c_j\,\Psi(\alpha_i-\alpha_j)\preceq0
\quad\text{in }A_{\rm sa}.
\tag{3}
\]

Let `phi:A->C` be any **fixed positive linear functional** and define the scalar readout

\[
\psi_\phi(\alpha):=\phi(\Psi(\alpha)).
\tag{4}
\]

Then `psi_phi` is a scalar conditionally negative-definite function on `Gamma`. Consequently, if there are `a>0` and `R>=0` such that

\[
\psi_\phi(\alpha)\ge aL(\alpha)^2
\qquad\text{whenever }|L(\alpha)|\ge R,
\tag{5}
\]

then the scalar Levy--Khinchin quadratic component `q_phi` of `psi_phi` already satisfies

\[
\boxed{
q_\phi(\alpha)\ge aL(\alpha)^2
\qquad(\alpha\in\Gamma).
}
\tag{6}
\]

Equivalently, in the canonical Hilbert realization `q_phi(alpha)=||D_phi alpha||^2`, there is a bounded covector `w_phi` with

\[
\boxed{
L(\alpha)=\langle D_\phi\alpha,w_\phi\rangle,
\qquad
\|w_\phi\|\le a^{-1/2}.
}
\tag{7}
\]

Thus **passing from a scalar stationary transport to a matrix/C*-algebra-valued stationary transport does not by itself evade `WP-341` if the Weil-relevant observable is obtained by a fixed positive linear scalarization**. Any quadratic logarithmic control visible after that readout was already present as the arithmetic log-square in the readout's scalar quadratic sector.

For the concrete matrix-valued case `A=M_d(C)`, every vector state

\[
\phi_v(T)=v^*Tv,
\qquad \|v\|=1,
\tag{8}
\]

therefore obeys the same obstruction. Normalized traces and positive mixtures of vector states do as well.

**Classification:** `EXACT-DERIVED + OPERATOR-ORDER-CND + POSITIVE-LINEAR-SCALARIZATION + WP-341-REDUCTION + FULL-PRIME-EXPONENT-LATTICE + MATCHED-CONTROL + DECISIVE-NEGATIVE-FOR-STATIONARY-OPERATOR-LIFT-WITH-FIXED-POSITIVE-READOUT + NONCOMMUTATIVE-AND-NONLINEAR-BOUNDARY-LEFT-OPEN + NOT-WEIL-POSITIVITY`.

## 1. Positive scalarization preserves conditional negative type

Apply `phi` to (3). Positivity of `phi` means that `X\preceq0` implies `phi(X)\le0`. By linearity,

\[
\sum_{i,j}\overline{c_i}c_j\,
\psi_\phi(\alpha_i-\alpha_j)
=
\phi\!\left(
\sum_{i,j}\overline{c_i}c_j\,
\Psi(\alpha_i-\alpha_j)
\right)
\le0.
\tag{9}
\]

Hence `psi_phi` is scalar CND. No representation choice is involved in this step: it uses only the order cone of the C*-algebra and a positive functional.

If one instead starts with an `A`-valued positive-definite kernel, the analogous scalarization statement is also standard. A positive functional on a C*-algebra is completely positive, so applying it entrywise to a positive matrix over `A` yields a positive scalar matrix. Matrix/operator-valued positive-definite kernels and their scalar projections are classical operator-theoretic objects; no novelty is claimed for this preservation fact.

The important point for this research line is what happens **after** the reduction: a fixed positive observable cannot hide the output from scalar negative-type rigidity.

## 2. WP-341 applies verbatim after the readout

Once (9) is established, `psi_phi` satisfies exactly the hypotheses classified by `WP-341`: it is a scalar translation-invariant CND cost on the full prime-exponent displacement group.

Assume the operator-valued construction is proposed to repair the logarithmic-variance defect from `WP-338`--`WP-340` through the observable `phi`, so that (5) holds. `WP-341` then gives the scalar Levy--Khinchin decomposition

\[
\psi_\phi(\alpha)
=q_\phi(\alpha)
+
\int_{\widehat\Gamma\setminus\{1\}}
(1-\operatorname{Re}\chi(\alpha))\,d\mu_\phi(\chi),
\tag{10}
\]

with

\[
q_\phi(\alpha)
=
\lim_{m\to\infty}
\frac{\psi_\phi(m\alpha)}{m^2}.
\tag{11}
\]

Scaling (5) along `m alpha` therefore yields (6), and the bounded-covector factorization from `WP-341` yields (7).

This is stronger than saying that the operator-valued object can be represented by many scalar probes. For **every particular positive probe actually used to obtain the Weil-relevant scalar cost**, the arithmetic burden reappears in that probe's quadratic sector. Internal matrix channels or operator multiplicity cannot transfer the required second-order growth into the bounded spectral/jump part of the scalarized stationary cost.

## 3. Matrix-valued examples do not create a hidden escape

Take `A=M_d(C)`. For a fixed unit vector `v`, (4) becomes

\[
\psi_v(\alpha)=v^*\Psi(\alpha)v.
\tag{12}
\]

If `psi_v` controls `L(alpha)^2`, then its quadratic component already contains `L^2`. The same is true for the normalized trace

\[
\tau(T)=\frac1d\operatorname{Tr}(T)
\tag{13}
\]

and for any density-matrix state

\[
\phi_\rho(T)=\operatorname{Tr}(\rho T),
\qquad \rho\succeq0,
\quad \operatorname{Tr}\rho=1.
\tag{14}
\]

Thus merely replacing a scalar transport cost by a matrix of channels and then evaluating it by a state, trace, expectation value, or fixed positive mixture does not change the stationary obstruction. The scalar readout still lands in the same CND cone classified by `WP-341`.

This also supplies a direct falsification test for proposed operator-valued repairs: identify the actual scalar observable used in the explicit-formula comparison. If it is a fixed positive linear functional and the induced cost is stationary, compute its quadratic dilation limit (11). If that limit does not dominate `L^2`, the proposal cannot supply the required logarithmic second-moment control.

## 4. Matched controls remain fatal to arithmetic selectivity

The proof never uses the special values `log p` until condition (5). Replace them by arbitrary nonzero generator weights `omega_p` and define

\[
L_\omega(\alpha)=\sum_p\alpha_p\omega_p.
\tag{15}
\]

Exactly the same argument gives

\[
\phi(\Psi(\alpha))\gtrsim L_\omega(\alpha)^2
\Longrightarrow
q_\phi(\alpha)\gtrsim L_\omega(\alpha)^2.
\tag{16}
\]

So positive operator-valued scalarization supplies no arithmetic selector. If a Mathia construction canonically singles out `omega_p=log p`, that selectivity must come from additional structure in `Psi`, in the choice of the observable, or in a theorem coupling the operator geometry to arithmetic. It is not a consequence of operator-valued positivity itself.

## 5. Aggressive falsification: what this does not rule out

This result is deliberately narrower than a blanket rejection of operator-valued geometry.

**A genuinely operator-level positivity theorem remains open.** The candidate may never collapse to one fixed scalar state before the decisive positivity argument. Matrix order, complete positivity, modules, correspondences, or noncommutative intersection data could matter intrinsically.

**A basepoint-dependent/nonstationary geometry remains open.** If the response is `Psi(alpha,beta)` rather than a function only of `alpha-beta`, the scalarized object need not fall under the stationary Levy--Khinchin classification used by `WP-341`.

**A nonlinear scalar readout remains open.** Determinants, extremal eigenvalues, Schur complements, infima over states, or state selection depending on the test vector are not fixed positive linear functionals. Some preserve useful positivity, some do not, but they require a separate theorem. `WP-030` already showed that a nonlinear Gram-volume readout can encode arithmetic support in a way a linear trace cannot.

**A non-positive scalar readout is not covered.** An indefinite trace-like functional or subtraction of positive channels can manufacture signs. But then the sign of the resulting scalar Weil form no longer follows merely from positivity of the operator-valued object; an independent sign theorem is again required.

**Noncommutative arithmetic domains remain open.** Here the displacement domain itself is still the abelian group `Gamma`. Replacing the codomain by a noncommutative algebra is not the same as deriving a genuinely noncommutative arithmetic geometry in which the domain/composition law changes.

**The finite--archimedean bridge remains open.** Even if an operator-level theorem forces an arithmetic quadratic direction, this finding does not generate the Gamma factor, polar counterterms, or the full Weil explicit-formula pairing.

These boundaries are essential. For example, a positive block operator can have negative off-diagonal matrix entries, so operator positivity certainly does not imply entrywise positivity. The present obstruction is not an entrywise-sign argument; it is specifically the preservation of CND under a fixed positive scalar probe followed by the exact scalar classification in `WP-341`.

## 6. Prior-art and novelty audit

Schoenberg's negative-type/positive-definite correspondence is classical. Matrix-valued conditional positive/negative definiteness has an established literature; Gesztesy--Pang analyze the matrix-valued Schoenberg setting and explicitly show that some scalar equivalences become subtler in the matrix-valued context. Modern C*-algebraic/operator-valued kernel factorization likewise belongs to standard operator theory; Jorgensen--Tian give a recent Stinespring-type treatment connecting operator-valued kernels, completely positive maps, states, and scalar-valued kernels.

Accordingly, **no novelty is claimed for operator-valued kernels, C*-positivity, positive scalarization, or complete positivity**. The Mathia-specific contribution is the negative reduction against the live `WP-341` frontier:

- `WP-341` left operator-valued transport open;
- the subclass with an abelian stationary displacement domain and a fixed positive linear Weil-relevant readout collapses exactly to the scalar CND setting;
- if that readout controls logarithmic variance, its quadratic Levy--Khinchin sector already contains the arithmetic log-square;
- arbitrary-weight matched controls show that operator-valued positivity alone does not explain why the arithmetic weights are `log p`;
- therefore a surviving operator-valued route must exploit structure that is genuinely lost under fixed positive scalarization: nonstationarity, nonlinear/state-dependent extraction, operator-level coupling, or a genuinely noncommutative/cohomological mechanism.

A bounded literature audit found the expected classical and modern operator-valued positivity frameworks, but no claim is made that the scalarization lemma is new. The finding is a branch-specific **route narrowing**, not a new theorem of operator algebras.

## Representation audit

The order condition (3), positivity of `phi`, and the scalar CND conclusion (9) are basis-independent. In `M_d(C)`, changing matrix coordinates by unitary conjugation changes `v` or `rho` covariantly but does not alter the statement that a fixed positive state produces a scalar CND function.

Stationarity on `Gamma` is substantive rather than a coordinate artifact: it asserts that the transport depends only on the multiplicative exponent displacement. The arithmetic homomorphism `L(alpha)=sum alpha_p log p` is intrinsic to the prime-exponent group once the prime generators are identified by unique factorization.

What is **not** intrinsic without further structure is the choice of scalar state `phi`. If a candidate hand-picks a state precisely to recover `log p`, that is inserted arithmetic data, not a geometric theorem. A serious operator-valued route must explain canonically why the relevant readout exists and why it is the one coupled to the explicit formula.

## Consequence for the Weil-positivity search

The operator-valued escape from `WP-341` can now be narrowed to a precise boundary:

\[
\boxed{
\text{stationary operator-order CND geometry}
+\text{fixed positive scalar readout}
+\text{quadratic control of arithmetic log}
\Longrightarrow
\text{the scalarized quadratic sector already contains }L^2.
}
\tag{17}
\]

Therefore **operator-valuedness is not by itself a new source of Weil positivity**. To remain live, an operator-valued Mathia construction must use genuinely operator-level/nonseparable structure before scalarization, a nonlinear or state-dependent but canonical positive extraction, nonstationary/source-supported geometry, or a noncommutative/cohomological mechanism whose independent positivity theorem survives the explicit-formula bridge.