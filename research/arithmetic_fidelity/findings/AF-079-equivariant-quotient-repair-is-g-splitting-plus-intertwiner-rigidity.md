# AF-079 — Equivariant quotient repair is G-splitting plus intertwiner rigidity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let

\[
0\longrightarrow K\xrightarrow{i}E\xrightarrow{q}F\longrightarrow0
\tag{1}
\]

be a normalized short exact sequence of real or complex Banach spaces as in AF-078: `K=\ker q\subseteq E` carries the inherited norm, `F=E/K` carries the quotient norm, and `i` is inclusion. Let a group `G` act by bounded invertible operators

\[
u_g:E\to E,
\qquad
w_g:K\to K,
\qquad
v_g:F\to F,
\tag{2}
\]

so that the exact sequence is `G`-equivariant:

\[
u_g i=i w_g,
\qquad
q u_g=v_g q.
\tag{3}
\]

Call a bounded linear map

\[
r:E\to K
\tag{4}
\]

a **`G`-equivariant kernel repair** when

\[
r|_K=I_K,
\qquad
r u_g=w_g r
\quad(g\in G).
\tag{5}
\]

Then:

1. **Equivariant repair exists exactly when the extension `G`-splits.** The following are equivalent:

   \[
   \boxed{
   \begin{array}{c}
   \exists\text{ bounded `G`-equivariant repair }r:E\to K;\\
   K\text{ has a bounded `G`-invariant complement in }E;\\
   q\text{ has a bounded `G`-equivariant linear section }s:F\to E;\\
   (1)\text{ splits in the category of `G`-Banach spaces.}
   \end{array}}
   \tag{6}
   \]

   Thus symmetry is not merely a rule for choosing among the repairs of AF-078. It can impose a strictly stronger **existence gate** than ordinary Banach-space splitting.

2. **When one equivariant repair exists, all of them form a torsor over the intertwiner space.** Write

   \[
   \mathcal L_G(F,K)
   =
   \{A\in\mathcal L(F,K):A v_g=w_g A\ \forall g\in G\}.
   \tag{7}
   \]

   If `r_0` is one `G`-equivariant repair, every other one is uniquely

   \[
   \boxed{
   r_A=r_0+Aq,
   \qquad A\in\mathcal L_G(F,K).
   }
   \tag{8}
   \]

   Consequently the symmetry-constrained ambiguity is not the full `\mathcal L(F,K)` torsor of AF-078 but exactly its intertwiner subspace.

3. **Endpoint-fixed equivariant symmetries are the same intertwiners.** Every `A\in\mathcal L_G(F,K)` defines

   \[
   g_A=I_E+iAq,
   \tag{9}
   \]

   a bounded `G`-equivariant automorphism of the exact sequence satisfying

   \[
   g_A i=i,
   \qquad
   qg_A=q,
   \qquad
   g_A^{-1}=I_E-iAq.
   \tag{10}
   \]

   Conversely every bounded `G`-equivariant automorphism of `E` that fixes `K` pointwise and induces the identity on `F` is uniquely of the form (9). The action on repairs is

   \[
   r_0g_A=r_0+Aq.
   \tag{11}
   \]

   Therefore, **conditional on existence**, the repair is unique from the endpoint-fixed `G`-sequence data exactly when

   \[
   \boxed{
   \mathcal L_G(F,K)=\{0\}.
   }
   \tag{12}
   \]

   This gives an exact version of the vague statement that “symmetry may choose a complement”: it does so precisely when the declared symmetry leaves no nonzero retained-to-lost intertwiner.

4. **Compact symmetry removes no existing split but may remove all noncanonical choices.** Assume now that `G` is compact, the action `g\mapsto u_g` is strongly continuous, and

   \[
   M=\sup_{g\in G}\|u_g\|<\infty.
   \tag{13}
   \]

   Because inversion permutes `G`, the same `M` bounds `\|u_g^{-1}\|`. If `P:E\to E` is any bounded projection onto `K`, normalized Haar averaging gives

   \[
   P_G
   =
   \int_G u_g P u_g^{-1}\,d\mu(g),
   \tag{14}
   \]

   which is a bounded `G`-equivariant projection onto `K` and satisfies

   \[
   \|P_G\|\le M^2\|P\|.
   \tag{15}
   \]

   Hence for compact `G`, ordinary complementedness of `K` already implies `G`-complementedness. If the action on `E` is isometric, define

   \[
   \lambda_G(K,E)
   =
   \inf\{\|P\|:P^2=P,\ \operatorname{Ran}P=K,\ P u_g=u_gP\ \forall g\}.
   \tag{16}
   \]

   Then

   \[
   \boxed{
   \lambda_G(K,E)=\lambda(K,E).
   }
   \tag{17}
   \]

   Compact isometric averaging therefore imposes **no extra projection-norm cost**. Its effect is categorical: it restricts admissible repairs to the equivariant torsor (8), which may collapse to one point when (12) holds.

