---
id: WP-428
title: Bohr-diagonal noncommuting KMS sandwiches cannot orient the Bost-Connes Weil defect
branch: weil_positivity
status: triage
kind: bost-connes-kms-noncommuting-sandwich-obstruction
claim_strength: exact RH-independent obstruction for source-preserving KMS extensions whose positive readout is assembled from homogeneous auxiliary sandwiches; noncommutativity alone does not move a nonzero source Bohr mode into the invariant sector, and any equivariant expected operator-valued version falls back under WP-225
created: 2026-09-24
related: [WP-225, WP-412, WP-425, WP-426, WP-427]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics II, 2nd ed., Springer, 1997
  - I. Marvian and R. W. Spekkens, Modes of asymmetry: The application of harmonic analysis to symmetric quantum dynamics and quantum reference frames, Phys. Rev. A 90 (2014), 062110, DOI 10.1103/PhysRevA.90.062110
---

# WP-428 — Bohr-diagonal noncommuting KMS sandwiches cannot orient the Bost-Connes Weil defect

## Claim

`WP-427` leaves a precise escape: once the auxiliary insertion is allowed to **not commute** with the Bost-Connes source, the relative-commutant KMS argument no longer applies. Noncommutativity by itself, however, is still insufficient for the most natural positive sandwich readout.

Let `(C,\gamma)` be a C*-dynamical system, let `A\subset C` be a `\gamma`-invariant C*-subalgebra, and write `\alpha=\gamma|_A`. Let `\Omega` be any `\gamma`-invariant state; in particular, every positive-temperature `\gamma`-KMS state is allowed. Suppose `b_\nu\in C` is a homogeneous auxiliary operator,

\[
\gamma_t(b_\nu)=e^{i\nu t}b_\nu.
\]

Define the positive sandwich functional on the source by

\[
\psi_{b_\nu}(a):=\Omega(b_\nu^*ab_\nu),
\qquad a\in A.
\]

Then `\psi_{b_\nu}` is `\alpha`-invariant. Consequently every nonzero source Bohr mode is annihilated:

\[
\boxed{
\alpha_t(a_\omega)=e^{i\omega t}a_\omega,\ \omega\ne0
\quad\Longrightarrow\quad
\Omega(b_\nu^*a_\omega b_\nu)=0.
}
\tag{1}
\]

No commutation relation between `b_\nu` and `A` is assumed. The same conclusion holds for any finite or norm-convergent positive sum of such diagonal homogeneous sandwiches.

There is also an operator-valued version. If `E:C\to A` is an equivariant conditional expectation and

\[
\Phi_{b_\nu}(a):=E(b_\nu^*ab_\nu),
\tag{2}
\]

then `\Phi_{b_\nu}` is completely positive and source-time-covariant. In any normal finite-prime realization where `E` and `\Phi_{b_\nu}` are normal, `WP-225` therefore applies to the critical Bost-Connes Weil defect `W_F`:

\[
\boxed{
\Phi_{b_\nu}(W_F)\succeq0
\quad\Longrightarrow\quad
\Phi_{b_\nu}(W_F)=0.
}
\tag{3}
\]

Thus the surviving noncommuting branch after `WP-427` is narrower than “use a noncommuting auxiliary.” A viable positive sandwich mechanism must contain **coherent interference between distinct auxiliary Bohr sectors**, or else deform the source time evolution itself. A single homogeneous auxiliary sector, or an incoherent positive sum of homogeneous sectors, cannot supply the missing zero-frequency orientation.

## Derivation

The key point is elementary frequency bookkeeping and does not use commutation.

Take a source Bohr eigenoperator `a_\omega\in A` and a homogeneous ambient operator `b_\nu\in C`. Then

\[
\begin{aligned}
\gamma_t(b_\nu^*a_\omega b_\nu)
&=e^{-i\nu t}b_\nu^*\,e^{i\omega t}a_\omega\,e^{i\nu t}b_\nu\\
&=e^{i\omega t}b_\nu^*a_\omega b_\nu.
\end{aligned}
\tag{4}
\]

The auxiliary frequency cancels between the two sides of the positive sandwich. Since `\Omega` is invariant,

\[
\Omega(b_\nu^*a_\omega b_\nu)
=e^{i\omega t}\Omega(b_\nu^*a_\omega b_\nu)
\qquad(t\in\mathbb R).
\tag{5}
\]

For `\omega\ne0`, choose `t` with `e^{i\omega t}\ne1`; equation (1) follows.

Equivalently, for arbitrary `a\in A`,

