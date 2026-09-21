---
id: WP-394
title: Source-resolvent visibility collapses positive unbounded mixed-prime selectors
branch: weil_positivity
status: supported
kind: bost-connes-closed-positive-form-resolvent-support-obstruction
claim_strength: exact RH-independent extension of WP-392 from bounded positive source elements to densely defined closed nonnegative forms, and by closure to closable nonnegative forms, whenever the associated self-adjoint operator has one canonical resolvent in the represented Bost--Connes source algebra; this genuinely unbounded class is nonempty, but exact mixed-prime nullity still forces the form to vanish
created: 2026-09-21
related: [WP-216, WP-304, WP-391, WP-392, WP-393]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - T. Kato, Perturbation Theory for Linear Operators, representation theorems for densely defined closed nonnegative forms
  - C. Budde and K. Landsman, A bounded transform approach to self-adjoint operators: functional calculus and affiliated von Neumann algebras, Annals of Functional Analysis 7 (2016), 411--420, arXiv:1508.06772
  - Bost--Connes standard positive-energy representations and the diagonal C(hat Z) source algebra
  - WP-392 full bounded Bost--Connes positive-cone support obstruction
---

# WP-394 — Source-resolvent visibility collapses positive unbounded mixed-prime selectors

## Claim

`WP-393` shows that Woronowicz affiliation with the original unital Bost--Connes C-star algebra does not create genuinely unbounded source elements. That does **not** dispose of closed positive forms: an unbounded positive self-adjoint operator may have a bounded resolvent inside the represented source algebra without being Woronowicz-affiliated with the unital algebra itself.

Nevertheless, exact prime-power selection already fails in this broader class.

Let `pi_alpha` be a standard positive-energy representation of the Bost--Connes algebra `A_BC` on

\[
\mathcal H=\ell^2(\mathbf N^\times),
\]

with basis `epsilon_k`. Let `q` be a densely defined closed nonnegative quadratic form on `H`, and let `T>=0` be its associated self-adjoint operator, so that

\[
D(q)=D(T^{1/2}),
\qquad
q(\xi)=\|T^{1/2}\xi\|^2.
\tag{1}
\]

Assume that for some `lambda>0`

\[
R_\lambda=(T+\lambda I)^{-1}\in\pi_\alpha(A_{BC}).
\tag{2}
\]

If every integer `k` divisible by at least two distinct primes satisfies

\[
\varepsilon_k\in D(q),
\qquad
q(\varepsilon_k)=0,
\tag{3}
\]

then

\[
\boxed{T=0\quad\text{and}\quad q=0.}
\tag{4}
\]

Equivalently: **a nonzero closed positive form with exact mixed-prime nullity cannot keep even one canonical resolvent inside the represented bounded Bost--Connes source algebra**.

The same conclusion holds for a densely defined **closable** nonnegative form `q_0` when the mixed-prime basis vectors lie in `D(q_0)` with `q_0(epsilon_k)=0` and the self-adjoint operator associated with its closure has a resolvent satisfying (2). The closure agrees with `q_0` on its original domain, so the closed-form theorem applies unchanged.

