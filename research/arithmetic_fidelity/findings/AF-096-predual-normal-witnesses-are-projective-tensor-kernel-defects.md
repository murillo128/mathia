# AF-096 — Predual-normal fidelity witnesses are projective-tensor kernel defects

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `ADMISSIBLE-WITNESS-REFINEMENT`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
0\longrightarrow Z_F\xrightarrow{j}\mathcal F(F)\xrightarrow{\beta_F}F\longrightarrow0,
\qquad Z_F=\ker\beta_F,
\tag{1}
\]

be the canonical Lipschitz-free exact sequence of a real Banach space `F`. Fix a real Banach space `Y`, take the coefficient space in the explicitly dual form `K=Y^*`, and set

\[
P:=Z_F\widehat\otimes_\pi Y,
\qquad
Q:=\mathcal F(F)\widehat\otimes_\pi Y,
\qquad
A:=j\widehat\otimes_\pi I_Y:P\to Q.
\tag{2}
\]

Projective-tensor duality gives canonical isometric identifications

\[
P^*\cong\mathcal L(Z_F,Y^*),
\qquad
Q^*\cong\mathcal L(\mathcal F(F),Y^*),
\tag{3}
\]

where

\[
\left\langle T,\sum_i z_i\otimes y_i\right\rangle
=
\sum_i\langle Tz_i,y_i\rangle.
\tag{4}
\]

Under (3), the restriction map from AF-093--AF-095,

\[
R_{F,Y^*}(S)=S|_{Z_F},
\tag{5}
\]

is exactly

\[
\boxed{R_{F,Y^*}=A^*.}
\tag{6}
\]

Regard `P^*=\mathcal L(Z_F,Y^*)` with the weak-star topology `\sigma(P^*,P)` supplied by this declared predual. Every weak-star continuous linear witness is evaluation by some `u\in P`,

\[
\Phi_u(T)=\langle T,u\rangle.
\tag{7}
\]

Such a witness annihilates every linearly extendable fiber operator exactly when

\[
\boxed{
\Phi_u|_{\operatorname{ran}R_{F,Y^*}}=0
\iff
u\in\ker A
}
\tag{8}
\]

with the symbol on the right understood as the same representing tensor `u`; equivalently, without introducing a separate symbol,

\[
\boxed{
W^{w^*}_{F,Y}
\cong
\ker(j\widehat\otimes_\pi I_Y).
}
\tag{9}
\]

For `T\in\mathcal L(Z_F,Y^*)`, define the predual-normal witness margin

\[
\rho^{w^*}_{F,Y}(T)
:=
\sup_{\substack{u\in\ker A\\ \|u\|_\pi\le1}}
|\langle T,u\rangle|.
\tag{10}
\]

Then

\[
\boxed{
\rho^{w^*}_{F,Y}(T)
=
\|T|_{\ker A}\|
=
\operatorname{dist}\!\left(T,(\ker A)^\perp\right)
=
\operatorname{dist}\!\left(
T,
\overline{\operatorname{ran}R_{F,Y^*}}^{\,w^*}
\right).
}
\tag{11}
\]

The final distance is operator-norm distance to a weak-star closed comparison set. Since norm closure is contained in weak-star closure,

\[
\boxed{
0\le \rho^{w^*}_{F,Y}(T)
\le
\rho_{F,Y^*}([T]),
}
\tag{12}
\]

where the right-hand side is AF-094/AF-095's unrestricted robust margin. Thus an AF-095 Hahn--Banach witness need not belong to the declared predual. In particular,

\[
\boxed{
\ker(j\widehat\otimes_\pi I_Y)=\{0\}
\Longrightarrow
\text{every nonzero AF-095 witness is weak-star discontinuous relative to }P.
}
\tag{13}
\]

Conversely,

\[
\boxed{
\text{a nonzero predual-normal witness exists}
\iff
j\widehat\otimes_\pi I_Y\text{ is not injective}.
}
\tag{14}
\]

There is also an exact finite-complexity obstruction. The algebraic map

\[
j\otimes I_Y:Z_F\otimes Y\to\mathcal F(F)\otimes Y
\tag{15}
\]

is injective because tensoring vector spaces over `\mathbb R` preserves injections. Hence

\[
\boxed{
\ker(j\widehat\otimes_\pi I_Y)\cap(Z_F\otimes Y)=\{0\}.
}
\tag{16}
\]

