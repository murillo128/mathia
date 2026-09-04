# AF-104 — Reinov realizes the infinite bounded-accessibility regime

**Status:** `LITERATURE+DERIVED`, `CLASSICALIZED`, `EXACT-TRANSLATION`, `DECISIVE-EXISTENCE`, `NO-NOVELTY-CLAIM`

## Claim

The infinite-cost regime left open as a formal possibility in AF-100 and AF-101 is realized by a classical Banach-space construction.

There exist a completely separable Banach space `Z` with the approximation property but without the bounded approximation property, and an operator

\[
C\in\mathcal L(Z^*,Z^*)
\tag{1}
\]

such that, if

\[
R_\alpha\in\mathcal L(Z,Z),
\qquad
R_\alpha^*\longrightarrow C
\tag{2}
\]

pointwise on `Z\times Z^*`, then necessarily

\[
\|R_\alpha\|\longrightarrow+\infty.
\tag{3}
\]

This is Reinov's Corollary 3.4 in *Approximation of operators in dual spaces by adjoint operators*.

Let

\[
U:=C^*J_Z:Z\longrightarrow Z^{**}
\tag{4}
\]

be the transposed bidual realization used in AF-102. Then the AF-100 bounded pointwise weak-star accessibility gauge and the AF-102 second-leg accessibility cost satisfy

\[
\boxed{
 a_Z(U)=\beta_{Z,Z}(C)=+\infty.
}
\tag{5}
\]

Consequently AF-101's universal accessibility constant is genuinely infinite for this pair:

\[
\boxed{
C_{\mathrm{acc}}(Z,Z)=+\infty.
}
\tag{6}
\]

At the same time AF-100's unbudgeted density theorem gives

\[
U\in
\overline{J_Z\mathcal L(Z,Z)}^{\,\tau_{pw^*}}.
\tag{7}
\]

Hence every finite collection of declared scalar observations can still be reproduced arbitrarily well by genuine `Z`-valued operators; what fails is the existence of **any finite uniform norm budget** across those finite tests.

Thus there is an exact realized separation

\[
\boxed{
\text{unbudgeted finite observational reproducibility}
\not\Rightarrow
\text{bounded accessibility}.
}
\tag{8}
\]

The obstruction can be purely quantitative: all finite observations are individually spoofable, while every net that coheres them toward the target must pay a norm cost diverging to infinity.

## Derivation

### 1. Translate Reinov's adjoint approximation problem into the AF-100 target-accessibility problem

Reinov works with the natural isometric identification

\[
\mathcal L(Z,Z^{**})
\cong
\mathcal L(Z^*,Z^*)
\tag{9}
\]

that sends a bidual-valued operator `V:Z\to Z^{**}` to the restriction of `V^*` to `Z^*`, and sends `C:Z^*\to Z^*` back to

\[
C^*J_Z:Z\to Z^{**}.
\tag{10}
\]

For `R\in\mathcal L(Z,Z)`, the embedded target-valued operator `J_ZR` corresponds exactly to the adjoint `R^*`. Indeed, for every `z\in Z` and `z^*\in Z^*`,

\[
\langle J_ZRz,z^*\rangle
=z^*(Rz)
=\langle R^*z^*,z\rangle.
\tag{11}
\]

Therefore

\[
J_ZR_\alpha\to U
\quad\text{pointwise weak-star on }Z\times Z^*
\tag{12}
\]

is equivalent to

\[
R_\alpha^*\to C
\quad\text{pointwise on }Z\times Z^*.
\tag{13}
\]

This is not an analogy between the two frameworks: it is the same locally convex approximation problem under the canonical transpose identification.

### 2. Any finite accessibility radius contradicts Reinov's example

By AF-100,

\[
a_Z(U)
=
\inf\Bigl\{
M\ge0:
U\in
\overline{\{J_ZR:\|R\|\le M\}}^{\,\tau_{pw^*}}
\Bigr\}.
\tag{14}
\]

Suppose `a_Z(U)<\infty`. Choose a finite `M>a_Z(U)`. By the definition of the closure in (14), there exists a net `R_\alpha\in\mathcal L(Z,Z)` satisfying

