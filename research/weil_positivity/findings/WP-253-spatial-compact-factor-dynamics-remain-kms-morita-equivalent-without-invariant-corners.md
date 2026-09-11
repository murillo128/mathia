# WP-253 — Spatial compact-factor dynamics remain KMS-Morita equivalent without invariant corners

**Status:** `EXACT-DERIVED + EQUIVARIANT-HILBERT-MODULE + KMS-WEIGHT-CORRESPONDENCE + CONTINUOUS-SPECTRUM-CONTROL + NO-INVARIANT-CORNER-ESCAPE + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-252` proves that ordinary equivariant stabilization

\[
(\mathcal K(\mathcal H)\otimes\mathcal B,\operatorname{id}\otimes\gamma)
\]

cannot create the nonzero-temperature KMS weight missing from the canonical crossed-product gauge system `(\mathcal B,\gamma)` of `WP-250`. It also notes a useful full-corner argument when a compact-factor flow has an invariant rank-one projection, while leaving compact-factor dynamics with no invariant finite corner as a category change requiring separate analysis.

For **spatial product dynamics on the compact factor**, the absence of an invariant rank-one corner is not an escape. Let

\[
V:\mathbb R\to U(\mathcal H)
\]

be any strongly continuous one-parameter unitary group, with no assumption that `V` has eigenvectors, and define

\[
\delta_t
=\operatorname{Ad}(V_t)\otimes\gamma_t
\quad\text{on}\quad
\mathcal C=\mathcal K(\mathcal H)\otimes\mathcal B.
\tag{1}
\]

Then `(\mathcal C,\delta)` is still the generalized-compact algebra of a **full equivariant Hilbert `\mathcal B`-module**. The standard KMS-weight induction theorem therefore gives a bijection between the `\beta`-KMS weights of `(\mathcal B,\gamma)` and those of `(\mathcal C,\delta)`. Since `WP-250` excludes every nonzero proper `\beta`-KMS weight on `(\mathcal B,\gamma)` for `\beta\ne0`,

\[
\boxed{
\beta\ne0
\Longrightarrow
(\mathcal K(\mathcal H)\otimes\mathcal B,
\operatorname{Ad}(V)\otimes\gamma)
\text{ has no nonzero proper }\beta\text{-KMS weight}.
}
\tag{2}
\]

This remains true when `V` has purely continuous spectrum and there is **no invariant rank-one projection at all**. Thus changing the compact stabilization from a trivial clock to an arbitrary spatial Hamiltonian clock does not leave the relevant equivariant Morita class and cannot restore the missing equilibrium object.

## 1. The product flow is induced by a full equivariant module

Let

\[
X=\mathcal H\otimes\mathcal B
\tag{3}
\]

be the standard right Hilbert `\mathcal B`-module, with

\[
(\xi\otimes b)c=\xi\otimes bc,
\qquad
\langle \xi\otimes b,\eta\otimes c\rangle
=\langle\xi,\eta\rangle_{\mathcal H}\,b^*c.
\tag{4}
\]

It is full because the closed linear span of its inner products is all of `\mathcal B`. Define

\[
U_t(\xi\otimes b)
=V_t\xi\otimes\gamma_t(b).
\tag{5}
\]

Then

\[
U_t(xb)=U_t(x)\gamma_t(b),
\qquad
\langle U_tx,U_ty\rangle
=\gamma_t(\langle x,y\rangle).
\tag{6}
\]

Thus `U` is exactly the kind of strongly continuous compatible module dynamics used in the standard KMS-weight induction theory.

The generalized compact operators satisfy

\[
\mathcal K(X)\cong\mathcal K(\mathcal H)\otimes\mathcal B.
\tag{7}
\]

For rank-one module operators,

\[
\theta_{\xi\otimes b,\eta\otimes c}
\longleftrightarrow
|\xi\rangle\langle\eta|\otimes bc^*.
\tag{8}
\]

Conjugating by `U_t` gives

\[
U_t\theta_{x,y}U_{-t}
=\theta_{U_tx,U_ty},
\tag{9}
\]

which under (8) is precisely