\[
\begin{aligned}
\psi_{b_\nu}(\alpha_t(a))
&=\Omega(b_\nu^*\alpha_t(a)b_\nu)\\
&=\Omega\!\left(\gamma_t(b_\nu^*ab_\nu)\right)\\
&=\psi_{b_\nu}(a),
\end{aligned}
\tag{6}
\]

where the scalar phases of `b_\nu^*` and `b_\nu` cancel. Positivity is automatic because `a\succeq0` implies `b_\nu^*ab_\nu\succeq0`.

For a family `(b_j)` with each `b_j` homogeneous, every functional

\[
\psi(a)=\sum_j \Omega(b_j^*ab_j)
\tag{7}
\]

is again positive and invariant whenever the sum is well defined. The frequencies of different `b_j` may differ; what matters is that each Kraus/sandwich term is **diagonal in its own Bohr label**. There are no cross terms `b_i^*ab_j` with `i\ne j` from which a compensating relative frequency could arise.

Now suppose an equivariant conditional expectation `E:C\to A` is present. Then

\[
\begin{aligned}
\alpha_t(\Phi_{b_\nu}(a))
&=\alpha_t\!\left(E(b_\nu^*ab_\nu)\right)\\
&=E\!\left(\gamma_t(b_\nu^*ab_\nu)\right)\\
&=E(b_\nu^*\alpha_t(a)b_\nu)\\
&=\Phi_{b_\nu}(\alpha_t(a)).
\end{aligned}
\tag{8}
\]

Hence `\Phi_{b_\nu}` is a positive, indeed completely positive, source-time-covariant map. The same is true for sums of homogeneous sandwich terms. This places the operator-valued expected construction exactly inside the class already classified by `WP-225`.

## Bost-Connes consequence

For a finite prime set `F`, write the critical one-prime Poisson factor with `r_p=p^{-1/2}` as

\[
G_p
=I+\sum_{k\ge1}r_p^k\bigl(S_p^k+(S_p^*)^k\bigr),
\tag{9}
\]

where the series is absolutely convergent in operator norm. The finite critical Weil defect is therefore

\[
W_F
=\sum_{p\in F}(\log p)(I-G_p)
=-\sum_{p\in F}(\log p)\sum_{k\ge1}p^{-k/2}
\bigl(S_p^k+(S_p^*)^k\bigr).
\tag{10}
\]

Every summand in (10) has nonzero Bost-Connes time frequency `\pm k\log p`; the zero-frequency component is exactly absent. Therefore every homogeneous noncommuting sandwich functional above gives

\[
\boxed{\psi_{b_\nu}(W_F)=0.}
\tag{11}
\]

The same holds for every positive sum (7). This is stronger than merely saying that a particular matrix element vanishes: the entire finite defect disappears under this class of positive scalar readouts.

If instead the construction keeps an operator-valued source output through an equivariant normal expectation, (8) makes that output a normal positive source-time-covariant image of `W_F`. `WP-225` then gives the exact dichotomy: the output is either zero or indefinite; it cannot be a nonzero positive completion.

Thus a noncommuting auxiliary operator does not by itself evade the earlier KMS obstructions. What matters is whether the construction can **change Bohr degree before positivity is invoked**.

## Matched control: coherent multi-frequency interference is a real escape

The homogeneity hypothesis is load-bearing. A nonhomogeneous auxiliary can generate cross terms whose relative auxiliary frequency cancels the source frequency.

Take `C=M_2`,

\[
H=\operatorname{diag}(0,E),
\qquad
\gamma_t(x)=e^{itH}xe^{-itH},
\]

and let `\Omega_\beta` be the faithful Gibbs `\beta`-KMS state. Put

\[
a=e_{01},
\qquad
b=1+e_{01}.
\]

Here `a` has frequency `-E`, while `b` is a coherent sum of the zero-frequency and `-E` sectors. Direct multiplication gives

\[
b^*ab=e_{01}+e_{11},
\tag{12}
\]

so

\[
\Omega_\beta(b^*ab)=\Omega_\beta(e_{11})>0.
\tag{13}
\]

The invariant contribution `e_{11}` is exactly a cross-frequency interference term: the `+E` component in `b^*` cancels the `-E` frequency of `a`. The map `a\mapsto b^*ab` remains completely positive even though `b` is not homogeneous.

This control prevents overclaiming. Positivity of a sandwich does **not** in general force source-frequency preservation. It does so for a Bohr-diagonal Kraus realization, where each positive term uses one homogeneous sector on both sides. A coherent source-forced superposition of distinct auxiliary frequencies is therefore a genuine surviving category.

## Relation to the current obstruction chain

`WP-412` records the basic KMS selection rule for homogeneous observables in passive Bost-Connes fibre systems. The present result moves that rule into the coupled-extension setting and shows that an apparently stronger operation—surrounding the source observable by a genuinely noncommuting positive sandwich—still leaves its source Bohr frequency unchanged whenever the auxiliary belongs to one dynamical spectral sector.

