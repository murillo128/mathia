# WP-176 — Nevanlinna relation-valued passive limits Cayley back to Schur

**Status:** `LITERATURE+DERIVED + BOUNDARY-RELATION-NO-GO + NEVANLINNA-CAYLEY + MULTIVALUED-DECOMPOSITION + WEAK-BOUNDARY-GAMMA + DECISIVE-NARROWING + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION`.

`WP-173` leaves singular feedback and relation-valued closure open, while `WP-175` shows that weakening ordinary scalar passive convergence to weak or distributional boundary convergence still cannot produce the exact archimedean phase

\[
R_\infty(\tau)
=\pi^{i\tau}
\frac{\Gamma(\tfrac14-\tfrac{i\tau}{2})}
     {\Gamma(\tfrac14+\tfrac{i\tau}{2})},
\qquad |R_\infty(\tau)|=1.
\tag{1}
\]

A natural remaining escape is therefore to let the limiting passive boundary object cease to be an operator and become a **linear relation**, as happens canonically for singular boundary triples, generalized resolvents, and Weyl families. In the ordinary Hilbert-passive category this does not provide the needed new freedom.

If `M(z)` is a Nevanlinna family of linear relations on a Hilbert boundary space, then for every `z` in the upper half-plane `M(z)` is maximal dissipative. Its Cayley transform is consequently an everywhere-defined contraction, and the resolvent-holomorphy in the definition of a Nevanlinna family makes these contractions an ordinary operator-valued Schur function. Moreover, the multivalued part of a Nevanlinna family is independent of `z`; under the canonical orthogonal decomposition it contributes only a **constant identity channel** to the Cayley transform. The genuinely spectral part is just the operator-valued Nevanlinna part already controlled by Schur passivity.

Thus relation-valuedness by itself does not evade `WP-175`. Any normalized scalar matrix coefficient of the canonical Cayley response is a scalar Schur function, even if the boundary-space dimension and the chosen normalized vectors vary with the regularization. Any unrenormalized determinant of a finite-dimensional Cayley response is likewise scalar Schur, even when the dimension varies. Neither scalarization can converge to (1) in any of the positive-length weak boundary topologies closed by `WP-175`.

This is a prior-art classicalization, not a new theorem about Nevanlinna families. The Mathia-specific content is that the explicit **relation-valued passive escape** left after `WP-173`--`WP-175` collapses back to the already-forbidden Schur class unless an additional singular or unbounded scalarization is introduced. Such an additional operation must then carry its own source-forced coercivity theorem; it cannot inherit the desired Weil sign merely from ordinary boundary-relation passivity.

## 1. Maximal dissipative relations have ordinary contractive Cayley transforms

Let `H` be a Hilbert space and let

\[
M(z),\qquad z\in\mathbb C_+,
\tag{2}
\]

be a Nevanlinna family of linear relations in `H`, in the convention in which `M(z)` is maximal dissipative in `C_+`. One equivalent holomorphy condition is that

\[
(M(z)+iI)^{-1}\in\mathcal B(H)
\tag{3}
\]

exists and is holomorphic in `z`. Define the Cayley response

\[
\boxed{
S_M(z)
:=I-2i(M(z)+iI)^{-1}.
}
\tag{4}
\]

For an operator value this is the familiar formula

\[
S_M(z)=(M(z)-iI)(M(z)+iI)^{-1}.
\tag{5}
\]

Formula (4) remains meaningful when `M(z)` is multivalued because the inverse in (3) is an everywhere-defined bounded operator. The classical Cayley theorem for linear relations says precisely that the Cayley transform of a maximal dissipative relation is an everywhere-defined contraction. Hence

\[
\boxed{
\|S_M(z)\|\le1,
\qquad z\in\mathbb C_+.
}
\tag{6}
\]

Since (3) is holomorphic, so is (4). Therefore

\[
\boxed{
M(\cdot)\text{ Nevanlinna relation family}
\Longrightarrow
S_M(\cdot)\text{ operator-valued Schur family}.
}
\tag{7}
\]

