---
id: WP-418
title: Bost--Connes phase-inserted ratio rays are GCD Grams masked by character compatibility
branch: weil_positivity
status: supported
kind: critical-kms-phase-inserted-fixed-ratio-gram-classification
claim_strength: exact RH-independent classification of the canonical Bost--Connes fixed-ratio partial-isometry family after insertion of arbitrary phase-algebra characters; KMS degree locking still separates rational ratios, and within each ratio the normalized critical Gram is the WP-216 GCD/Poisson kernel multiplied by an exact rational-character compatibility mask, equivalently an ordinary profinite Haar Gram, so phase insertion creates incidence but not a new Weil-oriented sign mechanism
created: 2026-09-23
related: [WP-209, WP-216, WP-217, WP-413, WP-416, WP-417]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411-457
  - Pontryagin duality and Haar orthogonality for Q/Z and Z-hat
---

# WP-418 — Bost--Connes phase-inserted ratio rays are GCD Grams masked by character compatibility

## Claim

`WP-417` shows that the native Bost--Connes two-sided partial isometries

\[
v_{m,n}=\mu_m\mu_n^*
\]

are first split by KMS dynamics according to the rational ratio `m/n`, and that every fixed-ratio block reduces after critical normalization to the old `WP-216` GCD/Poisson Gram. A natural remaining escape is to retain the phase algebra between the two semigroup legs rather than use a bare partial isometry.

That escape can be classified exactly for the canonical character insertions. Fix a reduced ratio `a/b` and define, for `k>=1` and `r in Q/Z`,

\[
x_{k,r}^{a/b}:=\mu_{ak}\,e(r)\,\mu_{bk}^*.
\tag{1}
\]

At the critical Bost--Connes `KMS_1` state `phi_1`, vectors with different ratios remain orthogonal. Inside one fixed ratio, let

\[
g=(k,\ell),\qquad k=gk',\qquad \ell=g\ell',\qquad (k',\ell')=1.
\]

Then the exact unnormalized inner product is

\[
\boxed{
\phi_1\!\left((x_{k,r}^{a/b})^*x_{\ell,s}^{a/b}\right)
=\frac1b\frac{g}{k\ell}
\,\mathbf 1_{\ell' r=k's\ \text{in }\mathbf Q/\mathbf Z}.
}
\tag{2}
\]

Since

\[
\|x_{k,r}^{a/b}\|_{\phi_1}^2=\frac1{bk},
\tag{3}
\]

the normalized critical Gram is

\[
\boxed{
G\big((k,r),(\ell,s)\big)
=\frac{\gcd(k,\ell)}{\sqrt{k\ell}}
\,\mathbf 1_{(\ell/g)r=(k/g)s\ \text{in }\mathbf Q/\mathbf Z}.
}
\tag{4}
\]

Thus ordinary phase-algebra insertion does retain more information than `WP-417`: it can erase overlaps through exact rational-character incompatibility. But every surviving overlap has **exactly the same GCD amplitude** as the old critical Poisson carrier. Equation (4) is itself an ordinary `L^2(Z-hat,Haar)` Gram of partial characters on profinite cylinder sets. Its nonnegativity is therefore compact-group Haar positivity before any Riemann-specific interpretation.

The result closes the canonical phase-character insertion branch left open by `WP-417`. It does not rule out active modular fibre dynamics, a non-character coefficient module, a genuinely orientation-sensitive non-Gram readout, altered scalarization, or a source-forced finite--archimedean coupling.

