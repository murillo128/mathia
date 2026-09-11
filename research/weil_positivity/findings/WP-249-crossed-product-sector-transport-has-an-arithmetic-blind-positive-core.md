# WP-249 — Crossed-product sector transport has an arithmetic-blind positive core

**Status:** `EXACT-DERIVED + CROSSED-PRODUCT-CORE + LOCAL-SUPPORT-THEOREM + CONDITIONAL-EXPECTATION + POSITIVE-SQUARE + MATCHED-CONTROLS + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-248` leaves crossed-product enlargement as one explicit way to make the critical product automorphism algebraically implementable after it becomes nonspatial in the spherical quasi-local representation. The immediate hope is that adjoining the implementing unitary might itself create a new canonical positive form coupling the spherical and critical sectors.

For the bare crossed product, that hope fails for a precise reason. The implementing unitary contributes a universal shift geometry whose elementary positive forms do not know the prime weights, while every positive square built from finitely supported quasi-local coefficients remains supported on the same finite set of primes after applying the canonical conditional expectation. Thus adjoining the sector-transport generator removes the *algebraic* obstruction to writing the automorphism as conjugation, but it does not manufacture the all-prime finite-place distribution, the archimedean completion, or the Weil sign theorem.

This is deliberately not a no-go for Bost--Connes systems, KMS weights, Hilbert-module correspondences, non-quasi-local boundary states, or noncommutative geometry in general. It kills only the most direct continuation of `WP-248`: **cross the quasi-local prime algebra by the critical product automorphism and take positivity from the canonical implementing-unitary/Fourier core itself**.

## 1. Exact object and representation boundary

Use the quasi-local algebra from `WP-248`,

\[
\mathcal A
=\overline{\bigcup_{F\Subset\mathbb P}\mathcal A_F},
\qquad
\mathcal A_F=\bigotimes_{p\in F}\mathcal B(K_p),
\tag{1}
\]

and let

\[
\alpha=\bigotimes_p\alpha_p
\tag{2}
\]

be the product automorphism induced by the local rotations carrying the spherical local lines toward the critical product data. Because every quasi-local observable has finite support, `alpha` is a well-defined C*-automorphism even at the critical scale where `WP-248` proves that it is nonspatial in the spherical product representation.

Form the crossed product

\[
\mathcal B=\mathcal A\rtimes_\alpha\mathbb Z.
\tag{3}
\]

Since `Z` is amenable, there is no full/reduced ambiguity relevant here. Let `u` be the canonical implementing unitary, with convention

\[
uau^*=\alpha(a),\qquad a\in\mathcal A.
\tag{4}
\]

Equation (4) is the exact mechanism under test. No KMS state, modular Hamiltonian, extra boundary algebra, archimedean factor, or target-selected functional calculus is added.

The representation audit is important. At the critical tail, `u` should **not** be interpreted as a unitary recovered inside the spherical GNS representation: `WP-248` rules out such a spatial implementer there. The crossed product instead adjoins a new abstract generator in a larger algebra. This legitimately changes category, but that category change must itself supply new arithmetic structure if it is to help Weil positivity.

## 2. The canonical shift energy is positive but arithmetic-blind

The most primitive positive form supplied by the new generator is

\[
(1-u)^*(1-u)=2-u-u^*\succeq0.
\tag{5}
\]

Its algebraic expression is independent of the local prime rotations defining `alpha`. Replacing `alpha` by any other automorphism of `A` still gives the same positive Laurent polynomial in the implementing unitary. In the regular covariant representation this is the ordinary discrete shift Laplacian in the `Z` direction.

Therefore (5) cannot by itself distinguish the critical amplitudes `p^{-1/2}`, the Mangoldt amplitudes `(log p)/sqrt(p)`, a generalized-prime control, or even an automorphism unrelated to arithmetic. Any arithmetic dependence must enter through coefficient observables or through additional state/weight/domain data. The crossed-product shift is a transport coordinate, not a source-forced Weil kernel.

This matched control matters because it prevents the category enlargement itself from being counted as new arithmetic positivity. A positive operator that survives unchanged after the arithmetic automorphism is replaced is not the missing finite-prime sign mechanism.

## 3. Commutator squares with local observables remain local

The first mixed positive object is also exact. From (4),

