---
id: WP-287
title: Nonlinear Arthur-height scalarizations that remain distributions collapse to linear height filters
branch: weil_positivity
status: supported
kind: nonlinear-scalarization-factorization-obstruction
claim_strength: exact algebraic reduction showing that arbitrary post-processing of the scalar Arthur-height profile gives no escape from the linear-height obstruction if the output is required to be a linear Weil-type distribution
created: 2026-09-13
related: [WP-237, WP-238, WP-239, WP-240, WP-241]
prior_art:
  - Tian An Wong, Explicit formulas for the spectral side of the trace formula of SL(2), Acta Arithmetica 195 (2020), 149-175, DOI 10.4064/aa190115-9-10
  - elementary universal factorization of linear maps through a quotient/image
---

# WP-287 — Nonlinear Arthur-height scalarizations that remain distributions collapse to linear height filters

## Claim

`WP-237` closes every **linear** operation acting only on the Arthur truncation-height variable of Wong's positive Maaß--Selberg family: the complete explicit-formula block

\[
D(g)=W(g)+P_{\rm fin}(g)+A_\infty(g)+C_{\rm pol}(g)
\]

is independent of the truncation height, so a height filter either removes that common block or retains it without internally resolving the Weil zero functional `W` from its finite-prime and archimedean/polar companions.

A natural apparent escape is to abandon linear height filtering while keeping the same positive scalar data. One could minimize or maximize over heights, take ratios, logarithms, products, nonlinear regressions of several height values, or apply an arbitrary nonlinear functional to the entire profile

\[
T\longmapsto Q_T(g).
\]

That does not create a new route **if the claimed output is still a Weil-type linear distribution in the test function**.

Let `V` be the linear test-function space on which Wong's distributions `Q_T` are defined, and define the complete scalar height-profile map

\[
\mathcal Q:V\longrightarrow \mathcal P,
\qquad
(\mathcal Q g)(T):=Q_T(g),
\tag{1}
\]

where `P:=im(Q)` is the vector space of profiles actually attainable from admissible tests. Each `Q_T` is a distribution, hence `mathcal Q` is linear.

Now let

\[
\Phi:\mathcal P\to\mathbb C
\tag{2}
\]

be **arbitrary**: no continuity, differentiability, convexity, positivity, or a priori linearity is assumed. Suppose only that the resulting scalar rule

\[
R(g):=\Phi(\mathcal Qg)
\tag{3}
\]

is claimed to be a linear distribution on `V`, as the Weil zero functional is.

Then `Phi` is automatically linear on the entire attainable profile space `P`. Indeed, for `u=Qg`, `v=Qh`, and `lambda in C`,

\[
\Phi(u+v)
=R(g+h)
=R(g)+R(h)
=\Phi(u)+\Phi(v),
\tag{4}
\]

and

\[
\Phi(\lambda u)
=R(\lambda g)
=\lambda R(g)
=\lambda\Phi(u).
\tag{5}
\]

Thus every nonlinear scalarization that genuinely returns a distribution **collapses, on the only profiles it ever sees, to a linear height-profile functional**. Any nonlinear behavior of `Phi` away from `im(Q)` is mathematically irrelevant.

For a finite set of heights `T_1,...,T_N`, this becomes especially concrete. If

\[
R(g)=F\bigl(Q_{T_1}(g),\ldots,Q_{T_N}(g)\bigr)
\tag{6}
\]

is linear in `g`, then there are constants `a_1,...,a_N` such that

\[
\boxed{
R(g)=\sum_{j=1}^N a_jQ_{T_j}(g)
\qquad(g\in V).
}
\tag{7}
\]

No regularity of `F` is required. Equation (7) follows because the linear functional induced on the subspace

\[
\operatorname{im}
\bigl(g\mapsto(Q_{T_1}(g),\ldots,Q_{T_N}(g))\bigr)
\subseteq\mathbb C^N
\]

extends linearly to `C^N`.

Therefore **finite nonlinear post-processing of positive Arthur-height scalar data cannot evade `WP-237` while still producing the Weil distribution**. For the full height profile the same quotient/image argument says that any successful profile-only rule must already be linear on the attainable profile space; it has not acquired a genuinely nonlinear source of resolution between the zero, prime, Gamma, and polar pieces.

