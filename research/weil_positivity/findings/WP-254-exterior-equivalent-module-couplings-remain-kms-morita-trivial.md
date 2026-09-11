# WP-254 — Exterior-equivalent module couplings remain KMS-Morita trivial

**Status:** `EXACT-DERIVED + MODULE-COCYCLE-NO-GO + EXTERIOR-EQUIVALENCE + KMS-WEIGHT-CORRESPONDENCE + NONPRODUCT-INTERACTION-CONTROL + BOUNDED-ARAKI-PERTURBATION-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-253` rules out every spatial product clock

\[
\delta_t=\operatorname{Ad}(V_t)\otimes\gamma_t
\]

on the stabilization

\[
\mathcal C=\mathcal K(\mathcal H)\otimes\mathcal B
\cong \mathcal K(X),
\qquad
X=\mathcal H\otimes\mathcal B,
\]

because the product flow is induced by a full `\gamma`-compatible Hilbert-`\mathcal B` module dynamics and KMS weights are transported through the resulting equivariant Morita equivalence. Its exact boundary deliberately left **genuinely non-product coupling** open.

A large class of such couplings is not an escape. Any strongly continuous unitary **module cocycle** on `X` produces a generally non-product exterior perturbation of the compact-algebra flow, but it remains a `\gamma`-compatible full module dynamics over the same coefficient system. Hence its KMS-weight cone is still exactly the KMS-weight cone of `(\mathcal B,\gamma)`, which is empty at every nonzero inverse temperature by `WP-250`.

More precisely, if `U_t` is the module flow used in `WP-253` and

\[
w_t\in\mathcal U(\mathcal L(X))
\]

is a point-norm continuous unitary cocycle satisfying

\[
w_{s+t}=w_s\,\operatorname{Ad}(U_s)(w_t),
\tag{1}
\]

then

\[
\widetilde U_t=w_tU_t
\tag{2}
\]

is another strongly continuous `\gamma`-compatible module flow. Its induced dynamics on `\mathcal K(X)` is

\[
\widetilde\delta_t
=\operatorname{Ad}(w_t)\circ\delta_t,
\tag{3}
\]

which can contain arbitrary non-separable interaction between the compact/"archimedean" factor and the arithmetic coefficient algebra. Nevertheless,

\[
\boxed{
\beta\ne0
\Longrightarrow
(\mathcal K(X),\widetilde\delta)
\text{ has no nonzero proper }\beta\text{-KMS weight}.
}
\tag{4}
\]

Thus **non-product is not enough**. The surviving finite--archimedean coupling must leave the exterior-equivalence class of the same full coefficient module, alter the coefficient thermodynamics in a genuinely new way, or change the correspondence/algebraic category itself.

## 1. Cocycle perturbation still gives a compatible full module flow

Keep the full right Hilbert `\mathcal B`-module

\[
X=\mathcal H\otimes\mathcal B
\tag{5}
\]

and a strongly continuous compatible flow `U` satisfying

\[
U_t(xb)=U_t(x)\gamma_t(b),
\qquad
\langle U_tx,U_ty\rangle
=\gamma_t(\langle x,y\rangle).
\tag{6}
\]

Let `w` satisfy (1), with every `w_t` an adjointable right-`\mathcal B`-linear unitary. Then

\[
\widetilde U_s\widetilde U_t
=w_sU_sw_tU_t
=w_s\operatorname{Ad}(U_s)(w_t)U_{s+t}
=w_{s+t}U_{s+t}
=\widetilde U_{s+t}.
\tag{7}
\]

Because `w_t` is right-`\mathcal B`-linear,

\[
\widetilde U_t(xb)
=w_tU_t(x)\gamma_t(b)
=\widetilde U_t(x)\gamma_t(b),
\tag{8}
\]

and because it is unitary,

\[
\langle \widetilde U_tx,\widetilde U_ty\rangle
=\gamma_t(\langle x,y\rangle).
\tag{9}
\]

So the perturbation has not changed the coefficient dynamics or the right-module relation. It has only changed the compatible module implementation.

On generalized compacts,

\[
\widetilde\delta_t(T)
=\widetilde U_tT\widetilde U_t^*
=w_t\delta_t(T)w_t^*,
\tag{10}
\]

which is exactly the exterior/cocycle perturbation (3). The resulting flow need not factorize as a tensor product. The cocycle may have matrix coefficients containing noncommuting elements of `\mathcal B` and may mix the auxiliary Hilbert direction with arithmetic operators before equilibrium is taken.

