# AF-078 — Linear quotient repair has separate splitting and naturality gates

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-BOUNDARY`

## Claim

Let

\[
0\longrightarrow K\xrightarrow{i}E\xrightarrow{q}F\longrightarrow0
\tag{1}
\]

be a short exact sequence of real or complex Banach spaces and bounded linear maps, where `i` is an isomorphic embedding onto the closed subspace `i(K)=\ker q` and `q` is the corresponding quotient map. Identifying `K` with `i(K)\subseteq E`, call a bounded linear map

\[
r:E\to K
\tag{2}
\]

an **exact kernel repair** when

\[
r|_K=I_K.
\tag{3}
\]

Thus the retained quotient `q(x)` is augmented not by an arbitrary target-dependent mark but by a coordinate valued in the subspace that the quotient itself discards.

Then:

1. **Existence of a bounded linear kernel repair is exactly split exactness.** The following are equivalent:

   \[
   \boxed{
   \begin{array}{c}
   \exists\text{ bounded }r:E\to K\text{ with }r|_K=I_K;\\
   K\text{ is complemented in }E;\\
   q\text{ admits a bounded linear section }s:F\to E;\\
   (1)\text{ splits in the Banach-space category.}
   \end{array}}
   \tag{4}
   \]

   Whenever these conditions hold, the augmented observation

   \[
   \Psi_r:E\to F\oplus_1 K,
   \qquad
   \Psi_r(x)=(q x,r x),
   \tag{5}
   \]

   is a Banach-space isomorphism. Hence a quotient can be repaired by a bounded linear coordinate on its lost directions **if and only if its extension class is trivial**.

2. **The repair cost is the projection constant of the lost kernel.** Define

   \[
   \lambda(K,E)
   =
   \inf\{\|P\|:P:E\to E,\ P^2=P,\ \operatorname{Ran}P=K\},
   \tag{6}
   \]

   with value `+\infty` when no such projection exists. Kernel repairs `r` correspond exactly to projections `P=i\circ r`, so

   \[
   \boxed{
   \inf_r\|r\|=\lambda(K,E).
   }
   \tag{7}
   \]

   If `r` is a repair and `P=i\circ r`, the associated section `s=(q|_{\ker P})^{-1}` satisfies

   \[
   \|s\|\le \|I-P\|\le 1+\|P\|.
   \tag{8}
   \]

   Consequently, with the `\ell^1` product norm on `F\oplus K`,

   \[
   \|\Psi_r\|\le1+\|r\|,
   \qquad
   \|\Psi_r^{-1}\|\le1+\|r\|.
   \tag{9}
   \]

   Split exactness therefore has a quantitative stability cost even before any discriminator-specific condition is imposed.

3. **Existence does not imply canonicity.** Suppose one repair `r_0` exists. Every other bounded linear repair has the unique form

   \[
   \boxed{
   r_A=r_0+Aq,
   \qquad A\in\mathcal L(F,K).
   }
   \tag{10}
   \]

   Thus the repair set is an affine space, or torsor, over `\mathcal L(F,K)`.

   More strongly, for every `A\in\mathcal L(F,K)` the shear

   \[
   g_A=I_E+iAq
   \tag{11}
   \]

   is a bounded automorphism of `E` with

   \[
   g_A i=i,
   \qquad
   qg_A=q,
   \qquad
   g_A^{-1}=I_E-iAq.
   \tag{12}
   \]

   It preserves both the embedded lost kernel and the retained quotient **exactly**, while

   \[
   r_0g_A=r_0+Aq.
   \tag{13}
   \]

   Hence the shear automorphisms act simply transitively on all repairs.

4. **No nontrivial repair is canonical from the exact-sequence data alone.** Formalize “canonical from `(K,E,F,i,q)` alone” by requiring invariance under every automorphism `g` of the exact sequence that fixes `K` pointwise and induces the identity on `F`:

   \[
   gi=i,
   \qquad qg=q,
   \qquad rg=r.
   \tag{14}
   \]

   If both `K\ne0` and `F\ne0`, then

   \[
   \boxed{
   \text{no bounded linear kernel repair can satisfy (14).}
   }
   \tag{15}
   \]

   Indeed `\mathcal L(F,K)` contains a nonzero rank-one operator, and (13) would force `Aq=0`, hence `A=0`, for every `A`. Therefore **split exactness is only an existence gate**. A distinguished repair requires additional structure that reduces the admissible symmetry group: an inner product, order, grading, locality rule, boundary condition, equivariance constraint, source-derived basis/marking, or another independently justified choice.

5. **Finite-dimensional repairability does not assemble automatically.** Every finite-dimensional subspace `G\subseteq K` is complemented in `E` by Hahn–Banach, even when `K` itself is uncomplemented. Thus

   \[
   \boxed{
   \text{every finite-dimensional slice of the lost directions can admit a linear retraction while the full quotient has no bounded repair.}
   }
   \tag{16}
   \]

   This is an exact linear analogue of the cross-scale warning in AF-073--AF-077: separately solvable finite stages do not supply one coherent global carrier.

The reusable Arithmetic Fidelity conclusion is therefore

\[
\boxed{
\begin{array}{c}
\text{a target-independent linear repair of quotient loss first requires a split extension;}\\
\text{even a split extension supplies an affine family of repairs rather than a canonical one;}\\
\text{the exact-sequence symmetries themselves move every possible repair;}\\
\text{therefore intrinsic recovery needs extra structure both to make repair exist and to select it.}
\end{array}}
\tag{17}
\]

## Derivation

### A kernel repair is exactly a bounded projection

If `r:E\to K` satisfies `r|_K=I_K`, then

\[
P=i\circ r:E\to E
\tag{18}
\]

obeys

\[
P^2=i r i r=i r=P,
\qquad
\operatorname{Ran}P=K.
\tag{19}
\]

Conversely, every bounded projection `P:E\to E` with range `K` restricts to the identity on `K`; viewing its range in `K` gives a repair `r`. This proves equivalence of the first two statements in (4) and the norm identity in (7).

Let `P` be such a projection and put

\[
N=\ker P.
\tag{20}
\]

Every `x\in E` has the unique decomposition

\[
x=Px+(I-P)x\in K\oplus N.
\tag{21}
\]

The restriction

\[
q|_N:N\to F
\tag{22}
\]

is injective because `N\cap K=\{0\}`, and it is surjective because

\[
q((I-P)x)=qx.
\tag{23}
\]

It is therefore a bounded bijection between Banach spaces, so the open mapping theorem gives a bounded inverse

\[
s=(q|_N)^{-1}:F\to N\subseteq E,
\tag{24}
\]

with `qs=I_F`. Thus the sequence splits.

Conversely, if `s:F\to E` is a bounded section, then

\[
P=I_E-sq
\tag{25}
\]

has range in `K` because `qP=0`, fixes `K` because `q|_K=0`, and satisfies `P^2=P`. Hence a bounded section gives a kernel repair. This completes (4).

### The augmented quotient plus kernel coordinate reconstructs the whole source

Assume `r` exists and let `P=i\circ r`, `N=\ker P`, and `s` be (24). Since

\[
x=s(qx)+Px,
\tag{26}
\]

one has the explicit inverse

\[
\Psi_r^{-1}(y,k)=s(y)+i(k).
\tag{27}
\]

Thus `(q,r)` does not merely recover one discriminator: it reconstructs the complete Banach-space source. This is why AF-078 treats kernel repair as a **full-provenance upper bound**, not as a claim of minimality for a particular target discriminator.

For the quantitative estimate, fix `y\in F`. By the quotient norm, for every `\varepsilon>0` choose `x\in E` with

\[
qx=y,
\qquad
\|x\|\le\|y\|+\varepsilon.
\tag{28}
\]

The unique element of `N` mapping to `y` is `(I-P)x`, so

\[
\|sy\|
\le
\|I-P\|(\|y\|+\varepsilon).
\tag{29}
\]

Letting `\varepsilon\downarrow0` yields the first inequality in (8). The remaining norm estimates follow from

\[
\|qx\|+\|rx\|
\le
(1+\|r\|)\|x\|
\tag{30}
\]

and (27).

### Repairs form a torsor over operators from retained to lost data

Let `r` and `r_0` be two repairs. Their difference vanishes on `K`:

\[
(r-r_0)|_K=0.
\tag{31}
\]

By the universal property of the Banach quotient there is a unique bounded

\[
A:F\to K
\tag{32}
\]

such that

\[
r-r_0=Aq.
\tag{33}
\]

Conversely `r_0+Aq` still restricts to `I_K`, proving (10).

For each bounded `A`, the operator `iAq` squares to zero because `qi=0`. Therefore

\[
(I_E+iAq)(I_E-iAq)=I_E,
\tag{34}
\]

which proves that `g_A` is an automorphism and establishes (12). Finally

\[
r_0g_A
=r_0+r_0iAq
=r_0+Aq,
\tag{35}
\]

because `r_0i=I_K`. Equations (33) and (35) show that the shear group moves one repair to every other repair, uniquely.

### Full extension symmetry forbids a canonical repair

Assume `K` and `F` are both nonzero. Choose `0\ne k\in K`, `0\ne f\in F`, and by Hahn–Banach choose `\phi\in F^*` with `\phi(f)\ne0`. Then

\[
A(y)=\phi(y)k
\tag{36}
\]

is a nonzero bounded operator `F\to K`.

If a repair `r` were invariant under all exact-sequence automorphisms fixing the endpoints, it would in particular satisfy

\[
rg_A=r.
\tag{37}
\]

But (13) gives

\[
Aq=0.
\tag{38}
\]

Surjectivity of `q` forces `A=0`, contradiction. Thus the exact sequence itself never distinguishes one repair from its shear translates in the nontrivial case.

This is stronger than saying that complements are “usually nonunique.” It identifies the precise symmetry that generates the ambiguity while leaving the compressed quotient and its lost kernel unchanged.

## Exact controls

### Hilbert structure passes the existence gate by adding geometry

If `E` is Hilbert and `K\subseteq E` is closed, orthogonal projection

\[
P_K:E\to K
\tag{39}
\]

has norm `1` and supplies a repair. The quotient can be identified with `K^\perp`, so the exact sequence splits stably.

This does **not** contradict (15). Orthogonal projection is distinguished only after the inner product has been declared part of the structure. The shears `I+iAq` are generally not unitary and therefore are no longer admissible symmetries in the metric category. The example isolates exactly what the extra geometry buys: not new raw dimensions, but a rule selecting one complement from the affine family.

### The Kalton–Peck space fails the existence gate despite Hilbert endpoints

Kalton and Peck constructed the twisted Hilbert space `Z_2` fitting into a short exact sequence

\[
0\longrightarrow\ell^2
\longrightarrow Z_2
\longrightarrow\ell^2
\longrightarrow0
\tag{40}
\]

that does **not** split. Therefore the embedded copy of `\ell^2` is not complemented in `Z_2`, and no bounded linear kernel repair exists for the quotient in (40).

This is a sharp matched control against endpoint-only reasoning: both the lost kernel and the retained quotient are Hilbert spaces, yet the middle-space extension class prevents linear reconstruction. Knowing the categories of the two endpoints is insufficient; how they are glued is itself retained mathematical information.

At the same time every finite-dimensional subspace `G` of the embedded `\ell^2` is complemented in `Z_2`, as every finite-dimensional subspace of a Banach space is. Thus all finite-dimensional kernel slices pass an existence test while the complete infinite-dimensional kernel fails it. No collection of unrelated finite-stage projections is evidence of one bounded global repair.

### A split direct sum passes existence but still fails exact-sequence canonicity

Take nonzero Banach spaces `K,F` and

\[
E=K\oplus F,
\qquad
q(k,f)=f.
\tag{41}
\]

The obvious repair `r_0(k,f)=k` exists. For every bounded `A:F\to K`, however,

\[
r_A(k,f)=k+A f
\tag{42}
\]

is another repair, and the shear

\[
g_A(k,f)=(k+A f,f)
\tag{43}
\]

fixes the kernel pointwise and quotient exactly. Therefore even the most transparent split quotient contains no preferred kernel coordinate in the bare exact-sequence category.

This control separates two questions that are easy to conflate:

\[
\text{Can the loss be repaired linearly?}
\qquad\ne\qquad
\text{Does the declared mathematics force a particular repair?}
\tag{44}
\]

## Application to AF-077's canonical compact provenance space

AF-077 showed that for a relatively compact witness family `A\subset V`, its canonical disk produces a Banach space `E_A` compactly embedded in `V`, and every bounded linear downstream map `B:V\to W` induces a surjective contraction

\[
\widetilde B:E_A\to E_{B(A)}
\tag{45}
\]

with

\[
E_{B(A)}\cong E_A/\ker\widetilde B
\tag{46}
\]

isometrically. Put

\[
K_B=\ker\widetilde B.
\tag{47}
\]

AF-078 therefore supplies an exact next gate:

\[
\boxed{
\begin{array}{c}
\text{a bounded linear coordinate that restores all canonical provenance lost by }\widetilde B\\
\text{exists iff }K_B\text{ is complemented in }E_A;\\
\text{even then, the quotient data alone cannot canonically choose that coordinate when}\\
K_B\ne0\text{ and }E_{B(A)}\ne0.
\end{array}}
\tag{48}
\]

This makes AF-077's final caveat precise. Canonicalizing the pooled witness envelope does not canonicalize a repair after downstream quotienting. A viable mathematical mechanism must derive extra structure that either forces a split and selects a complement or avoids losing the discriminator into the quotient kernel in the first place.

## Prior art and novelty assessment

The functional-analytic and homological mechanisms are classical.

- Félix Cabello Sánchez and Jesús M. F. Castillo, ***Homological Methods in Banach Space Theory***, Cambridge Studies in Advanced Mathematics 203, Cambridge University Press (2023), DOI `10.1017/9781108778312`, especially Chapter 1, **“Complemented Subspaces of Banach Spaces,”** DOI `10.1017/9781108778312.003`, and Chapter 2, **“The Language of Homology,”** DOI `10.1017/9781108778312.004`. Role: modern authoritative treatment of complemented subspaces, projections, Banach-space exact sequences, splitting, extension/lifting language, and the homological interpretation of uncomplemented kernels.
- N. J. Kalton and N. T. Peck, **“Twisted Sums of Sequence Spaces and the Three Space Problem,”** *Transactions of the American Mathematical Society* 255 (1979), 1–30, DOI `10.2307/1998164`. Role: primary twisted-sum source and origin of the Kalton–Peck construction underlying the non-split `\ell^2`--`Z_2`--`\ell^2` control.
- Félix Cabello Sánchez, **“Twisted Hilbert spaces,”** *Bulletin of the Australian Mathematical Society* 59(2) (1999), 177–180, DOI `10.1017/S0004972700032792`. Role: explicit modern statement that `Z_2` contains an isometric `\ell^2` with isometric `\ell^2` quotient and that Kalton--Peck proved the corresponding exact sequence does not split.

No novelty is claimed for complementedness, projection constants, splitting of short exact sequences, twisted sums, `Ext`, the affine structure of splittings, or the Kalton–Peck example. The shear calculation is elementary homological algebra in Banach-space clothing.

The durable Arithmetic Fidelity contribution is the **two-gate interpretation forced by AF-001 and AF-077**. AF-001 ruled out arbitrary marks because they can simply store the answer. AF-077 turned a source-derived compact provenance carrier under linear post-processing into an exact Banach quotient. AF-078 identifies what happens when the admissible repair is restricted to a target-independent bounded linear coordinate on the actual lost kernel: nontrivial extension class blocks existence, while extension automorphisms block canonicity even after existence is secured. These are different obstructions and must not be collapsed into one generic statement that “extra information is needed.”

## Boundaries and failure modes

- A kernel repair restores the **entire lost Banach coordinate**, not the smallest information needed for one discriminator. It is therefore a target-independent full-provenance upper bound, not a minimal-lift theorem for a specific `d`.
- The canonicity no-go uses invariance under the full automorphism group of the bare exact sequence fixing kernel and quotient. A richer category may legitimately admit fewer symmetries and thereby select a repair; the Hilbert control shows precisely this possibility.
- Split exactness is category-dependent. A sequence may split algebraically but not by a bounded linear section, so the topology/norm cannot be dropped from a stable-fidelity claim.
- Small finite-dimensional repairs do not imply a global repair. To promote finite-stage complements, one needs a coherent and quantitatively controlled assembly theorem rather than mere existence at every cutoff.
- Complementability of `K_B` in AF-077's `E_A` says that all lost canonical provenance can be coordinatized linearly. It does not show that a prime-specific or RH-relevant discriminator occupies those directions, nor that the chosen projection is intrinsic to the arithmetic construction.
- If either `K=0` or `F=0`, the shear obstruction degenerates. Those cases are correctly trivial: there is respectively nothing lost or nothing retained.

## Consequence for the line

For linear quotient-type compressions, replace the vague question “what extra mark restores the lost information?” by two independent audits.

First compute the exact kernel and ask whether the associated Banach extension splits. Failure is a hard no-go for every bounded linear full-kernel repair. Second, if it splits, identify what **additional mathematical structure** chooses a complement despite the shear symmetry. A proposed projection, boundary coordinate, transverse mode, or marked channel is not intrinsic merely because it exists; it must be forced by structure that is absent from the bare quotient sequence.

For growing-resolution constructions, finite-dimensional complementability should be treated as a weak control only. The global object must supply one coherent bounded split or an alternative mechanism that proves the relevant discriminator never enters the lost kernel.