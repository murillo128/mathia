# WP-250 — Canonical crossed-product gauge flow has no nonzero-temperature KMS state

**Status:** `EXACT-DERIVED + CROSSED-PRODUCT-DUAL-GAUGE + KMS-NO-GO + PROPER-KMS-WEIGHT-COLLAPSE + EIGENUNITARY-OBSTRUCTION + CSTAR-VERSUS-VON-NEUMANN-BOUNDARY + BILATERAL-VERSUS-SEMIGROUP-DICHOTOMY + MATCHED-CONTROLS + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-248` shows that the critical all-prime deformation is disjoint from the spherical quasi-local representation, and `WP-249` tests the most direct category enlargement: adjoin a unitary implementing the critical product automorphism by forming

\[
\mathcal B=\mathcal A\rtimes_\alpha\mathbb Z.
\]

The bare crossed-product positive core is too universal: its shift energy is arithmetic-blind and finite Fourier positive squares remain finite-prime local. A more structured possibility is that the enlarged algebra carries a canonical KMS/modular object whose thermodynamic positivity supplies the missing critical half-density and eventually a global Weil form.

For the canonical dual gauge dynamics, that route fails already at the C*-algebraic level. Let `u` be the implementing unitary and lift the dual circle action to

\[
\gamma_t(a)=a\quad(a\in\mathcal A),
\qquad
\gamma_t(u)=e^{it}u.
\tag{1}
\]

Then

\[
\boxed{
(\mathcal B,\gamma)
\text{ has neither a }\beta\text{-KMS state nor a proper }\beta\text{-KMS C*\!-weight for any }\beta\ne0.
}
\tag{2}
\]

The state obstruction is the eigenunitary identity from the original derivation. The stronger weight statement follows from an elementary but decisive fact: **every proper weight on a unital C*-algebra is automatically finite on the unit and therefore bounded.** Hence a proper KMS weight on `B` can be normalized to a KMS state, and the same contradiction applies.

This removes an apparent escape left by the earlier formulation of this finding. An infinite-on-the-unit **von Neumann** KMS weight may still exist after passing to a represented weak closure, and nonunital/stabilized/semigroup categories can support genuine unbounded C*-weights, but those are category changes. They are not hidden thermodynamic structure already present as a proper C*-weight on the unital crossed product itself.

## 1. Exact crossed-product object and canonical gauge flow

Use the quasi-local algebra and product automorphism of `WP-248`--`WP-249`,

\[
\mathcal A
=\overline{\bigcup_{F\Subset\mathbb P}\mathcal A_F},
\qquad
\alpha=\bigotimes_p\alpha_p,
\tag{3}
\]

and form

\[
\mathcal B=\mathcal A\rtimes_\alpha\mathbb Z.
\tag{4}
\]

The canonical unitary `u` satisfies

\[
uau^*=\alpha(a).
\tag{5}
\]

Because the acting group is `Z`, its Pontryagin dual is the circle. The crossed product therefore has the canonical dual action

\[
\widehat\alpha_z(a)=a,
\qquad
\widehat\alpha_z(u)=zu,
\qquad z\in\mathbb T.
\tag{6}
\]

Composing `z=e^{it}` gives (1). The finite Fourier algebra

\[
\mathcal B_{\mathrm{fin}}
=\left\{
\sum_{n=-N}^{N}a_nu^n
\right\}
\tag{7}
\]

consists of entire analytic elements for `gamma`, with

\[
\gamma_z(a_nu^n)=e^{inz}a_nu^n,
\qquad z\in\mathbb C.
\tag{8}
\]

In particular `u` is an entire analytic unitary eigenoperator of gauge frequency `+1`. No domain or analytic-continuation subtlety is needed for the first obstruction.

## 2. An eigenunitary forbids every nonzero-temperature KMS state

Let `(C,sigma)` be a unital C*-dynamical system and suppose there is an entire analytic unitary `v\in C` with

\[
\sigma_t(v)=e^{i\lambda t}v,
\qquad \lambda\ne0.
\tag{9}
\]

Then

\[
\sigma_{i\beta}(v)=e^{-\beta\lambda}v.
\tag{10}
\]

For a normalized `beta`-KMS state `phi`, use the convention