Every nonzero predual-normal witness is therefore a genuinely completed projective-tensor phenomenon and cannot be a finite sum of elementary evaluations

\[
T\longmapsto\sum_{i=1}^m\langle Tz_i,y_i\rangle.
\tag{17}
\]

In particular, if `Y` is finite-dimensional then `Z_F\otimes Y` is already complete up to its canonical finite-coordinate Banach-space identification, so

\[
\boxed{
\dim Y<\infty
\Longrightarrow
\ker(j\widehat\otimes_\pi I_Y)=\{0\}
\Longrightarrow
W^{w^*}_{F,Y}=\{0\}.
}
\tag{18}
\]

The resulting Arithmetic Fidelity boundary is sharp: **robust nonrecoverability can be visible to an unrestricted bounded functional while remaining invisible to every witness normal for a mathematically declared predual.**

## Derivation

### Restriction is the adjoint tensor map

For Banach spaces `X,Y`, the universal property of the completed projective tensor product gives

\[
(X\widehat\otimes_\pi Y)^*
\cong
\mathcal B(X\times Y)
\cong
\mathcal L(X,Y^*).
\tag{19}
\]

For `S\in\mathcal L(\mathcal F(F),Y^*)` and algebraic `u=\sum_i z_i\otimes y_i`,

\[
\langle A^*S,u\rangle
=
\langle S,Au\rangle
=
\sum_i\langle S(jz_i),y_i\rangle
=
\langle S|_{Z_F},u\rangle.
\tag{20}
\]

Density proves (6) on all of `P`.

### Normal annihilators are tensor-kernel vectors

A `\sigma(P^*,P)`-continuous linear functional is evaluation at an element `u\in P`. Using (6), for every `S\in Q^*`,

\[
\Phi_u(R_{F,Y^*}S)
=
\langle A^*S,u\rangle
=
\langle S,Au\rangle.
\tag{21}
\]

Since `Q^*` separates points of `Q`, this vanishes for all `S` iff `Au=0`, proving (9) and (14). AF-095 permits the whole bidual `P^{**}` as a witness space; AF-096 identifies exactly the part lying in the canonical copy of `P` selected by the chosen predual.

### The normal margin is distance to weak-star recoverability

Restriction of `T\in P^*` to `\ker A` gives

\[
\rho^{w^*}_{F,Y}(T)=\|T|_{\ker A}\|.
\tag{22}
\]

Hahn--Banach extension gives

\[
\|T|_{\ker A}\|
=
\operatorname{dist}(T,(\ker A)^\perp).
\tag{23}
\]

For every bounded `A:P\to Q`, annihilator duality gives

\[
\overline{\operatorname{ran}A^*}^{\,\sigma(P^*,P)}
=(\ker A)^\perp.
\tag{24}
\]

Together with `R=A^*`, this proves (11)--(12). The distinction from AF-095 is therefore exact: norm closure tests arbitrary bounded separation, while weak-star closure tests separation by the declared predual.

### Completion is essential

Before completion, `j\otimes I_Y` is injective algebraically. The canonical maps from algebraic projective tensor products into their completions are injective because the projective crossnorm is a norm. Therefore an algebraic tensor killed by `A` must already be zero, proving (16).

If `Y` is finite-dimensional, every element of `Z_F\widehat\otimes_\pi Y` has a finite-coordinate representation `\sum_{i=1}^n z_i\otimes y_i`; coordinate functionals on `Y` identify the tensor product with a finite Banach direct sum of copies of `Z_F`. The induced map is coordinatewise `j` and hence injective, proving (18).

## Exact controls

### Complemented barycentric kernel

If `Z_F` is complemented in `\mathcal F(F)` by a bounded projection `P_F`, then `P_F\widehat\otimes_\pi I_Y` is a bounded left inverse of `j\widehat\otimes_\pi I_Y`. Thus `A` is injective for every `Y`. By AF-093 this includes targets with the Lipschitz lifting property, including the separable-target regime used there.

### Finite-dimensional predual

Equation (18) shows that finite-dimensional `Y` cannot realize a nonzero normal witness kernel even when `Z_F` itself is not complemented. Noncomplementability is therefore not sufficient for this admissible witness class.

### Algebraic finite-sum control

If a witness of the finite form (17) vanishes on every extendable operator, its representing algebraic tensor lies in `\ker A`; (16) forces that tensor to be zero. Thus no nonzero finite predual tensor can certify the complete extension defect.