\[
\operatorname{Ad}(V_t)\otimes\gamma_t.
\tag{10}
\]

Therefore (1) is not merely a tensor product carrying two unrelated clocks. It is the compact-operator algebra of a full equivariant module over the original forbidden coefficient system `(\mathcal B,\gamma)`.

## 2. KMS weights are unchanged by the spatial compact clock

Laca--Neshveyev's Hilbert-module induction theorem for KMS weights applies to a full right Hilbert C*-module equipped with a compatible one-parameter group of module isometries. In the notation above it yields a one-to-one correspondence

\[
\left\{
\beta\text{-KMS weights on }(\mathcal B,\gamma)
\right\}
\longleftrightarrow
\left\{
\beta\text{-KMS weights on }
(\mathcal K(X),\operatorname{Ad}U)
\right\}.
\tag{11}
\]

Using (7)--(10), the right-hand side is exactly the KMS-weight cone of `(\mathcal C,\delta)`. No invariant finite-dimensional subspace of `V` is needed for the correspondence.

Now apply `WP-250`: for every real `\beta\ne0`, `(\mathcal B,\gamma)` has no nonzero proper C*-KMS weight. Equation (11) therefore proves (2).

This also answers a tempting objection to `WP-252`. One might try to choose the compact-factor Hamiltonian so that some of its Bohr frequencies cancel the gauge frequency of the implementing unitary `u`, creating zero-frequency tensors and apparently evading the eigenunitary argument. Such cancellations can occur at the level of individual analytic matrix coefficients when `V` has point spectrum. They do **not** create a KMS weight, because the full KMS cone is transported bijectively through the module equivalence. Local frequency cancellation is therefore weaker than equilibrium existence.

## 3. Continuous spectrum shows that invariant corners were never essential

Take

\[
\mathcal H=L^2(\mathbb R),
\qquad
(V_t f)(x)=e^{itx}f(x).
\tag{12}
\]

The self-adjoint generator is multiplication by `x` and has purely continuous spectrum. There is no nonzero vector `f\in L^2(\mathbb R)` satisfying

\[
V_tf=e^{it\lambda}f
\quad\text{for all }t,
\tag{13}
\]

because such a vector would have to be supported on the measure-zero singleton `{\lambda}`. Hence the compact-factor action has no invariant rank-one projection.

Nevertheless the module construction (3)--(10) is unchanged, so (11) still gives the exact KMS-weight correspondence and (2) still holds. This is the decisive matched control against the idea that removing invariant finite corners is enough to escape the stabilization obstruction:

\[
\boxed{
\text{no invariant rank-one corner}
\not\Rightarrow
\text{new KMS thermodynamics}.
}
\tag{14}
\]

What matters is the equivariant Morita class, not the existence of an easy finite corner proof.

## 4. Arithmetic compact clocks do not help while the coupling remains a product

The argument never uses the spectrum of `V`. Therefore one may choose a positive or unbounded generator with prime-dependent levels, logarithmic energies, critical half-density scales, or any other arithmetic-looking spectral pattern. As long as the enlarged dynamics remains exactly

\[
\operatorname{Ad}(V_t)\otimes\gamma_t
\tag{15}
\]

on `\mathcal K(\mathcal H)\otimes\mathcal B`, the same full module transports the KMS cone back to `(\mathcal B,\gamma)`.

Thus appending an auxiliary Hamiltonian with the desired prime energies is not enough. Even if its spectrum is source-derived rather than target-fitted, a **separable product clock on a compact stabilization cannot repair the equilibrium obstruction**. The new arithmetic data has to enter through a coupling that changes the equivariant module class, the coefficient dynamics, or the operator category itself.

This is stronger than the generalized-product controls used in many earlier findings: the auxiliary factor is allowed to contain arbitrary detailed spectral information. What it is not allowed to do is interact nontrivially with the `\mathcal B` coefficient system before the KMS structure is formed.

## 5. Aggressive falsification and exact boundary

Several apparent escapes fail inside the theorem's scope.

**Discrete spectral cancellation.** If `V` has eigenvalues whose differences cancel the gauge frequency, some tensors can become `\delta`-invariant. The module correspondence still forbids a nonzero `\beta`-KMS weight when `\beta\ne0`.

