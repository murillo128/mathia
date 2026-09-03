# AF-088 — Reflexive local Lipschitz quotient repair globalizes with no loss

**Status:** `EXACT-DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-COMPACTNESS-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `E` and `F` be real or complex Banach spaces, let

\[
q:E\to F
\]

be a bounded linear surjection, and assume that **the source space `E` is reflexive**. Use the local and global Lipschitz section costs from AF-087:

\[
\lambda_{\mathrm{Lip}}(q)
:=
\inf\{\operatorname{Lip}(L):L:F\to E,\ qL=I_F\},
\]

and

\[
\lambda_{\mathrm{locLip}}(q)
:=
\inf\left\{
\operatorname{Lip}(s):
\begin{array}{l}
y_0\in F,\ r>0,\\
s:y_0+rB_F\to E,\\
qs(y)=y
\end{array}
\right\},
\]

with the infimum of an empty family interpreted as `+∞`. Then

\[
\boxed{
\lambda_{\mathrm{locLip}}(q)
=
\lambda_{\mathrm{Lip}}(q).
}
\tag{1}
\]

More precisely, every `L`-Lipschitz right inverse on one nontrivial quotient ball gives a **global `L`-Lipschitz right inverse**. Thus reflexivity removes the universal factor `3` in AF-087's elementary conical globalization bound.

If, in addition, `F` is separable, AF-082/Godefroy--Kalton gives

\[
\boxed{
\lambda_{\mathrm{locLip}}(q)
=
\lambda_{\mathrm{Lip}}(q)
=
\lambda_{\mathrm{lin}}(q),
}
\tag{2}
\]

where `lambda_lin(q)` is the best norm of a bounded linear right inverse. Hence, for quotients with reflexive source and separable target, **there is no quantitative advantage at all in passing from linear splitting to global Lipschitz repair or even to Lipschitz repair on a single neighborhood**.

The reusable Arithmetic Fidelity conclusion is that AF-087's factor `3` is not intrinsic to locality. In reflexive sources, weak compactness lets compatible finite-scale repairs be assembled without degrading the Lipschitz constant. The remaining gap in the unrestricted Banach category is therefore a **compactness issue**, not a directional or scaling issue.

## Derivation

### 1. Center the local section

Suppose that for some `y_0 in F`, `r>0`, and finite `L` there is an `L`-Lipschitz section

\[
s:y_0+rB_F\to E,
\qquad
qs(y)=y.
\]

As in AF-087, define

\[
f(h):=s(y_0+h)-s(y_0),
\qquad h\in rB_F.
\]

Then

\[
f(0)=0,
\qquad
qf(h)=h,
\qquad
\operatorname{Lip}(f)\le L.
\tag{3}
\]

In particular,

\[
\|f(h)\|\le L\|h\|.
\tag{4}
\]

### 2. Dilate the same local repair to every finite scale

For each positive integer `n`, define

\[
f_n:nrB_F\to E,
\qquad
f_n(y):=n f(y/n).
\tag{5}
\]

Then, on its domain,

\[
qf_n(y)=y,
\qquad
f_n(0)=0,
\qquad
\operatorname{Lip}(f_n)\le L,
\tag{6}
\]

and

\[
\|f_n(y)\|\le L\|y\|.
\tag{7}
\]

Therefore every **finite** subset of `F` is contained in the domain of one common `f_n`, and on that finite set the quotient has an `L`-Lipschitz section with the same radial bound (7).

The point is that scaling already supplies exact finite compatibility at arbitrarily large radii. AF-087 used a conical formula to turn this into one explicit global map and paid a factor `3`. Reflexivity allows a different final step: compactness can choose a globally compatible limit without modifying any pairwise inequality.

### 3. Build compact fiber slices

For each `y in F`, set

\[
K_y
:=
\{e\in E:q e=y,\ \|e\|\le L\|y\|\}.
\tag{8}
\]

Each `K_y` is nonempty: choose `n` with `y in nrB_F` and use `f_n(y)`. Since `E` is reflexive, the closed ball `L||y|| B_E` is weakly compact. The affine fiber `q^{-1}(y)` is weakly closed because a bounded linear map is weak-to-weak continuous. Hence every `K_y` is weakly compact.

For `y=0`, (8) gives

\[
K_0=\{0\}.
\tag{9}
\]

Now form the product

\[
K:=\prod_{y\in F}K_y
\tag{10}
\]

with each factor carrying its weak topology. By Tychonoff compactness, `K` is compact.

An element `H in K` is simply a choice of one bounded representative `H(y)` in every quotient fiber; the quotient identity is already built into the product.

### 4. Impose all Lipschitz inequalities as closed constraints

For every pair `y,z in F`, let

\[
C_{y,z}
:=
\{H\in K:\|H(y)-H(z)\|\le L\|y-z\|\}.
\tag{11}
\]

Each `C_{y,z}` is closed in the product weak topology. Indeed, the coordinate map

\[
H\mapsto H(y)-H(z)
\]

is weakly continuous, and the norm ball

\[
\{e\in E:\|e\|\le L\|y-z\|\}
\]

is weakly closed.

The family `{C_{y,z}}` has the finite-intersection property. Given finitely many pair constraints, only finitely many points of `F` occur in them. Choose `n` large enough that all those points lie in `nrB_F`. Assign

\[
H(y)=f_n(y)
\]

on those finitely many coordinates. Equations (6)--(7) place those values in the corresponding `K_y` and satisfy every selected pair constraint. Fill all other coordinates by arbitrary elements of their nonempty `K_y`.

Thus every finite subfamily of the closed sets `C_{y,z}` has nonempty intersection. Compactness of `K` gives

\[
\bigcap_{y,z\in F}C_{y,z}\ne\varnothing.
\tag{12}
\]

Choose `H` in this intersection. Then, for every `y,z in F`,

\[
qH(y)=y,
\qquad
\|H(y)-H(z)\|\le L\|y-z\|.
\tag{13}
\]

Therefore `H:F->E` is a global `L`-Lipschitz right inverse of `q`.

This proves

\[
\lambda_{\mathrm{Lip}}(q)
\le
\lambda_{\mathrm{locLip}}(q).
\]

The reverse inequality follows by restricting any global section to a ball, proving (1).

## Exact controls

### Hilbert quotient control

If `E` is Hilbert and `q` is the normalized quotient by a closed subspace, the orthogonal minimum-norm section is linear and `1`-Lipschitz. Hence

\[
\lambda_{\mathrm{locLip}}(q)
=
\lambda_{\mathrm{Lip}}(q)
=
\lambda_{\mathrm{lin}}(q)
=1.
\]

The compactness theorem recovers the correct endpoint with no artificial constant.

### Reflexive nonsplitting control

Let `1<p<infty`, `p != 2`, and let `K subset ell^p` be a closed uncomplemented subspace of the kind used in AF-081. Then `E=ell^p` is reflexive and `F=ell^p/K` is separable. AF-082 says there is no global Lipschitz section, while (1) now says equivalently that there is no Lipschitz section on even one nontrivial quotient neighborhood. Quantitatively,

\[
\lambda_{\mathrm{locLip}}(q)
=
\lambda_{\mathrm{Lip}}(q)
=
\lambda_{\mathrm{lin}}(q)
=+\infty.
\]

This is the exact-cost version of AF-087's existence statement for this matched control.

### Split reflexive control with nontrivial projection cost

If a reflexive quotient splits linearly but its best section norm is larger than `1`, separability of `F` gives (2). A nonlinear local section cannot lower the optimum below the best linear splitting constant. Thus the equality is not confined to orthogonal/Hilbert quotients.

### Why the compactness hypothesis is doing real work

Without reflexivity, the sets `K_y` in (8) need not be weakly compact. The finite-intersection argument then has no reason to produce an `E`-valued global choice. AF-087 still gives a global section with a universal `3L` bound by an explicit conical formula, so existence survives; what is not established in the general Banach category is preservation of the **optimal constant**.

No strict nonreflexive example

\[
\lambda_{\mathrm{locLip}}(q)
<
\lambda_{\mathrm{Lip}}(q)
\]

is claimed here. Reflexivity is proved sufficient for equality, not necessary.

## Prior art and novelty assessment

The ingredients of the proof are classical: scaling in a linear quotient, weak compactness of bounded closed sets in reflexive Banach spaces, weak closedness of norm balls and affine fibers, and Tychonoff's finite-intersection compactness principle. No novelty is claimed for those mechanisms.

The closest quotient-section prior art remains the literature already audited in AF-082 and AF-087:

- Gilles Godefroy and Nigel J. Kalton, **“Lipschitz-free Banach spaces,”** *Studia Mathematica* 159(1) (2003), 121--141, DOI `10.4064/sm159-1-6`, for linearization of global Lipschitz sections onto separable quotient targets.
- Nigel J. Kalton, **“Spaces of Lipschitz and Hölder Functions and Their Applications,”** *Collectanea Mathematica* 55(2) (2004), 171--217, DOI `10.1344/CM.V55I2.4055`, especially the discussion preceding Proposition 7.2, for homogeneous normalization of uniformly continuous quotient sections on the unit ball and extension to the whole quotient while retaining bounded-scale uniform continuity.
- AF-087 for the unrestricted local-to-global Lipschitz existence theorem and its explicit universal factor `3`.

A targeted literature search for local Lipschitz right inverses of Banach quotients, reflexive-source quotient sections, pointwise-weak compactness of Lipschitz selections, and local-to-global Lipschitz lifting did not locate this exact optimal-cost formulation as a named theorem. That absence is **not** treated as a novelty proof. The durable claim here is the exact derivation and its structural boundary: weak compactness closes the finite-compatibility system without increasing the metric distortion, whereas the explicit conical construction works without compactness but pays a universal constant.

## Boundaries and failure modes

- Reflexivity is required here for the **source `E`**, because the selected representatives live in `E`. Reflexivity of the quotient `F` alone does not make the fiber slices `K_y subset E` weakly compact.
- Separability is not used in (1). It enters only when importing AF-082/Godefroy--Kalton to identify the common Lipschitz cost with the linear splitting cost in (2).
- The argument is nonconstructive: it proves existence of a global section by compactness and does not supply a canonical, measurable, equivariant, order-preserving, or algorithmically computable representative rule.
- The result controls the exact global Lipschitz constant. It does not imply that the resulting global section inherits homogeneity or any extra structure of the original local section.
- A local section must be Lipschitz between every pair of points in a full ball/neighborhood. Pointwise Lipschitz behavior, directional control, Hölder regularity, or bounded-ball uniform continuity remain weaker categories covered by AF-083--AF-087.
- The theorem uses the linear scaling symmetry of a Banach quotient. It does not automatically extend to nonlinear quotient maps, manifolds, general metric submersions, or arbitrary compression maps.
- The theorem concerns recovery of complete quotient representatives. A specific discriminator may require less information and may have a different fidelity threshold.
- No rational-prime or RH-specific conclusion follows directly. The relevance is the sharper general lesson that **compactness can turn all finite-scale faithful repairs into a globally faithful repair without quantitative loss**.