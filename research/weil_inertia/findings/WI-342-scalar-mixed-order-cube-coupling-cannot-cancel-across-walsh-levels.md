# WI-342 — scalar mixed-order cube coupling cannot cancel across Walsh levels

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-IDENTITY`.

**Parent findings:** WI-338, WI-339, WI-340, WI-341.

WI-341 shows that, at one fixed Gowers order, every deterministic scalar reweighting of injective additive-cube monomials factors through the Walsh character indexed by the unordered vertex set. A natural continuation left open there is to couple several derivative orders, hoping that cross-order interference can suppress the matched-energy Rademacher chaos while retaining information useful for the distinguished bow covariance of WI-195.

Two broad source-blind versions of that continuation admit exact reductions. First, **linear scalar mixtures of different injective cube orders are exactly orthogonal in Rademacher `L^2`**: order `s` lives on Walsh level `2^s`, so no character occurring at one order can occur at another. There is therefore no destructive cross-order term to exploit. Second, the canonical nonlinear coupling supplied by the Gowers multiplicative-derivative recursion — multiplying two parallel `s`-faces with the conjugation dictated by the derivative — is identically the `(s+1)`-cube product. It does not create a new observable; it merely moves one step up the higher-order hierarchy already stress-tested in WI-334--WI-340.

This does **not** rule out every nonlinear mixed-order construction. Products of unrelated post-quotient observables can generate new Walsh characters through symmetric differences, and source- or carrier-dependent coefficients can leave the deterministic scalar setting entirely. The exact no-go is narrower: ordinary linear pooling across orders gives no cancellation, while the standard facewise derivative coupling is just the next Gowers order.

## 1. Exact orthogonality of distinct injective cube orders

Let `I` be a finite integer interval. For each order `s` in a finite set `S`, let `\mathcal C_s` be any deterministic family of **injective** additive `s`-cubes in `I`. Thus every

\[
c=(x,h_1,\ldots,h_s)\in\mathcal C_s
\]

has `2^s` pairwise distinct vertices

\[
A_s(c):=\{x+\omega\cdot h:\omega\in\{0,1\}^s\},
\qquad |A_s(c)|=2^s.
\tag{1}
\]

For independent Rademacher signs `\varepsilon_n\in\{\pm1\}`, write

\[
\chi_A(\varepsilon):=\prod_{n\in A}\varepsilon_n.
\tag{2}
\]

Give the cubes arbitrary deterministic complex coefficients `a_{s,c}` and define, for nonzero `Z`,

\[
P
:=
\frac1Z
\sum_{s\in S}\sum_{c\in\mathcal C_s}
 a_{s,c}\chi_{A_s(c)}.
\tag{3}
\]

Within each order collect equal vertex sets exactly as in WI-341:

\[
T_{s,A}
:=
\sum_{c\in\mathcal C_s:\,A_s(c)=A}a_{s,c}.
\tag{4}
\]

If `s\ne t`, then a set occurring at order `s` has cardinality `2^s` whereas a set occurring at order `t` has cardinality `2^t`. Hence

\[
A_s(c)\ne A_t(c')
\qquad(s\ne t).
\tag{5}
\]

Distinct Walsh characters are orthogonal. Therefore the order components

\[
P_s:=\sum_A T_{s,A}\chi_A
\tag{6}
\]

satisfy the exact identities

\[
\boxed{
\langle P_s,P_t\rangle_{L^2(\varepsilon)}=0
\qquad(s\ne t),
}
\tag{7}
\]

and

\[
\boxed{
\|P\|_2^2
=
\frac1{|Z|^2}
\sum_{s\in S}\sum_A |T_{s,A}|^2.
}
\tag{8}
\]

Thus there is no negative cross-order covariance hidden by the separate-order treatment in WI-341. Whatever cancellation deterministic scalar weights create occurs **inside one fixed Walsh character**, hence inside one fixed order, and has already been exposed by the quotient `c\mapsto A(c)` of WI-341.

The injectivity hypothesis is essential to the clean level separation: a degenerate cube can collapse to a lower-cardinality parity support. This is not a missing generic escape in the present bow audit. WI-340 proves that all repeated-vertex cubes form only a `K^{-1+o(1)}` fraction of the relevant geometry for `s=O(\log\log N)` and that deleting or isolating any `o(D)` deterministic family does not change the renormalized random-chaos floor. The statement here deliberately concerns the generic injective sector left after that audit.

## 2. Honest renormalization still has an effective-sample floor

Let

\[
W:=\sum_{s,A}|T_{s,A}|,
\qquad
Q:=\sum_{s,A}|T_{s,A}|^2,
\qquad
M_{\rm eff}:=\frac{W^2}{Q}
\tag{9}
\]

when `W>0`. Equation (8) gives exactly

\[
\boxed{
\left\|
\frac1W\sum_{s,A}T_{s,A}\chi_A
\right\|_2
=M_{\rm eff}^{-1/2}.
}
\tag{10}
\]

If

\[
M:=|\{(s,A):T_{s,A}\ne0\}|,
\tag{11}
\]

then Cauchy--Schwarz gives `M_eff<=M`, so

\[
\boxed{
\left\|
\frac1W\sum_{s,A}T_{s,A}\chi_A
\right\|_2
\ge M^{-1/2}.
}
\tag{12}
\]

Moreover

\[
M\le\sum_{s\in S}|\mathcal C_s|.
\tag{13}
\]

For the full interval cube families at orders `2<=s<=S_N`, with interval length `K=N^{\kappa+o(1)}` and `S_N=O(\log\log N)`, the elementary cube counts used in WI-338--WI-340 give

\[
\sum_{s=2}^{S_N}|\mathcal C_s|
=K^{S_N+1+o(1)}.
\tag{14}
\]

Indeed the top-order family already has `K^{S_N+1-o(1)}` elements, while the sum of the trivial upper bounds for all lower orders is `K^{S_N+1+o(1)}`. Hence pooling all orders through a scalar linear statistic does not create a larger effective-sample exponent than the highest included order. It can redistribute weight among mutually orthogonal Walsh levels, but it cannot gain a new cancellation exponent from their interaction.

Equation (14) is only an exponent-level comparison; the exact content is (7)--(12). No claim is made that every possible normalization or nonlinear postprocessing of mixed orders is equivalent to one `U^{S_N}` norm.

## 3. The canonical facewise nonlinear coupling is exactly the next cube

The standard Gowers coupling has an even stronger reduction that holds for every complex source, not just for Rademacher signs. Define the multiplicative `s`-cube product

\[
C_s(f;x,h_1,\ldots,h_s)
:=
\prod_{\omega\in\{0,1\}^s}
\mathcal C^{|\omega|}
 f(x+\omega\cdot h),
\tag{15}
\]

where `\mathcal C z=\overline z`. Splitting an `(s+1)`-cube into its two parallel `s`-faces gives the exact recursion

\[
\boxed{
C_{s+1}(f;x,h_1,\ldots,h_s,k)
=
C_s(f;x,h_1,\ldots,h_s)
\overline{C_s(f;x+k,h_1,\ldots,h_s)}.
}
\tag{16}
\]

This is simply the multiplicative-derivative identity underlying the Gowers norms. Therefore a proposal that couples adjacent orders by matching two parallel faces in the canonical derivative way has not defined an intermediate statistic: it has written the next-order cube product in factored form.

For a real Rademacher source and an injective `(s+1)`-cube, the two faces have disjoint vertex sets `A_0,A_1`, each of size `2^s`, and (16) reduces to

\[
\chi_{A_0}\chi_{A_1}
=
\chi_{A_0\cup A_1},
\qquad
|A_0\cup A_1|=2^{s+1}.
\tag{17}
\]

So the canonical face coupling moves exactly from Walsh level `2^s` to level `2^{s+1}`. Any attempt to escape WI-334--WI-340 by this operation is therefore already contained in their growing-order analysis.

## 4. What remains outside the no-go

The identities above do not say that **every** mixed-order observable collapses. If two unrelated quotient-level polynomials are multiplied, Walsh multiplication gives

\[
\chi_A\chi_B=\chi_{A\triangle B},
\tag{18}
\]

so overlaps can create a genuinely new spectrum of symmetric-difference characters. A nonlinear functional can also compare several order components before summation, or insert the bow carrier and the arithmetic source before the scalar vertex product has been collapsed. Those constructions are not covered by (8), and only the specially matched parallel-face product is reduced by (16).

This boundary is important for the accepted clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation`. After WI-341, “couple orders” was still a generic escape label. The present result removes its two most immediate source-blind realizations:

