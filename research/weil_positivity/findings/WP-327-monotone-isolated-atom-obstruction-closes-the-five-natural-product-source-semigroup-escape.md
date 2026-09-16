---
id: WP-327
title: Monotone isolated-atom obstruction closes the five-natural-product source-semigroup escape
branch: weil_positivity
status: supported
kind: noncommutative-convolution-semigroup-obstruction
claim_strength: exact literature-backed obstruction for the pole-normalized Mangoldt source under monotone convolution, exact reduction of anti-monotone self-divisibility to monotone self-divisibility, and synthesis with WP-325/WP-326 across Muraki's five natural products
created: 2026-09-16
related: [WP-304, WP-318, WP-325, WP-326]
prior_art:
  - Takahiro Hasebe, Monotone convolution and monotone infinite divisibility from complex analytic viewpoint, Infinite Dimensional Analysis, Quantum Probability and Related Topics 13 (2010), no. 1, 111-131, DOI 10.1142/S0219025710003973; broader preprint arXiv:1002.3430, especially Theorem 3.5 on isolated atoms of monotone-infinitely-divisible laws
  - Naofumi Muraki, The five independences as natural products, Infinite Dimensional Analysis, Quantum Probability and Related Topics 6 (2003), no. 3, 337-371, DOI 10.1142/S0219025703001365
  - David Andrew Jekel, Evolution equations in non-commutative probability, UCLA PhD dissertation (2020), for the order-reversal relation between monotone and anti-monotone convolution and the equality of their convolution-semigroup classes
---

# WP-327 — Monotone isolated-atom obstruction closes the five-natural-product source-semigroup escape

## Claim

`WP-325` and `WP-326` leave a precise residual question for the direct source-semigroup route. The exact pole-normalized Mangoldt law cannot be classically or freely infinitely divisible, whereas Boolean infinite divisibility is universal and therefore nonselective. Muraki's classification of natural products leaves monotone and anti-monotone independence as the remaining additive convolution categories in that axiomatic class.

They do not rescue the route.

For `s>0`, let

\[
\nu_s
=
\frac1{L(s)}
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}n^{-s}\,\delta_{\log n},
\qquad
L(s)=
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}n^{-s}.
\tag{1}
\]

This is the probability law isolated in `WP-325` and reused in `WP-326`. Its first two support points are `log 2` and `log 3`, both with positive mass, with no support between them. In particular `log 2` is an isolated atom.

Hasebe's Theorem 3.5 states that if a monotone-infinitely-divisible probability measure has an isolated atom `a`, then the entire remainder after that atom is absolutely continuous with respect to Lebesgue measure and has support separated from `a`. Since `nu_s` has the further atom `log 3`, it cannot satisfy that conclusion. Therefore, for every `s>0`,

\[
\boxed{\nu_s\text{ is not monotone infinitely divisible.}}
\tag{2}
\]

Anti-monotone convolution is the order reversal of monotone convolution. For repeated copies of one law the reversal disappears: the `m`-fold anti-monotone self-convolution of `rho` equals its `m`-fold monotone self-convolution. Hence monotone and anti-monotone infinite divisibility coincide for a single law, and

\[
\boxed{\nu_s\text{ is not anti-monotone infinitely divisible.}}
\tag{3}
\]

Combining (2)--(3) with `WP-325` and `WP-326` gives a finite synthesis. Within Muraki's five natural products, the direct source-preserving additive-convolution-semigroup strategy has no selective surviving category:

- tensor/classical: the exact source fails even two-divisibility (`WP-325`);
- free: the prime-power support gap makes it freely indecomposable (`WP-326`);
- Boolean: every probability measure is infinitely divisible, so divisibility supplies no arithmetic-selective theorem (`WP-326`);
- monotone: the isolated prime-power atom contradicts Hasebe's structural theorem;
- anti-monotone: self-divisibility is the same as in the monotone category.

Thus

\[
\boxed{
\text{changing only the natural notion of additive independence cannot turn the exact scalar Mangoldt source into the needed selective positive semigroup.}
}
\tag{4}
\]

This is a closure statement only for the **direct source-preserving additive convolution-semigroup architecture under Muraki's natural-product axioms**. It does not exclude operator-valued, conditionally free, bi-free, deformed, multiplicative, non-semigroup, or genuinely geometric constructions. In particular it does not address a finite--archimedean pairing whose positivity comes from geometry rather than probabilistic divisibility.

