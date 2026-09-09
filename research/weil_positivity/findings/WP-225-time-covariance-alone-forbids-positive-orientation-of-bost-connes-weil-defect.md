# WP-225 — Time covariance alone forbids positive orientation of the Bost–Connes Weil defect

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-GRAM + SOURCE-TIME-COVARIANCE + NORMAL-POSITIVE-MAP + BOHR-MODE-PRESERVATION + HOLLOW-DEFECT + POPULATION-TRANSFER-NO-GO + DECISIVE-NARROWING + PRIOR-ART-CLASSICAL-MODE-THEORY + NOT-A-WEIL-BRIDGE`.

`WP-224` proves that a unital completely positive channel which fixes the Bost--Connes state-energy masa pointwise cannot turn the source-forced finite Weil defect into a nonzero positive operator. Its explicit boundary leaves open channels that **change energy populations**, because such channels need not fix the diagonal algebra pointwise.

That escape is still too large. Pointwise energy nondemolition is not needed. It is enough to preserve the **source time symmetry**.

Fix a nonempty finite prime set `F`, let

\[
H_F e_\alpha=E_\alpha e_\alpha,
\qquad
E_\alpha=\sum_{p\in F}\alpha_p\log p,
\]

and let

\[
\tau_t(X)=e^{itH_F}Xe^{-itH_F}.
\]

Let `Phi:B(H_F)->B(H_F)` be any **normal positive** linear map satisfying the time-covariance law

\[
\Phi\circ\tau_t=\tau_t\circ\Phi
\qquad(t\in\mathbb R).
\tag{1}
\]

No unitality, trace preservation, detailed balance, KMS preservation, or pointwise fixing of the energy diagonal is assumed. In particular, `Phi` is allowed to redistribute diagonal populations whenever covariance permits it.

For the critical Bost--Connes finite-place Weil defect `W_F` of `WP-216`, one nevertheless has

\[
\boxed{
\Phi(W_F)\succeq0
\quad\Longrightarrow\quad
\Phi(W_F)=0.
}
\tag{2}
\]

Equivalently, every nonzero normal positive **source-time-covariant** image of `W_F` is indefinite. The reason is exact: `W_F` has no zero-Bohr-frequency component, and time covariance cannot convert nonzero frequency modes into zero frequency. Since the source Hamiltonian has simple spectrum, the zero-frequency algebra is precisely the diagonal masa. Hence `Phi(W_F)` remains hollow even though `Phi` may act nontrivially on populations of other inputs, and a nonzero hollow self-adjoint operator cannot be positive.

This closes the principal channel-theoretic escape deliberately left open by `WP-224`: **population transfer does not help if it is still covariant with the original Bost--Connes time evolution**. A surviving channel mechanism must therefore break or enlarge the source time symmetry, use a singular/non-normal or unbounded category, or form an active mixed-prime/finite--archimedean interaction before the finite defect enters the channel. Such extra structure must itself be source-derived rather than selected because it repairs the Weil sign.

## 1. The critical defect has no zero-frequency component

On the finite-prime exponent space

\[
\mathcal H_F=\ell^2(\mathbb N_0^F),
\]

unique factorization makes the energy spectrum simple:

\[
E_\alpha=E_\beta
\iff
\prod_{p\in F}p^{\alpha_p}
=
\prod_{p\in F}p^{\beta_p}
\iff
\alpha=\beta.
\tag{3}
\]

Thus the fixed-point algebra of `tau` is exactly

\[
\operatorname{Fix}(\tau)=W^*(H_F)=\mathcal D_F,
\tag{4}
\]

the diagonal masa in the exponent basis.

`WP-216` derives the critical conditional Bost--Connes Gram, and `WP-223` records the corresponding finite defect as

\[
W_F
=
\sum_{p\in F}(\log p)(I-G_p),
\qquad
G_p(a,b)=p^{-|a-b|/2}
\tag{5}
\]

on the `p` coordinate. Each `G_p` is bounded and `F` is finite, so `W_F` is a bounded self-adjoint operator. Its diagonal vanishes identically:

\[
\langle e_\alpha,W_Fe_\alpha\rangle=0
\qquad(\alpha\in\mathbb N_0^F).
\tag{6}
\]

Every nonzero matrix element joins two distinct energies. If `alpha` and `beta` differ only in the coordinate `p`, then

\[
\langle e_\alpha,W_Fe_\beta\rangle
=
-(\log p)p^{-|\alpha_p-\beta_p|/2},
\tag{7}
\]

and the associated Bohr frequency is

\[
\omega_{\alpha\beta}
=E_\alpha-E_\beta
=(\alpha_p-\beta_p)\log p\ne0.
\tag{8}
\]

If they differ in at least two coordinates, the matrix element in `W_F` is zero. Therefore the entire zero-frequency component of `W_F` vanishes.

## 2. Covariance forces every output diagonal matrix element to remain zero

The statement can be proved without choosing a Kraus representation and without summing an infinite Bohr-mode expansion.

Fix an output basis vector `e_gamma` and define the normal functional

\[
f_\gamma(X)
=
\langle e_\gamma,\Phi(X)e_\gamma\rangle.
\tag{9}
\]

Because `Phi` is normal, `f_gamma` is a normal functional on `B(H_F)`. Covariance (1) and the fact that `e_gamma` is an energy eigenvector give

\[
\begin{aligned}
f_\gamma(\tau_t(X))
&=
\langle e_\gamma,\Phi(\tau_t(X))e_\gamma\rangle\\
&=
\langle e_\gamma,\tau_t(\Phi(X))e_\gamma\rangle\\
&=
f_\gamma(X).
\end{aligned}
\tag{10}
\]

Hence `f_gamma` is invariant under the source time action.

Every normal functional on `B(H_F)` has the form

\[
f_\gamma(X)=\operatorname{Tr}(T_\gamma X)
\tag{11}
\]

for a trace-class operator `T_gamma`. Invariance (10) implies

\[
e^{-itH_F}T_\gamma e^{itH_F}=T_\gamma
\qquad(t\in\mathbb R).
\tag{12}
\]

By the simple spectrum (3), `T_gamma` is diagonal in the exponent basis. Combining this with (6),

\[
\operatorname{Tr}(T_\gamma W_F)=0.
\tag{13}
\]

Therefore

\[
\boxed{
\langle e_\gamma,\Phi(W_F)e_\gamma\rangle=0
\qquad\text{for every }\gamma.
}
\tag{14}
\]

This is the crucial strengthening over `WP-224`. There the zero output diagonal followed from the multiplicative-domain theorem because the channel fixed `D_F` pointwise. Here `Phi` need not fix any nonconstant diagonal observable. It may mix populations. The output diagonal still vanishes **for this particular input** because that input contains only nonzero time-asymmetry modes and a covariant map cannot feed them into the invariant mode.

## 3. Positivity then forces annihilation

A positive linear map is star-preserving on self-adjoint inputs, so

\[
A:=\Phi(W_F)=A^*.
\tag{15}
\]

Suppose `A` were positive. Equation (14) gives

\[
\|A^{1/2}e_\gamma\|^2
=
\langle e_\gamma,Ae_\gamma\rangle
=0
\tag{16}
\]

for every basis vector. Hence `A^{1/2}` annihilates a complete orthonormal basis and therefore

\[
A=0.
\tag{17}
\]

This proves (2).

The stronger indefinite alternative is equally elementary. If `A` is nonzero while all of its diagonal entries vanish, some off-diagonal entry

\[
z=\langle e_\alpha,Ae_\beta\rangle
\]

is nonzero. The two-dimensional principal compression is

\[
\begin{pmatrix}
0&z\\
\overline z&0
\end{pmatrix},
\tag{18}
\]

with eigenvalues `+|z|` and `-|z|`. Thus

\[
\boxed{
\Phi(W_F)\ne0
\quad\Longrightarrow\quad
\Phi(W_F)\text{ is indefinite}.
}
\tag{19}
\]

No complete positivity is required for this conclusion. Normality, positivity, and exact covariance with the source time action suffice.

## 4. What population transfer does and does not buy

A time-covariant channel need not be energy-nondemolition in the sense of `WP-224`. Covariance constrains **energy differences**, not individual energy populations. It can therefore act nontrivially on the diagonal fixed-point algebra and, in a suitable system, induce genuine population dynamics while preserving each Bohr-frequency sector.

That extra freedom is irrelevant for `W_F`. Its diagonal/zero-frequency sector is exactly zero before the channel. Equation (14) says the channel cannot manufacture an invariant component from its nonzero-frequency edges. Consequently a KMS-preserving, detailed-balance, thermalizing, or Davies-type operation does not evade the obstruction **whenever the particular map is normal, positive, and covariant with this same source time evolution**. Those stronger thermodynamic properties are not used by the proof.

This distinction matters. `WP-224` rules out the pointwise-diagonal-fixing subclass through multiplicative-domain/Schur rigidity. The present theorem rules out the larger covariance class through harmonic-mode rigidity. The two mechanisms are logically different:

\[
\text{fix }\mathcal D_F\text{ pointwise}
\Longrightarrow
\text{Schur channel}
\Longrightarrow
\text{hollowness},
\tag{20}
\]

whereas here

\[
\text{time covariance}
\Longrightarrow
\text{Bohr-mode preservation}
\Longrightarrow
\text{hollowness of }\Phi(W_F).
\tag{21}
\]

The second implication survives even when the diagonal algebra itself is not fixed pointwise.

## 5. Matched control: the theorem is category-generic

The proof uses no primality, no Euler product, and no special value of the coefficients in (7) beyond the fact that the source Hamiltonian is nondegenerate and the input has zero invariant component.

More generally, let `H` have simple pure point spectrum with eigenbasis `(e_j)`, let

\[
\tau_t(X)=e^{itH}Xe^{-itH},
\]

and let `A=A^*` be bounded with

\[
\langle e_j,Ae_j\rangle=0
\qquad\text{for every }j.
\tag{22}
\]

Then every normal positive `tau`-covariant map satisfies

\[
\Phi(A)\succeq0
\Longrightarrow
\Phi(A)=0.
\tag{23}
\]

Thus generalized-product systems, randomized logarithmic energies, and non-prime weighted hollow graphs obey the same obstruction. That genericity is appropriate for a **negative classification theorem**: it shows that the failure is caused by the proposed operator category, not by a hidden Riemann-specific identity.

The Mathia-specific content is the exact placement of the source-forced Bost--Connes critical Weil defect inside this category. `WP-216` supplies the arithmetic carrier before the sign is inspected; `WP-225` shows that source-time-covariant positive processing cannot provide the missing orientation.

## 6. Prior-art and novelty audit

The harmonic-analysis statement that symmetry-covariant quantum operations preserve symmetry modes is classical. Iman Marvian and Robert W. Spekkens, *Modes of asymmetry: the application of harmonic analysis to symmetric quantum dynamics and quantum reference frames*, Physical Review A **90** (2014), 062110, DOI `10.1103/PhysRevA.90.062110`, arXiv `1312.0680`, explicitly develops the decomposition of states, measurements, and channels into group-frequency modes and shows that symmetric processing maps an input mode only to the corresponding output mode.

No novelty is claimed for that mode-preservation theorem, for normal-predual duality of `B(H)`, or for the elementary positivity fact that a positive operator with zero diagonal in a complete orthonormal basis is zero. The proof above is deliberately self-contained because the current source object is especially simple.

A targeted audit against Bost--Connes/endomotive and Weil-positivity prior art also leaves the interpretation unchanged. Bost--Connes supplies the logarithmic time evolution but not an independent sign theorem for the completed Weil form. Connes--Consani style semilocal/compressed scaling constructions change the global operator/test-space architecture and therefore lie outside the same-space covariance theorem rather than being rediscoveries of it.

The durable delta is consequently a **route restriction**, not a new general theorem of covariant quantum dynamics: the explicit population-transfer escape left by `WP-224` collapses as soon as the proposed repair is required to remain normal, positive, and covariant with the original finite Bost--Connes time action.

## 7. Aggressive falsification and exact boundary

Several exits remain genuine and must not be overclaimed.

First, **normality is load-bearing** in the proof through the trace-class predual representation of the invariant functionals. A singular covariant positive map is not classified here. Such an escape would have to be derived from the arithmetic/global source and audited for whether it merely hides a target-dependent limiting prescription.

Second, the theorem acts on bounded operators in the same finite-prime `B(H_F)` category. An unbounded closable form, relation-valued response, or singular boundary object can carry information not represented by a bounded normal channel. The line already contains examples where critical arithmetic data naturally sits at a singular boundary, so these categories cannot be dismissed by analogy.

Third, a **new input formed before the channel** is outside the theorem. If a finite-prime mode of frequency `omega` is coupled to an archimedean or mixed-prime mode of frequency `-omega`, their joint product can contain a zero total-frequency component. That is precisely the kind of active finite--archimedean incidence the current research mandate still permits. But the coupling must be source-forced before its sign is read off, and it must simultaneously account for the Gamma and polar sectors.

Fourth, changing the time representation is a real resource. A noncovariant channel, or a covariant channel only after adjoining an external clock/reference frame, can move weight between asymmetry modes. In the language of symmetry-resource theory, the extra reference frame is itself the missing asymmetry resource. For Mathia this is not a free escape: the source must canonically supply that resource, and matched generalized-product controls must not produce the same claimed arithmetic sign for arbitrary systems.

Finally, coinvariant compression, shorting to a new space, nonlinear Gram/absolute-value constructions, and explicit positive diagonal counterterms remain outside (1). `WP-222` shows why quotient selection is dangerous, `WP-218` excludes compact same-space repairs, and the earlier critical-mass results expose divergent scalar compensation. None of those prior obstructions proves that every noncompact global category change fails.

## 8. Consequence for the live Bost–Connes completion clue

The active completion question can now be narrowed further. Starting from the source-forced critical divisibility Gram, a successful sign mechanism cannot be obtained by

\[
\text{finite Weil defect}
\xrightarrow{\text{normal positive source-time-covariant channel}}
\text{positive completed finite operator},
\tag{24}
\]

unless the finite defect is annihilated.

Therefore the live burden has moved beyond both state-energy selection (`WP-223`) and source-time-covariant positive processing (`WP-224`--`WP-225`). The remaining plausible families require an operation that **changes the zero-frequency content before positivity is invoked**: a canonically sourced quotient/shorting, a singular or unbounded global response, or an active mixed-prime/finite--archimedean coupling whose opposite modes generate a new invariant sector.

Any such proposal must still recover the actual finite coefficients `-log p p^{-|k|/2}`, produce the Gamma and polar terms from the same global structure, survive generalized-product controls, and prove nonnegativity independently of RH or inserted zero data. This finding provides no such bridge; it removes one more natural class of false ones.
