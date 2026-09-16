---
id: WP-328
title: Free scalar shadows block direct bi-free and c-free source lifts while the degenerate c-free lift is universal
branch: weil_positivity
status: supported
kind: enriched-convolution-shadow-obstruction
claim_strength: exact derived semigroup-shadow obstruction with literature-backed applications to bi-free and conditionally free additive convolution of the pole-normalized Mangoldt source
created: 2026-09-16
related: [WP-318, WP-325, WP-326, WP-327]
prior_art:
  - Dan-Virgil Voiculescu, Free Probability for Pairs of Faces I, Communications in Mathematical Physics 332 (2014), no. 3, 955-980, DOI 10.1007/s00220-014-2060-7
  - Takahiro Hasebe, Hao-Wei Huang, and Jiun-Chau Wang, Limit theorems in bi-free probability theory, Probability Theory and Related Fields 172 (2018), no. 3-4, 1081-1119, DOI 10.1007/s00440-017-0825-6, arXiv:1705.05523
  - Marek Bozejko, Michael Leinert, and Roland Speicher, Convolution and limit theorems for conditionally free random variables, Pacific Journal of Mathematics 175 (1996), no. 2, 357-388, DOI 10.2140/pjm.1996.175.357, arXiv:funct-an/9410004
  - Mihai Popa and Victor Vinnikov, Non-commutative functions and the non-commutative free Levy-Hincin formula, Advances in Mathematics 236 (2013), 131-157, DOI 10.1016/j.aim.2012.12.013, arXiv:1007.1932
---

# WP-328 — Free scalar shadows block direct bi-free and c-free source lifts while the degenerate c-free lift is universal

## Claim

`WP-327` closes the direct scalar source-preserving additive semigroup route across Muraki's five natural products, but deliberately leaves richer two-faced, two-state, and operator-valued probability categories open. The first two natural enlargements — bi-free and conditionally free additive convolution — can now be separated by a simple exact principle.

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

be the pole-normalized Mangoldt probability law used in `WP-325`--`WP-327`. By `WP-326`, `nu_s` has no nontrivial free square root, hence is not freely infinitely divisible.

The elementary structural observation is that **divisibility descends through every semigroup homomorphism**. If

\[
F:(\mathcal C,\diamond)\longrightarrow(\mathcal P,*)
\tag{2}
\]

satisfies `F(X diamond Y)=F(X)*F(Y)`, then

\[
X=Y^{\diamond m}
\quad\Longrightarrow\quad
F(X)=F(Y)^{*m}.
\tag{3}
\]

Therefore a scalar law with no `m`-th root under `*` cannot be the homomorphic scalar shadow of an `m`-divisible enriched object.

Applied to the two closest enlargements left open by `WP-327`, this gives:

1. **Bi-free marginal obstruction.** Under additive bi-free convolution of planar laws, each coordinate marginal free-convolves. Consequently no bi-freely infinitely divisible planar law can have `nu_s` as either its left or right marginal.

2. **C-free reference obstruction.** Under additive conditionally free convolution of pairs `(mu,nu)`, the second/reference coordinate free-convolves. Consequently no c-freely infinitely divisible pair can have `nu_s` as its reference law.

3. **Degenerate c-free universality.** The opposite placement does not produce arithmetic selectivity. When the reference laws are `delta_0`, c-free convolution of the first coordinates reduces exactly to Boolean convolution:

\[
(\mu_1,\delta_0)\boxplus_c(\mu_2,\delta_0)
=
(\mu_1\uplus\mu_2,\delta_0).
\tag{4}
\]

Since every probability measure is Boolean infinitely divisible, **every** scalar probability law `mu` — arithmetic or not — has the c-free infinitely divisible lift `(mu,delta_0)`. In particular `(nu_s,delta_0)` is c-freely infinitely divisible for a completely universal reason.

Thus merely adding a second face or second state does not rescue the direct source-semigroup program. If the exact Mangoldt source is retained as a free scalar shadow, divisibility is impossible; if it is placed in the degenerate c-free outer coordinate, divisibility is automatic for all sources and supplies no selective sign theorem.

