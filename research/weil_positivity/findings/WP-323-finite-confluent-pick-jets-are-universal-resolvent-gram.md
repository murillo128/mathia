---
id: WP-323
title: Finite confluent scalar Pick jets are universal resolvent Grams, not arithmetic-selective positivity
branch: weil_positivity
status: supported
kind: finite-confluent-pick-jet-universality-obstruction
claim_strength: exact finite-jet extension of WP-322 for scalar Herglotz sources; every finite collection of boundary Pick-kernel derivatives at regular real nodes is a Gram matrix of higher resolvent vectors, so all positivity inherited from finite confluent Pick matrices, their principal minors, and their Schur-complement reductions holds for every positive scalar Herglotz measure and cannot by itself be an arithmetic-selective Weil sign theorem
created: 2026-09-15
related: [WP-304, WP-312, WP-317, WP-318, WP-321, WP-322]
prior_art:
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for boundary Pick matrices and Julia-Nevanlinna reduction by Schur complementation
  - Jim Agler, Zinaida A. Lykova, and N. J. Young, The boundary Caratheodory-Fejer interpolation problem, Journal of Mathematical Analysis and Applications 382 (2011), no. 2, 645-662, DOI 10.1016/j.jmaa.2011.04.071, arXiv:1011.1399, for finite boundary derivative interpolation in the Pick class
  - Jim Agler, Zinaida A. Lykova, and N. J. Young, Pseudo-Taylor expansions and the Caratheodory-Fejer problem, Journal of Mathematical Analysis and Applications 386 (2012), no. 1, 308-318, DOI 10.1016/j.jmaa.2011.08.001, arXiv:1101.1251, for boundary jet solvability criteria and their positive Hankel matrices
---

# WP-323 — Finite confluent scalar Pick jets are universal resolvent Grams, not arithmetic-selective positivity

## Claim

`WP-322` closes the most canonical exact multipoint escape from the scalar Herglotz/Julia route: first-order boundary Loewner matrices at any finite family of regular arithmetic gap nodes are universal resolvent Grams. A natural remaining objection is that first-order data may be too coarse. Exact higher derivatives at the same arithmetic nodes retain progressively sharper local information about the atomic source, so perhaps a **confluent** Pick or Caratheodory-Fejer positivity condition could become source-selective even though the ordinary multipoint Pick matrix is not.

It does not. Every finite confluent Pick-kernel matrix has an exact higher-resolvent Gram factorization for every positive scalar Herglotz measure.

Let

\[
f(z)=az+b+\int_{\mathbb R}
\left(\frac1{x-z}-\frac{x}{1+x^2}\right)d\mu(x),
\qquad a\ge 0,\quad b\in\mathbb R,\quad \mu\ge0,
\tag{1}
\]

and let

\[
K_f(z,w):=\frac{f(z)-\overline{f(w)}}{z-\overline w}.
\tag{2}
\]

Choose finitely many distinct regular real nodes `t_1,...,t_m`. At node `t_i` choose a finite jet order `R_i>=0`, and assume the required boundary resolvent moments exist,

\[
\int_{\mathbb R}\frac{d\mu(x)}{|x-t_i|^{2(r+1)}}<\infty,
\qquad 0\le r\le R_i.
\tag{3}
\]

For the index set

\[
\mathcal I=\{(i,r):1\le i\le m,\ 0\le r\le R_i\},
\tag{4}
\]

define the normalized confluent Pick matrix

\[
C_{(i,r),(j,s)}
:=\left.
\frac1{r!s!}
\partial_z^r\partial_{\overline w}^{\,s}K_f(z,w)
\right|_{z=t_i,w=t_j}.
\tag{5}
\]

Then exactly

\[
\boxed{
C_{(i,r),(j,s)}
=
a\,\delta_{r0}\delta_{s0}
+\int_{\mathbb R}
\frac{d\mu(x)}
{(x-t_i)^{r+1}(x-t_j)^{s+1}}.
}
\tag{6}
\]

Hence, with

\[
v_{i,r}
=\left(
\delta_{r0}\sqrt a,
\frac1{(x-t_i)^{r+1}}
\right)
\in\mathbb C\oplus L^2(\mu),
\tag{7}
\]

we have

\[
\boxed{
C_{(i,r),(j,s)}=\langle v_{i,r},v_{j,s}\rangle,
\qquad C\succeq0.
}
\tag{8}
\]

No prime, prime-power, Mangoldt, Gamma, or functional-equation input enters the sign theorem. The source can affect every numerical entry of the jet matrix, but **the reason the matrix is positive is universal scalar Pick geometry**.

For the reflected Mangoldt Herglotz source used in `WP-318`--`WP-322`, exact gap-node derivatives of arbitrary fixed finite order therefore do not provide the missing independent arithmetic positivity. Principal minors and any positivity obtained only by Schur-complementing this finite confluent matrix remain positive for the same reason for arbitrary positive scalar Herglotz controls.