`WP-425` eliminates product-dynamics compensation even for correlated KMS states. `WP-426` then warns that arbitrary state-selected interacting dynamics is programmable. `WP-427` removes commuting compensation in every source-preserving KMS extension but deliberately leaves noncommuting auxiliaries open. The present finding closes the first natural part of that survivor: **noncommuting but Bohr-diagonal positive sandwiches**.

The remaining branch now has an explicit extra burden. It needs a source-derived rule that fixes relative phases and amplitudes between at least two distinct auxiliary Bohr sectors so that cross terms can move the finite defect into total frequency zero. Merely having noncommutativity, an active fibre, or an interacting ambient algebra does not provide such a rule. If an equivariant expectation reduces the construction to a source-time-covariant positive map, `WP-225` closes it again.

## Prior-art and novelty audit

The generic ingredients are classical. KMS states are invariant under their defining time evolution, and invariant functionals annihilate nonzero spectral subspaces of a one-parameter automorphism group; standard C*-dynamical/KMS treatments include Bratteli and Robinson, *Operator Algebras and Quantum Statistical Mechanics II*. The quantum-resource-theory formulation of the same harmonic principle is developed by Marvian and Spekkens, *Modes of asymmetry*, Phys. Rev. A **90** (2014), 062110: symmetry-covariant processing preserves asymmetry/frequency modes rather than manufacturing a missing mode.

No novelty is claimed for frequency conservation, homogeneous Kraus covariance, conditional expectations, or KMS invariance. The Mathia-specific delta is the exact placement of the **noncommuting escape left open by `WP-427`**. A positive source readout constructed from homogeneous ambient sandwiches is not a new completion category: scalarization kills the critical defect, while an equivariantly expected operator-valued version reduces to the source-time-covariant class already ruled out by `WP-225`.

This is not identical to `WP-412`, whose object is a passive decorated Bost-Connes word, nor to `WP-427`, whose decisive hypothesis is membership in the source relative commutant. Here the auxiliary may fail to commute maximally with the source; the decisive hypothesis is instead **Bohr diagonality of the positive sandwich**. The `M_2` control shows that removing that hypothesis changes the conclusion immediately.

## Boundary conditions and falsification

The result does not classify arbitrary noncommuting correspondences, nonhomogeneous Kraus operators, or coherent matrices of cross-sandwiches. In particular, terms

\[
b_\nu^*a_\omega b_\mu
\]

have total frequency

\[
\omega+\mu-\nu,
\tag{14}
\]

and can survive an invariant/KMS scalar readout exactly when `\nu-\mu=\omega`. Such terms are absent from the diagonal positive sum (7) but appear when a positive sandwich uses a nonhomogeneous coherent operator `b=\sum_\nu b_\nu`.

The theorem also assumes that the ambient flow restricts to the original source dynamics. A genuinely source-derived deformation of the Bost-Connes flow lies outside it, subject to the programmability and exterior-equivalence controls already recorded in `WP-254` and `WP-426`.

For the operator-valued statement, equivariance of the conditional expectation and normality in the finite-prime representation are load-bearing for the direct appeal to `WP-225`. Without an equivariant retraction to the source, an ambient positive output is not classified here.

A decisive falsification of the main theorem would be a `\gamma`-invariant state, a nonzero source Bohr eigenoperator `a_\omega`, and a homogeneous `b_\nu` with `\Omega(b_\nu^*a_\omega b_\nu)\ne0`; equation (4) shows that this would contradict invariance itself. By contrast, a nonzero mixed-sector example such as (12)--(13) is not a falsification; it lies exactly on the surviving boundary.

## Consequence for the Weil program

The Bost-Connes completion clue remains unresolved, but its active KMS/correspondence branch is sharper. After `WP-427`, it was necessary to leave the source relative commutant. After the present result, it is also necessary to leave **Bohr-diagonal positive sandwiching** if the original source flow is retained.

The next admissible construction must therefore derive, from arithmetic source data and before inspecting the Weil sign, a coherent relation between distinct ambient Bohr sectors (or a genuinely new source flow) whose cross terms generate the required zero-frequency orientation. That construction must still recover the exact coefficients `-\log p\,p^{-k/2}`, produce the Gamma and polar sectors from the same global structure, survive the matched nonarithmetic controls in the line mandate, and prove positivity independently of RH or target-coded spectral data.

This finding supplies no such bridge and no RH consequence. It removes a natural class of false noncommuting KMS completions and identifies the precise additional resource—source-forced **cross-frequency coherence**—that a surviving positive sandwich architecture would have to explain.