**Classification:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE + MONOTONE-INFINITE-DIVISIBILITY + ISOLATED-ATOM + ANTI-MONOTONE + MURAKI-FIVE + MATCHED-CONTROL + SOURCE-SEMIGROUP-CLOSURE + NOT-WEIL-POSITIVITY`.

## 1. The canonical source has an isolated left atom for every positive tilt

All coefficients in (1) are strictly positive and the normalization `L(s)` is finite for `s>0`, as established in `WP-325`. Therefore

\[
\operatorname{supp}\nu_s
=
\{k\log p:p\text{ prime},\ k\ge1\}.
\tag{5}
\]

The smallest support point is `log 2`. The next one is `log 3`: indeed `2\log2=\log4>\log3`, and every prime `p>=3` contributes at least `log3`. Hence

\[
\nu_s(\{\log2\})>0,
\qquad
\nu_s(\{\log3\})>0,
\qquad
\nu_s((\log2,\log3))=0.
\tag{6}
\]

So `log2` is isolated in the exact topological sense

\[
\log2\notin
\operatorname{supp}\nu_s\setminus\{\log2\}.
\tag{7}
\]

No estimate for primes, analytic continuation, critical-line input, or limiting argument is used. Positive exponential tilting changes the atomic masses but leaves (5)--(7) unchanged.

Distinct prime powers also give distinct support points: if `p^k=q^ell` for primes `p,q`, unique factorization forces `p=q` and `k=ell`. Thus the atom at `log3` cannot be hidden by a collision with another source component.

## 2. Hasebe's isolated-atom theorem kills monotone infinite divisibility

For a probability measure `mu`, write its reciprocal Cauchy transform as

\[
H_\mu(z)
=
\left(\int_{\mathbb R}\frac{d\mu(x)}{z-x}\right)^{-1}.
\tag{8}
\]

Monotone convolution is characterized by composition,

\[
H_{\mu\triangleright\lambda}
=
H_\mu\circ H_\lambda.
\tag{9}
\]

Hasebe's Theorem 3.5 is exactly tailored to the present support geometry. If a monotone-infinitely-divisible distribution `mu` contains an isolated atom at `a`, then

\[
\mu=\mu(\{a\})\delta_a+\mu_{ac},
\tag{10}
\]

where `mu_ac` is absolutely continuous with respect to Lebesgue measure and `a` is outside its support. In particular, a monotone-infinitely-divisible law cannot have an isolated atom and also a second atom elsewhere.

Apply (10) to `nu_s` and `a=log2`. Equation (6) supplies the second atom `log3` with strictly positive mass. Such a point mass cannot belong to an absolutely continuous remainder, contradicting (10). This proves (2) for every `s>0`.

The conclusion is stronger than a failure of one selected embedding or generator. It rules out monotone infinite divisibility of the exact source law itself. Equivalently, by the monotone Lévy--Khintchine/semigroup correspondence, `nu_s` cannot be a nontrivial time-one law of a weakly continuous monotone convolution semigroup starting at `delta_0`.

## 3. Anti-monotone order reversal gives no separate self-divisibility escape

Monotone independence is order-sensitive. Anti-monotone independence is obtained by reversing that order; correspondingly, if `triangleleft` denotes anti-monotone convolution, then

\[
\mu\triangleleft\lambda
=
\lambda\triangleright\mu.
\tag{11}
\]

For one repeated law `rho`, this reversal cannot distinguish the two products. Let `rho^{\triangleright m}` and `rho^{\triangleleft m}` denote the respective `m`-fold self-convolutions. The claim

\[
\rho^{\triangleleft m}=\rho^{\triangleright m}
\tag{12}
\]

follows by induction. It is trivial for `m=1`; using associativity and (11),

\[
\rho^{\triangleleft(m+1)}
=
\rho^{\triangleleft m}\triangleleft\rho
=
\rho\triangleright\rho^{\triangleright m}
=
\rho^{\triangleright(m+1)}.
\tag{13}
\]

Consequently a measure has an anti-monotone `m`-th self-root exactly when it has a monotone `m`-th self-root. In particular the two infinite-divisibility classes coincide. This agrees with the standard semigroup formulation: monotone and anti-monotone convolution semigroups are the same one-parameter families, with the distinction reappearing only for nonstationary/time-ordered increments.

Equation (2) therefore implies (3) without a second analytic obstruction theorem.

## 4. Synthesis across Muraki's five natural products

Muraki's classification theorem concerns **natural products**: under the canonical universal-product axioms with commutativity dropped, there are exactly five possibilities — tensor, free, Boolean, monotone, and anti-monotone. This is the correct scope for the present closure statement.

The source law `nu_s` has now been tested in every one of those additive categories. The outcomes are structurally different, which is useful diagnostically.

Classical/tensor convolution fails because a hypothetical square root forces support arithmetic incompatible with the first prime-power atoms (`WP-325`). Free convolution fails by the Bercovici--Wang atom-gap indecomposability theorem (`WP-326`). Monotone convolution fails by Hasebe's stronger isolated-atom regularity theorem. Anti-monotone adds no new self-power because it reverses order only. Boolean convolution alone permits all roots, but precisely because **every** probability measure has them.

There is therefore no remaining category in this fivefold classification where the exact scalar source is both divisible and selectively so. Either the prime-power support prevents divisibility, or the category grants it universally.

That dichotomy matters for the README mandate. A semigroup intended to explain Weil positivity would need its nonnegativity to arise independently from a structure that knows something special about the arithmetic source. Universal Boolean divisibility fails that provenance test; the other four natural products cannot even support the proposed exact source semigroup.

## 5. Adversarial controls and what the obstruction does not prove

The monotone obstruction is deliberately tested against a non-arithmetic control. Replace `nu_s` by any discrete probability law with at least two atoms and with one isolated atom — for example a two-point Bernoulli law. Hasebe's theorem rejects monotone infinite divisibility there for the same reason. Thus the theorem is **not an arithmetic positivity theorem**. Its value is narrower: the exact Mathia/Mangoldt source is forced into a generic forbidden support class, so changing the independence category does not rescue the source-semigroup architecture.

The Boolean side supplies the opposite matched control. An arbitrary probability law, arithmetic or not, is Boolean infinitely divisible. Thus the only member of Muraki's five that automatically admits the desired scalar roots is maximally unselective. This prevents the synthesis in (4) from being misread as evidence that some hidden arithmetic theorem has been found.

The support argument is stable under every positive tilt `s>0`, but it is not invariant under arbitrary preprocessing of the source. A nonlinear map, smoothing, dilation mixture, matrix lift, operator-valued enlargement, or coupling to extra degrees of freedom can destroy the isolated atom. Such a move is not ruled out here. It must, however, justify independently why the modified object still carries the exact finite-prime contribution rather than replacing it by a standard divisible completion.

The result also says nothing directly about the archimedean Gamma term, the polar counterterm, or the Weil autocorrelation kernel. It closes a proposed **source-semigroup precursor**, not the global positivity problem itself.

Finally, Muraki's theorem is an axiomatic classification, not a claim that every conceivable noncommutative probability construction belongs to these five categories. Conditionally free/monotone products, bi-free structures, operator-valued variants, tree/deformed convolutions, and non-additive operations lie outside the exact closure statement and must be assessed on their own hypotheses if they become canonical Mathia candidates.

## 6. Prior-art and novelty audit

The theorem doing the monotone work is classical. In the broader preprint `arXiv:1002.3430`, Hasebe defines an isolated atom and states in Theorem 3.5 that a monotone-infinitely-divisible law with such an atom consists of that atom plus an absolutely continuous remainder. The corresponding published work is *Monotone convolution and monotone infinite divisibility from complex analytic viewpoint*, IDAQPRT 13 (2010), no. 1, 111--131. The application to (1) is immediate once the exact support is written down; no novelty is claimed for the analytic theorem.

Muraki's 2003 classification supplies the five-category boundary. It must be kept explicit because saying that the present calculation exhausts “noncommutative convolution” would be false. The exact claim is exhaustion of the direct additive source-semigroup escape **inside the five natural products**.

The monotone/anti-monotone order-reversal relation is also standard. Jekel's treatment of noncommutative evolution equations records both the reversal relation and the fact that monotone and anti-monotone convolution semigroups coincide. Equation (13) gives the elementary self-power proof needed here, so the anti-monotone conclusion does not depend on an unproved analogy.

The Mathia-specific delta is the synthesis with the exact pole-normalized Mangoldt source and the preceding `WP-325`/`WP-326` obstructions. The first prime-power gap is not merely a free-convolution problem: its left endpoint is an isolated atom that triggers the monotone theorem as well. With anti-monotone reduced to the same self-powers and Boolean exposed as universal, there is no unresolved Muraki-natural independence category left for this particular semigroup architecture.

No claim is made that this advances RH directly or produces a Weil-positive form.

## Consequence for the research line

The direct scalar source-semigroup search should no longer spend effort switching among the five natural additive notions of independence. That candidate family is now exhausted at the level required by the README's falsification standard.

A surviving route must change more than the convolution law. It must introduce a canonical geometric/operator structure — for example a nonseparable finite--archimedean coupling, quotient/compression, boundary response, cohomological pairing, or other Mathia-native construction — whose **own** sign theorem survives matched controls and whose local-to-global decomposition reproduces both the prime contribution and the archimedean/global counterterms.

That is exactly the distinction the line mandate requires: the next useful mechanism must explain global Weil-type positivity geometrically, not manufacture a different probabilistic semigroup around already-extracted arithmetic coefficients.
