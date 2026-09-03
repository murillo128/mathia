# AF-089 — Compact fiber compatibility globalizes exact Lipschitz fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-COMPACTNESS-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

AF-088 showed that for a bounded linear surjection between Banach spaces, reflexivity of the source removes the factor `3` in AF-087: a Lipschitz right inverse on one nontrivial quotient ball globalizes with exactly the same Lipschitz constant. The proof used weak compactness of bounded fiber slices.

The reusable mechanism is more general. Reflexivity is only one way to obtain the compactness needed to close all finite compatibility constraints.

### Compact-fiber selection principle

Let `(M,rho)` be a metric space. Let `Z` be a Hausdorff topological space equipped with a function

\[
d:Z\times Z\longrightarrow [0,+\infty]
\]

such that every sublevel set

\[
\{(u,v)\in Z\times Z:d(u,v)\le c\}
\]

is closed. For each `x in M`, let `K_x subset Z` be nonempty and compact.

Fix `L>=0`. Suppose that for every finite set `A subset M` there exists a selection

\[
s_A:A\to Z,
\qquad s_A(x)\in K_x,
\]

such that

\[
d(s_A(x),s_A(y))\le L\rho(x,y)
\qquad(x,y\in A).
\tag{1}
\]

Then there exists one global selection

\[
s:M\to Z,
\qquad s(x)\in K_x,
\]

satisfying the same inequalities

\[
\boxed{
d(s(x),s(y))\le L\rho(x,y)
\quad\text{for all }x,y\in M.
}
\tag{2}
\]

No convexity, finite-dimensionality, sequential compactness, or choice of compatible finite selections is required. Compactness itself performs the compatibility step.

### Weak-star dual-quotient corollary

Let `X` and `Y` be real or complex Banach spaces and let

\[
q:X^*\longrightarrow Y^*
\tag{3}
\]

be a bounded linear surjection that is continuous from `sigma(X^*,X)` to `sigma(Y^*,Y)`. Define the local and global Lipschitz right-inverse costs exactly as in AF-087/AF-088:

\[
\lambda_{\mathrm{Lip}}(q)
:=
\inf\{\operatorname{Lip}(S):S:Y^*\to X^*,\ qS=I_{Y^*}\},
\tag{4}
\]

and

\[
\lambda_{\mathrm{locLip}}(q)
:=
\inf\left\{
\operatorname{Lip}(s):
\begin{array}{l}
y_0\in Y^*,\ r>0,\\
s:y_0+rB_{Y^*}\to X^*,\\
qs(y)=y
\end{array}
\right\}.
\tag{5}
\]

Then

\[
\boxed{
\lambda_{\mathrm{locLip}}(q)
=
\lambda_{\mathrm{Lip}}(q).
}
\tag{6}
\]

More precisely, every `L`-Lipschitz right inverse on one nontrivial ball produces a global `L`-Lipschitz right inverse.

This strictly extends the hypothesis of AF-088. The source `X^*` need not be reflexive. Banach--Alaoglu supplies weak-star compactness of the bounded fiber slices, while weak-star continuity of `q` makes the fibers weak-star closed.

A particularly natural special case is a restriction quotient. If `Y` is a closed subspace of `X`, then

\[
R:X^*\to Y^*,
\qquad
R(x^*)=x^*|_Y,
\tag{7}
\]

is surjective by Hahn--Banach and weak-star to weak-star continuous. Hence

\[
\boxed{
\lambda_{\mathrm{locLip}}(R)
=
\lambda_{\mathrm{Lip}}(R)
}
\tag{8}
\]

for every Banach-space inclusion `Y subset X`, independently of reflexivity.

The Arithmetic Fidelity conclusion is therefore sharper than AF-088's initial boundary:

\[
\boxed{
\text{exact local-to-global fidelity is driven by compact admissible fiber slices,}
\text{ not by reflexivity itself.}
}
\tag{9}
\]

Reflexive weak compactness and dual weak-star compactness are two realizations of the same compact-compatibility mechanism.

## Derivation

### 1. Compactness closes arbitrary finite compatibility

Form the product

\[
K:=\prod_{x\in M}K_x.
\tag{10}
\]

By Tychonoff, `K` is compact. An element `z in K` is an unconstrained choice `z_x in K_x` for every `x`.

For each ordered pair `(x,y)` define

\[
C_{x,y}
:=
\{z\in K:d(z_x,z_y)\le L\rho(x,y)\}.
\tag{11}
\]

The coordinate map

\[
z\mapsto(z_x,z_y)
\]

is continuous, and the relevant `d`-sublevel set is closed. Therefore every `C_{x,y}` is closed in `K`.

The family `{C_{x,y}}` has the finite-intersection property. Indeed, a finite collection of pair constraints involves only finitely many points `A subset M`. By hypothesis there is one selection `s_A` satisfying all pair inequalities on `A`. Use those values on the coordinates in `A` and choose arbitrary elements of the remaining nonempty `K_x`. This gives a point of every selected `C_{x,y}`.

