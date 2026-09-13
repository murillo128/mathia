# AF-310 — Prime phase relation lattices are cyclic; the pentagon is the first compatible zero geometry

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `CHARACTER-LATTICE`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-307–AF-309 leave the first unresolved saturated equal-weight prime-support exact-zero problem at cardinality `k>=5`. The obstruction used at `k=3,4` has a clean general form.

Let `p_1,...,p_k` be distinct rational primes, let `t!=0`, and normalize by the last phase:

\[
u_j=(p_j/p_k)^{-it},\qquad 1\le j<k.
\tag{1}
\]

Define the integer multiplicative-relation lattice of this normalized phase point by

\[
L_{p,t}
=
\left\{a\in\mathbb Z^{k-1}:
\prod_{j=1}^{k-1}u_j^{a_j}=1
\right\}.
\tag{2}
\]

Then

\[
\boxed{\operatorname{rank}_{\mathbb Z}L_{p,t}\le1,}
\tag{3}
\]

indeed `L_{p,t}` is cyclic. Equivalently, a common nonzero prime-log time orbit can satisfy at most one independent exact monomial phase relation.

This bound is sharp: for every nonzero `a in Z^{k-1}`, the prime-log linear form

\[
\Lambda_a=\sum_{j=1}^{k-1}a_j\log(p_j/p_k)
\tag{4}
\]

is nonzero, and choosing `t=2 pi/\Lambda_a` forces the relation indexed by `a`. Thus one exact character relation can always be manufactured by choosing the time; two independent ones cannot coexist.

The zero-sum geometry now separates sharply by cardinality.

1. Every normalized three-phase zero configuration has relation rank at least two, because a zero-sum unit triple is a rotated regular triangle.
2. Every normalized four-phase zero configuration has relation rank at least two, because a zero-sum unit quadruple splits into two antipodal pairs.
3. Consequently, the cyclic relation-lattice theorem gives one unified arithmetic reason for the exact `k=3,4` prime zero-freeness proved separately in AF-306–AF-307.
4. For `k=5`, this mechanism stops being geometrically decisive. The normalized equilateral-pentagon zero locus `M_5` is a connected closed genus-four surface. The subset on which the multiplicative relation lattice has rank at least two is meagre in `M_5`; equivalently, a dense residual subset of pentagon zero configurations has relation rank at most one.

Therefore `k=5` is the first saturated cardinality at which the exact polygon closure geometry is compatible with the strongest conclusion obtainable from unique factorization at the level of integer phase characters. Extending the `k=3,4` proof merely by extracting more monomial/torsion relations cannot settle the prime-support problem generically.

A further exact corollary is useful for prior-art control:

\[
\boxed{
\text{a normalized prime phase point cannot lie in a torsion coset of codimension }\ge2.
}
\tag{5}
\]

In particular, for `k>=3` it cannot be a torsion point. Hence classifications of exact vanishing sums of roots of unity describe comparison strata and approximants, but an exact rational-prime hit—if one exists for `k>=5`—must be genuinely nontorsion.

## The winding map injects the relation lattice into `Z`

For `a in L_{p,t}`, equation (2) says

\[
\exp\!\left(
-it\sum_{j=1}^{k-1}a_j\log(p_j/p_k)
\right)=1.
\tag{6}
\]

Hence there is an integer `m(a)` such that

\[
t\sum_{j=1}^{k-1}a_j\log(p_j/p_k)=2\pi m(a).
\tag{7}
\]

The assignment

\[
m:L_{p,t}\to\mathbb Z
\tag{8}
\]

is a group homomorphism. It is injective. Indeed, if `m(a)=0`, then

\[
\sum_{j=1}^{k-1}a_j\log(p_j/p_k)=0.
\tag{9}
\]

Expanding the ratios gives

\[
\sum_{j=1}^{k-1}a_j\log p_j
-\left(\sum_{j=1}^{k-1}a_j\right)\log p_k=0.
\tag{10}
\]

Exponentiation turns (10) into a multiplicative relation among the distinct rational primes. Unique factorization forces every exponent to vanish, so `a=0`.

Thus `L_{p,t}` embeds in `Z`. Every subgroup of `Z` is cyclic, proving (3).

There is also a direct two-relation form of the same argument. If independent `a,b in L_{p,t}` had windings `m,n`, then neither winding can vanish. Eliminating `t` from

\[
t\Lambda_a=2\pi m,
\qquad
t\Lambda_b=2\pi n
\]

gives

\[
n\Lambda_a-m\Lambda_b=0.
\tag{11}
\]

Prime-log rational independence forces

\[
na=mb,
\tag{12}
\]

contradicting independence. The obstruction is therefore exactly an integer-character obstruction, not a metric or equidistribution statement.

## Torsion-coset corollary

Let `u=(u_1,...,u_{k-1})` be the normalized prime phase point (1). Suppose `u` belongs to a torsion affine coset of codimension at least two in `(S^1)^{k-1}`. Then there are independent character vectors `a,b in Z^{k-1}` and roots of unity `xi,eta` such that

