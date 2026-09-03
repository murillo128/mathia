# AF-097 — Finite pointwise observations cannot detect linear extension defects

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `ADMISSIBLE-WITNESS-REFINEMENT`, `DECISIVE-NEGATIVE`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let `Z` be a closed linear subspace of a Banach space `X`, let `K` be a Banach space, and consider the restriction operator

\[
R:\mathcal L(X,K)\longrightarrow \mathcal L(Z,K),
\qquad R(S)=S|_Z.
\tag{1}
\]

Then every bounded operator on `Z` is **exactly indistinguishable from an extendable operator on every finite pointwise observation**.

More precisely, for every `T\in\mathcal L(Z,K)` and every finite-dimensional subspace `E\subset Z`, there is `S_E\in\mathcal L(X,K)` such that

\[
\boxed{S_E|_E=T|_E.}
\tag{2}
\]

If `n=\dim E`, one may choose

\[
\boxed{\|S_E\|\le n\,\|T\|.}
\tag{3}
\]

Consequently, for every finite family `z_1,\ldots,z_m\in Z`, the evaluation map

\[
\operatorname{ev}_{\mathbf z}:\mathcal L(Z,K)\to K^m,
\qquad
\operatorname{ev}_{\mathbf z}(T)=(Tz_1,\ldots,Tz_m)
\tag{4}
\]

has exactly the same image on all operators as on extendable operators:

\[
\boxed{
\operatorname{ev}_{\mathbf z}(\operatorname{ran}R)
=
\operatorname{ev}_{\mathbf z}(\mathcal L(Z,K)).
}
\tag{5}
\]

Thus even an arbitrary nonlinear decision rule applied after finitely many exact vector-valued samples cannot determine whether `T` extends to `X`.

Equivalently, if `\mathrm{SOT}` denotes the strong operator topology of pointwise norm convergence and `\mathrm{WOT}` the weak operator topology, then

\[
\boxed{
\overline{\operatorname{ran}R}^{\,\mathrm{SOT}}
=
\overline{\operatorname{ran}R}^{\,\mathrm{WOT}}
=
\mathcal L(Z,K).
}
\tag{6}
\]

This remains true when `\operatorname{ran}R` is a proper subspace and even when AF-095's norm-stability defect is positive:

\[
\operatorname{dist}(T,\operatorname{ran}R)>0.
\tag{7}
\]

Hence any nonzero norm-continuous AF-095 witness

\[
\Phi\in (\operatorname{ran}R)^\perp
\subset \mathcal L(Z,K)^*
\tag{8}
\]

is necessarily discontinuous for both `\mathrm{SOT}` and `\mathrm{WOT}`. In fact, no scalar-valued `\mathrm{SOT}`-continuous function that vanishes on all extendable operators can be nonzero anywhere, because the extendable range is already `\mathrm{SOT}` dense.

For the barycentric-kernel model of AF-093--AF-096,

\[
Z=Z_F\subset \mathcal F(F),
\tag{9}
\]

this conclusion holds for **every** coefficient Banach space `K`, including non-ultrasummand coefficients for which the exact extension quotient may remain nonzero. AF-096 showed that declaring `K=Y^*` to obtain a predual-normal witness collapses the defect by ultrasummand linearization. The present result closes a different escape: retaining an arbitrary non-ultrasummand `K` but restricting admissible observations to finitely many point evaluations also makes every global extension defect invisible.

The resulting Arithmetic Fidelity boundary is

\[
\boxed{
\text{global operator nonextension can be norm-robust while being exactly invisible at every finite pointwise scale.}
}
\tag{10}
\]

Any source-natural witness for such a defect must therefore encode genuinely global coherence, uniform conditioning, or another infinite-data feature not reducible to finitely many values `Tz`.

## Derivation

### 1. Every finite-dimensional restriction extends exactly

Fix a finite-dimensional subspace `E\subset Z` of dimension `n`. Choose an Auerbach basis

\[
e_1,\ldots,e_n\in E,
\qquad
e_1^*,\ldots,e_n^*\in E^*,
\tag{11}
\]

so that

\[
e_i^*(e_j)=\delta_{ij},
\qquad
\|e_i\|=\|e_i^*\|=1.
\tag{12}
\]

By Hahn--Banach, each `e_i^*` extends to some `\widetilde e_i^*\in X^*` with

\[
\|\widetilde e_i^*\|=1.
\tag{13}
\]

For `T\in\mathcal L(Z,K)`, define the finite-rank operator

\[
S_E(x)
:=
\sum_{i=1}^n
\widetilde e_i^*(x)\,T e_i.
\tag{14}
\]

