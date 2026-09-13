# AF-314 — A single complex invariant completes the five-point zero shape

**Status:** `EXACT-DERIVED`, `STRUCTURAL-RECOVERY`, `GAUGE-COMPRESSION`, `ARITHMETIC-CONTROL`, `NO-NOVELTY-CLAIM`

## Claim

AF-313 shows that on the five-point unit-circle zero fiber, the pair of higher harmonics `(s_2,s_3)` recovers the complete unordered phase multiset except for the rotated regular-pentagon fiber. That pair still carries one redundant common-phase gauge. On the same zero fiber the redundancy can be removed exactly.

Let

\[
Z=\{z_1,\ldots,z_5\}\subset \mathbb S^1,
\qquad
s_m(Z)=\sum_{j=1}^5 z_j^m,
\]

with multiplicity allowed, and restrict to

\[
s_1(Z)=0.
\tag{1}
\]

Identify configurations under permutation and common rotation,

\[
Z\sim \rho Z,
\qquad \rho\in \mathbb S^1.
\tag{2}
\]

Define the extended weighted invariant

\[
\boxed{
\kappa(Z)=
\begin{cases}
\dfrac{s_2(Z)^3}{s_3(Z)^2},&s_2(Z)\ne0,\\[1.1ex]
0,&s_2(Z)=0.
\end{cases}}
\tag{3}
\]

Then:

