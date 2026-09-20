# PC-367 — homogeneous multichannel Fock type is classified by the channel Gram matrix

- **Finding ID:** `PC-367`
- **Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `NUMERICAL-SANITY` + `DECISIVE-NEGATIVE`
- **Status detail:** decisive negative for the finite same-degree multichannel full-Fock escape left open by PC-366: once a finite family of homogeneous Prime-Circle tensors is represented only through its left creators together with tensor grade, the complete joint unitary type retains exactly the channel Gram matrix and no further tensor orientation, entanglement, word-coordinate, or embedding data.
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact multivariable operator-theoretic classification / information-loss boundary
- **RH relevance:** high as a boundary result. Multiple channels do preserve relative pairwise inner products, unlike the single-channel norm collapse of PC-366, but the full homogeneous Fock representation contributes no additional source selectivity beyond that finite Gram data.

## Claim

PC-366 proves that one homogeneous tensor `g in K^{otimes q}` becomes spectrally blind to everything except its degree and norm when used as a full-Fock creation channel next to the number operator. Its explicit boundary leaves open two or more independent homogeneous tensors, since a multichannel tuple might retain relative geometry that one isometry cannot see.

For **any finite labelled family at one common tensor degree**, this remaining freedom can be classified exactly.

Let `K` be a complex Hilbert space of finite dimension `d>=1`, let

\[
\mathcal F(K)=\bigoplus_{n\ge0}K^{\otimes n},
\qquad
N|_{K^{\otimes n}}=nI,
\tag{1}
\]

and fix `q>=1`. For a labelled family

\[
g=(g_1,\ldots,g_m),
\qquad g_i\in K^{\otimes q},
\tag{2}
\]

define the left creators

\[
L_{g_i}\xi=g_i\otimes\xi
\tag{3}
\]

and the channel Gram matrix

\[
G(g)_{ij}:=\langle g_i,g_j\rangle.
\tag{4}
\]

Then for two such labelled families `g` and `h`,

\[
\boxed{
G(g)=G(h)
\iff
\exists\ U\text{ unitary on }\mathcal F(K):
UN=NU,
\quad
UL_{g_i}U^*=L_{h_i}\ \forall i.
}
\tag{5}
\]

Thus, for fixed `(d,q)`, the Gram matrix is the **complete joint unitary invariant** of the tuple

\[
(N,L_{g_1},\ldots,L_{g_m}).
\tag{6}
\]

The implication for spectral constructions is immediate. Every source-independent operator built functorially from `N`, the labelled creators and their adjoints -- including finite matrix-valued/ancilla couplings -- has a unitary class determined only by `G(g)`. Multiple homogeneous Fock channels therefore do not recover the absolute orientation of the source tensors inside `K^{otimes q}`. They retain only their pairwise Hilbert geometry.

This result strictly extends PC-366. For `m=1`, the Gram matrix is the single scalar `||g||^2`, recovering the norm-sphere collapse there. For `m>1`, relative Gram data genuinely survives, so the conclusion is not that multichannel input is scalar. The conclusion is sharper: **all information beyond the finite Gram matrix is gauge for this representation architecture**.

## 1. Orthonormal channel bases form a pure homogeneous row isometry

Let

\[
R_g:=\operatorname{span}\{g_1,\ldots,g_m\}
\subset K^{\otimes q},
\qquad r:=\dim R_g.
\tag{7}
\]

Choose an orthonormal basis `u_1,...,u_r` of `R_g` and put

\[
S_a:=L_{u_a}.
\tag{8}
\]

The Hilbert tensor norm gives

\[
S_a^*S_b=\langle u_a,u_b\rangle I=\delta_{ab}I.
\tag{9}
\]

Hence `S=(S_1,...,S_r)` is a row isometry: each `S_a` is an isometry and the ranges are pairwise orthogonal. Every word `S_\alpha` of length `|alpha|=ell` raises tensor grade by exactly `q ell`.

The common wandering space is

\[
W_g:=\bigcap_{a=1}^r\ker S_a^*
=\mathcal F(K)\ominus\bigl(R_g\otimes\mathcal F(K)\bigr).
\tag{10}
\]

It is graded. Writing `W_{g,k}=W_g cap K^{otimes k}`, one has exactly

\[
\boxed{
\dim W_{g,k}=
\begin{cases}
d^k,&0\le k<q,\\
d^k-rd^{k-q},&k\ge q.
\end{cases}}
\tag{11}
\]