Compactness of `K` now yields

\[
\bigcap_{x,y\in M}C_{x,y}\ne\varnothing.
\tag{12}
\]

Any element of this intersection is the desired global selection. This proves (2).

The principle is deliberately elementary. It does not say that checking subsets below some fixed cardinality is sufficient; it assumes feasibility on every finite subset and uses compactness only to pass from all finite constraints to the infinite system.

### 2. A local quotient section gives all finite selections at the same cost

Now assume (3), and suppose that

\[
s:y_0+rB_{Y^*}\to X^*
\]

is an `L`-Lipschitz right inverse. Center it as in AF-087:

\[
f(h):=s(y_0+h)-s(y_0),
\qquad h\in rB_{Y^*}.
\tag{13}
\]

Then

\[
f(0)=0,
\qquad qf(h)=h,
\qquad \operatorname{Lip}(f)\le L,
\qquad \|f(h)\|\le L\|h\|.
\tag{14}
\]

For each positive integer `n`, dilate the same patch:

\[
f_n(y):=n f(y/n),
\qquad y\in nrB_{Y^*}.
\tag{15}
\]

Thus

\[
qf_n(y)=y,
\qquad
\operatorname{Lip}(f_n)\le L,
\qquad
\|f_n(y)\|\le L\|y\|.
\tag{16}
\]

Every finite subset of `Y^*` lies in one common ball `nrB_{Y^*}`, so (16) provides exactly the finite compatibility required by the compact-fiber principle.

### 3. Banach--Alaoglu supplies the compact fiber slices

For each `y in Y^*`, define

\[
K_y
:=
\{x^*\in X^*:qx^*=y,\ \|x^*\|\le L\|y\|\}.
\tag{17}
\]

Equation (16) shows that every `K_y` is nonempty. The closed norm ball

\[
L\|y\|B_{X^*}
\]

is compact in `sigma(X^*,X)` by Banach--Alaoglu. Since `q` is weak-star to weak-star continuous and the weak-star topology of `Y^*` is Hausdorff, the affine fiber

\[
q^{-1}(\{y\})
\]

is weak-star closed. Hence each `K_y` is weak-star compact.

Use `Z=X^*` with its weak-star topology and

\[
d(u,v)=\|u-v\|.
\tag{18}
\]

For every `c>=0`, the set

\[
\{(u,v):\|u-v\|\le c\}
\]

is weak-star closed: subtraction is weak-star continuous and the closed norm ball is weak-star compact, hence weak-star closed in the Hausdorff dual space. Therefore the compact-fiber principle applies and produces

\[
S:Y^*\to X^*,
\qquad
qS=I_{Y^*},
\qquad
\operatorname{Lip}(S)\le L.
\tag{19}
\]

Every global section restricts to a local one, so

\[
\lambda_{\mathrm{locLip}}(q)
\le
\lambda_{\mathrm{Lip}}(q).
\tag{20}
\]

Conversely, applying (19) to local sections with constants arbitrarily close to `lambda_locLip(q)` gives the reverse inequality. This proves (6), including the `+infinity` case.

### 4. Restriction quotients are automatically in the weak-star category

Let `j:Y\hookrightarrow X` be the inclusion of a closed subspace. The adjoint

\[
j^*:X^*\to Y^*
\]

is exactly restriction. Hahn--Banach says every `y^* in Y^*` has a norm-preserving extension to `X^*`, so `j^*` is surjective. For each fixed `y in Y`,

\[
(j^*x^*)(y)=x^*(j y),
\tag{21}
\]

which is a weak-star coordinate functional on `X^*`. Therefore `j^*` is weak-star to weak-star continuous, proving (8).

This is not a special feature of restriction maps: every weak-star continuous dual-space quotient has the same exact globalization property. Restriction maps simply make the predual origin and surjectivity completely transparent.

## Exact controls

### Nonreflexive source control

Take

\[
X=\ell^1,
\qquad
Y=\{x\in\ell^1:x_{2k-1}=0\text{ for all }k\}.
\]

Then `X^*=ell^infinity`, which is nonreflexive, and `Y^*` is canonically another copy of `ell^infinity`. The restriction map is the even-coordinate projection

\[
R((a_n)_{n\ge1})=(a_{2k})_{k\ge1}.
\tag{22}
\]

Zero-filling the odd coordinates is a linear isometric right inverse, so

\[
\lambda_{\mathrm{locLip}}(R)
=
\lambda_{\mathrm{Lip}}(R)
=1.
\tag{23}
\]

This does not prove the theorem, but it is an exact matched control showing that source reflexivity is not necessary for the no-loss conclusion. The weak-star compactness route applies directly.

### Reflexive source recovers AF-088

If `E` is reflexive, take `Z=E` with the weak topology. Bounded closed balls are weakly compact, affine fibers of a bounded linear map are weakly closed, and norm-distance sublevel sets are weakly closed. The compact-fiber principle reproduces AF-088 verbatim.

