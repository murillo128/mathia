# WP-252 — Equivariant stabilization cannot create the missing KMS weight

**Status:** `EXACT-DERIVED + STANDARD-HILBERT-MODULE + EQUIVARIANT-MORITA + KMS-WEIGHT-CORRESPONDENCE + NONUNITAL-STABILIZATION-NO-GO + MATCHED-CONTROLS + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-250` proves that the canonical dual gauge system

\[
(\mathcal B,\gamma),
\qquad
\mathcal B=\mathcal A\rtimes_\alpha\mathbb Z,
\]

has no nonzero proper `β`-KMS C*-weight for any `β\ne0`. Because that obstruction used unitality, `WP-250` left stabilization/nonunital categories as an explicit escape. The most immediate version of that escape is ordinary equivariant stabilization,

\[
\mathcal C=\mathcal K(\ell^2)\otimes\mathcal B,
\qquad
\delta_t=\operatorname{id}_{\mathcal K}\otimes\gamma_t.
\tag{1}
\]

That escape is not genuine. The standard Hilbert-module induction theorem for KMS weights gives a bijection between the `β`-KMS weights of `(\mathcal B,\gamma)` and those of `(\mathcal C,\delta)`. Therefore

\[
\boxed{
\beta\ne0
\quad\Longrightarrow\quad
(\mathcal K\otimes\mathcal B,\operatorname{id}\otimes\gamma)
\text{ has no nonzero proper }\beta\text{-KMS weight}.
}
\tag{2}
\]

Thus merely making the algebra nonunital by stabilization cannot restore the equilibrium object missing in `WP-250`. The surviving category-change escape is narrower: it must alter the equivariant Morita class or the dynamics, not just tensor the same system with compact operators.

## 1. The stabilized system is the compact-operator algebra of a full equivariant module

Let

\[
X=\ell^2(\mathbb N)\otimes\mathcal B
\tag{3}
\]

be the standard countably generated right Hilbert `\mathcal B`-module, with

\[
\langle (b_j),(c_j)\rangle
=\sum_j b_j^*c_j.
\tag{4}
\]

It is full because the closed span of its inner products is all of `\mathcal B`. Define a one-parameter group of module isometries by applying the gauge flow coordinatewise,

\[
U_t((b_j))=(\gamma_t(b_j)).
\tag{5}
\]

Then

\[
U_t(\xi b)=U_t(\xi)\gamma_t(b),
\qquad
\langle U_t\xi,U_t\eta\rangle
=\gamma_t(\langle\xi,\eta\rangle).
\tag{6}
\]

The generalized compact operators on the standard module satisfy

\[
\mathcal K(X)\cong
\mathcal K(\ell^2)\otimes\mathcal B.
\tag{7}
\]

Under this identification, the dynamics induced by `U_t`,

\[
\widetilde\gamma_t(T)=U_tTU_{-t},
\tag{8}
\]

is exactly

\[
\widetilde\gamma_t
=\operatorname{id}_{\mathcal K}\otimes\gamma_t.
\tag{9}
\]

So (1) is not merely analogous to the original system: it is the standard full equivariant-Morita stabilization of it.

## 2. KMS weights are preserved by this full-module equivalence

Laca--Neshveyev's KMS-weight induction theorem gives the exact tool needed here. For a full right Hilbert `A`-module `X` equipped with a compatible one-parameter isometry group `U`, their Theorem 3.2(iv) states that induction defines a one-to-one correspondence

\[
\{(\sigma,\beta)\text{-KMS weights on }A\}
\longleftrightarrow
\{(\operatorname{Ad}U,\beta)\text{-KMS weights on }\mathcal K(X)\}.
\tag{10}
\]

Their KMS weights are lower-semicontinuous and densely defined C*-weights, exactly the nonunital class relevant to the escape left open by `WP-250`.

Apply (10) with

\[
A=\mathcal B,
\qquad
\sigma=\gamma,
\qquad
X=\ell^2\otimes\mathcal B,
\qquad
\operatorname{Ad}U=\operatorname{id}_{\mathcal K}\otimes\gamma.
\tag{11}
\]

If a nonzero `β`-KMS weight `\Phi` existed on the stabilized algebra for `β\ne0`, the inverse Morita induction map would produce a nonzero `β`-KMS weight `\phi` on `(\mathcal B,\gamma)`. But `WP-250` proves that no such weight exists on the unital crossed product: every proper C*-weight there is bounded and normalizes to a KMS state, while the analytic gauge eigenunitary forces `1=e^{-\beta}`.

Hence the KMS cone on the stabilization is empty at every nonzero inverse temperature, proving (2).

This argument is preferable to naively restricting an arbitrary stabilized weight to one chosen rank-one corner. Such a restriction can raise domain questions if finiteness on that particular projection has not been established. Full Hilbert-module induction avoids that gap and gives a genuine bijection of the entire KMS-weight cones.

## 3. Full invariant corners expose the same reason geometrically

There is nevertheless a useful geometric picture behind the module theorem. For a rank-one projection `p\in\mathcal K(\ell^2)`,

\[
e=p\otimes1_{\mathcal B}
\tag{12}
\]

is invariant under (1), is full in `\mathcal C`, and has corner

\[
e\mathcal C e\cong\mathcal B.
\tag{13}
\]

The restricted dynamics on this corner is exactly `\gamma`. Thus ordinary stabilization has not created a new thermodynamic boundary; it has placed the original forbidden system inside a full invariant corner of an equivariantly Morita-equivalent algebra.

