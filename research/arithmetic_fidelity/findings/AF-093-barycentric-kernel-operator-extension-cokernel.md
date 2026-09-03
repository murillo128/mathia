# AF-093 — Barycentric-kernel operator nonextension is the exact Lipschitz fidelity defect

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `OPERATOR-EXTENSION-REFORMULATION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
0\longrightarrow Z_F\xrightarrow{j}\mathcal F(F)\xrightarrow{\beta_F}F\longrightarrow0,
\qquad
Z_F:=\ker\beta_F,
\tag{1}
\]

be the canonical Lipschitz-free exact sequence of a real Banach space `F`, and let `K` be a real Banach space. Write `\mathcal L(X,Y)` for bounded linear operators. Restriction along `j` gives

\[
j^*:\mathcal L(\mathcal F(F),K)\longrightarrow\mathcal L(Z_F,K),
\qquad
j^*(S)=S|_{Z_F}.
\tag{2}
\]

Then the exact Lipschitz-versus-linear quotient-repair defect from AF-092 has the concrete operator-extension description

\[
\boxed{
\ker\!\left(
\beta_F^*: \operatorname{Ext}(F,K)
\to
\operatorname{Ext}(\mathcal F(F),K)
\right)
\cong
\frac{\mathcal L(Z_F,K)}{j^*\mathcal L(\mathcal F(F),K)}.
}
\tag{3}
\]

The quotient in (3) is algebraic: two operators `T_1,T_2:Z_F\to K` define the same defect class exactly when `T_1-T_2` extends to a bounded linear operator on `\mathcal F(F)`. No closedness or Banach-space quotient structure is asserted.

Equivalently, for fixed `F` and `K`,

\[
\boxed{
\beta_F^*\text{ is injective}
\iff
\text{every bounded }T:Z_F\to K\text{ extends boundedly to }\mathcal F(F).
}
\tag{4}
\]

Moreover every class on the left of (3) is represented by the pushout of (1) along some `T:Z_F\to K`. That pushout has a canonical `1`-Lipschitz right inverse induced by the Dirac embedding `\delta_F`. Thus the operator-extension quotient in (3) is not merely an abstract description of `Ext`: it parametrizes precisely the extension obstructions that disappear when bounded linear quotient repair is enlarged to Lipschitz quotient repair.

Two universal consequences sharpen the target-side and kernel-side gates of AF-092 and AF-091:

\[
\boxed{
F\text{ has the Lipschitz lifting property}
\iff
Z_F\text{ is complemented in }\mathcal F(F)
\iff
\forall K\;\forall T:Z_F\to K,\ T\text{ extends to }\mathcal F(F),
}
\tag{5}
\]

and

\[
\boxed{
K\text{ ultrasummand}
\Longrightarrow
\forall F\;\forall T:Z_F\to K,\ T\text{ extends to }\mathcal F(F).
}
\tag{6}
\]

Statement (6) is specific to the barycentric kernel `Z_F\subset\mathcal F(F)`; it is not a claim that ultrasummand targets extend operators from arbitrary Banach subspaces.

## Derivation

### 1. The homology sequence turns the abstract pullback kernel into an operator-extension cokernel

Apply the contravariant functor `\mathcal L(-,K)` and its first derived functor `\operatorname{Ext}(-,K)` to the short exact sequence (1). The standard Banach-space homology sequence contains the exact segment

\[
\mathcal L(\mathcal F(F),K)
\xrightarrow{j^*}
\mathcal L(Z_F,K)
\xrightarrow{\partial}
\operatorname{Ext}(F,K)
\xrightarrow{\beta_F^*}
\operatorname{Ext}(\mathcal F(F),K).
\tag{7}
\]

Exactness at `\mathcal L(Z_F,K)` and `\operatorname{Ext}(F,K)` gives

\[
\ker\partial=\operatorname{im}j^*,
\qquad
\operatorname{im}\partial=\ker\beta_F^*.
\tag{8}
\]

Therefore `\partial` descends to the bijection (3).

This is the exact refinement missing from AF-092. AF-092 located nonlinear repair in `\ker\beta_F^*`; (7)--(8) identify what an element of that kernel actually is: a bounded operator on the forgotten barycentric fiber, modulo the operators that were already compatible with the uncompressed free space.

### 2. The connecting map is the pushout obstruction to extending `T`

For `T\in\mathcal L(Z_F,K)`, form the Banach pushout

\[
P_T=
\bigl(K\oplus_1\mathcal F(F)\bigr)
\Big/
N_T,
\qquad
N_T=\{(Tz,-jz):z\in Z_F\}.
\tag{9}
\]

Because the second coordinate contains `-jz` isometrically, `N_T` is closed. Define

\[
\iota_T(k)=[(k,0)],
\qquad
q_T[(k,m)]=\beta_F(m).
\tag{10}
\]

Then

\[
0\to K\xrightarrow{\iota_T}P_T\xrightarrow{q_T}F\to0
\tag{11}
\]

is the pushout extension representing `\partial T`.

The standard pushout criterion says

\[
\partial T=0
\iff
T\text{ extends to some }S\in\mathcal L(\mathcal F(F),K).
\tag{12}
\]

This can also be checked directly. If `S|_{Z_F}=T`, the map

\[
[(k,m)]\longmapsto k+S(m)
\tag{13}
\]

is well defined on the quotient and supplies the splitting data. Conversely, a splitting of the pushout recovers a bounded extension of `T`. Thus the denominator in (3) is exactly the class of operator data that can already be propagated across the compression fiber.

### 3. Every pushout defect has a canonical Lipschitz section

The Dirac embedding gives

\[
s_T:F\to P_T,
\qquad
s_T(y)=[(0,\delta_F(y))].
\tag{14}
\]

Since `\beta_F\delta_F=I_F`,

\[
q_Ts_T=I_F.
\tag{15}
\]

Using the quotient norm and the isometry of `\delta_F`,

\[
\|s_T(y)-s_T(y')\|
\le
\|\delta_F(y)-\delta_F(y')\|
=
\|y-y'\|,
\tag{16}
\]

so `s_T` is `1`-Lipschitz.

Hence every operator `T` produces a representative of `\partial T` that is already Lipschitz-split. It is linearly split exactly when `T` is extendable. This gives a concrete representative-level version of AF-092's class-level identity

\[
\ker\beta_F^*
=
\{\text{Lipschitz-splittable extension classes}\}.
\tag{17}
\]

### 4. The target-side lifting property is universal extension from `Z_F`

Suppose `\beta_F` has a bounded linear right inverse `A:F\to\mathcal F(F)`. Then

\[
P=I_{\mathcal F(F)}-A\beta_F
\tag{18}
\]

is a bounded projection from `\mathcal F(F)` onto `Z_F`. For every Banach space `K` and every `T:Z_F\to K`, the operator `TP` extends `T` to all of `\mathcal F(F)`.

Conversely, if every operator `Z_F\to K` extends for every `K`, take `K=Z_F` and `T=I_{Z_F}`. An extension `P:\mathcal F(F)\to Z_F` of the identity is a bounded projection, so (1) splits and `\beta_F` has a bounded linear right inverse.

Combining this with Godefroy--Kalton's characterization used in AF-092 proves (5). In particular, for separable `F`, every bounded operator from the special kernel `Z_F` into every Banach space extends to `\mathcal F(F)`.

### 5. The ultrasummand gate becomes a coefficient-side extension theorem

AF-091 proves that a quotient extension with ultrasummand kernel `K` cannot be Lipschitz-split without already being linearly split. Every pushout (11) is Lipschitz-split by (14)--(16). Therefore, if `K` is ultrasummand, every `\partial T` is zero. By (12), every bounded

\[
T:Z_F\to K
\tag{19}
\]

extends to `\mathcal F(F)`, proving (6).

This is the coefficient-side counterpart to (5). The target condition in (5) complements the particular subspace `Z_F` and therefore extends operators into arbitrary `K`; the coefficient condition in (6) fixes `K` and forces extension from every barycentric kernel `Z_F`, even when `Z_F` is not complemented.

## Exact controls

### Split / lifting-property target

If `F` has the Lipschitz lifting property, `Z_F` is complemented in `\mathcal F(F)`, so restriction `j^*` is surjective for every `K`. The quotient in (3) is zero and no Lipschitz-but-not-linear defect remains. For separable `F`, Godefroy--Kalton place the system in this regime.

### Nonlifting target and the identity witness

If `F` fails the Lipschitz lifting property, the identity

\[
I_{Z_F}:Z_F\to Z_F
\tag{20}
\]

cannot extend to a bounded operator `\mathcal F(F)\to Z_F`; such an extension would be a projection. Its connecting class `\partial I_{Z_F}` is exactly the canonical nonsplit free-space sequence (1), up to the standard pushout identification. Thus failure of target lifting has a distinguished operator-nonextension witness rather than only an existential `Ext` class.

### Ultrasummand coefficient

If `K` is reflexive, a dual Banach space, L-embedded, or more generally complemented in `K^{**}`, AF-091 applies and the quotient in (3) vanishes for every `F`. This is a special extension theorem for `Z_F\subset\mathcal F(F)`, not a general injectivity property of such `K`.

### Aharoni--Lindenstrauss escape

For a classical nonseparable Lipschitz-but-not-linear lifting example with kernel `c_0`, AF-092 gives a nonzero class in `\ker\beta_F^*`. Equation (3) therefore forces the existence of a bounded operator

\[
T:Z_F\to c_0
\tag{21}
\]

that does not extend boundedly to `\mathcal F(F)`. The nonlinear quotient phenomenon can therefore be re-read as a concrete failure of operator extension on the barycentric kernel.

### Representative dependence and norm control

The isomorphism (3) is at the level of extension classes. Different equivalent representatives of one `Ext` class need not preserve a chosen quotient norm or the optimal Lipschitz-section constant. The pushout representative (11) has a canonical `1`-Lipschitz section, but this does not say that every equivalent quotient realization has optimal Lipschitz constant `1`.

## Prior art and novelty assessment

The mechanism is classical homological Banach-space theory, and **no novelty is claimed** for the long homology sequence, pushouts, connecting morphisms, operator-extension obstructions, Lipschitz-free spaces, or the barycenter map.

- Félix Cabello Sánchez and Jesús M. F. Castillo, ***Homological Methods in Banach Space Theory***, Cambridge Studies in Advanced Mathematics 203, Cambridge University Press (2023), Chapter 4, **“The Functor Ext and the Homology Sequences,”** pp. 197--242, DOI `10.1017/9781108778312.006`. Role: authoritative modern source for `Ext`, longer exact sequences, connecting maps, and their use in Banach-space homology.
- Félix Cabello Sánchez and Jesús M. F. Castillo, **“The Long Homology Sequence for Quasi-Banach Spaces, with Applications,”** *Positivity* 8(4) (2004), 379--394, DOI `10.1007/s11117-002-2465-y`. Role: primary source establishing long homology sequences in the quasi-Banach/Banach setting.
- Jesús M. F. Castillo, Yolanda Moreno, and Jesús Suárez, **“On Lindenstrauss--Pełczyński spaces,”** *Studia Mathematica* 174(3) (2006), 213--231, DOI `10.4064/sm174-3-1`. Role: explicit operator-extension/pushout language; extending an operator from the kernel of an exact sequence is equivalent to triviality of the corresponding pushout extension.
- Gilles Godefroy and Nigel J. Kalton, **“Lipschitz-free Banach spaces,”** *Studia Mathematica* 159(1) (2003), 121--141, DOI `10.4064/sm159-1-6`. Role: universal Lipschitz linearization and the separable Lipschitz lifting property used to interpret the canonical barycenter sequence.

A targeted search did not identify a source packaging the particular specialization (3) for the barycentric kernel as an Arithmetic Fidelity classifier. That absence is **not** a novelty claim: (3) is the immediate specialization of the classical homology sequence to (1), combined with AF-092's already-derived identification of `\ker\beta_F^*` with Lipschitz-splittable extension classes. Its durable value is conceptual and operational: it replaces the phrase “nonlinear recovery forgets some extension obstruction” by the exact statement “the forgotten obstruction is a bounded operator on `Z_F`, modulo bounded extension to `\mathcal F(F)`.”

## Boundaries and failure modes

- The claim uses the ordinary Banach-space `Ext`/bounded-linear category and the real Lipschitz-free formalism used in AF-092. No automatic identification with complex `Ext`, quasi-Banach variants, operator ideals, Hölder recovery, or other categories is asserted.
- The quotient in (3) is an algebraic quotient unless additional closed-range information is proved. In particular, no norm, Hausdorff topology, stability modulus, or quantitative distance-to-extendability is obtained for free.
- The theorem classifies **complete quotient representative repair**. A discriminator-specific observable may survive without supplying a right inverse of the quotient, so weaker notions of fidelity can lie outside this extension-theoretic model.
- The pushout section (14) is canonical only relative to the chosen free-space presentation and pushout construction. It need not respect extra order, group action, arithmetic provenance, positivity, locality, or another admissibility constraint.
- Statement (6) is not a general operator-extension theorem for ultrasummand spaces. The domain subspace must be the canonical `Z_F` inside `\mathcal F(F)`; the proof uses its special property that every pushout along it is automatically Lipschitz-split.
- No prime-specific or RH conclusion follows. The reusable Arithmetic Fidelity lesson is sharper: **a category change can erase an obstruction exactly because data living on the forgotten kernel cease to be nonextendable in the enlarged recovery category.**

## Consequences for Arithmetic Fidelity

AF-092 converted Lipschitz nonlinear repair into the abstract homological kernel `\ker\beta_F^*`. AF-093 resolves that kernel one level further into concrete retained-versus-forgotten data: bounded operators on the compression fiber `Z_F`, modulo those compatible with the full pre-compression object `\mathcal F(F)`.

This supplies a reusable template for future compression categories. Whenever a transformation admits a canonical exact presentation and a broader recovery category admits a universal linearization, the next question is not merely whether the induced map on obstruction classes has a kernel. It is whether that kernel can itself be represented as a quotient of **fiber data by extendable data**. In the Lipschitz-free Banach setting this template is now exact; outside it, it remains a falsifiable research program rather than an analogy.