\[
\phi(xy)=\phi\!\left(y\sigma_{i\beta}(x)\right)
\tag{11}
\]

for analytic `x`. Taking `x=v`, `y=v^*` gives

\[
1
=\phi(vv^*)
=e^{-\beta\lambda}\phi(v^*v)
=e^{-\beta\lambda}.
\tag{12}
\]

Therefore

\[
\boxed{\beta\lambda=0.}
\tag{13}
\]

Applying the lemma with `v=u` and `lambda=1` proves the state part of (2). The conclusion is independent of the automorphism `alpha`, independent of whether `alpha` is spatial in a chosen representation, and independent of the critical prime amplitudes used to define its local factors.

The same calculation survives every nonzero constant rescaling `gamma_t(u)=e^{ict}u`: every KMS state still requires `beta c=0`. Choosing `c=0` makes the gauge flow trivial rather than arithmetic; choosing `c\ne0` restores the obstruction.

At `beta=0`, the KMS identity degenerates to traciality on the analytic algebra. Whether `B` admits a trace depends on `A` and `alpha`; no existence claim is needed here. The point is that the only temperature compatible with the eigenunitary loses the nonzero thermal parameter entirely.

## 3. Proper weights on a unital C*-algebra are bounded

The stronger weight statement is elementary but closes the main apparent loophole.

Let `Phi` be a proper C*-weight on a unital C*-algebra `C`. In the standard Kustermans/Combes terminology, proper means nonzero, lower semicontinuous, and densely defined. Equivalently, its square-integrable left ideal

\[
\mathcal N_\Phi
=\{x\in C:\Phi(x^*x)<\infty\}
\tag{14}
\]

is norm dense in `C`.

Choose `x\in\mathcal N_\Phi` with

\[
\|x-1\|<\varepsilon<1.
\tag{15}
\]

Then `x` is invertible and

\[
x^*x\succeq (1-\varepsilon)^2 1.
\tag{16}
\]

By monotonicity of a weight,

\[
\Phi(1)
\le (1-\varepsilon)^{-2}\Phi(x^*x)
<\infty.
\tag{17}
\]

For every `a\in C_+`,

\[
0\le a\le \|a\|1,
\]

so

\[
\Phi(a)\le \|a\|\Phi(1)<\infty.
\tag{18}
\]

Thus `Phi` is finite everywhere on `C_+` and extends to a bounded positive functional with norm `Phi(1)`. Since `Phi` is nonzero, `Phi(1)>0`, and

\[
\phi=\frac{\Phi}{\Phi(1)}
\tag{19}
\]

is a state.

Consequently,

\[
\boxed{
\text{proper KMS weight on a unital C*\!-algebra}
\Longrightarrow
\text{bounded KMS functional}
\Longrightarrow
\text{KMS state after normalization}.
}
\tag{20}
\]

Combining (20) with the eigenunitary obstruction proves the second half of (2): the canonical dual gauge flow on the unital crossed product has **no proper nonzero-temperature KMS C*-weight**.

This is stronger than the original statement that only weights finite on the unit are excluded. Under the standard C*-weight definition, norm-dense properness itself forces finiteness on the unit in the unital category.

## 4. Why infinite von Neumann weights are not a counterexample

The distinction between C*-weights and von Neumann weights is structural, not terminological.

For a C*-algebra, dense definition is a **norm-density** requirement. That is what drives (15)--(17). By contrast, a normal semifinite weight on a von Neumann algebra is required to have a finite domain dense in a weak/operator topology, not in operator norm. The usual trace on `B(\ell^2)` is the standard example: it is normal and semifinite, has

\[
\operatorname{Tr}(1)=\infty,
\tag{21}
\]

and its finite-rank ideal is weakly dense but not norm dense in `B(\ell^2)`.

Therefore an infinite-on-the-unit modular/KMS weight can reappear only after changing category, for example by passing to a represented von Neumann closure, a nonunital ideal/corner, a stabilization, or another algebra whose finite-weight domain can be dense in the relevant topology without approximating the unit in norm.

That is a legitimate surviving research direction, but it is additional mathematical structure. A future Weil bridge must specify the representation or nonunital algebra, prove the weight is canonical there, identify a finite quadratic-form domain, and show that the finite-prime and archimedean/polar terms arise from the same source. Merely saying "use a KMS weight instead of a state" no longer evades `WP-250` inside the original unital crossed product.

