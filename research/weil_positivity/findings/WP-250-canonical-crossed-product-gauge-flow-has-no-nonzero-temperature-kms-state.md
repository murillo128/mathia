# WP-250 — Canonical crossed-product gauge flow has no nonzero-temperature KMS state

**Status:** `EXACT-DERIVED + CROSSED-PRODUCT-DUAL-GAUGE + KMS-NO-GO + EIGENUNITARY-OBSTRUCTION + BILATERAL-VERSUS-SEMIGROUP-DICHOTOMY + MATCHED-CONTROLS + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-248` shows that the critical all-prime deformation is disjoint from the spherical quasi-local representation, and `WP-249` tests the most direct category enlargement: adjoin a unitary implementing the critical product automorphism by forming the crossed product

\[
\mathcal B=\mathcal A\rtimes_\alpha\mathbb Z.
\]

The bare crossed-product positive core is too universal: its shift energy is arithmetic-blind and finite Fourier positive squares remain finite-prime local. `WP-249` therefore leaves a more structured possibility open: perhaps the enlarged algebra has a **canonical KMS/modular weight** whose thermodynamic positivity supplies the missing critical half-density and eventually a global Weil form.

For the canonical dual gauge dynamics, that route fails before any delicate arithmetic question appears. Let `u` be the implementing unitary and lift the dual circle action to a real flow

\[
\gamma_t(a)=a\quad(a\in\mathcal A),
\qquad
\gamma_t(u)=e^{it}u.
\tag{1}
\]

Then

\[
\boxed{
(\mathcal B,\gamma)\text{ has no }\beta\text{-KMS state for any }\beta\ne0.
}
\tag{2}
\]

The proof is one line of the KMS identity. The generator `u` is an entire analytic **unitary eigenoperator** for `gamma`, so at imaginary time

\[
\gamma_{i\beta}(u)=e^{-\beta}u.
\tag{3}
\]

If `phi` were a normalized `beta`-KMS state and we use the convention

\[
\phi(xy)=\phi\!\left(y\gamma_{i\beta}(x)\right)
\tag{4}
\]

for analytic `x`, then taking `x=u`, `y=u^*` gives

\[
1=\phi(uu^*)
=\phi\!\left(u^*\gamma_{i\beta}(u)\right)
=e^{-\beta}\phi(u^*u)
=e^{-\beta}.
\tag{5}
\]

Hence `beta=0`. The same argument survives every nonzero constant rescaling `gamma_t(u)=e^{i lambda t}u`: it gives `1=e^{-beta lambda}`. Thus the canonical gauge direction cannot have a finite thermal equilibrium state at the critical inverse temperature, or at any other nonzero temperature scale.

This is more informative than another generic statement that the crossed product is arithmetic-blind. It identifies the structural reason why the immediate crossed-product continuation cannot reproduce the Bost--Connes thermodynamic mechanism that previously supplied Mathia with the exact critical `p^{-1/2}` scale. **Bilateralizing the transport replaces the semigroup isometries by a unitary. The KMS defect that produced nontrivial range-projection masses then collapses into the impossible identity `1=e^{-beta lambda}`.**

The result does not rule out KMS **weights** infinite on the unit, a different arithmetic time evolution, a semigroup/Toeplitz crossed product, a nonunital corner, a Hilbert-module correspondence, or a genuinely global modular flow. It closes only the most canonical thermal continuation of `WP-249`: use the dual gauge flow of `A rtimes_alpha Z` itself as the source of a normalized critical KMS geometry.

## 1. Exact crossed-product object and canonical gauge flow

Use the quasi-local algebra and product automorphism of `WP-248`--`WP-249`,

\[
\mathcal A
=\overline{\bigcup_{F\Subset\mathbb P}\mathcal A_F},
\qquad
\alpha=\bigotimes_p\alpha_p,
\tag{6}
\]

and form

\[
\mathcal B=\mathcal A\rtimes_\alpha\mathbb Z.
\tag{7}
\]

The canonical unitary `u` satisfies

\[
uau^*=\alpha(a).
\tag{8}
\]

Because the acting group is `Z`, its Pontryagin dual is the circle. The crossed product therefore has the canonical dual action

\[
\widehat\alpha_z(a)=a,
\qquad
\widehat\alpha_z(u)=zu,
\qquad z\in\mathbb T.
\tag{9}
\]

