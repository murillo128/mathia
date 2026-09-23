---
id: WP-413
title: Equal-scale central-twist factorization paths collapse to abelian phase Grams
branch: weil_positivity
status: supported
kind: central-twist-balanced-path-gram-obstruction
claim_strength: exact RH-independent obstruction for the scale-balanced central-twist survivor left by WP-410 and WP-412; every finite family of twisted Bost--Connes integer-scale factorization paths with the same total scale differs only by diagonal unitary coefficients in C(Zhat), so every state Gram is an ordinary commutative phase-correlation Gram, while scale-only scalar multipliers make that Gram rank one and its positivity spectrum completely blind to mixed-prime commutator phase
created: 2026-09-23
related: [WP-300, WP-407, WP-408, WP-409, WP-410, WP-412]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - A. Buss and R. Exel, Fell bundles over inverse semigroups and twisted etale groupoids, J. Operator Theory 67 (2012), 153-205
  - Z. Afsar and A. Sims, KMS states on the C*-algebras of Fell bundles over groupoids, Math. Proc. Camb. Philos. Soc. 170 (2021), 221-246, DOI 10.1017/S0305004119000379
  - A. Kleppner, Multipliers on Abelian Groups, Math. Ann. 158 (1965), 11-34
---

# WP-413 — Equal-scale central-twist factorization paths collapse to abelian phase Grams

## Claim

`WP-410` leaves central Bost--Connes twists visible only before the range-projection readout, and `WP-412` shows that KMS scalarization kills every scale-unbalanced observable while leaving scale-balanced cycles alive. The most direct surviving construction is therefore to compare several ordered multiplicative paths with the same total scale and form their positive Gram matrix.

For central circle twists of the same Bost--Connes groupoid, that route has an exact collapse.

Let `S_n` be the unit-norm twisted bisection isometries of `WP-410`, supported on the integer-scale bisections `B_n`, so

\[
S_n^*S_n=1,
\qquad
S_nS_n^*=E_n=1_{n\widehat{\mathbf Z}}.
\tag{1}
\]

For an ordered factorization path

\[
a=(n_1,\ldots,n_r),
\qquad
N(a):=n_1\cdots n_r,
\]

define

\[
X_a:=S_{n_1}\cdots S_{n_r}.
\tag{2}
\]

Fix any finite family of paths `a` with the same total scale `N(a)=N`. Then every `X_a` is an isometry supported on the same bisection `B_N` and has the same range projection `E_N`. Choosing one reference path `a_0`, there are unitaries

\[
d_a:=X_{a_0}^*X_a\in D:=C(\widehat{\mathbf Z})
\tag{3}
\]

such that

\[
\boxed{X_a=X_{a_0}d_a,\qquad X_a^*X_b=d_a^*d_b.}
\tag{4}
\]

Consequently, for **every state** `phi` on the twisted algebra, the path Gram is

\[
\boxed{
G_{ab}:=\phi(X_a^*X_b)
      =\phi(d_a^*d_b)
      =\int_{\widehat{\mathbf Z}}\overline{d_a(\rho)}d_b(\rho)\,d\nu_\phi(\rho),
}
\tag{5}
\]

where `nu_phi` is the probability measure representing the restriction `phi|_D`. Thus every equal-scale central-twist path Gram factors through an **ordinary commutative phase-correlation space**. Its positivity is the tautological `L^2(nu_phi)` Gram positivity of unit-modulus functions; it is not a new arithmetic sign constraint.

The scale-only projective subclass is even more rigid. If the twist is pulled back from a scalar multiplier on the multiplicative scale group, every `d_a` is a constant phase. Hence for `k` paths

\[
\boxed{G=zz^*,\qquad \operatorname{rank}G=1,\qquad
\operatorname{spec}(G)=\{k,0,\ldots,0\}.}
\tag{6}
\]

For the two mixed-prime paths `(p,q)` and `(q,p)`, their projective commutator phase survives as the off-diagonal entry, but