5. **Outside that favorable regime, symmetry can destroy repairability even when the bare Banach sequence splits.** Castillo and Ferenczi give the exact `2^{<\omega}`-space sequence

   \[
   0\longrightarrow c_0\longrightarrow c\longrightarrow\mathbb R\longrightarrow0,
   \tag{18}
   \]

   where `2^{<\omega}` acts diagonally on `c` and `c_0` and trivially on the quotient. The sequence splits as Banach spaces but has no `2^{<\omega}`-equivariant lifting `\mathbb R\to c`, hence does not `2^{<\omega}`-split. Thus an ordinary repair can exist while **every symmetry-respecting repair is forbidden**.

The reusable Arithmetic Fidelity rule is therefore

\[
\boxed{
\begin{array}{c}
\text{extra symmetry changes quotient repair through two independent invariants:}\\
\text{the equivariant extension class controls whether a repair exists;}\\
\mathcal L_G(F,K)\text{ controls how many symmetry-compatible repairs remain;}\\
\text{canonicity requires both `G`-splitting and }\mathcal L_G(F,K)=0.
\end{array}}
\tag{19}
\]

This refines AF-078's two-gate existence/canonicity audit into a category-indexed theorem. “Add symmetry” is not itself a solution: the symmetry must simultaneously permit an equivariant split and eliminate the intertwiners that shear one admissible repair into another.

## Derivation

### Equivariant repair is the same as an invariant projection

Suppose `r` satisfies (5) and put

\[
P=i r:E\to E.
\tag{20}
\]

As in AF-078, `P^2=P` and `\operatorname{Ran}P=K`. Equivariance gives

\[
P u_g
=i r u_g
=i w_g r
=u_g i r
=u_gP.
\tag{21}
\]

Thus `P` is a `G`-equivariant projection and

\[
E=K\oplus\ker P
\tag{22}
\]

with `\ker P` `G`-invariant. Conversely a bounded `G`-equivariant projection onto `K` gives a repair by viewing its range in `K`.

If `N\subset E` is a bounded `G`-invariant complement of `K`, then

\[
q|_N:N\to F
\tag{23}
\]

is a bounded bijection. Its inverse

\[
s=(q|_N)^{-1}:F\to N\subset E
\tag{24}
\]

is bounded by the open mapping theorem. Because `N` is invariant and `q` intertwines the actions,

\[
s v_g=u_g s.
\tag{25}
\]

So `s` is a `G`-equivariant section. Conversely, a `G`-equivariant section `s` gives

\[
P=I_E-sq,
\tag{26}
\]

a `G`-equivariant projection onto `K`. This proves (6). It is the repair-language specialization of the standard `G`-splitting equivalences for exact sequences of `G`-Banach spaces.

### The equivariant repair fiber is exactly an intertwiner torsor

Let `r` and `r_0` be two `G`-equivariant repairs. Their difference vanishes on `K`, so the Banach quotient universal property gives a unique bounded

\[
A:F\to K
\tag{27}
\]

with

\[
r-r_0=Aq.
\tag{28}
\]

For every `g`, equivariance of `r-r_0` gives

\[
Aq u_g=w_gAq.
\tag{29}
\]

Using `qu_g=v_gq` and surjectivity of `q`,

\[
A v_g=w_g A.
\tag{30}
\]

Hence `A\in\mathcal L_G(F,K)`. Conversely, if `A` satisfies (30), then `r_0+Aq` still fixes `K` and is `G`-equivariant. This proves (8).

The same computation classifies endpoint-fixed `G`-automorphisms. If `h:E\to E` is bounded, `G`-equivariant, `h|_K=I_K`, and `qh=q`, then `(h-I_E)(E)\subset K` and `(h-I_E)|_K=0`. Therefore there is a unique `A:F\to K` with

\[
h-I_E=iAq.
\tag{31}
\]

Equivariance forces `A` to satisfy (30). Conversely (9) is invertible because

\[
(iAq)^2=iA(qi)Aq=0.
\tag{32}
\]

Thus endpoint-fixed equivariant automorphisms are exactly the shears generated by `\mathcal L_G(F,K)`, and (11) proves simple transitivity on the repair set. Equation (12) follows immediately.

### Compact averaging preserves the projection while enforcing symmetry

