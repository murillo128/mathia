# PL-238 — Log-energy continuity annihilates scalar projective curvature on the prime group completion

## Claim

The source-forced twist escape left open by `PL-036` and narrowed again by `PL-237` has a sharp one-dimensional obstruction. Let

\[
G=\mathbb Z^{(\mathcal P)}\cong \mathbb Q_{>0}^{\times}
\]

be the group completion of the prime-exponent monoid and let

\[
L:G\to\mathbb R,\qquad
L(\alpha)=\sum_p \alpha_p\log p=\log n(\alpha).
\]

Because positive rationals are dense in `R_{>0}`, `L` identifies `G` with the dense additive subgroup

\[
\Lambda=\log \mathbb Q_{>0}\subset\mathbb R.
\]

Let `omega` be any scalar multiplier / normalized projective `2`-cocycle on `G`, and let

\[
c_\omega(\alpha,\beta)
:=\frac{\omega(\alpha,\beta)}{\omega(\beta,\alpha)}
\]

be its gauge-invariant commutator bicharacter. Suppose that, after transporting by `L`, the map

\[
(x,y)\longmapsto c_\omega(L^{-1}x,L^{-1}y)
\]

is jointly continuous on `Lambda x Lambda` for the ordinary topology inherited from the real line. Then

\[
\boxed{c_\omega\equiv1.}
\]

Hence the multiplier has no nontrivial scalar projective curvature. By the classical multiplier theory of abelian groups, a multiplier with trivial commutator bicharacter represents the trivial cohomology class, so `omega` is an abstract scalar coboundary. In the important special case in which the multiplier itself is a jointly log-continuous bicharacter, there is an explicit continuous gauge: every such bicharacter has the form

\[
\boxed{b(x,y)=e^{i\kappa xy}}
\]

for some real `kappa`, and therefore

\[
b(x,y)=q(x)q(y)q(x+y)^{-1},
\qquad
q(x)=e^{-i\kappa x^2/2}.
\]

