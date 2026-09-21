---
id: WP-395
title: Critical KMS centralizer erases exact prime-power orbit support
branch: weil_positivity
status: supported
kind: bost-connes-critical-kms-modular-centralizer-measure-class-support-obstruction
claim_strength: exact RH-independent classification of the original beta=1 Bost--Connes modular centralizer as the Haar-measurable closure of C*(Q/Z), with the consequence that exact prime-power support on any standard arithmetic orbit is either the zero affiliated operator or, if imposed only through point values, not an operator-level condition at all
created: 2026-09-21
related: [WP-216, WP-391, WP-392, WP-393, WP-394]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411--457, DOI 10.1007/BF01589495; especially Lemma 16 and Proposition 20
  - S. Neshveyev, von Neumann Algebras Arising from Bost--Connes Type Systems, IMRN 2011 (2011), 217--236, arXiv:0907.1456
  - standard spectral theory of abelian von Neumann algebras and affiliated measurable multiplication operators
---

# WP-395 — Critical KMS centralizer erases exact prime-power orbit support

## Claim

`WP-394` leaves open a genuinely different unbounded category: move from the standard positive-energy representation to the critical Bost--Connes KMS GNS factor and use its modular structure to constrain an operator or form. That move is source-forced rather than an arbitrary enlargement, because the inverse temperature `beta=1` and its modular flow belong to the Bost--Connes system itself.

For the **modular centralizer**, however, the exact prime-power selector problem degenerates in a new way.

Let `(A_BC,sigma)` be the original Bost--Connes system, let `phi_1` be its critical `KMS_1` state, and let

\[
M=\pi_{\phi_1}(A_{BC})''
\]

be the corresponding von Neumann algebra. Let

\[
D=C^*(\mathbf Q/\mathbf Z)\cong C(\widehat{\mathbf Z})
\subset A_{BC}.
\]

Then the modular centralizer of `phi_1` is exactly

\[
\boxed{
M_{\phi_1}=\pi_{\phi_1}(D)''
\cong L^\infty(\widehat{\mathbf Z},m_{\rm Haar}).
}
\tag{1}
\]

Consequently every self-adjoint operator affiliated with `M_{phi_1}` is, up to the usual almost-everywhere identification, multiplication by a measurable function on `hat Z`.

Fix any `alpha in hat Z^*` and write

\[
\mathcal O_\alpha=\{n\alpha:n\ge1\},
\qquad
\mathcal P_\alpha=\{p^j\alpha:p\ \text{prime},\ j\ge1\}.
\tag{2}
\]

Both sets are countable and therefore Haar-null. Hence:

1. if a centralizer projection, bounded centralizer element, or centralizer-affiliated operator has support contained in `P_alpha`, it is the zero operator;
2. if one instead asks only for point values such as "vanish at every mixed-prime `n alpha` but not at prime powers", that condition is **not well defined on the operator**: arbitrary changes on the countable arithmetic orbit `O_alpha` leave the same `L^infty` class and the same affiliated operator.

Thus the critical modular centralizer does not provide a nonzero exact prime-power selector. It does something more basic: **the Haar measure-class quotient forgets the discrete arithmetic orbit on which the standard positive-energy selector question was posed**.