**Classification:** `EXACT-DERIVED + ARBITRARY-NONLINEAR-SCALAR-POSTPROCESSING + DISTRIBUTION-LINEARITY-FACTOR-GATE + REDUCES-TO-LINEAR-HEIGHT-PROFILE-CLASS + MAASS-SELBERG-POSITIVE-CONTROL + ARITHMETIC-BLIND-ALGEBRAIC-OBSTRUCTION + NO-NOVELTY-CLAIM-FOR-FACTOR-LEMMA + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Why the target is linear before positivity is imposed

The subtle point is that Weil positivity is a positivity statement about a **linear distribution in the test function**. If `g=g_0*g_0^*`, then the resulting value is quadratic in `g_0`, but the underlying explicit-formula functional

\[
W(g)
\]

is linear in `g`. Wong's trace-formula distributions `Q_T(g)` have exactly the same structural status: for every fixed `T`, `Q_T` is linear in `g`, and positivity is asserted only after restricting to positive-type tests.

This distinction matters for proposed nonlinear repairs. A positive number obtained from

\[
\min_TQ_T(g),\qquad
\max_TQ_T(g),\qquad
\log Q_T(g),\qquad
Q_{T_1}(g)Q_{T_2}(g),
\tag{8}
\]

or from a nonlinear learned map of several height values may be a perfectly legitimate scalar statistic. But unless it is additive and homogeneous in `g`, it is **not** the Weil distribution and does not inherit Weil's criterion merely from being nonnegative on positive-type tests.

If a proposal does satisfy the required linearity exactly, equations (4)--(5) show that its apparent nonlinearity disappears on the source-generated data manifold `P`. This is not a smoothness argument and cannot be escaped by nonsmooth rules such as minima, maxima, thresholds, or piecewise definitions.

The same statement can be phrased through the universal property of the quotient. Because `R` depends only on the profile `Qg`,

\[
\ker\mathcal Q\subseteq\ker R.
\tag{9}
\]

Hence a linear `R` factors uniquely through

\[
V/\ker\mathcal Q
\cong
\operatorname{im}\mathcal Q.
\tag{10}
\]

The induced factor is linear. The entire theorem is this elementary algebraic fact applied to the Maaß--Selberg profile.

## 2. Finite-height nonlinear rules reduce exactly to finite linear combinations

Fix source-defined heights `T_1,...,T_N` and write

\[
L:V\to\mathbb C^N,
\qquad
L(g)=\bigl(Q_{T_1}(g),\ldots,Q_{T_N}(g)\bigr).
\tag{11}
\]

Suppose an arbitrary function `F` is used only through `L(g)`, and `R=F\circ L` is linear. Define

\[
\ell:L(V)\to\mathbb C,
\qquad
\ell(Lg):=R(g).
\tag{12}
\]

This is well-defined: if `Lg=Lh`, then `F(Lg)=F(Lh)`, so `R(g)=R(h)`. Linearity of `R` and `L` makes `ell` linear on `L(V)`. Since `L(V)` is a subspace of the finite-dimensional space `C^N`, extend `ell` to a linear functional on all of `C^N`. Thus there exist coefficients `a_j` for which

\[
\ell(z_1,\ldots,z_N)=\sum_j a_jz_j,
\tag{13}
\]

on `L(V)`, and (7) follows.

No assumption that the individual distributions `Q_{T_j}` are linearly independent is needed. If they are dependent, the extension coefficients are nonunique, but the resulting distribution `R` is still in their linear span. Consequently adding more finite scalar height samples and then applying a nonlinear combiner does not enlarge the class of linear distributions obtainable from those samples.

Now insert the exact decomposition from `WP-237`,

\[
Q_T(g)=D(g)+B_T(g).
\tag{14}
\]

Equation (7) becomes

\[
R(g)
=\left(\sum_ja_j\right)D(g)
+\sum_ja_jB_{T_j}(g).
\tag{15}
\]

Thus the allegedly nonlinear finite-height repair has returned to precisely the linear-height class already audited there. In particular, it has gained no new operation that can inspect the internal decomposition

\[
D=W+P_{\rm fin}+A_\infty+C_{\rm pol}
\tag{16}
\]

before scalarization. Any cancellation engineered through the second term of (15) is a linear height cancellation and must pass the same source-forcing and target-independence tests as before.

## 3. The entire height profile does not rescue nonlinear post-processing

The finite-dimensional statement is useful because it covers every proposal based on finitely many canonical truncations, but the factorization gate is not intrinsically finite.

Let `P=im(Q)` be the full attainable profile space. If `Phi:P->C` produces a linear distribution `R=Phi o Q`, then (4)--(5) prove directly that `Phi` is linear on `P`. Thus operations such as

\[
\inf_TQ_T(g),
\qquad
\sup_TQ_T(g),
\qquad
\operatorname*{argmin}_T Q_T(g)
\quad\text{followed by a scalar readout},
\tag{17}
\]

have only two possibilities relevant here.

Either their restriction to the actual Maaß--Selberg profile space is nonlinear, in which case the output is not a linear explicit-formula distribution. Or, after all source constraints are imposed, the rule happens to be linear on that profile space, in which case it belongs to the same profile-linear category and its apparent nonlinearity has supplied no additional resolution.

This sharpens the warning in `WP-237` about choosing a truncation height separately for each test. Wong's `T`-optimization is a legitimate way to improve a lower bound. But a test-dependent optimum is not thereby a new fixed Weil distribution. To become one, the optimized rule would first have to satisfy the exact additivity and homogeneity identities (4)--(5) on the full admissible test space; if it does, it has collapsed to a linear profile functional.

The conclusion is deliberately algebraic rather than analytic. It does not require existence or uniqueness of an optimizing height, differentiability in `T`, compactness of the height range, or any asymptotic control of `Q_T`.

## 4. Matched control: the factorization is completely arithmetic-blind

Nothing in (1)--(13) uses the Riemann zeta function, the zero divisor, the Gamma factor, or even the Maaß--Selberg formula beyond the fact that `Q_T` is linear in the test function.

Replace the zeta scattering normalizer by any matched scalar scattering system and let

\[
T\mapsto Q_{T,m}(g)
\tag{18}
\]

be its family of linear truncated distributions. Every scalar rule of the profile that returns a linear distribution again factors linearly through the attainable profile space.

Therefore the reduction is not itself arithmetic evidence. Its role is adversarial: **nonlinearity after scalarization cannot be credited as the missing geometric ingredient merely because the input family is positive and automorphic.** If the desired output remains a distribution, any genuine new structure must occur before the family has been compressed to the scalar height profile, or must add new source data not present in that profile.

This matched control is important because arbitrary nonlinear scalar maps are otherwise too programmable. Given enough target knowledge one can define a function on the set of observed profiles to return any desired values. Equations (4)--(5) show that exact distribution linearity removes that freedom on the attainable profile space; what remains is a linear factor and hence must be audited as such.

## 5. Aggressive falsification and exact boundary

**Could a nonlinear `F` be wildly discontinuous and evade the theorem?** No. Continuity is never used. If `F o L` is linear, the restriction of `F` to `L(V)` is linear by pure algebra.

**Could nonlinear processing of many heights create cross-height information absent from a linear combination?** It can create nonlinear statistics, but not a new linear distribution. For finitely many heights, any output that remains linear is exactly a linear combination by (7).

**Could positivity alone substitute for distribution linearity?** No. A nonnegative homogeneous or convex statistic of the positive `Q_T` family may be useful analytically, but it is a different object. To identify it with Weil positivity one still needs a theorem showing that it equals, polarizes to, or otherwise controls the canonical Weil quadratic form over the required full test class. That theorem is not supplied by Maaß--Selberg positivity.

**Does this rule out nonlinear operations on the underlying Eisenstein/intertwining operators before the scalar trace is taken?** No. This is the principal surviving boundary. A nonlinear operator-level construction can change the source object before the information bottleneck (1) is formed; it is not a function only of `T -> Q_T(g)` and is outside the theorem.

**Does it rule out a cone-only quadratic form defined solely on convolution squares?** Not automatically. A rule could be posed only on `g_0*g_0^*` and never claim a linear extension in `g`. But then matching the Weil criterion requires an additional polarization/extension theorem identifying that cone functional with the canonical Weil form, or a separate proof that its positivity is equivalent to the same global criterion. Without such a theorem it is merely another positive statistic. The present result closes the route only when the scalarized construction claims to recover a Weil-type distribution itself.

**Could a target-coded nonlinear rule return `W` on the observed profile set?** Formally yes, just as any lookup table can encode desired answers. If it returns `W` exactly then, because `W` is linear, its restriction to the attainable profile space is linear by the theorem. Such a rule has therefore hidden the target in the choice of that linear factor rather than produced a new nonlinear positivity mechanism, and it fails the line's source-independence gate unless that factor is independently forced.

## 6. Prior-art and novelty audit

The automorphic input is classical and is already the audited source of `WP-237` and the bounded cross-line control `PL-253`: Tian An Wong's 2020 `SL(2)` trace-formula paper proves positivity of the truncated continuous spectral distribution and derives a lower bound for the Weil zero sum depending on the Eisenstein truncation parameter. The current literature check again found Wong's published paper and dissertation as the direct source for this lower-bound/truncation interface; it did not reveal a distinct claimed theorem that nonlinear scalar post-processing of truncation heights isolates the Weil zero distribution.

No novelty is claimed for the algebraic factorization (9)--(13). It is the universal property of quotient spaces/images: a linear map that depends only on another linear map factors linearly through its image. In the finite-height case, extension of a linear functional from a subspace of `C^N` is elementary finite-dimensional linear algebra.

The Mathia-specific delta is therefore not a new theorem in functional analysis or trace formulas. It is a **category closure at the current search frontier**. `WP-237` left nonlinear processing of the scalar values `{Q_T(g)}` formally outside its linear-height statement. The present factorization shows that this apparent escape disappears as soon as the output is required to retain the defining structural property of the Weil explicit-formula functional: linearity in `g`.

## Consequence for `weil_positivity`

The Maaß--Selberg clue is narrowed one step further. The scalar positive family

\[
\{Q_T(g):T\}
\]

cannot be made more selective by post hoc nonlinear processing **and still remain the canonical kind of object whose positivity Weil's criterion asks about**. If the post-processor returns a distribution, it reduces on source-attainable profiles to a linear height functional and falls back into the `WP-237` obstruction class. If it remains genuinely nonlinear, its positivity concerns a different scalar functional and needs a new theorem before it can be compared to Weil positivity.

The surviving automorphic route is therefore pre-scalarization. A substantive advance must act inside the global continuous spectral Hilbert space, on the intertwining/scattering operators, on a source-defined finite--archimedean coupling, on a relative/cohomological object, or on another structure that changes the object **before** the positive Maaß--Selberg family is reduced to one scalar number per height. It must then supply an independent sign theorem and preserve the full finite-prime plus archimedean/polar normalization without inserting the zero divisor.