\[
ua=\alpha(a)u,
\qquad
[u,a]=(\alpha(a)-a)u.
\tag{6}
\]

Write `d_a=alpha(a)-a`. Then

\[
[u,a]^*[u,a]
=u^*d_a^*d_a u
=\alpha^{-1}(d_a^*d_a)
\succeq0.
\tag{7}
\]

Now let `a` have support in a finite set of primes `S`, so `a in A_S`. The product automorphism preserves every finite local algebra,

\[
\alpha(\mathcal A_S)=\mathcal A_S.
\tag{8}
\]

Hence

\[
\boxed{
[u,a]^*[u,a]\in\mathcal A_S.
}
\tag{9}
\]

Thus the canonical commutator energy does not spread one local observable into an all-prime object. It remains a positive observable on exactly the finite prime subsystem from which it started.

This is not a statement that `alpha-id` is nonclosable or unbounded. On the contrary, as a map on the C*-algebra,

\[
\|\alpha(a)-a\|\le2\|a\|.
\tag{10}
\]

The obstruction is support and arithmetic content, not operator-domain pathology.

## 4. The entire finite Fourier positive core has the same support obstruction

The local result extends from one commutator to the canonical dense Fourier *-algebra. Let

\[
x=\sum_{n=-N}^{N}a_nu^n,
\qquad a_n\in\mathcal A_S
\tag{11}
\]

for one finite prime set `S`. Let

\[
E:\mathcal B\to\mathcal A
\tag{12}
\]

be the canonical conditional expectation extracting Fourier degree zero. Expanding `x^*x`, all unequal Fourier degrees vanish under `E`, while the diagonal terms give

\[
\boxed{
E(x^*x)
=\sum_{n=-N}^{N}\alpha^{-n}(a_n^*a_n)
\in\mathcal A_S,
\qquad E(x^*x)\succeq0.
}
\tag{13}
\]

Equation (13) is the useful no-go statement. The standard source of scalar positivity on the finite crossed-product core factors through a sum of positive local terms and preserves the finite prime support of the coefficient data. If `omega` is any product/reference state on `A`, then

\[
(\omega\circ E)(x^*x)
=\sum_n\omega\!\left(\alpha^{-n}(a_n^*a_n)\right)
\ge0
\tag{14}
\]

depends only on the chosen finite subsystem and whatever local arithmetic was already put into the `a_n` and `alpha_p` there.

Consequently, the finite Fourier core cannot *generate* the all-prime prime-power distribution required by the finite part of the Weil explicit formula from a local probe. Still less does it produce the Gamma factor or the polar/global counterterms: those objects are absent from (1)--(4).

The scope is exact. General elements of the C*-completion need not have finite prime support, and non-quasi-local states, weights, correspondences, cycles, or unbounded multipliers may carry genuinely global information. Equation (13) does not rule them out. It shows that such information would be **additional structure**, not a hidden consequence of adjoining `u` and taking canonical positive squares.

## 5. Aggressive falsification and matched controls

**Automorphism control.** Replace the critical prime rotation by any other product automorphism preserving the local tensor factors. The pure shift energy (5) is unchanged, and the support theorem (13) still holds. The positivity mechanism is therefore generic crossed-product geometry, not Riemann-specific geometry.

**Finite-support control.** If the deformation is nontrivial at only finitely many primes, `alpha` is spatial in the obvious finite tensor representation, but (5)--(14) are unchanged. The same positive core exists on both sides of the critical representation transition. Hence its positivity does not detect the half-density boundary isolated by `WP-247`--`WP-248`.

**Subcritical control.** When the product deformation is square-summable and the spherical and deformed product states are quasi-equivalent, the crossed product can still be formed and has exactly the same Fourier-core identities. Crossing by `Z` therefore does not convert critical disjointness into a new sign theorem; it merely provides a uniform algebraic language for transport in both regimes.

**Arithmetic-insertion control.** One may choose the local rotations `alpha_p` using `p^{-1/2}` or `(log p)/sqrt(p)`. Then mixed expressions can of course contain those numbers. But they have entered through the definition of `alpha`; the bare crossed-product positivity has not derived them. A successful route must explain why the source geometry forces the critical coefficients and why the resulting *global* form has the Weil orientation independently of the target.

