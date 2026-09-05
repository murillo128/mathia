# WP-160 — Toric Manin–Mumford closes fixed algebraic torsion incidence

**Status:** `LITERATURE+DERIVED + DECISIVE-NARROWING + PRIME-CIRCLE + ALGEBRAIC-TORUS + TORIC-MANIN-MUMFORD + TORSION-COSET-CLASSICALIZATION + FIXED-LAURENT-NO-GO + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION` for fixed finite-arity algebraic incidence among root-of-unity coordinates.

`WP-158` shows that fixed torus-character and torsion-coset correspondences split over prime-primary shells. `WP-159` then tests the first genuinely additive relation left outside that class: `x+y=1` has only the sixth-root pair, while its homogeneous version `x+y=z` has only a fixed equilateral relative geometry.

The natural next question is whether a more complicated **fixed Laurent-polynomial relation** could evade both failures: perhaps four or more terms, several equations, or a nonlinear algebraic incidence could have an infinite torsion locus whose geometry genuinely correlates arbitrary prime-primary shells before any determinant or positivity operation is applied.

In characteristic zero, Laurent's toric Manin–Mumford theorem rules out that mechanism at the correct level of generality. For a fixed algebraic subvariety of a finite-dimensional torus, the Zariski closure of all torsion points is a finite union of torsion cosets. Those cosets are exactly translated character geometry. Combining that theorem with `WP-158` gives a dichotomy:

\[
\boxed{
\text{fixed algebraic torsion incidence}
\;\Longrightarrow\;
\begin{cases}
\text{only finitely many exceptional torsion configurations},\\
\text{or scalable torsion contained in finitely many translated subtori.}
\end{cases}}
\]

The second case supplies no irreducible mixed-prime incidence on products of distinct prime-primary shells, because translated subtori are cut out by translated character equations and those factor prime by prime. Hence a fixed finite-arity Laurent-polynomial template cannot be the missing source of scalable mixed-prime geometry required before Weil positivity is formed.

This result does **not** exclude algebraic families whose equations themselves vary with a source-forced global parameter, growing-arity constructions, nonalgebraic analytic/metric/differential incidence, or a genuine finite--archimedean relation. Those now become the relevant escape classes.

## 1. Fixed algebraic incidence in the torsion torus

Let

\[
\mathbf G_m^r=(\mathbf C^\times)^r
\]

and let

\[
V\subset \mathbf G_m^r
\tag{1}
\]

be a fixed algebraic subvariety defined by finitely many Laurent polynomials with coefficients in a characteristic-zero field. The word **fixed** is essential: the equations, coefficients, and arity are chosen independently of the prime labels or cutoff later used to test the construction.

The torsion subgroup is

\[
(\mathbf G_m^r)_{\mathrm{tors}}=\mu_\infty^r,
\tag{2}
\]

so its points are exactly tuples of roots of unity. Put

\[
V_{\mathrm{tors}}
=
V\cap \mu_\infty^r.
\tag{3}
\]

A torsion coset is a set

\[
\zeta T,
\tag{4}
\]

where `T` is an algebraic subtorus of `\mathbf G_m^r` and `\zeta` is a torsion point.

## 2. Laurent's theorem turns every scalable torsion locus into torsion cosets

The toric Manin–Mumford theorem proved by Michel Laurent says that there exist finitely many torsion cosets

\[
C_1,\ldots,C_J\subset V
\tag{5}
\]

such that

\[
\boxed{
\overline{V_{\mathrm{tors}}}^{\,\mathrm{Zar}}
=
\bigcup_{j=1}^J C_j.
}
\tag{6}
\]

Equivalently, solutions of a fixed finite system of algebraic equations in roots of unity occur in finitely many torsion-coset families, with isolated torsion solutions appearing as zero-dimensional cosets.

Two immediate consequences matter here.

First, if `V_{tors}` is infinite, then at least one `C_j` in (6) has positive dimension. Thus an algebraic relation can support an unbounded torsion family only through a positive-dimensional translated subtorus already contained in `V`.

Second, if `V` contains no positive-dimensional torsion coset, then

\[
\boxed{|V_{\mathrm{tors}}|<\infty.}
\tag{7}
\]

So there is no third possibility in which a fixed algebraic relation has infinitely many sporadic torsion points of ever-new orders while avoiding all torus-coset structure.

This is substantially stronger than checking higher-term root-of-unity equations one at a time.

## 3. Every positive-dimensional escape is translated character geometry

An algebraic subtorus `T\subset \mathbf G_m^r` is determined by a saturated lattice of characters. Concretely, there exist integer vectors

\[
u^{(1)},\ldots,u^{(s)}\in\mathbf Z^r
\tag{8}
\]

such that `T` is the common kernel of the corresponding monomial characters

\[
\chi_{u^{(j)}}(x)
=
\prod_{i=1}^r x_i^{u_i^{(j)}}.
\tag{9}
\]

After translating by a torsion point, the coset `C=\zeta T` is therefore described by finitely many equations