\[
u^a=\xi,
\qquad
u^b=\eta.
\tag{13}
\]

Choose positive integers `r,s` with `xi^r=eta^s=1`. Then

\[
u^{ra}=1,
\qquad
u^{sb}=1.
\tag{14}
\]

The scaled vectors `ra,sb` remain independent, so (14) gives two independent elements of `L_{p,t}`, contradicting (3). This proves (5).

If `u` itself is torsion and `k>=3`, then for every coordinate `u_j` some positive multiple of the basis vector `e_j` belongs to `L_{p,t}`. Hence the relation rank is `k-1>=2`, again impossible.

This sharply separates the present prime-log problem from root-of-unity vanishing-sum theory. The latter studies precisely a torsion regime that the common-time prime orbit cannot enter once at least three independent prime ratios are retained.

## The cyclic bound unifies the `k=3` and `k=4` exclusions

### Three phases

Let `z_1,z_2,z_3 in S^1` satisfy

\[
z_1+z_2+z_3=0.
\tag{15}
\]

Three unit vectors closing to zero form an equilateral triangle. After normalization by `z_3`, the two ratios are the two nontrivial cube roots of unity, up to permutation. Therefore

\[
(z_1/z_3)^3=1,
\qquad
(z_2/z_3)^3=1.
\tag{16}
\]

The corresponding exponent vectors `(3,0)` and `(0,3)` are independent, so every point of the normalized three-phase zero locus has relation rank two. Equation (3) therefore forbids such a configuration for three distinct rational primes at a common nonzero time.

### Four phases

AF-307 proves the elementary unit-circle lemma that

\[
z_1+z_2+z_3+z_4=0,
\qquad |z_j|=1,
\tag{17}
\]

forces two antipodal pairs after relabelling. Suppose, for example,

\[
z_2=-z_1,
\qquad
z_4=-z_3.
\tag{18}
\]

Normalize by `z_4`. Then

\[
(z_3/z_4)^2=1
\tag{19}
\]

and

\[
\left((z_1/z_4)/(z_2/z_4)\right)^2=1.
\tag{20}
\]

These give two independent character relations in the three normalized coordinates. Hence the four-phase zero locus also lies entirely in the relation-rank-at-least-two stratum, and (3) rules out a four-prime exact hit.

The earlier small-cardinality proofs are therefore instances of one reusable rule:

> if the target zero geometry forces two independent exact integer-character relations, multiplicative independence of the rational primes excludes the hit.

This rule is stronger and cleaner than treating each polygon symmetry separately, but its scope has a precise boundary at the pentagon.

## Why the pentagon is the first compatible zero geometry

AF-308 identifies the normalized five-phase zero locus

\[
M_5
=
\left\{
(z_1,z_2,z_3,z_4)\in(S^1)^4:
1+z_1+z_2+z_3+z_4=0
\right\}.
\tag{21}
\]

Classical equilateral-polygon theory identifies `M_5` with the moduli space of labelled oriented equilateral pentagons after fixing the final edge direction. Klaus and Kojima recall the stronger topological fact that it is a connected closed surface of genus four.

For independent `a,b in Z^4`, define

\[
H_{a,b}
=
\{z\in(S^1)^4:z^a=z^b=1\}.
\tag{22}
\]

The locus of points in `M_5` with relation rank at least two is exactly

\[
R_{\ge2}
=
\bigcup_{\substack{a,b\in\mathbb Z^4\\a,b\ \mathrm{independent}}}
(M_5\cap H_{a,b}).
\tag{23}
\]

This is a countable union. Each intersection in (23) has empty interior in `M_5`.

To see this, suppose `M_5\cap H_{a,b}` contained a nonempty open subset of `M_5`. The character equations `z^a=1` and `z^b=1` restrict to real-analytic equations on the connected real-analytic surface `M_5`. The real-analytic identity principle would then force both equations on all of `M_5`, so

\[
M_5\subseteq H_{a,b}.
\tag{24}
\]

The common kernel of two independent torus characters has dimension at most two and finitely many connected components, each a translate of a torus of dimension at most two. Since `M_5` is connected, (24) would put it in one component.

A component of dimension below two cannot contain the embedded two-manifold `M_5`. If the component has dimension two, the inclusion of the compact connected surface `M_5` into that two-torus is a continuous injective map between two-manifolds. By invariance of domain its image is open; compactness makes it closed. The connected target component would therefore equal the image, making `M_5` homeomorphic to a two-torus. That contradicts its genus four.

Thus every set in the countable union (23) is closed with empty interior. By the Baire category theorem,

\[
\boxed{
M_5\setminus R_{\ge2}
\text{ is dense and residual in }M_5.
}
\tag{25}
\]

Every point of the residual set (25) has relation rank at most one, exactly the relation-rank range allowed by the prime-log theorem (3).