Indeed, at grade `k>=q`, the row range is the orthogonal subspace

\[
R_g\otimes K^{\otimes(k-q)}
\tag{12}
\]

of dimension `r d^{k-q}`. Since `r<=d^q`, (11) is nonnegative.

The row isometry is pure. For word length `ell`, every vector in

\[
\bigoplus_{|\alpha|=\ell}S_\alpha\mathcal F(K)
\tag{13}
\]

has tensor grade at least `q ell`. The intersection of these spaces over all `ell` is therefore zero. Popescu's multivariable Wold decomposition consequently reduces here to

\[
\boxed{
\mathcal F(K)
=
\bigoplus_{\alpha\in\mathbb F_r^+}S_\alpha W_g.
}
\tag{14}
\]

The extra fact needed for Prime Circle is the grading: if `w in W_{g,k}`, then

\[
N(S_\alpha w)=(k+q|\alpha|)S_\alpha w.
\tag{15}
\]

Thus the complete graded multiplicity data of the row shift depends only on `(d,q,r)`, not on how `R_g` sits inside the homogeneous tensor sector.

## 2. Equal Gram matrices give a grade-preserving joint intertwiner

Assume now that

\[
G(g)=G(h).
\tag{16}
\]

Equality of Gram matrices implies equality of all linear relations among the labelled vectors. Therefore the assignment

\[
g_i\longmapsto h_i
\tag{17}
\]

extends uniquely to an isometry

\[
V:R_g\to R_h.
\tag{18}
\]

In particular, `dim R_g=dim R_h=r`. If `u_1,...,u_r` is the orthonormal basis above and

\[
v_a:=Vu_a,
\tag{19}
\]

then `v_1,...,v_r` is an orthonormal basis of `R_h`. Define

\[
T_a:=L_{v_a}.
\tag{20}
\]

The two row isometries `S` and `T` have the same graded wandering multiplicities (11). For every grade `k`, choose a unitary

\[
V_k:W_{g,k}\to W_{h,k}.
\tag{21}
\]

Using the orthogonal Wold decompositions, define

\[
U(S_\alpha w):=T_\alpha V_k w,
\qquad w\in W_{g,k}.
\tag{22}
\]

This is a unitary on `F(K)`. It satisfies

\[
US_a=T_aU
\tag{23}
\]

for every orthonormal channel generator, and (15) shows simultaneously that

\[
UN=NU.
\tag{24}
\]

Now write the labelled source vectors in the chosen basis,

\[
g_i=\sum_{a=1}^r c_{ai}u_a.
\tag{25}
\]

Because `v_a=Vu_a` and `Vg_i=h_i`, the **same coefficients** satisfy

\[
h_i=\sum_{a=1}^r c_{ai}v_a.
\tag{26}
\]

Linearity of left creation gives

\[
L_{g_i}=\sum_a c_{ai}S_a,
\qquad
L_{h_i}=\sum_a c_{ai}T_a.
\tag{27}
\]

Equations (23) and (27) therefore yield

\[
\boxed{UL_{g_i}U^*=L_{h_i}\quad\text{for every labelled channel }i,}
\tag{28}
\]

while (24) preserves tensor grade. This proves the nontrivial direction of (5).

The converse is even more rigid. If a unitary jointly intertwines the creator tuples, then

\[
L_{g_i}^*L_{g_j}
=\langle g_i,g_j\rangle I
\tag{29}
\]

is conjugated to

\[
L_{h_i}^*L_{h_j}
=\langle h_i,h_j\rangle I.
\tag{30}
\]

Hence every Gram entry agrees. The `N` condition is not needed for this converse; it is what makes the forward classification relevant to the source-native grade observable.

## 3. Scalar and matrix-valued spectral repairs retain no more than Gram data

A scalar linear combination of the channels does not even use the full Gram matrix. For `c=(c_1,...,c_m)`,

\[
\sum_i c_iL_{g_i}
=L_{\sum_i c_i g_i},
\tag{31}
\]

and

\[
\left\|\sum_i c_i g_i\right\|^2
=c^*G(g)c.
\tag{32}
\]

Thus every scalar self-adjoint repair

\[
aN+\sum_i\left(c_iL_{g_i}+\overline{c_i}L_{g_i}^*\right)
\tag{33}
\]

collapses back to the single-channel theorem PC-366 with effective norm `(c^*Gc)^{1/2}`.