**Nonlocal-coefficient escape.** A quasi-local element may be a norm limit of observables with growing support, so this finding does not assert that every element of `A` is finitely supported. The decisive distinction is that the canonical crossed-product operations in (5)--(13) do not supply the missing global tail or its renormalization. If a specially chosen nonlocal coefficient is used, its existence, convergence, normalization, and arithmetic selection become separate obligations and must pass the same target-programmability controls as other inserted kernels.

## 6. Prior-art and novelty audit

The operator-algebra ingredients are classical, not novel. For a discrete-group crossed product, the canonical conditional expectation extracts the identity Fourier coefficient; for `Z`-crossed products the canonical implementing unitary and the covariance relation (4) are standard. See, for example, Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, AMS (2007), and the explicit `A rtimes_alpha Z`/canonical-expectation setup in Del Vecchio--Fidaleo--Rossi, *Skew-product dynamical systems for crossed product C*-algebras and their ergodic properties*, arXiv:2105.00197.

Arithmetic crossed products and quantum-statistical systems are also established prior art. Arledge--Laca--Raeburn, *Semigroup crossed products and Hecke algebras arising from number fields*, Documenta Math. 2 (1997), 115--138, DOI `10.4171/DM/25`, realizes number-field Hecke algebras as semigroup crossed products. Bost--Connes-type C*-dynamical systems, their zeta partition functions, KMS states, phase transitions, and arithmetic correspondences form a substantial existing literature; see also Cohen, *A C*-dynamical system with Dedekind zeta partition function and spontaneous symmetry breaking*, J. Théorie des Nombres de Bordeaux 11 (1999), 15--30, and Laca--Neshveyev--Trifković, *Bost--Connes systems, Hecke algebras, and induction*, J. Noncommut. Geom. 7 (2013), 525--546, DOI `10.4171/JNCG/125`.

Therefore neither "use a crossed product" nor "obtain positivity from a canonical conditional expectation" can count as Mathia novelty. The substantive point here is narrower and Mathia-specific: **the exact sector-change escape produced by `WP-248` is not repaired by the bare crossed-product positive core**. The new generator algebraically implements the product automorphism, but its universal shift positivity is arithmetic-blind and its finite Fourier positive squares remain finite-prime local after the canonical expectation.

A bounded search across crossed-product C*-algebras, product automorphisms, conditional expectations, Bost--Connes/Hecke systems, KMS states, Weil/Riemann positivity, and the critical all-prime product-state boundary did not locate this exact negative application. That absence is not a completeness claim. The theorem used is elementary crossed-product algebra; the research contribution is the falsification of the immediate `WP-248` escape in the current Mathia construction.

## 7. Consequence for Weil Positivity

`WP-248` established that the critical all-prime product deformation is genuinely outside the spherical quasi-local representation. `WP-249` shows that the most obvious category enlargement does not yet provide the missing geometry:

\[
\boxed{
\text{critical nonspatial }\alpha
\ \xrightarrow{\;\mathcal A\rtimes_\alpha\mathbb Z\;}\
\text{algebraically implemented transport}
\not\Rightarrow
\text{new arithmetic/global positivity}.
}
\tag{15}
\]

The surviving route is therefore narrower. A crossed-product continuation must add something that is not already contained in the universal transport core: for example a **source-forced** KMS/modular weight, a non-quasi-local boundary state, a Hilbert-C*-module correspondence, an infinite-rank finite--archimedean coupling, or an unbounded cycle with a proved domain/closability theorem. Whatever object is chosen must intrinsically generate the finite-prime coefficients **and** the Gamma/polar terms, and its nonnegativity must follow from an independent theorem rather than from a target-selected coefficient, state, quotient, or regularization.

This is compatible with the existing Bost--Connes clue rather than a replacement for it. `WP-215`--`WP-222` already show that arithmetic C*-dynamics can source nontrivial critical finite-prime data while leaving the Weil orientation unsupported. `WP-249` adds a different control: **sector transport itself is not that missing orientation mechanism**. If a future noncommutative-geometric route succeeds, the mathematical work must occur in the additional global state/weight/correspondence or finite--archimedean coupling, not in the mere fact that an outer critical automorphism has been made inner in a crossed-product enlargement.