This is not the bounded C-star obstruction of `WP-392`, nor the unital-affiliation collapse of `WP-393`, nor the source-resolvent reduction of `WP-394`. The von Neumann centralizer is genuinely larger than `D`, but exact point support has disappeared rather than become more expressive.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CRITICAL-KMS-GNS + MODULAR-CENTRALIZER + HAAR-MEASURE-CLASS + ABELIAN-VON-NEUMANN-CLOSURE + AFFILIATED-MEASURABLE-MULTIPLIERS + ARITHMETIC-ORBIT-NULL + EXACT-PRIME-POWER-SUPPORT-ZERO + POINT-SAMPLING-NOT-WELL-DEFINED + CATEGORY-BOUNDARY + NOT-A-WEIL-BRIDGE`.

## 1. The critical modular fixed algebra starts at `C*(Q/Z)`

Bost--Connes construct the critical state as a faithful normal vector state on the weak closure of the Hecke algebra representation and prove that it is `KMS_1`; its modular automorphism group is the Bost--Connes time evolution, up to the conventional sign. In the same paper, Proposition 20 identifies the C-star fixed-point algebra of that flow, equivalently the C-star centralizer of the critical state, as

\[
D=C^*(\mathbf Q/\mathbf Z)\cong C(\widehat{\mathbf Z}).
\tag{3}
\]

The generator formulas are

\[
\sigma_t(\mu_n)=n^{it}\mu_n,
\qquad
\sigma_t(e(y))=e(y).
\tag{4}
\]

So an algebraic monomial `mu_m e(y) mu_n^*` has energy character `(m/n)^{it}`; zero energy is exactly the `m=n` sector, whose norm closure is (3).

The point that needs checking here is that passing to the von Neumann closure does not secretly add nonzero modular-frequency-zero operators outside the weak closure of `D`.

## 2. The von Neumann centralizer is exactly the weak closure of `D`

Let

\[
\Gamma=\mathbf Q_+^\times
\]

with the discrete topology and let `K=hat Gamma` be its compact Pontryagin dual. The energy grading in (4) extends the time flow to the compact gauge action

\[
\theta_\chi(\mu_m e(y)\mu_n^*)
=\chi(m/n)\,\mu_m e(y)\mu_n^*,
\qquad \chi\in K.
\tag{5}
\]

The one-parameter subgroup

\[
t\longmapsto \chi_t,
\qquad
\chi_t(q)=q^{it},
\tag{6}
\]

is dense in `K`. Indeed, the annihilator of its closure consists of those `q in Q_+^*` for which `q^{it}=1` for every real `t`; this forces `log q=0`, hence `q=1`. A closed subgroup of a compact abelian group with trivial annihilator is the whole group.

The critical state is invariant under the time flow. Since (6) is dense and the gauge action is norm-continuous on `A_BC`, `phi_1` is invariant under all of `K`. The GNS implementation therefore extends (5) to a normal action on `M`. Averaging over normalized Haar measure on `K` gives a normal conditional expectation

\[
E_K:M\to M^K.
\tag{7}
\]

On the C-star algebra this is exactly the zero-energy Fourier projection, so Proposition 20 gives

\[
E_K(A_{BC})=D.
\tag{8}
\]

Now let `x in M^K`. By Kaplansky density, choose a uniformly bounded net `a_i in A_BC` converging strongly-star to `x`. Normality of the compact-group average gives, at least ultraweakly on that bounded net,

\[
E_K(a_i)\longrightarrow E_K(x)=x.
\tag{9}
\]

Every `E_K(a_i)` lies in `D`, hence `x in pi_phi(D)''`. The reverse inclusion is immediate because `D` is fixed pointwise. Thus

\[
M^K=\pi_{\phi_1}(D)''.
\tag{10}
\]

Density of (6) implies `M^{sigma}=M^K`; because `sigma` is the modular group up to sign,

\[
M_{\phi_1}=M^{\sigma}=\pi_{\phi_1}(D)'',
\tag{11}
\]

which proves the first equality in (1).

## 3. The centralizer measure is Haar measure on `hat Z`

It remains to identify the measure class of the abelian von Neumann algebra in (11).

In the critical representation used by Bost--Connes, the restriction of the Hecke representation to `C[Q/Z]` contains the regular representation on the orbit of the distinguished vector defining `phi_1`. Therefore

\[
\phi_1(e(y))=
\begin{cases}
1,&y=0,\\
0,&y\ne0.
\end{cases}
\tag{12}
\]

Under Pontryagin duality `C^*(Q/Z)=C(hat Z)`, these are exactly the Fourier coefficients of normalized additive Haar measure `m_Haar` on `hat Z`. Hence

\[
\phi_1(f)=\int_{\widehat{\mathbf Z}} f(x)\,dm_{\rm Haar}(x),
\qquad f\in C(\widehat{\mathbf Z}).
\tag{13}
\]

The critical vector state is faithful normal on `M`, so its restriction to the centralizer is faithful normal. The abelian von Neumann completion of `C(hat Z)` in this measure class is therefore

\[
\pi_{\phi_1}(D)''\cong
L^\infty(\widehat{\mathbf Z},m_{\rm Haar}),
\tag{14}
\]

establishing (1).

This is compatible with the classical type-III description of the critical Bost--Connes factor: `M` itself is noncommutative and type `III_1`; the statement here concerns only the modular centralizer selected by the critical state.

## 4. Every discrete arithmetic orbit is invisible to the centralizer measure class

For any `x in hat Z` and positive integer `N`, the cylinder

\[
x+N\widehat{\mathbf Z}
\]

has Haar measure `1/N`. Since `{x}` lies in all these cylinders,

\[
m_{\rm Haar}(\{x\})\le \frac1N
\qquad\text{for every }N,
\]

and therefore

\[
m_{\rm Haar}(\{x\})=0.
\tag{15}
\]

Every countable subset of `hat Z` is consequently null. In particular, for every unit `alpha`,

\[
m_{\rm Haar}(\mathcal O_\alpha)
=m_{\rm Haar}(\mathcal P_\alpha)=0.
\tag{16}
\]

The same is true for the mixed-prime subset

\[
\mathcal M_\alpha
=\{n\alpha:n\text{ is divisible by at least two distinct primes}\}.
\tag{17}
\]

Now let `T` be a self-adjoint operator affiliated with the centralizer. Since the centralizer is abelian, the spectral theorem identifies `T` with multiplication by a measurable extended-real function `t(x)`, modulo almost-everywhere equality. Its support projection is multiplication by `1_{t != 0}`.

If `supp(T) subset P_alpha`, then by (16) that support projection is zero in `L^infty`; hence

\[
\boxed{T=0.}
\tag{18}
\]

This includes bounded positive elements, projections, closed positive multiplication operators, and arbitrary self-adjoint operators affiliated with the modular centralizer.

The alternative formulation fails in the opposite direction. Suppose one declares a representative `t(x)` to be zero on every point of `M_alpha` and nonzero on selected points of `P_alpha`. Those pointwise assignments occur entirely inside the null set `O_alpha`. They can be changed arbitrarily without changing the `L^infty` class, any spectral projection, or the affiliated operator. Thus

\[
\boxed{
\text{prime-power versus mixed-prime point values on }\mathcal O_\alpha
\text{ are not operator invariants of }M_{\phi_1}.
}
\tag{19}
\]

So there are only two exact readings of the selector request inside the modular centralizer: literal support on the prime-power orbit gives the zero operator, while prescribed values on the orbit give no condition on the operator at all.

## 5. Stress tests and what survives

The obstruction is not a statement that the critical centralizer is trivial. Positive-measure arithmetic cylinders survive perfectly well. For example, the divisibility set `p hat Z` has Haar measure `1/p`, and its characteristic function is a nonzero projection in the von Neumann centralizer. What disappears is **exact support on a countable standard orbit**.

Nor does the argument use RH, prime-density estimates, Dirichlet's theorem, or an asymptotic approximation. Countability plus the source-selected Haar measure is enough. Multiplication by `alpha in hat Z^*` preserves Haar measure, so the conclusion is independent of the chosen standard arithmetic unit orbit.

There is also no contradiction with the standard positive-energy representation. There the vectors `epsilon_n` are honest atoms of the Hilbert basis and diagonal matrix elements at every integer label are meaningful. At critical KMS, passing to the modular centralizer changes category: the corresponding diagonal source algebra is completed in a diffuse Haar measure class, and the individual orbit points cease to be measurable atoms of the operator algebra.

This distinction also prevents a false positive. A measurable set of full Haar measure can be represented by a Borel set containing every prime-power orbit point and excluding every mixed-prime orbit point, simply because both subsets are null. Its characteristic function is still the identity operator. Such a representative-level separation is therefore **maximally programmable but operator-theoretically empty**; it cannot count as source-forced prime selection.

## 6. Relation to `WP-392`--`WP-394`

The successive category boundaries are now different and explicit.

`WP-392` works in the full bounded represented Bost--Connes C-star algebra and proves that positivity plus exact mixed-prime diagonal nullity forces the operator to vanish. There the arithmetic basis states remain visible and norm continuity/finite arithmetic horizon carries the contradiction.

`WP-393` observes that Woronowicz affiliation with the original **unital** C-star algebra adds no genuinely unbounded elements, so it never leaves the category of `WP-392`.

`WP-394` then allows genuinely unbounded closed positive forms, but shows that one canonical resolvent landing back in the represented source C-star algebra produces a positive bounded transform to which `WP-392` applies.

The present result finally tests one of the genuine escapes left by `WP-394`: the **critical KMS modular centralizer and its affiliated operators**. This category really is different and includes weak limits not in `C(hat Z)`, but it does not restore the exact selector. Instead, the discrete orbit itself becomes null and hence invisible modulo almost-everywhere equivalence.

Therefore the phrase "use the critical KMS von Neumann algebra with its canonical modular structure" is still too broad. If the proposed selector is required to lie in, or be affiliated with, the modular centralizer, exact prime-power point support cannot carry nonzero operator content.

## 7. Prior-art and novelty audit

The operator-algebraic ingredients are classical. Bost--Connes Lemma 16 identifies the critical vector state as `KMS_1` and relates its modular automorphism group to the time evolution. Their Proposition 20 identifies the C-star fixed-point algebra/centralizer as `C^*(Q/Z)`. The regular representation of `Q/Z`, Pontryagin duality, Haar Fourier coefficients, compact-group averaging, and the description of affiliated operators of an abelian von Neumann algebra as measurable multipliers are standard. Neshveyev's later type classification confirms that the Bost--Connes KMS factors for `0<beta<=1` are type `III_1`.

A bounded literature search around Bost--Connes critical KMS centralizers, `C^*(Q/Z)`, Haar measure, and prime-power support found the classical centralizer/type-III structure but no theorem coupling it to exact prime-power-versus-mixed-prime support on the standard arithmetic orbit. No novelty is claimed for the centralizer computation itself or for measure theory.

The line-specific derived contribution is the support audit (15)--(19): **the most canonical modular-centralizer enlargement left open after `WP-394` quotients out exactly the countable orbit on which an exact prime-power selector would have to act**. This converts a vague surviving category into a sharp falsification boundary.

## Limits

- The theorem is about the modular centralizer `M_phi1` and operators affiliated with it. It does **not** classify all operators affiliated with the full critical type-`III_1` factor `M`.
- It does not rule out noncentral modular spectral subspaces, the continuous core/crossed product, a canonical correspondence or one-sided range defect, or an operator whose arithmetic effect emerges only after a larger global construction.
- Positive-measure congruence and valuation sets remain available. A route using them must derive a source-forced limiting/assembly mechanism rather than identify countable orbit representatives by hand.
- The conclusion concerns exact prime-power support or exact point sampling. Approximate suppression in positive-measure neighborhoods is a different quantitative problem.
- Nothing here supplies the archimedean Gamma term, polar term, completed Weil form, independent sign theorem, or RH consequence.

## Consequence for the research line

A critical-KMS modular route now has to state where its arithmetic information lives. If it stays in the modular centralizer, the source-selected von Neumann completion is

\[
L^\infty(\widehat{\mathbf Z},m_{\rm Haar}),
\]

so exact standard-orbit prime-power support is either zero or representative-dependent noise. A surviving construction must therefore use more than centralizer affiliation: for example a **noncentral** modular spectral sector, a source-derived continuous core or correspondence, a positive-measure adelic/cylinder structure with a nonprogrammable limiting law, or a global finite--archimedean assembly in which the required prime weights arise without first asking for a point selector.

This narrows the accepted Bost--Connes completion clue again, while leaving its actual global sign and archimedean obligations entirely open.