This does **not** prove that a rational-prime orbit hits `M_5`. It proves something strategically different: the mechanism that killed `k=3,4` no longer conflicts with a generic pentagon closure configuration. The arithmetic incidence question has crossed from an integer-relation obstruction into a finer exact-placement problem.

## Prior art and novelty assessment

No novelty is claimed for the character-lattice, polygon-space, topology, or roots-of-unity ingredients.

- Sidney A. Morris, *Pontryagin Duality and the Structure of Locally Compact Abelian Groups*, London Mathematical Society Lecture Note Series 29, Cambridge University Press (1977), DOI `10.1017/CBO9780511600722`, is standard background for compact-torus characters, annihilators, and subgroup/quotient duality. AF-005 already uses this language to audit monomial phase lifts.
- Mateusz Michałek and Bernd Sturmfels, *Invitation to Nonlinear Algebra*, Graduate Studies in Mathematics 211, AMS (2021), Chapter 8, gives the standard integer character-lattice description of algebraic tori and monomial maps.
- Stephan Klaus and Sadayoshi Kojima, “On the moduli space of equilateral plane pentagons,” *Beiträge zur Algebra und Geometrie* 60 (2019), 487–497, DOI `10.1007/s13366-018-0429-z`, gives two proofs that the equilateral pentagon moduli space is a closed genus-four surface and an algebraic model of that surface.
- T. Y. Lam and K. H. Leung, “On Vanishing Sums of Roots of Unity,” *Journal of Algebra* 224(1) (2000), 91–109, DOI `10.1006/jabr.1999.8089`, is classical prior art for exact torsion-phase cancellation. Ben Barber, “Small sums of five roots of unity,” *Bulletin of the London Mathematical Society* 55 (2023), 1890–1906, DOI `10.1112/blms.12826`, studies quantitative near-cancellation for five torsion phases. Those results concern the torsion comparison regime; (5) shows that a normalized distinct-prime common-time phase point cannot itself enter codimension-two torsion geometry.

The cyclicity proof is an elementary consequence of unique factorization and the character lattice. The Baire-category pentagon argument combines that arithmetic constraint with the classical topology of `M_5`. The durable Arithmetic Fidelity contribution is the exact **boundary of the proof mechanism**: multiplicative independence completely excludes the forced relation geometry at `k=3,4`, but it is already compatible with a residual set of the first unresolved zero manifold at `k=5`.

## Boundaries and failure modes

- The cyclic relation-lattice theorem uses distinct rational primes only through rational independence of their logarithmic ratios. It extends verbatim to any positive multiplicatively independent generators with the same exact log-independence property.
- Relation rank at most one does not imply an exact zero exists. Equation (25) is a compatibility statement about the target polygon geometry, not an incidence theorem for the prime-log orbit.
- The residual set in (25) is topological, not arithmetic. It supplies no positive measure, Diophantine approximation rate, or explicit prime-support example.
- Rank-one character relations are genuinely possible for prime phases because the time can be chosen to force one such relation. Therefore strengthening (3) to rank zero is false without an additional restriction on `t`.
- The torsion-coset corollary excludes codimension at least two. A codimension-one torsion character constraint is compatible with the prime orbit and cannot be discarded by unique factorization alone.
- Root-of-unity classifications do not decide the `k=5` prime problem. They live in a phase class that the prime orbit is forbidden to occupy exactly, even though torsion configurations may remain useful as near-zero controls.
- The Baire proof uses the connected genus-four topology of the normalized pentagon space. It is not asserted here that the same topological argument automatically gives the optimal relation-rank statement for every `k>5` polygon space.
- Nothing here decides whether `sum_j p_j^{-it}=0` has a solution for five or more distinct primes. In particular, no transcendence theorem strong enough to decide that exact incidence is being assumed.
- Nothing here supplies a zeta zero count, analytic continuation, a Riemann-zero divisor, or an RH implication.

## Consequence for the research line

AF-308–AF-309 showed that exact saturated zeros form a dense measure-zero ambient frequency-incidence set, so topology, generic measure, and near-zero numerics cannot decide the prime point. AF-310 now identifies exactly how much of the special arithmetic structure is captured by elementary character relations.

The prime phase tuple can satisfy **at most one** independent monomial relation. That single theorem subsumes the small-cardinality `k=3,4` exclusions and rules out every codimension-two torsion explanation. But the normalized pentagon zero space has a dense residual subset obeying the same rank bound. Therefore the first unresolved cardinality is also the first one at which unique factorization plus polygon symmetry no longer creates a contradiction.

The next useful attack on `k=5` must consequently use information finer than the integer relation lattice: for example a genuinely analytic/transcendence restriction on the special logarithmic ray, an arithmetic restriction on its intersection with the nontorsion part of `M_5`, or a different observation whose exact failure set carries stronger arithmetic rigidity. Re-running Kronecker–Weyl, extracting torsion approximants, or searching for two forced monomial relations cannot bridge the remaining gap.