## 5. Why Bost--Connes does not suffer the contradiction

In the Bost--Connes system, the multiplicative generators `mu_n` are isometries, not unitaries:

\[
\mu_n^*\mu_n=1,
\qquad
\mu_n\mu_n^*=E_n<1,
\tag{22}
\]

and the source time evolution satisfies

\[
\sigma_t(\mu_n)=n^{it}\mu_n.
\tag{23}
\]

Applying the KMS identity to `x=mu_n`, `y=mu_n^*` gives the nontrivial range-projection mass

\[
\phi_\beta(E_n)
=\phi_\beta(\mu_n\mu_n^*)
=n^{-\beta}\phi_\beta(\mu_n^*\mu_n)
=n^{-\beta},
\tag{24}
\]

rather than the impossible identity `1=n^{-beta}`.

At `beta=1`, these masses are exactly the source of the divisibility Gram used in `WP-216`, whose normalized overlaps carry the half-density `p^{-|a-b|/2}`. Bilateral group completion replaces the one-sided range defect by

\[
u^*u=uu^*=1,
\tag{25}
\]

and the thermodynamic defect collapses.

This does not imply that semigroup crossed products solve Weil positivity. The existing Bost--Connes chain shows that source-forcing the critical finite amplitudes still leaves the Weil orientation, global completion, and Gamma/polar sectors unsupported. The narrower point is that the canonical group-crossed-product gauge flow cannot even reproduce the nontrivial equilibrium mass mechanism of the one-sided system.

## 6. Bilateral Gibbs control

In the regular covariant representation of `A\rtimes_\alpha Z`, the gauge action is implemented on the `ell^2(Z)` coordinate by the number operator

\[
N\delta_k=k\delta_k,
\qquad k\in\mathbb Z.
\tag{26}
\]

A formal Gibbs factor is

\[
e^{-\beta N}.
\tag{27}
\]

Even before including multiplicity from the `A` representation,

\[
\operatorname{Tr}_{\ell^2(\mathbb Z)}e^{-\beta N}
=\sum_{k\in\mathbb Z}e^{-\beta k}
=\infty
\tag{28}
\]

for every real `beta`. This is not the proof of (2); it is a representation-level explanation of why the bilateral gauge coordinate has no finite Gibbs equilibrium. It also shows why moving to a von Neumann weight is genuinely a different infinite-mass category rather than a hidden finite equilibrium on the original unital C*-algebra.

Declaring `N` or `|N|` to be the missing Hamiltonian does not help. `N` is not positive, `|N|` forgets the orientation of the dual action, and any positive function of `N` is a universal Fourier-degree construction independent of the prime rotations `alpha_p`.

## 7. Matched controls and surviving escapes

**Automorphism control.** Replace the critical prime rotation `alpha` by any automorphism of any unital C*-algebra. The implementing unitary and the dual gauge eigenrelation remain, so both the KMS-state and proper-KMS-weight obstructions are unchanged. The theorem is category-theoretic, not Riemann-specific.

**Subcritical and finite-support controls.** Make the product deformation square-summable, spatial, or supported at finitely many primes. The same unital crossed product and eigenunitary argument still exclude every nonzero-temperature proper gauge-KMS weight. The obstruction therefore does not detect critical representation disjointness by itself.

**Generalized-product control.** Randomize local angles, replace primes by arbitrary labels, or remove arithmetic. Nothing changes. This is appropriate for a negative classification theorem: canonical dual-gauge equilibrium cannot be the missing source-specific positivity mechanism.

**Arithmetic-time escape.** A different flow whose action contains prime-dependent cocycles, Hamiltonians, or modular data is outside (1). It may evade the eigenunitary theorem if `u` is no longer a nonzero-frequency analytic eigenunitary for the relevant dynamics. The new flow then becomes a source-selection obligation and must be derived independently rather than chosen to reproduce the target coefficients.

**Nonunital/von-Neumann escape.** A nonunital corner, ideal, stabilization, Hilbert-module algebra, or represented von Neumann closure can carry genuine unbounded weights. This is now the correct weight escape. It must come with a canonical domain and a finite-form extraction theorem; otherwise infinite mass merely moves the regularization problem.

