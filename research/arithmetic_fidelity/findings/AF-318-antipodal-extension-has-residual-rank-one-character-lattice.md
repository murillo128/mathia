# AF-318 — The eight-point middle-singular antipodal-extension family is generically rank one

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `CHARACTER-LATTICE`, `STRUCTURAL-OBSTRUCTION`, `BAIRE-GENERIC`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-317 constructs an exact three-real-dimensional source of centered eight-point unit-circle configurations with middle coefficient `e_4=0`: start from a nondegenerate marked equilateral hexagon

\[
B=(b_1,\ldots,b_6)\in(S^1)^6,
\qquad \sum_{j=1}^6 b_j=0,
\tag{1}
\]

with `e_2(B)\ne0`, set

\[
A(B)=\frac{e_4(B)}{e_2(B)}
     =E_B\frac{\overline{e_2(B)}}{e_2(B)}\in S^1,
\qquad E_B=\prod_{j=1}^6 b_j,
\tag{2}
\]

choose `a\in S^1` with `a^2=A(B)`, and append the antipodal pair

\[
Z(B)=B\sqcup\{a,-a\}.
\tag{3}
\]

Then `Z(B)` is centered and `e_4(Z(B))=0`.

The deliberately inserted antipodal pair gives one unavoidable integer-character relation. The new point is that **generically it gives the only one**.

Let `D` be the open subset `e_2(B)\ne0` of the nondegenerate marked equilateral-hexagon moduli space, modulo common rotation. Normalize `Z(B)` by the appended phase `-a` and write

\[
u(B)=\left(-\frac{b_1}{a},\ldots,-\frac{b_6}{a},-1\right)\in(S^1)^7.
\tag{4}
\]

Its relation lattice is

\[
L_B=\left\{c\in\mathbb Z^7:\prod_{j=1}^7u_j(B)^{c_j}=1\right\}.
\tag{5}
\]

Then there is a dense residual subset `D_*\subset D` such that

\[
\boxed{L_B=2\mathbb Z e_7\quad\text{for every }B\in D_*.}
\tag{6}
\]

In particular,

\[
\boxed{\operatorname{rank}_{\mathbb Z}L_B=1}
\tag{7}
\]

on a dense residual subset of this exact middle-singular family.

Thus the universal alternative suggested after AF-317 is false: the centered eight-point singular fiber `e_4=0` does **not** force a second independent integer-character relation. The strongest elementary rational-prime restriction from AF-310, namely relation rank at most one, is already compatible with a residual set inside an explicit exact singular subfamily.

This does not prove that any common-time rational-prime orbit meets that subfamily. It proves that character-lattice rank alone cannot exclude the first unresolved even-support recovery singularity.

## 1. The antipodal-extension family is an exact singular family

For a centered six-point unit configuration `B`, self-inversivity gives

\[
e_4(B)=E_B\overline{e_2(B)}.
\tag{8}
\]

Appending `{a,-a}` multiplies the root polynomial by `w^2-a^2`, so AF-317 gives

\[
e_4(Z)=e_4(B)-a^2e_2(B).
\tag{9}
\]

On `D`, equation `(2)` therefore makes `(9)` vanish exactly. The choice of square root does not create two different unordered eight-point configurations: replacing `a` by `-a` merely swaps the two appended phases.

The moduli space used here is the standard marked equilateral-hexagon space modulo orientation-preserving Euclidean congruence. Edge directions identify a hexagon with a centered ordered sextuple `(1)`, modulo common rotation. Classical work on this space identifies its nondegenerate part as a finite-volume hyperbolic three-manifold; in particular it is a Baire real-analytic manifold. The subset `D` is nonempty and open.

## 2. Every extra relation forces a branch-independent analytic equation

Take

\[
c=(c_1,\ldots,c_6,c_7)\in L_B
\]

and put

\[
d=(c_1,\ldots,c_6),
\qquad
S=\sum_{j=1}^6c_j,
\qquad
M_d(B)=\prod_{j=1}^6b_j^{c_j}.
\tag{10}
\]

Using `(4)`, the character equation contains only a sign, `M_d(B)`, and `a^{-S}`. Squaring removes both the normalization sign and the choice of square root. Since `a^2=A(B)`, every relation with first-six part `d` satisfies