The surviving two-face/two-state possibility must therefore put essential arithmetic information in **genuinely mixed coupling data** that is not recoverable as a homomorphic scalar free shadow, and that mixed data must itself generate a nonautomatic positive theorem together with the archimedean and polar/global terms. This finding does not rule out that harder possibility, general operator-valued free convolution, or non-semigroup geometric constructions.

**Classification:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + SEMIGROUP-SHADOW + BI-FREE + C-FREE + FREE-MARGINAL-OBSTRUCTION + BOOLEAN-UNIVERSALITY + MATCHED-CONTROL + NOT-WEIL-POSITIVITY`.

## 1. Divisibility cannot be created above a homomorphic shadow

The reusable lemma is purely algebraic.

Let `(C,diamond)` and `(P,*)` be semigroups and let `F:C->P` be a semigroup homomorphism. For every integer `m>=2`, induction gives

\[
F(Y^{\diamond m})=F(Y)^{*m}.
\tag{5}
\]

Hence if `X` has an `m`-th `diamond`-root `Y`, then `F(X)` has the `m`-th `*`-root `F(Y)`. Contrapositively,

\[
F(X)\text{ has no }m\text{-th }*\text{-root}
\quad\Longrightarrow\quad
X\text{ has no }m\text{-th }\diamond\text{-root}.
\tag{6}
\]

Infinite divisibility is therefore impossible upstairs whenever one homomorphic shadow already fails a required root downstairs.

This observation is intentionally weaker than claiming that an enriched convolution is determined by its scalar shadows. It uses only functoriality of one projection. The enriched object may carry arbitrarily rich mixed information; that information simply cannot repair divisibility while the obstructed scalar shadow remains fixed and homomorphic.

For the source (1), `WP-326` supplies the downstairs input. The atoms at `log 2` and `log 3` with the empty interval between them trigger the Bercovici--Wang free indecomposability theorem. In particular there is no probability law `rho` with

\[
\nu_s=\rho\boxplus\rho.
\tag{7}
\]

Equation (6) can therefore be applied to every enriched additive convolution whose canonical shadow is ordinary free convolution.

## 2. A bi-free semigroup cannot keep the Mangoldt source as a face marginal

Voiculescu's bi-free probability attaches left and right faces to one noncommutative probability space. Restricting a bi-free family to only its left faces, or only its right faces, recovers ordinary freeness. Analytically, the bi-free partial `R`-transform contains the ordinary one-variable `R`-transforms of the two marginals; additivity of the bi-free transform therefore implies additivity of each marginal free transform.

For planar Borel laws, write `boxplusboxplus` for additive bi-free convolution and `pi_L, pi_R` for the two coordinate marginals. Then

\[
\pi_L(M_1\boxplus\!\boxplus M_2)
=
\pi_L(M_1)\boxplus\pi_L(M_2),
\tag{8}
\]

and likewise

\[
\pi_R(M_1\boxplus\!\boxplus M_2)
=
\pi_R(M_1)\boxplus\pi_R(M_2).
\tag{9}
\]

The general-Borel formulation matters because (1) has unbounded support. Hasebe--Huang--Wang develop additive bi-free convolution and bi-free infinite divisibility for general Borel probability measures, so no compact-support shortcut is being used here.

Suppose a planar law `M` has

\[
\pi_L(M)=\nu_s
\tag{10}
\]

and admits a bi-free square root `R`:

\[
M=R\boxplus\!\boxplus R.
\tag{11}
\]

Applying (8) gives

\[
\nu_s
=
\pi_L(R)\boxplus\pi_L(R),
\tag{12}
\]

contradicting (7). The same argument using (9) applies if `nu_s` is the right marginal. Therefore

\[
\boxed{
\text{no bi-freely infinitely divisible planar law has }\nu_s
\text{ as either coordinate marginal.}
}
\tag{13}
\]

The obstruction is stronger than saying that one particular bi-free generator has not been found. It rules out every additive bi-free semigroup that preserves the exact source as a face marginal.

It does **not** rule out a construction in which both scalar marginals are freely divisible auxiliary laws while the arithmetic source is encoded only in mixed left--right cumulants, a boundary pairing, or another genuinely joint observable. Such a construction evades the map used in (8)--(9), but it must then prove that its mixed data recover the exact prime contribution canonically rather than hiding the desired coefficients by hand.

## 3. The reference coordinate of c-free convolution is blocked for the same reason

Conditionally free probability starts with two states, conventionally written `(phi,psi)`. For scalar laws we write the corresponding pair as `(mu,nu)`, with `mu` the outer/`phi` distribution and `nu` the reference/`psi` distribution.

The defining c-free product makes the component algebras free with respect to the reference state `psi`. Consequently the reference distribution under additive c-free convolution is the ordinary free convolution:

\[
\pi_2\bigl((\mu_1,\nu_1)\boxplus_c(\mu_2,\nu_2)\bigr)
=
\nu_1\boxplus\nu_2.
\tag{14}
\]

This is exactly the homomorphic-shadow situation (2). If a c-free pair `X=(mu,nu_s)` had a c-free square root `Y=(rho,tau)`, then

\[
\nu_s=\tau\boxplus\tau,
\tag{15}
\]

again contradicting (7). Hence

\[
\boxed{
\text{no c-freely infinitely divisible pair can have }\nu_s
\text{ as its reference distribution.}
}
\tag{16}
\]

The standard c-free Lévy--Hinčin theory makes the same boundary visible from the classification side: c-free infinite divisibility requires a freely infinitely divisible reference component together with the appropriate conditional positive transform data. Equation (16) is the immediate source-specific consequence.

Because `nu_s` has exponentially decaying masses in log-energy for every `s>0`, it has all moments and a nontrivial exponential-moment neighborhood. The argument can therefore be read either in the original moment/cumulant formulation or in the analytic unbounded-support extension of c-free convolution; no moment-indeterminacy issue enters.

## 4. Putting the source in the other c-free coordinate gives a universal matched control

The first c-free coordinate behaves differently. Take both reference laws to be `delta_0`. In the two-state definition, a polynomial with zero constant term is centered for the reference state. Thus for alternating nonconstant polynomials from the two component algebras, the c-free factorization rule for the outer state is precisely the Boolean factorization rule. Therefore the first coordinate convolution reduces to Boolean convolution, giving (4).

This can also be expressed at the transform level: the c-free conditional transform with trivial free reference reduces to the Boolean self-energy/`K`-transform. It is the same Boolean structure that `WP-318` and `WP-326` already identified as universally infinitely divisible.

Let `mu` be any probability measure. For each integer `m>=2`, Boolean infinite divisibility gives a probability measure `rho_m` such that

\[
\mu=\rho_m^{\uplus m}.
\tag{17}
\]

Applying (4) repeatedly yields

\[
(\mu,\delta_0)
=
(\rho_m,\delta_0)^{\boxplus_c m}.
\tag{18}
\]

Hence

\[
\boxed{
(\mu,\delta_0)\text{ is c-freely infinitely divisible for every probability law }\mu.
}
\tag{19}
\]

In particular this holds for the exact arithmetic source `(nu_s,delta_0)`, but (19) remains true after replacing `nu_s` by a Gaussian, a two-point law, a random discrete law, or any other probability measure. The existence of this lift therefore fails the README's matched-control test maximally: the sign/divisibility comes from the universal c-free/Boolean category, not from prime powers, Mangoldt weights, or global arithmetic.

The two canonical placements of the exact scalar source in a c-free pair therefore give opposite failure modes:

\[
\boxed{
\text{source as reference: impossible;}
\qquad
\text{source with trivial reference: universally possible.}
}
\tag{20}
\]

Neither supplies a source-selective geometric positivity theorem.

## 5. Adversarial bypasses and exact scope

The strongest possible overstatement would be to conclude that bi-free, c-free, or operator-valued probability has been exhausted. It has not.

First, a bi-free construction may use freely divisible scalar marginals and place all arithmetic information in mixed bi-free cumulants. Equations (8)--(13) do not touch such a model. The price is that the mixed coupling must now be canonically forced by Mathia and must recover the exact finite-prime term without importing it as target data.

Second, a c-free pair `(nu_s,nu)` with a nontrivial freely infinitely divisible reference `nu` is not ruled out merely because its first coordinate is `nu_s`. Equation (16) obstructs only the **reference** placement. Equation (19) shows that one degenerate reference makes the lift automatic, but it does not prove that every nondegenerate reference is equally nonselective. A surviving c-free route would need a canonically forced reference law and conditional transform whose complete positivity is both nonautomatic on matched controls and strong enough to generate the desired global Weil sign.

Third, this argument does not generically descend from operator-valued free convolution to a scalar law. If `E:A->B` is a conditional expectation, composing `E` with an arbitrary scalar state on `B` need not turn amalgamated freeness into scalar freeness. Therefore there is no automatic scalar-shadow homomorphism to which (6) can be applied. Operator-valued free geometry remains open unless a proposed Mathia construction supplies a specific homomorphic scalar shadow; if it does, the lemma applies immediately.

Fourth, preprocessing the source before embedding it may fill the prime-power support gap and create a freely divisible shadow. That move is also outside the claim. It must independently prove exact recovery of the Mangoldt contribution after preprocessing, and its positivity must survive non-arithmetic controls rather than arise from a standard freely divisible completion.

Finally, none of the constructions above generates the archimedean Gamma term, the pole/global counterterm, or the Weil autocorrelation structure. Even a hypothetical selective enriched semigroup would still need a finite--archimedean bridge before it could answer the line's primary question.

## 6. Matched controls, prior art, and novelty audit

The probability theory used here is classical. Voiculescu introduced bi-free independence and its convolution operations; Hasebe--Huang--Wang extend additive bi-free convolution and infinite-divisibility theory to general Borel planar laws. The marginal identities (8)--(9) are structural consequences of the definition/partial `R`-transform, not Mathia discoveries.

Bozejko--Leinert--Speicher introduced conditionally free products and convolution. In their two-state construction the reference state is freely combined, giving (14), while the trivial-reference specialization yields the Boolean factorization used in (4). Popa--Vinnikov give modern operator-valued Boolean/free/c-free Lévy--Hinčin classifications; in particular the universal Boolean infinite-divisibility mechanism and the freely infinitely divisible reference requirement are standard theory.

The obstruction itself is also deliberately tested on controls. Replace `nu_s` by any scalar law that fails free two-divisibility. No bi-free divisible law can have it as a coordinate marginal, and no c-free divisible pair can have it as its reference coordinate. Conversely, (19) gives a degenerate c-free lift for **every** probability law. Thus neither half is an arithmetic positivity theorem.

A bounded literature search over bi-free infinite divisibility, c-free convolution, c-free Lévy--Hinčin theory, and the corresponding transform/marginal structures found the classical results above and no basis for attributing any of those probability-theoretic facts to Mathia. The Mathia-specific delta is narrower: combining those exact shadow maps with the source obstruction of `WP-326` closes the most direct two-face/two-state lifts that `WP-327` intentionally left open and identifies where any surviving enrichment must store its arithmetic information.

No claim is made that this result advances RH directly, that it exhausts noncommutative probability, or that absence of a matching phrase in the literature is evidence of novelty.

## Consequence for the research line

After `WP-327`, the next step is **not** to take the same scalar Mangoldt law and merely attach an auxiliary face or state while leaving the source as a free-convolution shadow. The shadow lemma makes such divisibility impossible in the bi-free marginal and c-free reference placements, while the simplest opposite c-free placement is universally divisible and therefore nonselective.

A viable enriched route must change the mechanism rather than the packaging. Arithmetic specificity has to live in a genuinely mixed operator/matrix/two-face relation, a nonseparable finite--archimedean coupling, a boundary/cohomological pairing, or another structure whose positive theorem is not inherited from a universal scalar convolution category. That mixed structure must still reproduce the exact finite prime contribution and independently produce the archimedean/global counterterms required by the Weil form.