This is a strict category extension of `WP-392`, not a restatement of `WP-393`. Genuinely unbounded positive operators satisfying (2) exist; what fails is the additional exact selector condition (3).

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CLOSED/CLOSABLE-POSITIVE-FORM + KATO-REPRESENTATION + SINGLE-SOURCE-RESOLVENT + BOUNDED-TRANSFORM + WP-392-REDUCTION + EXACT-MIXED-NULLITY-NO-GO + GENUINELY-UNBOUNDED-CLASS-NONEMPTY + CATEGORY-BOUNDARY + NOT-A-WEIL-BRIDGE`.

## 1. The closed form has a canonical positive bounded transform

By the representation theorem for closed nonnegative forms, (1) determines a unique positive self-adjoint `T`. For any `lambda>0` define

\[
B_\lambda
:=T(T+\lambda I)^{-1}
=I-\lambda(T+\lambda I)^{-1}.
\tag{5}
\]

Spectral calculus gives

\[
0\le B_\lambda\le I.
\tag{6}
\]

Under the source-resolvent hypothesis (2), unitality of `pi_alpha(A_BC)` immediately gives

\[
B_\lambda\in\pi_\alpha(A_{BC}).
\tag{7}
\]

Thus the unbounded form has a canonical bounded positive shadow **inside exactly the source category classified by `WP-392`**. No target-dependent choice of scalar interpolant is involved: `t -> t/(t+lambda)` is fixed by the resolvent.

## 2. Mixed-prime form nullity becomes mixed-prime diagonal nullity

Take a mixed-prime label `k`. From (1) and (3),

\[
0=q(\varepsilon_k)=\|T^{1/2}\varepsilon_k\|^2,
\]

hence

\[
T^{1/2}\varepsilon_k=0.
\tag{8}
\]

Therefore `epsilon_k` lies in the zero spectral subspace of `T`. Applying the bounded function `t/(t+lambda)` gives

\[
B_\lambda\varepsilon_k=0,
\qquad
\langle B_\lambda\varepsilon_k,\varepsilon_k\rangle=0
\tag{9}
\]

for every mixed-prime `k`.

Now (6)--(7) put `B_lambda` exactly under the positive-cone theorem of `WP-392`. Its diagonal vanishes on every mixed-prime basis state, so

\[
\boxed{B_\lambda=0.}
\tag{10}
\]

The scalar function in (5) vanishes only at `t=0`. The spectral theorem therefore forces the spectral measure of `T` to be supported at zero, hence

\[
T=0.
\tag{11}
\]

Equation (1) then gives the zero form on all of `H`, proving (4).

Only one resolvent is needed. There is no requirement that the entire bounded functional calculus of `T` lie in the source algebra.

## 3. This is genuinely broader than Woronowicz affiliation

The hypothesis (2) is nonempty for unbounded operators in the standard Bost--Connes representation. The diagonal source algebra contains `C(hat Z)`. In a standard representation its elements act by evaluation along the dense arithmetic orbit

\[
k\longmapsto k\alpha,
\qquad \alpha\in\widehat{\mathbf Z}^{\,*}.
\tag{12}
\]

Choose a compatible metric `d` on the compact metrizable space `hat Z` and a continuous function

\[
r(x)=\min\{1,d(x,0)\}.
\tag{13}
\]

For every positive integer `k`, `k alpha !=0`, so `r(k alpha)>0`; but `n! alpha ->0` in `hat Z`, hence

\[
\inf_{k\ge1}r(k\alpha)=0.
\tag{14}
\]

Thus `R=pi_alpha(r)` is a positive injective contraction in `pi_alpha(A_BC)` that is not bounded below. The spectral operator

\[
T:=R^{-1}-I
\tag{15}
\]

is therefore positive, self-adjoint, and genuinely unbounded on its natural dense domain, while

\[
(T+I)^{-1}=R\in\pi_\alpha(A_{BC}).
\tag{16}
\]

By `WP-393`, this `T` cannot be a Woronowicz-affiliated element of the original unital `A_BC`; nevertheless it satisfies the source-resolvent condition (2). Hence the present theorem closes a real unbounded class that `WP-393` did not close.

The example deliberately does **not** satisfy the mixed-prime nullity condition. Its role is only to show that source-resolvent visibility and Woronowicz affiliation are different boundaries.

## 4. Consequence for nonunital and boundary-algebra proposals

A canonically produced nonunital ideal or boundary algebra can still be a genuinely new category, but mere nonunitality is not enough. Suppose a proposed positive self-adjoint `T` is realized through such a boundary construction and, in the standard Bost--Connes Hilbert space, one of its canonical resolvents lands in

\[
\pi_\alpha(A_{BC}).
\tag{17}
\]

Then the proof above applies without caring how that resolvent was produced. Exact mixed-prime form nullity again forces `T=0`.

Therefore a surviving nonunital/form route must do at least one mathematically substantive thing differently: its relevant resolvent or bounded transform must leave the represented source C-star algebra; its source-derived domain must not simply encode exact mixed-prime nullity on the basis; the representation/correspondence must change; or prime-power support must emerge only after a larger finite--archimedean/global operation.

This does **not** rule out source-derived nonunital boundary algebras in general. It rules out only those whose positive selector form re-enters the already-classified bounded source algebra through the canonical resolvent used above.

## 5. Relation to the earlier resolvent obstruction

`WP-304` studied a different resolvent boundary. There the object is a bounded compression of a **source spectral resolvent**,

\[
V^*(H-z)^{-1}V,
\]

whose finite spectral mass forces `O(1/y)` decay and prevents it from generating the logarithmically growing archimedean response. The present theorem instead starts with an **unbounded candidate selector/form operator `T`** and asks whether its own canonical resolvent remains inside the represented Bost--Connes C-star algebra.

Thus the two results constrain different roles of resolvents. `WP-304` is a high-energy/Gamma-sector obstruction for bounded source incidence; `WP-394` is a support-selection obstruction obtained by feeding the positive bounded transform of an unbounded form back into `WP-392`. Neither subsumes the other.

## 6. Prior-art and novelty audit

The operator-theoretic ingredients are classical. Kato's representation theorems identify densely defined closed nonnegative forms with positive self-adjoint operators and give (1). Resolvent and bounded-transform functional calculus for unbounded self-adjoint operators is standard; the modern bounded-transform treatment of Budde--Landsman is a convenient reference. The Bost--Connes diagonal `C(hat Z)` and its positive-energy representations are likewise classical.

The Mathia-specific input is `WP-392`: positivity plus exact mixed-prime-null diagonal inside the full bounded Bost--Connes C-star algebra forces the operator to vanish. The new line-specific consequence is the reduction (5)--(11): **one canonical source-valued resolvent is already enough to pull an exact mixed-null closed positive form back into that bounded no-go**.

A bounded literature search around closed positive forms, resolvent/bounded transforms, Bost--Connes representations, and prime-power support found the standard operator-theoretic machinery but no direct Bost--Connes support theorem of this form. No novelty is claimed for Kato theory, bounded transforms, or the diagonal representation. The recorded contribution is the exact source-category consequence obtained by combining those classical facts with `WP-392`.

## Limits

- Closedness, nonnegativity, and dense definition are used through the positive self-adjoint representation of the form; the closable variant is obtained only by passing to the closure.
- Exact mixed-prime nullity is essential. Approximate suppression is a different quantitative problem.
- The mixed-prime basis vectors must belong to the form domain. Excluding them from the domain is outside the theorem, but such a domain restriction would itself need a source-derived justification rather than target coding.
- The theorem assumes one resolvent belongs to the **represented norm-closed Bost--Connes C-star algebra**. A resolvent lying only in the bicommutant `B(H)`, a larger von Neumann algebra, or a genuinely different module/boundary representation is outside the result.
- The theorem says nothing by itself about modular weights, nonpositive/signed forms, one-sided correspondence defects, approximate selectors, or constructions where support appears only after global assembly.
- No Gamma factor, polar term, completed Weil form, independent sign theorem, or RH consequence is produced.

## Consequence for the research line

The phrase "use a source-forced closable form with a nonprogrammable domain" is now too broad to count as a surviving escape. For a closed nonnegative form, **if even one canonical resolvent remains in the standard represented Bost--Connes source algebra, exact mixed-prime nullity collapses the form to zero**; the same holds for a closable form after passage to its closure under the hypotheses stated above.

The live unbounded frontier must therefore explain a genuine categorical displacement: a source-derived domain/resolvent outside the bounded source representation, a canonical modular or von Neumann constraint, a nontrivial correspondence or one-sided range defect, a boundary algebra whose represented functional calculus does not fall back into `pi_alpha(A_BC)`, or a global finite--archimedean assembly in which prime-power support is not imposed beforehand. This narrows the accepted Bost--Connes completion clue without resolving its archimedean or global sign problem.
