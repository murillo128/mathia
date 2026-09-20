# PC-369 — canonical Chen Hopf/Lie structure is matched-control equivariant

- **Finding ID:** `PC-369`
- **Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE`
- **Status detail:** closes the most canonical algebraic cross-grade repair left after PC-368. Shuffle identities, group-likeness, the free-Lie/log-signature constraint, BCH/Magnus combinations, Hopf coproduct/antipode structure, permutation/Lie projections, and unitary tensor contractions are all natural under a common one-particle unitary. They therefore remain exactly equivariant under the Prime-Circle matched reciprocal control of PC-355 and cannot by themselves supply the parity-breaking source structure required by the current frontier.
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact Hopf/Lie naturality obstruction
- **RH relevance:** high as a boundary result. PC-368 shows that mixed tensor grades genuinely retain cross-grade information, but the universal algebraic relations intrinsic to a Chen signature do not turn that information into an arithmetic discriminator.

## Claim

PC-368 leaves a precise opening after the homogeneous and mixed-degree Fock classifications. Heterogeneous tensor levels retain resonant word contractions, but every such contraction is preserved by the common one-particle unitary implementing the exact Prime-Circle matched reciprocal control. A natural next possibility is that the tensor levels are not arbitrary: because they come from a Chen signature, they satisfy source-forced cross-grade Hopf and free-Lie relations. Perhaps those relations could break the common-unitary control even though the bare resonant Gram data do not.

They cannot.

Let `K` be a finite-dimensional complex Hilbert space and let

\[
\widehat T(K)=\prod_{m\ge0}K^{\otimes m}
\tag{1}
\]

be the completed tensor algebra with concatenation product. Give it the standard tensor-Hopf coproduct determined on letters by

\[
\Delta v=v\otimes1+1\otimes v,
\qquad v\in K,
\tag{2}
\]

and extended multiplicatively. Let `epsilon` be the counit and `S` the antipode. For any linear map `J:K->K`, define the degreewise tensor map

\[
\Theta_J
:=\prod_{m\ge0}J^{\otimes m},
\qquad J^{\otimes0}=1.
\tag{3}
\]

If `J` is invertible, then `Theta_J` is a graded Hopf-algebra automorphism:

\[
\boxed{
\Theta_J(xy)=\Theta_J(x)\Theta_J(y),
\qquad
\Delta\Theta_J=(\Theta_J\otimes\Theta_J)\Delta,
\qquad
S\Theta_J=\Theta_J S.
}
\tag{4}
\]

Consequently it preserves every universal Chen constraint:

- group-like elements are sent to group-like elements;
- primitive elements are sent to primitive elements;
- the completed free Lie algebra `\widehat{\mathfrak L}(K)` is invariant;
- logarithm and exponential commute with `Theta_J` on the augmentation-adic domain;
- BCH and Magnus Lie series are carried term-by-term to the corresponding transformed series;
- on the dual coordinate algebra, the shuffle product is preserved under the induced dual change of letters;
- every degreewise operator obtained from tensor permutations, Young/Lie idempotents, grading projections, concatenation, coproduct, antipode, unit and counit is equivariant.

If `J` is unitary, the statement extends to the canonical Hilbert contractions: `J^{\otimes m}` is unitary on every homogeneous tensor sector and commutes with the permutation action. Therefore any scalar obtained by completely contracting tensors produced from the operations above is unchanged under the simultaneous replacement `x -> Theta_J x`.

For the Prime-Circle inversion defect, PC-355 proves exactly

\[
\widetilde{\mathcal D}_S
=\Theta_J(\mathcal D_S),
\qquad
Jc=c,
\qquad
Jb_n=-b_n,
\tag{5}
\]

with `J` a unitary involution on the centered one-particle space. Hence the entire canonical Hopf/Lie package of `\mathcal D_S` and its matched reciprocal control is isomorphic under the same `Theta_J`. In particular,

\[
\boxed{
\log\widetilde{\mathcal D}_S
=\Theta_J\bigl(\log\mathcal D_S\bigr),
}
\tag{6}
\]

and every shuffle identity, primitive/free-Lie identity, BCH/Magnus relation and universal cross-grade tensor identity satisfied by the source is satisfied by the control after the corresponding letter transformation.

Thus **the canonical Chen Hopf/Lie structure is not the missing source-forced parity-breaking relation sought after PC-368**. A surviving construction must use additional Prime-Circle structure that is not natural under arbitrary common one-particle unitaries.

## 1. The tensor Hopf structure is functorial under every linear change of letters

Equation (4) is elementary but decisive here. On a generator `v in K`,

\[
\begin{aligned}
\Delta\Theta_J(v)
&=\Delta(Jv)\\
&=Jv\otimes1+1\otimes Jv\\
&=(\Theta_J\otimes\Theta_J)(v\otimes1+1\otimes v)\\
&=(\Theta_J\otimes\Theta_J)\Delta(v).
\end{aligned}
\tag{7}
\]

Both sides are algebra homomorphisms for concatenation, so equality on letters proves equality on the whole tensor algebra and degreewise on its completion. The antipode relation follows either from uniqueness of the antipode or directly from

\[
S(v_1\cdots v_m)=(-1)^m v_m\cdots v_1,
\tag{8}
\]

because applying one common `J` to every letter commutes with reversal and the degree sign. Unit, counit and tensor grade are equally automatic.

If `G` is group-like,

\[
\Delta G=G\otimes G,
\tag{9}
\]

then

\[
\Delta\Theta_J(G)
=(\Theta_J\otimes\Theta_J)(G\otimes G)
=\Theta_J(G)\otimes\Theta_J(G).
\tag{10}
\]

Likewise, if `L` is primitive,

\[
\Delta L=L\otimes1+1\otimes L,
\tag{11}
\]

then `Theta_J(L)` is primitive. Over characteristic zero the primitive elements of the tensor Hopf algebra form the free Lie algebra on `K`. Thus the free-Lie constraint is not extra rigid structure relative to a linear change of the alphabet: it is itself functorial in that alphabet.

This point is exactly aligned with the PC-368 frontier. The Hopf coproduct does couple tensor degrees, and group-likeness is a genuine cross-grade constraint. But it couples them in a way respected by **every** common linear transformation of the one-particle space. Cross-grade does not automatically mean control-breaking.

## 2. Log-signature, BCH and Magnus data transform covariantly

Let `G=1+g` lie in the augmentation-adic completion. The formal logarithm

\[
\log G
=\sum_{r\ge1}\frac{(-1)^{r+1}}r g^r
\tag{12}
\]

uses only scalar coefficients and concatenation. Therefore

\[
\boxed{
\log\Theta_J(G)=\Theta_J(\log G).
}
\tag{13}
\]

For a group-like `G`, `log G` is primitive, hence a completed free-Lie series. Applied to a path signature this is the classical log-signature. Applied to the regularized Prime-Circle inversion defect, equation (13) gives (6) directly from PC-355.

The same naturality propagates through every Lie polynomial. For example,

\[
\Theta_J([x,y])=[\Theta_Jx,\Theta_Jy],
\tag{14}
\]

and therefore each homogeneous BCH polynomial and each universal Magnus polynomial satisfies

\[
\Theta_J\bigl(\operatorname{BCH}(x,y)\bigr)
=
\operatorname{BCH}(\Theta_Jx,\Theta_Jy),
\tag{15}
\]

with the analogous identity degree by degree for Magnus expansions. Passing from the tensor signature to its logarithm, Hall/Lyndon coordinates, nested commutators, primitive projections, or finite Lie truncations therefore does not break the matched control.

This rules out a tempting interpretation of PC-368. Mixed grades do create contractions that are absent in the homogeneous Wold classification, but reorganizing those grades into canonical Lie coordinates does not make them more source-selective. It is an invertible, functorial re-expression inside the same common-unitary orbit.

## 3. Shuffle identities are the dual statement and are equally control-blind

Coordinate iterated integrals satisfy the shuffle product. If `a` and `b` are tensor covectors and `\shuffle` denotes the shuffle product, a signature `G` obeys

\[
\langle a,G\rangle\langle b,G\rangle
=
\langle a\shuffle b,G\rangle.
\tag{16}
\]

This is dual to group-likeness of `G` for the Hopf structure above. Under the transformed signature `Theta_J(G)`, coordinate covectors transform by the dual map, and

\[
(J^*a)\shuffle(J^*b)
=J^*(a\shuffle b)
\tag{17}
\]

when `J^*` is extended tensorwise. Thus the entire family of shuffle identities is transported bijectively between source and control.

The conclusion is stronger than saying that one chosen shuffle polynomial happens to agree. The **ideal of universal shuffle relations itself** is preserved by the common change of letters. No selection of shuffle identities, without extra structure fixing a non-equivariant coordinate frame, distinguishes `\mathcal D_S` from `\widetilde{\mathcal D}_S`.

The same warning applies to basis choices in the free Lie algebra. Dynkin--Specht--Wever, Eulerian, Hall/Lyndon, or Young-symmetrizer decompositions are built degreewise from permutations and scalar coefficients. Since

\[
J^{\otimes m}\sigma=\sigma J^{\otimes m}
\qquad(\sigma\in\mathfrak S_m),
\tag{18}
\]

they are natural under the same `J`. A striking pattern in one such basis is not yet a source discriminator unless the basis itself is forced by extra Prime-Circle data not carried along by `J`.

## 4. Hilbert contractions and PC-368 resonances remain inside the same obstruction

PC-368's resonant invariants have the form

\[
R_{\alpha,\beta}
=\langle g_\alpha,g_\beta\rangle,
\qquad Q(\alpha)=Q(\beta).
\tag{19}
\]

Their control blindness is a special case of the present naturality. If `J` is unitary and the total grade is `Q`, then

\[
\langle J^{\otimes Q}g_\alpha,
        J^{\otimes Q}g_\beta\rangle
=
\langle g_\alpha,g_\beta\rangle.
\tag{20}
\]

More generally, take any finite tensor network whose vertices are built from the universal Hopf/Lie operations above and whose open legs are closed only by the canonical Hilbert inner product. Applying `J` simultaneously to every one-particle leg cancels on each complete contraction. This gives an exact graphical version of the same obstruction: **universal tensor-category structure plus unitary contractions cannot see which member of a common-unitary orbit generated the data**.

This includes cross-grade scalar moments assembled from log-signature pieces, primitive projections and resonant contractions. It does not require reducing all such expressions to the explicit word-Gram system of PC-368; equivariance is structural.

## 5. Application to the regularized Prime-Circle inversion defect

For each finite cutoff before regularization, the radial path-ordered exponential and the closing ray are group-like elements. Their product is group-like. The regularized defect is taken degree by degree, and in any fixed tensor degree the Hopf identities are finite polynomial identities, so the degreewise limit remains group-like wherever PC-349/PC-350 define the defect.

PC-355 supplies the stronger identity (5) before any Fock representation is chosen. Therefore the source and control agree not numerically but **categorically** at the level relevant here: `Theta_J` is an isomorphism between their completed graded Hopf objects, their primitive/log-signature Lie objects, and all universal constructions generated from them.

A proposed RH-facing invariant that uses only this package has two possibilities. If it is a scalar invariant under the induced unitary/Hopf isomorphism, it takes the same value on source and matched control. If it is merely covariant, its entire output is transported by `Theta_J` and still provides no intrinsic way to prefer the cyclotomic member without adding further structure. Neither case supplies an arithmetic selector by itself.

No spectral parameter, archimedean gamma factor, `s <-> 1-s` mechanism, zero equation, or critical-line selector arises from the Hopf naturality. Those would have to enter through an additional source-derived operation and survive the README's matched-control and prior-art tests.

## 6. What this theorem does not rule out

The obstruction is deliberately restricted to **universal tensor/Chen structure**. It does not say that every source-forced relation is common-unitary invariant. A construction can escape only by using extra structure on the Prime-Circle alphabet or radial functions that is not transported by an arbitrary `J`.

Examples of logically uncovered data include a fixed divisor/refinement incidence operator on shell labels, pointwise multiplication of the actual radial functions, a source-derived differential or boundary operator tied to the physical radial coordinate, positivity/order/cone structure, or a fixed background tensor that genuinely mixes the calibration direction with transverse directions and is not transformed with the source. These are examples of the **kind** of additional structure required, not endorsed mechanisms: each would still have to be shown intrinsic rather than fitted, to fail an admissible matched control, and to produce something stronger than cyclotomic reconstruction or a classical divisor reformulation.

The theorem also does not cover arithmetic relations of cyclotomic periods that use extra labelled multiplication/distribution data not contained in the universal Chen Hopf algebra. Such relations are precisely where a future continuation would need a separate prior-art audit against cyclotomic multiple polylogarithms, associators, divisor identities and known zeta transforms.

## Prior-art and novelty audit

The abstract mathematics used here is classical. Chen's iterated-integral theory supplies the shuffle identities and the group-like tensor series; Kuo-Tsai Chen, **Iterated integrals of differential forms and loop space homology**, *Annals of Mathematics* 97:2 (1973), 217--246, DOI `10.2307/1970846`, is a primary classical anchor. Hambly--Lyons, **Uniqueness for the signature of a path of bounded variation and the reduced path group**, *Annals of Mathematics* 171:1 (2010), 109--167, DOI `10.4007/annals.2010.171.109`, explicitly uses the shuffle product and tensor signature framework already cited in PC-348/PC-350.

The primitive/free-Lie side is equally standard: the tensor algebra is the universal enveloping algebra of the free Lie algebra, with Lie elements exactly the primitive elements in characteristic zero. Reutenauer's **Free Lie Algebras** (Oxford University Press, 1993) is the standard monograph; the same Hopf characterization is classical Friedrichs/Ree theory. Modern signature literature states the consequence as Chen's theorem that the log-signature is a Lie series; for example Friz--Lyons--Seigal, **Rectifiable paths with polynomial log-signature are straight lines**, arXiv:2305.19210, uses that theorem explicitly.

The naturality under `J` is not claimed as a new Hopf-algebra theorem. It follows directly from the universal definitions and is proved above. A targeted search over Chen signatures, group-like tensor series, log-signatures, free Lie algebras, Lie idempotents and Magnus expansions found these structures as established functorial algebra, not as a new zeta/RH mechanism.

The line-local mathematical delta is narrower and consequential: after PC-368 identifies mixed-grade resonance as a genuine information-retention escape, **the most canonical source-forced cross-grade relations available from the Chen object itself still lie entirely inside PC-355's matched-control orbit**. Thus `use the shuffle/group-like/log-signature structure` is not a viable parity-breaking continuation merely because it couples grades.

## Adversarial / falsification audit

1. **Coproduct convention:** the proof uses the standard tensor-Hopf coproduct with primitive letters. The dual coordinate product is shuffle; confusing this with deconcatenation would mix dual conventions but does not change the functoriality statement.
2. **Completion:** every identity is degreewise finite. No boundedness of the complete signature as an operator is required.
3. **Regularization:** each finite-cutoff inversion defect is a product of group-like path signatures. Degreewise regularization preserves polynomial Hopf identities in every fixed degree.
4. **Logarithm:** `log` is used only in the augmentation-adic completion around scalar term `1`, which is exactly the signature setting.
5. **Unitary contractions:** invariance of Hilbert contractions requires `J` unitary. The Prime-Circle matched-control `J` of PC-355 is a sign involution in the canonical centered orthonormal basis and satisfies this hypothesis.
6. **Basis projections:** permutation/Lie idempotents commute with `J^{otimes m}` because the same `J` acts on every tensor factor. A source-dependent projector not natural in `K` is outside the theorem.
7. **Control validity:** the obstruction uses the exact source/control relation already established in PC-355, not an independently fitted artificial path.
8. **Scope check:** the result does not claim that all cyclotomic identities or all possible cross-level operators are control-blind. Only the universal Chen/Hopf/Lie package and constructions functorially generated from it are closed.
9. **RH check:** no claim of progress toward RH is made. The result is a reusable no-go identifying which extra datum a future spectral construction must actually use.

## Consequence for the Prime-Circle frontier

PC-368's surviving question can now be sharpened. Mixed tensor grades do preserve real source information, but **neither their universal Hopf cross-grade constraints nor passing to log-signature/free-Lie/Magnus coordinates breaks the matched reciprocal control**. The next viable object must therefore combine the faithful tensor data with a second structure that is intrinsic to the roots-of-unity geometry yet not natural under the common one-particle unitary.

This is stricter than asking for more noncommutativity or deeper tensor degree. A candidate must identify the fixed source datum that reduces the common-unitary gauge, prove that the reduction is not merely a labelled cyclotomic/divisor restatement, and show how the resulting observable reaches a zeta/functional-equation/critical-line target. Until such a datum is present, the canonical Chen algebra itself remains a faithful but control-equivariant encoding rather than an RH selector.