If `e\in E`, then

\[
S_E(e)
=
\sum_i e_i^*(e)Te_i
=T\!\left(\sum_i e_i^*(e)e_i\right)
=T(e),
\tag{15}
\]

so (2) holds. Moreover,

\[
\begin{aligned}
\|S_E x\|
&\le
\sum_{i=1}^n
|\widetilde e_i^*(x)|\,\|Te_i\|\\
&\le
n\,\|x\|\,\|T\|,
\end{aligned}
\tag{16}
\]

which proves (3).

This is only finite-dimensional solvability. The operators `S_E` need not be compatible as `E` grows, and the bound in (3) deteriorates with dimension. Neither a global extension nor a uniform extension constant follows.

### 2. Finite evaluation images coincide exactly

Given `z_1,\ldots,z_m\in Z`, set

\[
E=\operatorname{span}\{z_1,\ldots,z_m\}.
\tag{17}
\]

For arbitrary `T\in\mathcal L(Z,K)`, the operator `S_E` from (2) satisfies

\[
R(S_E)z_j=Tz_j
\qquad(1\le j\le m).
\tag{18}
\]

Therefore every finite evaluation vector achieved by an arbitrary operator is achieved by an extendable operator, proving (5). The reverse inclusion is automatic.

This is stronger than merely saying that no chosen finite list of samples is known to distinguish extension. The complete finite observation spaces are identical. Any function

\[
G:K^m\to V
\tag{19}
\]

applied after the samples receives exactly the same possible inputs from `\operatorname{ran}R` as from the full operator space, regardless of whether `G` is linear, continuous, measurable, or arbitrary.

### 3. Exact finite matching is strong-operator density

A basic `\mathrm{SOT}` neighborhood of `T` is specified by finitely many source vectors and positive tolerances. Equation (18) supplies an element of `\operatorname{ran}R` that agrees with `T` exactly on those vectors, hence belongs to every such neighborhood. Thus

\[
\overline{\operatorname{ran}R}^{\,\mathrm{SOT}}
=
\mathcal L(Z,K).
\tag{20}
\]

Because `\mathrm{WOT}` is weaker than `\mathrm{SOT}`, its closure can only be larger, proving the second equality in (6).

The topology distinction is therefore sharp. Norm topology asks for one extension operator to approximate `T` uniformly on the whole unit ball of `Z`. Strong operator topology asks only for approximation on each finite set of source vectors at a time. The latter is always solvable exactly even when the former has a positive gap.

### 4. Finite matrix-coefficient witnesses vanish identically

The classical continuous duals of `\mathcal L(Z,K)` for `\mathrm{SOT}` and `\mathrm{WOT}` coincide. Every continuous linear functional has the finite matrix-coefficient form

\[
\Phi(T)
=
\sum_{i=1}^m
k_i^*(Tz_i),
\qquad
z_i\in Z,
\quad k_i^*\in K^*.
\tag{21}
\]

This also follows directly for `\mathrm{SOT}`: continuity bounds `\Phi` by finitely many seminorms `T\mapsto\|Tz_i\|`, so `\Phi` factors through a finite evaluation map and Hahn--Banach on its image yields (21).

If `\Phi` vanishes on `\operatorname{ran}R`, choose `S_E` matching arbitrary `T` on the span of the finitely many `z_i`. Then

\[
\Phi(T)=\Phi(RS_E)=0.
\tag{22}
\]

Hence the `\mathrm{SOT}`/`\mathrm{WOT}` annihilator of the extendable range is zero. This recovers the linear-witness consequence of density without invoking norm closure.

## Exact controls

### Complemented subspace

If `Z` is complemented in `X`, `R` is already surjective: for a bounded projection `P:X\to Z`, every `T` extends as `TP`. Then there is no extension defect in any topology. The result is interesting only when `Z` is not complemented or when the chosen coefficient `K` otherwise permits nonextension.

### Proper but norm-dense range

If `\operatorname{ran}R` is proper but norm dense, AF-095 already says all algebraic defects are invisible to bounded norm-continuous linear witnesses. Equation (6) adds no new separation failure in that regime; it identifies the stronger finite-local reason that pointwise topologies cannot see the defect at all.

### Positive norm-stability defect

If

\[
\operatorname{dist}(T,\operatorname{ran}R)>0,
\tag{23}
\]

AF-095 provides a norm-one bounded linear separator. Nevertheless every finite-dimensional restriction of `T` is exactly extendable by (2). Thus robust norm separation does **not** imply finite-local observability. The separating functional must depend on the global Banach geometry of the operator space rather than finitely many matrix coefficients.