1. `\kappa` is invariant under permutation and common rotation;
2. the extension in `(3)` is continuous on the entire five-point zero fiber;
3. `\kappa` is a **complete invariant modulo common rotation**:
   \[
   \boxed{
   \kappa(Z)=\kappa(Z')
   \iff
   Z'=\rho Z\text{ for some }\rho\in\mathbb S^1;
   }
   \tag{4}
   \]
4. consequently the compact unordered rotation quotient is homeomorphic, via `\kappa`, to its image in `\mathbb C`;
5. on every nondegenerate fiber, `\kappa` is the primitive Laurent-monomial invariant of the weighted rotation action on `(s_2,s_3)`, whose weights are `(2,3)`.

Thus AF-313's two complex higher-harmonic observations can be compressed to **one complex scalar without losing any unordered shape information after the first-harmonic cancellation**.

For five distinct rational primes, write

\[
F_P(t)=\sum_{j=1}^5p_j^{-it}.
\tag{5}
\]

If `t\ne0` and `F_P(t)=0`, AF-312 gives `F_P(2t),F_P(3t)\ne0`, so

\[
\boxed{
\kappa_P(t)=\frac{F_P(2t)^3}{F_P(3t)^2}
}
\tag{6}
\]

is well-defined and recovers the complete unordered phase configuration

\[
\{p_1^{-it},\ldots,p_5^{-it}\}
\]

**modulo one common phase**. It does not recover prime labels, the time `t`, or the existence of a first exact hit.

## Derivation

### 1. The zero fiber supplies exactly the missing radial relation

AF-313 derives, for every five-point unit-circle configuration satisfying `(1)`,

\[
s_3=-\frac32 E\,\overline{s_2},
\qquad
E=\prod_{j=1}^5z_j\in\mathbb S^1.
\tag{7}
\]

Hence

\[
\boxed{|s_3|=\frac32|s_2|.}
\tag{8}
\]

In particular `s_2` and `s_3` vanish together. AF-313 also proves that this common zero occurs exactly for a rotated regular pentagon,

\[
Z=\rho\mu_5.
\tag{9}
\]

For `s_2\ne0`, equations `(3)` and `(8)` give

\[
\boxed{
|\kappa|
=\frac{|s_2|^3}{|s_3|^2}
=\frac49|s_2|.
}
\tag{10}
\]

Therefore `\kappa\to0` whenever a configuration approaches the exceptional regular-pentagon fiber. Defining `\kappa=0` there gives a continuous extension, not an arbitrary patch of a `0/0` expression.

Equation `(10)` is also the key reason one complex invariant is sufficient here. For a general weighted pair `(u,v)` with weights `(2,3)`, the phase invariant `u^3/v^2` would not retain an independent radial modulus. On the five-point zero fiber, `(8)` locks the two radii together, and the modulus of `\kappa` recovers that remaining radial information automatically.

### 2. Common rotation leaves `\kappa` unchanged

Under a common rotation `Z\mapsto\rho Z`,

\[
s_2\mapsto \rho^2s_2,
\qquad
s_3\mapsto \rho^3s_3.
\tag{11}
\]

Thus on the nondegenerate fiber

\[
\frac{(\rho^2s_2)^3}{(\rho^3s_3)^2}
=\frac{s_2^3}{s_3^2}.
\tag{12}
\]

The exceptional fiber is already one common-rotation orbit by `(9)`, so the continuous extension is invariant there as well. Permutation invariance is immediate because every `s_m` is symmetric in the five points.

The exponent relation behind `(12)` is primitive:

\[
2a+3b=0,
\qquad (a,b)\in\mathbb Z^2,
\tag{13}
\]

has kernel

\[
\mathbb Z(3,-2).
\tag{14}
\]

Hence `s_2^3s_3^{-2}` is the primitive Laurent character killed by the common-phase action on the nonzero two-harmonic pair. This is the two-coordinate specialization of the annihilator-lattice principle in AF-005.

### 3. Equality of `\kappa` forces equality up to rotation

Take two nondegenerate configurations `Z,Z'` satisfying `(1)` and suppose

\[
\kappa(Z)=\kappa(Z').
\tag{15}
\]

Write

\[
A=\frac{s_2(Z')}{s_2(Z)},
\qquad
B=\frac{s_3(Z')}{s_3(Z)}.
\tag{16}
\]

By `(10)`, equality of `\kappa` implies

\[
|s_2(Z')|=|s_2(Z)|,
\]

and then `(8)` also gives equality of the `s_3` moduli. Therefore

\[
|A|=|B|=1.
\tag{17}
\]

Equation `(15)` itself gives

\[
A^3=B^2.
\tag{18}
\]

Set

\[
\rho=\frac BA\in\mathbb S^1.
\tag{19}
\]

Using `(18)`,

\[
\rho^2=\frac{B^2}{A^2}=A,
\qquad
\rho^3=\frac{B^3}{A^3}=B.
\tag{20}
\]

Consequently

\[
\bigl(s_2(Z'),s_3(Z')\bigr)
=
\bigl(\rho^2s_2(Z),\rho^3s_3(Z)\bigr)
=
\bigl(s_2(\rho Z),s_3(\rho Z)\bigr).
\tag{21}
\]

AF-313 proves that `(s_2,s_3)` uniquely determines the unordered multiset on every nondegenerate `s_1=0` fiber. Therefore

\[
Z'=\rho Z.
\tag{22}
\]

If instead `\kappa(Z)=\kappa(Z')=0`, equation `(10)` forces `s_2=s_2'=0`, and AF-313 identifies both configurations as rotated regular pentagons. They are again equivalent under `(2)`. This proves `(4)` globally.

Conversely, `(12)` already showed that common rotation preserves `\kappa`, so the equivalence is exact in both directions.

### 4. Explicit reconstruction of the shape from one complex number

The completeness proof is constructive. Given a nonzero admissible value `\kappa`, equation `(10)` recovers

\[
r:=|s_2|=\frac94|\kappa|.
\tag{23}
\]

Use common rotation to choose a representative with

\[
s_2=r>0.
\tag{24}
\]

Then `(3)` requires

\[
s_3^2=\frac{r^3}{\kappa}.
\tag{25}
\]

The two square roots differ by sign. That sign is precisely the residual rotation `\rho=-1`, because it fixes `s_2` and sends `s_3\mapsto-s_3`. Thus either square root represents the same shape orbit.

With `(s_2,s_3)` fixed, AF-313 reconstructs the phase multiset as the roots of

\[
w^5-rac{s_2}{2}w^3-rac{s_3}{3}w^2+rac{2s_3}{3\overline{s_2}}.
\tag{26}
\]

For `\kappa=0`, the unique shape orbit is the regular pentagon. Hence `(23)`--`(26)` give an explicit inverse on the image of `\kappa`.

## Topological compression count

There is a genuine reduction here, not only an algebraic repackaging of two complex numbers.

Consider the ordered zero set

\[
\mathcal M
=
\left\{(z_1,\ldots,z_5)\in(\mathbb S^1)^5:
\sum_jz_j=0
\right\}.
\tag{27}
\]

The summation map from the five-torus to `\mathbb C\cong\mathbb R^2` has differential of real rank two at every point of `\mathcal M`. Rank could fail only if all tangent vectors `iz_j` lay on one real line, equivalently if all `z_j` belonged to one antipodal pair `{u,-u}`. Five unit vectors chosen from one antipodal pair cannot sum to zero because the two multiplicities have odd total. Therefore `\mathcal M` is a smooth real three-manifold.

Common rotation acts freely on ordered configurations, so the rotation quotient has real dimension two. Quotienting further by the finite permutation group does not change the local dimension at generic configurations. Thus the unordered shape space has two-real-dimensional regular patches.

Accordingly, no continuous exact Euclidean summary taking values in one real coordinate can be faithful on the whole generic shape space: a two-dimensional manifold patch cannot topologically embed in `\mathbb R`. A single complex coordinate supplies exactly two real coordinates. In this restricted sense, `\kappa` is **dimension-tight among continuous Euclidean shape summaries**.

This is not a claim that `\kappa` is uniquely canonical, that discontinuous encodings are impossible, or that one complex number minimizes every computational, algebraic, or arithmetic notion of cost.

## Prime-phase specialization

Let `p_1,\ldots,p_5` be distinct rational primes and suppose

\[
t\ne0,
\qquad
F_P(t)=0.
\tag{28}
\]

AF-312 proves

\[
F_P(2t)\ne0,
\qquad
F_P(3t)\ne0,
\tag{29}
\]

by excluding the torsion geometries that would force those higher harmonics to vanish. Therefore `(6)` is always defined at a hypothetical nonzero five-prime exact hit.

AF-313 then gives exact recovery from the pair `(F_P(2t),F_P(3t))`. The present theorem quotients precisely the one common-phase degree of freedom in that pair while retaining the entire unordered relative phase geometry. So after incidence,

\[
\boxed{
F_P(t)=0
\quad\Longrightarrow\quad
\kappa_P(t)
\text{ is a complete unordered phase-shape coordinate.}
}
\tag{30}
\]

This is a post-incidence fidelity statement. It does not decide whether the prime logarithmic orbit ever reaches the five-point zero surface. Nor does shape recovery identify which recovered phase belongs to which rational prime. Any use that requires labels, absolute phase, or the original time parameter must pay for that information separately.

There is also no uniform conditioning claim. Although prime phases exclude the exact regular-pentagon orbit, the present argument gives no positive lower bound on `|s_2|` for hypothetical prime hits. Since `(23)`--`(26)` become singular as `\kappa\to0`, exact quotient fidelity can coexist with arbitrarily poor stable recovery near that exceptional orbit.

## Prior art and novelty assessment

The broad geometry is classical. Stephan Klaus and Sadayoshi Kojima, **“On the moduli space of equilateral plane pentagons,”** *Beiträge zur Algebra und Geometrie* 60 (2019), 487--497, DOI `10.1007/s13366-018-0429-z`, describe the equilateral-pentagon moduli space as a closed genus-four surface and give an algebraic model. Lyle Ramshaw, **“The Bring sextic of equilateral pentagons,”** arXiv:`2205.08196` (2022), likewise treats the shape space as a real two-manifold and relates its conformal geometry to the Bring sextic. Harry W. Braden and Linden Disney-Hogg, **“Bring's curve: old and new,”** *European Journal of Mathematics* 10, article 3 (2024), DOI `10.1007/s40879-023-00706-0`, gives modern invariant/quotient context for the genus-four Bring curve and its large `S_5` symmetry.

The exact weighted-action mechanism is also classical in spirit: characters of a torus and their primitive integer relations control phase quotients, as already audited in AF-005. AF-313 supplies the special five-point self-inversive/Newton relation that makes the primitive weighted invariant sufficient rather than merely phase-invariant.

A targeted literature search did not identify the exact coordinate `s_2^3/s_3^2` with the completeness statement `(4)` for the unordered unit-edge zero fiber. That absence is not evidence of novelty, and **no novelty claim is made**. The durable result is the exact fidelity reduction obtained by combining classical weighted-invariant structure with the special algebraic constraint already proved in AF-313.

## Boundaries and falsification checks

- The theorem assumes exactly five unit-modulus points and exact first-harmonic cancellation `s_1=0`.
- Recovery is of the **unordered** multiset modulo common rotation. It does not restore labels or absolute phase.
- The exceptional `s_2=s_3=0` set is harmless only because AF-313 proves that it is exactly one rotation orbit, the regular pentagon.
- The quotient coordinate is exact, not uniformly conditioned near `\kappa=0`.
- The dimension-tight statement concerns continuous maps into Euclidean coordinate spaces on generic shape patches. It does not exclude discontinuous encodings or compare algebraic complexity.
- No claim is made that the image of `\kappa` is a disk, that its boundary has been classified, or that every complex value satisfying the elementary modulus bounds is realizable.
- The prime specialization assumes a hypothetical exact hit and uses AF-312/AF-313. It gives no first-incidence theorem and no RH consequence.
- Equality of `\kappa_P` values at different prime systems or different times is only equality of unordered phase shape modulo common phase; it is not equality of the underlying prime sets.

## Dependency audit

- **AF-005:** supplies the exact annihilator-lattice viewpoint for primitive phase-invariant monomials; here the weight relation `(2,3)` has primitive kernel generator `(3,-2)`.
- **AF-312:** excludes vanishing second and third harmonics at a nonzero five-prime exact hit, so the arithmetic coordinate `(6)` is well-defined.
- **AF-313:** supplies the five-point zero-fiber relation `|s_3|=(3/2)|s_2|`, classifies the common zero as the regular-pentagon orbit, and proves exact recovery from `(s_2,s_3)` away from that orbit.
- **This finding:** removes the remaining common-phase redundancy and shows that one complex weighted invariant is already complete for the unordered post-incidence shape.