So the canonical one-dimensional energy geometry `log n` cannot by itself source a noncommutative scalar twist once the prime lattice is completed continuously in the ratio/logarithmic topology. A surviving twisted-tensor/projective route must either be discontinuous in that topology or use additional arithmetic structure that does not factor through the single real coordinate `log n`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM` for the route

\[
\text{prime group completion}
+\text{ scalar projective cocycle}
+\text{ continuity in the canonical }\log\text{-energy topology}
\longrightarrow
\text{ nontrivial arithmetic curvature / RH rigidity}.
\]

The classification of multipliers on abelian groups and the fact that symmetric multipliers are coboundaries are classical. Chernoff and Kleppner also studied extension/triviality of regular multipliers on real and locally compact abelian semigroups. The dense-logarithm specialization below is an elementary exact deduction recorded only as a research-line obstruction; no novelty is claimed.

## 1. The group-completed prime lattice is a dense one-dimensional energy subgroup

Unique factorization identifies

\[
G=\mathbb Z^{(\mathcal P)}
\]

with the multiplicative group of positive rationals through

\[
\alpha\mapsto n(\alpha)=\prod_p p^{\alpha_p}.
\]

The logarithmic energy map is injective, because

\[
L(\alpha)=0
\Longleftrightarrow
n(\alpha)=1
\Longleftrightarrow
\alpha=0.
\]

It is also additive. Since `Q_{>0}` is dense in `R_{>0}` and logarithm is a homeomorphism from `R_{>0}` to `R`, its image

\[
\Lambda=L(G)=\log\mathbb Q_{>0}
\]

is dense in `R`.

This topology is additional structure absent from the bare free abelian group. It is precisely the topology obtained when ratios are admitted and the canonical energy `log n` is treated as a real coordinate rather than merely as a list of independent prime weights.

## 2. Continuous bicharacters on a dense subgroup of the real line are symmetric

Let `Lambda` be any dense additive subgroup of `R` and let

\[
b:\Lambda\times\Lambda\to\mathbb T
\]

be a jointly continuous bicharacter. For fixed `y`, the map

\[
x\mapsto b(x,y)
\]

is a continuous character of `Lambda`. Every continuous homomorphism between topological groups is uniformly continuous for their natural uniformities; because `T` is complete, this character extends uniquely from the dense subgroup `Lambda` to a continuous character of `R`. Thus there is a unique real number `a(y)` such that

\[
b(x,y)=e^{i a(y)x}
\qquad(x\in\Lambda).
\]

Bicharacter multiplicativity in the second variable gives

\[
e^{i a(y+z)x}
=e^{i(a(y)+a(z))x}
\qquad(x\in\Lambda).
\]

Density of `Lambda` forces

\[
a(y+z)=a(y)+a(z).
\]

It remains to exclude discontinuous additive `a`. Joint continuity of `b` at `(0,0)` does exactly that. If `a` were not locally bounded at `0`, there would be `y_j->0` in `Lambda` with `|a(y_j)|->infinity`. By density choose `x_j in Lambda` with

\[
\left|x_j-\frac{\pi}{a(y_j)}\right|
<\frac{1}{|a(y_j)|^2}.
\]

Then `x_j->0` but

\[
a(y_j)x_j\to\pi,
\qquad
b(x_j,y_j)\to-1,
\]

contradicting joint continuity, which requires `b(x_j,y_j)->b(0,0)=1`.

Therefore the additive map `a:Lambda->R` is locally bounded, hence continuous. It extends to a continuous additive map on `R`, so for some real constant `kappa`,

\[
a(y)=\kappa y.
\]

Consequently

\[
\boxed{b(x,y)=e^{i\kappa xy}.}
\]

In particular every jointly log-continuous bicharacter is symmetric.

The same conclusion holds if the subgroup of `R` is discrete: every discrete subgroup of `R` is cyclic, and a bicharacter on a cyclic group is automatically symmetric. Thus the absence of continuous alternating bicharacters is a one-dimensional phenomenon, not a special property of the rational primes.

## 3. The projective commutator must vanish

For a scalar multiplier `omega` on an abelian group, classical multiplier theory gives the gauge-invariant commutator

\[
c_\omega(x,y)=\omega(x,y)\omega(y,x)^{-1}.
\]

It is an alternating bicharacter:

\[
c_\omega(x+y,z)=c_\omega(x,z)c_\omega(y,z),
\]

\[
c_\omega(x,y+z)=c_\omega(x,y)c_\omega(x,z),
\]

and

\[
c_\omega(x,x)=1.
\]

Assume this bicharacter is jointly continuous after transporting `G` to `Lambda=log Q_{>0}`. Section 2 gives

\[
c_\omega(x,y)=e^{i\kappa xy}.
\]

Alternation now forces

\[
e^{i\kappa x^2}=1
\qquad\text{for every }x\in\Lambda.
\]

Because `Lambda` contains arbitrarily small nonzero elements, this is possible only for `kappa=0`. Hence

\[
\boxed{c_\omega(x,y)=1\quad\text{for all }x,y.}
\]

Equivalently, every prime-square projective commutator is trivial:

\[
V_pV_q=V_qV_p
\]

up to the scalar gauge used to represent the multiplier. Kleppner's classical classification of multipliers on abelian groups identifies cohomology classes by their alternating commutator bicharacters; since the commutator is trivial, the abstract multiplier class is trivial.

For a bicharacter multiplier the gauge can be written explicitly. If

\[
b(x,y)=e^{i\kappa xy},
\qquad
q(x)=e^{-i\kappa x^2/2},
\]

then

\[
q(x)q(y)q(x+y)^{-1}=e^{i\kappa xy}=b(x,y).
\]

This gauge is itself continuous in the log-energy topology.

## 4. Why this is a real restriction beyond PL-036

`PL-036` showed that the bare exponent monoid admits arbitrary independent pairwise projective phases. That flexibility remains true. On the positive cone,

\[
L(\mathbb N_0^{(\mathcal P)})=\{\log n:n\ge1\}
\]

is a discrete subset of `R`; merely saying that a cocycle is continuous there imposes no useful restriction. The positive-cone cocycle also extends algebraically to the group completion by Ore-semigroup multiplier theory, but the extension need not be continuous in the real logarithmic topology.

The present obstruction starts only when a proposal makes the stronger and mathematically meaningful demand that the projective curvature respect the **continuous ratio geometry** generated by

\[
\log(m/n)=L(v(m)-v(n)).
\]

That requirement kills the arbitrary alternating phase matrix: a one-dimensional real completion has no continuous alternating `2`-form.

This directly narrows the escape left by `PL-237`. That finding showed that abstract order/spreadability is too coarse and noted that genuinely twisted tensor products can evade the spreadability-implies-exchangeability theorem. The present calculation shows that such a twist cannot be sourced merely by making the scalar projective phase continuous in the canonical `log p` geometry. The log-energy coordinate is too low-dimensional to carry scalar projective curvature.

## 5. Prior-art and falsification audit

The group-cohomological part is classical. Adam Kleppner's *Multipliers on Abelian Groups* identifies multiplier classes on abelian groups through bicharacter/commutator data; this is already the main cohomological prior art used in `PL-036`.

Close semigroup prior art is even more explicit:

- P. R. Chernoff, “Extensions and triviality of multipliers on sub-semigroups of the reals,” *Semigroup Forum* **41**(2) (1990), 237–244. The paper studies extension/triviality questions for regular multipliers on additive real subsemigroups.
- Adam Kleppner, “Multipliers on subsemigroups of locally compact abelian groups,” *Semigroup Forum* **47**(1) (1993), 81–86. It places symmetric multipliers and extension questions for abelian subsemigroups in the established harmonic-analysis framework.
- Adam Kleppner, “Multipliers on Abelian Groups,” *Mathematische Annalen* **158** (1965), 11–34. DOI: https://doi.org/10.1007/BF01370393.

A targeted search did not find the exact specialization to `log Q_{>0}` presented as a prime-exponent-lattice obstruction, but the underlying mathematics is elementary harmonic analysis and multiplier theory. This finding therefore records a **prior-art-controlled redirect**, not a new multiplier theorem.

The matched generalized-prime control is immediate. Whenever a multiplicative system is encoded by an injective additive energy map into a subgroup of the real line, the same continuous-commutator argument applies. Thus this no-go does not distinguish rational primes from Beurling systems; it instead identifies the missing ingredient: one real energy coordinate cannot support nontrivial continuous scalar projective curvature.

## 6. What survives

This result does **not** rule out every source-forced noncommutative relation. It leaves several genuinely different possibilities:

- a cocycle or commutator that is discontinuous in the real log topology because it uses local arithmetic data, as Hilbert symbols do in `PL-038`;
- a relation depending on at least one additional independent arithmetic coordinate rather than factoring through `log n` alone;
- an operator-valued cocycle whose invariant is not a scalar alternating bicharacter;
- a nonlocal pair relation on rational primes that is constrained by a theorem stronger than continuity in their one-dimensional norm coordinate;
- a target-relative construction in which the relevant invariant is not projective commutation of the prime shifts.

These escapes still face the existing controls: arbitrary extra labels are programmable, scalar local-global Hilbert-symbol products trivialize by reciprocity (`PL-038`), and spherical operator-valued scattering scalarizes in the Riemann-zeta channel (`PL-039`).

The useful design constraint is therefore sharper than “use the actual `log p` values.” A future twist must exhibit a source-forced invariant that **does not factor continuously through the single homomorphism**

\[
L:\mathbb Z^{(\mathcal P)}\to\mathbb R.
\]

Otherwise its scalar projective curvature is forced to vanish before any zeta-zero or critical-line question is reached.

## Consequence for the research line

The current frontier can be narrowed from

\[
\text{actual prime labels / log-energy geometry}
+\text{ twisted completion}
\]

to the more discriminating requirement

\[
\boxed{
\text{additional source-forced arithmetic relation not continuously reducible to }\log n.
}
\]

This is a decisive negative only for scalar projective curvature compatible with the one-dimensional log-energy completion. It makes no claim about arbitrary discontinuous arithmetic cocycles, operator-valued curvature, or target-sensitive noncommutative structures, and it supplies no analytic continuation or RH criterion by itself.
