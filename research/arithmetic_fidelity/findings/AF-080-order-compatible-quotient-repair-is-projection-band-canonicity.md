# AF-080 — Order-compatible quotient repair is canonical exactly for projection bands

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `E` be a real Banach lattice, let `K\subseteq E` be a closed linear subspace, and let

\[
0\longrightarrow K\xrightarrow{i}E\xrightarrow{q}E/K\longrightarrow0
\tag{1}
\]

be the normalized quotient sequence. As in AF-078, a bounded linear map

\[
r:E\to K,
\qquad r|_K=I_K,
\tag{2}
\]

is a full-kernel repair, with associated projection

\[
P=i\circ r:E\to E,
\qquad P^2=P,
\qquad \operatorname{Ran}P=K.
\tag{3}
\]

Call the repair **order-compatible** when both the recovered part and the retained complementary part preserve the positive cone:

\[
P\ge0,
\qquad I_E-P\ge0,
\tag{4}
\]

or equivalently

\[
0\le P\le I_E.
\tag{5}
\]

Then:

1. **Order-compatible repair exists exactly for projection bands.** There is an order-compatible repair onto `K` if and only if `K` is a projection band of `E`, equivalently

   \[
   \boxed{
   E=K\oplus K^d,
   }
   \tag{6}
   \]

   where

   \[
   K^d=\{x\in E:|x|\wedge |k|=0\text{ for every }k\in K\}
   \tag{7}
   \]

   is the disjoint complement. In that case the associated projection is the classical band projection `P_K`.

2. **Existence already implies canonicity in the declared order category.** For a fixed projection band `K`, the order-compatible repair is unique:

   \[
   \boxed{
   P=P_K,
   \qquad
   \ker P=K^d.
   }
   \tag{8}
   \]

   Thus the affine shear family from AF-078 collapses to one point after imposing the two-sided order condition (4). If `K\ne\{0\}`, then

   \[
   \boxed{\|P_K\|=\|r\|=1.}
   \tag{9}
   \]

   So this particular canonicity mechanism carries no projection-norm instability.

3. **Positivity of the recovered coordinate alone is not enough.** Requiring only

   \[
   P\ge0
   \tag{10}
   \]

   can leave a nontrivial family of repairs. On `E=\mathbb R^2` with coordinate order and `K=\mathbb R\times\{0\}`, every

   \[
   P_a(x,y)=(x+a y,0),
   \qquad a\ge0,
   \tag{11}
   \]

   is a positive projection onto the same `K`. But

   \[
   (I-P_a)(x,y)=(-a y,y),
   \tag{12}
   \]

   is positive for all `(x,y)\ge0` only when `a=0`. Hence

   \[
   \boxed{
   P\ge0\text{ does not select a repair, whereas }0\le P\le I\text{ does.}
   }
   \tag{13}
   \]

   This separates generic positivity from the much stronger requirement that the decomposition itself respect order on both sides.

4. **Order completeness supplies an exact existence regime.** In a Dedekind-complete Riesz space every band is a projection band. Consequently, in a Dedekind-complete Banach lattice every band `K` has a unique order-compatible full-kernel repair. For the classical support bands in

   \[
   E=L^p(\Omega,\mu),
   \qquad 1\le p<\infty,
   \tag{14}
   \]

   a measurable set `A` gives

   \[
   K_A=\{f:f=0\text{ a.e. on }\Omega\setminus A\},
   \qquad
   P_A f=\mathbf1_A f.
   \tag{15}
   \]

   This is the canonical order-compatible recovery of the discarded support component.

5. **Order structure does not manufacture a repair when the required projection band is absent.** If `X` is compact, connected, and Hausdorff, the Banach lattice `C(X)` has no nontrivial band projections. Therefore no nonzero proper subspace can be recovered by an order-compatible projection merely because the ambient space is ordered. The order category imposes a real existence obstruction rather than supplying a universal canonicalizer.

6. **Nested order-compatible repairs compose canonically.** If `B\subseteq C` are projection bands with band projections `P_B,P_C`, then

   \[
   \boxed{
   P_BP_C=P_CP_B=P_B,
   \qquad
   P_B\le P_C.
   }
   \tag{16}
   \]

   Thus nested order-defined losses have path-independent canonical repair. This is a genuine composition law: the smaller lost band can be recovered either directly or after projecting to the larger lost band, with exactly the same result.

7. **Compatible lattice symmetry cannot move the order-canonical repair.** If a group `G` acts on `E` by Banach-lattice automorphisms and preserves a projection band `K`, then

   \[
   u_gP_Ku_g^{-1}=P_K
   \qquad(g\in G).
   \tag{17}
   \]

   Hence `P_K` is automatically `G`-equivariant. This does not imply that AF-079's full space of `G`-equivariant linear repairs is a singleton; it says that after the order condition is also declared, the unique admissible repair cannot be moved by any order-preserving symmetry of the same data.

The reusable Arithmetic Fidelity conclusion is therefore

