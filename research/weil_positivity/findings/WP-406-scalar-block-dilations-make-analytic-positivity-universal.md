---
id: WP-406
title: Scalar block dilations make analytic positivity universal
branch: weil_positivity
status: supported
kind: scalar-diagonal-two-by-two-positive-completion-phase-blind-universality
claim_strength: exact RH-independent obstruction showing that every bounded source element admits a positive 2-by-2 scalar-diagonal completion, so bare linking-matrix or dilation positivity outside the pointed analytic algebra is universal and phase-blind; any meaningful continuation after WP-405 must source-force nontrivial diagonal or coupling data rather than use existence of a positive completion itself
created: 2026-09-22
related: [WP-392, WP-404, WP-405]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - M. S. Moslehian, M. Kian, and Q. Xu, Positivity of 2x2 block matrices of operators, Banach Journal of Mathematical Analysis 13 (2019), 726--743, DOI 10.1215/17358787-2019-0019, arXiv:1904.08680
  - R. G. Douglas, On majorization, factorization, and range inclusion of operators on Hilbert space, Proceedings of the American Mathematical Society 17 (1966), 413--415
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411--457
---

# WP-406 — Scalar block dilations make analytic positivity universal

## Claim

`WP-405` closes ambient positivity **inside** a pointed analytic gauge algebra: self-adjointness pairs every nontrivial frequency with its inverse, so an analytic half-spectrum contains no positive elements beyond the fixed-point cone. One explicit boundary remained: place a non-self-adjoint analytic element in the off-diagonal corner of a larger self-adjoint or positive linking matrix, so that positivity lives outside the analytic algebra itself.

That category change is real, but its most immediate form is completely nonselective.

Let `A` be a unital C-star algebra and let `x in A`. For `t >= 0` define

\[
P_t(x)=
\begin{pmatrix}
t1 & x\\
x^* & t1
\end{pmatrix}
\in M_2(A).
\tag{1}
\]

Then

\[
\boxed{P_t(x)\ge 0\quad\Longleftrightarrow\quad t\ge \|x\|.}
\tag{2}
\]

Consequently **every bounded element of every unital C-star algebra has such a positive completion**, with the least scalar bath exactly `||x||`. Moreover the completion is phase-blind: for every scalar `lambda` with `|lambda|=1`,

\[
P_t(\lambda x)
=
\begin{pmatrix}\lambda 1&0\\0&1\end{pmatrix}
P_t(x)
\begin{pmatrix}\overline\lambda 1&0\\0&1\end{pmatrix}.
\tag{3}
\]

In particular `x` and `-x` have unitarily equivalent positive completions with exactly the same admissible values of `t`.

Thus a Bost--Connes analytic element may indeed retain nonzero arithmetic gauge degree in an off-diagonal corner of a positive matrix and thereby evade the literal hypothesis of `WP-405`. But the **existence** of that positive dilation supplies no arithmetic orientation: the same construction works for every bounded operator, every matched nonarithmetic control, and both signs/phases of the off-diagonal datum.

A viable dilation or correspondence route must therefore source-force additional structure—nontrivial diagonal blocks, a coupling law, a module/domain relation, a boundary condition, or another constraint whose positivity is not automatically available for arbitrary `x`. Merely embedding an oriented analytic element into a positive `2x2` matrix is not an explanatory Weil-sign mechanism.

**Classification:** `EXACT-DERIVED + CLASSICAL-BLOCK-POSITIVITY + RH-INDEPENDENT + UNIVERSAL-POSITIVE-COMPLETION + PHASE-BLIND + BOST-CONNES-ANALYTIC-DILATION-CONTROL + NEGATIVE/OBSTRUCTION + WP-405-BOUNDARY-CLASSIFICATION + NOT-A-WEIL-BRIDGE`.

## 1. Scalar block positivity is exactly a norm bound

Assume first that `t>0` and put `y=x/t`. Dividing (1) by `t` reduces the problem to

\[
M(y)=
\begin{pmatrix}
1&y\\
y^*&1
\end{pmatrix}.
\tag{4}
\]

The standard `2x2` block-positivity criterion gives

\[
M(y)\ge0
\quad\Longleftrightarrow\quad
\|y\|\le1.
\tag{5}
\]

For completeness, sufficiency follows from an explicit factorization. If `||y||<=1`, then `1-y^*y>=0` and

\[
\begin{pmatrix}
1&0\\
y^*&(1-y^*y)^{1/2}
\end{pmatrix}
\begin{pmatrix}
1&y\\
0&(1-y^*y)^{1/2}
\end{pmatrix}
=
\begin{pmatrix}
1&y\\
y^*&1
\end{pmatrix}.
\tag{6}
\]