\[
\boxed{
\Phi_d(B):=A(B)^{-S}M_d(B)^2=1.
}
\tag{11}
\]

The expression is invariant under common rotation of `B`: `M_d^2` and `A^S` both acquire the factor `\rho^{2S}`. Hence `(11)` is well-defined on hexagon moduli.

If `d=0`, the unsquared relation reduces to `(-1)^{c_7}=1`, so `c_7` is even. These are exactly the multiples of `2e_7`. Therefore an independent second relation can exist only if `(11)` holds for some nonzero `d\in\mathbb Z^6`.

For fixed nonzero `d`, let

\[
R_d=\{B\in D:\Phi_d(B)=1\}.
\tag{12}
\]

It is closed in `D`. We next show that it has empty interior.

## 3. No nontrivial character equation can hold on an open set

Assume for contradiction that `R_d` contains a nonempty open subset of `D`. Equation `(11)` can be cleared of its `e_2/e_4` denominator to give a real-analytic identity on the full connected nondegenerate hexagon moduli space.

If `S\ge0`, the cleared identity is

\[
M_d(B)^2e_2(B)^S-e_4(B)^S=0.
\tag{13}
\]

If `S=-r<0`, it is

\[
M_d(B)^2e_4(B)^r-e_2(B)^r=0.
\tag{14}
\]

The real-analytic identity principle therefore makes the corresponding equation hold on the entire nondegenerate moduli space.

Now choose any perfect matching of the six labels and restrict to the nondegenerate three-antipodal-pair family. For one matching write

\[
B=(u,-u,v,-v,w,-w),
\qquad U=u^2,\ V=v^2,\ W=w^2.
\tag{15}
\]

Its root polynomial is

\[
(x^2-U)(x^2-V)(x^2-W),
\]

so

\[
e_2=-(U+V+W),
\qquad
e_4=UV+UW+VW,
\tag{16}
\]

and

\[
M_d(B)^2=U^\alpha V^\beta W^\gamma,
\tag{17}
\]

where `\alpha,\beta,\gamma` are the sums of the two `d`-coefficients in the three matched pairs. On the open set where the denominators are nonzero, `(11)` becomes

\[
U^\alpha V^\beta W^\gamma
=
\left(-\frac{UV+UW+VW}{U+V+W}\right)^S.
\tag{18}
\]

Because this holds on an open subset of the three-torus, Fourier/analytic uniqueness makes it an identity of Laurent rational functions.

If `S\ne0`, `(18)` is impossible. The left side is a Laurent monomial, whose divisor is supported only on coordinate hyperplanes. The right side has the non-coordinate factors `U+V+W` and `UV+UW+VW`; they are nonassociate and neither is a coordinate monomial. Hence the two sides cannot agree for nonzero `S`.

Therefore `S=0`. Equation `(18)` then reduces to

\[
U^\alpha V^\beta W^\gamma=1,
\tag{19}
\]

which forces

\[
\alpha=\beta=\gamma=0.
\tag{20}
\]

Thus, for the chosen perfect matching, the sum of the two `d`-coefficients in every matched pair is zero.

But the global analytic identity must also hold on the antipodal-pair family for **every** perfect matching of the six marked labels. Every pair of labels can occur as one pair in some perfect matching, so `(20)` would imply

\[
d_i+d_j=0
\qquad\text{for every }i\ne j.
\tag{21}
\]

Taking three distinct indices forces all `d_i=0`, contradicting the choice `d\ne0`.

Hence no `R_d` with `d\ne0` has interior in `D`.

## 4. Baire category leaves exactly the forced antipodal relation

There are countably many nonzero vectors `d\in\mathbb Z^6`. Each `R_d` is closed and nowhere dense in the Baire space `D`. Therefore

\[
D_*=D\setminus\bigcup_{d\in\mathbb Z^6\setminus\{0\}}R_d
\tag{22}
\]

is dense and residual.

For `B\in D_*`, any relation in `L_B` must have first-six part `d=0`; as observed above, this forces `c_7` even. Conversely `u_7=-1` gives `2e_7\in L_B`. This proves `(6)` and `(7)`.