\[
\boxed{
\begin{array}{c}
\text{order can genuinely turn quotient loss into a canonical repair, but only in a specific category;}\\
\text{the lost subspace must be a projection band, and the decisive condition is }0\le P\le I;\\
\text{mere positivity }P\ge0\text{ leaves shear freedom and is not a canonicity principle.}
\end{array}}
\tag{18}
\]

## Derivation

### AF-078 reduces the question to a constrained projection

Every repair `r` in (2) gives the projection `P=i r` in (3), and every bounded projection onto `K` gives a repair by viewing its range as `K`. Therefore the additional order requirement is entirely a question about which projections satisfy (5).

The classical vector-lattice theorem is exact:

\[
\boxed{
P\text{ is a band projection}
\quad\Longleftrightarrow\quad
P^2=P\text{ and }0\le P\le I_E.
}
\tag{19}
\]

If (5) holds, (19) says that `K=\operatorname{Ran}P` is a projection band and that the complementary range is its disjoint complement. Conversely, if `K` is a projection band, the decomposition (6) defines its band projection `P_K`, and (19) gives `0\le P_K\le I`.

This proves the existence equivalence in (6).

### The disjoint complement removes the AF-078 torsor

For a projection band one has a direct sum

\[
E=K\oplus K^d.
\tag{20}
\]

The decomposition is intrinsic to the lattice disjointness relation. Hence the projection onto `K` along `K^d` is unique. Any order-compatible projection onto `K` is a band projection by (19), so its kernel must be `K^d`; therefore it equals `P_K`.

Compare this with AF-078. Once one unconstrained repair `r_0` exists, all repairs are

\[
r_A=r_0+Aq,
\qquad A\in\mathcal L(E/K,K).
\tag{21}
\]

For a projection band, (5) cuts this entire affine family down to the unique element whose complementary range is the disjoint complement. The extra order structure is doing real work: it supplies a distinguished complement rather than merely decorating an already chosen one.

For the norm statement, positivity gives the standard inequality

\[
|P_Kx|\le P_K|x|\le |x|.
\tag{22}
\]

The lattice norm is monotone, so

\[
\|P_Kx\|\le\|x\|.
\tag{23}
\]

Thus `\|P_K\|\le1`. If `K\ne0`, choose nonzero `k\in K`; since `P_Kk=k`, every projection norm is at least one, proving (9).

### One-sided positivity leaves a shear cone

For (11), direct calculation gives

\[
P_a^2=P_a,
\qquad
\operatorname{Ran}P_a=K.
\tag{24}
\]

If `(x,y)\ge0`, then `x+a y\ge0` for every such pair exactly when `a\ge0`, so `P_a\ge0` for all `a\ge0`. The complementary projection is (12). For `y>0`, its first coordinate is nonnegative only if `a\le0`. Therefore both projections are positive exactly at `a=0`.

This is a minimal matched control against an overly weak positivity proposal. The cone condition on the recovered coordinate alone can preserve an entire one-parameter slice of AF-078's shear ambiguity. Canonicity appears only when positivity constrains both the recovered and residual components.

### Dedekind completeness closes the band existence gate

A classical theorem of Riesz-space theory states that every band in a Dedekind-complete Riesz space is a projection band. Combined with (19), every such band admits the unique order projection characterized above.

The support-band example (15) makes the geometry literal. `P_A` and `I-P_A=P_{\Omega\setminus A}` are both positive, the two ranges are disjoint, and

\[
f=\mathbf1_Af+\mathbf1_{\Omega\setminus A}f
\tag{25}
\]

is the canonical decomposition. No choice of basis, section, metric complement, or target-dependent mark is required once the measurable support band is part of the declared structure.

The opposite regime is also classical. For connected compact `X`, `C(X)` has no nontrivial band projections. Thus the same order language does not guarantee existence in arbitrary Banach lattices. The projection-band hypothesis is the exact gate rather than a technical convenience.

### Projection bands carry their own composition law

For band projections the standard inclusion theorem gives

\[
B\subseteq C
\quad\Longleftrightarrow\quad
P_B\le P_C
\quad\Longleftrightarrow\quad
P_BP_C=P_CP_B=P_B.
\tag{26}
\]

Equation (16) follows immediately. In Arithmetic Fidelity terms, this means a nested family of order-defined discarded directions does not require separately chosen compatible sections at each stage. The lattice already forces coherence of the repair maps.

### Uniqueness forces equivariance under compatible lattice symmetries

Let `u:E\to E` be a Banach-lattice automorphism with `uK=K`. Because `u` and `u^{-1}` preserve order, conjugation preserves (5). Hence

\[
Q=uP_Ku^{-1}
\tag{27}
\]

is another order-compatible projection with range `K`. Uniqueness gives `Q=P_K`, proving (17).

This sharpens the comparison with AF-079. Symmetry alone has two separate gates: equivariant splitting and residual intertwiner freedom. Order-defined projection-band structure instead singles out one repair directly; any compatible lattice symmetry must respect that already-selected repair.

## Exact controls

### Positive but noncanonical: the coordinate shear family

The family (11) is the decisive control against replacing (5) by the superficially similar condition `P\ge0`. Every `P_a` for `a\ge0` preserves positivity of the recovered `K` coordinate, but all `a>0` contaminate that coordinate with retained `y` data. The positive cone alone does not prohibit this contamination.

