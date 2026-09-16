---
id: WP-326
title: Prime-power gaps make every Mangoldt tilt freely indecomposable while Boolean divisibility is universal
branch: weil_positivity
status: supported
kind: noncommutative-convolution-semigroup-obstruction
claim_strength: exact literature-backed application of free-convolution gap indecomposability to every positive Laplace tilt of the pole-normalized Mangoldt source, both additively in log-energy and multiplicatively after exponentiation, paired with the universal Boolean infinite-divisibility matched control
created: 2026-09-16
related: [WP-318, WP-304, WP-324, WP-325]
prior_art:
  - Hari Bercovici and Jiun-Chau Wang, On freely indecomposable measures, Indiana University Mathematics Journal 57 (2008), no. 6, 2601-2610, DOI 10.1512/iumj.2008.57.3662, arXiv:0710.1295, especially Theorems 2.5 and 3.2 on additive and positive multiplicative free indecomposability from an atom-to-atom support gap
  - Roland Speicher and Reza Woroudi, Boolean convolution, Fields Institute Communications 12 (1997), 267-279, DOI 10.1090/fic/012/13, for Boolean K-transform linearization and the universal Boolean infinite divisibility of probability measures
---

# WP-326 — Prime-power gaps make every Mangoldt tilt freely indecomposable while Boolean divisibility is universal

## Claim

`WP-325` rules out the ordinary classical convolution-semigroup escape for the positive pole-normalized Mangoldt source: every positive exponential tilt of its prime-power carrier fails even two-divisibility. A natural category change is to replace classical independence by a noncommutative notion of independence and ask whether the same exact source law can become the time-one state of a positive convolution semigroup.

For the two canonical transforms already adjacent to the Mathia scalar geometry, free and Boolean convolution give opposite but equally decisive answers.

Let

\[
\nu_s
=
\frac1{L(s)}
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}n^{-s}\,\delta_{\log n},
\qquad s>0,
\tag{1}
\]

be the probability law from `WP-325`. Then for every `s>0`,

\[
\boxed{\nu_s\text{ is freely indecomposable under additive free convolution.}}
\tag{2}
\]

If instead the energy coordinate is exponentiated,

\[
\eta_s:=(\exp)_*\nu_s
=
\frac1{L(s)}
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}n^{-s}\,\delta_n,
\tag{3}
\]

then for every `s>0`,

\[
\boxed{\eta_s\text{ is freely indecomposable under multiplicative free convolution on }\mathbb R_+.}
\tag{4}
\]

Both statements follow immediately, but nontrivially, from the Bercovici--Wang gap theorem. The first two atoms are `log 2<log 3` in (1), respectively `2<3` in (3), and the open interval between them has zero mass. Bercovici--Wang prove that a probability measure with two atomic endpoints and no mass between them cannot be a nontrivial free additive convolution; they prove the analogous theorem for free multiplicative convolution on the positive half-line.

Consequently neither `nu_s` nor `eta_s` can be freely infinitely divisible. In particular, no source-preserving free additive or positive multiplicative convolution semigroup can have the exact Mangoldt tilt as a nontrivial time-one law.

The Boolean alternative goes in the opposite direction. For the convention already used in `WP-318`,

\[
G_\mu(z)=\int\frac{d\mu(x)}{z-x},
\qquad
K_\mu(z)=z-\frac1{G_\mu(z)},
\tag{5}
\]

Boolean additive convolution linearizes `K`:

\[
K_{\mu\uplus\lambda}=K_\mu+K_\lambda.
\tag{6}
\]

Every probability measure is Boolean infinitely divisible, so for every `t>0` there is a Boolean power with

\[
K_{\mu^{\uplus t}}=tK_\mu.
\tag{7}
\]

Hence the exact source law `nu_s` does admit a Boolean convolution semigroup, but **for the universal reason that every probability law does**. This gives no arithmetic-selective sign theorem and is the semigroup analogue of the universal Boolean self-energy classification already found in `WP-318`.

Thus the two closest noncommutative convolution escapes from `WP-325` separate cleanly:

\[
\boxed{
\text{free convolution preserves selectivity too rigidly and the gapped source is indecomposable,}
}
\tag{8}
\]

while

\[
\boxed{
\text{Boolean convolution always supplies divisibility, so its positivity is matched-control universal.}
}
\tag{9}
\]