Thus AF-088 is one specialization of the more abstract compatibility theorem rather than a separate phenomenon.

### Compactness is sufficient, not claimed necessary

The theorem does **not** say that a quotient can have exact local/global cost equality only if some chosen bounded-fiber topology is compact. Another mechanism may force equality without a compactness proof. Equation (9) is a statement about the mechanism isolated here, not a characterization of every possible quotient.

### Weak-star continuity is load-bearing

If `X^*` is a dual space but

\[
q:X^*\to F
\]

is an arbitrary norm-continuous quotient, its fibers need not be weak-star closed for the given predual. Banach--Alaoglu then does not make the slices (17) compact in a topology compatible with the right-inverse constraint.

Even when the target is another dual space, a bounded linear map need not be weak-star to weak-star continuous for the chosen preduals. The present theorem therefore does not remove AF-088's unresolved unrestricted nonreflexive optimal-cost gap; it relocates the boundary to **topological compatibility of the quotient with a compact dual structure**.

### No canonicity follows from compactness

The Tychonoff argument selects a globally compatible point in a product. It gives no reason for the resulting right inverse to be linear, homogeneous, weak-star continuous, measurable, equivariant, order-preserving, computable, or canonical.

Thus exact metric recovery and structural/natural recovery remain different fidelity categories, in agreement with AF-078--AF-080.

## Prior art and novelty assessment

The proof mechanism is classical compactness, and no novelty is claimed for Banach--Alaoglu, Hahn--Banach, Tychonoff compactness, weak-star topology, or the general idea of obtaining selections from compact compatibility.

- Leonidas Alaoglu, **“Weak Topologies of Normed Linear Spaces,”** *Annals of Mathematics* 41 (1940), 252--267, DOI `10.2307/1968829`. This is the classical source behind compactness of the closed unit ball in a dual space under the weak-star topology.
- Charles Fefferman and Pavel Shvartsman, **“Sharp Finiteness Principles for Lipschitz Selections,”** *Geometric and Functional Analysis* 28(6) (2018), 1641--1705, DOI `10.1007/s00039-018-0467-6`. They prove much stronger finite-test principles for Lipschitz selections of compact convex finite-dimensional-valued set-valued maps: under their hypotheses one need only check subsets up to a fixed sharp cardinality, with controlled global Lipschitz norm. The elementary principle above instead assumes compatible selections on **every** finite subset and therefore follows directly from compactness; it must not be presented as a new finiteness principle.
- Gilles Godefroy and Nigel J. Kalton, **“Lipschitz-free Banach spaces,”** *Studia Mathematica* 159(1) (2003), 121--141, DOI `10.4064/sm159-1-6`. Their quotient-lifting theorem remains the decisive separable-target prior art used in AF-082: a Lipschitz right inverse of a linear quotient onto a separable Banach space forces a linear right inverse.
- AF-087 and AF-088 supply the immediately preceding Mathia results: local quotient Lipschitz repair always globalizes with a universal factor `3`, while weak compactness of reflexive source balls removes that quantitative loss.

A targeted search across Lipschitz selection finiteness principles, local Lipschitz right inverses of Banach quotients, weak-star continuous quotient maps, and compact-selection arguments did not locate the exact identity (6) as a named theorem. That absence is **not** a novelty proof. The durable result is the exact derivation and the corrected boundary it establishes for this line: the factor-`3` frontier is already closed on every weak-star continuous dual quotient, including nonreflexive sources.

## Boundaries and failure modes

- The general compact-fiber principle assumes feasibility on every finite subset. It does not provide a bounded-cardinality test and does not compete with Helly-type or Fefferman--Shvartsman finiteness theorems.
- In the dual quotient corollary, the weak-star structures are part of the data. Changing preduals can change which maps are weak-star continuous.
- Banach--Alaoglu gives compactness of bounded dual balls, but the fiber intersection is useful only because weak-star continuity makes the quotient equation weak-star closed.
- The construction is nonconstructive and does not preserve extra structure beyond the pairwise Lipschitz inequalities and fiber membership.
- The theorem concerns complete representative recovery for a linear quotient. A specific discriminator may descend through a weaker representation without requiring a full right inverse.
- The theorem does not determine whether a strict gap

\[
\lambda_{\mathrm{locLip}}(q)
<
\lambda_{\mathrm{Lip}}(q)
\]

exists for some genuinely non-dual-compatible, nonreflexive Banach quotient. That remains the natural quantitative boundary left by AF-087--AF-089.
- No rational-prime or RH-specific conclusion follows directly. The reusable lesson for later arithmetic compressions is that **finite-scale faithful representatives can globalize with zero distortion loss when the admissible fibers admit a compact topology in which all fidelity constraints are closed**. Before attributing a local/global gap to arithmetic or geometry, one should first test whether a hidden weak, weak-star, or other compact-fiber topology already removes it.