Keeping the channels separate inside a finite internal matrix space does not restore the lost tensor orientation. Let `E` be any finite-dimensional ancilla, let `B_i in B(E)` and let `A,C` be fixed source-independent operators on `E` with the symmetry assumptions required for the desired self-adjoint model. Any operator of the form

\[
H_g
=A\otimes N+C\otimes I
+\sum_i\left(B_i\otimes L_{g_i}+B_i^*\otimes L_{g_i}^*\right)
\tag{34}
\]

satisfies

\[
\boxed{
(I_E\otimes U)H_g(I_E\otimes U)^*=H_h
}
\tag{35}
\]

whenever `G(g)=G(h)`. The same statement holds for fixed `*`-polynomials, resolvents where defined, degree projections, the vacuum projection, singular-value constructions, and other unitary invariants built functorially from the tuple.

Therefore the hoped-for multichannel escape is only real to the extent that the **Gram matrix itself** carries useful source-specific information. The full-Fock representation creates no additional invariant from channel placement inside the tensor sector.

## 4. A strong matched control changes entanglement while preserving the entire operator type

The collapse is much larger than second-quantization symmetry. Take `K=C^2`, `q=2` and two orthonormal product channels

\[
g_1=e_0\otimes e_0,
\qquad
g_2=e_1\otimes e_1.
\tag{36}
\]

Compare them with

\[
h_1=\frac{e_0\otimes e_0+e_1\otimes e_1}{\sqrt2},
\qquad
h_2=\frac{e_0\otimes e_1+e_1\otimes e_0}{\sqrt2}.
\tag{37}
\]

Both labelled families have

\[
G=I_2.
\tag{38}
\]

But the `g_i` are product tensors while the `h_i` have Schmidt rank two. No one-particle basis change, nor any tensor product of local unitaries, can map the first labelled pair to the second because such maps preserve Schmidt rank. Nevertheless (5) supplies a unitary on the **full Fock space** that commutes with `N` and jointly conjugates both creators.

This shows exactly what the Wold gauge is erasing. It is not merely a phase, parity, or ordinary change of shell basis. It can identify homogeneous channel systems with radically different tensor-factor geometry while preserving every spectral observable constructed only from `(N,L_{g_1},...,L_{g_m})`.

As a numerical sanity check, truncating full Fock space at grade `5` for this example and coupling the two channels to two fixed noncommuting `2 x 2` ancilla matrices gives identical self-adjoint spectra to machine precision (`<7e-15` maximum eigenvalue discrepancy). This check is not evidence for (5); it only verifies a nontrivial finite-cutoff instance of the exact intertwining theorem.

## 5. Prior-art and novelty audit

The abstract operator theory is classical. Gelu Popescu, **Isometric dilations for infinite sequences of noncommuting operators**, *Transactions of the American Mathematical Society* 316:2 (1989), 523--536, DOI `10.1090/S0002-9947-1989-0972704-3`, proves the multivariable Wold decomposition for sequences of isometries with orthogonal ranges. A modern explicit statement is Theorem 2.2 of Adam H. Fuller, **Słociński--Wold decompositions for row isometries**, *Canadian Mathematical Bulletin* 66:3 (2023), 779--795, DOI `10.4153/S0008439522000686`: a row isometry decomposes into a row-unitary part and an `m`-shift, with the shift generated by the common wandering space. Muhly--Solel's tensor-algebra Wold framework already cited in PC-366 supplies a neighboring Fock-module formulation.

Equality of finite Gram matrices giving an isometry between the spans of the labelled vectors is elementary Hilbert-space linear algebra. Combining that fact with the pure row-isometry Wold theorem makes the ungraded unitary classification essentially immediate. The only line-local refinement used here is to carry the tensor number operator through the Wold decomposition: formula (11) resolves the wandering space grade by grade, and (22) then gives an intertwiner that **also commutes with `N`**.

A targeted prior-art search over row-isometry Wold decompositions, wandering subspaces, left creation operators and Gram-matrix classifications found the general ingredients but no reason to claim a new abstract operator theorem. The durable contribution is instead the Prime-Circle boundary: the precise multichannel representation architecture left open by PC-366 keeps no homogeneous source information beyond `G(g)`. This is an application/classification result, not a new Wold theorem and not an RH criterion.

The result also avoids a false positive common in spectral wrappers. If a future construction starts from the same finite homogeneous channel family and produces a striking spectrum, it has not yet used roots-of-unity geometry beyond the Gram matrix unless it introduces and justifies additional source-forced structure.

## 6. Consequence for the Prime-Circle RH frontier