No finite-dimensionality, boundedness of the relation values, or single-valuedness is used in (7). The relation formalism enlarges the Weyl object on the dissipative side, but its canonical passive Cayley transfer still lands in the ordinary unit ball of analytic operator functions.

## 2. The multivalued sector is spectrally constant

The apparent extra freedom from a multivalued Weyl family is even more restricted. A classical structural theorem for Nevanlinna families gives a `z`-independent multivalued subspace

\[
H_\infty:=\operatorname{mul}M(z),
\tag{8}
\]

and an orthogonal decomposition

\[
H=H_s\oplus H_\infty,
\qquad
M(z)=\operatorname{gr}M_s(z)\oplus M_\infty,
\qquad
M_\infty=\{0\}\times H_\infty,
\tag{9}
\]

where `M_s(z)` is a densely defined operator-valued Nevanlinna family on `H_s`. For the purely vertical relation `M_infty`,

\[
(M_\infty+iI)^{-1}=0,
\tag{10}
\]

so (4) yields

\[
\boxed{
S_M(z)=S_{M_s}(z)\oplus I_{H_\infty}.
}
\tag{11}
\]

The multivalued sector is therefore not a hidden frequency-dependent channel. It becomes a constant unitary `1` block in the passive transfer representation. All nonconstant analytic behavior is carried by the single-valued operator part.

In boundary dimension one this leaves only two cases. Either `mul M(z)=0`, so `M` is an ordinary scalar Nevanlinna function and (4) is an ordinary scalar Schur function, or `mul M(z)=C`, in which case the family is purely vertical and its Cayley response is identically `1`. There is no third scalar relation-valued passive class capable of carrying a nonconstant phase such as (1).

This fixed-multivalued decomposition is important for the singular-feedback interpretation. A pole or verticalization at an isolated real boundary point can occur as a boundary phenomenon, but an ordinary Nevanlinna family cannot use a spectral-parameter-dependent multivalued subspace as a moving carrier of the Gamma phase. A proposal with such a moving singular subspace has already left the classical Nevanlinna-family hypothesis whose passivity theorem is being invoked.

## 3. Weak boundary limits remain Schur after normalized scalarization

The collapse (7) combines directly with `WP-175`, and it sharpens one of that finding's deliberately conservative caveats.

Let `M_m(z)` be Nevanlinna families on arbitrary Hilbert spaces `H_m`; the spaces may change with `m`. Let `u_m,v_m in H_m` be unit vectors and define

\[
s_m(z)
:=\langle u_m,S_{M_m}(z)v_m\rangle.
\tag{12}
\]

By (6), every `s_m` is analytic and

\[
|s_m(z)|\le1.
\tag{13}
\]

Thus the whole sequence lies in the same scalar Schur unit ball regardless of the dimensions of `H_m` or of the variation of the normalized readout vectors. `WP-175` then applies verbatim: on any nonempty open real interval `I`, the boundary traces of (12) cannot converge to `R_infty` in distributions. Consequently they also cannot converge to it in weak-* `L^infty(I)`, weak `L^p`, local `L^1`, in measure, or almost everywhere under the hypotheses used there.

Hence

\[
\boxed{
\text{Nevanlinna relation families}
+\text{ normalized Cayley coefficients}
\not\Longrightarrow
R_\infty
\text{ even by weak boundary limits}.
}
\tag{14}
\]

The same observation closes plain finite-dimensional determinants even when the dimension varies. If `dim H_m=d_m<infinity`, then all singular values of `S_{M_m}(z)` are at most one, so

\[
d_m(z):=\det S_{M_m}(z)
\tag{15}
\]

is analytic and satisfies

\[
|d_m(z)|\le1.
\tag{16}
\]

Thus `d_m` is again a scalar Schur function for every `m`, with no fixed-dimension hypothesis needed after scalarization. The identity block in (11) contributes determinant one and cannot hide the Gamma phase. Therefore changing finite boundary dimension alone does not evade `WP-175` through an **unrenormalized determinant**.