\[
\boxed{
\chi_{u^{(j)}}(x)=\eta_j,
\qquad
\eta_j\in\mu_\infty.
}
\tag{10}
\]

Thus Laurent's theorem does not merely say that the torsion locus is structured. It says that every **infinite** torsion family inside a fixed algebraic incidence eventually lives in exactly the category already audited in `WP-158`: finite systems of translated torus-character equations.

A complicated Laurent polynomial can therefore create finite exceptional torsion configurations, but any scalable torsion component is forced back into monomial/character geometry.

## 4. Prime-primary restriction then separates coordinate by coordinate

Now test one torsion coset (10) on a product of primitive prime-primary shells

\[
X_P
=
\prod_{i=1}^r
\mu_{p_i^{a_i}}^{\mathrm{prim}},
\qquad
p_i\neq p_j\ \text{for }i\neq j.
\tag{11}
\]

Take one equation from (10):

\[
\prod_i x_i^{u_i}=\eta.
\tag{12}
\]

Write the unique primary decomposition of the fixed torsion constant as

\[
\eta=\prod_\ell \eta_\ell,
\tag{13}
\]

where `\eta_\ell` has `\ell`-power order. Since each `x_i^{u_i}` has `p_i`-power order and the primes in (11) are distinct, equality (12) is equivalent to the independent one-coordinate conditions

\[
\boxed{
x_i^{u_i}=\eta_{p_i}
\quad\text{for every }i,
}
\tag{14}
\]

plus `\eta_\ell=1` for primes outside `P`.

Applying this to every equation defining the coset gives

\[
\boxed{
C\cap X_P
=
\prod_{i=1}^r Y_i
}
\tag{15}
\]

for suitable one-prime subsets

\[
Y_i\subset\mu_{p_i^{a_i}}^{\mathrm{prim}}.
\tag{16}
\]

This is precisely the primary-decomposition mechanism proved directly in `WP-158`. The point of the present finding is that Laurent's theorem forces every scalable torsion component of **any fixed algebraic incidence** back into that class.

Therefore the scalable part of `V_{tors}` has no irreducible cross-prime incidence on (11). It can delete or retain points separately in each prime coordinate, but it cannot make the allowed choice at prime `p_i` depend genuinely on the choice at a different prime `p_j`.

## 5. Fixed character data become even more rigid under unbounded shell variation

The separation in (15) already kills the desired mixed interaction. Fixedness gives an additional useful boundary.

Suppose a coordinate shell varies through arbitrarily large prime powers `p^a` while the character exponent `u_i` in (12) remains fixed. When the corresponding primary component of `\eta` is trivial, a primitive point satisfies

\[
x_i^{u_i}=1
\quad\Longleftrightarrow\quad
p^a\mid u_i.
\tag{17}
\]

A fixed nonzero integer `u_i` is divisible by only finitely many prime powers. Hence a nontrivial fixed character constraint cannot keep acting on an unbounded family of new prime-primary shells. To survive such variation indefinitely it must eventually become trivial in that varying coordinate, or the intersection becomes empty.

Likewise, the fixed torsion constants `\eta_j` involve only finitely many rational primes. They cannot supply new right-hand-side primary components for arbitrarily many prime labels.

So a fixed torsion coset is not merely separable. On genuinely unbounded prime-shell variation, any coordinate whose prime/order keeps changing cannot carry a persistent nontrivial fixed character constraint.

## 6. `WP-159` is the smallest exact sanity check of the theorem

The two additive examples in `WP-159` fit the general theorem exactly.

For the affine curve

\[
V=\{(x,y)\in\mathbf G_m^2:x+y=1\},
\tag{18}
\]

`WP-159` computes the complete torsion locus directly:

\[
(x,y)=(\zeta_6,\zeta_6^{-1})
\quad\text{or}\quad
(\zeta_6^{-1},\zeta_6).
\tag{19}
\]

The curve contains no positive-dimensional torsion coset, so Laurent's theorem predicts that its torsion locus is finite; (19) is the explicit finite exceptional set.

For the homogeneous relation

\[
x+y=z,
\tag{20}
\]

`WP-159` finds the infinite family

\[
(x,y,z)
=
(t\zeta_6,t\zeta_6^{-1},t),
\qquad
t\in\mu_\infty.
\tag{21}
\]

But (21) is itself exactly one torsion coset: the torsion translate

\[
(\zeta_6,\zeta_6^{-1},1)
\cdot
\{(t,t,t):t\in\mathbf G_m\}
\tag{22}
\]

of the diagonal one-dimensional subtorus. Its apparently additive infinite family therefore classicalizes to translated-character geometry, and its relative configuration remains the same fixed equilateral triangle. This is the concrete prototype of (6)--(15).

The isolated prime-primary `(3,3,2)` order pattern found in `WP-159` is then an exceptional shell intersection of this fixed coset, not an unbounded source of mixed-prime geometry.

## 7. Consequence for fixed higher-arity Laurent-polynomial proposals

Consider any proposed fixed finite-arity source relation

\[
F_1(x_1,\ldots,x_r)=\cdots=F_m(x_1,\ldots,x_r)=0
\tag{23}
\]