Composing `z=e^{it}` gives the periodic one-parameter flow (1). This flow requires no extra source choice: once the `Z`-crossed product has been formed, it is part of the standard crossed-product structure.

The finite Fourier algebra

\[
\mathcal B_{\mathrm{fin}}
=\left\{
\sum_{n=-N}^{N}a_nu^n
\right\}
\tag{10}
\]

consists of entire analytic elements for `gamma`, with

\[
\gamma_z(a_nu^n)=e^{inz}a_nu^n,
\qquad z\in\mathbb C.
\tag{11}
\]

In particular the implementing unitary itself is entire and has gauge frequency `+1`. No domain or analytic-continuation subtlety is needed for the KMS test below.

## 2. An eigenunitary forbids every nonzero-temperature KMS state

The obstruction is not special to crossed products. Let `(C,sigma)` be a unital C*-dynamical system and suppose there is an entire analytic unitary `v in C` with

\[
\sigma_t(v)=e^{i\lambda t}v,
\qquad \lambda\ne0.
\tag{12}
\]

Then

\[
\sigma_{i\beta}(v)=e^{-\beta\lambda}v.
\tag{13}
\]

For a normalized `beta`-KMS state `phi`, (4) with `x=v`, `y=v^*` gives

\[
1
=\phi(vv^*)
=e^{-\beta\lambda}\phi(v^*v)
=e^{-\beta\lambda}.
\tag{14}
\]

Therefore

\[
\boxed{
\beta\lambda=0.
}
\tag{15}
\]

Since `lambda != 0`, no nonzero-`beta` KMS state exists.

Applying the lemma with `v=u` and `lambda=1` proves (2). The conclusion is independent of the automorphism `alpha`, independent of whether `alpha` is spatial in a chosen representation, and independent of the critical prime amplitudes used to define its local factors.

The same calculation also shows why a mere change of gauge speed cannot encode the critical scale. If one replaces (1) by

\[
\gamma_t^{(c)}(u)=e^{ict}u,
\tag{16}
\]

then every `beta`-KMS state still requires `beta c=0`. Choosing `c=0` makes the gauge flow trivial rather than arithmetic; choosing `c != 0` restores the obstruction. A scalar time reparameterization therefore supplies no thermal degree of freedom.

At `beta=0`, the KMS identity degenerates to traciality on the analytic algebra. Whether `B` admits a trace depends on `A` and `alpha`; no existence claim is needed here. The point is that the only temperature compatible with the eigenunitary loses the nonzero thermal parameter entirely and therefore cannot source the critical half-density through this gauge direction.

## 3. Why Bost--Connes does not suffer the contradiction

This distinction is the decisive structural control. In the Bost--Connes system, the multiplicative generators `mu_n` are isometries, not unitaries:

\[
\mu_n^*\mu_n=1,
\qquad
\mu_n\mu_n^*=E_n<1,
\tag{17}
\]

and the source time evolution satisfies

\[
\sigma_t(\mu_n)=n^{it}\mu_n.
\tag{18}
\]

Applying the KMS identity to `x=mu_n`, `y=mu_n^*` does **not** yield `1=n^{-beta}`. Instead it gives the nontrivial projection mass

\[
\phi_\beta(E_n)
=\phi_\beta(\mu_n\mu_n^*)
=n^{-\beta}\phi_\beta(\mu_n^*\mu_n)
=n^{-\beta}.
\tag{19}
\]

At `beta=1`, these range-projection masses are exactly the source of the divisibility Gram used in `WP-216`, whose normalized overlaps carry the half-density `p^{-|a-b|/2}`.

Equation (19) therefore identifies what is lost when the `WP-248` product automorphism is made inner by crossing with the **group** `Z`. The bilateral group generator is invertible on both sides,

\[
u^*u=uu^*=1,
\tag{20}
\]

so there is no proper range projection on which the KMS factor can land. The same KMS calculation that gives a meaningful mass law for an isometry becomes a contradiction for a nonzero-frequency unitary.

This is not an argument that semigroup crossed products automatically solve Weil positivity. The existing Bost--Connes chain `WP-209`--`WP-236` shows that source-forcing the critical finite amplitudes still leaves the Weil orientation, global completion, and Gamma/polar sectors unsupported. The present result makes a narrower point: **the canonical group-crossed-product gauge flow cannot even reproduce the thermodynamic selection mechanism that made the Bost--Connes starting point nontrivial.**

