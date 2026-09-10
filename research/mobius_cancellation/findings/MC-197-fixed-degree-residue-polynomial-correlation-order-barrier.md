# MC-197 — Fixed-degree residue polynomials cannot reach the rough zero mode without a same-residue correlation bill

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `DECISIVE-NEGATIVE`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-196` exhibits one genuine nonlinear escape from the linear/Herimitian sector-separation results `MC-190`--`MC-194`: after aggregating the logarithmically rough Möbius coefficient by residue class modulo the primorial, a cubic polynomial in the transverse class variables can land in the principal representation. Its exact source expansion, however, opens same-residue pair and triple correlations.

The phenomenon is not special to the cubic chosen there. It is forced for **every fixed-degree classwise polynomial built from residue-aggregate moments of a ternary source**.

Fix a modulus `q`, a finite source set in each reduced residue class `a`, and values

\[
x_n\in\{-1,0,1\}.
\]

For each class put

\[
A_a=\sum_{n\equiv a\pmod q}x_n,
\qquad
B_a=\sum_{n\equiv a\pmod q}x_n^2.
\tag{1}
\]

Every one-site power-sum aggregate already reduces to these two coordinates, because

\[
\sum_{n\equiv a}x_n^j
=
\begin{cases}
A_a,&j\text{ odd},\\
B_a,&j\text{ even}.
\end{cases}
\tag{2}
\]

Let

\[
P(U,V)=\sum_{r,s\ge0}c_{r,s}U^rV^s
\tag{3}
\]

be a polynomial of effective total degree `d`, with coefficients fixed independently of the unknown source values. For `r+s=k`, define the ordered distinct-index source statistic

\[
D_{r,s}(a)
:=
\sum_{\substack{i_1,\ldots,i_r,j_1,\ldots,j_s\\
\text{all distinct in class }a}}
 x_{i_1}\cdots x_{i_r}
 x_{j_1}^2\cdots x_{j_s}^2.
\tag{4}
\]

Then every monomial has an exact triangular collision expansion

\[
\boxed{
A_a^rB_a^s
=
D_{r,s}(a)
+
\sum_{r'+s'<r+s}
\kappa_{r,s}^{r',s'}D_{r',s'}(a),
}
\tag{5}
\]

for explicit integer coefficients `kappa` obtained by grouping index assignments by their equality partition. Consequently, the interaction-order-`d` component of `P(A_a,B_a)` is exactly

\[
\boxed{
\sum_{r+s=d}c_{r,s}D_{r,s}(a).
}
\tag{6}
\]

It cannot vanish identically unless all degree-`d` coefficients vanish. Thus **a genuinely degree-`d>=2` classwise polynomial necessarily contains a genuine `d`-point distinct-source interaction.** Normal-ordering can cancel diagonal/repeated-index pieces, but it cannot remove the highest distinct-index interaction while retaining the same effective degree.

The same conclusion holds after centering. Write

\[
S=\sum_aA_a,
\qquad Q=\sum_aB_a,
\qquad
u_a=A_a-\frac S\phi,
\qquad
v_a=B_a-\frac Q\phi,
\tag{7}
\]

where `phi` is the number of reduced residue classes. Translation by the constants `S/phi,Q/phi` does not change the highest homogeneous part of `P`; therefore

\[
\sum_aP(u_a,v_a)
\tag{8}
\]

has the same nonzero top interaction order `d` whenever `P` has effective degree `d>=2`.

This gives a sharp sign-sensitive dichotomy for the principal rough Möbius mode.

- For an **uncentered** uniform classwise polynomial, the only sign-sensitive contribution that avoids every multipoint source interaction is a direct affine term `alpha A_a`, whose class sum is `alpha S`; it has simply reinserted the target principal sum.
- For a **centered** uniform classwise polynomial, `sum_a u_a=0`, so even that linear escape disappears. Any nontrivial sign-sensitive classwise polynomial capable of feeding information back toward `S` has degree at least two and therefore exposes a same-residue multipoint source term.

At the active logarithmic primorial

\[
q=q_y=\prod_{p\le c\log X}p=X^{c+o(1)},
\qquad
x_n=g_y(n)=\mu(n)\mathbf 1_{(n,q)=1},
\tag{9}
\]

the top interaction in `(6)` is supported on a deterministic polynomially sparse shift lattice. Anchor one of the `k=d` distinct indices. The remaining `k-1` differences are all multiples of `q`. Hence the source obligation lives on

\[
(q\mathbb Z)^{k-1}\subset\mathbb Z^{k-1},
\tag{10}
\]

with density `q^{-(k-1)+o(1)}` in a polynomial shift box.

For any corresponding `k`-point mixed correlation family `C(\mathbf r)` and fixed `p>=1`, a generic full-shift moment estimate

\[
\left(
\frac1{R^{k-1}}
\sum_{\mathbf r\in[1,R]^{k-1}}
|C(\mathbf r)|^p
\right)^{1/p}
\le XE(X)
\tag{11}
\]

implies by Hölder, **without using extra arithmetic structure of the sublattice**, only

\[
\boxed{
\frac1{L^{k-1}}
\sum_{\mathbf h\in[1,L]^{k-1}}
|C(q\mathbf h)|
\ll
q^{(k-1)/p+o(1)}XE(X),
\qquad L=\lfloor R/q\rfloor.
}
\tag{12}
\]

Thus the generic restriction price rises with interaction order:

\[
\boxed{
q^{(k-1)/p}=X^{c(k-1)/p+o(1)}.
}
\tag{13}
\]

For fixed `p`, an inverse-logarithmic or merely `X^{o(1)}` averaged saving cannot pay this polynomial restriction cost. A full-shift power saving `E(X)=X^{-\delta+o(1)}` must satisfy at least

\[
\delta>\frac{c(k-1)}p
\tag{14}
\]

just to leave a fixed-power saving after generic restriction. Alternatively one needs a genuinely uniform/high-moment theorem strong enough to remove the restriction loss, or arithmetic information that sees the primorial lattice directly.

Therefore the live nonlinear frontier after `MC-196` is narrower than “try a different fixed polynomial.” **Every fixed-degree classwise polynomial either collapses to affine/source-complete data or moves the burden to a finite-order same-residue correlation, and higher degree makes the generic sparse-shift budget worse rather than better.** A successful escape must exploit a source identity with additional arithmetic cancellation, a non-classwise/cross-scale operation, a non-polynomial mechanism whose source expansion has new structure, or a correlation theorem specifically strong on the growing primorial lattice.

## 1. Exact collision-partition expansion

Expand `A^rB^s` using `r` labelled `A` slots and `s` labelled `B` slots. Every term chooses one source index for each slot. Partition the `r+s` slots according to which chosen indices coincide.

For one block of an equality partition, suppose it contains `u` `A` slots and `v` `B` slots. Its source contribution is

\[
x^{u+2v}.
\]

Because `x in {-1,0,1}` and the block is nonempty,

\[
x^{u+2v}
=
\begin{cases}
x,&u\text{ odd},\\x^2,&u\text{ even}.
\end{cases}
\tag{15}
\]

After merging every block, the contribution is therefore a distinct-index statistic of the form `D_{r',s'}` with one factor `x` for each odd block and one factor `x^2` for each even block. If no collision occurs, there are exactly `r+s` blocks and the contribution is `D_{r,s}`. Every other equality partition has fewer blocks, giving `(5)`.

This is the familiar set-partition/power-sum-to-distinct-monomial triangularity from classical symmetric-function combinatorics. The general algebra is not claimed as new; the point here is its exact consequence for the current rough-residue source interface.

## 2. Why the top interaction cannot cancel on ternary sources

The ternary relation `x^3=x` could in principle create extra identities absent for generic indeterminates, so the noncancellation in `(6)` needs an explicit check rather than an appeal to unrestricted polynomial algebra.

Consider one residue class containing `p` entries `+1` and `m` entries `-1`; zeros do not contribute. For fixed `k=r+s`, the distinct-index statistic `D_{r,s}` is a polynomial in `(p,m)` of total degree `k`. Its top homogeneous part is

\[
(p-m)^r(p+m)^s.
\tag{16}
\]

The omission of collisions changes only lower-degree terms. As `r` ranges from `0` to `k`, the polynomials

\[
(p-m)^r(p+m)^{k-r}
\tag{17}
\]

are linearly independent: the invertible linear change of variables

\[
U=p-m,\qquad V=p+m
\]

turns them into the ordinary monomial basis `U^rV^{k-r}` for homogeneous degree `k` polynomials. Hence no nonzero linear combination of the top-order `D_{r,k-r}` can vanish for all ternary source configurations. Equation `(6)` is therefore a genuine source interaction, not an artifact of treating ternary values as free variables.

## 3. Low-degree examples show what normal-ordering can and cannot do

The first identities make the mechanism transparent:

\[
A^2-B=D_{2,0},
\tag{18}
\]

\[
AB-A=D_{1,1},
\tag{19}
\]

and

\[
A^3-3AB+2A=D_{3,0}.
\tag{20}
\]

The corrections `-B`, `-A`, and `-3AB+2A` remove collision strata. They do **not** manufacture cancellation of the all-distinct source term; they isolate it. Equation `(20)` is exactly the one-class ternary identity underlying the `D_3` term in `MC-196`.

This also explains why searching for a higher-degree analogue of the cubic correction is not, by itself, an escape. One can recursively subtract every lower collision stratum and obtain a cleaner `k`-point U-statistic, but the resulting object is then *more directly* a `k`-point same-residue correlation.

## 4. Primorial restriction budget in arbitrary interaction order

For a fixed exponent pattern `epsilon_j in {1,2}`, anchor the first source index and write a `k`-point correlation schematically as

\[
C_{\boldsymbol\epsilon}(r_2,\ldots,r_k)
=
\sum_n
x_n^{\epsilon_1}
\prod_{j=2}^k x_{n+r_j}^{\epsilon_j},
\tag{21}
\]

with the summation restricted so all arguments lie in the observation interval. Same residue modulo `q` forces every `r_j` into `q Z`. Ordering the original tuple, choosing a different anchor, and excluding diagonal shifts change only finite combinatorial factors depending on fixed `k`; they do not change the sublattice density.

To prove `(12)`, let `Lambda` be the admissible `q`-sublattice points in the full `(k-1)`-dimensional shift box. Then `|Lambda|=R^{k-1}q^{-(k-1)+o(1)}`. Hölder gives

\[
\frac1{|\Lambda|}\sum_{\mathbf r\in\Lambda}|C(\mathbf r)|
\le
|\Lambda|^{-1/p}
\left(\sum_{\mathbf r\in[1,R]^{k-1}}|C(\mathbf r)|^p\right)^{1/p},
\]

and substituting `(11)` and the size of `Lambda` yields `(12)`--`(13)`.

This is an information bound, not an arithmetic impossibility theorem. A theorem specialized to primorial multiples can outperform it. What it rules out is a black-box passage from a generic fixed-`p` full-shift moment estimate to the source terms forced by a fixed-degree residue polynomial without paying for the polynomial sparsity.

## 5. Prior-art and novelty audit

The collision expansion itself belongs to classical set-partition and symmetric-function algebra; no novelty is claimed for the abstract change of basis between products of power sums and distinct-index symmetric sums.

The arithmetic boundary is consistent with the existing audited correlation sources. `MC-S13` gives averaged Chowla-type information after averaging over shifts, while `MC-S29` gives recent quantitative logarithmically weighted Liouville correlation information with fixed-moment polynomial shift windows and stronger individual control only in a polylogarithmic range. `MC-S2` supplies powerful almost-all short-interval/higher-uniformity information but not a stated fixed-power theorem on the prescribed `(q Z)^{k-1}` source lattice. `MC-S45` controls rough Möbius dispersion across the smooth primorial modulus only after removing the best-pretending character profile; `MC-188` already shows that this leaves the principal zero mode outside the fixed-power conclusion.

A targeted literature search over symmetric-function/set-partition normal ordering, averaged Möbius/Chowla correlations, and Möbius correlations in arithmetic progressions found the component languages above but no theorem that removes the exact growing-primorial restriction bill `(13)` for the mixed signed/support correlations forced here. The durable Mathia delta is therefore not a claim that polynomial collision expansions are new. It is the **method-class closure obtained by composing that classical triangularity with the exact rough primorial interface of `MC-180`, the sector separation of `MC-188`--`MC-194`, and the cubic source audit of `MC-196`.**

## 6. Boundaries and falsification tests

- The theorem covers **uniform classwise polynomials in finitely many one-site residue power sums**, equivalently polynomials in `(A_a,B_a)`, at fixed effective degree. It does not cover arbitrary kernels coupling several residue classes, cross-scale identities, operations applied before residue aggregation, rational/transcendental functions, or degree growing with `X`.
- Coefficients may depend on external deterministic parameters such as `q` or `X`, but `d` means the effective degree after that specialization. Coefficients chosen using the unknown principal sum or other target-complete source data require a separate circularity audit.
- Equation `(13)` is the generic restriction cost for a fixed-`p` moment theorem. It does not assert that every arithmetic proof must pay that cost; arithmetic structure recognizing primorial multiples may beat Hölder.
- A high-degree polynomial can suppress lower collision terms exactly. This does not contradict the claim: the highest surviving distinct-index term is precisely the source obligation the theorem identifies.
- Mixed exponents `1` and `2` include sign-support correlations as well as pure Chowla sign correlations. A theorem controlling only one of those subclasses cannot silently be substituted for the full source expansion.
- The result gives no new exponent for `M(x)` and proves no new zero-free region. It closes a representation/mechanism class and sharpens what arithmetic input a surviving nonlinear route must supply.

A counterexample to the core claim would be a source-independent fixed-degree `P` whose effective degree is at least two but whose classwise source expansion has no nonzero distinct-index interaction of that top order for all ternary inputs. The argument in Sections 1--2 excludes such a polynomial.

## Consequence for the line

`MC-196` left open whether another low-degree nonlinear residue statistic might couple transverse information into the rough principal mode while avoiding the pair/triple bill of its specific cubic. Within the fixed-degree classwise polynomial category, that loophole is now closed.

The next viable source-side question is not which quartic or quintic correction to try. It is whether the arithmetic itself supplies a relation that **cancels or controls the required same-residue interactions for structural reasons**, or whether one must leave the classwise fixed-degree polynomial category altogether. In particular, raising polynomial degree while relying on generic averaged correlation input is counterproductive at the primorial scale because the restriction exponent grows from `c/p` at order two to `c(k-1)/p` at interaction order `k`.