## 2. KMS-weight induction kills the whole module-cocycle class

The Laca--Neshveyev/Combes--Zettl induction theorem used in `WP-253` is not restricted to product module dynamics. It applies to any strongly continuous compatible module flow on a full Hilbert module. Applying it to `\widetilde U` gives

\[
\left\{
\beta\text{-KMS weights on }(\mathcal B,\gamma)
\right\}
\longleftrightarrow
\left\{
\beta\text{-KMS weights on }
(\mathcal K(X),\widetilde\delta)
\right\}.
\tag{11}
\]

`WP-250` proves that the left-hand side contains no nonzero proper weight for every real `\beta\ne0`. Equation (11) therefore proves (4).

The important point is categorical. A cocycle can make the observable dynamics look strongly interacting and completely non-product while leaving the underlying equivariant Morita datum unchanged. KMS induction sees the latter. Consequently, local spectral mixing, prime-dependent interaction terms, or frequency cancellation inside `\mathcal K(X)` do not by themselves create a new equilibrium sector.

## 3. Bounded finite--archimedean Hamiltonians are a strict special case

Let

\[
K=K^*\in\mathcal L(X).
\tag{12}
\]

The usual Dyson/Araki construction gives a unitary cocycle `w^K_t` for the multiplier flow `\operatorname{Ad}(U_t)` and the perturbed compact-algebra generator

\[
D_K(T)=D(T)+i[K,T]
\tag{13}
\]

on the natural generator domain. Hence every bounded adjointable interaction lies inside (1)--(4).

This includes genuinely non-product finite--archimedean couplings. For example, finite sums of the form

\[
K=\sum_j k_j\otimes b_j,
\qquad
k_j\in\mathcal K(\mathcal H),
\quad
b_j\in\mathcal B,
\tag{14}
\]

with the sum made self-adjoint, can correlate auxiliary/archimedean modes with arithmetic crossed-product observables and need not reduce to `K_\infty\otimes1+1\otimes K_f`. They are nevertheless adjointable right-module operators, so their cocycles preserve (8)--(9) and cannot restore a nonzero-temperature proper KMS weight.

The theorem is actually broader than bounded perturbation. Boundedness is only a convenient sufficient condition for constructing the cocycle. Any possibly singular or unbounded candidate whose dynamics nevertheless integrates to a strongly continuous unitary cocycle in `\mathcal L(X)` satisfying (1) is still blocked by the same module argument. The true boundary is **module compatibility/exterior equivalence**, not bounded versus unbounded syntax.

## 4. Bounded perturbation of the coefficient flow also cannot create equilibrium

One might instead modify the coefficient dynamics itself before forming the module flow. The simplest possibility is a bounded local Araki perturbation. For

\[
V=V^*\in\mathcal B,
\]

let `\gamma^V` be generated by

\[
\partial_V=\partial+i[V,\,\cdot\,],
\tag{15}
\]

where `\partial` is the generator of `\gamma`.

Araki perturbation theory gives, for every fixed `\beta`, a bijection between the `\beta`-KMS states of `(\mathcal B,\gamma)` and those of `(\mathcal B,\gamma^V)`. Since `WP-250` shows that the former set is empty for `\beta\ne0`,

\[
\operatorname{KMS}_\beta(\mathcal B,\gamma^V)=\varnothing
\qquad(\beta\ne0).
\tag{16}
\]

Moreover `\mathcal B` is unital, and `WP-250` proves directly that every proper C*-weight on a unital C*-algebra is bounded and normalizable to a state. Therefore `(\mathcal B,\gamma^V)` also has no nonzero proper `\beta`-KMS C*-weight for `\beta\ne0`.

Combining this observation with the module-induction theorem gives a two-layer obstruction: a bounded inner change of the coefficient Hamiltonian cannot create equilibrium, and adding any compatible full-module finite--archimedean cocycle over that perturbed coefficient system cannot create it either.

This closes a materially larger family than the separable product clock of `WP-253`.

## 5. Aggressive falsification and matched controls

**Non-product interaction control.** Equation (14) can mix auxiliary matrix entries with arbitrary arithmetic elements of `\mathcal B`. The proof never diagonalizes `K`, never assumes tensor factorization, and never uses an invariant finite corner. Non-product spectral mixing alone is therefore not the missing relation.

**Prime-coded interaction control.** The coefficients `b_j` may be source-derived from prime labels, logarithmic energies, critical half-density data, or finite Bost--Connes observables. As long as they enter through a module cocycle over the same coefficient flow, the KMS-weight cone remains empty. Encoding more arithmetic in the interaction does not change the theorem.