The complementary-positivity requirement detects it immediately. `I-P_a` sends `(0,1)` to `(-a,1)`, which leaves the positive cone unless `a=0`. Thus the two-sided order condition is precisely what forbids importing retained information into the supposedly intrinsic lost coordinate.

### Canonical: measurable support bands in `L^p`

For `K_A` in (15), the projection `P_Af=\mathbf1_Af` is forced by disjoint support. Its complementary projection is multiplication by `\mathbf1_{\Omega\setminus A}`. If `A\subseteq B`, then

\[
P_AP_B=P_BP_A=P_A,
\tag{28}
\]

which realizes the abstract nested-band composition rule exactly.

### Existence failure: connected `C(X)`

Connected compact function spaces provide the opposite control. Their Banach-lattice order is rich, but there are no nontrivial band projections. Therefore an argument of the form “the source is ordered, so positivity should canonically restore the discarded component” is false without a projection-band theorem for the actual lost subspace.

## Prior art and novelty assessment

The underlying order theory is classical.

- Charalambos D. Aliprantis and Owen Burkinshaw, ***Positive Operators***, Springer (2006; originally Academic Press, 1985), DOI `10.1007/978-1-4020-5008-4`. The standard Riesz-space theory of bands, projection bands, order projections, and Dedekind completeness includes the fact that every band in a Dedekind-complete Riesz space is a projection band.
- Jonathan Mui, **“Spectral properties of locally eventually positive operator semigroups,”** *Semigroup Forum* 106 (2023), 460–480, DOI `10.1007/s00233-023-10347-0`, Section 3.1. Mui explicitly recalls the classical characterization that a projection is a band projection exactly when `0\le P\le I`, the nesting identity (26), support-band projections in `L^p`, and the absence of nontrivial band projections in `C(X)` for compact connected `X`.
- Jochen Glück, **“On Disjointness, Bands and Projections in Partially Ordered Vector Spaces,”** in *Positivity and its Applications*, Trends in Mathematics, Birkhäuser/Springer (2021), 141–171, DOI `10.1007/978-3-030-70974-7_7`. This supplies a modern structural account of bands and band projections and extends the classical language beyond vector lattices to pre-Riesz spaces.

No novelty is claimed for band projections, the equivalence (19), Dedekind-complete projection properties, support projections, or the Boolean/inclusion structure of projection bands.

The durable Arithmetic Fidelity contribution is the **repair-category separation** obtained by placing this classical theory after AF-078 and AF-079. “Add positivity” is too weak: positive repairs can retain shear ambiguity. The exact order-theoretic canonicity gate is instead `0\le P\le I`, and that gate is equivalent to the discarded kernel being a projection band. In that category, existence and canonicity collapse to one structural condition, stability is contractive, nested repairs compose coherently, and compatible lattice symmetries cannot move the selected repair.

## Boundaries and failure modes

- This is a full-kernel repair theorem, not a minimal-lift theorem for a particular discriminator. Recovering all of `K` can contain substantially more information than a target property needs.
- `P\ge0` alone is not enough; the exact characterization uses positivity of both `P` and `I-P`.
- The result is category-relative. A projection canonical in the Banach-lattice order category need not be canonical after the order structure is forgotten.
- The lost subspace must actually be a projection band in the declared lattice structure. An externally chosen lattice order introduced solely to force this property would move the arbitrary choice into the category declaration.
- Dedekind completeness guarantees projection-band status only for bands; it does not turn an arbitrary closed subspace into a band.
- Contractivity in (9) concerns full-kernel reconstruction. It does not by itself imply robustness of a particular arithmetic discriminator to perturbations upstream of the quotient.
- Automatic equivariance in (17) requires genuine lattice automorphisms preserving `K`. A merely bounded group action that does not preserve order falls back under AF-079's separate equivariant-splitting analysis.
- The nested composition law applies to projection bands. Arbitrary complemented subspaces retain AF-078's noncanonical complement choices and need not admit coherent projections.

## Consequence for the line

AF-078 showed that an unconstrained linear quotient repair has separate existence and canonicity problems. AF-079 showed that symmetry refines those into equivariant splitting plus an intertwiner-rigidity gate. AF-080 identifies a qualitatively different extra-structure regime:

\[
\boxed{
\text{order-compatible full-kernel repair}
\quad\Longleftrightarrow\quad
\text{projection-band kernel},
}
\tag{29}
\]

and, once the condition holds, the repair is already unique and contractive.

For any future claim that positivity, order, monotonicity, or a positive operator restores information lost by a quotient, the first audit should therefore distinguish three levels:

\[
\text{positive recovered map}
\;<\;
\text{order-compatible decomposition }(0\le P\le I)
\;<\;
\text{discriminator-specific minimal recovery}.
\tag{30}
\]

Only the middle level has the exact projection-band canonicity theorem proved here; the first can remain noncanonical, and the third remains a separate problem. This provides a precise stopping rule for positivity-based repair proposals before they are used as evidence that a compressed arithmetic or geometric object has retained its original provenance.