The same observation indicates the precise extension that is safe. If a product compact-factor dynamics

\[
\delta_t=\eta_t\otimes\gamma_t
\tag{14}
\]

admits an `\eta`-invariant rank-one projection `p`, then (12)--(13) again give a full invariant copy of `(\mathcal B,\gamma)`. Standard equivariant Morita/full-corner KMS induction therefore cannot turn such a product-clock stabilization into the missing finite-temperature equilibrium mechanism either.

The claim does **not** cover every conceivable nonunital enlargement. A compact-factor flow with no invariant finite full corner, a continuous-spectrum boundary algebra, a non-product coupling, or a represented von Neumann completion can leave this exact Morita class. Those remain category changes that require separate analysis.

## 4. Matched controls show that stabilization contributes no arithmetic selection

**Automorphism control.** Nothing in the stabilization theorem uses the prime origin of `\alpha`. If `(D,\rho)` is any C*-dynamical system with no nonzero `β`-KMS weight, then its standard equivariant stabilization `(\mathcal K\otimes D,\operatorname{id}\otimes\rho)` has none either. The no-go is Morita-theoretic, not Riemann-specific.

**Subcritical control.** Replacing the critical local prime rotations by a square-summable/subcritical family changes the representation issue of `WP-248` but does not alter the stabilization correspondence. Stabilization itself therefore cannot identify the Weil half-density boundary.

**Random/nonarithmetic control.** Arbitrary label rotations or a nonarithmetic product automorphism produce the same standard-module correspondence. Tensoring with compacts supplies no Mangoldt support, no prime energies, and no source-selection principle.

**Finite-support control.** With finitely many nontrivial prime factors the same equivalence holds. No thermodynamic event occurs when the support becomes infinite or critical merely because compact operators are added.

These controls are exactly what a negative classification result should show: ordinary stabilization can change unitality and permit unbounded weights in principle, but it does not create KMS weights that were absent before because the two systems carry equivalent equilibrium-weight data.

## 5. Consequence for the Weil-positivity search

`WP-250` left several formally possible routes after excluding proper nonzero-temperature KMS weights on the unital bilateral crossed product. `WP-252` removes the cheapest one:

\[
\boxed{
(\mathcal B,\gamma)
\xrightarrow{\ \otimes\mathcal K\ }
(\mathcal K\otimes\mathcal B,\operatorname{id}\otimes\gamma)
\quad\text{does not enlarge the KMS-weight cone.}
}
\tag{15}
\]

This matters because a successful escape cannot now appeal merely to the fact that nonunital C*-algebras may carry genuinely unbounded proper weights. The new nonunital object must contain **new equivariant structure** rather than a Morita-equivalent stabilization of the old gauge system.

In particular, a surviving route must do at least one of the following before positivity can become relevant: derive a different arithmetic/modular flow, introduce a one-sided source-defined semigroup with nontrivial range defects, use a boundary sector whose dynamics is not reducible through an invariant full corner to `\gamma`, or pass to a genuinely different von Neumann/modular completion. `WP-251` already shows that the minimal one-isometry Toeplitz repair restores equilibrium only by thermalizing the critical deformation into a universal tracial/Fock sector. `WP-252` now shows that ordinary stabilization does even less: it cannot restore equilibrium at all.

None of these operator-algebraic category changes by itself supplies the actual target of this research line. A Weil bridge still has to derive from one intrinsic geometric object the finite prime-power/Mangoldt term, the archimedean Gamma and polar completion, and an independently proved positive quadratic form with the correct orientation.

## 6. Prior-art and novelty audit

The induction theorem used here is classical prior art, not a new operator-algebra theorem. François Combes and Heinrich Zettl, *Order Structures, Traces and Weights on Morita Equivalent C*-Algebras*, **Mathematische Annalen 265** (1983), 67--82, developed induction of weights, modular automorphism groups, and KMS weights under Morita equivalence. EuDML record: `https://eudml.org/doc/163810`.

Marcelo Laca and Sergey Neshveyev, *KMS states of quasi-free dynamics on Pimsner algebras*, **Journal of Functional Analysis 211** (2004), 457--482, arXiv:`math/0304435`, DOI `10.1016/j.jfa.2003.08.008`, give the C*-module formulation used above. Their Section 3 explicitly constructs induced KMS weights, and Theorem 3.2(iv) states the one-to-one correspondence of KMS weights for a full module and its compact-operator algebra.

The Mathia-specific contribution is only the application of that classical theorem to the precise `WP-249`/`WP-250` crossed-product escape. It establishes that **ordinary equivariant stabilization cannot be the missing KMS/modular positivity source**. The novelty claim is this decisive narrowing of the search space, not Morita invariance itself.

## 7. Provenance and falsification boundary

This finding depends on the exact `WP-250` no-go and on the standard full-module KMS correspondence. It should be withdrawn or narrowed if either (i) the dynamics on the proposed stabilized object is not equivariantly Morita-related to `\gamma`, or (ii) a claimed weight lies in a category not covered by lower-semicontinuous densely defined C*-KMS weights.

Accordingly, this finding does not reject von Neumann KMS weights, continuous-spectrum boundary completions, non-product modular couplings, or arithmetic semigroup/endomotive constructions. It rejects only the hypothesis that **stabilization itself** repairs the missing equilibrium structure while leaving the original gauge dynamics unchanged up to equivariant Morita equivalence.