with Laurent polynomials `F_j` chosen independently of the prime labels and desired Weil coefficients.

If (23) has only finitely many torsion points, it cannot encode the required family of finite-prime contributions across arbitrarily many prime powers.

If it has infinitely many torsion points, Laurent's theorem puts the scalable part into finitely many torsion cosets, and `WP-158` then separates those cosets prime by prime on distinct primary shells.

Hence

\[
\boxed{
\begin{aligned}
&\text{fixed finite-arity algebraic/Laurent incidence}\\
&\qquad\not\Longrightarrow
\text{scalable irreducible mixed-prime torsion geometry}.
\end{aligned}}
\tag{24}
\]

This closes the broad fixed-algebraic continuation left open in `WP-159`. In particular, merely moving from three-term addition to a more elaborate fixed polynomial in roots of unity is no longer a distinct escape strategy unless the construction leaves the hypotheses of the toric Manin--Mumford reduction.

## 8. Matched controls and what the result does not say

The obstruction is deliberately upstream of positivity. It uses no zeta zeros, no Weil functional, no regularization, and no sign assumption. It is a classification of the information carrier available from fixed algebraic incidence on torsion coordinates.

It is also not arithmetic selection. Laurent's theorem applies to every characteristic-zero algebraic subvariety of a torus, and the prime-primary factorization in (14) is simply uniqueness of primary decomposition in finite abelian torsion. Replacing arithmetic labels by any matched pairwise-coprime cyclic shell system leaves the mechanism unchanged.

Several escape classes remain genuinely outside the claim:

- **growing-arity or varying algebraic families:** a sequence `V_R` whose equations or dimension change with the global cutoff is not one fixed `V`; such dependence must itself be source-forced rather than chosen to encode the desired prime pattern;
- **source-forced non-torsion parameters:** an algebraic family depending on a canonical real/global parameter may require a relative or unlikely-intersection analysis rather than fixed-variety Laurent;
- **nonalgebraic incidence:** analytic, metric, differential, operator-domain, boundary-response, or other relations need not be zero loci of Laurent polynomials;
- **finite--archimedean coupling:** the real place can participate in the same relation before positivity, which is outside pure torus torsion geometry;
- **higher/cohomological data not determined by the point locus:** a correspondence or complex may carry information beyond the set of torsion solutions, but that extra structure must be exhibited and its mixed response derived independently.

The theorem also does not say that fixed algebraic incidence has no torsion points. It says that finite exceptions cannot scale and infinite families are forced into torsion-coset geometry. Those are different statements.

## 9. Prior art and novelty audit

No new Diophantine theorem is claimed.

Michel Laurent, *Équations diophantiennes exponentielles*, Inventiones Mathematicae **78** (1984), 299--327, proves the characteristic-zero toric Manin--Mumford/Lang theorem underlying (6). Modern formulations state that the Zariski closure of the torsion points on an algebraic subvariety of `\mathbf G_m^r` is a finite union of torsion cosets.

Iskander Aliev and Chris Smyth, *Solving algebraic equations in roots of unity*, arXiv:`0704.1747`, summarize the same theorem in the form most directly relevant here: solutions of polynomial equations in roots of unity are described by finitely many maximal torsion-coset families.

Gerold Schefer, *Counting torsion points on subvarieties of the algebraic torus*, Acta Arithmetica **218** (2025), 297--336, DOI `10.4064/aa221025-14-1`, explicitly uses Laurent's theorem in characteristic zero and records the decomposition

\[
\overline{X\cap(\mathbf G_m^n)_{\mathrm{tors}}}
=
\bigcup_i C_i
\tag{25}
\]

into torsion cosets before deriving torsion-counting asymptotics.

The Mathia-specific contribution is therefore not theorem novelty but **branch-local closure**. `WP-158` had proved that translated character geometry cannot create cross-prime incidence, while `WP-159` left general fixed additive/Laurent incidence open. Laurent's theorem shows that every scalable torsion component of exactly that broader algebraic class collapses back to the `WP-158` category. The combination removes an apparently much larger search space without importing any RH-equivalent positivity statement.

## 10. Research consequence

The source-ordering constraint is now sharper:

\[
\boxed{
\text{fixed algebraic root-of-unity incidence}
\xrightarrow{\text{Laurent}}
\text{finite torsion exceptions + torsion cosets}
\xrightarrow{\text{WP-158}}
\text{prime-primary separation}.
}
\tag{26}
\]

Therefore the missing mixed-prime structure cannot be obtained merely by choosing a cleverer fixed Laurent polynomial before taking a Gram form, determinant, Hodge completion, or positive operator. If it is algebraic, it must involve genuinely new global dependence not covered by a fixed finite-arity torsion subvariety; otherwise the route must change category to nonalgebraic, boundary/operator, finite--archimedean, or higher-cohomological structure.

A surviving proposal should now state explicitly **which hypothesis of this reduction it leaves** and why that escape is intrinsic to Mathia. Without that, higher-term algebraic torsion incidence is prior-art-classicalized rather than a new Weil-positivity mechanism.