Assume `G` compact and strongly continuously represented on `E`. For each fixed `x\in E`, the map

\[
g\mapsto u_g P u_g^{-1}x
\tag{33}
\]

is continuous, so the Bochner integral (14) is defined. Since `K` is invariant, each conjugate `u_gPu_g^{-1}` has range `K` and fixes `K` pointwise. The same is therefore true of their average:

\[
P_G(E)\subseteq K,
\qquad
P_G|_K=I_K.
\tag{34}
\]

Hence `P_G^2=P_G` and `\operatorname{Ran}P_G=K`.

For `h\in G`, invariance of normalized Haar measure gives

\[
\begin{aligned}
u_hP_Gu_h^{-1}
&=
\int_G u_{hg}Pu_{hg}^{-1}\,d\mu(g)\\
&=P_G,
\end{aligned}
\tag{35}
\]

so `P_G` is equivariant. The norm estimate is

\[
\|P_G\|
\le
\int_G\|u_g\|\,\|P\|\,\|u_g^{-1}\|\,d\mu(g)
\le
M^2\|P\|,
\tag{36}
\]

proving (15).

If all `u_g` are isometries, then `\|P_G\|\le\|P\|`. Since every equivariant projection is in particular an ordinary projection,

\[
\lambda(K,E)\le\lambda_G(K,E).
\tag{37}
\]

Averaging arbitrary projections and taking infima gives the reverse inequality, proving (17).

## Exact controls

### A two-sign action converts an affine repair family into one canonical point

Take

\[
E=\mathbb R\oplus\mathbb R,
\qquad
K=\mathbb R\oplus\{0\},
\qquad
q(k,f)=f,
\tag{38}
\]

and let `G=\mathbb Z/2\mathbb Z` act by

\[
u(k,f)=(k,-f).
\tag{39}
\]

The induced action on `K` is trivial and on `F` is sign change. Every ordinary repair has the AF-078 form

\[
r_a(k,f)=k+af,
\qquad a\in\mathbb R.
\tag{40}
\]

Equivariance requires

\[
r_a(k,-f)=r_a(k,f),
\tag{41}
\]

hence `a=0`. Equivalently `\mathcal L_G(F,K)=0`. The bare split exact sequence has infinitely many repairs, while the declared symmetry forces exactly one.

This is the clean positive control for (12): symmetry can genuinely remove noncanonicity without adding a hidden copy of the discarded coordinate.

### Trivial symmetry does nothing

If `G` acts trivially on `K`, `E`, and `F`, then

\[
\mathcal L_G(F,K)=\mathcal L(F,K).
\tag{42}
\]

Equivariant repair is then identical to ordinary repair, so AF-078's full shear ambiguity survives. Merely naming a symmetry group has no effect unless its representations actually restrict the admissible intertwiners.

### Symmetry may eliminate all repairs rather than select one

For the `2^{<\omega}` action in (18), the ordinary complement of `c_0` in `c` is the constant-sequence direction. It is not invariant under the diagonal sign action. Castillo and Ferenczi prove that no alternative equivariant lifting exists. Thus the symmetry-constrained repair set is empty even though the unconstrained repair set is nonempty.

This separates two logically independent outcomes:

\[
\mathcal L_G(F,K)=0
\quad\text{does not help if the extension does not `G`-split,}
\tag{43}
\]

while `G`-splitting alone does not yield uniqueness when `\mathcal L_G(F,K)\ne0`.

## Application to AF-077's canonical provenance quotient

Suppose AF-077's relatively compact witness family `A\subset V` is stable under a compact group `G` of linear isometries of `V`. Then

\[
D_V(A)=\overline{\operatorname{aconv}}(A)
\tag{44}
\]

is `G`-stable, so the induced action on its canonical Banach space `E_A` is isometric for the Minkowski norm. If a bounded linear downstream map

\[
B:V\to W
\tag{45}
\]

intertwines this action with an isometric `G`-action on `W`, then AF-077's quotient

\[
\widetilde B:E_A\twoheadrightarrow E_{B(A)}
\tag{46}
\]

is a `G`-equivariant Banach quotient. Put

\[
K_B=\ker\widetilde B.
\tag{47}
\]

AF-079 sharpens AF-078's next gate in this symmetric setting:

\[
\boxed{
\begin{array}{c}
K_B\text{ complemented in }E_A
\Longleftrightarrow
K_B\text{ `G`-complemented in }E_A;\\
\text{the optimal projection norm is unchanged by imposing compact isometric symmetry;}\\
\text{a unique symmetry-compatible full-provenance repair exists exactly when additionally}\\
\mathcal L_G(E_{B(A)},K_B)=0.
\end{array}}
\tag{48}
\]