\[
\|R_\alpha\|\le M
\tag{15}
\]

and (12). By (13), the adjoints converge to `C` pointwise on `Z\times Z^*` while remaining uniformly bounded. Reinov's Corollary 3.4 says that every such approximating net must instead satisfy (3). This contradiction proves

\[
a_Z(U)=+\infty.
\tag{16}
\]

AF-102 defines

\[
\beta_{Z,Z}(C)=a_Z(C^*J_Z),
\tag{17}
\]

so (16) gives the second equality in (5).

Finally AF-101 defines

\[
C_{\mathrm{acc}}(Z,Z)
=
\sup_{0\ne V\in\mathcal L(Z,Z^{**})}
\frac{a_Z(V)}{\|V\|}.
\tag{18}
\]

The single bounded nonzero operator `U` with `a_Z(U)=+\infty` forces (6).

### 3. Unbudgeted observability still collapses completely

AF-100 proves for arbitrary Banach spaces `X,K` that

\[
\overline{J_K\mathcal L(X,K)}^{\,\tau_{pw^*}}
=
\mathcal L(X,K^{**}).
\tag{19}
\]

Applying this with `X=K=Z` yields (7). Equivalently there exists at least one net of adjoints `R_\alpha^*` converging to `C` on every scalar coordinate `(z,z^*)`.

Combining this with Reinov's Corollary 3.4 says more than either statement alone: such approximation exists, but **every** convergent approximating net has unbounded norms, in fact norms tending to infinity.

For every fixed finite family

\[
(z_i,z_j^*)_{1\le i\le m,\,1\le j\le n}
\tag{20}
\]

and every `\varepsilon>0`, some genuine `R:Z\to Z` can therefore match all corresponding scalar observations within `\varepsilon`. No finite family of unbudgeted matrix coefficients detects the failure. The discriminator is the impossibility of making those local repairs coherent under one global resource bound.

### 4. Reinov's finite-tensor gauges are direct prior art for the AF bounded-observation gauge

Reinov also studies norms `\|\cdot\|_{W_n}` on operators `Y^*\to X^*`. For finite `n`, these quantify the least operator-norm radius needed to reproduce the pairing against tensors of bounded finite dimension. He records the radius characterization

\[
\|C\|_{W_n}
=
\inf\Bigl\{
r>0:
\text{every admissible finite tensor test is reproducible by some }R:X\to Y,
\ \|R\|\le r
\Bigr\},
\tag{21}
\]

with `n=+\infty` allowing arbitrary algebraic finite-tensor tests.

After the identification (9), this is the same classical bounded-adjoint-approximation geometry that AF-100 later packages as a closed absolutely convex accessibility envelope and polar gauge. AF-101's tensor-norm formulation is therefore not evidence for a new operator-theoretic phenomenon; it is a re-expression of a mature approximation/accessibility problem in Arithmetic Fidelity language.

## Exact controls and boundaries

### Approximation property is not a sufficient uniform-fidelity condition

Reinov's `Z` has the approximation property. Thus ordinary AP does not prevent (5). Finite-rank approximation or finite observational recoverability without a globally controlled norm is too weak to certify bounded fidelity.

The example was deliberately constructed with failure of the bounded approximation property, but this finding does **not** claim the converse statement

\[
\mathrm{BAP}\iff C_{\mathrm{acc}}(Z,Z)<\infty,
\tag{22}
\]

nor any analogous equivalence for arbitrary pairs `(X,K)`. Reinov's example proves an existence boundary, not a complete classification of `C_{\mathrm{acc}}` by standard approximation properties.

### This is stronger than an arbitrarily large finite distortion sequence

AF-101 proved abstractly that if the ratios between the relaxed and original finite-observation gauges are unbounded, completeness forces some operator to have infinite accessibility cost. Reinov supplies a concrete classical realization of that terminal regime: one fixed `C` already requires divergent approximation norms.

So the example is not merely a family with increasingly poor constants. It exhibits actual loss of all finite-budget recoverability for one bounded target object.

### The example does not establish a beta/eta separation

AF-103 introduced the stronger SOT recovery cost `\eta` and proved