PC-366's statement that multichannel constructions remain live must now be narrowed. **Finite same-degree channels are not a way to recover the full oriented tensor geometry merely by keeping the creators separate.** Their complete grade-preserving Fock type is already exhausted by the pairwise matrix `G(g)`.

This does not make Gram data irrelevant. A source-forced family could have a Gram matrix with genuine arithmetic structure, and a future argument might prove that those pairwise correlations themselves support a nonclassical zero-sensitive mechanism. Such a claim would have to be derived at the Gram level and survive matched non-arithmetic controls; the Fock lift would not supply the missing arithmetic by itself.

The branches not covered by this theorem are correspondingly sharper: mixed tensor degrees, where word lengths can meet the same total grade in nonuniform ways; source-dependent inner products or metrics rather than the standard Hilbert tensor norm; same-grade or backward couplings not generated by homogeneous left creation; source-forced domains/boundary conditions; and constructions whose extra operator datum is not functorial under the graded Wold equivalence. Those are genuinely different hypotheses rather than repetitions of the same homogeneous multichannel lift.

No spectral variable, Gamma factor, `s <-> 1-s` symmetry, critical-line selector, or zeta-zero equation appears in the Gram classification itself. Therefore the result is negative for the immediate RH objective but materially useful: it removes an entire finite multichannel representation family from the list of places where hidden tensor orientation could survive spectralization.

## Falsification / adversarial controls

- **Creator relation:** verify `L_u^*L_v=<u,v>I` in the full-Fock Hilbert tensor norm. Failure would invalidate both row orthogonality and the Gram converse.
- **Purity:** the length-`ell` row ranges begin at grade `q ell`; any nonzero row-unitary summand would contradict this exact grade escape.
- **Wandering multiplicity:** on grade `k>=q`, `R_g tensor K^{tensor(k-q)}` must have dimension `r d^{k-q}`. Any dependence on the orientation of `R_g` would refute (11).
- **Graded intertwiner:** (22) must preserve the grade `k+q|alpha|`, not merely the row shift. This is what proves `UN=NU`.
- **General-family reduction:** equal Gram matrices must make `g_i -> h_i` a well-defined span isometry, including when the labelled channels are linearly dependent.
- **Completeness:** joint unitary equivalence must force Gram equality through `L_{g_i}^*L_{g_j}`. This rules out a hidden invariant being omitted from (5).
- **Ancilla control:** any fixed matrix-valued coupling must be conjugated by `I tensor U`; if a proposed multichannel spectrum changes between equal-Gram controls, it has introduced extra source-dependent structure somewhere outside the tuple classified here.
- **Entanglement control:** the explicit product/Bell pair in (36)--(38) must remain jointly equivalent despite different Schmidt structure. This checks that the theorem is strictly stronger than one-particle or second-quantized basis covariance.
- **RH wrapper test:** a zero-sensitive claim based on this architecture must identify arithmetic already present in `G(g)` or an additional source-forced datum. A spectrum arising solely from the universal row-shift/Wold machinery is not Prime-Circle evidence.

## Boundary assessment

PC-367 closes the **finite, homogeneous, same-degree multichannel full-Fock** version of the escape explicitly left open by PC-366. Several channels do preserve their pairwise Gram geometry, but the row-isometry representation has enough graded Wold gauge freedom to erase everything else about their location inside the tensor sector. Scalar combinations reduce further to PC-366, while fixed matrix-valued channel couplings still see only the same Gram matrix.

The next meaningful question is therefore not whether adding more same-degree creators yields a richer universal Fock spectrum. It is whether Prime Circle forces useful arithmetic into a Gram family itself, or forces a structure outside this classification -- especially mixed-degree/nontriangular coupling, a source-dependent metric/domain, or another non-functorial operator datum. Repackaging the same homogeneous channels in a larger fixed matrix Hamiltonian is now classified and should not be treated as a new spectral mechanism.

## Formalization handoff

No automatic Lean handoff is warranted. The core finite-dimensional Gram lemma is easy, but the useful statement depends on full Fock space, pure row-isometry Wold decomposition, graded wandering subspaces, and an infinite direct-sum intertwiner. Formalizing that infrastructure would currently cost substantially more than the verification value of this negative boundary theorem.

## Artifact status

Single durable finding. No clue disposition is changed. The literature anchors are used to delimit the classical row-Wold mechanism; the Prime-Circle-specific graded Gram classification is derived explicitly above, so no separate `SOURCES.md` edit is required.