This closes only the finite **Pick-kernel jet** escape. It does not classify arbitrary nonlinear invariants of exact support and masses, infinite-order jets, infinite-node operator-domain phenomena, matrix/operator-valued Herglotz geometry, or genuinely nonseparable finite--archimedean constructions.

**Classification:** `EXACT-DERIVED + CLASSICAL-PICK/CARATHEODORY-FEJER + NEGATIVE/OBSTRUCTION + FINITE-CONFLUENT-JETS + RESOLVENT-GRAM + MATCHED-CONTROL + NOT-WEIL-POSITIVITY`.

## 1. Exact higher-resolvent factorization

The Herglotz representation gives the standard positive Pick-kernel factorization

\[
K_f(z,w)
=a+\int_{\mathbb R}
\frac{d\mu(x)}{(x-z)(x-\overline w)}.
\tag{9}
\]

For every integer `r>=0`,

\[
\frac1{r!}\partial_z^r\frac1{x-z}
=\frac1{(x-z)^{r+1}},
\tag{10}
\]

and likewise

\[
\frac1{s!}\partial_{\overline w}^{\,s}
\frac1{x-\overline w}
=\frac1{(x-\overline w)^{s+1}}.
\tag{11}
\]

Under (3), Cauchy--Schwarz controls every mixed integral and allows the finite boundary differentiation. Applying (10)--(11) to (9) gives (6) directly. Equation (8) is then immediate.

Thus confluence does not create a new positive object. It only replaces the first resolvent vectors of `WP-322`,

\[
(x-t_i)^{-1},
\tag{12}
\]

by the finite family of higher resolvent vectors

\[
(x-t_i)^{-1},(x-t_i)^{-2},\ldots,(x-t_i)^{-(R_i+1)}.
\tag{13}
\]

The full exact finite jet is still ordinary Hilbert-space Gram geometry.

## 2. The reflected Mangoldt source satisfies every fixed finite jet condition in a support gap

For the source of `WP-318`,

\[
\mu_{\rm M}
=\sum_{q=p^k}
\frac{\Lambda(q)}{q+1}\,\delta_{-\log q},
\tag{14}
\]

a real node inside a support gap has positive distance from the nearby atoms. For the remote tail, a fixed `r` gives summands of size

\[
\frac{\Lambda(q)}{q+1}\,
\frac1{|\log q+t|^{2(r+1)}}.
\tag{15}
\]

The prime-power tail converges already for `r=0`: its prime contribution is comparable to

\[
\sum_p\frac1{p\log p}<\infty,
\tag{16}
\]

and higher `r` only improves convergence; powers `k>=2` are absolutely smaller. Therefore every exact arithmetic gap node admits every **fixed finite** confluent order used above.

Consequently this is not a vacuous regularity obstruction. The finite jet matrices genuinely exist on the arithmetic source and can contain exact high-order local fingerprints of the prime-power support. What fails is the stronger requirement of the research mandate: their positive sign does not originate in that fingerprint.

## 3. Strict positivity is also generic for infinite positive support

One might try to rescue arithmetic selectivity by replacing semidefinite positivity with nonvanishing of confluent determinants. That also fails as a generic sign discriminator.

Assume for simplicity `a=0`, the positive measure has infinitely many distinct support points, and all chosen nodes are outside the support with the required moments finite. If a finite linear combination of the Gram vectors vanishes in `L^2(mu)`, then

\[
R(x):=
\sum_{i=1}^m\sum_{r=0}^{R_i}
\frac{c_{i,r}}{(x-t_i)^{r+1}}
=0
\quad \mu\text{-a.e.}
\tag{17}
\]

The rational function `R` therefore vanishes at infinitely many support points. Multiplying by

\[
D(x)=\prod_{i=1}^m(x-t_i)^{R_i+1}
\tag{18}
\]

gives a polynomial with infinitely many zeros, hence the zero polynomial. Uniqueness of partial fractions then forces every coefficient `c_{i,r}` to vanish. Thus

\[
\boxed{C\succ0}
\tag{19}
\]

for every finite confluent family under these hypotheses.

The reflected Mangoldt measure has infinite support, so its finite confluent determinants are strictly positive. But the same conclusion holds for arbitrary non-arithmetic positive measures with infinite support. Strictness therefore does not supply the missing source-selective theorem either.

## 4. Matched controls are exact, not asymptotic

`WP-319`--`WP-321` constructed increasingly strong same-source or smoothed controls for gap-adapted Julia laws. Here no approximation is required. Let `mu_ctrl` be any positive scalar Herglotz measure for which the same finite real nodes and jet orders satisfy (3). Then its matrix is

\[
C^{\rm ctrl}_{(i,r),(j,s)}
=a_{\rm ctrl}\delta_{r0}\delta_{s0}
+\int
\frac{d\mu_{\rm ctrl}(x)}
{(x-t_i)^{r+1}(x-t_j)^{s+1}}
\succeq0.
\tag{20}
\]

No matching of entries is needed to falsify the proposed sign mechanism. Arithmetic and non-arithmetic sources inhabit the same positive cone because the cone is generated by resolvent jets of **every** positive measure.