The argument deliberately excludes more than necessary: `(11)` is only a necessary condition for an unsquared character relation, because squaring forgets one sign. Proving that the larger squared-relation loci are nowhere dense is therefore enough to eliminate all genuine extra relations generically.

## Arithmetic-fidelity consequence

AF-316 identifies `e_4=0` as the exact failure set of the generic eight-point low-harmonic recovery formula. AF-317 shows that this set is not confined to torsion or globally antipodal configurations. AF-318 now closes the remaining elementary character-rank escape: even inside AF-317's deliberately antipodal extension family, one forced relation is generically the **only** relation.

For a hypothetical eight-prime common-time zero, AF-310 permits relation rank at most one. Therefore no theorem using only

- centering,
- the middle singularity `e_4=0`, and
- the rank bound supplied by multiplicative independence of rational primes

can exclude the singular stratum: an exact ambient singular family already satisfies the same rank budget on a residual set.

What remains is source-specific incidence. To rule out `e_4=0` for rational-prime phases one needs arithmetic information finer than the integer-character rank captured by AF-310, or else the recovery representation must explicitly retain the missing product phase `E` on the singular stratum rather than hope that singularity is automatically source-impossible.

## Prior art and novelty assessment

No novelty is claimed for equilateral-hexagon moduli, torus characters, Baire category, real-analytic continuation, or the elementary symmetric-function identities.

- Yutaka Hirano, **“The moduli space of equilateral hexagons,”** *RIMS Kôkyûroku* 1660 (2009), 144–157, describes marked equilateral hexagons by their unit edge directions and identifies the nondegenerate moduli space with a finite-volume hyperbolic three-manifold with ten cusps.
- Sadayoshi Kojima, Haruko Nishi, and Yasushi Yamashita, **“Configuration spaces of points on the circle and hyperbolic Dehn fillings,”** *Topology* 38(3) (1999), 497–516, DOI `10.1016/S0040-9383(98)00022-6`, supplies the neighboring configuration-space/hyperbolic-manifold framework cited by Hirano.
- AF-005 and AF-310 already locate the integer-character/annihilator-lattice language in classical Pontryagin duality and algebraic-torus character theory; the present proof uses only that elementary character language.

A targeted search found these established moduli and character frameworks but not a standard theorem packaging the specific middle-singular antipodal-extension family into the residual rank-one statement `(6)`. That absence is not evidence of novelty, so none is claimed. The durable contribution here is the exact obstruction boundary relative to AF-310, AF-316, and AF-317.

## Boundaries and failure modes

- Residuality is proved **inside the antipodal-extension family parametrized by `D`**, not in the entire eight-point singular fiber `s_1=e_4=0`.
- Every member of this family has one explicit antipodal relation; the theorem says that additional integer-character relations disappear generically. It does not produce a rank-zero point.
- The result is about exact monomial relations, not Diophantine approximation, near-relations, or conditioning close to character subtori.
- The Baire statement is topological. It supplies no measure estimate, explicit algebraic rank-one witness, or quantitative distance from higher-rank relation strata.
- No common-time rational-prime orbit is shown to meet the family, the full singular fiber, or even the centered eight-point locus.
- Consequently no eight-prime exact zero, zeta zero, critical-line statement, or RH implication follows.
- The theorem kills a **source-independent rank-two exclusion**. A finer prime-log transcendence, incidence, approximation, or analytic argument may still rule out the same singular configurations for rational primes.
- The proof is specialized to the first unresolved even support. No claim is made that the same antipodal-extension/Baire argument automatically gives the optimal relation-rank statement for every larger even support.

## Consequence for the research line

The eight-point singular gate is no longer “does `e_4=0` force a second character relation?” It does not, even generically within a natural exact singular subfamily.

The post-incidence recovery picture is therefore sharper. Generic eight-point centered configurations are recovered from the low harmonics by AF-316. On the exceptional `e_4=0` stratum, elementary prime character rank cannot certify source impossibility. The remaining currencies are **actual prime-log incidence**, quantitative separation from the singular set, or retention of the missing product-phase lift. This prevents further work from repeatedly trying to upgrade the six-point antipodal accident into a universal even-support obstruction.