\[
\beta(C)\le\eta(C).
\tag{23}
\]

For the Reinov operator, (5) therefore also forces

\[
\eta_{Z,Z}(C)=+\infty.
\tag{24}
\]

This does **not** answer AF-103's separate question whether there exist useful examples with a strict finite or infinite separation

\[
\beta(C)<\eta(C).
\tag{25}
\]

The new result realizes the failure of bounded scalar accessibility itself, not a gap between the two witness categories.

### Do not infer arithmetic specificity

Nothing in the example is arithmetic and no RH consequence follows. Its value for Arithmetic Fidelity is as a clean exact control demonstrating that a structural discriminator may be absent from every unbudgeted finite observation yet survive as a global **conditioning law**: the cost of coherent recovery can diverge even when local recovery is always possible.

## Prior art and novelty assessment

The decisive source is classical prior art:

- Oleg I. Reinov, **“Approximation of operators in dual spaces by adjoint operators,”** *Journal of Mathematical Sciences* 173(5), 632–642 (2011), DOI `10.1007/s10958-011-0263-4`. The paper studies exactly the approximation of `C:Y^*\to X^*` by adjoints `R^*`, both in pointwise `X\times Y^*` convergence and stronger operator topologies, together with the equivalent approximation of `C^*|_X:X\to Y^{**}` by operators `X\to Y`. Its finite-tensor `W_n` gauges are direct prior art for bounded finite-observation costs. Proposition 3.3 constructs a bidual-valued operator outside every finite-radius pointwise closure, and Corollary 3.4 gives the single-space form used in (1)–(5): a separable AP-but-not-BAP space `Z` and an operator whose every pointwise adjoint approximation has norms diverging to infinity.
- Åsvald Lima and Eve Oja, **“Ideals of operators, approximability in the strong operator topology, and the approximation property,”** *Michigan Mathematical Journal* 52(2), 253–265 (2004), DOI `10.1307/mmj/1091112074`. Role: neighboring classical framework connecting approximation properties, operator ideals, Hahn–Banach extension operators, and uniformly bounded nets whose adjoints converge in SOT; it reinforces that the norm-controlled adjoint-approximation theme underlying AF-103 belongs to established Banach-space theory.

Accordingly, **no theorem-level novelty is claimed** for the existence of infinite bounded-accessibility defects, bounded approximation by adjoints, or their relation to Banach-space approximation properties. The direct literature match is stronger than the prior-art boundary recorded in AF-100–AF-103 and materially classicalizes that part of the line.

The Arithmetic Fidelity contribution is only the translation into its general audit vocabulary: the example is an exact model in which finite unbudgeted observability is maximally nonfaithful while the resource-bounded recovery problem remains maximally obstructed.

## Consequences for Arithmetic Fidelity

AF-100 separated unbudgeted pointwise weak-star density from bounded accessibility but intentionally did not assert that the infinite-cost regime occurs. AF-101 showed abstractly that its accessibility constant has a finite-tensor norm formula and that unbounded distortion would force an actually inaccessible operator. AF-102 transported the same gauge to second-leg functoriality, and AF-103 reinterpreted it as bounded approximation by genuine preadjoints.

Reinov's 2011 construction closes the remaining existence question and simultaneously sharpens the novelty boundary. The line should no longer treat bounded versus unbounded adjoint accessibility in Banach spaces as merely an internally discovered abstract possibility: it is a classical operator-approximation phenomenon with explicit counterexamples.

The reusable structural lesson remains valuable beyond that prior art. In any later compression category, one should separately ask:

1. whether each finite observation can be reproduced at all;
2. whether those reproductions admit one uniform resource bound;
3. whether the bound stays stable under refinement/composition;
4. whether the resource itself is intrinsic to the declared category rather than an artifact of coordinates.

A positive answer to the first question alone can coexist with the strongest possible negative answer to the second. For prime-specific applications, this means that matching every finite observable by non-prime controls does not settle the problem if the required control complexity necessarily diverges — but claiming that escape requires an independently justified, mathematically natural resource budget rather than an arbitrary penalty introduced after the fact.