**Continuous-spectrum removal of corners.** Equation (12) removes invariant rank-one projections completely, but the KMS cone remains empty. The corner argument of `WP-252` was sufficient, not necessary.

**Infinite multiplicity.** Replacing `\mathcal H` by any larger Hilbert space or taking arbitrary spectral multiplicities changes neither fullness of `X` nor the correspondence.

**Arithmetic spectral engineering.** Prime-labelled eigenvalues or a source-derived Hamiltonian on `\mathcal H` still do not help while the enlarged flow factorizes as (15).

The theorem does **not** cover a genuinely non-product dynamics on `\mathcal K(\mathcal H)\otimes\mathcal B` that is not induced from a compatible module action over `(\mathcal B,\gamma)`. It also does not cover a boundary algebra not Morita equivalent to `\mathcal B`, a one-sided correspondence whose range defect changes the coefficient thermodynamics, or a represented von Neumann completion with a normal semifinite modular weight. Those remain legitimate category changes.

The practical boundary is now sharper than in `WP-252`: merely replacing the trivial compact clock by a spatial one—even one with continuous spectrum and no invariant finite corners—is **not** such a category change.

## 6. Prior-art and novelty audit

The functional-analytic theorem used here is classical. François Combes and Heinrich Zettl, *Order Structures, Traces and Weights on Morita Equivalent C*-Algebras*, **Mathematische Annalen 265** (1983), 67--82, develops induction of weights, modular automorphism groups, and KMS weights under Morita equivalence. The EuDML record explicitly classifies KMS weights and modular automorphism groups among the paper's subjects: `https://eudml.org/doc/163810`.

Marcelo Laca and Sergey Neshveyev, *KMS states of quasi-free dynamics on Pimsner algebras*, **Journal of Functional Analysis 211** (2004), 457--482, arXiv:`math/0304435`, DOI `10.1016/j.jfa.2003.08.008`, gives the C*-module formulation. Their setup allows a nontrivial coefficient flow together with a compatible strongly continuous module isometry group, and Section 3 develops induction of KMS weights. This is exactly the level of generality used in (3)--(11); the compact-factor unitary group is absorbed into the module dynamics rather than treated by an invariant-corner argument.

Accordingly, no novelty is claimed for (11), for equivariant Morita invariance, or for the continuous-spectrum example. The Mathia-specific result is the application to the precise escape left after `WP-250`--`WP-252`: **a spatial compact-factor clock, including one with no invariant rank-one projections, cannot be the missing modular/KMS source for Weil positivity.**

A bounded literature audit across equivariant Morita equivalence, Hilbert-module KMS induction, compact-operator dynamics, and Pimsner thermodynamics found the mechanism to be standard operator-algebra theory rather than an unrecognized positivity theorem. That is a useful negative result here because it prevents ordinary stabilization with a more elaborate auxiliary Hamiltonian from being mistaken for new arithmetic geometry.

## 7. Consequence for the Weil-positivity mandate

The surviving critical-sector route can no longer be described as

\[
\text{crossed product}
\to
\text{nonunital stabilization}
\to
\text{choose a better compact Hamiltonian}
\to
\text{KMS positivity}.
\tag{16}
\]

Every spatial product version of the last two steps remains equivariantly Morita equivalent to the original gauge system and therefore inherits its empty nonzero-temperature proper KMS cone.

A viable continuation must instead introduce **new relational structure before equilibrium is taken**: a source-forced non-product finite--archimedean coupling, a one-sided semigroup/range-defect construction whose coefficient state is not the tracial collapse of `WP-251`, a boundary algebra outside the compact stabilization Morita class, or a genuinely different von Neumann/modular object with a canonical finite quadratic-form domain.

Even such a category change would only reopen the thermodynamic gate. It would still have to derive the finite prime-power/Mangoldt term, the Gamma and polar completion, and a global positive quadratic form with the correct Weil orientation from one intrinsic object. `WP-253` does not supply that object; it removes one more apparently flexible but actually Morita-trivial family from the search.