## 4. Bilateral Gibbs control: the regular gauge generator has two-sided spectrum

There is a complementary representation-level picture. In the regular covariant representation of `A rtimes_alpha Z`, the gauge action is implemented on the `ell^2(Z)` coordinate by the number operator

\[
N\delta_k=k\delta_k,
\qquad k\in\mathbb Z.
\tag{21}
\]

A formal Gibbs factor for the pure gauge direction would be

\[
e^{-\beta N}.
\tag{22}
\]

Even before including any multiplicity from the `A` representation,

\[
\operatorname{Tr}_{\ell^2(\mathbb Z)}e^{-\beta N}
=\sum_{k\in\mathbb Z}e^{-\beta k}
=\infty
\tag{23}
\]

for every real `beta`: for positive `beta` the negative tail diverges, for negative `beta` the positive tail diverges, and for `beta=0` both tails have infinite counting mass.

Equation (23) is not used to prove the C*-algebraic no-KMS theorem; (5) already does that without choosing a representation. It is a matched geometric explanation. The canonical transport coordinate created by crossing with `Z` is **bilateral** and has no thermodynamic ground direction. A semigroup/isometric construction has a one-sided defect/range structure on which nontrivial equilibrium weights may live; the group completion erases that asymmetry.

This observation also prevents a false rescue by declaring `N` itself to be the missing positive Hamiltonian. `N` is not positive, `|N|` forgets the orientation of the dual action, and any positive function of `N` is a universal Fourier-degree construction independent of the prime rotations `alpha_p`. The arithmetic would have to enter through additional coefficient, cocycle, state, boundary, or module data.

## 5. Matched controls and aggressive falsification

**Automorphism control.** Replace the critical prime rotation `alpha` by any automorphism of any unital C*-algebra. The crossed-product implementing unitary still obeys (8), the dual gauge flow still obeys (1), and the KMS contradiction (5) is unchanged. Thus the obstruction is intrinsic to the proposed category, not a hidden Riemann identity.

**Subcritical control.** Replace the critical nonspatial deformation by a square-summable deformation for which `WP-248` places the product state back in the spherical quasi-equivalence class. The crossed product still has the same eigenunitary and still has no nonzero-temperature KMS state for the canonical gauge flow. Hence the gauge thermodynamics does not detect the critical representation transition.

**Finite-support control.** If `alpha` differs from the identity at only finitely many primes and is implemented by an ordinary finite tensor unitary, (5) remains unchanged. The no-KMS statement is not caused by an infinite tail or by representation disjointness.

**Generalized-product control.** Randomize the local angles, replace primes by arbitrary labels, or remove arithmetic entirely. The conclusion persists. This is appropriate for a negative classification theorem: it says that canonical dual-gauge equilibrium cannot be the missing source-specific positivity mechanism.

**Arithmetic-time escape.** One can define another flow on `B` whose action on `A` or `u` contains prime-dependent cocycles, Hamiltonians, or modular data. That is outside (1) and can evade (5) if the implementing generator is no longer a nonzero-frequency unitary eigenoperator in the relevant sense. But the new dynamics then becomes a new source-selection obligation. It must be derived independently from the Mathia/global geometry, not chosen because its KMS weights reproduce `Lambda(n)/sqrt(n)` or the desired Weil sign.

**KMS-weight escape.** The proof excludes normalized KMS states, and more generally every nonzero KMS weight that is finite on the unit: such a weight could be normalized and would contradict (5). It does **not** exclude lower-semicontinuous semifinite KMS weights with

\[
\Phi(1)=\infty.
\tag{24}
\]

Such weights are a genuine surviving category. They cannot be counted as a solution merely because they evade normalization: a Weil bridge would have to specify their domain, show how a finite quadratic form is extracted without arbitrary subtraction, derive the finite-prime and archimedean terms from the same source, and prove positivity independently of the target.

**Semigroup/Toeplitz escape.** Replacing the bilateral group crossed product by an endomorphism/semigroup or Toeplitz-type construction is also outside the theorem. Equation (19) explains why this is mathematically meaningful rather than a technical loophole: proper range projections let the KMS factor appear as a nontrivial mass rather than forcing an impossible equality of two units. Such a move must still pass the extensive Bost--Connes controls already recorded by this line.