### Robust-but-not-normal regime

It is logically possible that

\[
\overline{\operatorname{ran}R}^{\,\|\cdot\|}
\subsetneq
\overline{\operatorname{ran}R}^{\,w^*}
=P^*.
\tag{25}
\]

Then AF-095 has nonzero bounded witnesses while AF-096 has no weak-star continuous witness because `A` is injective. This is an exact conditional regime classification, not a claim that a particular barycentric pair `(F,Y)` realizing it is presently known.

### Chosen-predual control

If the same coefficient Banach space `K` admits inequivalent preduals, the topology `\sigma(\mathcal L(Z_F,K),Z_F\widehat\otimes_\pi Y)` can depend on the declared representation `K=Y^*`. AF-096 therefore does not call predual-normality intrinsic to bare `K`. An application must justify the predual independently rather than select it after observing which witnesses it allows.

## Prior art and novelty assessment

The tensor and duality ingredients are classical, and **no novelty is claimed** for projective tensor products, operator duality, failure of completed projective tensoring to be left exact in general, annihilator identities, or weak-star closure of adjoint ranges.

- Raymond A. Ryan, ***Introduction to Tensor Products of Banach Spaces***, Springer Monographs in Mathematics, Springer London (2002), DOI `10.1007/978-1-4471-3903-4`, especially Chapter 2. Role: the projective norm, `(X\widehat\otimes_\pi Y)^*\cong\mathcal B(X\times Y)\cong\mathcal L(X,Y^*)`, functoriality, and the classical warning that the projective tensor product does not in general respect subspaces. Ryan's Corollary 2.12 relates the stronger isometric-subspace property to operator extension into `Y^*`.
- Joe Diestel, Jan Fourie, and Johan Swart, **“The Metric Theory of Tensor Products (Grothendieck's Résumé Revisited) Part 5: Injective and Projective Tensor Norms,”** *Quaestiones Mathematicae* 26(4) (2003), 477--497, DOI `10.2989/16073600309486077`. Role: standard metric tensor-norm framework, including left/right injectivity and projectivity.
- Walter Rudin, ***Functional Analysis***, 2nd ed., McGraw--Hill (1991), Chapters 3--4. Role: standard Hahn--Banach, annihilator, and dual-pair background for (23)--(24).

The literature therefore blocks any claim that the underlying tensor theorem is new. The durable Arithmetic Fidelity result is the specialization and admissibility boundary: AF-095's unrestricted separators divide into witnesses represented by a declared predual and witnesses necessarily outside it, and the first class is measured exactly by the completed tensor kernel (9). Equation (16) adds a sharp finite-complexity no-go inside that class.

## Boundaries and failure modes

- The coefficient must be presented as a specific dual `K=Y^*`; the theorem does not manufacture a preferred predual.
- `W^{w^*}_{F,Y}` is only the weak-star continuous sector relative to `P`, not the full AF-095 witness space `P^{**}`.
- `\ker A=0` does not imply absence of robust defect; it implies only that any separator must be weak-star discontinuous for this predual.
- `\ker A\ne0` supplies a normal separator but no arithmetic provenance, positivity, locality, equivariance, computability, or prime specificity.
- Equation (16) rules out finite **predual tensors**, not every finitely described functional in every possible representation.
- Failure to preserve a subspace projectively is more nuanced than kernel noninjectivity: the induced tensor norm may change even when the completed canonical map remains injective. AF-096 uses only the kernel condition required by its witness classification.
- No RH conclusion follows.

## Consequences for Arithmetic Fidelity

AF-093 identifies exact nonlinear recovery defects as fiber operators modulo extension; AF-094 separates algebraic from robust defects by norm closure; AF-095 converts robust defect into arbitrary bounded separation. AF-096 adds a source-sensitive admissibility layer:

\[
\text{arbitrary bounded witness}
\supseteq
\text{declared-predual normal witness}
\cong
\ker(j\widehat\otimes_\pi I_Y).
\tag{26}
\]

A positive Hahn--Banach margin is therefore not sufficient when the application supplies a distinguished predual, topology, locality class, symmetry class, or other observable category. In the present Banach/Lipschitz model, predual-normal witnessability is exact and no finite algebraic tensor can realize it. Future arithmetic applications should ask whether the **source-justified observable class** contains a separator, rather than relying on a singular functional manufactured after the compression is already known.