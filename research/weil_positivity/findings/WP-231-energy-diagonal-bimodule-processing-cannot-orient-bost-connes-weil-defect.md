# WP-231 — Energy-diagonal bimodule processing cannot orient the Bost–Connes Weil defect

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-GRAM + ENERGY-DIAGONAL-MASA + BIMODULE-MAP + ASYMMETRIC-LEFT-RIGHT-WEIGHTING + HOLLOWNESS-INVARIANCE + POSITIVITY-ANNIHILATION + MODULAR-SPATIAL-BOUNDARY + MATCHED-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICAL-MODULE-MAPS + NOT-A-WEIL-BRIDGE`.

`WP-230` closes faithful positive metric congruence around the already-formed critical Bost--Connes Weil defect but deliberately leaves asymmetric/spatial operator constructions open. A substantial same-space subclass of that escape can be closed without assuming that the processing map itself is positive, completely positive, unital, normal, or even symmetric between its two legs.

Fix a nonempty finite prime set `F`. Let

\[
\mathcal H_F=\ell^2(\mathbb N_0^F),
\qquad
\mathcal D_F=W^*(H_F)
\]

be the exponent Hilbert space and the atomic state-energy masa. Let `W_F` be the source-forced finite critical Weil defect from `WP-216`/`WP-223`. In the exponent basis its diagonal vanishes identically:

\[
P_\alpha W_F P_\alpha=0,
\qquad
P_\alpha=|e_\alpha\rangle\langle e_\alpha|.
\tag{1}
\]

Now let

\[
\Psi:B(\mathcal H_F)\to B(\mathcal H_F)
\]

be any bounded linear `D_F`-bimodule map,

\[
\Psi(d_1Xd_2)=d_1\Psi(X)d_2
\qquad
(d_1,d_2\in\mathcal D_F).
\tag{2}
\]

Then every diagonal corner of the processed defect still vanishes:

\[
\boxed{
P_\alpha\Psi(W_F)P_\alpha
=
\Psi(P_\alpha W_FP_\alpha)
=0.
}
\tag{3}
\]

Consequently

\[
\boxed{
\Psi(W_F)\succeq0
\quad\Longrightarrow\quad
\Psi(W_F)=0.
}
\tag{4}
\]

If `Psi(W_F)` is self-adjoint and nonzero, it is necessarily indefinite. Thus **no same-space operation that remains a bimodule over the source energy algebra can turn the already-formed Bost--Connes defect into a nonzero positive operator**, even when the left and right weights differ and even when the operation is not a positive map.

This strictly enlarges the operator class eliminated by `WP-223` and `WP-224` in the direction left open by `WP-230`. It includes arbitrary bounded finite sums of asymmetric energy-diagonal left/right multipliers and their self-adjoint symmetrizations. In particular, bounded modular interpolations of the form

\[
M_s(W_F)
=
\frac12\left(
 e^{-sH_F}W_Fe^{-(1-s)H_F}
+
 e^{-(1-s)H_F}W_Fe^{-sH_F}
\right),
\qquad 0\le s\le1,
\tag{5}
\]

remain indefinite for every nonempty `F`: their prime-axis edges are merely rescaled by strictly positive energy factors, while the diagonal stays zero.

The obstruction is deliberately narrower than a no-go for all modular or spatial constructions. A correspondence that uses noncommuting source data, changes representation or Hilbert space, creates finite--archimedean zero-frequency content before the defect is formed, or is genuinely domain-sensitive and unbounded is outside (2). The result instead identifies the exact point where an apparently asymmetric repair is still only **energy-diagonal post-processing** and therefore cannot be the missing sign-producing geometry.

## 1. Exact source object and hollow structure

For `alpha in N_0^F`, the finite-prime Bost--Connes Hamiltonian is

\[
H_Fe_\alpha
=
E_\alpha e_\alpha,
\qquad
E_\alpha=\sum_{p\in F}\alpha_p\log p.
\tag{6}
\]

Unique factorization makes the spectrum simple, so `D_F=W^*(H_F)` is exactly the bounded diagonal algebra in the exponent basis.

The critical conditional Gram derived in `WP-216` has one-prime kernel

\[
G_p(a,b)=p^{-|a-b|/2},
\tag{7}
\]

and the finite Weil defect is

\[
W_F
=
\sum_{p\in F}(\log p)(I-G_p),
\tag{8}
\]

with each `G_p` acting on its own exponent coordinate. Hence

\[
\langle e_\alpha,W_Fe_\alpha\rangle=0
\tag{9}
\]

for every `alpha`. If `alpha != beta`, the only nonzero matrix entries occur when the two exponent vectors differ in one coordinate `p`, in which case

\[
\langle e_\alpha,W_Fe_\beta\rangle
=
-(\log p)p^{-|\alpha_p-\beta_p|/2}.
\tag{10}
\]

Thus the desired finite arithmetic interaction is carried entirely by off-diagonal prime-axis coherences. The source energy algebra is diagonal with respect to precisely the basis in which those coherences are hollow.

## 2. Bimodule locality preserves every zero diagonal corner

Equation (3) is immediate but is the load-bearing point. Since every rank-one energy projection `P_alpha` belongs to `D_F`, the bimodule identity gives

\[
P_\alpha\Psi(W_F)P_\alpha
=
\Psi(P_\alpha W_FP_\alpha).
\tag{11}
\]

By (1), the right side is zero. Therefore

\[
\langle e_\alpha,\Psi(W_F)e_\alpha\rangle=0
\qquad
\text{for every }\alpha.
\tag{12}
\]

No expansion of `Psi` into Kraus operators, Schur multipliers, or a convergent sum of elementary left/right maps is needed. No positivity or normality hypothesis on `Psi` is used. The conclusion follows solely from its retaining the source energy algebra as a two-sided module.

Suppose now that

\[
A:=\Psi(W_F)\succeq0.
\]

Then (12) implies

\[
\|A^{1/2}e_\alpha\|^2
=
\langle e_\alpha,Ae_\alpha\rangle
=0
\tag{13}
\]

for every basis vector, so `A^{1/2}=0` and `A=0`. This proves (4).

If instead `A=A^*` and `A != 0`, some off-diagonal matrix element

\[
z=\langle e_\alpha,Ae_\beta\rangle
\]

is nonzero. The two-dimensional principal compression is

\[
\begin{pmatrix}
0&z\\
\overline z&0
\end{pmatrix},
\tag{14}
\]

with eigenvalues `+|z|` and `-|z|`. Hence every nonzero self-adjoint bimodule image has strict directions of both signs.

This is stronger than merely saying that a particular positive congruence preserves inertia. The map may be nonpositive and may combine many asymmetric left/right source weights. As long as it does not leave the `D_F`-bimodule category, it cannot create the diagonal mass required by a nonzero positive output.

## 3. Asymmetric left/right source weights are inside the theorem

Let `A_j,B_j in D_F` and suppose

\[
\Psi(X)=\sum_{j=1}^N A_jXB_j.
\tag{15}
\]

Because the coefficients commute with every element of `D_F`, (15) is a `D_F`-bimodule map. Therefore any self-adjoint combination of such terms is either zero or indefinite on `W_F`.

The simplest asymmetric Hermitianization is

\[
T_{A,B}(W_F)
=
\frac12\left(AW_FB+B^*W_FA^*\right).
\tag{16}
\]

It is self-adjoint, and its diagonal is zero by (3). Thus

\[
\boxed{
T_{A,B}(W_F)\succeq0
\quad\Longrightarrow\quad
T_{A,B}(W_F)=0.
}
\tag{17}
\]

This remains true even when `A` and `B` have very different spectra or supports. If their support choices kill all prime-axis edges, the result is zero; if any edge survives, the output has a `2 x 2` compression of the form (14) and is indefinite.

The modular interpolation (5) makes the boundary especially concrete. For an edge joining `alpha` and `beta`, its coefficient is

\[
-\frac{\log p}{2}
 p^{-|\alpha_p-\beta_p|/2}
\left(
 e^{-sE_\alpha-(1-s)E_\beta}
+
 e^{-(1-s)E_\alpha-sE_\beta}
\right),
\tag{18}
\]

which is strictly negative. Hence no edge is annihilated for finite energies, while every diagonal entry remains zero. Therefore `M_s(W_F)` is genuinely nonzero and indefinite for every `s in [0,1]`.

At `s=1/2`, this is the symmetric Gibbs-like congruence already covered by the faithful-metric principle of `WP-230`. The present result shows that moving away from the symmetric midpoint does not open a sign mechanism as long as both legs remain functions of the same state Hamiltonian.

## 4. Relation to the earlier Bost--Connes no-go chain

`WP-223` proves that spectral projections and diagonal congruences from the state Hamiltonian either annihilate the critical defect or leave it indefinite. That result treats vector selection and a single equal left/right diagonal weight.

`WP-224` treats a different extension: a UCP operation fixing the energy masa pointwise. The multiplicative-domain theorem then implies that such a map is a `D_F`-bimodule Schur channel, so hollowness survives. `WP-225` enlarges the positive-map side further: every normal positive map covariant with the source time action preserves the absence of zero Bohr frequency and therefore cannot produce nonzero positivity.

The present theorem removes assumptions in the **spatial/asymmetric** direction rather than the positive-channel direction. A `D_F`-bimodule map need not itself be positive, UCP, unital, normal, or described by a probability kernel. Nevertheless it is unable to orient `W_F`, because bimodule locality alone prevents off-diagonal source information from feeding the diagonal.

This matters after `WP-230`. A faithful positive metric congruence is symmetric by construction, so one natural attempted escape is to use different source densities on the left and right and Hermitianize only afterwards. Equations (16)--(18) show that this does not change category if the two legs remain energy-diagonal. The apparent asymmetry changes amplitudes but not the structural reason for indefiniteness.

## 5. Matched control and exact generality

The theorem is not arithmetic-specific. Let `H` be any Hilbert space with a fixed orthonormal basis `(e_i)`, let `D` be the associated atomic masa, and let `X=X^*` be any bounded hollow operator,

\[
\langle e_i,Xe_i\rangle=0
\qquad\text{for all }i.
\tag{19}
\]

For every bounded `D`-bimodule linear map `Psi`,

\[
\boxed{
\Psi(X)\succeq0
\Longrightarrow
\Psi(X)=0.
}
\tag{20}
\]

If the output is self-adjoint and nonzero, it is indefinite. Randomized edge weights, generalized-product systems, arbitrary positive radii in place of `p^{-1/2}`, and non-prime logarithmic energy scales obey exactly the same obstruction.

That genericity is appropriate for a negative classification result. It shows that an alleged sign theorem obtained only by diagonal bimodule processing would not use the Riemann-specific source structure. A genuine positive bridge must leave this generic category and explain why the additional operation is forced by the arithmetic/global geometry.

## 6. Prior-art and novelty audit

The abstract module-map language is classical. Takashi Itoh and Masaru Nagisa, *Schur Products and Module Maps on B(H)*, Publications of the Research Institute for Mathematical Sciences **36** (2000), 253--268, DOI `10.2977/PRIMS/1195143103`, characterizes Schur product maps through completely bounded module maps. Rupert Levene, Nico Spronk, Ivan G. Todorov, and Lyudmyla Turowska, *Schur Multipliers of Cartan Pairs*, Proceedings of the Edinburgh Mathematical Society **60** (2017), 413--440, DOI `10.1017/S0013091516000067`, develops the general identification of Schur multipliers with normal bimodule maps for Cartan masas.

No novelty is claimed for masa bimodule maps, Schur multipliers, or the elementary fact that a positive operator with zero diagonal in a complete orthonormal basis must vanish. The proof above intentionally needs less than the classical Schur-multiplier representation theorem: equation (11) follows directly from the bimodule identity.

A bounded literature audit across atomic masa bimodule maps, Schur multipliers, Bost--Connes systems, modular weighting, and Weil positivity did not expose a published theorem identifying this particular critical Bost--Connes defect with the no-go (4). The nearby arithmetic prior art instead changes the global object. The Connes--Consani archimedean positivity construction uses compression of the scaling action on a source-defined orthogonal complement, while the Connes--Consani--Marcolli adelic/cohomological program introduces global correspondences and a trace pairing. Those are not energy-diagonal post-processings of the fixed finite defect and therefore are not instances of (2).

The durable Mathia delta is correspondingly narrow: **once the source-forced Bost--Connes Gram has produced the correct critical finite amplitudes but the wrong Weil orientation, every same-space asymmetric left/right operation that remains bimodular over the state-energy algebra is sign-inert in exactly the same sense as the symmetric metric repair**.

## 7. Exact boundary and surviving route

Several escapes remain genuine and are not ruled out.

First, a noncommuting source operator can break the `D_F`-bimodule identity and convert off-diagonal information into diagonal mass. Such an operator must be derived independently from the source; choosing it because it makes the result positive would reproduce the sign-programming problem of `WP-222`.

Second, a finite--archimedean interaction may be formed before `W_F` exists. As `WP-225` already emphasizes, coupling a finite mode of frequency `omega` to an archimedean mode of frequency `-omega` can create a new zero-total-frequency sector. That is a real category change because the completed source is no longer hollow relative to the original finite energy masa.

Third, a correspondence between different Hilbert spaces or representations need not be a same-space `D_F`-bimodule map. A genuinely spatial or Morita-type construction may have different left and right algebras and a nontrivial relative modular operator. The theorem does not classify that situation.

Fourth, unbounded asymmetric products can have domain and boundary terms not visible to a bounded map on `B(H_F)`. `WP-230` already treats arbitrary unbounded **symmetric** faithful metric congruence, but the fully asymmetric unbounded/domain-sensitive category remains open. Any proposal there must specify a common dense domain, closability, adjoint relation, source selection, and how boundary terms produce the Gamma and polar sectors without target tuning.

Finally, nonlinear Gram squares, absolute values, shorting to a new space, or operator-valued distributional pairings lie outside (2). Earlier findings explain why several of those categories lose the signed Weil orientation or become source-programmable, but the present theorem does not extend those conclusions by analogy.

The live frontier is therefore sharper than the phrase "asymmetric/spatial construction" alone suggests. Merely putting different functions of the Bost--Connes Hamiltonian on the two sides of the same finite defect is **not** a new relational geometry. A survivor must introduce a source-forced relation that is non-diagonal relative to the finite state energy, changes representation/category, or couples the finite and archimedean sectors before the final positive scalarization. It must still recover the repeated-prime-power coefficients, Gamma term, polar normalization, and an independent positivity theorem.

## 8. Research disposition

This passes the substantive-finding gate as a decisive narrowing of a live route exposed explicitly after `WP-230`. The result does not prove Weil positivity or RH and is not presented as new operator theory. It closes the bounded same-space **energy-diagonal bimodule** subclass of asymmetric/spatial repairs of the critical Bost--Connes defect.

The Bost--Connes completion clue remains unresolved. Its surviving burden is now more specific: any successful asymmetric or modular completion must derive genuinely noncommuting left/right structure, a different representation/correspondence, an unbounded boundary mechanism, or active finite--archimedean incidence before positivity is read off. Energy-diagonal bimodule asymmetry alone cannot supply the missing sign.