This does not rule out every noncommutative or operator-valued construction. It rules out the direct source-preserving free additive/multiplicative semigroup and the direct Boolean divisibility mechanism as explanations of Weil positivity. A surviving noncommutative route must introduce additional canonical structure whose sign is neither forbidden by the prime-power gaps nor automatic for arbitrary positive laws, and it must still generate the finite-prime and archimedean/global pieces of the Weil form.

**Classification:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIME-POWER-GAP + FREE-INDECOMPOSABLE + ADDITIVE-FREE + MULTIPLICATIVE-FREE + BOOLEAN-INFINITE-DIVISIBILITY + UNIVERSAL-MATCHED-CONTROL + NONCOMMUTATIVE-CONVOLUTION + NOT-WEIL-POSITIVITY`.

## 1. The exact gap survives every positive Mangoldt tilt

All coefficients in (1) are strictly positive. Exponential tilting changes their masses but not their support, so

\[
\operatorname{supp}\nu_s
=
\{\log(p^k):p\text{ prime},\ k\ge1\}
\tag{10}
\]

for every `s>0`. In particular,

\[
\nu_s(\{\log2\})>0,
\qquad
\nu_s(\{\log3\})>0,
\qquad
\nu_s((\log2,\log3))=0.
\tag{11}
\]

No asymptotic information about primes is involved. The obstruction is already visible in the first support gap and is invariant under every admissible positive tilt.

Exponentiating is a bijective change of coordinate from the support in (10) to the positive prime-power carrier. Hence

\[
\operatorname{supp}\eta_s
=
\{p^k:p\text{ prime},\ k\ge1\},
\tag{12}
\]

with

\[
\eta_s(\{2\})>0,
\qquad
\eta_s(\{3\})>0,
\qquad
\eta_s((2,3))=0.
\tag{13}
\]

This second formulation matters because one might hope that multiplicative free convolution is more natural for arithmetic than additive free convolution in logarithmic energy. The same gap theorem blocks both.

## 2. Bercovici--Wang makes the additive free obstruction exact

Bercovici--Wang Theorem 2.5 states that if `alpha<beta` are atoms of a free additive convolution

\[
\mu_1\boxplus\mu_2
\tag{14}
\]

and the convolution has no mass in `(alpha,beta)`, then one of `mu_1,mu_2` is a point mass. Equivalently, any probability measure possessing such an atom-to-atom gap is freely indecomposable up to the trivial translation factors represented by point masses.

Apply the theorem to `nu_s` with

\[
\alpha=\log2,
\qquad
\beta=\log3.
\tag{15}
\]

Equation (11) verifies the hypotheses exactly. Therefore every factorization

\[
\nu_s=\rho_1\boxplus\rho_2
\tag{16}
\]

has a point-mass factor.

If `nu_s` were freely infinitely divisible, it would in particular possess a free square root `rho` satisfying

\[
\nu_s=\rho\boxplus\rho.
\tag{17}
\]

Theorem 2.5 would force `rho` to be a point mass, making `nu_s` itself a point mass, contrary to the positive atoms at both `log2` and `log3`. Hence (2) and the failure of additive free infinite divisibility follow.

This is stronger than merely transporting the classical contradiction from `WP-325`. The classical proof there constructs a forbidden forced atom at `log(9/2)`. Free convolution does not add supports by ordinary Minkowski addition, so that proof does not transfer. The analytic-subordination theorem of Bercovici--Wang supplies the genuinely free replacement: the **gap itself** is enough to forbid any nontrivial free factorization.

## 3. The multiplicative free escape is blocked in the arithmetic coordinate as well

Bercovici--Wang Theorem 3.2 gives the positive multiplicative analogue. If `alpha<beta` are positive atoms of

\[
\mu_1\boxtimes\mu_2
\tag{18}
\]

and there is no mass in `(alpha,beta)`, then one factor is a point mass.

Applying the theorem to `eta_s` with `alpha=2`, `beta=3` and (13) proves (4). As before, a hypothetical multiplicative free square root

\[
\eta_s=\rho\boxtimes\rho
\tag{19}
\]

would force `rho` to be a point mass and therefore `eta_s` to be a point mass, contradiction.

This closes a natural coordinate objection to (2). The obstruction is not an artifact of taking logarithms before invoking free independence: the exact prime-power law is freely indecomposable in the native positive multiplicative coordinate too.

## 4. Boolean divisibility exists but is maximally nonselective

The same family already met Boolean probability in `WP-318`, where regular scalar Julia responses were classified as scaled negative Boolean self-energies. The relevant transform is precisely (5). Boolean convolution satisfies (6), so its convolution roots are obtained by scalar division of the `K`-transform.

The classical Speicher--Woroudi theory proves that every probability measure on the real line is Boolean infinitely divisible. In particular, for every integer `m>=2`, there is a probability `rho_m` with

\[
K_{\rho_m}=\frac1mK_{\nu_s},
\qquad
\nu_s=\rho_m^{\uplus m}.
\tag{20}
\]

Nothing in (20) uses prime powers, Mangoldt weights, the exact gap, or the zeta function. Replacing `nu_s` by an arbitrary non-arithmetic probability law leaves the same theorem intact. Thus Boolean infinite divisibility fails the README's matched-control test at the sign-provenance stage: the positive semigroup structure is already present for the whole comparison class.

This is not a contradiction with free indecomposability. Free and Boolean convolution encode different notions of noncommutative independence and are linearized by different analytic transforms. Here that difference is diagnostically useful: the exact same source is **too rigid** for free factorization and **automatically divisible** for Boolean factorization.

## 5. Adversarial controls and boundaries

The free obstruction does not use the values of the masses beyond positivity. Therefore it is not itself a uniquely arithmetic sign theorem: any probability law with two atomic endpoints and an empty interval between them is a matched free-indivisibility control. The arithmetic content is that the exact Mangoldt carrier necessarily lies in this rigid class for every positive tilt.

Point-mass factors do not rescue the route. Under additive free convolution they only translate the law, and under positive multiplicative free convolution they only rescale it. Infinite divisibility would require identical nontrivial roots at every order, so the Bercovici--Wang conclusion already contradicts divisibility for the nondegenerate laws (1) and (3).

The result also does **not** prove that every free-probabilistic construction from the Mangoldt source is useless. It leaves logically open operator-valued free convolution, transforms that first change the source law, monotone or conditionally free notions of independence, and non-semigroup free constructions. But any such escape must pay for the change: if a preprocessing map fills the support gap or replaces the source by a freely divisible law, the new positivity must be shown to retain the exact finite-prime information and to fail on appropriate non-arithmetic controls rather than merely manufacturing a standard freely infinitely divisible completion.

Likewise, Boolean convolution could still participate in a larger construction, but its divisibility or `K`-transform positivity cannot be the independent arithmetic sign theorem. `WP-318` and the universal statement (7) together make that provenance failure exact.

Finally, neither side produces the archimedean Gamma term, the polar/global counterterm, or the full Weil autocorrelation structure. The finding is therefore a route restriction, not a partial proof of Weil positivity.

## 6. Prior-art and novelty audit

The free indecomposability theorem is classical prior art, not a Mathia theorem. Bercovici and Wang prove exactly the atom-gap criterion used above for additive free convolution and its positive multiplicative analogue by analytic subordination. A bounded literature search on free infinite divisibility, atoms, support gaps, and free multiplicative convolution therefore redirects the candidate immediately to their Theorems 2.5 and 3.2 rather than supporting a novelty claim.

Boolean `K`-transform linearization and universal Boolean infinite divisibility are likewise classical, originating in Speicher--Woroudi. `WP-318` had already identified the same transform as the exact normal form of scalar Julia tangents, so the Boolean half of the present result is a deliberate matched-control reuse, not a new probability theorem.

The Mathia-specific delta is the joint application to the exact pole-normalized Mangoldt tilt isolated in `WP-304` and sharpened in `WP-325`: the first prime-power gap simultaneously forbids both additive and multiplicative **free** source-preserving semigroups, while the closest Boolean semigroup is available for every probability source. This sharply narrows the obvious noncommutative-convolution category change left open after classical infinite divisibility failed.

No claim is made that free or Boolean probability in general is exhausted, nor that this obstruction is equivalent to a Weil criterion.

## Consequence for the research line

After `WP-325`, changing the notion of independence does not by itself rescue the source-semigroup program. The exact prime-power carrier cannot be the state of a nontrivial free additive semigroup in log-energy or a free multiplicative semigroup in the native positive coordinate, while Boolean divisibility is universal and therefore supplies no source-selective sign.

A viable noncommutative route must therefore contain **more than a convolution law on the existing scalar source**. It needs a canonical operator/matrix/global coupling whose positive theorem depends on arithmetic structure beyond the mere existence of the prime-power gap, survives matched controls, and simultaneously retains or derives the finite-prime and archimedean/global terms required by the Weil form. Otherwise the route lands on one of the two failure modes isolated here: impossible factorization or automatic positivity.