This does not justify a claim about Fredholm determinants, regularized determinants, dimension-dependent multiplicative counterterms, or scalarizations whose operator norm is allowed to diverge. Those operations need not remain in the scalar Schur unit ball and are genuinely outside (14)--(16). Precisely for that reason, however, their positivity cannot be inherited for free from the Nevanlinna relation: the renormalization itself becomes part of the proposed geometric mechanism.

## 4. Direct Weyl readouts have the same sign rigidity on regular real intervals

One might avoid the Cayley phase and try to identify the Gamma logarithmic derivative directly with a Weyl derivative. Relation-valuedness does not rescue that regular route either.

For the active operator part `M_s`, the Nevanlinna kernel

\[
K_M(z,w)
:=
\frac{M_s(z)-M_s(w)^*}{z-\overline w}
\tag{17}
\]

is positive in the usual operator-kernel sense. Suppose `M_s` extends holomorphically through a real interval `J` with self-adjoint values there. Taking the diagonal boundary limit in (17) gives

\[
\boxed{
M_s'(t)\succeq0,
\qquad t\in J.
}
\tag{18}
\]

The opposite Nevanlinna orientation reverses this fixed semidefinite sign. The exact Gamma phase velocity retained by `WP-169` is

\[
A_\infty(t)
=
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)-\log\pi,
\tag{19}
\]

which is negative near the origin and positive after its unique positive zero. Therefore no positive scalar readout of (18), in either fixed orientation, can equal `A_infty(t)` on a real interval spanning both sign regions. The vertical block (9) has no varying operator derivative to contribute.

So the two most canonical ways to extract a visible passive response from a Nevanlinna boundary relation fail for complementary but equivalent reasons: its Cayley response remains Schur, while its regular self-adjoint Weyl derivative has one semidefinite orientation. The sign-changing archimedean term cannot be hidden in ordinary multivaluedness.

## 5. Aggressive falsification and matched controls

**The theorem does not exclude singular scalarizations.** If the visible observable is obtained only after multiplying by an unbounded factor, subtracting a divergent counterterm, taking a regularized Fredholm determinant, or differentiating a singular graph limit outside the bounded Cayley topology, the scalar result need not be Schur. Such a proposal remains logically open, but its new operation must be source-forced and must come with a closed/coercive positive form. Ordinary Nevanlinna passivity no longer proves the desired sign after that operation.

**A genuinely changing domain can leave the audited category.** Equations (7)--(11) concern an ordinary Nevanlinna family on each boundary Hilbert space. If a proposed scaling limit changes the underlying graph topology so severely that no maximal-dissipative Nevanlinna family survives, this finding does not classify the limit. That is exactly the stronger sort of domain degeneration left open by `WP-175`; calling the limit a `relation` is not enough. The construction must specify which relation class survives and where positivity is proved.

**Moving multivalued parts are not an ordinary Nevanlinna-family effect.** The constancy in (8) is structural. A frequency-dependent vertical subspace can only enter by changing the family/category, by a parameter-dependent identification of boundary spaces, or by an additional singular reduction. Each option becomes extra mechanism rather than inherited boundary-relation passivity.

**Generalized Nevanlinna/Pontryagin families are different.** Finite negative index is the route audited in `WP-172`; infinite negative index remains outside both that result and the present Hilbert-Nevanlinna argument. Relation-valuedness does not convert negative-square geometry into Hilbert positivity.

**Nonseparable finite--archimedean assembly remains open.** The result assumes that the exact real-place Gamma data is extracted as a standalone Weyl/Cayley observable before the final global Weil form is established. It does not apply if finite-prime incidence and the archimedean sector are coupled first and `R_infty` appears only as a derived signed observable after a genuinely global positive theorem. That remains the branch's preferred structural escape.

A matched positive control shows that the obstruction is not an artefact of relations. Let `H=H_0 direct_sum H_infty` and

\[
M(z)=\operatorname{gr}(zI_{H_0})
\oplus(\{0\}\times H_\infty).
\tag{20}
\]