Necessity is the corresponding Schur-complement/contraction implication: positivity of (4) forces `1-y^*y>=0`, hence `||y||<=1`. Therefore `P_t(x)>=0` exactly when `||x||<=t`.

When `t=0`, positivity of

\[
\begin{pmatrix}0&x\\x^*&0\end{pmatrix}
\tag{7}
\]

forces `x=0`; this agrees with (2). Thus no closure, approximation, spectral assumption, or arithmetic hypothesis is involved in the equivalence.

## 2. The positive-completion existence problem is vacuous

Equation (2) immediately gives

\[
\inf\{t\ge0:P_t(x)\ge0\}=\|x\|.
\tag{8}
\]

Hence every bounded `x` has a positive linking matrix, for example `P_{||x||}(x)`. If the diagonal is allowed to be chosen after `x` is known, positivity is only another expression of the ambient C-star norm bound.

This matters for the post-`WP-405` escape because moving positivity to a larger matrix algebra can look structurally stronger than asking the analytic element itself to be positive. It is stronger as a category change—`x` need not become self-adjoint—but weaker as a selector. The dilation exists before any arithmetic property of `x` is inspected.

The matched-control test is therefore exact. Replace a Bost--Connes analytic element by an arbitrary element of a nonarithmetic C-star algebra with the same norm. The same scalar diagonal produces the same positive `2x2` architecture. Bare completion existence cannot distinguish the arithmetic source from that control.

## 3. Positivity cannot orient an odd linear readout

The unitary covariance (3) sharpens the universality statement. The positive-completion condition depends only on `||x||`, so it is invariant under every scalar phase. Taking `lambda=-1` shows that the condition is exactly sign-symmetric.

Suppose a complex linear source space `X` is closed under `x -> -x`, and suppose one tries to infer a one-sided sign for a real-linear functional `L` using only the hypothesis that `x` admits a scalar block completion (1). That hypothesis holds for both `x` and `-x`. Therefore

\[
L(x)\ge0
\quad\hbox{and}\quad
L(-x)=-L(x)\ge0
\tag{9}
\]

would force `L(x)=0` for every `x` in the source class.

This does **not** say that every positive quadratic or nonlinear readout is trivial. It says that scalar block positivity, by itself, cannot explain a nonzero oriented linear coefficient. Any such orientation must enter through additional source-asymmetric structure rather than through existence of the positive completion.

The distinction is relevant to Weil positivity. A norm square may be positive for universal Hilbert-space reasons, but identifying its cross terms with the finite Mangoldt coefficients and simultaneously obtaining the archimedean and polar terms is an additional theorem. Equation (2) does not provide that bridge.

## 4. Bost--Connes analytic specialization

Let `A_BC` denote the represented Bost--Connes C-star algebra and `A_+` the pointed analytic half-spectrum considered in `WP-405`. For `x in A_+` with nonzero positive gauge frequencies, `WP-405` says that `x` cannot itself be ambient positive unless those frequencies vanish.

Nevertheless

\[
P_{\|x\|}(x)
=
\begin{pmatrix}
\|x\|1&x\\
x^*&\|x\|1
\end{pmatrix}
\in M_2(A_{BC})_+
\tag{10}
\]

is positive. The upper-right corner retains the positive analytic frequencies and the lower-left corner carries their adjoints, hence the inverse frequencies required by self-adjointness. The matrix enlargement therefore genuinely escapes the coefficientwise collapse of `WP-405`.

But it escapes by restoring the missing adjoint data in a second corner and paying a universal scalar bath `||x||1`. Nothing in (10) uses divisibility, the KMS state, critical inverse temperature, the Mangoldt support, prime logarithms, or the completed Weil functional. Replacing `x` by any bounded operator gives the same theorem.

The dilation route is therefore not killed as a category. What is killed is the inference

> source-canonical analytic orientation + existence of a positive linking matrix => source-canonical Weil orientation.

The second premise is universal. Any arithmetic force must reside in a stricter relation between the corners.

## 5. General positive block matrices locate the missing structure

The classical Douglas/Ando block-positivity theorem makes the boundary precise. For positive operators `A` and `B`,

\[
\begin{pmatrix}
A&X\\
X^*&B
\end{pmatrix}\ge0
\tag{11}
\]

if and only if the off-diagonal block factors, with the usual support interpretation when kernels are present, as