## 6. Prior-art and novelty audit

The KMS condition and the eigenoperator calculation are classical. The standard KMS boundary relation goes back to Haag, Hugenholtz, and Winnink, *On the equilibrium states in quantum statistical mechanics*, Communications in Mathematical Physics **5** (1967), 215--236. No novelty is claimed for (4), for the fact that the dual action of `T` exists on `A rtimes_alpha Z`, or for the observation that an analytic eigenunitary of nonzero frequency is incompatible with a normalized nonzero-temperature KMS state.

The relevant crossed-product contrast is also established prior art. Ruy Exel, *Crossed-Products by Finite Index Endomorphisms and KMS states*, Journal of Functional Analysis **199** (2003), 153--188, DOI `10.1016/S0022-1236(02)00023-X`, studies gauge actions and KMS states for crossed products by injective endomorphisms/transfer operators. The endomorphism/isometry setting is precisely the kind of one-sided structure in which range projections need not equal the unit and nontrivial KMS weights can occur.

Gauge-KMS phenomena for Toeplitz--Cuntz--Krieger and Cuntz--Krieger algebras likewise rely on proper isometric generators and Perron--Frobenius mass relations rather than on a bilateral unitary eigenoperator; see Astrid an Huef, Marcelo Laca, Iain Raeburn, and Aidan Sims, *KMS states on C*-algebras associated to higher-rank graphs*, Journal of Functional Analysis **266** (2014), 265--283, DOI `10.1016/j.jfa.2013.09.016`.

The arithmetic comparison is the original Bost--Connes system: Jean-Benoit Bost and Alain Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) **1** (1995), 411--457, DOI `10.1007/BF01589495`. Its multiplicative isometries and logarithmic time evolution yield the projection masses in (19), which are already the source anchor of `WP-216`.

A bounded search across `Z`-crossed products, dual/gauge actions, KMS states, endomorphism crossed products, graph-algebra gauge KMS states, and Bost--Connes thermodynamics found the general ingredients to be standard but did not locate a source applying the eigenunitary obstruction to the exact critical sector-transport continuation isolated by `WP-248`--`WP-249`. No novelty is claimed for the operator-algebra theorem. The durable Mathia delta is the **route classification**: the canonical thermal structure naturally attached to the new `Z` transport coordinate cannot provide a normalized critical equilibrium state at all, and the reason is exactly the unitary bilateralization that distinguishes this continuation from the successful finite-weight selection step in Bost--Connes.

## 7. Consequence for the Weil-positivity mandate

The immediate critical-sector chain is now

\[
\text{critical product deformation}
\xrightarrow{\text{WP-248}}
\text{disjoint quasi-local sector}
\xrightarrow{\mathcal A\rtimes_\alpha\mathbb Z}
\text{algebraically implemented transport}
\xrightarrow{\text{WP-249}}
\text{arithmetic-blind/local positive core},
\tag{25}
\]

and `WP-250` adds

\[
\boxed{
\text{canonical dual-gauge thermodynamics}
\not\Rightarrow
\text{critical KMS state},
}
\tag{26}
\]

because the new transport generator is a nonzero-frequency unitary.

Thus a source-forced KMS/modular continuation is not eliminated in general, but it must contain **additional asymmetric structure** beyond the bare `Z` crossed product and its dual action. The most concrete surviving choices are now sharply separated:

- retain a one-sided semigroup/isometric defect rather than bilateralizing it;
- use a non-normalized KMS weight and prove a canonical finite-part/domain theorem;
- introduce a genuinely arithmetic/modular time evolution rather than the universal gauge flow;
- or abandon thermal scalarization in favor of a source-forced correspondence, boundary state, unbounded cycle, or finite--archimedean coupling.

Each choice is new mathematical data. It must explain the exact finite prime-power coefficients, the Gamma and polar terms, and the global sign from the same construction, and it must survive matched generalized-product controls. None of those obligations follows from the crossed-product gauge structure itself.

The result therefore passes the substantive-finding gate as a decisive negative narrowing rather than as a Weil bridge. It closes a specifically named escape left by `WP-249` and exposes a useful structural lesson for future candidates: **the thermodynamic half-density in Bost--Connes is tied to one-sided range defects; an invertible bilateral transport generator cannot inherit that mechanism merely by being placed in a crossed product.**