- a deterministic scalar **linear** combination cannot cancel between orders because the orders occupy disjoint Walsh levels;
- the canonical Gowers **multiplicative derivative** coupling is exactly the next order and therefore does not leave the existing hierarchy.

A remaining generic route must consequently introduce a genuinely new nonlinear post-quotient observable whose Walsh support is not just the union of the old levels and is not algebraically the next cube. The more direct alternative remains the one demanded by WI-195 itself: retain source/carrier-specific signed two-point covariance at the distinguished bow twist, including the `Lambda^sharp` structured term in the same norm.

## 5. Prior art and novelty audit

The ingredients are classical. Walsh characters form an orthonormal basis on the discrete cube, and Parseval decomposes `L^2` by Fourier level; a standard reference is Ryan O'Donnell, *Analysis of Boolean Functions* (Cambridge University Press, 2014), Chapter 1, DOI `10.1017/CBO9781139814782`. Gowers' uniformity norms and their cube/multiplicative-derivative structure originate in W. T. Gowers, *A new proof of Szemerédi's theorem*, *Geom. Funct. Anal.* 11 (2001), 465--588, DOI `10.1007/s00039-001-0332-9`.

A bounded prior-art search found the standard homogeneous-chaos orthogonality and Gowers derivative recursion, but not this specific bow-line deduction combining them with the WI-339--WI-341 Rademacher obstruction. No priority claim is made. The additional content here is the exact classification of two proposed mixed-order escapes relative to the already-persisted bow interface.

## 6. Evidence boundary and falsification

This finding is an exact algebraic/random-model obstruction, not a theorem about primes and not a proof that the distinguished bow variance is large. It changes no zeta-zero proportion and does not exclude an individual off-critical zero.

The linear orthogonality claim can be falsified only by producing injective cubes of two distinct orders with the same Walsh character; (1) and cardinality make that impossible. The canonical-coupling claim can be falsified only by violating the direct factorization (16).

A genuine escape is therefore sharply identifiable: exhibit a nonlinear mixed-order statistic whose post-expansion Walsh characters are not merely a disjoint union of fixed-order characters or the next-order parallel-face cube, and then show that the arithmetic source controls that statistic strongly enough to imply the WI-195 signed covariance. Source-dependent coefficient systems or carrier-dependent interactions introduced before scalar collapse also lie outside the present no-go.

## Lineage

`WI-338 -> WI-339 -> WI-340 -> WI-341 -> WI-342`.

- WI-338--WI-340 establish the growing-order Rademacher countermodel and isolate the generic injective cube sector.
- WI-341 proves the exact fixed-order Walsh-character quotient and closes scalar tapering/reweighting.
- WI-342 proves cross-order orthogonality for linear scalar pooling and identifies the canonical adjacent-face coupling with the next Gowers cube.