This is a perfectly valid Nevanlinna relation family. Its Cayley transform is

\[
S_M(z)
=
\frac{z-i}{z+i}I_{H_0}\oplus I_{H_\infty},
\tag{21}
\]

an ordinary passive Schur response with a nontrivial vertical sector. The relation formalism works exactly as intended; what it does **not** do is create a new sign-changing passive transfer class.

## 6. Prior-art and novelty audit

The relation-valued machinery is classical. Vladimir Derkach, Seppo Hassi, Mark Malamud, and Henk de Snoo, *Boundary relations and their Weyl families*, Transactions of the American Mathematical Society 358 (2006), 5351--5400, DOI `10.1090/S0002-9947-06-04033-5`, introduced boundary relations and Weyl families and proved realization results for maximal-dissipative holomorphic families of linear relations. Their later *Boundary relations and generalized resolvents of symmetric operators*, Russian Journal of Mathematical Physics 16 (2009), 17--60, DOI `10.1134/S1061920809010026`, develops the same Nevanlinna-family framework in the Krein--Naimark generalized-resolvent setting.

Jussi Behrndt, Seppo Hassi, and Henk de Snoo, *Boundary Relations, Unitary Colligations, and Functional Models*, Complex Analysis and Operator Theory 3 (2009), 57--98, DOI `10.1007/s11785-008-0064-z`, explicitly connects Nevanlinna/Weyl families with operator-valued Schur transfer functions and unitary colligations. Volodymyr Derkach, Seppo Hassi, and Mark Malamud, *Generalized boundary triples, I. Some classes of isometric and unitary boundary pairs and realization problems for subclasses of Nevanlinna functions*, Mathematische Nachrichten 293 (2020), no. 7, 1278--1327, records the generalized boundary-pair setting in which the Weyl objects are Nevanlinna functions or families. The standard decomposition of a Nevanlinna family into a `z`-independent multivalued part and an operator part is part of this literature.

Yury Arlinskiĭ and Seppo Hassi, *Stieltjes and inverse Stieltjes holomorphic families of linear relations and their representations*, Studia Mathematica (2019/2020), DOI `10.4064/sm180714-12-3`, gives explicit Cayley-transform connections from Nevanlinna families to operator-valued Schur functions in its representation theory. The maximal-dissipative-relation Cayley correspondence itself is standard linear-relation theory.

No novelty is claimed for maximal dissipativity, Cayley transforms, the fixed multivalued decomposition, Nevanlinna kernels, boundary monotonicity, or Schur functional models. The substantive branch-specific statement is the combination of those classical facts with the exact Gamma obstruction of `WP-169`--`WP-175`:

\[
\boxed{
\text{ordinary Hilbert Nevanlinna/Weyl relation-valued closure}
+\text{ bounded passive scalarization}
\Longrightarrow
\text{Schur/one-sign rigidity, not the Gamma channel}.
}
\tag{22}
\]

## 7. Research consequence

The word **relation-valued** no longer constitutes a live escape from the recent passive no-go chain by itself. Within the ordinary Hilbert Nevanlinna/Weyl category, singular boundary geometry is Cayley-equivalent to an operator Schur family; the genuinely multivalued component is spectrally constant, and both normalized matrix coefficients and plain finite-dimensional determinants remain in the scalar Schur ball even under changing channel dimension.

A viable continuation therefore has to introduce something mathematically stronger before identifying the Gamma channel: a genuinely domain-degenerate limit not represented by an ordinary Nevanlinna family, an unbounded/source-forced renormalized scalarization with its own coercivity theorem, an infinite-index indefinite structure with a separately proved positive termination, or a nonseparable finite-prime/archimedean geometry in which the Gamma phase never appears as a standalone passive transfer response.

The last option remains the one most aligned with the research mandate. `WP-176` removes another way of changing functional-analytic vocabulary without changing the underlying positivity mechanism; it does not remove the need for a genuinely global Mathia-native sign theorem.