Thus a concrete Mathia proposal that says “the natural symmetry should restore the lost transverse/boundary/provenance coordinate” has two exact obligations. It must prove equivariant splitting, and it must compute the retained-to-lost intertwiner space. Only the simultaneous result

\[
\text{`G`-split}
\quad+\quad
\mathcal L_G(F,K)=0
\tag{49}
\]

supports a claim that the symmetry forces one bounded linear repair.

Even then, AF-079 establishes only **canonicity of the full-kernel coordinate in the declared symmetry category**. It does not show that the repaired directions carry the discriminator of interest, that full-kernel recovery is minimal for that discriminator, or that the chosen symmetry is itself forced by the original arithmetic/geometric construction.

## Prior art and novelty assessment

The equivariant splitting mechanism is classical.

- Jesús M. F. Castillo and Valentin Ferenczi, **“Group Actions on Twisted Sums of Banach Spaces,”** *Bulletin of the Malaysian Mathematical Sciences Society* 46, article 135 (2023), DOI `10.1007/s40840-023-01531-0`. Proposition 10.6 gives the equivalence between `G`-splitting, a continuous linear `G`-lifting of the quotient, a `G`-invariant complement, and `G`-complementation. Theorem 10.7 identifies an amenable-group / `G`-ultrasummand regime in which ordinary splitting implies `G`-splitting. Section 11.3 supplies the split-as-Banach-but-not-`2^{<\omega}`-split sequence (18), providing a direct matched control for the stronger equivariant existence gate.
- Compact-group averaging with normalized Haar measure is the standard averaging mechanism behind invariant projections and finite/compact-group representation theory. AF-079 derives the projection formula and norm estimates directly rather than claiming them as new results.

No novelty is claimed for `G`-Banach exact sequences, equivariant splitting, invariant complements, Haar averaging, or the ordinary homological interpretation of extension classes. The affine description of splittings is also standard homological algebra.

The durable Arithmetic Fidelity contribution is the **paired category-indexed audit** obtained by combining that classical existence theory with AF-078's repair-fiber viewpoint. Once admissible repairs must respect a declared symmetry, the extension class and the intertwiner space play different roles: equivariant `Ext`-type data decide whether any repair exists, while `\mathcal L_G(F,K)` is exactly the residual shear freedom after existence. This converts “symmetry might make the lost coordinate canonical” into two falsifiable computations and provides the compact-isometric control (17), where canonicity may improve without paying an additional projection-stability cost.

## Boundaries and failure modes

- `G`-equivariant uniqueness is category-relative. A different or weaker declared symmetry can enlarge `\mathcal L_G(F,K)` and restore ambiguity; a stronger symmetry can make the extension fail to split.
- Equation (12) is conditional on existence. Vanishing intertwiners cannot manufacture a repair of a nontrivial equivariant extension.
- Compact averaging uses the compactness/continuity hypotheses stated above. Amenability alone requires additional hypotheses in the general Banach setting; the `2^{<\omega}` example prevents silently extending (14)--(17) to arbitrary amenable actions.
- A unique full-kernel repair is still an upper bound on discriminator recovery, not a minimal lift for a particular target property.
- Symmetry must be intrinsic to the source construction. Adding an externally chosen group solely because it kills `\mathcal L_G(F,K)` would simply move the arbitrary choice into the category declaration.
- The projection constant controls stability of full-kernel reconstruction, not sensitivity of a specific arithmetic discriminator inside the kernel.
- AF-077's compact-isometric corollary requires `A` itself to be `G`-stable and the downstream map to intertwine the declared actions. Symmetry of an ambient formula that does not descend to the canonical witness family is not enough.

## Consequence for the line

For quotient-type compression with a proposed symmetry, replace the informal claim “symmetry selects the missing information” by a two-stage calculation:

1. determine whether the exact sequence splits in the **symmetry-respecting category**; and
2. if it does, compute the intertwiner space from retained data to lost data.

A symmetry is a genuine canonicity mechanism only when the first calculation leaves at least one repair and the second leaves exactly one. Compact isometric symmetry is especially diagnostic because ordinary splitting already guarantees equivariant splitting with the same optimal projection cost, so any remaining ambiguity is isolated cleanly in `\mathcal L_G(F,K)`.

This gives the next reusable template for Arithmetic Fidelity: extra structure should be audited not by whether it produces a plausible coordinate, but by the exact category it declares, the extension obstruction inside that category, and the automorphisms/intertwiners that remain after the declaration.