\[
X=A^{1/2} K B^{1/2}
\tag{12}
\]

for a contraction `K`.

The scalar construction is the special case `A=B=t1`, where the factorization constraint reduces to `||X||<=t`. Thus enlarging the diagonal category does not by itself create arithmetic content: if `A` and `B` may be freely chosen after `X`, large scalar diagonals solve the problem universally.

A nontrivial continuation must reverse that order of dependence. The source must first provide `A`, `B`, their supports/domains, or a restricted class of admissible contractions `K`; only then is it meaningful to ask whether the actual arithmetic `X` fits (12) and whether the resulting positive form has the required completed Weil coefficients.

This gives a concrete audit gate for correspondence/linking-algebra proposals. **Charge every diagonal block.** If a proposed sign proof uses a positive block matrix, identify which source theorem fixes each diagonal term before the target off-diagonal Weil coefficients are evaluated. A diagonal chosen merely large enough to dominate `X` is a positivity bath, not an explanation.

## 6. Stress tests and boundaries

The result is deliberately narrower than a no-go for all dilations or correspondences.

First, source-forced diagonal blocks can make (11) genuinely restrictive. If Bost--Connes/KMS data, a boundary algebra, an archimedean sector, or a canonical correspondence fixes `A` and `B` independently of the desired sign, the contraction condition (12) becomes mathematical content. `WP-406` does not prejudge whether such a construction exists.

Second, the argument is bounded. Singular forms, unbounded regular operators, source-forced graph domains, and nonunital boundary modules can fall outside the literal matrix (1). They still need their own nonprogrammability and matched-control audits; the present theorem should not be extended to them by analogy alone.

Third, phase blindness concerns what follows from the scalar completion condition. A source may impose a genuinely one-sided admissible set not closed under `x -> -x`, as the sharpness phenomenon of `WP-404` warns. Such asymmetry must itself be source-canonical and must survive the arithmetic-provenance controls; it cannot be inferred from (1).

Fourth, no archimedean or polar term is produced here. Even a nontrivial source-fixed block factorization at finite places would still need a completed global normalization and an independent positivity theorem on the Weil test class.

Finally, matrix positivity can certainly generate useful quadratic cross terms. The obstruction is not that off-diagonal information disappears, but that **generic positive completion does not select or orient that information**. Reading the already chosen `x` back from the corner is recovery, not a sign theorem.

## 7. Prior art and novelty audit

The operator theorem is classical. Douglas factorization underlies the standard characterization of positive `2x2` block operator matrices; Moslehian--Kian--Xu review the equivalence and its applications explicitly. No theorem-level novelty is claimed for (2), (11), or (12).

The program-specific contribution is the placement of that classical theorem exactly at the boundary left open by `WP-405`. The previous finding shows that a pointed analytic algebra cannot contain a nonfixed ambient positive element. The obvious next move—put the analytic element in a positive linking matrix—does evade that theorem, but the scalar-block calculation proves that this escape is **too universal to supply the missing arithmetic sign**.

This is not a duplicate of the bounded Bost--Connes selector obstruction `WP-392`: that result constrains positive elements of the source algebra that would isolate prime-power support. Here the off-diagonal datum may be completely arbitrary and need not be positive or a selector at all. The obstruction instead concerns the explanatory content of positivity after passing to a larger `2x2` matrix algebra.

Nor is it a repetition of the generic thin-slice warning `WP-404`. Thin source geometry can manufacture a one-sided cone. `WP-406` shows a complementary failure mode: a larger positive cone may be so generous that **every** bounded source datum enters it after a scalar completion. One route is too thin in a noncanonical way; this one is too permissive in a universal way.

## 8. Consequence for the live completion clue

The accepted Bost--Connes completion clue remains unresolved. `WP-406` only removes the cheapest dilation interpretation of its surviving category changes.

A future correspondence, module, linking-algebra, or finite--archimedean block proposal should therefore be tested in the following order: derive the diagonal sectors and admissible coupling from source data; prove that they are not freely inflatable scalar baths; apply the factorization/support constraint to the actual arithmetic off-diagonal block; then check whether the resulting quadratic form produces the finite Mangoldt coefficients, Gamma term, and polar normalization under one audited convention.

If the construction remains positive after replacing the arithmetic off-diagonal datum by arbitrary matched controls of the same norm, positivity has still not supplied the missing selection law. The decisive unresolved possibility is a **source-fixed positive block geometry whose admissible off-diagonal range is genuinely arithmetic** and whose global completion yields the Weil form without choosing the corners from the desired answer.