**Classification:** `CLASSICAL-BC-RELATIONS + EXACT-DERIVED + RH-INDEPENDENT + FIXED-RATIO-KMS-LOCKING + PHASE-ALGEBRA-INSERTION + RATIONAL-CHARACTER-COMPATIBILITY + MASKED-GCD-GRAM + PROFINITE-HAAR-CONTROL + DECISIVE-NARROWING + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. KMS dynamics still locks the ratio

The Bost--Connes time evolution fixes the phase algebra and scales the semigroup isometries:

\[
\sigma_t(e(r))=e(r),\qquad
\sigma_t(\mu_n)=n^{it}\mu_n.
\]

Hence

\[
\sigma_t(x_{k,r}^{a/b})=(a/b)^{it}x_{k,r}^{a/b}.
\tag{5}
\]

For two possibly different reduced ratios `a/b` and `c/d`, the mixed GNS coefficient has nonzero time degree unless `a/b=c/d`. Invariance of every positive-temperature KMS state therefore gives zero across distinct ratios, exactly as in `WP-416`--`WP-417`.

Phase insertion does not mix time degrees because `e(r)` lies in the fixed-point algebra. Any benefit must therefore occur **inside** a fixed-ratio block.

## 2. Exact fixed-ratio reduction

Write

\[
P_k(e(r)):=\mu_k e(r)\mu_k^*.
\]

Commutativity of the integer semigroup isometries gives

\[
x_{k,r}^{a/b}
=\mu_a P_k(e(r))\mu_b^*.
\tag{6}
\]

Therefore

\[
(x_{k,r}^{a/b})^*x_{\ell,s}^{a/b}
=\mu_b\,P_k(e(-r))P_\ell(e(s))\,\mu_b^*.
\tag{7}
\]

For a time-invariant element `f`, the `KMS_1` relation gives

\[
\phi_1(\mu_b f\mu_b^*)=b^{-1}\phi_1(f).
\tag{8}
\]

The standard Bost--Connes transfer relation is

\[
P_k(e(r))
=\frac1k\sum_{ku=r}e(u).
\tag{9}
\]

At the critical point, the unique `KMS_1` state restricts to Haar measure on the phase algebra `C^*(Q/Z) ~= C(Z-hat)`, so

\[
\phi_1(e(q))=\mathbf 1_{q=0}.
\tag{10}
\]

Insert (9) into (7)--(8). The Haar mean survives precisely when a pair `u,v` obeys

\[
ku=-r,\qquad \ell v=s,\qquad u+v=0.
\]

Equivalently, with `w=-u`,

\[
kw=r,\qquad \ell w=s.
\tag{11}
\]

The map

\[
w\longmapsto(kw,\ell w)
\]

from `Q/Z` has kernel of cardinality `g=gcd(k,ell)`. Its image consists exactly of pairs satisfying

\[
\ell' r=k's.
\tag{12}
\]

Necessity is immediate. For sufficiency choose integers `u_0,v_0` with `u_0 k'+v_0 ell'=1`. If (12) holds, then

\[
y=u_0 r+v_0 s
\]

satisfies `k'y=r` and `ell'y=s`; divisibility of `Q/Z` gives exactly `g` preimages under multiplication by `g`. Thus (11) has `g` solutions when (12) holds and none otherwise. Multiplying by the prefactor `1/(bk ell)` proves (2).

Taking `k=ell` and `r=s` gives (3). Normalizing (2) by the two diagonal norms proves (4). Setting `r=s=0` removes the mask and recovers exactly the fixed-ratio Gram of `WP-417`, providing an internal normalization check.

## 3. Profinite Haar model makes the positivity source explicit

Under Pontryagin duality `C^*(Q/Z)=C(Z-hat)`, the transferred character has the concrete form

\[
P_k(e(r))(\rho)
=\mathbf 1_{k\widehat{\mathbf Z}}(\rho)
\,e(r)(\rho/k).
\tag{13}
\]

Thus `P_k(e(r))` is simply a unit-modulus character on the cylinder `k Z-hat`, extended by zero. The intersection of two supports is

\[
k\widehat{\mathbf Z}\cap \ell\widehat{\mathbf Z}
=\operatorname{lcm}(k,\ell)\widehat{\mathbf Z},
\]

whose Haar measure is

\[
\frac1{\operatorname{lcm}(k,\ell)}
=\frac{g}{k\ell}.
\tag{14}
\]

On that intersection the relative character is trivial exactly when (12) holds. Otherwise Haar orthogonality makes the integral zero. Consequently (2) is not merely a counting coincidence: it is the ordinary Haar inner product of two profinite partial characters, followed by the universal `b^{-1}` KMS factor.

This gives a matched nonarithmetic control immediately. Any compact profinite model with the same nested finite-index subgroup geometry and partial characters has the same positive Gram mechanism. No zeta zero, Weil kernel, Gamma factor, or polar term enters the sign theorem.

## 4. What the character mask can and cannot do

The phase insertion creates a real incidence effect. For fixed labels `r,s`, an overlap can vanish even when the underlying divisibility projections overlap. Therefore it would be incorrect to describe ordinary phase-algebra insertions as completely Gram-invisible.

What remains rigid is the **magnitude of every surviving overlap**: it is exactly

\[
\frac{g}{\sqrt{k\ell}},
\]

the critical `WP-216`/`WP-417` GCD amplitude. The additional information is only the compatibility predicate (12).

Moreover, the character labels are not selected by the critical KMS state or by the divisibility semigroup. Choosing a family `r_k` can therefore program many compatibility patterns. A proposed arithmetic selector based on such labels must first derive those labels from independent source geometry; merely choosing them to erase unwanted mixed-prime overlaps would import the desired support rather than explain it.

Even if a source-forced label family were found, equation (4) supplies only a finite/profinite Gram block. It produces neither the archimedean Gamma contribution nor the polar/global counterterms required by the canonical Weil-positivity mandate. The positivity here is established before those terms exist.

## 5. Adversarial and boundary audit

Several checks prevent overreading the result.

First, the compatibility condition has the correct sign. The Haar constraint in (7) is `u+v=0`; replacing `u` by `-w` gives simultaneously `kw=r` and `ell w=s`, hence `(ell/g)r=(k/g)s`.

Second, the solution multiplicity is exactly `g`, not `1` or `lcm(k,ell)`: the common kernel of multiplication by `k` and `ell` in `Q/Z` is the `g`-torsion subgroup. This is also forced by the cylinder-intersection mass (14).

Third, `a` drops out and `b` survives only as the common unnormalized KMS factor. After normalization both disappear, agreeing with `WP-417`. Thus phase insertion does not secretly restore ratio-dependent arithmetic weight.

Fourth, the theorem is deliberately restricted to canonical group-algebra characters inserted between the two semigroup legs and to scalarization by the standard critical KMS state. It does not classify arbitrary elements of the fixed-point algebra, non-character coefficient modules, active dynamics on the inserted fibre, operator-valued conditional expectations, or nonlinear/orientation-sensitive readouts.

A decisive falsification would be a pair in this exact family for which the normalized `KMS_1` inner product differs from (4). Such a counterexample would contradict either the Bost--Connes transfer relation, critical Haar restriction, or the elementary simultaneous-congruence count.

## 6. Prior-art and novelty boundary

The ingredients are classical. The Bost--Connes relations (including the transfer average (9)), the time evolution, the critical KMS state, and Pontryagin duality between `Q/Z` and `Z-hat` are standard. Haar orthogonality of compact-group characters and the gcd/lcm subgroup identities are also classical. No novelty is claimed for any of these facts separately.

The prior-art audit across the classical Bost--Connes/KMS formulations and the neighboring Mathia findings found no distinct theorem needed here beyond those standard ingredients. The durable Mathia contribution is the **line-specific exact composition**: the particular fixed-ratio phase-inserted two-sided family left open by `WP-417` has the normalized critical Gram (4), so its extra phase information is precisely a rational-character compatibility mask on the already-audited GCD carrier. This is recorded as a scoped obstruction/classification, not as a claim of new general operator-algebra mathematics.

This differs from `WP-410`, where a central groupoid twist disappears after passage to canonical range projections, and from `WP-413`, where equal-scale factorization paths scalarize to generic phase-correlation Grams. Here the phase algebra is retained explicitly **inside each native two-sided semigroup ray**, and the result shows exactly what survives: a profinite incidence mask but no new positive amplitude or global Weil completion.

## Consequence

**Supported exact negative with a narrower survivor.** Ordinary source-native Bost--Connes character insertions do not escape the `WP-417` fixed-ratio obstruction. They refine the old critical GCD/Poisson Gram only by the compatibility predicate `(ell/g)r=(k/g)s`; the sign remains universal Haar-Gram positivity, and the construction still lacks an intrinsic finite-plus-archimedean Weil form.

The enlarged-category route must therefore obtain genuinely new structure from a hypothesis not covered here: source-forced non-character incidence, active modular/fibre dynamics, mixing of time degrees, a changed scalarization, an orientation-sensitive non-Gram observable, or a canonical finite--archimedean coupling. Any such proposal must still fail matched nonarithmetic controls and derive rather than program the arithmetic labels or support.