A stronger matched control is any infinite discrete set of non-prime locations with arbitrary positive masses satisfying (3). Equation (19) then gives the same strict positivity of every finite confluent determinant. Exact atomicity and exact finite-jet coherence therefore do not make the Pick sign arithmetic-selective.

## 5. Relation to classical boundary Caratheodory-Fejer theory

Finite boundary derivative interpolation in the Pick class is classical Caratheodory-Fejer theory. Agler--Lykova--Young give boundary derivative solvability criteria and associated positive Hankel matrices, and analyze Julia--Nevanlinna reduction of such jet data. Agler--Young likewise identify boundary Julia reduction with Schur complementation of Pick matrices.

No novelty is claimed here for positivity of confluent Pick matrices, boundary Caratheodory-Fejer interpolation, or reduction/augmentation. The exact formula (6) is simply the Herglotz-measure specialization that makes the matched-control issue transparent for the live Mathia source.

The line-specific contribution is narrower: after `WP-322` leaves exact higher derivatives as the immediate finite scalar escape, (6)--(8) show that **raising the finite jet order cannot change the provenance of positivity**. It adds source information to the coordinates while leaving the sign theorem universal.

This distinction is essential. A finite jet may identify or constrain an arithmetic source numerically. That is a source fingerprint. The `weil_positivity` mandate instead asks for a source-forced geometric sign theorem. A positive matrix whose sign is automatic throughout the full positive Herglotz class does not provide one.

## 6. Adversarial checks and boundaries

1. **The factorial normalization matters only for coordinates.** Equations (10)--(11) show that the chosen normalization removes factorials and exposes the exact Gram vectors. Any positive diagonal rescaling of jet coordinates gives a congruent positive matrix and cannot create arithmetic selectivity.

2. **Odd powers do not create a sign problem.** Individual mixed integrands in (6) can have either sign when the nodes lie on different sides of a source atom. Positivity is not termwise; it is the Gram identity (8).

3. **This does not say all algebraic functions of jets are positive.** The obstruction applies when the proposed sign is the canonical finite confluent Pick-kernel positivity, a principal-minor consequence, or a Schur-complement consequence of that positive matrix. A nonlinear support-sensitive invariant not reducible to this cone is outside the claim.

4. **Finite atomic sources can be rank deficient.** If `mu` has too few atoms, the Gram rank is bounded by the source dimension (plus the affine coordinate). That does not help the Mangoldt route: its source is infinite, and rank deficiency of specially chosen finite controls is not an arithmetic sign theorem.

5. **Infinite jets are a genuine category change.** The proof treats a finite set of nodes and finitely many derivatives at each node. An infinite confluent matrix raises closability, domain, and completion questions not decided by finite-section positivity, exactly as the infinite-node caveat in `WP-322` does.

6. **No archimedean completion appears.** The construction still starts solely from a positive scalar Herglotz measure. It neither generates the Riemann Gamma term nor the polar/global counterterms. Adding those terms by hand would violate the line's source-native requirement.

7. **No RH or zero data are used.** This makes the no-go independent of the desired conclusion. The failure is that the positive theorem is too universal, not that positivity is difficult to prove.

## Consequence for the research line

The finite scalar Pick frontier is now closed one step further. `WP-322` classifies exact values and first derivatives at arbitrarily many regular nodes as a universal resolvent Gram. The present result shows that allowing any fixed finite collection of higher derivatives merely enlarges that Gram to higher resolvent powers:

\[
\boxed{
\text{finite scalar confluent Pick positivity}
=
\text{finite higher-resolvent Gram positivity}.
}
\tag{21}
\]

Therefore the next scalar test should not be another finite Caratheodory-Fejer determinant, higher-order Pick minor, or finite jet Schur complement at prime-power gaps. A viable scalar route must use an exact support-sensitive sign invariant that is **not** automatic for arbitrary positive Herglotz measures, or exploit a genuinely infinite-domain phenomenon whose operator theorem adds source-specific structure. Otherwise the search should change category to matrix/operator-valued geometry or to a direct finite--archimedean construction with an independent sign theorem.

This remains a negative result for the primary question. It materially narrows the live scalar support-side route without confusing increasingly precise arithmetic coordinates with an arithmetic origin of positivity.

## References

- Jim Agler and N. J. Young, *Boundary Nevanlinna-Pick interpolation via reduction and augmentation*, Mathematische Zeitschrift 268 (2011), 791--817, DOI `10.1007/s00209-010-0696-3`, arXiv:`0905.4759`.
- Jim Agler, Zinaida A. Lykova, and N. J. Young, *The boundary Caratheodory-Fejer interpolation problem*, Journal of Mathematical Analysis and Applications 382 (2011), no. 2, 645--662, DOI `10.1016/j.jmaa.2011.04.071`, arXiv:`1011.1399`.
- Jim Agler, Zinaida A. Lykova, and N. J. Young, *Pseudo-Taylor expansions and the Caratheodory-Fejer problem*, Journal of Mathematical Analysis and Applications 386 (2012), no. 1, 308--318, DOI `10.1016/j.jmaa.2011.08.001`, arXiv:`1101.1251`.