**Continuous-spectrum control.** The auxiliary `U` may have continuous spectrum as in `WP-253`; the cocycle argument uses only module compatibility. There is no hidden return to the invariant-corner proof.

**Generalized-label control.** Replacing primes by arbitrary labels, randomizing local rotations, or changing the critical angles does not affect (7)--(11). This is appropriate for a negative classification result: exterior-equivalent module thermodynamics is too universal to select the Riemann sign.

**Coefficient-Hamiltonian control.** A bounded self-adjoint perturbation `V` of `\gamma` is allowed to be arithmetic and noncentral, but Araki's KMS-state bijection still preserves emptiness. The obstruction is therefore not merely that the auxiliary interaction was placed on the wrong tensor factor.

**What is not covered.** A flow that changes the right-module structure or is not exterior-equivalent through a `\mathcal B`-linear adjointable cocycle is outside (4). So is a new one-sided correspondence/range defect that changes coefficient thermodynamics, an outer or genuinely singular coefficient flow not related to `\gamma` by bounded Araki perturbation, or a represented von Neumann category carrying a normal semifinite weight whose finite domain is only weakly dense. Those are genuine category changes and remain live.

## 6. Prior-art and novelty audit

The operator-algebraic ingredients are classical.

François Combes and Heinrich Zettl, *Order Structures, Traces and Weights on Morita Equivalent C*-Algebras*, **Mathematische Annalen 265** (1983), 67--82, develops induction of weights, modular automorphism groups, and KMS weights under Morita equivalence.

Marcelo Laca and Sergey Neshveyev, *KMS states of quasi-free dynamics on Pimsner algebras*, **Journal of Functional Analysis 211** (2004), 457--482, DOI `10.1016/j.jfa.2003.08.008`, arXiv:`math/0304435`, develops the Hilbert-module KMS-weight induction used in (11). Its generality is precisely what makes replacing `U` by the cocycle-perturbed compatible flow `\widetilde U` immediate.

Huzihiro Araki, *Relative Hamiltonian for Faithful Normal States of a von Neumann Algebra*, **Publ. RIMS 9** (1973), 165--209, DOI `10.2977/prims/1195192744`, is the primary relative-Hamiltonian/modular source behind bounded perturbation theory. The standard C*-dynamical formulation gives a bijection between KMS states of a dynamics and its bounded self-adjoint local perturbation at fixed inverse temperature; see also Bratteli--Robinson, *Operator Algebras and Quantum Statistical Mechanics II*, §5.4.

No novelty is claimed for exterior equivalence, Araki perturbation, or KMS-Morita induction. The Mathia-specific content is the classification of the exact escape left open after `WP-253`: **a large family of genuinely non-product finite--archimedean interactions is still thermodynamically trivial for this search because it is exterior-equivalent over the same forbidden coefficient system.**

The novelty audit also prevents an overclaim. General unitary cocycles outside the module category, coefficient flows not related by bounded Araki perturbation, and new one-sided/von-Neumann objects are not ruled out. Calling all of those "cocycle perturbations" without preserving the precise module and continuity hypotheses would be false.

## 7. Consequence for the Weil-positivity mandate

The surviving route can no longer be described merely as

\[
\text{critical finite sector}
\to
\text{add a non-product finite--archimedean Hamiltonian}
\to
\text{KMS positivity}.
\tag{17}
\]

If the added interaction is an exterior perturbation inside the same full Hilbert-`\mathcal B` module, even an arithmetic and non-separable one, the KMS-weight cone is unchanged and remains empty at nonzero temperature. If the coefficient gauge flow itself is changed only by a bounded self-adjoint Araki perturbation, its KMS-state cone also remains empty, and unitality excludes proper KMS C*-weights.

A viable thermodynamic continuation must therefore introduce **non-Morita-trivial relational structure**: change the coefficient thermodynamics beyond bounded inner perturbation, change the correspondence/right-module relation (for example through a genuine one-sided range defect), change the boundary algebra, or pass to a different von Neumann/modular object with a canonical semifinite weight and finite quadratic-form domain.

Even that would reopen only the equilibrium gate. The resulting object would still have to derive the Mangoldt prime-power term, the archimedean Gamma contribution, the polar counterterms, and the completed Weil orientation from one source-forced positive structure. `WP-254` supplies no such structure; it removes another broad but ultimately exterior-equivalent family from the search.