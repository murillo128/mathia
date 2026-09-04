# AF-122 — Uniform-modulus recovery orders conditional quantization profiles

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-INGREDIENTS`, `CATEGORY-INDEXED`, `MULTISCALE-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-119--AF-121 separate finite exact-description cost from first-order information-dimension cost, but information dimension retains only one asymptotic slope. A stronger invariant survives regular exact recovery: the **entire conditional fine-quantization entropy profile**, up to the scale change forced by the recovery modulus.

Let `Y` be arbitrary retained side information taking values in a standard Borel space, and let

\[
M\in[0,1)^r,
\qquad
D\in[0,1)^q
\]

be respectively an auxiliary mark and a discriminator. Assume

\[
D=R(Y,M)
\qquad\text{almost surely}.
\tag{1}
\]

Suppose there is one nondecreasing modulus

\[
\omega:[0,\infty)\to[0,\infty),
\qquad
\omega(t)\to0\quad(t\downarrow0),
\tag{2}
\]

such that for almost every `y`, uniformly over the relevant mark domain,

\[
\|R_y(m)-R_y(m')\|_2
\le
\omega(\|m-m'\|_2),
\qquad
R_y(m):=R(y,m).
\tag{3}
\]

For `k>=0`, define the dyadic cell label

\[
Q_k(X):=\lfloor 2^k X\rfloor
\tag{4}
\]

coordinatewise and the conditional quantization-entropy profile

\[
E_X(k\mid Y):=H_2(Q_k(X)\mid Y).
\tag{5}
\]

Define the modulus-induced scale transfer

\[
\phi_\omega(k)
:=
\min\left\{m\ge0:
\omega(\sqrt r\,2^{-m})\le2^{-k}
\right\}.
\tag{6}
\]

Then `phi_omega(k)` is finite for every sufficiently large `k`, and

\[
\boxed{
E_D(k\mid Y)
\le
E_M(\phi_\omega(k)\mid Y)+q.
}
\tag{7}
\]

Equivalently, every uniformly continuous exact repair must pay at the mark scale selected by its own recovery modulus:

\[
\boxed{
E_M(\phi_\omega(k)\mid Y)
\ge
E_D(k\mid Y)-q.
}
\tag{8}
\]

Thus regular recovery does not merely order information dimensions. It orders the full multiscale entropy-growth curve after the exact deterministic rescaling induced by the modulus.

### Hölder specialization

If the sections are uniformly `(L,alpha)`-Hölder,

\[
\|R_y(m)-R_y(m')\|_2
\le
L\|m-m'\|_2^\alpha,
\qquad 0<\alpha\le1,
\tag{9}
\]

then there is a fixed integer `c=c(L,r,alpha)` such that

\[
\boxed{
E_D(k\mid Y)
\le
E_M\!\left(\left\lceil\frac{k}{\alpha}\right\rceil+c\middle|Y\right)+q
}
\tag{10}
\]

for every `k>=0`. Consequently the lower and upper conditional information dimensions obey

\[
\boxed{
\underline d(D\mid Y)
\le
\frac1\alpha\,\underline d(M\mid Y),
\qquad
\overline d(D\mid Y)
\le
\frac1\alpha\,\overline d(M\mid Y).
}
\tag{11}
\]

For `alpha=1`, `(11)` recovers the dimension inequality of AF-121, while `(10)` is strictly more informative whenever the normalized slope is zero or fails to capture the relevant growth regime.

### Composition

The profile order composes. If a second exact repair

\[
M=S(Y,N)
\tag{12}
\]

has a uniform modulus `eta`, then applying `(7)` twice gives

\[
\boxed{
E_D(k\mid Y)
\le
E_N\bigl(\phi_\eta(\phi_\omega(k))\mid Y\bigr)+q+r.
}
\tag{13}
\]

At the metric level the composed decoder has modulus `omega o eta`. Hence a chain of regular repairs carries an explicit scale-cost calculus: lost fine structure cannot be restored downstream without paying the composed resolution demand.

## Derivation

### One sufficiently fine mark cell reaches only constantly many discriminator cells

Fix a target scale `k` and put

\[
m=\phi_\omega(k).
\tag{14}
\]

Every `Q_m(M)` cell is a half-open cube of side `2^{-m}` in `R^r`, hence has Euclidean diameter at most

\[
\sqrt r\,2^{-m}.
\tag{15}
\]

By `(3)` and the definition of `m`, the image under every admissible fiber map `R_y` has diameter at most

\[
\omega(\sqrt r\,2^{-m})
\le
2^{-k}.
\tag{16}
\]

A subset of `R^q` with Euclidean diameter at most `2^{-k}` has coordinate range at most one target-cell width in every coordinate. It can therefore intersect at most two dyadic intervals per coordinate and at most

\[
2^q
\tag{17}
\]

target `Q_k(D)` cells in total.

Since `(1)` makes `D` deterministic given `(Y,M)`, the conditional support of `Q_k(D)` given `(Y,Q_m(M))` has cardinality at most `2^q`. Therefore

\[
H_2(Q_k(D)\mid Y,Q_m(M))\le q.
\tag{18}
\]

The entropy chain rule now gives

\[
\begin{aligned}
E_D(k\mid Y)
&=H_2(Q_k(D)\mid Y)\\
&\le H_2(Q_m(M),Q_k(D)\mid Y)\\
&=E_M(m\mid Y)
 +H_2(Q_k(D)\mid Y,Q_m(M))\\
&\le E_M(m\mid Y)+q,
\end{aligned}
\tag{19}
\]

which proves `(7)`.

The additive `q` is deliberately coarse and scale-independent. The theorem concerns asymptotic and profile fidelity, not optimization of the boundary-cell constant.

### Hölder scale transfer

Under `(9)`, a mark cell at depth `m` has image diameter at most

\[
L r^{\alpha/2}2^{-\alpha m}.
\tag{20}
\]

Choose any integer

\[
c\ge
\max\left\{0,
\left\lceil
\frac{\log_2(Lr^{\alpha/2})}{\alpha}
\right\rceil
\right\}.
\tag{21}
\]

Then `m=ceil(k/alpha)+c` makes `(20)` at most `2^{-k}`, proving `(10)`.

For the upper dimension, divide `(10)` by `k` and use

\[
\frac{\lceil k/\alpha\rceil+c}{k}\to\frac1\alpha.
\tag{22}
\]

For the lower dimension one cannot simply take the liminf along the possibly sparse sequence `ceil(k/alpha)+c`. Instead use the monotonicity of the dyadic profile: `Q_{m+1}(M)` refines `Q_m(M)`, so

\[
E_M(m+1\mid Y)\ge E_M(m\mid Y).
\tag{23}
\]

Take a sequence `m_j` realizing the lower information-dimension liminf and set

\[
k_j:=\left\lfloor\alpha(m_j-c-1)\right\rfloor.
\tag{24}
\]

For large `j`, `k_j>0`, `k_j/m_j->alpha`, and

\[
\left\lceil\frac{k_j}{\alpha}\right\rceil+c\le m_j.
\tag{25}
\]

Applying `(10)` and `(23)` along this subsequence yields

\[
\liminf_k\frac{E_D(k\mid Y)}k
\le
\frac1\alpha
\liminf_m\frac{E_M(m\mid Y)}m.
\tag{26}
\]

The ordinary all-integer uniform-quantizer definition of conditional information dimension gives the same lower and upper limits as the dyadic subsequence here: between two adjacent dyadic resolutions the cell widths differ by less than a factor of two, so the two finite partitions refine each other up to a scale-independent bounded-overlap entropy term. Thus `(11)` is the corresponding Rényi-dimension statement.

## Why the profile is stronger than information dimension

AF-121 already proves that positive conditional information dimension cannot be created by a uniformly fiberwise Lipschitz decoder from a lower-dimensional side mark. But its own Bernoulli control shows that information dimension assigns zero to every finite discrete ambiguity, and AF-120 shows something stronger: even a countably atomic variable of infinite Shannon entropy can have information dimension zero while its exact dyadic entropy profile diverges.

Equation `(8)` survives that collapse. If a discriminator has

\[
E_D(k\mid Y)\to\infty
\qquad\text{but}\qquad
\frac{E_D(k\mid Y)}k\to0,
\tag{27}
\]

then every uniformly continuous repair must still have an unbounded mark profile along the transferred scales. The divergence may be logarithmic, iterated-logarithmic, or another sublinear regime invisible to information dimension; regular recovery cannot make it disappear merely because its normalized first-order slope is zero.

This puts the recent entropy findings into one hierarchy:

- AF-119 detects whether a coherent exact description has bounded total Shannon cost;
- AF-120 identifies the first-order linear growth coefficient with Rényi information dimension;
- AF-121 makes that coefficient a category-indexed lower bound under Lipschitz recovery;
- AF-122 retains the full growth profile and lets the recovery modulus determine the required scale conversion.

The profile is still not a category-free amount of information. It becomes a valid fidelity resource only after the observable geometry and reconstruction regularity have been independently justified.

## Sharpness and controls

### Hölder scale loss is genuinely necessary

The factor `1/alpha` in `(11)` cannot be improved in general. Standard `d`-dimensional space-filling curves can be chosen Lebesgue-measure preserving and `1/d`-Hölder. Let

\[
U\sim\operatorname{Unif}[0,1],
\qquad
D=F(U)\sim\operatorname{Unif}[0,1]^d
\tag{28}
\]

for such a curve `F`. Then

\[
E_U(m)=m,
\qquad
E_D(k)=dk,
\tag{29}
\]

while `alpha=1/d`. Thus the leading scale conversion in `(10)` is attained exactly:

\[
d(D)=d=\frac1\alpha d(U).
\tag{30}
\]

This is also the correct adversarial control against replacing Hölder regularity by the false intuition that a scalar parameter can carry at most one-dimensional fine structure under every continuous map.

### Arbitrary measurable recovery kills the theorem

The digit-interleaving construction from AF-121 remains decisive. A scalar uniform mark can measurably encode a two-dimensional uniform discriminator with no Lipschitz or Hölder decoder. Without a uniform modulus, there is no finite scale-transfer function `phi_omega` and no profile inequality of the form `(7)`.

### Uniformity over the retained base is load-bearing

The proof uses one modulus for almost every `y`. If the fiberwise moduli deteriorate without a common bound, one mark cell can map across an unbounded number of target cells as `y` varies. An application with nonuniform regularity needs a separate quantitative theorem; `(7)` cannot be invoked by averaging an uncontrolled family of moduli.

### Tautological copying remains non-explanatory

Taking `M=D` and the identity decoder saturates the profile order. As in AF-001 and AF-121, this proves sharpness but not a useful minimal lift. Canonicity, intrinsic availability, and the prohibition on hiding a copy of the target inside the mark remain separate gates.

### The dyadic Euclidean filtration is part of the category

An arbitrary Borel reparameterization can drastically change fine quantization entropy while preserving set-theoretic recoverability. Therefore the profile is meaningful only when the Euclidean metric/dyadic filtration, or a uniformly comparable intrinsic refinement family, is part of the declared observable category.

## Prior art and novelty assessment

The mathematical ingredients are classical, and **no standalone novelty claim is made for the entropy inequality, Hölder dimension monotonicity, or space-filling sharpness example**.

- Alfréd Rényi, **“On the Dimension and Entropy of Probability Distributions,”** *Acta Mathematica Academiae Scientiarum Hungaricae* 10, 193–215 (1959), DOI `10.1007/BF02063299`. Role: foundational quantization-entropy definition of information dimension.
- Yihong Wu and Sergio Verdú, **“Rényi Information Dimension: Fundamental Limits of Almost Lossless Analog Compression,”** *IEEE Transactions on Information Theory* 56(8), 3721–3748 (2010), DOI `10.1109/TIT.2010.2050803`. Role: direct prior art for information dimension as a regularity-constrained analog-compression resource, in particular under Lipschitz decompression.
- Tsutomu Kawabata and Amir Dembo, **“The Rate-Distortion Dimension of Sets and Measures,”** *IEEE Transactions on Information Theory* 40(5), 1564–1572 (1994/1995 bibliographic indexing), DOI `10.1109/18.333868`. Role: classical rate-distortion-dimension bridge showing that fine-scale entropy growth already has an operational compression language beyond raw coordinate counting.
- Bernhard C. Geiger and Tobias Koch, **“On the Information Dimension of Stochastic Processes,”** *IEEE Transactions on Information Theory* 65(10), 6496–6518 (2019), DOI `10.1109/TIT.2019.2922186`. Role: modern information-dimension-rate and conditional/regular-transformation context adjacent to AF-121 and the present profile formulation.
- Manuel Fernández-Martínez, Juan Luis García Guirao, and Miguel Ángel Sánchez-Granero, **“Calculating Hausdorff Dimension in Higher Dimensional Spaces,”** *Symmetry* 11(4), 564 (2019), DOI `10.3390/sym11040564`. Role: explicit higher-dimensional space-filling-curve framework recording both `1/d`-Hölder regularity and Lebesgue-measure preservation, which supplies the sharpness control `(28)`--`(30)`.

The exact profile inequality `(7)` is an elementary consequence of a modulus-of-continuity covering estimate plus Shannon's chain rule. It should therefore be treated as an Arithmetic Fidelity organization of classical ingredients unless stronger novelty evidence appears. The substantive line-level advance is the **resource choice**: after AF-121, do not collapse every regular-recovery question to one information-dimension scalar. The whole conditional quantization profile is a composable discriminator-relative resource, and information dimension is only one asymptotic quotient of it.

## Consequences for Arithmetic Fidelity

AF-122 gives a general composition law directly aligned with the line's mandate. For a declared regular recovery category, each compression/repair stage induces a scale-transfer map, and the conditional entropy profile can only move downward through that transfer up to a fixed boundary-cell constant. If a downstream proposal claims to recover a discriminator whose profile is richer than the upstream retained mark can support at the required scales, the proposal is impossible before any spectral, positivity, determinant, or asymptotic interpretation is considered.

For eventual arithmetic use, this suggests a sharper audit than asking only whether prime provenance has positive information dimension. First identify a genuinely prime-specific residual factor `D` after the proposed compression `Y`; then identify an intrinsic multiscale observation family and its conditional profile `E_D(k|Y)`. Even when the normalized dimension is zero, an unbounded sublinear profile can impose a real regular-recovery cost. A proposed marking, boundary datum, phase variable, transverse coordinate, or other lift should then be tested against `(7)` using the strongest independently justified modulus available.

This still does not prove that the rational primes possess a special positive or divergent profile in any natural RH representation. It supplies the general theorem needed to ask that question without throwing away sublinear structural complexity at the outset.