### Uniform local extension is a different gate

Equation (3) provides a dimension-dependent bound only. Classical local complementation asks for a dimension-independent constant controlling finite-dimensional local retractions/extensions. Such a uniform local property is substantially stronger than the automatic finite matching proved here and has genuine global consequences.

Therefore one must not infer from (2) that `Z` is locally complemented, that the exact sequence locally splits with a uniform constant, or that `T` extends globally. The obstruction can survive precisely in the failure to choose finite repairs coherently and with uniform control.

### Arbitrary coefficient category

No duality, reflexivity, separability, approximation property, or ultrasummand assumption on `K` is used. This is why the result is complementary to AF-096 rather than a special case of it.

## Prior art and novelty assessment

The mechanism is classical and **no novelty is claimed** for finite-dimensional complementation, Hahn--Banach extension of coordinate functionals, strong/weak operator topologies, or their continuous duals.

- Nelson Dunford and Jacob T. Schwartz, ***Linear Operators. Part I: General Theory***, Interscience Publishers, New York (1958), Theorem VI.1.4. Role: classical operator-topology source for the fact that the continuous linear functionals for the strong and weak operator topologies on `\mathcal L(Z,K)` coincide and are finite sums of matrix coefficients.
- Antonio Avilés, Gonzalo Martínez-Cervantes, and Abraham Rueda Zoca, **“Local complementation in Banach spaces and its preservation under free constructions,”** *Quaestiones Mathematicae* 48(2) (2025), 287--298, DOI `10.2989/16073606.2024.2393682`. Role: modern source for classical local complementation and its equivalent Lipschitz-local forms, including preservation under Lipschitz-free constructions; it marks the stronger uniform-local boundary that must not be confused with the automatic unbounded finite interpolation above.
- Jesús M. F. Castillo, Ricardo García, Andreas Defant, David Pérez-García, and Jesús Suárez, **“Local complementation and the extension of bilinear mappings,”** *Mathematical Proceedings of the Cambridge Philosophical Society* 152(1) (2012), 153--175, DOI `10.1017/S0305004111000533`. Role: established Banach-space local-complementation and extension framework, reinforcing that dimension-uniform local extension is a substantive structural property rather than the elementary finite-dimensional extension available separately on each `E`.

The finite interpolation proof (11)--(16) is elementary, and the operator-topology consequence is an immediate reformulation. A targeted literature search did not identify a need for a new theorem name, and this finding makes no claim that the density statement itself is novel. Its durable Arithmetic Fidelity value is the category audit it supplies after AF-095--AF-096: pointwise finite observability is too weak to witness a global extension defect even when norm topology sees that defect robustly.

## Boundaries and failure modes

- The result concerns bounded linear operator extension from a closed Banach subspace. It does not classify nonlinear extension, operator ideals with extra structure, positivity-preserving extension, equivariant extension, order extension, or arithmetic admissibility constraints.
- Exact matching on every finite-dimensional subspace does not produce one compatible family `S_E`. Compatibility is a separate global condition.
- The bound `n\|T\|` is only a universal elementary estimate. Better projection constants may be available for specific `E\subset X`; no sharpness is claimed.
- `\mathrm{SOT}` density says nothing about norm density. A positive AF-095 distance can coexist with exact matching on every finite sample because the local extension norms can grow and the chosen extensions can drift globally.
- The theorem rules out witnesses that factor through finitely many point evaluations and, by density, all `\mathrm{SOT}`-continuous scalar separators. It does not rule out infinite-coordinate source-natural observables with a topology stronger than `\mathrm{SOT}`.
- No rational-prime specificity or RH conclusion follows.

## Consequences for Arithmetic Fidelity

AF-095 showed that positive norm distance from the extendable range is equivalent to a bounded Hahn--Banach witness. AF-096 then showed that one apparently natural regularity restriction on that witness -- declaring a predual and asking for weak-star normality -- collapses the barycentric defect when the coefficient becomes dual.

AF-097 supplies a different admissibility obstruction that does not alter the coefficient category. If admissible source observations consist only of finitely many values of the forgotten-fiber operator, then **every candidate defect and every extendable control have exactly the same finite observation envelope**. The obstruction is not hidden because the right finite test has not yet been found; no finite pointwise test exists.

This isolates the next live boundary more sharply. A source-justified observable for a robust extension defect must carry some form of global coherence or uniform control across infinitely many fiber directions. In future arithmetic applications, an abstract norm-separating functional should therefore not be accepted as a meaningful discriminator until the proposed source category explains how that global aggregation is generated intrinsically rather than manufactured after the nonextension is already known.