**Semigroup/Toeplitz escape.** Replacing the bilateral group crossed product by an endomorphism/semigroup or Toeplitz-type construction remains outside the theorem. Proper range projections let the KMS factor appear as a nontrivial mass as in (24). Such a move must still pass the extensive Bost--Connes controls already recorded by this line.

## 8. Prior-art and novelty audit

The KMS condition and the eigenoperator calculation are classical. The standard boundary relation goes back to Haag, Hugenholtz, and Winnink, *On the equilibrium states in quantum statistical mechanics*, Communications in Mathematical Physics **5** (1967), 215--236.

The weight terminology used above is standard. Johan Kustermans, *KMS-weights on C*-algebras*, arXiv:`funct-an/9704008` (1997), develops the proper lower-semicontinuous densely defined C*-weight framework and proves equivalence with the Combes formulation. Klaus Erik Thomsen, *An introduction to KMS weights*, arXiv:`2204.01125` (2022), gives a modern account and emphasizes the role of stabilization/nonunital categories in relating KMS weights to KMS states. The implication "proper weight on a unital C*-algebra is bounded" used here is an elementary consequence of the standard norm-density definition, not a new operator-algebra theorem.

The crossed-product contrast is also prior art. Ruy Exel, *Crossed-Products by Finite Index Endomorphisms and KMS states*, Journal of Functional Analysis **199** (2003), 153--188, DOI `10.1016/S0022-1236(02)00023-X`, studies gauge actions and KMS states in the one-sided endomorphism/transfer-operator setting. Gauge-KMS phenomena for Toeplitz--Cuntz--Krieger and higher-rank graph algebras likewise rely on proper isometric generators and Perron--Frobenius mass relations rather than a bilateral eigenunitary; see an Huef--Laca--Raeburn--Sims, *KMS states on C*-algebras associated to higher-rank graphs*, Journal of Functional Analysis **266** (2014), 265--283.

The arithmetic comparison remains Bost--Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica **1** (1995), 411--457. Its one-sided multiplicative isometries yield the projection masses already used by `WP-216`.

A bounded literature search across KMS weights, unital C*-algebras, crossed-product dual actions, semigroup crossed products, stabilization, and Bost--Connes thermodynamics confirms that the functional-analytic ingredients are standard. No novelty is claimed for them. The durable Mathia contribution is the route classification: **the apparent infinite-weight escape in the unital crossed-product C*-category is not an escape at all; genuine infinite equilibrium weights require a different topology/category.**

## 9. Consequence for the Weil-positivity mandate

The critical-sector chain is now

\[
\text{critical product deformation}
\xrightarrow{\text{WP-248}}
\text{disjoint quasi-local sector}
\xrightarrow{\mathcal A\rtimes_\alpha\mathbb Z}
\text{algebraically implemented transport}
\xrightarrow{\text{WP-249}}
\text{arithmetic-blind/local positive core},
\tag{29}
\]

and `WP-250` strengthens the thermal obstruction to

\[
\boxed{
\text{canonical dual-gauge thermodynamics on the unital crossed product}
\not\Rightarrow
\text{nonzero-temperature state or proper C*\!-KMS weight}.
}
\tag{30}
\]

Thus a source-forced modular continuation is not eliminated in general, but it must cross an explicit categorical boundary: retain one-sided semigroup defects, pass to a source-forced nonunital/stabilized algebra, or derive a represented von Neumann modular object with a canonical finite-form domain. Alternatively it must introduce a genuinely arithmetic time evolution or abandon thermal scalarization for a correspondence, boundary state, unbounded cycle, or active finite--archimedean coupling.

Each surviving choice is new mathematical data. It must explain the exact finite prime-power coefficients, the Gamma and polar terms, and the global sign from the same construction, and it must survive matched generalized-product controls. None of those obligations follows from the crossed-product gauge structure itself.

The substantive narrowing is therefore sharper than the original version: **bilateralization kills not only normalized KMS states but every proper KMS weight in the original unital C*-category. Infinite thermal mass becomes available only after a genuine category change, which must itself be justified by the Mathia/global geometry.**