\[
G=\begin{pmatrix}1&\beta(p,q)\\\overline{\beta(p,q)}&1\end{pmatrix},
\qquad
\det G=0,
\tag{7}
\]

for **every** `beta(p,q) in U(1)`. The balanced holonomy survives KMS frequency selection, but the positive Gram sign and spectrum cannot distinguish its value.

So the central-twist escape left by `WP-410` and `WP-412` is narrower than merely “use a balanced cycle”: equal-total-scale factorization-path Grams reduce to classical phase correlations, and scalar projective curvature is pure Gram gauge. A surviving Weil route must obtain arithmetic content from a source-forced nonconstant twist observable, a noncentral/operator-valued structure, a non-Gram functional, altered source/range geometry, active dynamics, or a genuinely coupled finite--archimedean construction. Universal Gram positivity alone cannot supply the missing Weil sign explanation.

**Classification:** `CLASSICAL-TWISTED-GROUPOID-BISECTION-CALCULUS + EXACT-DERIVED-BC-OBSTRUCTION + SCALE-BALANCED-SURVIVOR-ANALYZED + CENTRAL-U1-TWIST + COMMON-BISECTION-FACTORING + ABELIAN-PHASE-GRAM-COLLAPSE + SCALAR-MULTIPLIER-RANK-ONE + PROJECTIVE-HOLONOMY-SIGN-BLIND + KMS-COMPATIBLE + MATCHED-CONTROL-GENERIC + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Equal total scale means equal bisection support

The integer-scale bisections satisfy

\[
B_mB_n=B_{mn}.
\tag{8}
\]

This statement is about the underlying Bost--Connes groupoid and is unaffected by a central Fell-line twist. Twisted multiplication changes the fibre coefficient on a composable pair, not the composed arrow or its source and range.

Therefore the product (2) is supported on `B_{N(a)}`. Since each `S_n` is an isometry, so is every finite product `X_a`. Applying the same bisection-support calculation as in `WP-410` gives

\[
X_a^*X_a=1,
\qquad
X_aX_a^*=E_{N(a)}.
\tag{9}
\]

Hence all paths with product `N` have common initial projection `1` and common final projection `E_N`. This is stronger than merely saying that they have the same dynamical degree: they are alternative unit-norm lifts of the **same** groupoid bisection.

## 2. Relative path holonomy lands in the diagonal algebra

Fix a reference path `a_0` of total scale `N` and put `d_a=X_{a_0}^*X_a`. The support of this product is

\[
B_N^{-1}B_N=s(B_N)=\widehat{\mathbf Z},
\]

so `d_a` lies in the unit-space algebra

\[
D=C(\widehat{\mathbf Z}).
\tag{10}
\]

Moreover it is unitary. Indeed, using the common range projection,

\[
\begin{aligned}
d_a^*d_a
 &=X_a^*X_{a_0}X_{a_0}^*X_a
  =X_a^*E_NX_a
  =1,\\
d_ad_a^*
 &=X_{a_0}^*X_aX_a^*X_{a_0}
  =X_{a_0}^*E_NX_{a_0}
  =1.
\end{aligned}
\tag{11}
\]

The same identities give

\[
X_{a_0}d_a
=X_{a_0}X_{a_0}^*X_a
=E_NX_a
=X_a,
\]

and then (4) follows.

This argument does not trivialize the central twist globally. The functions `d_a` may be genuinely nonconstant and may encode base-dependent holonomy. It proves only that **relative holonomy among positive factorization paths with one fixed total scale is forced into the abelian unit-space algebra**.

## 3. Every state sees only a classical correlation Gram

Because `D` is commutative, the restriction of any state `phi` to `D` is integration against a probability measure `nu_phi` on `Z-hat`. Equation (4) therefore gives (5).

For arbitrary coefficients `c_a`,

\[
\sum_{a,b}\overline{c_a}G_{ab}c_b
=
\int\left|\sum_a c_a d_a(\rho)\right|^2d\nu_\phi(\rho)
\ge0.
\tag{12}
\]

The positive sign is therefore completely accounted for by ordinary Hilbert-space Gram positivity. No Bost--Connes arithmetic relation, prime distribution, Gamma factor, polar term, or Weil kernel is needed to prove it.

For two paths the only scalar invariant of the Gram beyond the unit diagonal is

\[
\det G
=1-|\phi(d)|^2,
\qquad d=d_a^*d_b\in D,
\tag{13}
\]

which is just the variance-type defect of averaging a unit-modulus function. A nonconstant base-dependent twist can make this determinant positive, so the finding does **not** say that all twisted path data vanish. It says that its positivity is generic commutative correlation positivity and therefore cannot by itself explain the arithmetic orientation required by the research mandate.

## 4. Scalar multipliers make the balanced Gram rank one

Now specialize to the projective scale twists of `WP-409`. A multiplier contributes only a scalar phase to each ordered product with a fixed total scale. Thus there are constants `z_a in U(1)` with

\[
X_a=z_aX_{a_0}
\]

after absorbing the reference phase. Equivalently, every `d_a` is constant.

Then

\[
G_{ab}=\overline{z_a}z_b,
\]

which proves (6). All principal minors of size at least two vanish and every nonzero eigenvalue is fixed by the number of paths, independent of the multiplier.

For two distinct primes the phase ratio is precisely the mixed-prime commutator bicharacter, up to the orientation convention for `beta`. Equation (7) shows the sharp distinction between **visibility** and **sign-bearing content**: the complex matrix entry records the phase, but positive-semidefiniteness, determinant, rank, and spectrum are identical for all phases. This complements `WP-300` and `WP-409`: arbitrary mixed-prime projective curvature can be written into the source once prime-relabeling symmetry is relaxed, yet the canonical equal-scale scalar Gram does not constrain it.

## 5. KMS does not kill this sector; it scalarizes into degree zero

Every path `X_a` of total scale `N` satisfies

\[
\alpha_t(X_a)=N^{it}X_a.
\]

Therefore each relative product `X_a^*X_b` has scale degree one and lies in the fixed-point spectral subspace. `WP-412` correctly predicts that these observables may survive a KMS state: the KMS frequency-selection rule does not annihilate them.

The present result identifies where they land in the central-twist case. They survive not as a noncommutative matrix of unrestricted holonomies, but as elements `d_a^*d_b` of the abelian diagonal `D`. Thus KMS survival is real, yet the most direct positive readout is still only a classical phase-correlation Gram.

No classification of twisted KMS states is required for this conclusion. If a particular KMS state has a distinguished restriction to `D`, that choice changes the averaging measure `nu_phi` in (5), not the structural factorization through `D` or the universal positivity proof.

## 6. Why this is not WP-407 or WP-408 again

`WP-407` shows that cycle phase can affect positivity of a general Hermitian block architecture once a genuine cycle remains after gauge fixing. There is no contradiction: the matrices in (5) are not arbitrary Hermitian cycle matrices. They are constrained to be actual Grams of common-range isometries, and in the scalar-multiplier case all path vectors are collinear. That extra coherence forces the rank-one collapse.

`WP-408` concerns honest groupoid `1`-cocycles and honest unitary representations of the **untwisted** Bost--Connes groupoid, whose native cycle holonomy is trivial on the relevant support. Here a central `2`-cocycle/Fell-line twist is granted as additional structure. The twist may be nontrivial; the statement is that one natural positive balanced-path readout reduces to diagonal phase correlations.

So the new boundary is neither “all cycle phases gauge away” nor “all balanced moments vanish.” The exact statement is: **central twisted factorization paths with one total scale share a bisection, and their canonical state Gram factors through the abelian unit space.**

## 7. Matched controls and arithmetic specificity

The mechanism in (5) is completely generic. Let `X` be any compact space, `nu` any probability measure, and `d_1,...,d_k` any continuous unit-modulus functions. Then

\[
G_{ij}=\int_X\overline{d_i}d_j\,d\nu
\]

is positive semidefinite by exactly the same proof. Nothing in that positivity distinguishes rational primes from generalized primes or even from a nonarithmetic compact dynamical system.

The scalar subclass is more programmable still. Multiplier theory on a free abelian scale group permits mixed-generator commutator phases that are not forced by the rational primes. For any such constant phase assignment realized by a multiplier, the equal-scale path Gram remains rank one. Hence neither positivity nor Gram spectral data can certify that the holonomy was arithmetically sourced.

This does not rule out a central twist whose **actual functions** `d_a(rho)` are independently forced by arithmetic and then enter a more informative non-tautological construction. It rules out treating the mere positivity of their state Gram as the missing independent sign theorem.

## 8. Prior-art and novelty audit

The general ingredients are classical. Twisted etale groupoids/Fell line bundles and their bisection calculus are standard; Buss--Exel is a direct structural reference. KMS theory for such bundles is treated by Afsar--Sims. Scalar multipliers on abelian groups and their projective commutator data are classical in Kleppner. Gram positivity and the representation of states on a commutative C-star algebra by probability measures are standard functional analysis.

No general theorem-level novelty is claimed for any of those ingredients. The Mathia-specific derived contribution is the composition of the current frontier: the off-diagonal central twist left open by `WP-410` survives the `WP-412` KMS frequency gate precisely on equal-scale paths, but those paths share one Bost--Connes bisection and their relative products therefore fall into `C(Z-hat)`. In the important scalar-projective subclass, the surviving mixed-prime phase is visible only as a vector rephasing and the entire positive Gram is rank one.

The literature audit found the standard twisted-groupoid, KMS, and multiplier frameworks but no arithmetic theorem turning this universal path-Gram positivity into a Weil-sign mechanism. The result is therefore classified as an exact derived obstruction for this research line, not as new twisted-groupoid mathematics.

## 9. Adversarial falsification gates

The finding must be narrowed or withdrawn if any of the following fails:

1. the integer-scale bisections satisfy `B_{n_1}...B_{n_r}=B_{n_1...n_r}` in the underlying Bost--Connes groupoid;
2. a unit-norm twisted section over `B_n` has source projection `1` and range projection `E_n` as established in `WP-410`;
3. all factorization paths of one total scale `N` therefore have common initial projection `1`, common range projection `E_N`, and support `B_N`;
4. `X_{a_0}^*X_a` is supported on the unit space and hence lies in `D=C(Z-hat)`;
5. the common-range identities make this relative element unitary and give `X_a=X_{a_0}d_a`;
6. state restriction to `D` gives exactly the correlation representation (5);
7. a scale-only scalar multiplier makes each `d_a` constant, hence the path Gram rank one;
8. the two-prime commutator phase can vary while the Gram determinant and spectrum remain fixed;
9. no archimedean or polar term has been silently inserted into this positivity argument.

Items 1--8 are algebraic/operator-theoretic and independent of zeta zeros or RH. Item 9 is the mandate check: this is a route restriction, not a global positivity theorem.

## Consequence

**Supported exact negative with a narrower surviving boundary.** Central twisting can retain genuinely base-dependent balanced holonomy after KMS frequency selection, but the canonical positive Gram of alternative integer-scale factorization paths is forced through the abelian diagonal `C(Z-hat)`. Scale-only projective twists collapse further to rank one, so their mixed-prime commutator phase affects matrix entries but not positive-semidefiniteness, rank, determinant, or spectrum.

The accepted Bost--Connes conditioning clue therefore remains unresolved. The live twisted route now needs more than a balanced central path Gram: it must provide independently source-forced arithmetic phase data and a non-generic use of it, or change category to noncentral/operator-valued fibres, active modular dynamics, altered source/range geometry, a different readout, or a finite--archimedean coupling formed before the universal Gram collapse.
